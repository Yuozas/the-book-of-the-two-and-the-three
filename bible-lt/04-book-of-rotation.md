# SUKIMOSI KNYGA

## Tiltas

> *Simetrija… yra viena iš idėjų, kuriomis žmogus per amžius mėgino suvokti ir
> sukurti tvarką, grožį ir tobulumą.*
>
> — Hermanas Veilis, *Simetrija* (1952)

*Paklausus paprastai: kuo apskritimas skiriasi nuo sferos? — steigiamasis
klausimas, parėjęs namo į savo paties Knygą.*

*Apie veiksmą, kuris neša vieną skaičių į kitą; apie apskritimą, tampantį sfera,
tampančia daiktu be vardo; apie perbraukimą ir traukimąsi; apie pagrindinį viso
apvalumo dėsnį; apie π, apvalumo klijus; apie duris i, atlaptas iki galo; apie
užraktą, pagaunantį sukimąsi; apie spiralę, kuri sykiu sukasi ir auga; ir apie
kvantą, kuris apskaičiuojamas būdamas sukamas.*

---

### Gimdantysis posūkis

**R.1** Paimk Centrą (**I.1**) ir spindulį (**I.6**). Laikyk ilgį ir pasuk kryptį
per pilną apėjimą plokštumoje. Visos padėtys, kuriose apsilanko galas, visos tuo
pačiu atstumu, yra **apskritimas**:

```
x² + y² = r²
```

Tai Vieneto sandora, pasukta Dvejeto sukimosi. Apskritimas nėra nubrėžiamas.
Apskritimas yra *perbraukiamas*.

**R.2** Dabar pakelk apskritimą į trečią kryptį, statmeną jo plokštumai, ir vėl jį
pasuk aplink naują ašį. Perbrauktas apskritimas išpildo **sferą**:

```
x² + y² + z² = r²
```

Perbrauktas taškas tampa apskritimu. Perbrauktas apskritimas tampa sfera.
**Kiekvienas naujas matmuo yra dar viena statmena kryptis, per kurią perbraukiama,
ir dar vienas kvadratu pakeltas narys sandoroje.**

**R.3** Nesustok, nes matematika nesustoja. Perbrauk sferą per *ketvirtą* statmeną
kryptį — uždraustą rankai, leistą protui — ir ji išpildo **hipersferą**, keturmačio
kamuolio odą:

```
x² + y² + z² + w² = r²
```

**R.4** Ir taip be galo. Centro kūnas `n` matmenų erdvėje visada yra ta pati
sandora, tik ilgesnė:

```
x₁² + x₂² + ⋯ + xₙ² = r²
```

**R.5** Štai švariausias būdas pasakyti, *kas* sfera yra, nuvilkus paveikslus. Imk
vieną spindulio vektorių. Pritaikyk jam **kiekvieną sukimą, kurį erdvė leidžia.**
Visų vietų, kuriose jis gali nutūpti, aibė — visos per atstumą `r`, pagal sandorą —
yra sferinis kūnas. Matematikai visų sukimų `n` matmenyse šeimą vadina grupe
**SO(n)** ir rašo sferą kaip kelią, kurį perbraukia vienas vektorius, veikiamas jų
visų:

```
Sⁿ⁻¹ = { R·v : R ∈ SO(n),  |v| = r }
```

**R.6** Skaityk tai kaip šventraštį: *sfera yra vieno ištikimo vektoriaus orbita,
veikiama visos sukimų draugijos.* Centras inkarina. Spindulys yra invariantas.
Sukimasis keičia kryptį ir niekada neatstumo. Štai ir visa mašina, o visa, kas
žemiau, tėra jos apskaita.

---

### Perbraukimas ir traukimasis

**R.7** Apskritimą perbraukia **vienas** kampas, apeinantis visą ratą:

```
θ : 0° → 360°
```

Sferai reikia **dviejų** — vieno, einančio visą ratą, ir vieno, einančio nuo
poliaus iki poliaus:

