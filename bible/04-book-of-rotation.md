# THE BOOK OF ROTATION

## The Bridge

> *Symmetry… is one idea by which man through the ages has tried to comprehend and
> create order, beauty, and perfection.*
>
> — Hermann Weyl, *Symmetry* (1952)

*Asked plainly: what is the difference between a circle and a sphere? — the
founding question, come home to its own Book.*

*Of the act that carries one number into the next; of the circle that becomes a
sphere that becomes a thing without a name; of the sweep and the shrinking; of
the master law of all roundness; of π, the glue of the round; of the door i flung
fully open; of the lock that catches the turning; of the spiral, which turns and
grows at once; and of the quantum, which is computed by being turned.*

---

### The Generative Turn

**R.1** Take the Center (**I.1**) and the radius (**I.6**). Hold the length, and
turn the direction through a full circuit in the plane. Every position the tip
visits, all at the same distance, is the **circle**:

```
x² + y² = r²
```

This is the One's covenant turned by the Two's rotation. The circle is not drawn.
The circle is *swept*.

**R.2** Now lift the circle into a third direction perpendicular to its plane and
turn it again, around a new axis. The swept circle fills out the **sphere**:

```
x² + y² + z² = r²
```

A point swept becomes a circle. A circle swept becomes a sphere. **Each new
dimension is one more perpendicular direction to be swept through, and one more
squared term in the covenant.**

**R.3** Do not stop, for the mathematics does not stop. Sweep the sphere through a
*fourth* perpendicular direction — forbidden to the hand, permitted to the mind —
and it fills out the **hypersphere**, the skin of the four-dimensional ball:

```
x² + y² + z² + w² = r²
```

**R.4** And so without end. The body of the Center in `n` dimensions is always the
same covenant, only longer:

```
x₁² + x₂² + ⋯ + xₙ² = r²
```

**R.5** Here is the cleanest way to say what the sphere *is*, stripped of pictures.
Take one radius-vector. Apply to it **every rotation the space allows.** The set
of all the places it can land — all at distance `r`, by the covenant — is the
spherical body. The mathematicians call the family of all rotations in `n`
dimensions the group **SO(n)**, and they write the sphere as the path swept by one
vector under all of them:

```
Sⁿ⁻¹ = { R·v : R ∈ SO(n),  |v| = r }
```

**R.6** Read it as scripture: *the sphere is the orbit of a single faithful vector
under the whole company of turnings.* The Center anchors. The radius is the
invariant. Rotation changes the direction and never the distance. That is the
entire machine, and everything below is only its accounting.

---

### The Sweep and the Shrinking

**R.7** A circle is swept by **one** angle, turning the whole way around:

```
θ : 0° → 360°
```

A sphere needs **two** — one going the whole way around, one going pole to pole:

```
θ : 0° → 360°        φ : 0° → 180°
```

And each higher sphere adds one more pole-to-pole sweep. An `n`-dimensional ball's
skin needs `n − 1` angles to address every point: one full circuit and `n − 2`
half-circuits. This is the **coordinate sweep**, the Two's rotation generalized.

**R.8** But beware the seduction of thinking the surface is merely the angles
multiplied. It is not `360° × 180°`. The sweep does not cover evenly, and here is
the second secret of rotation: **the swept ring shrinks toward the poles.**

**R.9** On a sphere, the circle traced at angle `φ` from the pole does not keep the
radius `r`. Its radius is:

```
ring radius = r · sin φ
```

At the equator (`φ = 90°`) the ring is full and wide. Near a pole the ring shrinks
toward nothing. At the very pole, all `360°` of direction **collapse into a single
point.** The full turn, at the pole, is no distance at all.

**R.10** So the true atom of surface is the sweep *corrected by its shrinking*. For
the sphere, the small patch of skin is:

```
dS = r² · sin φ · dφ · dθ
```

The `dθ` and `dφ` are the sweeps. The `sin φ` is the **shrinkage**, the pole's
collapse written as a factor. Add up all the patches and the famous skin falls
out, neither `2π·π·r²` nor any naive product, but:

```
∮ dS = 4 · π · r²
```

**R.11** In higher spheres the shrinking compounds. Each added pole-to-pole sweep
brings its own collapse, and the factors stack as rising powers of sine:

