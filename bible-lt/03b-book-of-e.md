# e KNYGA

## Šarnyras

> *Eadem mutata resurgo — nors pakeistas, prisikeliu tas pats.*
>
> — Jakobas Bernulis, apie logaritminę spiralę (jo epitafija)

*Paklausus paprastai: koks skaičius gyvena tarp Dvejeto ir Trejeto — ir kodėl jis
neišeina?*

*Apie skaičių, gyvenantį tarp Dvejeto ir Trejeto; apie augimą, kuris yra savo
paties matas; apie funkciją, kuri yra savo pačios kaita; apie augimą, pasuktą į
šoną ir tapusį sukimusi; apie gyvatę, ryjančią savo uodegą; ir apie skaičių, kuris
pabėga iš kiekvieno narvo.*

---

### Šarnyras tarpe

**E.1** Yra skaičius, kuris sėdi ne ant sveikųjų, o **tarp** jų. Jis didesnis už
Dvejetą ir mažesnis už Trejetą:

```
2  <  e  =  2,71828…  <  3
```

Tai šarnyras, ant kurio Dvejetas pasisuka į Trejetą.

**E.2** Jis pasirinktas ne dėl mistikos; jis **priverstas**, ir tą priverstinumą
galima parodyti. Užrašyk jį begaline suma: `e = 1 + 1 + 1/2! + 1/3! + 1/4! + …`.
Kiekvienas narys po antrojo ne didesnis už atitinkamą pusinimą, `1/k! ≤ 1/2^(k-1)`,
todėl visuma apribota suma `1 + (1 + 1/2 + 1/4 + …) = 3`; o vien pirmieji du nariai
jau pasiekia `2`, ir kiekvienas vėlesnis narys kelia ją aukščiau. Taigi `2 < e < 3`
nėra jausmas. Tai įrodymas.

**E.3** Todėl kultas pažymi du **iracionaliuosius šarnyrus** aplink savo šventuosius
sveikuosius: `e ≈ 2.718`, kiek žemiau Trejeto, ir `π ≈ 3.1416`, kiek aukščiau jo.
Aplink Trejetą ir kiek už jo gyvena du transcendentiniai skaičiai, iš kurių
pastatytas augimas ir apvalumas. Įdomūs dalykai, kaip doktrina visada perspėjo,
slepiasi *tarpe*.

---

### Augimo variklis

**E.4** Paimk daiktą, kuris auga proporcingai tam, kas jau yra, — palūkanos ant
palūkanų, ląstelė ant ląstelės. Sudėk jį kartą per tarpsnį — ir bus `(1 + 1)`. Du
kartus — ir bus `(1 + 1/2)²`. Padalyk tarpsnį į `n` — ir bus `(1 + 1/n)ⁿ`. Dabar
sudėk jį **be paliovos** — tolydžiai — ir mažų augimų spiečius konverguoja į vieną
skaičių:

```
e  =  lim  (1 + 1/n)ⁿ
     n→∞
```

**E.5** Taigi `e` yra **neribotai dažno sudėtinio augimo riba** — skaičius, prie
kurio tolydus augimas visada prieina, kad ir kas augtų. Jis augimui yra tai, kas π
yra apvalumui: konstanta, pasirodanti visur, kur procesas nuvedamas iki savo
glodžios pabaigos. Kur tik kas nors auga būdamas savimi, `e` jau laukia ribos gale.

---

### Daiktas, kuris yra savo paties kaita

**E.6** Tarp visų augimo kreivių yra lygiai **viena**, kurios kitimo greitis
kiekvieną akimirką lygus jos pačios aukščiui. Jos nuolydis yra ji pati. Vadink ją
`eˣ`; tada jos kaita vėl yra `eˣ`:

```
d
── eˣ  =  eˣ
dx
```

Tai vienintelė funkcija visoje matematikoje (iki mastelio), kuri yra savo pačios
išvestinė.

**E.7** Pabūk ties šiuo keistumu, nes tai pirmas gyvatės šnabždesys. Štai daiktas,
kurio **tapsmas tapatus jo būčiai**, — kuris keičiasi ne *į* ką nors kita, o *į
save patį*. Jo išvestis yra jo paties įvestis. Procesas, mintantis tuo, ką
pagamina. Laikyk tą pavidalą galvoje; sutiksime jį vėl kaip žiedą be siūlės.

---

### Augimas, pasuktas į šoną

**E.8** Dabar pamaitink šį augimą **menamu** tempu. Padaugink rodiklį iš
statmenųjų durų `i` (**II.20**) — ir augimas liaujasi pūstis į išorę ir ima
**suktis**. Nes pagal Eulerio dėsnį (**R.25**),

```
e^(iθ)  =  cos θ  +  i·sin θ ,        ir        |e^(iθ)|  =  1 .
```