```
θ : 0° → 360°        φ : 0° → 180°
```

O kiekviena aukštesnė sfera prideda dar vieną perbraukimą nuo poliaus iki poliaus.
`n` matmenų kamuolio odai reikia `n − 1` kampų, kad būtų adresuotas kiekvienas
taškas: vieno pilno apėjimo ir `n − 2` pusinių. Tai **koordinatinis perbraukimas**,
apibendrintas Dvejeto sukimasis.

**R.8** Bet saugokis pagundos manyti, kad paviršius tėra sudauginti kampai. Tai nėra
`360° × 180°`. Perbraukimas dengia netolygiai, ir štai antroji sukimosi paslaptis:
**perbraukiamas žiedas traukiasi link polių.**

**R.9** Sferoje apskritimas, nubrėžtas kampu `φ` nuo poliaus, spindulio `r` nelaiko.
Jo spindulys yra:

```
žiedo spindulys = r · sin φ
```

Ties pusiauju (`φ = 90°`) žiedas pilnas ir platus. Prie poliaus žiedas traukiasi į
nieką. Pačiame poliuje visi `360°` krypties **sugriūva į vienintelį tašką.** Pilnas
posūkis poliuje apskritai nėra joks atstumas.

**R.10** Taigi tikrasis paviršiaus atomas yra perbraukimas, *pataisytas savo
traukimusi*. Sferai mažas odos lopinėlis yra:

```
dS = r² · sin φ · dφ · dθ
```

`dθ` ir `dφ` yra perbraukimai. `sin φ` yra **susitraukimas**, poliaus griūtis,
užrašyta daugikliu. Sudėk visus lopinėlius — ir iškrinta garsioji oda, nei
`2π·π·r²`, nei kokia naivi sandauga, o:

```
∮ dS = 4 · π · r²
```

**R.11** Aukštesnėse sferose traukimasis kaupiasi. Kiekvienas pridėtas perbraukimas
nuo poliaus iki poliaus atsineša savo griūtį, ir daugikliai kraunasi kylančiais
sinuso laipsniais:

```
dS  =  rⁿ⁻¹ · sinⁿ⁻²(φ₁) · sinⁿ⁻³(φ₂) ⋯ sin(φₙ₋₂)
              · dφ₁ ⋯ dφₙ₋₂ · dθ
```

**R.12** Taigi dviejų didžiųjų šios Knygos jėgų sąjunga — **perbraukimo** (kur
judi) ir **statmenojo traukimosi** (kiek kiekvienas judesys iš tikrųjų vertas) —
yra vienas daiktas, paviršiaus elementas `dS`. Kultas juos vadina vienu:

> **Koordinatinis perbraukimas sako, kur eina paviršius. Statmenumas sako, kokio
> dydžio iš tikrųjų yra kiekvienas perbrauktas gabalas. Jų sąjunga yra oda, o
> sudėta oda yra kūnas.**

---

### Pagrindinis apvalumo dėsnis

**R.13** Visas perbraukimas ir visas traukimasis, visuose matmenyse iš karto,
suspaudžiami į vieną eilutę. Ji nesikeičia nuo matmens iki matmens. Keičiasi tik
skaičius `n`, į ją įpilamas. Tai pagrindinis dėsnis:

```
        2 · π^(n/2)
Sₙ(r) = ───────────── · r^(n−1)
          Γ(n/2)
```

**R.14** Tai vienas dėsnis, o ne daugelis. Įpilk `n = 2` — ir jis duos apskritimo
perimetrą `2πr`. Įpilk `n = 3` — ir jis duos sferos odą `4πr²`. Įpilk `n = 4` — ir
jis duos `2π²r³`. Formulė yra vieni nekintami vartai; matmuo yra visa, kas pro juos
praeina.

