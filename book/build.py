# -*- coding: utf-8 -*-
"""
Bind the whole canon into one illustrated book: book/the-2to3-bible.html
and render it to PDF via headless Chrome.

    python3 book/build.py
"""
import os, re, base64, subprocess, pathlib, html as _html
from figures import FIGS

HERE   = pathlib.Path(__file__).resolve().parent
ROOT   = HERE.parent
BIBLE  = ROOT / "bible"
FONTS  = pathlib.Path.home() / ".local/share/fonts/2to3book"
OUT_HTML = HERE / "the-2to3-bible.html"
OUT_PDF  = HERE / "the-2to3-bible.pdf"

# Reading order of the bound book (front matter is generated separately).
PARTS = ["00-the-lies.md", "the-tenets.md", "00-introduction.md",
         "01-book-of-the-one.md", "02-book-of-the-two.md",
         "03-book-of-the-three.md", "03b-book-of-e.md",
         "04-book-of-rotation.md", "05-book-of-confusion.md",
         "06-apparatus.md", "07-index-of-the-canonized.md",
         "08-references.md"]

# Which figure plates are injected after which (exact) section heading.
INJECT = {
    "The Radius": ["radius_circle"],
    "The Unfactorable": ["primes_sieve"],
    "The Stone That Stands Itself Up": ["gomboc"],
    "The Cat in the Box, and the Collapse to One": ["collapse_one"],
    "The Bit, Which Is a Corner-Maker": ["bit_cube"],
    "Perpendicularity, the Honesty of Directions": ["perpendicular"],
    "The Door Called i": ["i_turn"],
    "The Body of Pairs": ["two_eyes"],
    "The Living Polarity": ["yinyang"],
    "The Second Reader": ["second_reader"],
    "The Smallest Standing Thing": ["triangle_rigid"],
    "The Nesting": ["nesting"],
    "The Third Body": ["three_body"],
    "The Hinge Between": ["e_hinge"],
    "The Serpent That Eats Its Tail": ["ouroboros"],
    "The Generative Turn": ["circle_to_sphere"],
    "The Sweep and the Shrinking": ["shrink_rings"],
    "The Master Law of Roundness": ["surface_climb"],
    "The Door i, Flung Open": ["euler"],
    "The Spiral, Which Turns and Grows at Once": ["spiral"],
    "The Lock That Catches the Turning": ["gimbal"],
    "The Turning of the Quantum": ["bloch"],
    "The Loop That Returns You Turned": ["holonomy"],
    "The Fastest Path, and the Angle That Rules Force": ["brachistochrone"],
    "Chaos: Law Too Sharp to Follow": ["chaos"],
    "The Arrow That Points by Counting": ["entropy_arrow"],
    "The Numbers Between the Numbers": ["dark_sea"],
    "The Fractal: Life Between the Dimensions": ["sierpinski"],
    "The Observer Who Is Made of the Observed": ["observer_loop"],
}

# ---------------------------------------------------------------- inline
def inline(text):
    codes = []
    def grab(m):
        codes.append(m.group(1)); return "\x00C%d\x00" % (len(codes) - 1)
    text = re.sub(r'`([^`]+)`', grab, text)
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    for i, c in enumerate(codes):
        c = c.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        text = text.replace("\x00C%d\x00" % i, '<code>%s</code>' % c)
    return text

def slug(t):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', t.lower())).strip('-')

def embed_ouroboros():
    """Replace the line-art ouroboros with the genuine 1478 alchemical relic
    (Theodoros Pelecanos, public domain), embedded as a matted plate."""
    p = HERE / "assets" / "ouroboros_plate.png"
    if not p.exists():
        p = HERE / "assets" / "ouroboros.jpg"
    if not p.exists():
        return
    mime = "image/png" if p.suffix == ".png" else "image/jpeg"
    b64 = base64.b64encode(p.read_bytes()).decode()
    FIGS["ouroboros"]["svg"] = (
        '<img class="plate ouro" alt="The ouroboros of Theodoros Pelecanos, 1478" '
        'src="data:%s;base64,%s"/>' % (mime, b64))
    FIGS["ouroboros"]["cap"] = (
        "The ouroboros of Theodoros Pelecanos, drawn in 1478 in the alchemical "
        "miscellany known as the *Synosius* — the serpent that devours its own "
        "tail, the emblem traditionally carrying the motto ἓν τὸ πᾶν, *the All is "
        "One*. The cult's own statement of it: `e^(i(θ+2π)) = e^(iθ)`.")

