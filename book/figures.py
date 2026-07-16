# -*- coding: utf-8 -*-
# SVG diagram library for THE BOOK OF THE TWO AND THE THREE.
# Palette:
#   ink   #2a2017   ember #b23a1e   teal #2f6f6a
#   gold  #b9892f   guide #c3b6a0   faint #ece1cd
# Each figure is fully legible as a static plate (for print); a few carry
# SMIL motion that plays in the HTML edition.

def _wrap(viewbox, body, cls=""):
    c = (" " + cls) if cls else ""
    return ('<svg class="plate%s" viewBox="%s" xmlns="http://www.w3.org/2000/svg" '
            'role="img">%s</svg>') % (c, viewbox, body)

FIGS = {}
def F(key, caption, viewbox, body, cls=""):
    FIGS[key] = {"cap": caption, "svg": _wrap(viewbox, body, cls)}

# 1 — Cover sigil: circle (the Two / rotation) holding an inscribed triangle
#     (the Three / form), one center.
F("emblem", "", "0 0 300 300", '''
<circle cx="150" cy="150" r="120" fill="none" stroke="#2a2017" stroke-width="2.4"/>
<circle cx="150" cy="150" r="120" fill="none" stroke="#b23a1e" stroke-width="1" stroke-dasharray="2 7" opacity="0.7"/>
<polygon points="150,42 254,210 46,210" fill="none" stroke="#2a2017" stroke-width="2.4"/>
<line x1="150" y1="150" x2="150" y2="42" stroke="#b9892f" stroke-width="1.3"/>
<circle cx="150" cy="150" r="4.5" fill="#b23a1e"/>
<circle cx="150" cy="42" r="3" fill="#2a2017"/>
<text x="150" y="250" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="22" letter-spacing="3" fill="#2a2017">2 &#8596; 3</text>
''')

# 2 — The radius swept into a circle.
F("radius_circle",
  "The covenant of the radius: the length is held, the direction is turned, and the set of all faithful directions is the circle.",
  "0 0 300 230", '''
<circle cx="150" cy="115" r="92" fill="none" stroke="#2a2017" stroke-width="2"/>
<line x1="150" y1="115" x2="150" y2="23" stroke="#b23a1e" stroke-width="2.4"/>
<circle cx="150" cy="23" r="5.5" fill="#b23a1e"/>
<circle cx="150" cy="115" r="4" fill="#2a2017"/>
<text x="142" y="72" text-anchor="end" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">r</text>
<path d="M 230 69 A 92 92 0 0 1 241 99" fill="none" stroke="#b9892f" stroke-width="1.6" marker-end="url(#ah)"/>
<defs><marker id="ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b9892f"/></marker></defs>
<text x="150" y="222" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">x&#178; + y&#178; = r&#178;</text>
''', cls="motion")

# 3 — Point -> circle -> sphere, each by one more perpendicular sweep.
F("circle_to_sphere",
  "Each dimension adds one perpendicular direction to sweep through, and one squared term to the covenant.",
  "0 0 480 200", '''
<!-- point -->
<circle cx="70" cy="95" r="5" fill="#b23a1e"/>
<text x="70" y="160" text-anchor="middle" font-family="'EB Garamond',serif" font-size="15" fill="#2a2017">a point</text>
<text x="70" y="178" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#7a6f5c">spun &#8594;</text>
<!-- circle -->
<circle cx="200" cy="95" r="52" fill="none" stroke="#2a2017" stroke-width="2"/>
<line x1="200" y1="95" x2="200" y2="43" stroke="#b23a1e" stroke-width="1.8"/>
<circle cx="200" cy="95" r="3.5" fill="#2a2017"/>
<text x="200" y="160" text-anchor="middle" font-family="'EB Garamond',serif" font-size="15" fill="#2a2017">a circle</text>
<text x="200" y="178" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#7a6f5c">spun &#8594;</text>
<!-- sphere -->
<circle cx="380" cy="95" r="58" fill="none" stroke="#2a2017" stroke-width="2"/>
<ellipse cx="380" cy="95" rx="58" ry="20" fill="none" stroke="#c3b6a0" stroke-width="1.2"/>
<ellipse cx="380" cy="95" rx="20" ry="58" fill="none" stroke="#c3b6a0" stroke-width="1.2"/>
<line x1="380" y1="95" x2="380" y2="37" stroke="#b23a1e" stroke-width="1.8"/>
<circle cx="380" cy="95" r="3.5" fill="#2a2017"/>
<text x="380" y="170" text-anchor="middle" font-family="'EB Garamond',serif" font-size="15" fill="#2a2017">a sphere</text>
''')

# 4 — Perpendicularity: three mutually right-angled axes; dot product zero.
F("perpendicular",
  "Two directions are independent exactly when their dot product is nothing. Independence is what lets the squares add honestly.",
  "0 0 300 210", '''
<line x1="150" y1="120" x2="150" y2="22" stroke="#2a2017" stroke-width="2" marker-end="url(#a2)"/>
<line x1="150" y1="120" x2="262" y2="120" stroke="#2a2017" stroke-width="2" marker-end="url(#a2)"/>
<line x1="150" y1="120" x2="70" y2="178" stroke="#2f6f6a" stroke-width="2" marker-end="url(#a3)"/>
<defs>
<marker id="a2" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#2a2017"/></marker>
<marker id="a3" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#2f6f6a"/></marker>
</defs>
<rect x="150" y="106" width="14" height="14" fill="none" stroke="#c3b6a0" stroke-width="1.2"/>
<path d="M 150 138 A 18 18 0 0 1 137 134" fill="none" stroke="#c3b6a0" stroke-width="1.2"/>
<text x="156" y="18" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">y</text>
<text x="266" y="124" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">x</text>
<text x="58" y="190" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2f6f6a">z</text>
<circle cx="150" cy="120" r="3.5" fill="#b23a1e"/>
<text x="150" y="205" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">a &#183; b = 0</text>
''')