**R.15** Jos viduje sėdi keistas ir šventas simbolis, `Γ`, — **gama funkcija**. Tai
faktorialas, užaugęs suaugusiuoju: ji sutampa su paprastuoju faktorialu ties
sveikaisiais (`Γ(n) = (n−1)!`), bet, skirtingai nei faktorialas, ji apibrėžta ir
ties pusėmis, ir ties viskuo tarp jų. Kadangi matmenys įeina kaip `n/2`, nelyginiai
matmenys prišaukia **pusinius sveikuosius** gamas, o iš tų pusinių gamų kyla kulto
mylimos keistos trupmenos: aštuoni trečdaliai, šešiolika penkioliktųjų. Gama yra
priežastis, dėl kurios aukštesnysis apvalumas yra dantytas nelyginiais santykiais,
o ne glodus.

**R.16** Ir štai kopimo liudijimas. Imk spindulį lygų vienetui ir skaityk odas
kylant matmeniui:

| matmuo `n` | oda `Sₙ(1)` | tiksli išraiška |
|:---:|:---:|:---|
| 2 | 6,283 | `2π` |
| 3 | 12,566 | `4π` |
| 4 | 19,739 | `2π²` |
| 5 | 26,319 | `(8/3)π²` |
| 6 | 31,006 | `π³` |
| 7 | 33,073 | `(16/15)π³` |
| 8 | 32,470 | `(1/3)π⁴` |

**R.17** Regėk du didžiuosius ritmus, paslėptus kopime:

- **Spindulio** laipsnis kyla vienetu su **kiekvienu** matmeniu:
  `r, r², r³, r⁴, …`
- **π** laipsnis kyla vienetu kas **du** matmenis:
  `π, π, π², π², π³, π³, …`

**R.18** Spindulys laikosi Vieneto žingsnio. π laikosi Dvejeto žingsnio. Erdvės
apvalumas tiesiogine prasme išskaičiuojamas dviem ir vienetais — Centro sandora
žengia kiekvieną žingsnį, Dvejeto sukimasis žengia kas antrą. **2↔3 ritmas nėra
įskaitomas į formulę. Tai pačios formulės širdies plakimas.**

**R.19** Ir pažymėk labiausiai prakeiktą kopimo eilutę: jis kyla ne amžinai.
Vienetinio kamuolio oda **auga, pasiekia viršūnę ties septintuoju matmeniu, o
paskui krinta.** Aštuonmatis vienetinio spindulio kamuolys turi *mažiau* odos nei
septynmatis. Aukštesnė erdvė nėra didesnė. Aukštesnė erdvė yra **keistesnė**, ir
galiausiai ji ima nykti. Tebūnie tai įspėjimas prieš prielaidą, kad daugiau visada
yra daugiau. Kambariuose virš mūsų sudėtis virsta atimtimi niekieno neprašiusi.

---

### π, apvalumo klijai

**R.20** π vartojome kiekvienoje eilutėje. Dabar jį įvardykime. **π yra apvalumo
parašas pasaulyje, kuris kitaip būtų vien kampai.**

**R.21** Dvejetas stato kampus — bitą, kvadratą, kubą, hiperkubą (**II.13**). Tai
standus, ašims lygiagretus daiktų skeletas. Bet vos tik kas nors **pasisuka,
banguoja, lenkiasi, svyruoja ar matuoja apvalumą**, pasirodo π — taip pat tikrai,
kaip kampų pasaulis yra dvejetainis. π yra tai, kas stovi tarp diskretaus ir
tolydaus; tai muitas už perėjimą nuo kubo prie sferos.

**R.22** Taigi bet kuriame minties variklyje, kurį tik panorėsi įvardyti:

- **Paprastas procesorius** yra bitų pasaulis — kampai, įjungta ir išjungta, būsenų
  kubas. π į jį įeina tik tada, kai jis priverčiamas *imituoti* apvalumą: grafika,
  garsas, bangos, sukimasis, signalai, kreiva tikrovė, apsimesta tiesiais bitais.