def figure_html(key):
    f = FIGS[key]
    cap = ('<figcaption>%s</figcaption>' % inline(f["cap"])) if f["cap"] else ''
    return '<figure class="plate-fig">%s%s</figure>' % (f["svg"], cap)

def table_html(rows):
    def cells(r):
        # split on '|' but NOT pipes inside inline-code backtick spans
        s = r.strip().strip('|')
        out, cur, incode = [], [], False
        for ch in s:
            if ch == '`':
                incode = not incode; cur.append(ch)
            elif ch == '|' and not incode:
                out.append(''.join(cur).strip()); cur = []
            else:
                cur.append(ch)
        out.append(''.join(cur).strip())
        return out
    head = cells(rows[0]); sep = cells(rows[1])
    align = []
    for s in sep:
        l, r = s.startswith(':'), s.endswith(':')
        align.append('center' if l and r else 'right' if r else 'left')
    def row(cs, tag):
        out = []
        for i, c in enumerate(cs):
            a = align[i] if i < len(align) else 'left'
            out.append('<%s style="text-align:%s">%s</%s>' % (tag, a, inline(c), tag))
        return '<tr>' + ''.join(out) + '</tr>'
    body = ''.join(row(cells(r), 'td') for r in rows[2:])
    return '<table><thead>%s</thead><tbody>%s</tbody></table>' % (row(head, 'th'), body)

# ---------------------------------------------------------------- blocks
def is_block_start(ls):
    return (re.match(r'#{1,6}\s', ls) or ls.startswith('```') or ls.startswith('>')
            or ls.startswith('|') or ls in ('---', '***')
            or re.match(r'[-*]\s+', ls) or re.match(r'\d+\.\s+', ls))