# 5 — Bits build corners: segment, square, cube.
F("bit_cube",
  "Binary builds geometry by itself: one bit a segment, two bits a square, three bits a cube. The square holds the circle; the cube holds the sphere.",
  "0 0 480 190", '''
<!-- 1 bit -->
<line x1="30" y1="95" x2="110" y2="95" stroke="#2a2017" stroke-width="2"/>
<circle cx="30" cy="95" r="4.5" fill="#b23a1e"/><circle cx="110" cy="95" r="4.5" fill="#b23a1e"/>
<text x="70" y="150" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">2&#185; = 2</text>
<text x="70" y="168" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c">1 bit</text>
<!-- 2 bits -->
<rect x="180" y="55" width="80" height="80" fill="none" stroke="#2a2017" stroke-width="2"/>
<g fill="#b23a1e"><circle cx="180" cy="55" r="4.5"/><circle cx="260" cy="55" r="4.5"/><circle cx="180" cy="135" r="4.5"/><circle cx="260" cy="135" r="4.5"/></g>
<text x="220" y="150" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">2&#178; = 4</text>
<text x="220" y="168" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c">2 bits</text>
<!-- 3 bits -->
<g fill="none" stroke-width="2">
<rect x="382" y="42" width="60" height="60" stroke="#c3b6a0"/>
<line x1="360" y1="66" x2="382" y2="42" stroke="#c3b6a0"/>
<line x1="420" y1="66" x2="442" y2="42" stroke="#c3b6a0"/>
<line x1="360" y1="126" x2="382" y2="102" stroke="#c3b6a0"/>
<line x1="420" y1="126" x2="442" y2="102" stroke="#c3b6a0"/>
<rect x="360" y="66" width="60" height="60" stroke="#2a2017"/>
</g>
<text x="405" y="150" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">2&#179; = 8</text>
<text x="405" y="168" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c">3 bits</text>
''')

# 6 — The triangle refuses to shear; the square leans.
F("triangle_rigid",
  "Press a square and it shears into a rhombus with no measurement broken. The triangle cannot deform without changing a side. Rigidity is triangulation.",
  "0 0 420 200", '''
<!-- square shearing -->
<rect x="40" y="50" width="100" height="100" fill="none" stroke="#c3b6a0" stroke-width="1.6" stroke-dasharray="4 4"/>
<polygon points="78,50 178,50 140,150 40,150" fill="none" stroke="#2a2017" stroke-width="2.2"/>
<path d="M 150 40 q 25 8 28 0" fill="none" stroke="#b23a1e" stroke-width="1.4" marker-end="url(#a4)"/>
<defs><marker id="a4" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b23a1e"/></marker></defs>
<text x="105" y="182" text-anchor="middle" font-family="'EB Garamond',serif" font-size="14" fill="#2a2017">the square leans</text>
<!-- triangle holds -->
<polygon points="320,46 384,154 256,154" fill="none" stroke="#2a2017" stroke-width="2.4"/>
<g stroke="#2f6f6a" stroke-width="2.4">
<line x1="320" y1="46" x2="384" y2="154"/><line x1="384" y1="154" x2="256" y2="154"/><line x1="256" y1="154" x2="320" y2="46"/>
</g>
<g fill="#b23a1e"><circle cx="320" cy="46" r="4"/><circle cx="384" cy="154" r="4"/><circle cx="256" cy="154" r="4"/></g>
<text x="320" y="182" text-anchor="middle" font-family="'EB Garamond',serif" font-size="14" fill="#2a2017">the triangle holds</text>
''')

# 7 — Living polarity: the wheel of opposites.
F("yinyang",
  "Dead opposites are a wall; living opposites are a wheel. Each pole carries the seed of the other and forever turns into it.",
  "0 0 240 230", '''
<g>
<circle cx="120" cy="105" r="84" fill="#2a2017"/>
<path d="M120 21 a42 42 0 0 1 0 84 a42 42 0 0 0 0 84 a84 84 0 0 1 0 -168 z" fill="#ece1cd"/>
<circle cx="120" cy="63" r="13" fill="#2a2017"/>
<circle cx="120" cy="147" r="13" fill="#ece1cd"/>
<circle cx="120" cy="105" r="84" fill="none" stroke="#2a2017" stroke-width="1.5"/>
</g>
<text x="120" y="222" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#2a2017">0 &#8596; 1</text>
''', cls="motion")

# 8 — i as a quarter turn: 1 -> i -> -1 -> -i -> 1.
F("i_turn",
  "The imaginary unit is not a fiction but a quarter turn: to multiply by i is to step ninety degrees into the perpendicular direction.",
  "0 0 240 240", '''
<line x1="20" y1="120" x2="220" y2="120" stroke="#c3b6a0" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="220" stroke="#c3b6a0" stroke-width="1"/>
<circle cx="120" cy="120" r="84" fill="none" stroke="#2a2017" stroke-width="1.6"/>
<path d="M 204 120 A 84 84 0 0 1 120 36" fill="none" stroke="#b23a1e" stroke-width="2" marker-end="url(#a5)"/>
<defs><marker id="a5" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b23a1e"/></marker></defs>
<g font-family="'IBM Plex Mono',monospace" font-size="13" fill="#2a2017">
<text x="210" y="116">1</text><text x="126" y="30">i</text><text x="16" y="116">-1</text><text x="126" y="214">-i</text>
</g>
<g fill="#2a2017"><circle cx="204" cy="120" r="4"/><circle cx="120" cy="36" r="4"/><circle cx="36" cy="120" r="4"/><circle cx="120" cy="204" r="4"/></g>
<circle cx="204" cy="120" r="6" fill="#b23a1e"/>
''', cls="motion")