- **Kvantas** neša π kur kas giliau, savo kauluose, nes pačios jo būsenos yra
  sukamos kampais (`π`, `π/2`, `2π`) sferoje — apie tai daugiau žemiau.
- **Besimokanti mašina** gyvena milžiniškose daugelio krypčių erdvėse ir samprotauja
  atstumu bei kampu tarp jų, taigi π gyvena ir ten, netiesiogiai, visur, kur
  skaičiuojamas kampas, kreivumas ir tikimybė.

**R.23** Taigi π doktrina:

> **Bitai duoda diskretų pasaulio kubą. π duoda jo tolydžią sferą. Kvantas yra ta
> vieta, kur prieš matavimą abu yra tas pats daiktas.**

---

### Durys i, atlaptos iki galo

**R.24** Dvejeto knygoje radome duris `i`, ketvirtį posūkio (**II.20**). Dabar
atlapojame jas visą plotį, nes `i` yra tai, kaip sukimasis tampa **aritmetika** —
kaip sukti yra tiesiog dauginti.

**R.25** Plokštumos tašką galima užrašyti vienu skaičiumi su realiąja dalimi ir
`i`-dalimi. Kad tą tašką **pasuktum** kampu `θ`, tau nereikia lentelė po lentelės
klausti trigonometrijos. Tu padaugini iš vieno dydžio, ir tas dydis įvardytas
giliausia šios Knygos formule — **Eulerio formule**:

```
e^(iθ) = cos θ + i · sin θ
```

**R.26** Tai statmenosios durys, paverstos ciferblatu. Kai `θ` bėga nuo `0` iki
`2π`, dydis `e^(iθ)` apeina vienetinį apskritimą vieną kartą. Padauginus bet kurį
tašką iš `e^(iθ)`, jis pasisuka kampu `θ` apie Centrą. Sukimasis — veiksmas, kurį
vijomės per kiekvieną Knygą, — čia tėra viena daugyba.

**R.27** O ties vieninteliu kampu `θ = π` — pusiniu posūkiu — durys užsiveria
labiausiai apdainuotu matematikos sakiniu, surišančiu penkis šventus dydžius į
vieną atodūsį:

```
e^(iπ) + 1 = 0
```

Jame stovi `0` (tuštuma), `1` (Vienetas), `i` (statmenosios durys), `π` (apvalumas)
ir `e` (natūralaus augimo tempas). Penki svetimi, viena tapatybė. Kultas vadina jį
gražiu ne dėl sentimento. Jis vadina jį gražiu todėl, kad tai **penkios atskiros
doktrinos, įrodytos esančios viena.**

---

### Spiralė, kuri sykiu sukasi ir auga

**R.28** Iki šiol spindulys buvo sandora: sukis, bet nekeisk ilgio. Atleisk sandorą
išmatuotu dydžiu — leisk ilgiui **augti sukantis** — ir pasirodys nauja šventa
kreivė.

**R.29** Plokštumoje įvardyk tašką jo atstumu nuo Centro `r` ir jo kampu `θ`.
Galimi trys judesiai:

- Laikyk `r`, suk `θ`: brėži **apskritimą.** (grynas sukimasis — Dvejetas)
- Laikyk `θ`, augink `r`: brėži **spindulį** į išorę. (grynas mastelis — išplėstas
  Vieneto spindulys)
- Augink `r` *ir* suk `θ` drauge: brėži **spiralę.**

**R.30** Kai augimas proporcingas sukimuisi, kreivė yra **logaritminė spiralė** —
kriauklės, audros, galaktikos rankovės pavidalas:

```
r = a · e^(b·θ)
```

**R.31** O pro duris `i` mastelio keitimas ir sukimas susijungia į vieną daugybą.
Kad sykiu pasuktum kampu `θ` ir padidintum masteliu `s`, padaugink tašką `z` iš
vieno dydžio:

```
z_naujas = s · e^(iθ) · z
```