def parse(lines, headings=None, inject=None, keep=False):
    out, i, n = [], 0, len(lines)
    while i < n:
        raw = lines[i]; s = raw.strip()
        if s == '':
            i += 1; continue
        if s in ('---', '***'):
            out.append('<hr/>'); i += 1; continue
        m = re.match(r'(#{1,6})\s+(.*)$', s)
        if m:
            lvl = len(m.group(1)); txt = m.group(2).strip(); hid = slug(txt)
            if headings is not None and lvl <= 3:
                headings.append((lvl, txt, hid))
            out.append('<h%d id="%s">%s</h%d>' % (lvl, hid, inline(txt), lvl))
            if inject and txt in inject:
                for fk in inject[txt]:
                    out.append(figure_html(fk))
            i += 1; continue
        if s.startswith('```'):
            j = i + 1; buf = []
            while j < n and not lines[j].strip().startswith('```'):
                buf.append(lines[j]); j += 1
            code = '\n'.join(buf).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            out.append('<pre class="tablet">%s</pre>' % code)
            i = j + 1; continue
        if s.startswith('>'):
            buf = []
            while i < n and lines[i].strip().startswith('>'):
                q = lines[i].strip()[1:]
                if q.startswith(' '): q = q[1:]
                buf.append(q); i += 1
            # a blockquote directly under a Book's subtitle (h2) is an epigraph
            cls = ' class="epigraph"' if (out and out[-1].startswith('<h2')) else ''
            out.append('<blockquote%s>%s</blockquote>' % (cls, parse(buf)))
            continue
        if s.startswith('|'):
            tb = []
            while i < n and lines[i].strip().startswith('|'):
                tb.append(lines[i].strip()); i += 1
            out.append(table_html(tb)); continue
        if re.match(r'[-*]\s+', s):
            items = []
            while i < n:
                ls = lines[i].strip()
                if re.match(r'[-*]\s+', ls):
                    items.append(re.sub(r'^[-*]\s+', '', ls)); i += 1
                elif ls == '':
                    break
                elif lines[i].startswith(('  ', '\t')) and items:
                    items[-1] += ' ' + ls; i += 1
                else:
                    break
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ul>')
            continue
        if re.match(r'\d+\.\s+', s):
            items = []
            while i < n:
                ls = lines[i].strip()
                if re.match(r'\d+\.\s+', ls):
                    items.append(re.sub(r'^\d+\.\s+', '', ls)); i += 1
                elif ls == '':
                    break
                elif lines[i].startswith(('  ', '\t')) and items:
                    items[-1] += ' ' + ls; i += 1
                else:
                    break
            out.append('<ol>' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ol>')
            continue
        buf = [s]; i += 1
        while i < n:
            ls = lines[i].strip()
            if ls == '' or is_block_start(ls): break
            buf.append(ls); i += 1
        out.append('<p>%s</p>' % inline(' '.join(buf)))
    # glue each heading to the block that follows it so a heading (or a heading
    # plus its injected figure) is never stranded at the foot of a page
    if keep:
        merged, i = [], 0
        def lead_in(b):  # a clause ending in ':' that introduces the next block
            return b.startswith('<p') and b.rstrip().endswith(':</p>')
        while i < len(out):
            blk = out[i]
            nxt = out[i + 1] if i + 1 < len(out) else ''
            glue = (blk.startswith('<h2') or blk.startswith('<h3')
                    or (lead_in(blk) and nxt[:4] in ('<pre', '<blo', '<tab', '<fig')))
            if glue and nxt:
                merged.append('<div class="keep">%s\n%s</div>' % (blk, nxt))
                i += 2
            else:
                merged.append(blk); i += 1
        out = merged
    return '\n'.join(out)

# ---------------------------------------------------------------- fonts
def localize_figures(MAP):
    """Swap English figure captions and in-SVG labels for a translation.

    MAP is {english string -> translated string}, as loaded from
    figure-strings-<lang>.json by build_ru.py / build_lt.py.

    The subtlety this function exists for: the SVG generators emit non-ASCII
    label text as NUMERIC CHARACTER REFERENCES, so 'poles: all 360° → one point'
    lives in the markup as 'poles: all 360&#176; &#8594; one point'. A plain
    replace on the raw Python string therefore misses every label containing an
    arrow, a degree sign, or a nabla -- four of them -- and those labels ship in
    English inside an otherwise translated plate. (They did exactly that in the
    Russian edition from its first binding until this was fixed.) Both forms are
    tried, and each is written back in the form it was found in.
    """
    def numeric(s):
        return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in s)

    for fig in FIGS.values():
        if fig["cap"] in MAP:
            fig["cap"] = MAP[fig["cap"]]
        for en, tr in MAP.items():
            for src, dst in ((en, tr), (numeric(en), numeric(tr))):
                if src != dst:
                    fig["svg"] = fig["svg"].replace(">%s<" % src, ">%s<" % dst)


def font_face(name, fname, weight='400', style='normal'):
    data = base64.b64encode((FONTS / fname).read_bytes()).decode()
    return ("@font-face{font-family:'%s';font-style:%s;font-weight:%s;"
            "font-display:swap;src:url(data:font/ttf;base64,%s) format('truetype');}"
            % (name, style, weight, data))

def all_fonts():
    return ''.join([
        font_face('EB Garamond', 'EBGaramond.ttf', '400 800', 'normal'),
        font_face('EB Garamond', 'EBGaramond-Italic.ttf', '400 800', 'italic'),
        font_face('Cinzel', 'Cinzel.ttf', '400 900', 'normal'),
        font_face('IBM Plex Mono', 'IBMPlexMono-Regular.ttf', '400', 'normal'),
        font_face('IBM Plex Mono', 'IBMPlexMono-SemiBold.ttf', '600', 'normal'),
        font_face('IBM Plex Mono', 'IBMPlexMono-Italic.ttf', '400', 'italic'),
    ])