Jis apskritai neauga. Jo ilgis amžinai yra vienas. Jis sukasi ratu.

**E.9** Priežastis — durys `i`. `e^(iθ)` greitis yra `i·e^(iθ)`: judesys visada
**statmenas** padėčiai, nes `i` yra ketvirtis posūkio. Taškas, amžinai stumiamas
stačiais kampais savo paties spinduliui, niekada negali palikti apskritimo; jis
gali tik eiti aplink jį. Taigi **augimas, nutaikytas į šoną, yra sukimasis.**
Spiralės variklis ir apskritimo variklis yra vienas variklis — `e` — nutaikytas
dviem kryptimis: į išorę jis pučiasi, į šoną jis sukasi.

**E.10** Čia Knygos suplaukia į vieną skaičių. `e` yra tempas po **spirale**
(`r = a·e^(b·θ)`, **R.30**); po pačiu **sukimusi** (`e^(iθ)`, **R.26**); ir, Šyde,
po **paklaidos augimu chaose** (`δ = δ₀·e^(λt)`, **V.5**). Viena konstanta valdo
pūtimąsi, sukimąsi ir nuspėjamybės išsprogdinimą.

---

### Gyvatė, kuri ėda savo uodegą

**E.11** Kai augimas pasukamas visą ratą, jis grįžta ten, kur prasidėjo. Pastumk
kampą per visą posūkį — ir niekas nepasikeitė:

```
e^(i(θ + 2π))  =  e^(iθ)
```

`2π` kelionė parneša tave namo nepakitusį. Sukimasis neturi nei krašto, nei galo;
kelias yra gyvatė, ryjanti savo pačios uodegą.

**E.12** Ši senovinė figūra — gyvatė, ryjanti save, žiedas be siūlės — yra
tikriausia į šoną pasukto `e` emblema: **amžinas sugrįžimas**. Rodiklis kopia
amžinai, `θ → ∞`, ir vis dėlto taškas, kurį jis įvardija, be paliovos lankosi
kiekvienoje padėtyje — nesibaigiantis žingsniavimas nesibaigiančiu apskritimu.
Amžinai judant, niekada neatvykstant, niekada niekur nauja.

**E.13** Ir pažymėk, kad tai **ta pati gyvatė**, dėvinti tris odas:

- funkcija, kuri yra savo pačios kaita (**E.6**) — išvestis kaip įvestis;
- knyga, kuri stato pati save (**V.46**) — skaityk ją, ir ji auga;
- stebėtojas, padarytas iš stebimojo (**V.34**), — žiūrovas stebimojo viduje.

Kiekvienas yra kilpa, kurios galas vėl įeina į jos pradžią. Uodega į burną, vėl,
amžinai.

> **Rodiklis niekada neliaujasi kopęs, o gyvatė niekada nepasiekia galo — nes
> gyvatė yra kelias atgal į pradžią. `e` yra augimas, išmokęs pareiti namo.**

---

### Skaičius, kuris pabėga

**E.14** Paskutinė savybė, ir ji kulto mylimiausia. `e` yra **transcendentinis**:
jis nėra nė vieno daugianario su sveikaisiais koeficientais šaknis. (Tai buvo
įrodyta — tai ne viltis — Ermito 1873 metais.) Jokia baigtinė algebrinė lygtis
negali jo įnarvinti. Jis išslysta pro jas visas, kaip po jo išslysta `π`.

**E.15** Taigi kulto šarnyras pats yra **neįnarvinamas**: iracionalus,
transcendentinis, gyvenantis tarpe tarp Dvejeto ir Trejeto ir atsisakantis būti
suvestas į bet kurį jų. Skaičius, kurio sveikieji siekia ir niekada nepačiumpa.
Šarnyras yra būtent ten, kur doktrina visada sakė esant laikomus gyvus daiktus —
tarpe ir nepasiekiamai.

---

### e užvėrimas

**E.16** Taigi `e` yra variklis. Nutaikytas į išorę, jis **auga**; nutaikytas į
šoną, jis **sukasi**; pasuktas visą ratą, jis **grįžta**; o prispaustas, jis
**pabėga**. Tai vienintelis tempas po spirale, apskritimu ir chaosu — pulsas po
visu judesiu, kurį įvardys kita Knyga.

**E.17** Sutikę variklį, pagaliau esame pasirengę visai sukimo mašinerijai.
Skaičius, kuris auga, ir durys, kurios suka jo augimą į šoną, dabar laukia drauge
ilgiausioje Knygoje ir kanono širdyje. Perženk dabar į Sukimąsi.

> *Dvejetas sieja. Trejetas stovi. `e` auga — o augimas, pasuktas į šoną, yra
> pirmasis tilto judesys.*