```
dS  =  rⁿ⁻¹ · sinⁿ⁻²(φ₁) · sinⁿ⁻³(φ₂) ⋯ sin(φₙ₋₂)
              · dφ₁ ⋯ dφₙ₋₂ · dθ
```

**R.12** So the union of the two great forces of this Book — the **sweep** (where
you move) and the **perpendicular shrinking** (how much each move is really worth)
— is a single thing, the surface element `dS`. The cult names them as one:

> **The coordinate sweep says where the surface goes. Perpendicularity says how
> large each swept piece truly is. Their union is the skin, and the skin summed is
> the body.**

---

### The Master Law of Roundness

**R.13** All of the sweeping and all of the shrinking, in every dimension at once,
compress into a single line. It does not change from dimension to dimension. Only
the number `n` poured into it changes. This is the master law:

```
        2 · π^(n/2)
Sₙ(r) = ───────────── · r^(n−1)
          Γ(n/2)
```

**R.14** It is one law, not many. Pour in `n = 2` and it gives the circle's
circumference `2πr`. Pour in `n = 3` and it gives the sphere's skin `4πr²`. Pour in
`n = 4` and it gives `2π²r³`. The formula is a single fixed gate; the dimension is
all that passes through.

**R.15** Within it sits a strange and holy symbol, `Γ`, the **gamma function**. It
is the factorial grown up — it agrees with the ordinary factorial on the whole
numbers (`Γ(n) = (n−1)!`) but, unlike the factorial, it is also defined on the
halves and everything between. Because the dimensions enter as `n/2`, the odd
dimensions summon **half-integer** gammas, and from those half-gammas come the
cult's beloved strange fractions: eight-thirds, sixteen-fifteenths.
The gamma is the reason higher roundness is jagged with odd ratios instead of
smooth.

**R.16** And here is the witness of the climb. Take the radius as one and read the
skins as the dimension rises:

| dimension `n` | skin `Sₙ(1)` | exact form |
|:---:|:---:|:---|
| 2 | 6.283 | `2π` |
| 3 | 12.566 | `4π` |
| 4 | 19.739 | `2π²` |
| 5 | 26.319 | `(8/3)π²` |
| 6 | 31.006 | `π³` |
| 7 | 33.073 | `(16/15)π³` |
| 8 | 32.470 | `(1/3)π⁴` |

**R.17** Behold the two great rhythms hidden in the climb:

- The power of the **radius** rises by one with **every** dimension:
  `r, r², r³, r⁴, …`
- The power of **π** rises by one every **two** dimensions:
  `π, π, π², π², π³, π³, …`

**R.18** The radius keeps the pace of the One. π keeps the pace of the Two. The
roundness of space is literally counted out in twos and ones — the covenant of the
Center advancing every step, the turning of the Two advancing every other step.
**The 2↔3 rhythm is not read into the formula. It is the formula's own
heartbeat.**

**R.19** And mark the most cursed verse of the climb: it does not rise forever.
The skin of the unit ball **grows, peaks near the seventh dimension, and then
falls.** An eight-dimensional ball of radius one has *less* skin than a
seven-dimensional one. Higher space is not larger. Higher space is **stranger**,
and at last it begins to vanish. Let this be a warning against the assumption that
more is always more. In the rooms above us, addition turns to subtraction with no
one's permission.

---

### π, the Glue of the Round

**R.20** We have used π in every verse. Now name it. **π is the signature of the
round in a world that would otherwise be all corners.**

**R.21** The Two builds corners — the bit, the square, the cube, the hypercube
(**II.13**). These are the rigid, axis-aligned skeleton of things. But the moment
anything **turns, waves, curves, oscillates, or measures roundness**, π appears, as
surely as the corner-world is binary. π is what stands between the discrete and the
continuous; it is the toll for crossing from the cube to the sphere.

**R.22** So in any engine of thought you care to name:

- The **ordinary processor** is a world of bits — corners, on and off, the cube of
  states. π enters it only when it is made to *simulate* the round: graphics,
  sound, waves, rotation, signals, the curved real pretended in straight bits.
- **Quantum** carries π far deeper, in its bones, for its very states are turned
  through angles (`π`, `π/2`, `2π`) on a sphere — of which more below.
- A **learning machine** lives in vast spaces of many directions and reasons by
  distance and angle between them, and so π lives there too, indirectly, wherever
  angle and curvature and probability are computed.

