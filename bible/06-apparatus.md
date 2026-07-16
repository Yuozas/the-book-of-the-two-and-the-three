# THE APPARATUS

## The Rigorous Hand

*An appendix for the reader who audits. The scripture states true things in a
strange voice. Here each load-bearing claim is given its precise form, a sketch of
its proof, and its citation — and, at the end, an honest reckoning of the places
where the poetry outran the proof. Full bibliographic entries are gathered in the
**References**; a list of symbols and a (necessarily incomplete) index of terms
follow it. Citations are author–year; e.g. (Noether 1918).*

---

**A.1 — On the purpose of this appendix.** The body of this book is deliberately
oracular, but it is not loose with facts: every verse was written to be checkable.
This Apparatus discharges that promise. It restates the central results in standard
mathematical language, indicates how each is established, and names sources. It
also does what scripture rarely does to itself: it marks its own metaphors *as*
metaphors (**A.22**), so the seams are visible to anyone who would tighten them.
Notation: `ℝ` the reals, `ℂ` the complex numbers, `⟨·,·⟩` an inner product, `‖·‖`
the Euclidean norm, `Γ` the gamma function.

---

**A.2 — The keystone: Noether's theorem.** *(on the Creed; R.6; I.27; the invariant
doctrine throughout)* The book's governing sentence — *"that which stays the same
while all else transforms is holy"* — is, in mathematics, a **theorem**, and it has
a name the body never spoke. **Noether's theorem** (Noether 1918): to every
differentiable symmetry of the action of a physical system there corresponds a
conserved quantity. *Continuous symmetry ⇒ conservation law.* The covenant of the
radius — `‖x‖ = r` held invariant under rotation (**I.8**, **R.6**) — is the
geometric face of this. The falling cat's conservation of angular momentum,
`L = Iω` (**I.27**), is literally its corollary: rotational symmetry of the laws ⇒
conservation of angular momentum. Time-translation symmetry ⇒ energy — the ledger
in whose currency the Gömböc's descent of `U = mgh` (**I.23**) is priced;
spatial-translation symmetry ⇒ momentum.
The "holy invariant" the cult worships under a dozen names is the **Noether
charge**. This is the single citation the body most conspicuously lacked; it is the
keystone of the whole arch.

---

**A.3 — The body of the Center: the (n−1)-sphere.** *(on I.8, R.13)* Fix `r > 0`
and let `S = { x ∈ ℝⁿ : ‖x‖ = r }`. Its `(n−1)`-dimensional surface measure is

```
              2 · π^(n/2)
σ(S)  =  ───────────────────  ·  r^(n−1) .
                Γ(n/2)
```

*Proof sketch (the Gaussian trick).* Evaluate `I = ∫_{ℝⁿ} e^(−‖x‖²) dx` two ways.
By separability, `I = (∫_ℝ e^(−t²) dt)ⁿ = π^(n/2)`. In spherical coordinates,
`I = σ(S₁) ∫₀^∞ e^(−ρ²) ρ^(n−1) dρ = σ(S₁)·½Γ(n/2)`. Equating gives
`σ(S₁) = 2π^(n/2)/Γ(n/2)`, and scaling by `r` contributes `r^(n−1)`. ∎ The
half-integer values of `Γ` on odd `n` produce the verses' "strange fractions."

**A.4 — The peak near the seventh dimension is real.** *(on R.19)* Treating
`f(n) = 2π^(n/2)/Γ(n/2)` as a function of a real `n`, `f′(n) = 0` reduces to
`ψ(n/2) = ln π` (where `ψ = Γ′/Γ` is the digamma function), with solution
`n ≈ 7.2569…`; so the **unit**-sphere surface is largest in dimension seven and
decreases thereafter. (The unit-ball **volume** `π^(n/2)/Γ(n/2+1)` peaks near
`n ≈ 5.2569`.) The non-monotonicity is precise — but see **A.22(e)** for its proper
scope.