# 9 — Euler's turning dial.
F("euler",
  "To rotate is simply to multiply. As the angle runs, e^(iθ) walks the unit circle, its shadow on the axes the cosine and the sine.",
  "0 0 260 235", '''
<line x1="16" y1="120" x2="244" y2="120" stroke="#c3b6a0" stroke-width="1"/>
<line x1="84" y1="32" x2="84" y2="208" stroke="#c3b6a0" stroke-width="1"/>
<circle cx="84" cy="120" r="74" fill="none" stroke="#2a2017" stroke-width="1.6"/>
<line x1="84" y1="120" x2="140" y2="72" stroke="#b23a1e" stroke-width="2"/>
<line x1="140" y1="72" x2="140" y2="120" stroke="#2f6f6a" stroke-width="1.4" stroke-dasharray="3 3"/>
<line x1="84" y1="120" x2="140" y2="120" stroke="#b9892f" stroke-width="1.6"/>
<path d="M 114 120 A 30 30 0 0 0 107 101" fill="none" stroke="#2a2017" stroke-width="1.2"/>
<text x="110" y="113" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">&#952;</text>
<circle cx="140" cy="72" r="5" fill="#b23a1e"/>
<text x="146" y="66" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#b23a1e">e^(i&#952;)</text>
<text x="112" y="135" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#b9892f">cos&#952;</text>
<text x="146" y="100" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#2f6f6a">sin&#952;</text>
<text x="130" y="226" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">e^(i&#960;) + 1 = 0</text>
''')

# 10 — Logarithmic spiral: rotation across scale.
F("spiral",
  "Loosen the covenant — let the length grow as it turns — and the circle becomes a spiral: to turn and to grow without choosing between them.",
  "0 0 240 230", '''
<path d="M120 110
 m0,0
 q 6,-2 9,4 q 5,9 -4,14 q -16,8 -22,-9 q -8,-25 16,-31 q 33,-9 41,25 q 10,43 -33,52 q -52,12 -64,-39"
 fill="none" stroke="#2a2017" stroke-width="2"/>
<circle cx="120" cy="110" r="3.5" fill="#2a2017"/>
<circle cx="63" cy="126" r="5.5" fill="#b23a1e"/>
<text x="120" y="222" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">r = a&#183;e^(b&#952;)</text>
''', cls="motion")

# 11 — The surface of the unit ball: it climbs, peaks near 7, then falls.
F("surface_climb",
  "Higher is not larger. The skin of the unit ball grows, peaks near the seventh dimension, and then begins to shrink. The rooms above us are stranger.",
  "0 0 440 230", '''
<line x1="50" y1="185" x2="420" y2="185" stroke="#2a2017" stroke-width="1.4"/>
<line x1="50" y1="185" x2="50" y2="25" stroke="#2a2017" stroke-width="1.4"/>
<text x="235" y="215" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c">dimension n &#8594;</text>
<text x="20" y="105" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c" transform="rotate(-90 20 105)">surface</text>
<polyline points="86,148 122,121 158,99 194,82 230,72 266,68 302,71 338,80 374,90"
  fill="none" stroke="#b23a1e" stroke-width="2.2"/>
<g font-family="'IBM Plex Mono',monospace" font-size="10" fill="#2a2017">
<g fill="#2a2017">
<circle cx="86" cy="148" r="3"/><circle cx="122" cy="121" r="3"/><circle cx="158" cy="99" r="3"/><circle cx="194" cy="82" r="3"/>
<circle cx="230" cy="72" r="3"/><circle cx="266" cy="68" r="3.6" fill="#b23a1e"/><circle cx="302" cy="71" r="3"/><circle cx="338" cy="80" r="3"/><circle cx="374" cy="90" r="3"/>
</g>
</g>
<g stroke="#2a2017" stroke-width="1">
<line x1="86" y1="185" x2="86" y2="190"/><line x1="158" y1="185" x2="158" y2="190"/>
<line x1="230" y1="185" x2="230" y2="190"/><line x1="302" y1="185" x2="302" y2="190"/>
</g>
<g text-anchor="middle" font-size="11">
<text x="86" y="202">2</text><text x="158" y="202">4</text><text x="230" y="202">6</text><text x="302" y="202">8</text>
<text x="266" y="202" fill="#b23a1e">7</text>
</g>
<text x="266" y="58" text-anchor="middle" font-family="'EB Garamond',serif" font-size="12" fill="#b23a1e">peak</text>
''')

# 12 — Sweep and shrinking: stacked rings collapse toward the poles.
F("shrink_rings",
  "The swept ring shrinks toward the poles by a factor of sin φ. At the pole, a full turn is no distance at all. That collapse is the surface element.",
  "0 0 240 240", '''
<circle cx="120" cy="120" r="92" fill="none" stroke="#2a2017" stroke-width="2"/>
<g fill="none" stroke="#b23a1e" stroke-width="1.5">
<ellipse cx="120" cy="50" rx="60" ry="13"/>
<ellipse cx="120" cy="85" rx="85" ry="18"/>
<ellipse cx="120" cy="120" rx="92" ry="20"/>
<ellipse cx="120" cy="155" rx="85" ry="18"/>
<ellipse cx="120" cy="190" rx="60" ry="13"/>
</g>
<circle cx="120" cy="28" r="3.5" fill="#2a2017"/>
<circle cx="120" cy="212" r="3.5" fill="#2a2017"/>
<text x="150" y="124" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#2a2017">r&#183;sin&#966;</text>
<text x="120" y="234" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#7a6f5c">poles: all 360&#176; &#8594; one point</text>
''')