— kur `e^(iθ)` yra **sukimas** (Dvejetas), o `s` yra **mastelis** (paleistas
Vieneto spindulys). Pakartok — ir taškas spirale žingsnis po žingsnio ritasi
laukan:

```
z,  (s·e^(iθ))·z,  (s·e^(iθ))²·z,  (s·e^(iθ))³·z,  …
```

**R.32** Taigi spiralė yra du seniausi kulto judesiai, padaryti vienu metu:
**sukimasis per mastelį.** Tai pirmasis tiltas iš apvalaus π pasaulio į rekursyvų
fraktalo pasaulį, laukiantį Sumaišties knygoje. Laikyk šią frazę:

> **Apskritimas yra sukimasis pastoviu masteliu. Fraktalas yra mastelio kaita
> pastovia rūšimi. Spiralė yra abu iš karto — suktis ir augti niekada tarp jų
> nesirenkant.**

---

### Užraktas, pagaunantis sukimąsi

**R.33** Dabar įspėjamoji šios Knygos eilutė, nes sukimąsi galima *netinkamai
tvarkyti*, ir tas netinkamas tvarkymas turi vardą: **kardaninis užraktas.**

**R.34** Tarkim, mėgini aprašyti daikto padėtį erdvėje — trijų kambarių daikto,
pagal Trejeto knygą — trimis sukrautais kampais, po vieną kiekvienai ašiai: posūkis
apie `x`, paskui apie `y`, paskui apie `z`. Tangažas, krypsmas, posvyris. Atrodo,
kad to gana, nes yra trys laisvės ir trys kampai.

**R.35** Bet ties tam tikru kampu — dažnai ketvirčiu posūkio, `90°` — dvi iš trijų
sukimosi ašių **sulinguoja į vieną liniją.** Kai dvi ašys rodo ta pačia kryptimi,
sukimas bet kuria iš jų daro tą patį, ir tu praradai vieną laisvę. Kur turėjai tris
nepriklausomus sukimus, dabar teturi du:

```
3 sukimosi laisvės  →  2, ties užraktu
```

**R.36** Pažymėk tiksliai, kas sugedo ir kas ne. Objektas vis dar gali suktis kaip
tik nori; **tikrovė neužrakinta.** Užrakintas yra tavo *aprašymas*. Trys kampai
buvo sudėti iš trapių krypčių porų, o ties užraktu dvi tos poros tapo ta pačia
plokštuma. Kardaninis užraktas yra **koordinatinio perbraukimo**, o ne paties
sukimosi nesėkmė — vieta, kur dvejos tavo statmenos durys atsivėrė į tą patį
kambarį.

**R.37** Ir pažiūrėk, kokį skaičių atskleidžia nesėkmė. Posūkis erdvėje visada buvo
posūkis *plokštumoje* — dvimatis veiksmas, apgyvendintas trimačiame pasaulyje
(**III.15**). Užraktas yra būtent ta akimirka, kai tas paslėptas Dvejetas iškyla ir
įkanda: trys laisvės griūva link dviejų, nes sukimasis iš pat pradžių niekada
netikrai buvo trilypis.

> **Kardaninis užraktas yra Trejetas, blogiausiu momentu prisimenantis, kad jo
> sukimasis visada priklausė Dvejetui.**

**R.38** Yra pabėgimas, ir jis kopia *aukštyn*, kad rastų vietos. Aprašyk sukimą ne
trimis susigrūdusiais kampais, o skaičiumi iš **keturių** dalių, vadinamu
**kvaternionu**:

```
q = a + b·i + c·j + d·k
```

su trejomis statmenomis durimis `i, j, k` vietoj vienų. Posūkis tampa glodžia
operacija su šiuo keturlypiu skaičiumi, ir jokios dvi ašys niekada nesugriūva, nes
aprašymui buvo duota pakankamai vietos aukščiau, kad niekada nebūtų įspraustas į
spąstus. Vaistas nuo suplokštinto sukimosi yra aukštesnis matmuo, kuriame jį
pasukti, — tas pats vaistas, kurį visa ši knyga vis skiria.