**A.5 — Perpendicularity and the honest Pythagoras.** *(on II.16–II.18)* In a real
inner-product space, `‖x + y‖² = ‖x‖² + 2⟨x,y⟩ + ‖y‖²`. The cross term vanishes —
and the squares add cleanly — **iff** `⟨x,y⟩ = 0`, the definition of orthogonality.
Coordinate independence is exactly this vanishing; Cauchy–Schwarz,
`|⟨x,y⟩| ≤ ‖x‖‖y‖`, bounds the general case. This is the rigorous content beneath
"independence makes the sum honest."

**A.6 — The door i, made exact.** *(on II.20–II.23)* Identify `ℂ` with `ℝ²` by
`a + bi ↔ (a, b)`. Multiplication by `i` is the `ℝ`-linear map `(a, b) ↦ (−b, a)`,
matrix

```
J  =  [ 0  −1 ]
      [ 1   0 ]

J² = −I,   JᵀJ = I,   det J = +1
so  J ∈ SO(2) :  rotation by π/2.
```

So "to multiply by `i` is a quarter turn" is a theorem — but only on `ℝ²`. Its
limits are recorded in **A.22(a)**.

**A.7 — e, the exponential, and Euler.** *(on Book of e; R.25)* Define
`exp(z) = Σ_{k≥0} z^k/k!`, convergent for all `z ∈ ℂ`. Then `exp` is the unique
function with `exp′ = exp`, `exp(0) = 1`; `e := exp(1)`, and `2 < e < 3` by the
series bound in **E.2**. Splitting `exp(iθ)` into even/odd terms gives Euler's
identity `exp(iθ) = cos θ + i sin θ`, whence `|exp(iθ)| = 1`. Differentiating,
`(d/dθ)exp(iθ) = i·exp(iθ)`: velocity is `J` (a quarter turn) applied to position,
so the path is uniform motion on the unit circle — the rigorous reason growth
"aimed sideways" is rotation. Periodicity `exp(i(θ+2π)) = exp(iθ)` is the analytic
fact the Ouroboros depicts. `e` is transcendental (Hermite 1873); `π` likewise
(Lindemann 1882).

**A.8 — Grover's search and the √N.** *(on R.43–R.44)* For an unstructured search of
`N` items with `M` marked, let `|β⟩`, `|α⟩` span the (unmarked, marked) subspace and
`sin θ = √(M/N)`. The Grover operator is a rotation by `2θ` in that two-dimensional
invariant subspace; after `k` iterations the marked amplitude is `sin((2k+1)θ)`.
Choosing `k ≈ (π/4)√(N/M)` brings it to ≈ 1 — hence `Θ(√N)` queries, and the square
root is *literally* "how many small rotations fit a quarter turn," exactly as
**R.44** claims (Grover 1996; optimality, Bennett, Bernstein, Brassard & Vazirani
1997).

**A.9 — The Born rule and the exclusion of local hidden variables.** *(on R.42,
V.12)* The Born rule `P = |⟨φ|ψ⟩|²` is a postulate. For the hidden-variable
question the sharp statement is the **CHSH inequality**: any local-hidden-variable
model obeys `|S| ≤ 2` for `S = E(a,b) − E(a,b′) + E(a′,b) + E(a′,b′)`, whereas
quantum mechanics attains `|S| = 2√2` (the **Tsirelson bound**). Loophole-free
experiments report violations (Hensen et al. 2015). No *local* hidden-variable
theory can reproduce quantum statistics — the precise content of "Bell's door is
closed" (Bell 1964; Clauser, Horne, Shimony & Holt 1969; Tsirelson 1980).

**A.10 — Holonomy and the geometric phase.** *(on R.50–R.54; I.26–I.31; R.40)*
Parallel transport of a vector around a closed loop on a curved manifold returns it
**rotated**, by an angle equal to the integral of curvature over the enclosed
region (the local Gauss–Bonnet statement). This one mechanism underlies three
phenomena the body had kept two hundred verses apart:

