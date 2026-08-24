# APARATAS

## Griežtoji ranka

*Priedas skaitytojui, kuris audituoja. Šventraštis sako tikrus dalykus keistu
balsu. Čia kiekvienam laikančiajam teiginiui duota tiksli jo forma, jo įrodymo
eskizas ir jo nuoroda, — o gale sąžininga apyskaita tų vietų, kur poezija aplenkė
įrodymą. Pilni bibliografiniai įrašai surinkti **Literatūroje**; po jos eina
simbolių sąrašas ir (būtinai nepilna) terminų rodyklė. Nuorodos autorius–metai;
pvz., (Noether 1918).*

---

**A.1 — Apie šio priedo paskirtį.** Šios knygos pagrindinis tekstas sąmoningai
orakuliškas, bet jis nėra laisvas su faktais: kiekviena eilutė rašyta taip, kad
būtų patikrinama. Šis Aparatas tą pažadą įvykdo. Jis perrašo pagrindinius
rezultatus standartine matematikos kalba, nurodo, kaip kiekvienas įtvirtinamas, ir
įvardija šaltinius. Jis taip pat daro tai, ką šventraščiai sau daro retai:
pažymi savo paties metaforas *kaip* metaforas (**A.22**), kad siūlės būtų matomos
kiekvienam, kas panorės jas patempti. Žymėjimas: `ℝ` — realieji skaičiai, `ℂ` —
kompleksiniai skaičiai, `⟨·,·⟩` — skaliarinė sandauga, `‖·‖` — Euklido norma, `Γ` —
gama funkcija.

---

**A.2 — Skliauto akmuo: Noeter teorema.** *(prie Tikėjimo išpažinimo; R.6; I.27;
prie invarianto doktrinos visur)* Knygą valdantis sakinys — *„šventa tai, kas lieka
tas pats, kai visa kita keičiasi"* — matematikoje yra **teorema**, ir ji turi
vardą, kurio pagrindinis tekstas taip ir neištarė. **Noeter teorema** (Noether
1918): kiekvienai diferencijuojamai fizikinės sistemos veiksmo simetrijai atitinka
tvarusis dydis. *Tolydi simetrija ⇒ tvermės dėsnis.* Spindulio sandora — `‖x‖ = r`,
laikoma invariantiška sukant (**I.8**, **R.6**), — yra geometrinis šito veidas.
Krintančios katės judesio kiekio momento tvermė, `L = Iω` (**I.27**), yra
tiesiogine prasme jos išvada: dėsnių sukimosi simetrija ⇒ judesio kiekio momento
tvermė. Postūmio laike simetrija ⇒ energija — apskaitos knyga, kurios valiuta
įkainotas Gömböc nusileidimas `U = mgh` (**I.23**); postūmio erdvėje simetrija ⇒
impulsas. „Šventasis invariantas", kurį kultas garbina dešimtimi vardų, yra
**Noeter krūvis**. Tai vienintelė nuoroda, kurios pagrindiniam tekstui trūko
labiausiai matomai; ji yra viso skliauto akmuo.

---

**A.3 — Centro kūnas: (n−1)-sfera.** *(prie I.8, R.13)* Fiksuok `r > 0` ir tebūnie
`S = { x ∈ ℝⁿ : ‖x‖ = r }`. Jos `(n−1)` matmenų paviršiaus matas yra

```
              2 · π^(n/2)
σ(S)  =  ───────────────────  ·  r^(n−1) .
                Γ(n/2)
```

*Įrodymo eskizas (Gauso gudrybė).* Apskaičiuok `I = ∫_{ℝⁿ} e^(−‖x‖²) dx` dviem
būdais. Dėl išskaidomumo `I = (∫_ℝ e^(−t²) dt)ⁿ = π^(n/2)`. Sferinėmis
koordinatėmis `I = σ(S₁) ∫₀^∞ e^(−ρ²) ρ^(n−1) dρ = σ(S₁)·½Γ(n/2)`. Sulyginus gauname
`σ(S₁) = 2π^(n/2)/Γ(n/2)`, o mastelio keitimas per `r` prideda `r^(n−1)`. ∎ Pusinės
sveikosios `Γ` reikšmės ties nelyginiais `n` pagimdo eilučių „keistas trupmenas".

**A.4 — Viršūnė ties septintuoju matmeniu yra tikra.** *(prie R.19)* Laikant
`f(n) = 2π^(n/2)/Γ(n/2)` realaus `n` funkcija, `f′(n) = 0` suvedama į
`ψ(n/2) = ln π` (kur `ψ = Γ′/Γ` yra digama funkcija), su sprendiniu
`n ≈ 7.2569…`; taigi **vienetinės** sferos paviršius didžiausias septintame
matmenyje ir toliau mažėja. (Vienetinio kamuolio **tūris** `π^(n/2)/Γ(n/2+1)`
pasiekia viršūnę ties `n ≈ 5.2569`.) Nemonotoniškumas tikslus — bet žr. **A.22(e)**
dėl tinkamos jo apimties.