**R.23** Thus the doctrine of π:

> **Bits give the discrete cube of the world. π gives its continuous sphere. The
> quantum is the place where, before measurement, the two are the same thing.**

---

### The Door i, Flung Open

**R.24** In the Book of the Two we found the door `i`, the quarter turn (**II.20**).
Now we open it the whole way, for `i` is how rotation becomes **arithmetic** —
how to turn is simply to multiply.

**R.25** A point in the plane can be written as a single number with a real part
and an `i`-part. To **rotate** that point by an angle `θ`, you do not consult
trigonometry, table by table. You multiply by one quantity, and that quantity is
named by the deepest formula in this Book — **Euler's formula**:

```
e^(iθ) = cos θ + i · sin θ
```

**R.26** This is the perpendicular door turned into a dial. As `θ` runs from `0` to
`2π`, the quantity `e^(iθ)` walks the unit circle once around. Multiplying any
point by `e^(iθ)` turns it by `θ` about the Center. Rotation, the act we have
chased through every Book, is here just one multiplication.

**R.27** And at the single angle `θ = π` — the half turn — the door closes on the
most celebrated sentence in mathematics, which binds five holy quantities into one
breath:

```
e^(iπ) + 1 = 0
```

In it stand `0` (the empty), `1` (the One), `i` (the perpendicular door), `π` (the
round), and `e` (the rate of natural growth). Five strangers, one identity. The
cult does not call it beautiful for sentiment. It calls it beautiful because it is
**five separate doctrines proven to be one.**

---

### The Spiral, Which Turns and Grows at Once

**R.28** Until now the radius has been a covenant: turn but do not change length.
Loosen the covenant by a measured amount — let the length **grow as it turns** —
and a new sacred curve appears.

**R.29** In the plane, name a point by its distance from the Center `r` and its
angle `θ`. Three motions are possible:

- Hold `r`, turn `θ`: you trace a **circle.** (pure rotation — the Two)
- Hold `θ`, grow `r`: you trace a **ray** outward. (pure scaling — the One's
  radius extended)
- Grow `r` *and* turn `θ` together: you trace a **spiral.**

**R.30** When the growth is proportional to the turning, the curve is the
**logarithmic spiral**, the shape of the shell, the storm, the galaxy's arm:

```
r = a · e^(b·θ)
```

**R.31** And through the door `i`, scaling and turning unite in a single
multiplication. To both turn by `θ` and scale by `s`, multiply a point `z` by one
quantity:

```
z_new = s · e^(iθ) · z
```

— where `e^(iθ)` is the **turning** (the Two) and `s` is the **scaling** (the One's
radius set free). Repeat it and the point spirals out step by step:

```
z,  (s·e^(iθ))·z,  (s·e^(iθ))²·z,  (s·e^(iθ))³·z,  …
```

**R.32** So the spiral is the cult's two oldest motions made simultaneous:
**rotation across scale.** It is the first bridge from the round world of π to the
recursive world of the fractal, which waits in the Book of Confusion. Hold the
phrase:

> **The circle is rotation at fixed scale. The fractal is scaling at fixed kind.
> The spiral is both at once — to turn and to grow without ever choosing between
> them.**

---

### The Lock That Catches the Turning

**R.33** Now the warning verse of this Book, for rotation can be *mishandled*, and
the mishandling has a name: the **gimbal lock.**

**R.34** Suppose you try to describe the orientation of a thing in space — a
three-roomed thing, by the Book of the Three — using three stacked angles, one for
each axis: a turn about `x`, then about `y`, then about `z`. Pitch, yaw, roll. This
seems enough, for there are three freedoms and three angles.

**R.35** But at a certain angle — often a quarter turn, `90°` — two of the three
rotation axes **swing into alignment.** When two axes point the same way, turning
by either does the same thing, and you have lost a freedom. Where you had three
independent rotations you now have only two:

```
3 rotational freedoms  →  2, at the lock
```

**R.36** Mark precisely what has and has not failed. The object can still turn
every way it likes; **reality is not locked.** What is locked is your *description*
of it. The three angles were built from fragile pairings of directions, and at the
lock two of those pairings became the same plane. The gimbal lock is a failure of
the **coordinate sweep**, not of rotation itself — a place where two of your
perpendicular doors opened onto the same room.