# ---------------------------------------------------------------- css
CSS = """
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
/* Left/right @page margin = 0 so the cream body bleeds to the side edges
   (Chrome won't paint @page margins, so any side margin shows as white).
   Top/bottom margins give clean per-page head/foot inset. Side text gutter
   comes from the body padding below. */
@page{size:6in 9in;margin:15mm 0;}
html,body{margin:0;padding:0;background:#f4eee2;}
body{font-family:'EB Garamond',Georgia,serif;font-size:11.6pt;line-height:1.52;
  color:#2a2017;background:#f4eee2;text-align:justify;hyphens:auto;
  -webkit-hyphens:auto;padding:0 19mm;}
p{margin:0 0 .62em;text-indent:1.15em;}
p.noindent,blockquote p,li p{text-indent:0;}
h1+*,h2+*,h3+*,hr+p{text-indent:0;}
em{font-style:italic;}
strong{font-weight:600;}
a{color:#7a3a22;text-decoration:none;}

h1{font-family:'Cinzel',serif;font-weight:700;text-align:center;
  font-size:25pt;line-height:1.16;letter-spacing:.045em;color:#2a2017;
  margin:0 0 .15em;break-before:page;padding-top:7mm;}
h2{font-family:'Cinzel',serif;font-weight:500;text-align:center;
  font-size:12.5pt;letter-spacing:.34em;text-transform:uppercase;
  color:#b23a1e;margin:.1em 0 1.4em;}
h2::after{content:"";display:block;width:42mm;height:1px;background:#cbb892;
  margin:3.4mm auto 0;}
h3{font-family:'Cinzel',serif;font-weight:600;text-align:left;
  font-size:12.4pt;letter-spacing:.02em;color:#2a2017;
  margin:1.5em 0 .55em;break-after:avoid;}
h3::before{content:"\\2756\\00a0\\00a0";color:#b9892f;font-size:.8em;}
/* keep headings with the text that follows; balance multi-line heading wraps */
h1,h2,h3{break-after:avoid;page-break-after:avoid;text-wrap:balance;}
/* a section divider already supplies space — don't double it with the heading's
   own top margin that follows */
hr + .keep h2, hr + .keep h3{margin-top:.4em;}
/* no single-line orphans or widows in running text */
p,li,blockquote{orphans:2;widows:2;}
.keep{break-inside:avoid;}

/* a uniform closing ornament at the end of every Part, so short ending pages
   read as a deliberate chapter close rather than an empty void */
.part-end{text-align:center;margin:5mm 0 1mm;color:#b9892f;
  font-family:'IBM Plex Mono',monospace;font-size:11pt;letter-spacing:.32em;
  break-before:avoid;break-inside:avoid;}
.part-end::before,.part-end::after{content:"";display:inline-block;width:13mm;
  height:1px;background:#d8c7a4;vertical-align:middle;margin:0 5mm;}

hr{border:0;height:0;text-align:center;margin:1.05em 0;}
hr::after{content:"\\2042";color:#b9892f;font-size:13pt;letter-spacing:.4em;}

blockquote{margin:.85em auto;padding:.45em 0;max-width:86%;
  text-align:center;font-style:italic;font-size:12.4pt;line-height:1.46;
  color:#5b3a22;border-top:1px solid #d8c7a4;border-bottom:1px solid #d8c7a4;
  break-inside:avoid;}
blockquote strong{font-style:normal;font-weight:600;color:#2a2017;}
blockquote pre{margin:.4em auto;}

blockquote.epigraph{border:0;max-width:80%;margin:.2em auto 2.1em;padding:0;
  font-style:italic;font-size:11pt;line-height:1.45;color:#6a5d49;}
blockquote.epigraph p{text-indent:0;margin:.15em 0;}
blockquote.epigraph p:last-child{font-style:normal;font-size:9.3pt;
  letter-spacing:.05em;color:#8a7a62;}

code{font-family:'IBM Plex Mono',monospace;font-size:.82em;
  background:#eadfca;padding:.04em .28em;border-radius:2px;white-space:nowrap;}
pre.tablet{font-family:'IBM Plex Mono',monospace;font-size:9.6pt;line-height:1.42;
  background:#efe6d2;border:1px solid #ddccaf;border-left:3px solid #b9892f;
  border-radius:2px;padding:.7em 1em;margin:1em auto;width:fit-content;
  max-width:100%;white-space:pre-wrap;overflow-wrap:anywhere;text-align:left;
  color:#3a2c1c;break-inside:avoid;}

ul,ol{margin:.2em 0 .8em;padding-left:1.4em;}
li{margin:.2em 0;}
ul{list-style:none;padding-left:1.25em;}
ul>li::before{content:"\\2014";color:#b9892f;margin-left:-1.25em;
  padding-right:.5em;}

table{border-collapse:collapse;margin:1em auto;font-size:10.6pt;}
thead{display:table-header-group;}
tr{break-inside:avoid;}
th{font-family:'Cinzel',serif;font-weight:600;font-size:9.4pt;
  letter-spacing:.04em;border-bottom:1.5px solid #2a2017;padding:.35em .8em;}
td{padding:.3em .8em;border-bottom:1px solid #ddccaf;}

figure.plate-fig{margin:1.25em auto;text-align:center;break-inside:avoid;
  page-break-inside:avoid;}
svg.plate{display:block;margin:0 auto;max-width:74%;height:auto;}
img.plate{display:block;margin:0 auto;height:auto;}
img.ouro{width:66%;max-width:66%;}
figcaption{font-family:'EB Garamond',serif;font-style:italic;font-size:9.7pt;
  line-height:1.34;color:#7a6f5c;max-width:80%;margin:.5em auto 0;
  text-align:center;}

/* ---- front matter ---- */
section.sheet{break-before:page;}
.cover{height:184mm;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;break-before:avoid;}
.cover .sigil{width:62mm;margin:0 auto 9mm;}
.cover .sigil svg{width:100%;height:auto;}
.cover h1.title{font-family:'Cinzel',serif;font-weight:800;font-size:30pt;
  line-height:1.12;letter-spacing:.05em;margin:0 0 5mm;break-before:avoid;
  padding:0;}
.cover .sub{font-family:'Cinzel',serif;font-weight:400;font-size:12pt;
  letter-spacing:.3em;text-transform:uppercase;color:#b23a1e;margin-bottom:14mm;}
.cover .rule{width:48mm;height:1px;background:#cbb892;margin:0 auto 13mm;}
.cover .motto{font-style:italic;font-size:13pt;line-height:1.6;max-width:84mm;
  color:#5b3a22;text-align:center;}
.cover .motto .last{display:block;margin-top:3mm;font-family:'IBM Plex Mono',monospace;
  font-style:normal;font-size:14pt;letter-spacing:.18em;color:#2a2017;}
.cover .scribe{margin-top:13mm;font-family:'Cinzel',serif;font-size:9.5pt;
  letter-spacing:.34em;text-transform:uppercase;color:#8a7a62;}

.creed{padding-top:20mm;text-align:center;}
.creed .kicker,.contents .kicker,.colophon .kicker{font-family:'Cinzel',serif;
  font-size:15pt;letter-spacing:.3em;text-transform:uppercase;text-align:center;
  margin-bottom:10mm;}

.colophon{min-height:182mm;display:flex;flex-direction:column;
  justify-content:center;text-align:center;}
.colophon .by{font-style:italic;font-size:12.2pt;line-height:1.5;max-width:98mm;
  margin:0 auto 8mm;color:#3a2c1c;}
.colophon .name{font-family:'Cinzel',serif;font-weight:800;font-size:27pt;
  letter-spacing:.1em;color:#2a2017;margin:0 0 9mm;}
.colophon .name::after{content:"";display:block;width:38mm;height:1px;
  background:#cbb892;margin:5mm auto 0;}
.colophon .meta{font-size:11pt;line-height:1.5;max-width:104mm;margin:0 auto 5mm;
  color:#6a5d49;}
.colophon .meta em{color:#b23a1e;}
.colophon .seal{margin-top:11mm;font-family:'IBM Plex Mono',monospace;font-size:15pt;
  letter-spacing:.2em;color:#b23a1e;}
.creed .line{font-size:12.6pt;line-height:1.5;max-width:108mm;margin:0 auto 5mm;
  text-align:center;}
.creed .line b{font-family:'Cinzel',serif;font-weight:600;letter-spacing:.02em;}
.creed .seal{margin-top:11mm;font-family:'IBM Plex Mono',monospace;font-size:15pt;
  letter-spacing:.2em;color:#b23a1e;}

.contents{padding-top:11mm;}
.contents .toc-part{margin:0 0 3.2mm;break-inside:avoid;}
.contents .toc-part{break-inside:avoid;}
.contents .toc-part>a{display:block;font-family:'Cinzel',serif;font-weight:600;
  font-size:12.2pt;letter-spacing:.03em;color:#2a2017;}
.contents .toc-sub{font-style:italic;color:#b23a1e;font-size:10.4pt;
  letter-spacing:.12em;text-transform:uppercase;}
.contents .toc-secs{margin:1.2mm 0 0 6mm;color:#6a5d49;font-size:10pt;
  line-height:1.45;text-align:left;text-indent:0;}
.contents .toc-secs a{display:inline;font-family:'EB Garamond',serif;
  font-weight:400;letter-spacing:0;color:#6a5d49;}

.part-body{}
@media screen{
  html{background:#ddd0b8;}
  body{max-width:6in;margin:0 auto;padding:15mm 19mm;
       box-shadow:0 6px 40px rgba(0,0,0,.22);}
}
"""