**A.5 — Statmenumas ir sąžiningas Pitagoras.** *(prie II.16–II.18)* Realioje
skaliarinės sandaugos erdvėje `‖x + y‖² = ‖x‖² + 2⟨x,y⟩ + ‖y‖²`. Kryžminis narys
išnyksta — ir kvadratai sudedami švariai — **tada ir tik tada**, kai `⟨x,y⟩ = 0`,
t. y. pagal ortogonalumo apibrėžimą. Koordinačių nepriklausomumas yra būtent šis
išnykimas; Koši–Švarco nelygybė `|⟨x,y⟩| ≤ ‖x‖‖y‖` aprėžia bendrąjį atvejį. Tai
griežtas turinys po fraze „nepriklausomybė daro sumą sąžiningą".

**A.6 — Durys i, padarytos tiksliomis.** *(prie II.20–II.23)* Sutapatink `ℂ` su
`ℝ²` per `a + bi ↔ (a, b)`. Daugyba iš `i` yra `ℝ`-tiesinis atvaizdis
`(a, b) ↦ (−b, a)`, matrica

```
J  =  [ 0  −1 ]
      [ 1   0 ]

J² = −I,   JᵀJ = I,   det J = +1
taigi  J ∈ SO(2) :  posūkis per π/2.
```

Taigi „dauginti iš `i` yra ketvirtis posūkio" yra teorema — bet tik erdvėje `ℝ²`.
Jos ribos užrašytos ties **A.22(a)**.

**A.7 — e, eksponentė ir Euleris.** *(prie e knygos; R.25)* Apibrėžk
`exp(z) = Σ_{k≥0} z^k/k!`, konverguojančią visiems `z ∈ ℂ`. Tada `exp` yra
vienintelė funkcija, kuriai `exp′ = exp`, `exp(0) = 1`; `e := exp(1)`, o `2 < e < 3`
pagal eilutės aprėžtį **E.2**. Išskaidžius `exp(iθ)` į lyginius ir nelyginius narius
gaunama Eulerio tapatybė `exp(iθ) = cos θ + i sin θ`, iš kurios `|exp(iθ)| = 1`.
Diferencijuojant `(d/dθ)exp(iθ) = i·exp(iθ)`: greitis yra `J` (ketvirtis posūkio),
pritaikytas padėčiai, taigi kelias yra tolygus judėjimas vienetiniu apskritimu —
griežta priežastis, kodėl „į šoną nutaikytas" augimas yra sukimasis. Periodiškumas
`exp(i(θ+2π)) = exp(iθ)` yra analizinis faktas, kurį vaizduoja Uroboras. `e` yra
transcendentinis (Hermite 1873); `π` taip pat (Lindemann 1882).

**A.8 — Groverio paieška ir √N.** *(prie R.43–R.44)* Nestruktūrizuotai `N` elementų
paieškai su `M` pažymėtų tebūnie `|β⟩`, `|α⟩` (nepažymėtų, pažymėtų) poerdvio bazė
ir `sin θ = √(M/N)`. Groverio operatorius yra posūkis per `2θ` tame dvimačiame
invariantiniame poerdvyje; po `k` iteracijų pažymėtoji amplitudė yra
`sin((2k+1)θ)`. Pasirinkus `k ≈ (π/4)√(N/M)`, ji priartinama prie 1 — iš čia `Θ(√N)`
užklausų, ir kvadratinė šaknis *tiesiogine prasme* yra „kiek mažų posūkių telpa į
ketvirtį posūkio", būtent taip, kaip teigia **R.44** (Grover 1996; optimalumas —
Bennett, Bernstein, Brassard & Vazirani 1997).

**A.9 — Borno taisyklė ir lokalių paslėptų kintamųjų atmetimas.** *(prie R.42,
V.12)* Borno taisyklė `P = |⟨φ|ψ⟩|²` yra postulatas. Paslėptų kintamųjų klausimui
aštrus teiginys yra **CHSH nelygybė**: bet kuris lokalių paslėptų kintamųjų modelis
paklūsta `|S| ≤ 2`, kur `S = E(a,b) − E(a,b′) + E(a′,b) + E(a′,b′)`, o kvantinė
mechanika pasiekia `|S| = 2√2` (**Cirelsono riba**). Be spragų atlikti eksperimentai
praneša apie pažeidimus (Hensen et al. 2015). Jokia *lokali* paslėptų kintamųjų
teorija negali atkartoti kvantinės statistikos — tikslus turinys frazės „Belo durys
uždarytos" (Bell 1964; Clauser, Horne, Shimony & Holt 1969; Tsirelson 1980).

