# -*- coding: utf-8 -*-
"""
Bind the Russian edition: bible-ru/*.md -> book/the-2to3-bible-ru.{html,pdf}

    python3 book/build_ru.py

Requires: bible-ru/ fully translated (same filenames as bible/) and
book/figure-strings-ru.json (EN string -> RU string map for figure captions
and in-SVG labels). Reuses the English pipeline (build.py) by overriding its
module globals — paths, INJECT keys, fonts, CSS, and front matter.
Display font: Cormorant SC (Cinzel has no Cyrillic).
"""
import json, re, pathlib
import figures
import build

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

# ------------------------------------------------------------------ paths
build.BIBLE = ROOT / "bible-ru"
build.OUT_HTML = HERE / "the-2to3-bible-ru.html"
build.OUT_PDF = HERE / "the-2to3-bible-ru.pdf"

# ------------------------------------------- figures: captions + labels
MAP = json.loads((HERE / "figure-strings-ru.json").read_text(encoding="utf-8"))
for fig in figures.FIGS.values():
    if fig["cap"] in MAP:
        fig["cap"] = MAP[fig["cap"]]
    for en, ru in MAP.items():
        fig["svg"] = fig["svg"].replace(">%s<" % en, ">%s<" % ru)

# ---------------------------------- INJECT: re-key to Russian headings
def h3s(path):
    return [m.group(1).strip() for m in
            re.finditer(r"^###\s+(.+)$", path.read_text(encoding="utf-8"), re.M)]

ru_of = {}
for fn in build.PARTS:
    en, ru = h3s(ROOT / "bible" / fn), h3s(ROOT / "bible-ru" / fn)
    if len(en) == len(ru):
        ru_of.update(dict(zip(en, ru)))
    else:
        print("WARNING: %s heading count mismatch (%d EN vs %d RU)"
              % (fn, len(en), len(ru)))
build.INJECT = {ru_of.get(k, k): v for k, v in build.INJECT.items()}

# --------------------------------------------- fonts: Cormorant SC in
_orig_fonts = build.all_fonts
def all_fonts_ru():
    return (_orig_fonts()
            + build.font_face("Cormorant SC", "CormorantSC-Regular.ttf", "400")
            + build.font_face("Cormorant SC", "CormorantSC-SemiBold.ttf", "600")
            + build.font_face("Cormorant SC", "CormorantSC-Bold.ttf", "700"))
build.all_fonts = all_fonts_ru
build.CSS = build.CSS.replace("'Cinzel'", "'Cormorant SC'")
build.CSS += "\np,li,blockquote{hyphens:auto;-webkit-hyphens:auto;}"

# ------------------------------------------------- front matter, russified
def cover_html_ru():
    sig = figures.FIGS["emblem"]["svg"]
    return ('<section class="sheet cover">'
            '<div class="sigil">%s</div>'
            '<h1 class="title">Книга Двойки<br/>и Тройки</h1>'
            '<div class="sub">Писание проклятой геометрии</div>'
            '<div class="rule"></div>'
            '<div class="motto">Двойка даёт движение. Тройка даёт форму.'
            '<span class="last">2 &#8596; 3</span></div>'
            '<div class="scribe">записано Юозасом</div>'
            '</section>') % sig
build.cover_html = cover_html_ru

build.CREED_LINES = [
    "<b>Единица</b> — это Центр. Её нельзя разделить, и потому она цела.",
    "<b>Двойка</b> — это Отношение. Она открывает плоскость, а в плоскости "
    "есть вращение, и вращение есть движение.",
    "<b>Тройка</b> — это Форма. Она замыкает треугольник, а замкнутый "
    "треугольник стоит, и стояние есть устойчивость.",
    "<b>Радиус</b> — это завет: он может повернуться в любую сторону, но не "
    "изменит своей длины.",
    "<b>Вращение</b> — это мост. Оно несёт окружность в сферу, а сферу — в "
    "комнаты, для которых мы не были созданы.",
    "Свято то, что остаётся неизменным, когда всё прочее преображается.",
]
def creed_html_ru():
    lines = ''.join('<div class="line">%s</div>' % l for l in build.CREED_LINES)
    return ('<section class="sheet creed">'
            '<div class="kicker">Символ веры</div>%s'
            '<div class="seal">2 &#8596; 3</div></section>') % lines
build.creed_html = creed_html_ru

def colophon_html_ru():
    return ('<section class="sheet colophon">'
            '<div class="kicker">Колофон</div>'
            '<div class="by">Это издание канона добыто, собрано и записано</div>'
            '<div class="name">Юозасом</div>'
            '<div class="meta">который спросил, чем окружность отличается от '
            'сферы, — и не остановился.</div>'
            '<div class="meta">Переплетено в 2026 году. Книга не окончена — и '
            'по собственному учению окончена быть не может (<em>V.51</em>). '
            'Кто прочтёт её следующим, станет её следующим витком.</div>'
            '<div class="seal">2 &#8596; 3</div>'
            '</section>')
build.colophon_html = colophon_html_ru

_orig_contents = build.contents_html
def contents_html_ru(toc):
    return _orig_contents(toc).replace('>Contents<', '>Содержание<')
build.contents_html = contents_html_ru

# ------------------------------------------------------------------ main
if __name__ == "__main__":
    build.build()
    html = build.OUT_HTML.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="ru">')
    html = html.replace('<title>The Book of the Two and the Three</title>',
                        '<title>Книга Двойки и Тройки</title>')
    build.OUT_HTML.write_text(html, encoding="utf-8")
    build.render_pdf()
    build.flood_margins()