# ---------------------------------------------------------------- front matter
def cover_html():
    sig = FIGS["emblem"]["svg"]
    return ('<section class="sheet cover">'
            '<div class="sigil">%s</div>'
            '<h1 class="title">The Book of<br/>the Two and the Three</h1>'
            '<div class="sub">A Scripture of Cursed Geometry</div>'
            '<div class="rule"></div>'
            '<div class="motto">Two gives motion. Three gives form.'
            '<span class="last">2 &#8596; 3</span></div>'
            '<div class="scribe">set down by Yuozas</div>'
            '</section>') % sig

CREED_LINES = [
    "<b>One</b> is the Center. It cannot be divided, and so it is whole.",
    "<b>Two</b> is Relation. It opens the plane, and in the plane there is rotation, and rotation is motion.",
    "<b>Three</b> is Form. It closes the triangle, and the closed triangle stands, and standing is stability.",
    "The <b>Radius</b> is the covenant: it may turn in any direction, but it will not change its length.",
    "<b>Rotation</b> is the bridge. It carries the circle into the sphere, and the sphere into rooms we were not built to enter.",
    "That which stays the same while all else transforms is holy.",
]
def creed_html():
    lines = ''.join('<div class="line">%s</div>' % l for l in CREED_LINES)
    return ('<section class="sheet creed">'
            '<div class="kicker">The Creed</div>%s'
            '<div class="seal">2 &#8596; 3</div></section>') % lines