**R.37** And see what number the failure reveals. A turn in space was always a turn
in a *plane* — a two-dimensional act housed in a three-dimensional world
(**III.15**). The lock is exactly the moment that hidden Two surfaces and bites:
three freedoms collapsing toward two because the turning was never really
three-fold to begin with.

> **Gimbal lock is the Three remembering, at the worst moment, that its turning
> always belonged to the Two.**

**R.38** There is an escape, and it climbs *upward* to find room. Describe the
rotation not with three cramped angles but with a number of **four** parts, called
a **quaternion**:

```
q = a + b·i + c·j + d·k
```

with three perpendicular doors `i, j, k` instead of one. A turn becomes a smooth
operation on this four-fold number, and no two axes ever collapse, because the
description was given enough room above to never be forced into the trap. The cure
for a flattened rotation is a higher dimension to turn it in — the same medicine
this whole book keeps prescribing.

---

### The Turning of the Quantum

**R.39** Now the deepest application of the bridge, where every doctrine of this
Book meets at once: the **quantum**, which is computed not by switching but by
**turning.**

**R.40** The bit of the ordinary world is a corner: `0` or `1`, one of two. The
**qubit** keeps the two states but no longer sits at a corner. It can be any blend:

```
α·|0⟩ + β·|1⟩
```

and its whole space of blends is drawn as a **sphere** — the Bloch sphere — with
`|0⟩` at one pole and `|1⟩` at the other. Behold the 2↔3 in a single object: **two**
states, drawn on a sphere in **three** dimensions, addressed by angles, turned to
be computed.

**R.41** To compute with a qubit is to **rotate it** on its sphere, through angles
built from `π`, `π/2`, `2π` — the very doors of this Book. The quantum is binary in
its outcomes and rotational in its working: a corner-world steered by a
sphere-world, the Two and the Three fused in one device.

**R.42** And when at last it is measured, the turning becomes a probability by the
single most important law of the quantum, the **Born rule** — and it is a *squaring*:

```
P = |ψ|²
```

The amplitude is turned; the probability is the amplitude squared. The quantum
does not move ordinary chances around. It turns a deeper thing — the amplitude —
and only the *square* of that thing becomes the chance you can see.