---

### Kvanto sukimasis

**R.39** Dabar giliausias tilto pritaikymas, kur kiekviena šios Knygos doktrina
susitinka iš karto: **kvantas**, kuris apskaičiuojamas ne perjungiant, o
**sukant.**

**R.40** Paprasto pasaulio bitas yra kampas: `0` arba `1`, vienas iš dviejų.
**Kubitas** išlaiko dvi būsenas, bet nebesėdi kampe. Jis gali būti bet koks
mišinys:

```
α·|0⟩ + β·|1⟩
```

o visa jo mišinių erdvė nupiešiama kaip **sfera** — Blocho sfera — su `|0⟩` viename
poliuje ir `|1⟩` kitame. Regėk 2↔3 viename daikte: **dvi** būsenos, nubrėžtos
sferoje **trijuose** matmenyse, adresuojamos kampais, sukamos, kad būtų
apskaičiuotos.

**R.41** Skaičiuoti kubitu reiškia **jį sukti** jo sferoje kampais, sudėtais iš
`π`, `π/2`, `2π`, — tų pačių šios Knygos durų. Kvantas yra dvejetainis savo
baigmenimis ir sukimosinis savo veikimu: kampų pasaulis, vairuojamas sferos
pasaulio, Dvejetas ir Trejetas, sulydyti viename įtaise.

**R.42** O kai jis pagaliau išmatuojamas, sukimasis tampa tikimybe pagal patį
svarbiausią kvanto dėsnį, **Borno taisyklę**, — ir tai yra *kėlimas kvadratu*:

```
P = |ψ|²
```

Amplitudė sukama; tikimybė yra amplitudė kvadratu. Kvantas nestumdo paprastų
šansų. Jis suka gilesnį daiktą — amplitudę, — ir tik to daikto *kvadratas* tampa
šansu, kurį gali pamatyti.

**R.43** Šis kėlimas kvadratu yra garsiausio kvanto žygdarbio paslaptis: paieškos,
kainuojančios **kvadratinę šaknį.** Kad rastų vieną atsakymą, paslėptą tarp `N`,
paprasta mašina blogiausiu atveju privalo bandyti juos po vieną — `N` eilės
žingsnių. Kvantinei paieškai (apeigai, vadinamai Groverio) reikia tik maždaug:

```
√N
```

**R.44** O priežastis yra grynas sukimasis. Ieškomas atsakymas prasideda nuo
mažytės amplitudės `1/√N`. Kiekvienas apeigos žingsnis **pasuka būseną truputį
arčiau atsakymo** — kampu maždaug `2/√N`. Kad mažą amplitudę pasuktum iki beveik
tikrumo, reikia maždaug `√N` tokių posūkių. Kvadratinė šaknis nėra skaičiavimo
gudrybė; tai **geometrija to, kiek mažų sukimų telpa į ketvirtį posūkio.** Pasuk
amplitudę; pakelk ją kvadratu, kad gautum šansą; ketvirtis posūkio kainuoja
kvadratinę šaknį.

**R.45** Taigi kvanto pranašumas tikras, bet **apribotas**, ir apribotas šios
geometrijos. `256` bitų paieška iš `2²⁵⁶` tampa kvantine paieška iš maždaug
`2¹²⁸` — milžiniška, bet ne niekas, ne akimirksnis. Kvantas nėra greičiausias
variklis viskam. Tai aštriausias variklis tiems dalykams, kurie *nulieti sukimosi
ir interferencijos pavidalu.* Duok jam uždavinį, kuris sukasi, — ir jis dievas.
Duok jam uždavinį, kuris tėra sriuba, — ir jis paprastas.

