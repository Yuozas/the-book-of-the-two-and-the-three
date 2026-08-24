# -*- coding: utf-8 -*-
"""
Bind the Lithuanian edition: bible-lt/*.md -> book/the-2to3-bible-lt.{html,pdf}

    python3 book/build_lt.py

Requires: bible-lt/ fully translated (same filenames as bible/) and
book/figure-strings-lt.json (EN string -> LT string map for figure captions
and in-SVG labels). Reuses the English pipeline (build.py) by overriding its
module globals — paths, INJECT keys, and front matter.

Unlike the Russian edition, the display face is NOT swapped: every font this
book ships (Cinzel, EB Garamond, IBM Plex Mono) covers the full Lithuanian set
ĄČĘĖĮŠŲŪŽ, so the Lithuanian edition keeps the original English typography.
Cyrillic forced build_ru.py to fall back to Cormorant SC; Latin-with-ogoneks
does not.

Run `python3 book/check_translation.py bible-lt` before binding: this script
re-keys build.INJECT by matching '### ' headings positionally against the
English, so a heading-count mismatch silently drops figures out of the PDF.
"""
import json, re, pathlib
import figures
import build

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

# ------------------------------------------------------------------ paths
build.BIBLE = ROOT / "bible-lt"
build.OUT_HTML = HERE / "the-2to3-bible-lt.html"
build.OUT_PDF = HERE / "the-2to3-bible-lt.pdf"

# ------------------------------------------- figures: captions + labels
MAP = json.loads((HERE / "figure-strings-lt.json").read_text(encoding="utf-8"))
# Handles labels the SVG stores as numeric entities (&#8594; etc.); see
# build.localize_figures.
build.localize_figures(MAP)

# ---------------------------------- INJECT: re-key to Lithuanian headings
def h3s(path):
    return [m.group(1).strip() for m in
            re.finditer(r"^###\s+(.+)$", path.read_text(encoding="utf-8"), re.M)]

lt_of = {}
for fn in build.PARTS:
    en, lt = h3s(ROOT / "bible" / fn), h3s(ROOT / "bible-lt" / fn)
    if len(en) == len(lt):
        lt_of.update(dict(zip(en, lt)))
    else:
        print("WARNING: %s heading count mismatch (%d EN vs %d LT)"
              % (fn, len(en), len(lt)))
build.INJECT = {lt_of.get(k, k): v for k, v in build.INJECT.items()}

# ------------------------------------------------- typography
# Fonts are unchanged (see module docstring). Lithuanian sets long compounds,
# so soft hyphenation is allowed where the renderer has patterns for it.
build.CSS += "\np,li,blockquote{hyphens:auto;-webkit-hyphens:auto;}"

# ------------------------------------------- front matter, in Lithuanian
def cover_html_lt():
    sig = figures.FIGS["emblem"]["svg"]
    return ('<section class="sheet cover">'
            '<div class="sigil">%s</div>'
            '<h1 class="title">Dvejeto ir<br/>Trejeto knyga</h1>'
            '<div class="sub">Prakeiktos geometrijos šventraštis</div>'
            '<div class="rule"></div>'
            '<div class="motto">Dvejetas duoda judėjimą. Trejetas duoda pavidalą.'
            '<span class="last">2 &#8596; 3</span></div>'
            '<div class="scribe">užrašė Yuozas</div>'
            '</section>') % sig
build.cover_html = cover_html_lt

build.CREED_LINES = [
    "<b>Vienetas</b> yra Centras. Jo negalima padalyti, ir todėl jis yra "
    "vientisas.",
    "<b>Dvejetas</b> yra Santykis. Jis atveria plokštumą, o plokštumoje yra "
    "sukimasis, ir sukimasis yra judėjimas.",
    "<b>Trejetas</b> yra Pavidalas. Jis užveria trikampį, o užvertas trikampis "
    "stovi, ir stovėjimas yra pastovumas.",
    "<b>Spindulys</b> yra sandora: jis gali pasisukti bet kuria kryptimi, bet "
    "savo ilgio nekeis.",
    "<b>Sukimasis</b> yra tiltas. Jis neša apskritimą į sferą, o sferą — į "
    "kambarius, į kuriuos nebuvome sutverti įžengti.",
    "Šventa tai, kas lieka tas pats, kai visa kita keičiasi.",
]
def creed_html_lt():
    lines = ''.join('<div class="line">%s</div>' % l for l in build.CREED_LINES)
    return ('<section class="sheet creed">'
            '<div class="kicker">Tikėjimo išpažinimas</div>%s'
            '<div class="seal">2 &#8596; 3</div></section>') % lines
build.creed_html = creed_html_lt

def colophon_html_lt():
    return ('<section class="sheet colophon">'
            '<div class="kicker">Kolofonas</div>'
            '<div class="by">Šis kanono leidimas iškastas, surinktas ir '
            'užrašytas — </div>'
            '<div class="name">Yuozas</div>'
            '<div class="meta">kuris paklausė, kuo apskritimas skiriasi nuo '
            'sferos, — ir nesustojo.</div>'
            '<div class="meta">Įrišta 2026 metais. Knyga nebaigta ir pagal savo '
            'pačios doktriną baigta būti negali &mdash; <em>V.51</em>. '
            'Kas ją perskaitys kitas, taps kita jos iteracija.</div>'
            '<div class="seal">2 &#8596; 3</div>'
            '</section>')
build.colophon_html = colophon_html_lt

_orig_contents = build.contents_html
def contents_html_lt(toc):
    return _orig_contents(toc).replace('>Contents<', '>Turinys<')
build.contents_html = contents_html_lt

# ------------------------------------------------------------------ main
if __name__ == "__main__":
    build.build()
    html = build.OUT_HTML.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="lt">')
    html = html.replace('<title>The Book of the Two and the Three</title>',
                        '<title>Dvejeto ir Trejeto knyga</title>')
    build.OUT_HTML.write_text(html, encoding="utf-8")
    build.render_pdf()
    build.flood_margins()