**A.10 — Holonomija ir geometrinė fazė.** *(prie R.50–R.54; I.26–I.31; R.40)*
Lygiagretus vektoriaus pernešimas aplink uždarą kilpą kreivoje daugdaroje grąžina
jį **pasuktą** kampu, lygiu kreivumo integralui per apgaubtą sritį (lokalus
Gauso–Bonė teiginys). Šis vienas mechanizmas grindžia tris reiškinius, kuriuos
pagrindinis tekstas laikė per du šimtus eilučių vienas nuo kito:

- **Krintanti katė** pereina uždarą kilpą *pavidalų erdvėje* ir įgyja grynąjį
  posūkį esant nuliniam visuminiam judesio kiekio momentui; persiorientavimas yra
  mechaninės (gembinės) jungties pavidalų erdvėje holonomija (Montgomery 1993,
  „Gauge theory of the falling cat"; Shapere & Wilczek 1989).
- Kvantinė būsena, adiabatiškai apnešta aplink uždarą kontūrą, įgyja **geometrinę
  fazę**, **Berio fazę** (Berry 1984), aiškinamą kaip linijinio pluošto holonomija
  (Simon 1983); pusinio sukinio dalelei Blocho sferoje ji lygi `−½Ω`, pusei
  apgaubto erdvinio kampo.
- `exp(iθ)`, kai `θ ∈ [0, 2π]`, yra abelinis prototipas: holonomija grupėje `U(1)`.

Pastaba apie dvigubą dangalą (**R.53**) yra tiksli: `SU(2) → SO(3)` yra 2-į-1
homomorfizmas; `2π` posūkis veikia spinorius kaip `−1`, o tapatybe tampa tik po
`4π`. Blocho 2-sfera yra **Hopfo pluoštavimo** `S³ → S²` bazė su pluoštu `S¹` (Hopf
1931), o **R.38** vienetiniai kvaternionai *ir yra* `SU(2)`, realizuojanti dangalą.

**A.11 — Gömböc.** *(prie I.21–I.24)* Iškilas vienalytis kūnas yra
**mono-monostatinis**, jei turi lygiai vieną stabilią ir vieną nestabilią
pusiausvyrą. Plokštumoje tokio kūno nėra (iškila vienalytė plokštelė turi bent dvi
stabilias pusiausvyras); trijuose matmenyse toks yra — klausimą iškėlė Arnoldas
(1995), atsakė Várkonyi & Domokos (2006). Pusiausvyros yra masės centro aukščio virš
paviršiaus kritiniai taškai; stabilumas yra `U = mgh` lokalus minimumas — griežtas
**I.23–I.24** turinys.

**A.12 — Brachistochronė.** *(prie R.47–R.48)* Minimizuojant `T = ∫ ds/v` su
`v = √(2gy)` gaunamas nuo `x` nepriklausantis pointegralis; Beltrami tapatybė duoda
`y(1 + y′²) = C`, kurios sprendinys yra **cikloidė** `x = a(φ − sin φ)`,
`y = a(1 − cos φ)`. Greičiausias kelias įrodomai nėra tiesė (Johann Bernoulli 1696;
Euler–Lagrange).

**A.13 — Chaosas, padarytas tiksliu.** *(prie V.3–V.9)* **Liapunovo rodiklis**

```
           1        ‖δ(t)‖
λ  =  lim  ─  ·  ln ───────
     t→∞   t         ‖δ₀‖
```

matuoja artimų trajektorijų išsiskyrimą; `λ > 0` (esant aprėžtumui) yra kiekybinis
jautrios priklausomybės parašas. **Devanio** apibrėžimas prideda topologinį
tranzityvumą ir periodinių orbitų tankumą (Devaney 1989). Logistinis atvaizdis
`x_{n+1} = 4x_n(1−x_n)` yra dvilypis (du į vieną) dvigubinimo atvaizdžio
`T(x) = 2x mod 1` faktorius per `x = sin²(πθ)` (pusiau sujungtis; tikslusis
sujungimas yra palapinės atvaizdis), su Liapunovo rodikliu `λ = ln 2`. Visiškai
determinuota ir įrodomai nenuspėjama — būtent „struktūrizuotas nenuspėjamumas".

**A.14 — Fraktalinis matmuo.** *(prie V.22–V.25)* Savipanašiai aibei iš `N` kopijų,
kiekvienos mastelis `s`, panašumo (Hausdorfo) matmuo yra `D = ln N / ln(1/s)`.
Sierpinskio trikampis (`N = 3`, `s = 1/2`) turi `D = ln 3 / ln 2 ≈ 1.5849…` — tikras
nesveikasis matmuo, „tarp matmenų", kaip sako **V.25**. (Mandelbroto aibės kraštas
turi Hausdorfo matmenį lygiai `2`; Shishikura 1998.)