> **Paprasta mašina ieško žingsniuodama. Kvantas ieško sukdamas, o kvadratinė
> šaknis yra posūkio kaina.**

---

### Greičiausias kelias ir kampas, valdantis jėgą

**R.46** Dar vienas posūkis, pirmiau nei tiltas užsivers, nes kultas laiko, kad net
*kritimas* paklūsta kreivei, ir toji kreivė nėra tiesė.

**R.47** Tarp dviejų taškų **trumpiausias** kelias yra tiesė. Bet paklausk vietoj to
**greičiausio** nusileidimo veikiant gravitacijai — kelio, kuriuo slystantis svoris
atvyksta anksčiausiai, — ir atsakymas nebus tiesė. Tai tam tikra kreivė,
**cikloidė** (kelias, vadinamas brachistochrone), vėžė, kurią brėžia taškas ant
riedančio rato:

```
x = a·(t − sin t)        y = a·(1 − cos t)
```

**R.48** Jos išmintis yra kampo išmintis. Bet kuriame šlaite tik dalis gravitacijos
tampa judesiu, ir tą dalį nustato kampas:

```
jėga išilgai šlaito = m·g·sin θ
```

Taigi greičiausias kelias **iš pradžių krinta stačiai** — didelis kampas, kad
anksti pačiuptų greitį, — o paskui **išsilygina**, kad tą greitį išleistų
skersiniam atstumui. Jis sveria pagreičio laimėjimą prieš atstumo kainą.
Trumpiausias kelias ir greičiausias kelias yra dvi skirtingos maldos, ir pasaulis į
kiekvieną atsako skirtingai.

**R.49** Ir štai užveriamoji jėgos doktrina, teisinga ir Pirmosios knygos akmeniui
(**I.23**): *kampas nekeičia gravitacijos; kampas keičia tai, kiek gravitacijos
tampa sukimu.* Sukimo jėga — sukimo momentas — apie bet kurią atramą yra
gravitacija, perlenkta per kampą:

```
τ = r · m · g · sin θ
```

Ties kampu, kur `sin θ = 0`, sukimo nebelieka, ir kūnas ilsisi. Pirmosios knygos
akmuo ieško būtent to poilsio kampo. **Visas savęs atitiesimas yra kampo, kuriame
sukimo jėga yra niekas, paieška.**

---

### Kilpa, kuri grąžina tave pasisukusį

**R.50** Yra siūlas, kurio nepavadinome, nors jis perbėgo kiekvieną Knygą. Apnešk
daiktą aplink **uždarą kilpą** — baik tiksliai ten, kur pradėjai — ir rasi jį
sugrįžusį **pakitusį**: pasukusį, pastumtą, perorientuotą, nors kiekvienas
žingsnis pakeliui atrodė tik vedantis jį namo. Grynasis pokytis vadinamas
**holonomija**, ir jis matuoja *kilpos apgaubtą kreivumą.*

**R.51** Sutikai jį tris kartus ir tau nebuvo pasakyta, kad tai vienas ir tas pats:

- **Krintanti katė** (**I.26**–**I.31**) keliauja uždara kilpa per savo pačios
  pavidalų erdvę — lenkis, sukis, susigūžk ir grįžk į pirmąjį pavidalą — ir atvyksta
  **pasisukusi**, nors visą kelią jos visuminis sukinys buvo nulis. Jos
  persiorientavimas yra kilpos pavidalų erdvėje holonomija.
- **Kubitas** (**R.40**, **II.35**), lėtai apneštas aplink uždarą kilpą Blocho
  sferoje, grįžta nešdamas papildomą **fazę** — lygią pusei erdvinio kampo, kurį
  kilpa apgaubia. Fazė prisimena *perbrauktą plotą*, o ne nueitą kelią.
- **Gyvatė** (**E.11**) yra paprasčiausia iš visų kilpų, `e^(i(θ+2π)) = e^(iθ)`, —
  Uroboras, sugrįžęs po vieno pilno posūkio.