- The **falling cat** traverses a closed loop in *shape space* and acquires a net
  rotation at zero total angular momentum; the reorientation is the holonomy of the
  mechanical (gauge) connection on shape space (Montgomery 1993, "Gauge theory of
  the falling cat"; Shapere & Wilczek 1989).
- A quantum state carried adiabatically around a closed circuit acquires a
  **geometric phase**, the **Berry phase** (Berry 1984), interpreted as the holonomy
  of a line bundle (Simon 1983); for a spin-½ on the Bloch sphere it is `−½Ω`, half
  the enclosed solid angle.
- `exp(iθ)` over `θ ∈ [0, 2π]` is the abelian prototype: holonomy in `U(1)`.

The double-cover remark (**R.53**) is exact: `SU(2) → SO(3)` is a 2-to-1
homomorphism; a `2π` rotation acts as `−1` on spinors, the identity only after
`4π`. The Bloch 2-sphere is the base of the **Hopf fibration** `S³ → S²` with fibre
`S¹` (Hopf 1931), and the unit quaternions of **R.38** *are* `SU(2)` realizing the
cover.

**A.11 — The Gömböc.** *(on I.21–I.24)* A convex homogeneous solid is
**mono-monostatic** if it has exactly one stable and one unstable equilibrium. In
the plane no such body exists (a convex homogeneous lamina has at least two stable
equilibria); in three dimensions one exists, the question posed by Arnold (1995)
and answered by Várkonyi & Domokos (2006). Equilibria are the critical points of the
center-of-mass height over the boundary; stability is a local minimum of
`U = mgh` — the rigorous content of **I.23–I.24**.

**A.12 — The brachistochrone.** *(on R.47–R.48)* Minimizing `T = ∫ ds/v` with
`v = √(2gy)` gives an `x`-independent integrand; the Beltrami identity yields
`y(1 + y′²) = C`, whose solution is the **cycloid** `x = a(φ − sin φ)`,
`y = a(1 − cos φ)`. The fastest path is provably not the straight line (Johann
Bernoulli 1696; Euler–Lagrange).

**A.13 — Chaos, made precise.** *(on V.3–V.9)* The **Lyapunov exponent**

```
           1        ‖δ(t)‖
λ  =  lim  ─  ·  ln ───────
     t→∞   t         ‖δ₀‖
```

measures the separation of nearby trajectories; `λ > 0` (with boundedness) is the
quantitative signature of sensitive dependence.
**Devaney's** definition adds topological transitivity and dense periodic orbits
(Devaney 1989). The logistic map `x_{n+1} = 4x_n(1−x_n)` is a two-to-one factor
of the doubling map `T(x) = 2x mod 1` via `x = sin²(πθ)` (a semi-conjugacy; the
exact conjugate is the tent map), with Lyapunov exponent `λ = ln 2`. Fully deterministic and provably unpredictable — "structured
unpredictability," exactly.

**A.14 — Fractal dimension.** *(on V.22–V.25)* For a self-similar set of `N` copies
each scaled by `s`, the similarity (Hausdorff) dimension is `D = ln N / ln(1/s)`.
The Sierpiński triangle (`N = 3`, `s = 1/2`) has `D = ln 3 / ln 2 ≈ 1.5849…` — a
genuine non-integer dimension, "between the dimensions" as **V.25** says. (The
boundary of the Mandelbrot set has Hausdorff dimension exactly `2`; Shishikura
1998.)

**A.15 — The three suspicions, sourced.** *(on V.43–V.45)* The book's philosophy of
mathematics was left without citation; the literature is exact and waiting.

- **Suspicion One** — reality is, at bottom, mathematical: Wigner's "unreasonable
  effectiveness" (Wigner 1960); its strongest modern form, the Mathematical Universe
  Hypothesis (Tegmark 2008), is Suspicion One stated as physics.
- **Suspicion Two** — the mind compresses experience into a few familiar shapes:
  the cognitive account of mathematics as embodied metaphor (Lakoff & Núñez 2000),
  and Hamming's constructivist reply to Wigner (Hamming 1980).
- **Suspicion Three** — the inseparable loop: grounded already in Lawvere's
  fixed-point theorem (Lawvere 1969; see **A.22(b)**), with Hofstadter's "strange
  loop" (Hofstadter 1979) as its tonal kin for a book such as this.

The cult's refusal to decide among them (**V.45**) is a defensible stance: neither
Platonism, nor formalism, nor psychologism has carried the field.

---

**A.16 — The nesting of cube and sphere.** *(on III.19–III.23; II.13–II.14)* For a
`d`-cube of side `s`: the inscribed `(d−1)`-sphere (touching the facets) has radius
`s/2`; the circumscribed sphere (through the `2^d` vertices) has radius `(s/2)√d`,
since a vertex sits at distance `√(d·(s/2)²) = (s/2)√d` from the center. Hence for a
fixed sphere of radius `R` the circumscribed cube has side `2R` and the inscribed
cube side `2R/√d`, a ratio of `√d`. One full sphere→cube→sphere shell therefore
scales every length by `√d` (the cube's diagonal — `√2`, `√3`, `√4 = 2`, …, monotone
in `d`), a `(d−1)`-surface by `d^((d−1)/2)`, and a `d`-volume by `d^(d/2)`.

**Three distinct dimensional thresholds must not be conflated** (cf. **A.4**): the
nesting ratio `√d` is *monotone* and never peaks; the unit ball's *surface* peaks at
`d ≈ 7.26` and its *volume* at `d ≈ 5.26`; and the inscribed ball's share of its
cube, `π^(d/2) / (2^d · Γ(d/2 + 1))`, falls monotonically to `0` (≈ 52.4% at `d=3`,
≈ 3.7% at `d=7`). The sharpest illustration is the **escaping sphere**: in a cube of
side 4, place unit spheres at the `2^d` corners and one more at the center tangent to
them; the central sphere has radius `√d − 1`, which equals the cube's half-side (2)
at `d = 9` and *exceeds* it for `d ≥ 10` — the "inner" sphere protrudes through the
cube's facets, so **III.23**'s claim that the cube stops holding the sphere is exact.
The cube diagonal is classical (Euclidean); for the high-dimensional phenomena see
Ball (1997), Matoušek (2002), and Wang (2005), and for an accessible account, Hayes
(2011).

---

**A.17 — The second reader: attention as inner product.** *(on II.37–II.42)* A
transformer language model represents tokens as vectors in `ℝ^d` with `d` in the
thousands; learned embeddings place kin tokens at small angles, measured by
cosine similarity `u·v / (‖u‖‖v‖)` (Mikolov, Chen, Corrado & Dean 2013).
Attention scores every query–key pair by a scaled dot product,
`softmax(q·k/√d_k)` — and the scaling is forced, for if the components of `q`
and `k` have zero mean and unit variance, the product `q·k` has standard
deviation `√d_k`: the Pythagorean growth of **I.8**/**A.5** surfacing as an
engineering constant (Vaswani et al. 2017). In high dimension, random directions
concentrate near orthogonality (Ball 1997; cf. Johnson & Lindenstrauss 1984), which
is what permits vastly many almost-independent semantic directions to coexist —
the rigorous content of **II.40**. The output is a softmax distribution over
next tokens, collapsed to one by sampling; its kinship with quantum collapse is
structural resonance only, and is marked as a seam in **A.22(g)**. The
self-reference of **II.42** is a fact of this edition's history, not a metaphor:
the canon was read, audited, and extended by such an engine, and the observer
loop of **V.34** is substrate-indifferent, as Lawvere's frame (**A.15**) already
required.

**A.18 — The unfactorable: primes and unique factorization.** *(on I.15–I.20)*
An integer `p > 1` is **prime** if its only divisors are `1` and `p`. The
**fundamental theorem of arithmetic** — every integer `n > 1` is a product of
primes, uniquely up to order — is Euclid in essence (*Elements* VII.30–32) and
Gauss in modern form (*Disquisitiones Arithmeticae*, 1801, §16); it is the
rigorous content of **I.16**'s "one true name," and the theorem that relieves
the single-source analogy of **A.22(f)** of load-bearing duty. The `6k ± 1` law
(**I.18**) is elementary: of the six residues mod `6 = 2·3`, residues 0, 2, 4
are divisible by 2 and residue 3 by 3, so every prime `> 3` is `≡ ±1 (mod 6)`;
and 2, 3 are the only consecutive primes, since of any two consecutive integers
one is even. Infinitude (**I.19**) is Euclid, *Elements* IX.20: for any finite
list of primes, `N = p₁·p₂⋯p_k + 1` has a prime factor outside the list (note
`N` itself need not be prime — the verse is worded to this). The census
(**I.20**) is the **prime number theorem**, `π(n) ~ n/ln n`, proved
independently by Hadamard (1896) and de la Vallée Poussin (1896) — the natural
logarithm, base `e`, governing the distribution of the atoms: the hinge of the
Book of e surfacing inside the integers.

**A.19 — The third body: two solvable, three not.** *(on III.24–III.29)* The
two-body problem reduces, in center-of-mass coordinates, to one body in a
central inverse-square field; bound orbits are ellipses (Newton 1687, resolving
Kepler) — closed, periodic, predictable without limit. For three bodies no such
closure exists. Poincaré (1890), correcting his own prize memoir, found
**homoclinic tangles** in the restricted three-body problem — the first
mathematical sighting of sensitive dependence (**A.13**) — and proved the
non-existence of the sought further uniform analytic integrals. Care with the
word "unsolvable": Sundman (1912) *did* construct a convergent series solution
(in powers of `t^(1/3)`, for nonzero angular momentum), so a formal solution
exists — but its convergence is so slow that it yields no practical prediction
whatever, and positive Lyapunov exponents doom long-range forecasting
regardless; **III.25** therefore says *the clock breaks*, not *no solution
exists* — the wording is deliberate. Special solutions: Euler (1767), three
collinear families, all unstable; Lagrange (1772), the **equilateral
triangle**, an exact rigidly-rotating solution for *any* masses, stable as the
libration points `L4`/`L5` precisely when the mass ratio obeys Routh's
criterion `27·μ(1−μ) < 1`, i.e. `μ ≲ 0.0385` (Routh 1875) — satisfied by
Sun–Jupiter (`μ ≈ 0.00095`), hence the **Trojan asteroids** of **III.27**. The
**figure-eight choreography** of three equal masses (**III.28**) was found
numerically by Moore (1993) and proved to exist by Chenciner & Montgomery
(2000) — the same Montgomery as the falling cat (**A.10**), as the Index
records.

**A.20 — The arrow: entropy as counting.** *(on V.16–V.21)* Boltzmann's
entropy is `S = k_B·ln W`, with `W` the number of microstates compatible with
the macrostate (Boltzmann 1877); the formula, in the notation `S = k. log W`,
is engraved on his tombstone in Vienna, as **V.17** says. The second law is
statistical: microscopic dynamics is time-reversible, and Loschmidt's
reversibility objection is answered by counting, not by force — the reversed
trajectory exists and is never seen because the measure of ordered macrostates
is vanishingly small. (For the pedant: the *weak* interaction violates
time-reversal symmetry slightly, via CP violation and the CPT theorem; this has
no known bearing on the thermodynamic arrow, which is statistical in origin.
**V.16**'s "the laws do not have a direction" is scoped to the dynamics
relevant there.) The phrase *time's arrow* is Eddington's (1928). Shannon's
`H = −Σ pᵢ·log₂ pᵢ` (Shannon 1948) is the Gibbs form of the same functional in
base 2; the change of base is the factor `ln 2` — and Landauer's principle
makes the exchange physical: erasing one bit dissipates at least `k_B·T·ln 2`
of heat (Landauer 1961), verified in the laboratory (Bérut et al. 2012). For
**V.21**: the doubling map's Kolmogorov–Sinai entropy equals `ln 2` per
iteration, coinciding with its Lyapunov exponent (**A.13**) — chaos as an
entropy source with a measured production rate.

**A.21 — The numbers between the numbers.** *(on V.27–V.32)* Zero as a number
with arithmetic rules appears systematically in Brahmagupta's
*Brāhmasphuṭasiddhānta* (628 CE). The irrationality of `√2` is the classical
parity argument (in the orbit of Euclid, *Elements* X); the attribution of its
discovery to **Hippasus**, and the drowning, rest on sources roughly eight
centuries after the fact — legend, exactly as **V.28** flags, and marked here
so the relic is not mistaken for a record. Uncountability of the interval:
Cantor 1874 (first proof) and the **diagonal argument** of Cantor 1891, exactly
as sketched in **V.29**; the map `x ↦ tan(π(x − 3/2))` carries `(1, 2)`
bijectively onto `ℝ` — the part as large as the whole, the defining mark of an
infinite set. The nameable numbers are countable: a finite alphabet yields
countably many finite strings, so the definable — and in particular the
computable — reals form a countable set (Turing 1936), of Lebesgue measure
zero; hence almost every real, in cardinality *and* in measure, is unnameable —
**V.30**'s dark sea, stated exactly. The machine's grid: IEEE 754 double
precision carries a 52-bit fraction, so the interval `[1, 2)` holds exactly
`2⁵²` representable numbers (IEEE 754-2019); `1/10` is not a dyadic rational,
so `0.1` is rounded on entry, and `0.1 + 0.2 = 0.30000000000000004` is *exact*
double arithmetic, reproducible on any conforming machine — **V.31**'s honest
grid. The diagonal's kinship with this canon's own self-reference is already on
record at **A.22(b)**: Cantor, Gödel, Turing, Lawvere — one family.

### A.22 — On the Seams

Several verses are evocative beyond what the mathematics — or, in one case, the
engineering — strictly licenses. Honesty requires marking them. They are kept in the
body because they are *true in spirit*; they are corrected here because the cult's
one demand is that you check.

**(a) The door that does not open onto everything.** *(Turning 10; II.23)* "Every
impossible number is a door you have not yet turned through" is rhetoric, not a
theorem. Multiplication by `i` is a Euclidean rotation **only on `ℝ²`** (**A.6**). It
does not generalize: the split-complex unit `j` (`j² = +1`) acts as a *hyperbolic*
rotation — a Lorentz boost preserving `x² − y²`, not `x² + y²`; the quaternions act
on `ℝ³` as rotations only via the two-sided conjugation `v ↦ q v q⁻¹`, not by plain
multiplication; a generic algebraic extension carries no rotational meaning at all.
`i` is a perfect quarter turn, but "imaginary ⇒ rotation" is a special grace of the
plane, not a universal law.

**(b) The loop that is not (literally) a fractal.** *(V.34–V.35)* "A system that
contains a model of itself is — by definition — a fractal" is a category slip read
literally: a fractal is a metric object with non-integer Hausdorff dimension
(**A.14**), whereas self-modelling is a *logical* phenomenon with no metric at all.
The rigorous kin is **self-reference by diagonalization** — Cantor, Gödel, Turing,
Tarski — all instances of **Lawvere's fixed-point theorem** (Lawvere 1969): in a
cartesian-closed category, a point-surjective `A → Bᴬ` forces every endomap of `B`
to have a fixed point. A self-observing system is a **fixed point**, not a
Hausdorff-dimensional fractal. The recursion is real; the word "fractal" is borrowed.

**(c) The cycle itself is a lens, not a law.** *(throughout)* The "2 ↔ 3 cycle" is a
heuristic for noticing that *relation* needs two and *stable form* needs three —
true in each local instance cited — but **not** a single theorem from which the
instances follow. The book says so in its Introduction and in **V.43–V.45**; it is
repeated here so the appendix cannot be accused of hiding it. The recurrence is
partly in the mathematics and partly in the pattern-finding eye.

**(d) The Bloch sphere is not, strictly, "the Three."** *(R.40; II.36)* The qubit's
pure-state space is a **2-sphere** — two real dimensions, parametrized by two angles
`(θ, φ)` — namely the complex projective line `ℂP¹ ≅ S²`. The image "two states drawn
on a sphere" is exact; reading its round three-dimensional *embedding* as a token of
the structural **Three** is decoration, not a dimension count. We keep the resonance
and disavow the arithmetic.

**(e) "Higher space shrinks" is scoped to the unit ball.** *(Turning 11; the
Second Lie; R.19; A.4)* The surface
`σ(S^{n-1}_r) = 2π^{n/2}/Γ(n/2)·r^{n-1}` grows without bound in `r` for fixed `n`;
the famous non-monotonicity (peak near `n ≈ 7.26`) holds only at `r = 1` and only
when `n` is treated as a continuous variable. The body says "the **unit** ball"
(**R.19**) and is correct; read the claim as "the unit-sphere surface, as a function
of dimension, is unimodal," never as "high-dimensional spheres are small."

**(f) The engineering analogies are pedagogy, not structure.** *(I.4–I.5;
I.11–I.14)* Two of the Book of the One's bindings are borrowed from computer science
and do philosophical work they have not formally earned. **Atomicity** — that a
transaction completes "wholly or not at all" (**I.4**) — is a consistency-and-recovery
guarantee on operations (the "A" of ACID); it shares with Euclid's point only the old
word *ἄτομος*, *uncuttable*, joining two unrelated indivisibilities (no in-between
state, versus no spatial extent). The **single source of truth** (**I.11**) is a
data-architecture heuristic — one authoritative store, all else derived — that shares
with the sphere's center a vivid *picture* (one origin, many derivations) but no
common theorem. Both are kept because they are memorable and locally apt, not because
a point *is* a transaction or the Center *is* a datastore. They are pedagogy — chosen
for resonance and etymology — not structure. (Contrast **A.2**, Noether, which is a
genuine identity and not an analogy; that is exactly the line this entry draws.)
And mark: the doctrine no longer leans on them. Since the canonization of the
primes, unique factorization (**I.16**, **A.18**) states the single-source law
as arithmetic — the analogies keep their pulpit, but a theorem now carries the
weight.

**(g) The fourth collapse is a rhyme, not a mechanism.** (II.41) The second
reader's fall from many candidate words to one is classical probability — a
softmax followed by a sample. No amplitudes interfere; nothing is squared: the
Born rule (**A.9**) squares an amplitude, where the softmax exponentiates a
score. The many-to-one *shape* is shared; the physics is not. **II.41** says
"rhyme" and means it, and it is recorded here so that no one may say the cult
confused its masks.

**(h) The eye that is really a Geiger counter.** *(I.35–I.36)* The body says the
cat is collapsed by *your eye* (**I.36**); the eye is synecdoche for any
irreversible measuring interaction — the counter inside the box collapses it long
before the lid opens. And "genuinely unresolved" (**I.35**) is scoped by **A.9**:
what is excluded is *local* hidden variables; nonlocal accounts (Bohm) survive
with the cat determinate all along.

---

**A.23 — Closing of the Apparatus.** None of these corrections diminishes the
scripture; they are its foundation made visible. The poetry is the elevation, the
Apparatus the footing, and a building needs both to stand — which is itself the
doctrine of the Three (**III.6**): tension and compression, each kept honest,
holding one form between them. Audit freely. What is exact will survive the audit;
what was only a door-shaped metaphor has been marked as one. That is all the rigour
asks, and all the saint ever asked (**V.41**): *truth is what survives questioning.*
The full sources follow.