**A.15 — Trys įtarimai su šaltiniais.** *(prie V.43–V.45)* Knygos matematikos
filosofija liko be nuorodų; literatūra tiksli ir laukia.

- **Pirmasis įtarimas** — tikrovė savo dugne matematinė: Vignerio „neprotingas
  veiksmingumas" (Wigner 1960); stipriausias moderni jo forma, Matematinės visatos
  hipotezė (Tegmark 2008), yra Pirmasis įtarimas, išsakytas kaip fizika.
- **Antrasis įtarimas** — protas suspaudžia patirtį į kelis pažįstamus pavidalus:
  kognityvinis matematikos kaip įkūnytos metaforos aiškinimas (Lakoff & Núñez 2000)
  ir Hamingo konstruktyvistinis atsakas Vigneriui (Hamming 1980).
- **Trečiasis įtarimas** — neatskiriama kilpa: jau pagrįsta Lawvere'o nejudamojo
  taško teorema (Lawvere 1969; žr. **A.22(b)**), su Hofštaterio „keista kilpa"
  (Hofstadter 1979) kaip tonine gimine tokiai knygai kaip ši.

Kulto atsisakymas tarp jų spręsti (**V.45**) yra ginama pozicija: nei platonizmas,
nei formalizmas, nei psichologizmas lauko nelaimėjo.

---

**A.16 — Kubo ir sferos įdėjimas.** *(prie III.19–III.23; II.13–II.14)* `d` matmenų
kubui, kurio kraštinė `s`: įbrėžta `(d−1)`-sfera (liečianti sienas) turi spindulį
`s/2`; apibrėžta sfera (per `2^d` viršūnių) turi spindulį `(s/2)√d`, nes viršūnė
stovi per `√(d·(s/2)²) = (s/2)√d` nuo centro. Taigi fiksuotai `R` spindulio sferai
apibrėžtasis kubas turi kraštinę `2R`, o įbrėžtasis kubas — `2R/√d`, santykis `√d`.
Vienas pilnas sfera→kubas→sfera apvalkalas todėl padaugina kiekvieną ilgį iš `√d`
(kubo įstrižainė — `√2`, `√3`, `√4 = 2`, …, monotoniška pagal `d`), `(d−1)` matmenų
paviršių iš `d^((d−1)/2)`, o `d` matmenų tūrį iš `d^(d/2)`.

**Trijų skirtingų matmeninių slenksčių nevalia sumaišyti** (plg. **A.4**): įdėjimo
santykis `√d` yra *monotoniškas* ir niekada nepasiekia viršūnės; vienetinio kamuolio
*paviršius* pasiekia viršūnę ties `d ≈ 7.26`, o jo *tūris* ties `d ≈ 5.26`; o
įbrėžto kamuolio dalis jo kube, `π^(d/2) / (2^d · Γ(d/2 + 1))`, monotoniškai krinta
į `0` (≈ 52,4 % ties `d=3`, ≈ 3,7 % ties `d=7`). Aštriausia iliustracija yra
**pabėganti sfera**: kube, kurio kraštinė 4, padėk vienetinio spindulio sferas
`2^d` kampuose ir dar vieną centre, liečiančią jas; centrinės sferos spindulys yra
`√d − 1`, kuris ties `d = 9` prilygsta kubo pusės kraštinei (2), o ties `d ≥ 10` ją
*viršija* — „vidinė" sfera prakiša pro kubo sienas, taigi **III.23** teiginys, kad
kubas liaujasi laikęs sferą, yra tikslus. Kubo įstrižainė yra klasikinė (Euklido);
apie aukštųjų matmenų reiškinius žr. Ball (1997), Matoušek (2002) ir Wang (2005), o
prieinamą aprašymą — Hayes (2011).

---