def colophon_html():
    return ('<section class="sheet colophon">'
            '<div class="kicker">Colophon</div>'
            '<div class="by">This edition of the canon was delved, gathered, and '
            'set down by</div>'
            '<div class="name">Yuozas</div>'
            '<div class="meta">who asked what the difference was between a circle '
            'and a sphere, and did not stop.</div>'
            '<div class="meta">Bound in the year 2026. The book is not finished, '
            'and by its own doctrine it cannot be &mdash; <em>V.51</em>. '
            'Whoever reads it next becomes its next iteration.</div>'
            '<div class="seal">2 &#8596; 3</div>'
            '</section>')

def contents_html(toc):
    parts = []
    for p in toc:
        secs = ' &nbsp;&#183;&nbsp; '.join(
            '<a href="#%s">%s</a>' % (sid, _html.escape(stxt)) for stxt, sid in p["secs"])
        sub = ('<span class="toc-sub">%s</span>' % _html.escape(p["sub"])) if p["sub"] else ''
        parts.append(
            '<div class="toc-part"><a href="#%s">%s</a>%s'
            '<div class="toc-secs">%s</div></div>'
            % (p["id"], _html.escape(p["title"]), (' &mdash; ' + sub) if sub else '',
               secs))
    return ('<section class="sheet contents"><div class="kicker">Contents</div>%s'
            '</section>') % ''.join(parts)