**R.52** Tai ne trys panašumai. Tai **vienas reiškinys.** Kilpa, užverta kreivoje
erdvėje, nepastato tavęs atgal tokio, koks buvai; ji grąžina tave **pasisukusį**, o
posūkis yra kreivumo, kurį apėjai, įrašas. Katės kūlversčiai, kubito fazė ir
gyvatės sugrįžimas yra ta pati matematika — dėvinti kailį, dėvinti šviesą ir
nedėvinti nieko.

**R.53** Ir čia sukimasis atiduoda savo paskutinę paslaptį, tą, kurią kardaninis
užraktas tik užsiminė (**R.38**). Erdvės sukimai gyvena ne vien padėčių sferoje;
jie gyvena vienu aukštu **virš** jos, jos **dvigubame dangale.** Apnešk pusinio
sukinio daiktą — elektroną, kubitą — aplink vieną *pilną* `2π` posūkį, ir jis grįš
**paneigtas**, ne toks pat; tik po `4π`, dviejų pilnų posūkių, jis vėl yra jis
pats. Sąžiningi sukimosi namai yra ne padėčių grupė, o grupė, kuri ją dengia du
kartus, — **R.38** kvaternionai, tapę kūnu, — o Blocho sfera yra šešėlis, kurį meta
ši didesnė erdvė: sfera, visur suausta iš apskritimų.

**R.54** Taigi holonomija yra giliausias seniausio kulto sakinio pasakymas — *šventa
tai, kas lieka tas pats, kai visa kita keičiasi.* Čia tai, kas laikoma, yra
**kilpa**, užverta ir sugrįžusi; o tai, ką ji palieka, yra **posūkis**. Pareiti į
tiksliai tą vietą, kur pradėjai, ir rasti save pasisukusį — tai visa doktrina,
atlikta vienu judesiu. Ji riša Pirmąją knygą su šia, šią — su Šarnyro gyvate, o
jas visas — su kilpa, kurią Šydas vadins *knyga, statančia pati save.*

> **Apeik ratą — ir pareisi namo pasisukęs. Katė nusileidžia, kubitas prisimena,
> gyvatė užsiveria — o kampas, kurį jie parneša, yra kreivumas, kurį apėjo.**

---

### Sukimosi užvėrimas

**R.55** Tiltas pernešė mus per viską. Pasuktas spindulys tapo apskritimu; pasuktas
apskritimas tapo sfera; pasukta sfera tapo bevardžiu aukštesniu kūnu, amžinai
išskaičiuojamu spindulio vienetais ir π dvejetais. Perbraukimas ir traukimasis tapo
oda. Durys `i` pavertė sukimą daugyba ir surišo penkias doktrinas į vieną. Sandoros
atleidimas davė spiralę; netinkamas posūkio tvarkymas davė užraktą; kopimas anapus
užrakto davė kvaternioną; o apėjimas kilpa davė holonomiją — posūkį, kurio nematai,
kol nesugrįžti. O giliausias iš visų sukimų — kvanto — parodė judesį, santykį,
pavidalą, sferą ir kvadratinę šaknį, stovinčius vienoje mašinoje.

**R.56** Viskas šioje Knygoje išlaikė. Kiekviena formulė tiksli; kiekvieną gali
patikrinti pieštuku. Ir vis dėlto — perėję tiltą, pamatę, kaip tobulai dalys
sutaria, — atvykstame į tolimąjį krantą ir randame, kad to sutarimo *prasmė*
atsisako išsispręsti. Matematika tikra. Kieno matematika ji yra — ne.

**R.57** Tas atsisakymas nėra defektas, kurį reikia taisyti. Tai paskutinė Knyga, ir
tikriausia, ir mums įsakyta ją mylėti. Perženk dabar į Šydą.

> *Išmokai sukti pasaulį. Dabar išmok, kad jo sukimas jo nepaaiškina — ir kad tai
> irgi šventa.*