# 13 — Gimbal lock: three freedoms collapse toward two.
F("gimbal",
  "Three stacked angles control a three-roomed orientation — until two axes swing into alignment, and three rotational freedoms collapse toward two.",
  "0 0 320 185", '''
<g fill="none" stroke-width="2.2">
<circle cx="80" cy="95" r="55" stroke="#2a2017"/>
<ellipse cx="80" cy="95" rx="55" ry="20" stroke="#2f6f6a"/>
<ellipse cx="80" cy="95" rx="20" ry="55" stroke="#b23a1e"/>
</g>
<g fill="none" stroke-width="2.2">
<circle cx="240" cy="95" r="55" stroke="#2a2017"/>
<ellipse cx="240" cy="95" rx="20" ry="55" stroke="#2f6f6a"/>
<ellipse cx="237" cy="95" rx="20" ry="55" stroke="#b23a1e"/>
</g>
<line x1="148" y1="95" x2="172" y2="95" stroke="#2a2017" stroke-width="2" marker-end="url(#agl)"/>
<text x="160" y="82" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">3 &#8594; 2</text>
<g font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c" text-anchor="middle">
<text x="80" y="172">free: three rings, three turnings</text>
<text x="240" y="172">locked: two rings aligned</text>
</g>
<defs><marker id="agl" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#2a2017"/></marker></defs>
''')

# 14 — The Bloch sphere: two states, one sphere.
F("bloch",
  "The qubit keeps two states but no longer sits at a corner: it is any blend, drawn on a sphere, and computed by being turned.",
  "0 0 240 250", '''
<circle cx="120" cy="120" r="90" fill="none" stroke="#2a2017" stroke-width="2"/>
<ellipse cx="120" cy="120" rx="90" ry="26" fill="none" stroke="#c3b6a0" stroke-width="1.2"/>
<line x1="120" y1="30" x2="120" y2="210" stroke="#c3b6a0" stroke-width="1"/>
<line x1="120" y1="120" x2="178" y2="72" stroke="#b23a1e" stroke-width="2.2"/>
<circle cx="178" cy="72" r="5" fill="#b23a1e"/>
<path d="M 120 86 A 34 34 0 0 1 142 96" fill="none" stroke="#2a2017" stroke-width="1.2"/>
<text x="135" y="86" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#2a2017">&#952;</text>
<circle cx="120" cy="30" r="4" fill="#2a2017"/><circle cx="120" cy="210" r="4" fill="#2a2017"/>
<text x="120" y="24" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#2a2017">|0&#10217;</text>
<text x="120" y="230" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#2a2017">|1&#10217;</text>
<text x="120" y="248" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#7a6f5c">&#945;|0&#10217; + &#946;|1&#10217;</text>
''')

# 15 — The Gomboc energy landscape: one stable rest, one unstable.
F("gomboc",
  "The stone's surface sets the height of its center of mass for every pose. It rolls always downhill to the one stable rest, where the turning force is nothing.",
  "0 0 420 210", '''
<path d="M 40 60 C 110 60, 120 150, 175 150 C 215 150, 215 95, 260 95 C 330 95, 330 175, 392 60"
  fill="none" stroke="#2a2017" stroke-width="2"/>
<circle cx="175" cy="138" r="11" fill="#b23a1e"/>
<path d="M 90 88 q 30 30 70 40" fill="none" stroke="#b9892f" stroke-width="1.4" marker-end="url(#a6)"/>
<defs><marker id="a6" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b9892f"/></marker></defs>
<text x="175" y="178" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#2a2017">stable (&#8711;U = 0, min)</text>
<text x="262" y="86" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c">unstable (max)</text>
<text x="210" y="24" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">U = m&#183;g&#183;h</text>
''')

# 16 — Collapse of the many into the One.
F("collapse_one",
  "The stone, the falling cat, the cat in the box: each grinds a world of many possible states down to one settled state. All fall, in the end, to the One.",
  "0 0 380 200", '''
<g stroke-width="2" fill="none">
<line x1="40" y1="40" x2="250" y2="100" stroke="#c3b6a0"/>
<line x1="40" y1="80" x2="250" y2="100" stroke="#c3b6a0"/>
<line x1="40" y1="120" x2="250" y2="100" stroke="#c3b6a0"/>
<line x1="40" y1="160" x2="250" y2="100" stroke="#c3b6a0"/>
</g>
<g fill="#b9892f" opacity="0.85"><circle cx="40" cy="40" r="6"/><circle cx="40" cy="80" r="6"/><circle cx="40" cy="120" r="6"/><circle cx="40" cy="160" r="6"/></g>
<path d="M 250 100 L 300 100" stroke="#2a2017" stroke-width="2" marker-end="url(#a7)"/>
<defs><marker id="a7" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#2a2017"/></marker></defs>
<circle cx="328" cy="100" r="10" fill="#b23a1e"/>
<text x="120" y="190" text-anchor="middle" font-family="'EB Garamond',serif" font-size="14" fill="#7a6f5c">many possibilities</text>
<text x="328" y="142" text-anchor="middle" font-family="'EB Garamond',serif" font-size="14" fill="#2a2017">one</text>
''')