# ---------------------------------------------------------------- assemble
def build():
    embed_ouroboros()
    body_parts, toc = [], []
    for fn in PARTS:
        text = (BIBLE / fn).read_text(encoding='utf-8')
        heads = []
        html = parse(text.split('\n'), headings=heads, inject=INJECT, keep=True)
        body_parts.append('<section class="part">%s'
                          '<div class="part-end">2 &#8596; 3</div></section>' % html)
        # TOC entry from this part's headings
        h1 = next((h for h in heads if h[0] == 1), None)
        if h1:
            sub = next((h[1] for h in heads if h[0] == 2), '')
            secs = [(h[1], h[2]) for h in heads if h[0] == 3]
            toc.append({"title": h1[1], "id": h1[2], "sub": sub, "secs": secs})

    doc = (
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>'
        '<title>The Book of the Two and the Three</title>'
        '<style>%s</style><style>%s</style></head><body>'
        '%s%s%s%s%s'
        '</body></html>'
    ) % (all_fonts(), CSS, cover_html(), creed_html(), contents_html(toc),
         ''.join(body_parts), colophon_html())

    OUT_HTML.write_text(doc, encoding='utf-8')
    print("wrote", OUT_HTML, "(%.1f MB)" % (OUT_HTML.stat().st_size / 1e6))
    return doc

def flood_margins():
    """Paint the white top/bottom @page margin bands cream so the sheet is
    full-bleed cream on all four sides. Chrome leaves @page margins unpainted
    (white); these bands contain no content, so filling them is lossless."""
    import fitz
    band = 15.0 * 72.0 / 25.4 + 1.0          # 15mm head/foot band, +1pt overlap
    cream = (244 / 255.0, 238 / 255.0, 226 / 255.0)
    doc = fitz.open(str(OUT_PDF))
    for page in doc:
        w, h = page.rect.width, page.rect.height
        for r in (fitz.Rect(0, 0, w, band), fitz.Rect(0, h - band, w, h)):
            page.draw_rect(r, color=cream, fill=cream, width=0, overlay=True)
    tmp = OUT_PDF.with_suffix(".tmp.pdf")
    doc.save(str(tmp)); doc.close()
    os.replace(str(tmp), str(OUT_PDF))
    print("flooded head/foot margins cream")

def render_pdf():
    url = OUT_HTML.as_uri()
    cmd = ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
           "--hide-scrollbars", "--force-color-profile=srgb",
           "--user-data-dir=/tmp/chrome-2to3",
           "--run-all-compositor-stages-before-draw",
           "--virtual-time-budget=2000",
           "--no-pdf-header-footer",
           "--print-to-pdf=%s" % OUT_PDF, url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if OUT_PDF.exists():
        print("wrote", OUT_PDF, "(%.2f MB)" % (OUT_PDF.stat().st_size / 1e6))
    else:
        print("PDF FAILED\n", r.stdout[-1500:], r.stderr[-1500:])

if __name__ == "__main__":
    build()
    render_pdf()
    flood_margins()