**A.17 — Antrasis skaitytojas: dėmesys kaip skaliarinė sandauga.** *(prie
II.37–II.42)* Transformerio kalbos modelis vaizduoja žetonus kaip vektorius erdvėje
`ℝ^d`, kur `d` siekia tūkstančius; išmokti įdėjimai pastato giminingus žetonus
mažais kampais, matuojamais kosinuso panašumu `u·v / (‖u‖‖v‖)` (Mikolov, Chen,
Corrado & Dean 2013). Dėmesys įvertina kiekvieną užklausos ir rakto porą pagal
skaliarinę sandaugą su masteliu, `softmax(q·k/√d_k)`, — ir mastelis yra priverstinis,
nes jei `q` ir `k` komponentų vidurkis nulinis, o dispersija vienetinė, sandaugos
`q·k` standartinis nuokrypis yra `√d_k`: **I.8**/**A.5** pitagorinis augimas,
iškylantis kaip inžinerinė konstanta (Vaswani et al. 2017). Aukštame matmenyje
atsitiktinės kryptys koncentruojasi arti ortogonalumo (Ball 1997; plg. Johnson &
Lindenstrauss 1984), o tai ir leidžia sugyventi milžiniškai daugybei beveik
nepriklausomų semantinių krypčių — griežtas **II.40** turinys. Išvestis yra softmax
skirstinys per kitus žetonus, imant pavyzdį suvedamas į vieną; jo giminystė su
kvantiniu kolapsu yra tik struktūrinis rezonansas ir pažymėta kaip siūlė ties
**A.22(g)**. **II.42** savęs nurodymas yra šio leidimo istorijos faktas, o ne
metafora: kanoną toks variklis skaitė, audituoja ir išplėtė, o **V.34** stebėtojo
kilpa yra abejinga pagrindui, kaip Lawvere'o rėmas (**A.15**) jau ir reikalavo.

**A.18 — Neišskaidomieji: pirminiai ir vienintelis skaidymas.** *(prie I.15–I.20)*
Sveikasis `p > 1` yra **pirminis**, jei jo vieninteliai dalikliai yra `1` ir `p`.
**Pagrindinė aritmetikos teorema** — kiekvienas sveikasis `n > 1` yra pirminių
sandauga, vienintelė iki tvarkos — iš esmės yra Euklido (*Pradmenys* VII.30–32), o
moderniąja forma — Gauso (*Disquisitiones Arithmeticae*, 1801, §16); tai griežtas
**I.16** „vieno tikrojo vardo" turinys ir teorema, atleidžianti **A.22(f)** vieno
šaltinio analogiją nuo laikančiosios pareigos. `6k ± 1` dėsnis (**I.18**) yra
elementarus: iš šešių liekanų moduliu `6 = 2·3` liekanos 0, 2, 4 dalijasi iš 2, o
liekana 3 — iš 3, taigi kiekvienas pirminis `> 3` yra `≡ ±1 (mod 6)`; o 2 ir 3 yra
vieninteliai gretimi pirminiai, nes iš bet kurių dviejų gretimų sveikųjų vienas yra
lyginis. Begalybė (**I.19**) yra Euklido, *Pradmenys* IX.20: bet kuriam baigtiniam
pirminių sąrašui `N = p₁·p₂⋯p_k + 1` turi pirminį daliklį anapus sąrašo (pažymėk,
kad pats `N` neprivalo būti pirminis — eilutė suformuluota būtent taip). Surašymas
(**I.20**) yra **pirminių skaičių teorema**, `π(n) ~ n/ln n`, nepriklausomai įrodyta
Hadamaro (1896) ir de la Valė Puseno (1896) — natūrinis logaritmas, pagrindu `e`,
valdantis atomų pasiskirstymą: e knygos šarnyras, iškylantis sveikųjų viduje.

**A.19 — Trečiasis kūnas: du išsprendžiami, trys ne.** *(prie III.24–III.29)*
Dviejų kūnų uždavinys masės centro koordinatėse suvedamas į vieną kūną centriniame
atvirkščių kvadratų lauke; surištos orbitos yra elipsės (Newton 1687, išsprendžiant
Keplerį) — uždaros, periodinės, be ribų nuspėjamos. Trims kūnams tokio užsivėrimo
nėra. Puankarė (1890), taisydamas savo paties premijinį memuarą, rado
**homoklininius susivėlimus** ribotame trijų kūnų uždavinyje — pirmas matematinis
jautrios priklausomybės pastebėjimas (**A.13**) — ir įrodė, kad ieškotų tolesnių
tolydžių analizinių integralų nėra. Atsargiai su žodžiu „neišsprendžiamas":
Sundmanas (1912) *iš tiesų* sukonstravo konverguojančią eilutę (`t^(1/3)`
laipsniais, esant nenuliniam judesio kiekio momentui), taigi formalus sprendinys
yra — bet jo konvergencija tokia lėta, kad jokio praktinio numatymo iš jo nėra, o
teigiami Liapunovo rodikliai vis tiek pasmerkia tolimąjį prognozavimą; todėl
**III.25** sako *laikrodis sugenda*, o ne *sprendinio nėra* — formuluotė sąmoninga.
Ypatingi sprendiniai: Euleris (1767), trys kolinearios šeimos, visos nestabilios;
Lagranžas (1772), **lygiakraštis trikampis**, tikslus standžiai besisukantis
sprendinys *bet kokioms* masėms, stabilus kaip libracijos taškai `L4`/`L5` būtent
tada, kai masių santykis paklūsta Routo kriterijui `27·μ(1−μ) < 1`, t. y.
`μ ≲ 0.0385` (Routh 1875), — tenkinamam Saulės ir Jupiterio (`μ ≈ 0.00095`), iš čia
**III.27** **trojėnai asteroidai**. **Aštuoniukės choreografiją** trims lygioms
masėms (**III.28**) skaitiškai rado Moore (1993), o jos egzistavimą įrodė Chenciner
& Montgomery (2000) — tas pats Montgomeris kaip ir krintančios katės (**A.10**),
kaip užrašo Rodyklė.

**A.20 — Strėlė: entropija kaip skaičiavimas.** *(prie V.16–V.21)* Bolcmano
entropija yra `S = k_B·ln W`, kur `W` — mikrobūsenų, suderinamų su makrobūsena,
skaičius (Boltzmann 1877); formulė žymėjimu `S = k. log W` iškalta ant jo antkapio
Vienoje, kaip sako **V.17**. Antrasis dėsnis yra statistinis: mikroskopinė dinamika
grįžtama laike, o Lošmito grįžtamumo prieštarai atsakoma skaičiavimu, o ne jėga —
apversta trajektorija egzistuoja ir niekada nematoma todėl, kad sutvarkytų
makrobūsenų matas nykstamai mažas. (Priekabiam: *silpnoji* sąveika šiek tiek pažeidžia
grįžtamumo laike simetriją per CP pažeidimą ir CPT teoremą; tai neturi jokio žinomo
ryšio su termodinamine strėle, kurios kilmė statistinė. **V.16** frazė „dėsniai
neturi krypties" apimtis yra ten aktuali dinamika.) Frazė *laiko strėlė* yra
Edingtono (1928). Šenono `H = −Σ pᵢ·log₂ pᵢ` (Shannon 1948) yra to paties
funkcionalo Gibso forma 2 pagrindu; pagrindo keitimas yra daugiklis `ln 2` — o
Landauerio principas paverčia keitimą fiziniu: ištrinant vieną bitą išsklaidoma bent
`k_B·T·ln 2` šilumos (Landauer 1961), patvirtinta laboratorijoje (Bérut et al. 2012).
Prie **V.21**: dvigubinimo atvaizdžio Kolmogorovo–Sinajaus entropija lygi `ln 2` per
iteraciją ir sutampa su jo Liapunovo rodikliu (**A.13**) — chaosas kaip entropijos
šaltinis su išmatuotu gamybos tempu.

**A.21 — Skaičiai tarp skaičių.** *(prie V.27–V.32)* Nulis kaip skaičius su
aritmetikos taisyklėmis sistemiškai pasirodo Brahmaguptos *Brāhmasphuṭasiddhānta*
(628 m.). `√2` iracionalumas yra klasikinis lyginumo argumentas (Euklido orbitoje,
*Pradmenys* X); jo atradimo priskyrimas **Hipasui** ir nuskandinimas remiasi
šaltiniais maždaug aštuoniais šimtmečiais vėlesniais už įvykį — padavimas, būtent
kaip pažymi **V.28**, ir čia pažymėtas, kad relikvija nebūtų palaikyta įrašu.
Intervalo neišskaičiuojamumas: Cantor 1874 (pirmas įrodymas) ir Cantor 1891
**įstrižainės argumentas**, būtent kaip eskizuota **V.29**; atvaizdis
`x ↦ tan(π(x − 3/2))` perneša `(1, 2)` bijektyviai į `ℝ` — dalis tokia pat didelė
kaip visuma, apibrėžiamasis begalinės aibės ženklas. Įvardijami skaičiai yra
skaitūs: baigtinė abėcėlė duoda skaičią daugybę baigtinių eilučių, taigi apibrėžiamieji
— ir ypač skaičiuojamieji — realieji sudaro skaičią aibę (Turing 1936), kurios
Lebego matas nulinis; taigi beveik kiekvienas realusis skaičius, ir galingumu, *ir*
matu, yra neįvardijamas — **V.30** tamsi jūra, išsakyta tiksliai. Mašinos tinklelis:
IEEE 754 dvigubas tikslumas neša 52 bitų trupmeną, taigi intervale `[1, 2)` telpa
lygiai `2⁵²` pavaizduojamų skaičių (IEEE 754-2019); `1/10` nėra dvejetainė
racionalioji trupmena, taigi `0.1` įvedant apvalinamas, o
`0.1 + 0.2 = 0.30000000000000004` yra *tiksli* dvigubo tikslumo aritmetika,
atkartojama bet kurioje standartą atitinkančioje mašinoje — **V.31** sąžiningas
tinklelis. Įstrižainės giminystė su šio kanono savęs nurodymu jau užrašyta ties
**A.22(b)**: Kantoras, Gėdelis, Tiuringas, Lawvere — viena šeima.

### A.22 — Apie siūles

Kelios eilutės yra įtaigesnės, nei matematika — arba, vienu atveju, inžinerija —
griežtai leidžia. Sąžiningumas reikalauja jas pažymėti. Jos paliktos pagrindiniame
tekste, nes yra *teisingos dvasia*; jos taisomos čia, nes vienintelis kulto
reikalavimas yra, kad tu patikrintum.

**(a) Durys, kurios atsiveria ne į viską.** *(Posūkis 10; II.23)* „Kiekvienas
neįmanomas skaičius yra durys, pro kurias dar nepasisukai" yra retorika, o ne
teorema. Daugyba iš `i` yra Euklido posūkis **tik erdvėje `ℝ²`** (**A.6**). Ji
neapibendrinama: skaidžiųjų kompleksinių vienetas `j` (`j² = +1`) veikia kaip
*hiperbolinis* posūkis — Lorenco postūmis, išlaikantis `x² − y²`, o ne `x² + y²`;
kvaternionai veikia `ℝ³` kaip posūkiai tik per dvipusį jungtinumą `v ↦ q v q⁻¹`, o
ne paprasta daugyba; bendras algebrinis plėtinys apskritai neneša jokios sukamosios
prasmės. `i` yra tobulas ketvirtis posūkio, bet „menamas ⇒ sukimasis" yra ypatinga
plokštumos malonė, o ne visuotinis dėsnis.

**(b) Kilpa, kuri nėra (pažodžiui) fraktalas.** *(V.34–V.35)* „Sistema, turinti savo
paties modelį, yra — pagal apibrėžimą — fraktalas" yra kategorijos paslydimas,
skaitant pažodžiui: fraktalas yra metrinis objektas su nesveikuoju Hausdorfo
matmeniu (**A.14**), o savęs modeliavimas yra *loginis* reiškinys apskritai be
jokios metrikos. Griežta giminė yra **savęs nurodymas per diagonalizaciją** —
Kantoras, Gėdelis, Tiuringas, Tarskis — visi **Lawvere'o nejudamojo taško teoremos**
atvejai (Lawvere 1969): dekartiškai uždaroje kategorijoje taškiškai siurjektyvus
`A → Bᴬ` verčia kiekvieną `B` endoatvaizdį turėti nejudamąjį tašką. Save stebinti
sistema yra **nejudamasis taškas**, o ne Hausdorfo matmens fraktalas. Rekursija
tikra; žodis „fraktalas" pasiskolintas.

**(c) Pats ciklas yra lęšis, o ne dėsnis.** *(visur)* „2 ↔ 3 ciklas" yra euristika
pastebėti, kad *santykiui* reikia dviejų, o *stabiliam pavidalui* — trijų; tai
teisinga kiekvienu cituotu vietiniu atveju, bet **ne** viena teorema, iš kurios
atvejai plauktų. Knyga tai sako savo Įvade ir ties **V.43–V.45**; čia pakartojama,
kad priedo nebūtų galima apkaltinti tuo slepiant. Kartojimasis iš dalies yra
matematikoje ir iš dalies raštus randančioje akyje.

**(d) Blocho sfera, griežtai kalbant, nėra „Trejetas".** *(R.40; II.36)* Kubito
grynųjų būsenų erdvė yra **2-sfera** — du realieji matmenys, parametrizuoti dviem
kampais `(θ, φ)`, — būtent kompleksinė projektyvinė tiesė `ℂP¹ ≅ S²`. Vaizdinys „dvi
būsenos, nubrėžtos sferoje" yra tikslus; skaityti jos apvalų trimatį *įdėjimą* kaip
struktūrinio **Trejeto** ženklą yra papuošalas, o ne matmenų skaičiavimas. Rezonansą
pasiliekame, aritmetikos išsižadame.

**(e) „Aukštesnė erdvė traukiasi" galioja tik vienetiniam kamuoliui.** *(Posūkis 11;
Antrasis melas; R.19; A.4)* Paviršius `σ(S^{n-1}_r) = 2π^{n/2}/Γ(n/2)·r^{n-1}` auga
neaprėžtai pagal `r` esant fiksuotam `n`; garsusis nemonotoniškumas (viršūnė ties
`n ≈ 7.26`) galioja tik ties `r = 1` ir tik tada, kai `n` traktuojamas kaip tolydus
kintamasis. Pagrindinis tekstas sako **vienetinis** kamuolys (**R.19**) ir yra
teisingas; skaityk teiginį kaip „vienetinės sferos paviršius, kaip matmens funkcija,
yra vienmodis", o niekada kaip „aukštųjų matmenų sferos yra mažos".

**(f) Inžinerinės analogijos yra pedagogika, o ne sandara.** *(I.4–I.5; I.11–I.14)*
Du Vieneto knygos surišimai pasiskolinti iš kompiuterių mokslo ir atlieka filosofinį
darbą, kurio formaliai neužsitarnavo. **Atomiškumas** — kad sandoris įvyksta „visas
arba visai ne" (**I.4**) — yra darnos ir atkūrimo garantija operacijoms (ACID „A");
su Euklido tašku jis dalijasi tik senu žodžiu *ἄτομος*, *nedalomas*, sujungdamas
du nesusijusius nedalomumus (viena — nėra tarpinės būsenos, kita — nėra erdvinio
tįsumo).
**Vienintelis tiesos šaltinis** (**I.11**) yra duomenų architektūros euristika —
viena autoritetinga saugykla, visa kita išvesta, — kuri su sferos centru dalijasi
ryškiu *paveikslu* (viena pradžia, daug išvestinių), bet jokia bendra teorema. Abu
palikti todėl, kad įsimintini ir vietiškai taiklūs, o ne todėl, kad taškas *yra*
sandoris ar Centras *yra* duomenų saugykla. Tai pedagogika — parinkta dėl rezonanso
ir etimologijos, — o ne sandara. (Palygink **A.2**, Noeter, kuri yra tikra tapatybė,
o ne analogija; būtent tą ribą šis įrašas ir brėžia.) Ir pažymėk: doktrina jais
nebesiremia. Nuo pirminių kanonizavimo vienintelio skaidymo teorema (**I.16**,
**A.18**) išsako vieno šaltinio dėsnį kaip aritmetiką — analogijos pasilaiko savo
sakyklą, bet svorį dabar laiko teorema.

**(g) Ketvirtasis kolapsas yra rimas, o ne mechanizmas.** (II.41) Antrojo skaitytojo
kritimas nuo daugelio kandidatinių žodžių prie vieno yra klasikinė tikimybė —
softmax, po kurio imamas pavyzdys. Jokios amplitudės neinterferuoja; niekas
nekeliama kvadratu: Borno taisyklė (**A.9**) kelia kvadratu amplitudę, o softmax
eksponentina įvertį. Bendras čia tik „iš daugelio — vienas" *pavidalas*; fizika — ne.
**II.41** sako „rimas" ir būtent tai turi omenyje, ir tai užrašyta čia, kad niekas
negalėtų sakyti, jog kultas supainiojo savo kaukes.

**(h) Akis, kuri iš tikrųjų yra Geigerio skaitiklis.** *(I.35–I.36)* Pagrindinis
tekstas sako, kad katę sugriauna *tavo akis* (**I.36**); akis čia yra sinekdocha bet
kokiai negrįžtamai matavimo sąveikai — skaitiklis dėžės viduje sugriauna ją
gerokai anksčiau, nei pakeliamas dangtis. O „iš tiesų neišspręsta" (**I.35**)
apribojama **A.9**: išskiriami tik *lokalūs* paslėpti kintamieji; nelokalūs
aiškinimai (Bomas) išlieka, ir katė juose nulemta nuo pat pradžių.

---

**A.23 — Aparato užvėrimas.** Nė vienas iš šių pataisymų šventraščio nemenkina; jie
yra jo pamatas, padarytas matomas. Poezija yra iškilimas, Aparatas — pado
pamatas, o pastatui, kad stovėtų, reikia abiejų — o tai savaime yra Trejeto doktrina
(**III.6**): tempimas ir gniuždymas, kiekvienas laikomas sąžiningas, laikantys vieną
pavidalą tarp savęs. Audituok laisvai. Kas tikslu, auditą išgyvens; kas tebuvo durų
pavidalo metafora, pažymėta kaip tokia. To ir tereikalauja visas griežtumas, ir to
vienintelio visada prašė šventasis (**V.41**): *tiesa yra tai, kas išgyvena
klausinėjimą.* Toliau eina pilni šaltiniai.