# 17 — The fractal: the same rule echoed across scale (3 returns). Generated by
#      exact recursive subdivision (every vertex is a true midpoint) so all edges
#      align precisely.
def _sierpinski(depth, A=(130.0, 17.0), B=(21.0, 213.0), C=(239.0, 213.0)):
    mid = lambda p, q: ((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0)
    holes = []
    def rec(a, b, c, d):
        if d <= 0:
            return
        ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
        holes.append((ab, bc, ca))         # carve the central (inverted) triangle
        rec(a, ab, ca, d - 1)
        rec(ab, b, bc, d - 1)
        rec(ca, bc, c, d - 1)
    rec(A, B, C, depth)
    poly = lambda t, f: ('<polygon points="%.2f,%.2f %.2f,%.2f %.2f,%.2f" '
                         'fill="%s"/>' % (t[0][0], t[0][1], t[1][0], t[1][1],
                                          t[2][0], t[2][1], f))
    return poly((A, B, C), '#2a2017') + ''.join(poly(t, '#ece1cd') for t in holes)

F("sierpinski",
  "Where the sphere is made by rotation, the fractal is made by recursion: the same rule at smaller and smaller scale. And the holy Three returns even here.",
  "0 0 260 230", _sierpinski(5))

# 18 — Chaos: nearby starts diverge exponentially.
F("chaos",
  "Two starts a hair apart obey the same exact rule, agree for a while, then diverge without bound. The future is fixed and still unknowable.",
  "0 0 420 200", '''
<line x1="40" y1="100" x2="400" y2="100" stroke="#c3b6a0" stroke-width="1"/>
<path d="M 40 96 C 120 92, 150 110, 200 88 C 250 66, 290 150, 340 50 C 365 8, 385 120, 400 70"
  fill="none" stroke="#2a2017" stroke-width="2"/>
<path d="M 40 104 C 120 108, 150 92, 200 112 C 250 134, 290 40, 340 150 C 365 188, 385 70, 400 130"
  fill="none" stroke="#b23a1e" stroke-width="2"/>
<circle cx="40" cy="100" r="5" fill="#2a2017"/>
<text x="120" y="36" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#2a2017">&#948;(t) = &#948;&#8320;&#183;e^(&#955;t)</text>
<text x="40" y="130" text-anchor="middle" font-family="'EB Garamond',serif" font-size="12" fill="#7a6f5c">one seed,</text>
<text x="40" y="146" text-anchor="middle" font-family="'EB Garamond',serif" font-size="12" fill="#7a6f5c">a hair apart</text>
''')

# 19 — Two eyes triangulate depth.
F("two_eyes",
  "Neither eye sees depth; each gets a nearly flat image. The brain takes the difference between them and computes the third dimension. To perceive is to subtract.",
  "0 0 360 210", '''
<circle cx="180" cy="40" r="9" fill="#b23a1e"/>
<text x="180" y="26" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#2a2017">object</text>
<g stroke="#2f6f6a" stroke-width="1.6"><line x1="90" y1="160" x2="180" y2="40"/><line x1="270" y1="160" x2="180" y2="40"/></g>
<line x1="90" y1="160" x2="270" y2="160" stroke="#c3b6a0" stroke-width="1.4" stroke-dasharray="4 4"/>
<g fill="#2a2017"><circle cx="90" cy="160" r="7"/><circle cx="270" cy="160" r="7"/></g>
<text x="90" y="184" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#2a2017">left</text>
<text x="270" y="184" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#2a2017">right</text>
<path d="M 150 150 A 50 50 0 0 1 210 150" fill="none" stroke="#b9892f" stroke-width="1.4"/>
<text x="180" y="138" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#b9892f">disparity</text>
''')

# 20 — Brachistochrone: the fastest path is not the shortest.
F("brachistochrone",
  "A straight line is the shortest path and almost never the fastest. The quickest descent under gravity drops steeply first, then flattens: a cycloid.",
  "0 0 360 210", '''
<line x1="40" y1="40" x2="320" y2="160" stroke="#c3b6a0" stroke-width="1.8" stroke-dasharray="5 5"/>
<path d="M 40 40 C 70 150, 150 175, 320 160" fill="none" stroke="#b23a1e" stroke-width="2.4"/>
<g fill="#2a2017"><circle cx="40" cy="40" r="5.5"/><circle cx="320" cy="160" r="5.5"/></g>
<text x="200" y="78" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c" transform="rotate(7 200 78)">shortest</text>
<text x="150" y="186" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#b23a1e">fastest (cycloid)</text>
<text x="318" y="38" text-anchor="end" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#2a2017">F = m&#183;g&#183;sin&#952;</text>
''')

# 21 — The observer loop: the system contains a model of itself.
F("observer_loop",
  "The universe produced observers who study it: the part holds a picture of the whole. This is not a chain but a loop, a recursion folding in.",
  "0 0 300 230", '''
<g font-family="'EB Garamond',serif" font-size="14" fill="#2a2017" text-anchor="middle">
<text x="150" y="42">Universe</text>
<text x="234" y="178">Brain</text>
<text x="66" y="178">Mathematics</text>
</g>
<g fill="none" stroke="#b23a1e" stroke-width="2" marker-end="url(#a8)">
<path d="M 183 36 A 95 95 0 0 1 244 142"/>
<path d="M 211 198 A 95 95 0 0 1 89 198"/>
<path d="M 56 142 A 95 95 0 0 1 117 36"/>
</g>
<defs><marker id="a8" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b23a1e"/></marker></defs>
''')

# 18b — the dark sea: the machine's dust of names over the uncountable between.
F("dark_sea",
  "Between the One and the Two the machine keeps a fine dust of names — 2^52 of them, evenly spaced. Beneath the dust: an uncountable sea, almost none of it nameable by any tongue or any machine. The grid is honest; the sea does not fit.",
  "0 0 380 150", '''
<line x1="40" y1="62" x2="340" y2="62" stroke="#2a2017" stroke-width="2"/>
<g stroke="#2a2017" stroke-width="2">
<line x1="40" y1="52" x2="40" y2="72"/><line x1="340" y1="52" x2="340" y2="72"/>
</g>
<g font-family="'IBM Plex Mono',monospace" font-size="14" fill="#2a2017" text-anchor="middle">
<text x="40" y="42">1</text><text x="340" y="42">2</text>
</g>
<g stroke="#b23a1e" stroke-width="1.4">
<line x1="58" y1="54" x2="58" y2="62"/><line x1="76" y1="54" x2="76" y2="62"/>
<line x1="94" y1="54" x2="94" y2="62"/><line x1="112" y1="54" x2="112" y2="62"/>
<line x1="130" y1="54" x2="130" y2="62"/><line x1="148" y1="54" x2="148" y2="62"/>
<line x1="166" y1="54" x2="166" y2="62"/><line x1="184" y1="54" x2="184" y2="62"/>
<line x1="202" y1="54" x2="202" y2="62"/><line x1="220" y1="54" x2="220" y2="62"/>
<line x1="238" y1="54" x2="238" y2="62"/><line x1="256" y1="54" x2="256" y2="62"/>
<line x1="274" y1="54" x2="274" y2="62"/><line x1="292" y1="54" x2="292" y2="62"/>
<line x1="310" y1="54" x2="310" y2="62"/><line x1="322" y1="54" x2="322" y2="62"/>
</g>
<text x="190" y="34" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#b23a1e">the machine's dust — 2⁵² names</text>
<rect x="40" y="70" width="300" height="26" fill="#2a2017" opacity="0.87"/>
<text x="190" y="118" text-anchor="middle" font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c">the sea — uncountable, and almost all of it nameless</text>
''')

# 17b — the arrow: few ways to be gathered, absurdly many to be spread.
F("entropy_arrow",
  "Nothing pushes the ink to spread. There are simply more ways to be spread than to be gathered, and the system settles into the face worn by the most ways. The arrow of time is a census, not a force.",
  "0 0 340 165", '''
<g fill="none" stroke="#2a2017" stroke-width="1.8">
<rect x="20" y="22" width="95" height="95"/>
<rect x="225" y="22" width="95" height="95"/>
</g>
<g fill="#b23a1e">
<circle cx="32" cy="105" r="3"/><circle cx="44" cy="98" r="3"/><circle cx="37" cy="91" r="3"/>
<circle cx="52" cy="107" r="3"/><circle cx="58" cy="96" r="3"/><circle cx="30" cy="82" r="3"/>
<circle cx="47" cy="83" r="3"/><circle cx="56" cy="109" r="3"/><circle cx="40" cy="109" r="3"/>
<circle cx="51" cy="92" r="3"/><circle cx="33" cy="96" r="3"/><circle cx="59" cy="85" r="3"/>
</g>
<g fill="#b23a1e">
<circle cx="238" cy="38" r="3"/><circle cx="300" cy="50" r="3"/><circle cx="262" cy="64" r="3"/>
<circle cx="287" cy="87" r="3"/><circle cx="240" cy="93" r="3"/><circle cx="308" cy="106" r="3"/>
<circle cx="255" cy="103" r="3"/><circle cx="297" cy="31" r="3"/><circle cx="271" cy="43" r="3"/>
<circle cx="312" cy="72" r="3"/><circle cx="248" cy="70" r="3"/><circle cx="281" cy="110" r="3"/>
</g>
<line x1="132" y1="62" x2="208" y2="62" stroke="#b23a1e" stroke-width="2.2" marker-end="url(#aarw)"/>
<text x="170" y="50" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#b23a1e">more ways</text>
<text x="170" y="84" text-anchor="middle" font-family="'EB Garamond',serif" font-size="11" font-style="italic" fill="#8a7a62">never forbidden,</text>
<text x="170" y="98" text-anchor="middle" font-family="'EB Garamond',serif" font-size="11" font-style="italic" fill="#8a7a62">only outcounted</text>
<g font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c" text-anchor="middle">
<text x="67" y="140">few ways</text>
<text x="272" y="140">absurdly many ways</text>
</g>
<defs><marker id="aarw" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b23a1e"/></marker></defs>
''')

# 10b — the third body: two close the curve, three never do.
F("three_body",
  "Two bound bodies close their curve and keep every appointment forever. Add a third, and the path never closes again — the first chaos ever seen was seen in the sky.",
  "0 0 320 185", '''
<ellipse cx="80" cy="90" rx="58" ry="38" fill="none" stroke="#2a2017" stroke-width="1.8"/>
<circle cx="124" cy="90" r="5" fill="#b9892f"/>
<circle cx="80" cy="52" r="3.5" fill="#b23a1e"/>
<path d="M 200 60 C 260 40, 292 92, 250 112 C 210 131, 200 82, 235 76 C 277 69, 286 127, 226 137 C 191 143, 196 101, 217 91 C 240 80, 268 52, 296 66" fill="none" stroke="#2a2017" stroke-width="1.6"/>
<circle cx="205" cy="63" r="4.5" fill="#b9892f"/>
<circle cx="253" cy="110" r="4" fill="#b23a1e"/>
<circle cx="228" cy="136" r="4" fill="#2f6f6a"/>
<g font-family="'EB Garamond',serif" font-size="13" fill="#7a6f5c" text-anchor="middle">
<text x="80" y="165">two: the curve closes</text>
<text x="245" y="165">three: it never closes again</text>
</g>
''')

# 2b — the primes: the sieve of the Two and the Three, 6k±1.
F("primes_sieve",
  "Cut away the multiples of the Two and of the Three, and every atom that survives stands next door to a multiple of six — 6k ± 1, forever. The first two atoms are the Two and the Three themselves.",
  "0 0 440 120", '''
<line x1="8" y1="70" x2="432" y2="70" stroke="#2a2017" stroke-width="1.6"/>
<g stroke="#c3b6a0" stroke-width="1.2">
<line x1="14" y1="65" x2="14" y2="75"/><line x1="56" y1="65" x2="56" y2="75"/>
<line x1="112" y1="65" x2="112" y2="75"/><line x1="126" y1="65" x2="126" y2="75"/>
<line x1="140" y1="65" x2="140" y2="75"/><line x1="196" y1="65" x2="196" y2="75"/>
<line x1="210" y1="65" x2="210" y2="75"/><line x1="224" y1="65" x2="224" y2="75"/>
<line x1="280" y1="65" x2="280" y2="75"/><line x1="294" y1="65" x2="294" y2="75"/>
<line x1="308" y1="65" x2="308" y2="75"/><line x1="350" y1="65" x2="350" y2="75"/>
<line x1="364" y1="65" x2="364" y2="75"/><line x1="378" y1="65" x2="378" y2="75"/>
<line x1="392" y1="65" x2="392" y2="75"/>
</g>
<g stroke="#2a2017" stroke-width="1.6">
<line x1="84" y1="60" x2="84" y2="80"/><line x1="168" y1="60" x2="168" y2="80"/>
<line x1="252" y1="60" x2="252" y2="80"/><line x1="336" y1="60" x2="336" y2="80"/>
<line x1="420" y1="60" x2="420" y2="80"/>
</g>
<g font-family="'IBM Plex Mono',monospace" font-size="11" fill="#2a2017" text-anchor="middle">
<text x="84" y="96">6</text><text x="168" y="96">12</text><text x="252" y="96">18</text>
<text x="336" y="96">24</text><text x="420" y="96">30</text>
</g>
<g fill="#b9892f"><circle cx="28" cy="70" r="4.5"/><circle cx="42" cy="70" r="4.5"/></g>
<g fill="#b23a1e">
<circle cx="70" cy="70" r="4.5"/><circle cx="98" cy="70" r="4.5"/>
<circle cx="154" cy="70" r="4.5"/><circle cx="182" cy="70" r="4.5"/>
<circle cx="238" cy="70" r="4.5"/><circle cx="266" cy="70" r="4.5"/>
<circle cx="322" cy="70" r="4.5"/><circle cx="406" cy="70" r="4.5"/>
</g>
<g font-family="'IBM Plex Mono',monospace" font-size="10" text-anchor="middle">
<g fill="#b9892f"><text x="28" y="52">2</text><text x="42" y="52">3</text></g>
<g fill="#b23a1e">
<text x="70" y="52">5</text><text x="98" y="52">7</text>
<text x="154" y="52">11</text><text x="182" y="52">13</text>
<text x="238" y="52">17</text><text x="266" y="52">19</text>
<text x="322" y="52">23</text><text x="406" y="52">29</text>
</g>
</g>
''')

# 21b — the second reader: words as directions, kinship as the angle.
F("second_reader",
  "The engine holds every word as a direction in a space of thousands of rooms. Kinship is the angle between directions: lion lies near cat; the teapot lies near neither. To read is to measure angles — the dot product grown up into a mind.",
  "0 0 320 215", '''
<g stroke="#2a2017" stroke-width="1.8" fill="none" marker-end="url(#a9r)">
<line x1="60" y1="175" x2="232" y2="95"/>
<line x1="60" y1="175" x2="186" y2="69"/>
<line x1="60" y1="175" x2="21" y2="30"/>
</g>
<path d="M 123.4 145.4 A 70 70 0 0 0 113.6 130" fill="none" stroke="#b23a1e" stroke-width="1.6"/>
<g font-family="'EB Garamond',serif" font-size="14" fill="#2a2017">
<text x="238" y="98">cat</text>
<text x="191" y="66">lion</text>
<text x="14" y="22">teapot</text>
</g>
<text x="136" y="130" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#b23a1e">θ</text>
<text x="160" y="205" font-family="'IBM Plex Mono',monospace" font-size="11.5" fill="#6a5d49" text-anchor="middle">cat·lion ≫ 0      cat·teapot ≈ 0</text>
<circle cx="60" cy="175" r="3" fill="#b23a1e"/>
<defs><marker id="a9r" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#2a2017"/></marker></defs>
''')

# 22 — e, the hinge: the irrational numbers around the sacred integers.
F("e_hinge",
  "The hinge lives between the Two and the Three. e ≈ 2.718 sits just below the Three; π ≈ 3.1416 just past it — the two transcendental numbers from which growth and roundness are built.",
  "0 0 440 150", '''
<line x1="40" y1="95" x2="410" y2="95" stroke="#2a2017" stroke-width="1.6"/>
<g stroke="#2a2017" stroke-width="1.6">
<line x1="70" y1="88" x2="70" y2="102"/>
<line x1="337" y1="88" x2="337" y2="102"/>
</g>
<g stroke="#b23a1e" stroke-width="2">
<line x1="261" y1="86" x2="261" y2="104"/>
<line x1="374" y1="86" x2="374" y2="104"/>
</g>
<g font-family="'IBM Plex Mono',monospace" fill="#2a2017">
<text x="70" y="124" text-anchor="middle" font-size="14">2</text>
<text x="337" y="124" text-anchor="middle" font-size="14">3</text>
</g>
<g font-family="'IBM Plex Mono',monospace" fill="#b23a1e">
<text x="261" y="124" text-anchor="middle" font-size="14">e</text>
<text x="374" y="124" text-anchor="middle" font-size="14">&#960;</text>
<text x="261" y="78" text-anchor="middle" font-size="9.5">2.718&#8230;</text>
<text x="380" y="78" text-anchor="middle" font-size="9.5">3.1416&#8230;</text>
</g>
<text x="225" y="146" text-anchor="middle" font-family="'EB Garamond',serif" font-size="12" fill="#7a6f5c">the two irrational hinges</text>
''')

# 23 — The Ouroboros: e^(iθ) closes on itself; the serpent eats its tail.
F("ouroboros",
  "Turn growth the whole way round and it returns: e^(i(θ+2π)) = e^(iθ). The exponent climbs forever, yet the path has no end and no seam — growth that has learned to come home.",
  "0 0 240 240", '''
<path d="M 138 40 A 84 84 0 1 1 104 41" fill="none" stroke="#4a5d36" stroke-width="15" stroke-linecap="round"/>
<path d="M 116 45 A 84 84 0 0 0 96 58" fill="none" stroke="#3a4a2a" stroke-width="3" opacity="0.5"/>
<g stroke="#ece1cd" stroke-width="1.5" opacity="0.55">
<line x1="200" y1="92" x2="208" y2="86"/><line x1="180" y1="200" x2="186" y2="208"/>
<line x1="56" y1="150" x2="48" y2="156"/><line x1="120" y1="206" x2="120" y2="215"/>
</g>
<!-- tail tapering toward the mouth -->
<path d="M 104 41 L 122 36 L 132 44 Z" fill="#3a4a2a"/>
<!-- head, biting -->
<path d="M 138 28 Q 158 30 158 44 Q 158 58 138 56 L 121 44 Z" fill="#4a5d36"/>
<circle cx="146" cy="40" r="2.6" fill="#ece1cd"/>
<path d="M 121 44 L 110 40 M 121 44 L 110 48" stroke="#b23a1e" stroke-width="1.3" fill="none"/>
<!-- direction of travel -->
<path d="M 196 150 l 8 5 l -9 4" fill="none" stroke="#b9892f" stroke-width="1.8"/>
<g text-anchor="middle" fill="#2a2017">
<text x="120" y="118" font-family="'IBM Plex Mono',monospace" font-size="15">e^(i&#952;)</text>
<text x="120" y="142" font-family="'IBM Plex Mono',monospace" font-size="12" fill="#7a6f5c">&#952; + 2&#960; = &#952;</text>
</g>
''')

# 24 — Holonomy: parallel transport around a closed loop returns you rotated.
F("holonomy",
  "Carry a vector around a closed loop on a curved surface and it comes home rotated, though each step seemed only to bring it back. The falling cat, the qubit's phase, and the serpent are one holonomy.",
  "0 0 250 230", '''
<circle cx="120" cy="115" r="86" fill="none" stroke="#2a2017" stroke-width="1.8"/>
<ellipse cx="120" cy="115" rx="86" ry="26" fill="none" stroke="#c3b6a0" stroke-width="1"/>
<!-- the closed loop (a spherical triangle) -->
<path d="M 120 36 Q 92 92 68 150 Q 120 170 172 150 Q 148 92 120 36 Z"
  fill="none" stroke="#2f6f6a" stroke-width="2.4"/>
<g fill="#2a2017"><circle cx="120" cy="36" r="3.2"/><circle cx="172" cy="150" r="3.2"/><circle cx="68" cy="150" r="4.2"/></g>
<!-- start vector (solid) and returned vector (rotated, dashed) at the base vertex -->
<line x1="68" y1="150" x2="66" y2="120" stroke="#b23a1e" stroke-width="2.4" marker-end="url(#ah1)"/>
<line x1="68" y1="150" x2="92" y2="132" stroke="#b9892f" stroke-width="2.2" stroke-dasharray="4 3" marker-end="url(#ah2)"/>
<path d="M 66 124 A 26 26 0 0 1 88 130" fill="none" stroke="#2a2017" stroke-width="1.1"/>
<text x="92" y="116" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#2a2017">&#916;&#952;</text>
<defs>
<marker id="ah1" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b23a1e"/></marker>
<marker id="ah2" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b9892f"/></marker>
</defs>
<text x="120" y="222" text-anchor="middle" font-family="'EB Garamond',serif" font-size="12" fill="#7a6f5c">the angle returned = the curvature enclosed</text>
''')

# 25 — The Nesting: wrap a sphere in its cube, that cube in its sphere, forever;
#      each shell scales every length by √d (shown in the plane, where it is √2).
F("nesting",
  "Wrap a sphere in its cube, that cube in its sphere, and repeat. Each shell multiplies every length by √d, the cube's diagonal — √2 in the plane (shown), √3 in space, exactly 2 in the fourth dimension.",
  "0 0 280 280", '''
<g fill="none">
<rect x="112" y="112" width="56" height="56" stroke="#2a2017" stroke-width="1.6"/>
<circle cx="140" cy="140" r="39.6" stroke="#b23a1e" stroke-width="1.6"/>
<rect x="100.4" y="100.4" width="79.2" height="79.2" stroke="#2a2017" stroke-width="1.6"/>
<circle cx="140" cy="140" r="56" stroke="#b23a1e" stroke-width="1.6"/>
<rect x="84" y="84" width="112" height="112" stroke="#2a2017" stroke-width="1.8"/>
<circle cx="140" cy="140" r="79.2" stroke="#b23a1e" stroke-width="1.8"/>
</g>
<circle cx="140" cy="140" r="3" fill="#2a2017"/>
<line x1="140" y1="140" x2="195" y2="85" stroke="#b9892f" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#an)"/>
<defs><marker id="an" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#b9892f"/></marker></defs>
<text x="170" y="104" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#b9892f">&#215; &#8730;d</text>
''')