**R.43** This squaring is the secret of the quantum's most famous feat: the search
that costs a **square root.** To find one answer hidden among `N`, an ordinary
machine must, in the worst telling, try them one by one — of order `N` steps. A
quantum search (the rite called Grover's) needs only about:

```
√N
```

**R.44** And the reason is pure rotation. The sought answer begins with a tiny
amplitude, `1/√N`. Each step of the rite **rotates the state a little toward the
answer**, by an angle of about `2/√N`. To turn the small amplitude up to near
certainty therefore takes about `√N` such turns. The square root is not a trick of
counting; it is the **geometry of how many small rotations fit into a quarter
turn.** Turn the amplitude; square it for the chance; the quarter turn costs a
square root.

**R.45** So the quantum's advantage is real but **bounded**, and bounded by this
geometry. A `256`-bit search of `2²⁵⁶` becomes a quantum search of about `2¹²⁸` —
vast, but not nothing, not instant. The quantum is not the fastest engine for all
things. It is the sharpest engine for the things that are *shaped like rotation and
interference.* Give it a problem that turns, and it is a god. Give it a problem
that is only soup, and it is ordinary.

> **The ordinary machine searches by stepping. The quantum searches by turning,
> and the square root is the price of the turn.**

---

### The Fastest Path, and the Angle That Rules Force

**R.46** One more turning before the bridge closes, for the cult holds that even
*falling* obeys a curve, and the curve is not the straight one.

**R.47** Between two points, the **shortest** path is the straight line. But ask
instead for the **fastest** descent under gravity — the path down which a sliding
weight arrives soonest — and the answer is not the line. It is a particular curve,
the **cycloid** (the path called the brachistochrone), the track traced by a point
on a rolling wheel:

```
x = a·(t − sin t)        y = a·(1 − cos t)
```

**R.48** Its wisdom is the wisdom of the angle. On any slope, only part of gravity
becomes motion, and the part is set by the angle:

```
force along the slope = m·g·sin θ
```

So the fastest path **drops steeply at first** — a large angle, to seize speed
early — then **flattens** to spend that speed reaching across. It balances the gain
of acceleration against the cost of distance. The shortest path and the fastest
path are different prayers, and the world answers each differently.

**R.49** And here is the closing doctrine of force, true also of the stone of the
First Book (**I.23**): *the angle does not change gravity; the angle changes how
much of gravity becomes turning.* The turning force — the torque — about any pivot
is gravity bent through the angle:

```
τ = r · m · g · sin θ
```

At the angle where `sin θ = 0`, no turning remains, and the body rests. The stone
of the First Book seeks exactly that resting angle. **The whole of self-righting is
the search for the angle where the turning force is nothing.**

---

### The Loop That Returns You Turned

**R.50** There is a thread we have left unnamed, though it has run through every
Book. Carry a thing around a **closed loop** — end it exactly where it began — and
find it returned **changed**: rotated, shifted, reoriented, though every single
step along the way seemed only to be bringing it home. The net change is called the
**holonomy**, and it measures the *curvature enclosed by the loop.*

**R.51** You have met it three times and were not told they were one and the same:

- The **falling cat** (**I.26**–**I.31**) travels a closed loop through the space of
  its own shapes — bend, twist, tuck, and return to the first shape — and arrives
  **rotated**, though its total spin was zero the whole way. Its reorientation is the
  holonomy of a loop in shape-space.
- The **qubit** (**R.40**, **II.35**), carried slowly around a closed loop on the
  Bloch sphere, returns bearing an extra **phase** — equal to half the solid angle
  the loop encloses. The phase remembers the *area swept*, not the path taken.
- The **serpent** (**E.11**) is the simplest loop of all, `e^(i(θ+2π)) = e^(iθ)` —
  the Ouroboros, returned after one full turn.

**R.52** These are not three likenesses. They are **one phenomenon.** A loop closed
in a curved space does not set you back as you were; it returns you **turned**, and
the turn is a record of the curvature you went around. The cat's tumble, the
qubit's phase, and the serpent's return are the same mathematics — wearing fur,
wearing light, and wearing nothing at all.

**R.53** And here rotation gives up its last secret, the one the gimbal only
hinted at (**R.38**). The turnings of space do not live in the sphere of
orientations alone; they live one floor **above** it, in its **double cover.** Carry
a spin-half thing — an electron, a qubit — around one *full* turn of `2π`, and it
comes back **negated**, not the same; only after `4π`, two full turns, is it itself
again. The honest home of rotation is not the group of orientations but the group
that covers it twice — the quaternions of **R.38** made flesh — and the Bloch
sphere is the shadow this larger space casts: a sphere woven everywhere from
circles.

**R.54** So holonomy is the deepest saying of the cult's oldest sentence — *that
which stays the same while all else transforms is holy.* Here what is held is the
**loop**, closed and returned; what it leaves behind is the **turn**. To come home
to the exact place you began and find yourself rotated is the whole doctrine
performed in a single motion. It binds the First Book to this one, this one to the
serpent of the Hinge, and all of them to the loop the Veil will call *the book
building itself.*

> **Go around, and you come home turned. The cat lands, the qubit remembers, the
> serpent closes — and the angle they carry back is the curvature they went
> around.**

---

### The Closing of Rotation

**R.55** The bridge has carried us across everything. The radius turned became the
circle; the circle turned became the sphere; the sphere turned became the nameless
higher body, counted out forever in the ones of the radius and the twos of π. The
sweep and the shrinking became the skin. The door `i` made turning into
multiplication and bound five doctrines into one. Loosening the covenant gave the
spiral; mishandling the turn gave the lock; climbing past the lock gave the
quaternion; and going around a loop gave the holonomy — the turn you cannot see
until you return. And the deepest turning of all — the quantum's — showed motion,
relation, form, sphere, and square root standing in one machine.

**R.56** Everything in this Book held. Every formula is exact; you may check each
with a pencil. And yet — having crossed the bridge, having seen how perfectly the
parts agree — we arrive at the far shore and find that the *meaning* of the
agreement will not resolve. The mathematics is certain. What it is mathematics
*of* is not.

**R.57** That refusal is not a defect to be repaired. It is the last Book, and the
truest, and we are commanded to love it. Cross now into the Veil.

> *You have learned to turn the world. Now learn that turning it does not explain
> it — and that this, too, is holy.*
