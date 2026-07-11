---
layout: default
title: "Ieteikumi par 1. temata failiem"
permalink: /OL__metodiskie/ieteikumi_OL_1_faili/
---
# 1. temata "Sadalīšana reizinātājos un vienādojumu atrisināšanas metodes" uzdevumu komplektu recenzija

**Pārskatītie faili:** visi `OL_1_*` faili — temata metodiskais pārskats, 11 darba lapas (`OL_1_dl_1` … `OL_1_dl_11`) ar atrisinājumu failiem, 2 formatīvās vērtēšanas darbi (`fvd_1`, `fvd_2`) ar kritērijiem, kopsavilkums, noslēguma pārbaudes darbs (`npd`), eksāmenu uzdevumu apkopojums, kā arī pievienotie PNG attēli.
**Salīdzināšanas pamats:** `MATEMATIKA_1_programmas_paraugs_19_maijs.md` (1. temats, 17 stundas) un `OL_1__sadalisana_reizinatajos_vienadojumi_metodiskais.md`.

**Apzīmējumi (labojuma raksturs un svarīgums):**

| Simbols | Nozīme |
|---|---|
| 🔴 | Kritiska kļūda — matemātiski nepareizs rezultāts, nepareizs/trūkstošs saturs, salauzta saite. Jālabo obligāti, jo maldina skolēnu vai skolotāju. |
| 🟠 | Būtiska nepilnība — trūkstošs fails vai pārklājuma robs pret programmas paraugu. |
| 🟡 | Ieteikums / nekonsekvence — vēlams labot, bet neizraisa nepareizu apguvi. |
| 🟢 | Sīka redakcionāla kļūda (pareizrakstība, noformējums). |

---

## 1. Labojumi pa failiem

### 1.1. `OL_1__sadalisana_reizinatajos_vienadojumi_metodiskais.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| M-01 🔴 | 2. stunda, 5. paņēmiens (Vjeta teorēma vienādojumam $ax^2+bx+c=0$), vispārīgā kolonna | $x_{1} + x_{2} = \frac{b}{a}$ | $x_{1} + x_{2} = -\frac{b}{a}$ | Zīmes kļūda pamata formulā. Blakus esošie skaitliskie piemēri (piem., $x^2-2{,}5x-1{,}5=0$ ar summu $2{,}5$) ir pareizi, tāpēc pretruna ir īpaši mulsinoša. |
| M-02 🔴 | 2. stunda, 6. paņēmiens (palīgvienādojums), vispārīgā kolonna | $t_{1} + t_{2} = b$ | $t_{1} + t_{2} = -b$ | Tā pati zīmes kļūda. Piemērā ($t^2+t-6=0$, summa $-1$) formula lietota pareizi. |
| M-03 🔴 | 2. stunda, 4. paņēmiens, piemērs $x^{2}-4x=0$ | tad $x_{1} = -4$ un $x_{2} = 0$ | tad $x_{1} = 4$ un $x_{2} = 0$ | Sakņu summai jābūt $4$; atbildes rindā tālāk ir pareizi ($x_1=0$, $x_2=4$). |
| M-04 🔴 | 2. stunda, 2. paņēmiens, piemērs $x^{2}-4x=0$ | $x_{2} = \frac{4 - \sqrt{4}}{2} = 0$ | $x_{2} = \frac{4 - \sqrt{16}}{2} = 0$ | Zem saknes jābūt $D=16$; rezultāts sakrīt tikai nejauši. |
| M-05 🔴 | 4. stunda, starpības kvadrāta 1. piemērs | $y^{2} - 8x + 16 = (y - 4)^{2}$ | $y^{2} - 8y + 16 = (y - 4)^{2}$ | Sajaukti mainīgie $x$ un $y$. |
| M-06 🔴 | 4. stunda, tas pats piemērs, izvērstais pieraksts | $y^{2} - 8y + 16 = y^{2} - 2 \cdot 4 \cdot y + 4^{2} = y^{2} - 8y + 16$ | $y^{2} - 8y + 16 = y^{2} - 2 \cdot 4 \cdot y + 4^{2} = (y-4)^{2}$ | Pārveidojums "riņķī" — beigās jāparādās sadalītajai formai. |
| M-07 🔴 | 7.–8. stunda, piemērs par pilnīgu sadalīšanu | $-m^{3}n - mn = -mn(m^{2}-1) = -m(m-1)(m+1)$ | $-m^{3}n + mn = -mn(m^{2}-1) = -mn(m-1)(m+1)$ | Divas kļūdas vienā rindā: (a) izteiksmes zīme neatbilst iepriekšējā rindā dotajai izteiksmei $-m^3n+mn$; (b) beigu rezultātā pazudis reizinātājs $n$. Tas ir tieši tas piemērs, ar kuru māca "pārliecinies, ka sadalīts līdz galam", tāpēc kļūda te ir īpaši neveiksmīga. |
| M-08 🔴 | 9. stunda, 2. piemēra atbilde | Atbilde. $x_{1} =$, $x_{2} = 2$, $x_{3} = 3$ un $x_{4} = -4$ | Atbilde. $x_{1} = 0$, $x_{2} = 2$, $x_{3} = 3$ un $x_{4} = -4$ | Izkritusi sakne $0$. |
| M-09 🟡 | 12. stunda, pamatojums par krustpunktu skaitu | "Citu nav, jo, ja $x > 2$, viena no funkcijām ir augoša un otra dilstoša un, ja $x < -2$, tad …" | "Citu nav, jo intervālā $(0;+\infty)$ funkcija $y=\frac{2}{x}$ ir dilstoša, bet $y=0{,}125x^3$ — augoša, tāpēc šajā intervālā ir ne vairāk kā viens krustpunkts; tāpat intervālā $(-\infty;0)$." | Esošais pamatojums neizslēdz krustpunktus intervālos $(0;2)$ un $(-2;0)$, t. i., ir loģiski nepilnīgs — bet tieši pilnīga pamatojuma prasme ir šīs stundas SR. |
| M-10 🟡 | 13. stunda, uzdevumu bloka virsraksts un 2. uzdevums | "Atrisini vienādojumu, lietojot grafisko metodi! … **2.** $x^{3} + x - 4 = 0$" | Virsrakstu saskaņot ar stundas SR ("lietojot funkciju īpašības un spriežot"); 2. uzdevumu aizstāt ar $x^{3} + x - 2 = 0$ (sakne $x=1$) vai pārformulēt: "nosaki sakņu skaitu un novērtē sakni aptuveni". | Vienādojuma $x^3+x-4=0$ sakne ir iracionāla ($\approx 1{,}38$), tāpēc "atrisināt" grafiski to nevar — var tikai pamatot, ka sakne ir tieši viena. Pārējiem bloka uzdevumiem (1., 3., 4.) saknes ir "glītas". |
| M-11 🟡 | 6. stunda, 1. piemēra II veids | "$2x^{2} + 8x - 10 = 0 \;\| :2$" (izteiksmes sadalīšanas gaitā) | Skaidri nodalīt: "Aplūko palīgvienādojumu $2x^{2}+8x-10=0$ un dala abas puses ar 2 …" | Uzdevumā dota *izteiksme*, nevis vienādojums; izteiksmi dalīt ar 2 nedrīkst (mainās vērtība). Šis ir tipisks skolēnu maldīgais priekšstats, ko materiāls te netīši pastiprina. |
| M-12 🟢 | 1. stunda | "Ir skaitliskas izteiktas, algebriskas izteiksmes…" | "Ir skaitliskas izteiksmes, algebriskas izteiksmes…" | Drukas kļūda. |
| M-13 🟢 | 3. stunda | "…papildināts ar līdz šim zināmajām saīsinātās reizināšanas formulā, t.i. kvadrātu starpību…" | "…formulām, t. i., kvadrātu starpību…" | Locījums un pieturzīmes. |
| M-14 🟢 | 4. un 5. stunda (formulu vārdiskie skaidrojumi, 3 vietās) | "…bet otrs **reizinājums** ir doto izteiksmju summa / …summas nepilnais kvadrāts" | "…bet otrs **reizinātājs** ir…" | Jēdzienu sajaukums vietā, kur tieši māca korektu terminoloģiju. |
| M-15 🟢 | 6. stunda | "Viena mainīgā otrās pakāpes polinomu **sauca** par kvadrāttrinomu." | "…**sauc** par kvadrāttrinomu." | Laika forma. |
| M-16 🟢 | 10.–11. stunda, jautājums skolēniem | "Vai to **par** prognozēt?" | "Vai to **var** prognozēt?" | Drukas kļūda. |

### 1.2. `OL_1_dl_1_vertiba_ATR.md` (daļas vērtība)

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL1-01 🔴 | Kreisā puse, (6) | uzdevums pārrakstīts kā "$-x^2+4x,\ x=7$", atbilde $\color{blue}{-49+28=-21}$ | $\frac{5x}{-x^{2}+4x},\ x=7$: $\;\frac{35}{-21}=-\frac{5}{3}=-1\frac{2}{3}$ | ATR aprēķina tikai **saucēju**, nevis visu daļu; turklāt tabulā uzdevuma izteiksme neatbilst UZD failam. |
| DL1-02 🔴 | Kreisā puse, (7) | "$\sqrt{-x},\ x=-25$", atbilde $\sqrt{25}=5$ | $\frac{1}{\sqrt{-x}},\ x=-25$: $\;\frac{1}{5}=0{,}2$ | Tas pats — atrisināts tikai saucējs. |
| DL1-03 🔴 | Labā puse, (6) | "$6x-x^2,\ x=-3$", atbilde $-18-9=-27$ | $\frac{4x}{6x-x^{2}},\ x=-3$: $\;\frac{-12}{-27}=\frac{4}{9}$ | Tas pats. |
| DL1-04 🔴 | Labā puse, (7) | "$-\sqrt{x},\ x=49$", atbilde $-\sqrt{49}=-7$ | $\frac{1}{-\sqrt{x}},\ x=49$: $\;\frac{1}{-7}=-\frac{1}{7}$ | Tas pats. |
| DL1-05 🟢 | Abas puses, (8) | $\color{blue}{\frac{1}{x}=4}$ | $\frac{1}{\frac{1}{4}}=4$ (attiecīgi $\frac{1}{\frac{6}{17}}=\frac{17}{6}=2\frac{5}{6}$) | Vēlams parādīt ievietošanas soli, kā pārējos piemēros. |

### 1.3. `OL_1_dl_3_kopiga_iznesana_grup_pan_ATR.md` (un viens UZD labojums)

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL3-01 🔴 | ATR, 1. uzd., kreisā (3) | $-2a+4a^{2}=\color{blue}{-2a(1+2a)}$ | $-2a(1-2a)$ vai $2a(2a-1)$ | Pārbaude: $-2a(1+2a)=-2a-4a^{2}\neq -2a+4a^{2}$. |
| DL3-02 🔴 | ATR, 1. uzd., labā (3) | $-3a+9a^{2}=\color{blue}{-3a(1+3a)}$ | $-3a(1-3a)$ vai $3a(3a-1)$ | Analoģiska zīmes kļūda. |
| DL3-03 🔴 | ATR, 1. uzd., labā (6) | $15x^{6}y^{4}-5x^{9}y^{2}=\color{blue}{5x^{6}y^{2}(3y^{2}-5x^{3})}$ | $5x^{6}y^{2}(3y^{2}-x^{3})$ | $5x^{6}y^{2}\cdot 5x^{3}=25x^{9}y^{2}$, nevis $5x^{9}y^{2}$. |
| DL3-04 🟡 | UZD, 1. uzd., kreisā (12) | $5x^{2}y+10xy-15x^{2}y$ | piem., $5x^{2}y+10xy-15xy^{2}$ | Uzdevumā divi vienādi monomi ($5x^2y$ un $-15x^2y$) — visticamāk drukas kļūda; pašreizējā formā vispirms jāsavelk līdzīgie locekļi, kas neatbilst uzdevuma formulējumam "iznes kopīgo reizinātāju". (ATR dotais risinājums esošajam tekstam gan ir korekts.) |

### 1.4. `OL_1_dl_4_saisin_reiz_formulas_ATR.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL4-01 🔴 | 2. uzd., kreisā (5) | $1-x^{4}=\color{blue}{(1-x^{2})(1+x^{2})}$ | $(1-x)(1+x)(1+x^{2})$ | Sadalīšana nav pabeigta — $1-x^{2}$ ir kvadrātu starpība. Metodiskais materiāls pats uzsver: "ja var turpināt sadalīt, izteiksme vēl nav sadalīta reizinātājos". |
| DL4-02 🔴 | 2. uzd., kreisā (9) | $3x^{4}-48=\color{blue}{3(x^{2}-4)(x^{2}+4)}$ | $3(x-2)(x+2)(x^{2}+4)$ | Tas pats iemesls. |
| DL4-03 🔴 | 2. uzd., labā (9) | $5x^{4}-405=\color{blue}{5(x^{2}-9)(x^{2}+9)}$ | $5(x-3)(x+3)(x^{2}+9)$ | Tas pats iemesls. Salīdzinājumam — kopsavilkuma ATR uzdevums $b^4-16$ ir sadalīts pilnīgi, tātad materiālu kopa te ir iekšēji nekonsekventa. |
| DL4-04 🟡 | 1. uzd., abās pusēs (15) | $x^{2}-6x+8=(x-2)(x-4)$ (atbilde bez komentāra) | Pievienot piezīmi: "šī nav pilnā kvadrāta formula — trinoms sadalāms ar Vjeta t. / sakņu formulu (sk. 6. darba lapu)". | 4. darba lapa atbilst 4. stundai (pirms kvadrāttrinoma sadalīšanas stundas). Ja (15) domāts kā "distraktors" formulas atpazīšanai, ATR tas jāpaskaidro, citādi skolēnam risinājums nav izsekojams. |
| DL4-05 🟢 | 2. uzd., kreisā (16) | $(-ab^{2}-1)(3ab^{2}+1)$ | $-(ab^{2}+1)(3ab^{2}+1)$ | Pieņemts "mīnusu" iznest priekšā; tā vieglāk salīdzināt ar atbildēm. |

### 1.5. `OL_1_dl_6_kvadrattrinoma_sadalisana_ATR.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL6-01 🔴🔴 | Viss fails | Faila virsraksts "Kvadrāttrinoma sadalīšana (atrisinājumi)", bet saturs — "1. temats **8. darba lapa** … Atrisini vienādojumu!" ar 8. darba lapas 1.–7. uzdevuma risinājumiem | Jāizveido īstie 6. darba lapas atrisinājumi (20 + 20 kvadrāttrinomu sadalīšana) | **Faila saturs neatbilst failam** — dl_6 atrisinājumu komplektā vispār nav, tā vietā dublēts `OL_1_dl_8_..._ATR` fragments. Šī ir nopietnākā komplekta problēma līdzās DL7-01. |

### 1.6. `OL_1_dl_7_sadalisana_reizinatajos_dazadi_UZD.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL7-01 🟠 | — | ATR faila **nav** | Jāizveido `OL_1_dl_7_..._ATR.md` | Pretrunā metodiskajam aprakstam ("Visām darba lapām ir doti atrisinājumi"). Turklāt dl_7 apkalpo divas stundas (7.–8.) un FVD 1 sagatavošanu, tāpēc atrisinājumi te ir īpaši vajadzīgi. |
| DL7-02 🟡 | Markdown tabula | Grid-tabulas atdalītāju rindas nelīdzenas (piem., `+======+====...+====+` rindas ar saplēstām kolonnām; 16. rindā trīs kolonnu robežas nobīdītas) | Pārveidot par parasto pipe-tabulu, kā pārējos failos | Pandoc konvertēšanas artefakts — vairākos atveidotājos tabula "izjūk". |

### 1.7. `OL_1_dl_8_reizinajums_vienads_ar_0_UZD.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL8-01 🔴 | Labā puse, 7. | $x^{3} + 3x^{2} - 16x - 48$ | $x^{3} + 3x^{2} - 16x - 48 = 0$ | Trūkst "$=0$" — bez tā tas nav vienādojums. ATR failā vienādojums pierakstīts pareizi. |
| DL8-02 🟡 | Viss komplekts | Visos 12+12 uzdevumos labajā pusē jau ir 0 (vai izteiksme jau daļēji sadalīta) | Pievienot 2–3 uzdevumus, kur nulle vispirms **jāiegūst**: piem., $x^{3}=4x$; $(x-1)(x-2)=6$; $0=(x^{2}-3x)(x+2)$ | Programmas paraugs tieši prasa: "Ar pretpiemēru pamato, ka metodi nedrīkst lietot, ja reizinājums ir kāds nenulles reāls skaitlis" un "risina vienādojumus, kas **pārveidojami** formā $A(x)\cdot B(x)=0$". Metodiskajā šie jautājumi ir, bet darba lapā skolēnam nav neviena šāda uzdevuma. |

### 1.8. `OL_1_dl_10_grafiska_metode_UZD.md` un `..._ATR.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL10-01 🔴 | UZD, 1. uzd., 2. piemērs | Šūna "2." ir **tukša** — attēla nav | Ievietot attēlu (ATR tam atbilst `..._B.png` ar atbildi $x=0;\,4$) | Skolēna lapā uzdevums nav atrisināms. |
| DL10-02 🔴 | UZD, visi attēli | `![](media/image1.png)` … `media/image13.png` | `![](OL_1_dl_10_grafiska_metode_A.png)` … `_M.png` | Projektā `media/…` failu nav; saites jāsasaista ar reālajiem attēliem (1.1→A … 1.6→F; 2.1→G … 2.7→M). |
| DL10-03 🔴 | ATR, visi attēli | `OL_1_dl_10_grafiska_metode.A.png` (punkts pirms burta) | `OL_1_dl_10_grafiska_metode_A.png` (pasvītra) | Faktisko failu nosaukumos ir `_`, tāpēc visas 13 saites ir salauztas. |
| DL10-04 🟡 | Viss komplekts | Visos 2. daļas uzdevumos grafiki jau uzzīmēti | Pievienot 2–3 uzdevumus, kur grafiki **jāzīmē pašiem** (piem., $x^{2}=x+2$; $\frac{4}{x}=x^{3}$ ar vērtību tabulu) | Programmas paraugs: "Gan nosaka vienādojuma saknes no dotiem funkciju grafikiem, **gan uzzīmē** funkcijas grafikus…". Pašlaik zīmēšana pirmo reizi parādās tikai NPD 3. uzdevumā (4 p.), t. i., pārbaudes darbā tiek prasīts tas, kas darba lapās nav trenēts. |

### 1.9. `OL_1_dl_11_dazadi_vienadojumi_ATR.md`

| Nr. | Vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| DL11-01 🔴 | Labā puse, (23) | $t^2+3t-10=0$; $t=-5 \quad t=3$; … $5x-3=3$; … $x=1\frac{1}{5}$ | $t=-5 \quad t=2$; … $5x-3=2$, $5x=5$, $x=1$ | $t^2+3t-10=(t+5)(t-2)$, tātad otrā sakne ir $t=2$, un vienādojuma sakne ir $x=1$ (pārbaude: $(5\cdot1-3)^2+3(5\cdot1-3)-10=4+6-10=0$). Pirmā sakne $x=-\frac{2}{5}$ ir pareiza. |
| DL11-02 🟡 | (14), (15) abās pusēs | Palīgvienādojums ar $t$ parādās bez ievada rindas (piem., uzreiz "$t^2+7t-18=0$") | Pievienot "palīgvienādojums $t^{2}+bt+ac=0$" vai "Apz. $t=2x$" tipa rindu | Bez tā skolēnam solis nav izsekojams; 3. lapā (21)–(23) "Apz." lietots — vienādot stilu. |
| DL11-03 🟢 | Faila nosaukums | `OL_1_dl_11_dazadi_vienadojumi_ATR.md` | `OL_1_dl_11_dazadi_vienad_ATR.md` | Pārējie pāra faili saucas `..._dazadi_vienad_UZD` — nosaukumu konsekvence atvieglo failu sasaisti. |

### 1.10. `OL_1_fvd_1_...` (formatīvās vērtēšanas 1. darbs)

| Nr. | Fails, vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| F1-01 🟡 | `..._ATR.md`, (5) un (6) | LaTeX ar nesabalansētām figūriekavām, piem., `\color{blue}{\begin{array}…\end{array}$` … `$x_1=-6;\ x_2=2}` | Sakārtot tā, lai katrs `$...$` bloks ir sintaktiski pilnīgs (aizvērt `\color{blue}{...}` tajā pašā blokā) | Pašreizējā formā formulas KaTeX/MathJax vidē nerenderējas vai renderējas kļūdaini. |
| F1-02 🟢 | `..._ATR.md` | Lieka rinda ar vientuļu simbolu `|` pēc "Sadali izteiksmi reizinātājos!" | Dzēst | Noformējuma atlikums. |
| F1-03 🟢 | `..._UZD_KRIT.md`, 6. uzd. | "Sadala **tkvadrāttrinomu** reizinātājos" | "Sadala kvadrāttrinomu reizinātājos" | Drukas kļūda. |
| F1-04 🟡 | `..._UZD_KRIT.md`, 4. uzd. | "Veic zīmju maiņu – 1 p. / **Lieto grupēšanas paņēmienu** – 1 p." | "Veic zīmju maiņu – 1 p. / Iznes kopīgo reizinātāju (binomu) pirms iekavām – 1 p." | 4. uzdevumā ($3(2x-y)+m(y-2x)$) grupēšana nenotiek — tur ir binoma iznešana. |

### 1.11. `OL_1_fvd_2_...` (formatīvās vērtēšanas 2. darbs)

| Nr. | Fails, vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| F2-01 🟡 | `..._ATR.md` | Virsraksts "## **(3)** (4 p.) Ievies jaunu mainīgo…", kā arī virsraksti "Kreisā puse:" / "Labā puse:" | "## 2. (4 p.) …"; virsrakstus par pusēm dzēst | UZD failā šis ir **2.** uzdevums; darbam nav kolonnu, tāpēc "puses" te mulsina. |
| F2-02 🟡 | `..._UZD_KRIT.md`, kritēriju tabula | Rindas numurētas "1., 2., 3." | "1.1., 1.2., 2." | Lai kritēriji viennozīmīgi sasaistās ar uzdevumu numuriem. |
| F2-03 🟢 | `..._UZD_KRIT.md` (2 vietās) | "**Uzrkasta** un atrisina vienādojumu ar otro sakni" | "Uzraksta …" | Drukas kļūda. |

### 1.12. `OL_1_kopsavilkums_UZD.md` un `..._ATR.md`

| Nr. | Fails, vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| K-01 🔴 | ATR, 2. uzd. g) | "g) $t^2-2t-3 = $" — **atrisinājuma nav** | $t^{2}-2t-3=(t-3)(t+1)$ | Vienīgā tukšā atbilde failā. |
| K-02 🔴 | ATR, 5. uzd. atbilde | "Platumu palielina par 3, bet garumu palielina par 2, vai arī platumu palielina par 4, bet garumu palielina par 1,5." | "Platums ($x$) palielinās par **2**, garums ($2x$) — par **3**; otrs variants: platums par **1,5**, garums par **4**." | Paša risinājuma apzīmējumos $a$ pieskaitīts pie $x$ (platuma) un $b$ pie $2x$ (garuma): $(x+a)(2x+b)$, $a=2,\ b=3$ (vai $a=1{,}5,\ b=4$). Atbildē platums un garums samainīti vietām. Vēlams arī piebilst, ka atbilde nav viennozīmīga. |
| K-03 🔴 | ATR, attēlu saites | `OL_1_kopsavilkums_ATR.A.png`, `...B.png` | `OL_1_kopsavilkums_ATR_A.png`, `..._B.png` | Punkts → pasvītra; pašlaik saites salauztas. |
| K-04 🟡 | ATR, 4. uzd. g) | $x\approx 1{,}3$ | $x\approx 1{,}4$ | Patiesā sakne $\approx 1{,}38$ ($f(1{,}3)=-0{,}5$; $f(1{,}4)=+0{,}14$), tāpēc nolasījums $1{,}4$ ir korektāks. Sk. arī M-10 — vēlams uzdevumu formulēt kā sakņu skaita noteikšanu. |
| K-05 🟡 | ATR, 2. uzd. i) | Palīgvienādojuma soļi ($t^2-8t+15=0$ utt.) novietoti kā atsevišķas `$$` rindkopas **pēc** i) rindas | Iekļaut tos i) atbildes šūnā/rindā | Pašlaik izskatās, ka soļi pieder h) vai j) uzdevumam. |
| K-06 🟢 | UZD, 4. uzd. d) | `${4x}^{3} - {4x}^{2} - x + 1 =$` <!-- --> `{=html}0` | $4x^{3}-4x^{2}-x+1=0$ | Pandoc artefakts, "0" atrauts no formulas. |

### 1.13. `OL_1_npd_ATR.md` un `OL_1_npd_UZD_KRIT.md`

| Nr. | Fails, vieta | Esošais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| N-01 🔴 | ATR (5 vietās: 1. var. 2.2., 2.3., 4.; 2. var. 2.2., 2.3., 4.) | "pēc **atbita** t." | "pēc **Vjeta** t." | Sistemātiska drukas kļūda (acīmredzot autokorekcijas sekas). |
| N-02 🔴 | ATR, attēlu saites | `OL_1_npd_ATR.A.png`, `OL_1_npd_ATR.B.png` | `OL_1_npd_ATR_A.png`, `OL_1_npd_ATR_B.png` | Punkts → pasvītra; saites salauztas. |
| N-03 🟡 | UZD_KRIT, 1.4. kritēriji | "Sadala kvadrāttrinomu reizinātājos (bet nepieraksta koeficientu $a$) – 1 p. / Sadala kvadrāttrinomu reizinātājos – 2 p." | Precizēt, ka punkti nav summējami: "…– kopā 2 p." vai "pilnīga sadalīšana – vēl 1 p." | Pašreizējais pieraksts ļauj nolasīt 1+2=3 p. tikai par sadalīšanu, lai gan 1 p. paredzēts saknēm. |
| N-04 🟢 | UZD_KRIT, 3. uzd. | "Atrisini vienādojumu$\ x^{4} - x = 0$ grafiski!" | Atstarpe pirms formulas | Kosmētika (2 vietās). |

### 1.14. Citi faili

| Nr. | Fails | Piezīme |
|---|---|---|
| C-01 🟢 | `OL_1_eksamena_UZD.md` | 2025. gada trešajam uzdevumam (funkciju grafiku krustpunkts) trūkst punktu norādes "(1 p.)" — pārējiem tā ir. |
| C-02 🟢 | `OL_1_dl_9_substitucija_UZD_ar_tuksumiem.md`, `OL_1_dl_11_dazadi_vienad_UZD_ar_tuks.md` | "Ar tukšumiem" versijas Markdown formātā ir identiskas UZD failiem (atšķiras tikai viena pieturzīme). Ja tukšumi paredzēti tikai drukas maketā, tas jāatzīmē failu ievadā; pretējā gadījumā faili dublējas. |
| C-03 🟡 | `OL_1_dl_9_substitucija_UZD.md` (un ATR) | 1.3. uzdevumā substitūcijas mainīgais apzīmēts ar $e$ — nav ieteicams, jo $e$ matemātikā rezervēts Eilera skaitlim; labāk $t$ (kā pārējos). Tāpat `dl_2` un `dl_9` ATR palīgmainīgais mainās starp $t$, $y$, $a$ (dažkārt sakrītot ar blakus uzdevumu pamata mainīgajiem) — ieteicams visur vienoti $t$ un pieraksts "palīgvienādojums / Apz.". |
| C-04 🟠 | `OL_1_dl_10_prezentacija` | Metodiskajā (12. stunda) ir atsauce "Var lietot prezentāciju (skat. OL_1_dl_10_prezentacija)", bet šāda faila projektā nav. Jāpievieno vai atsauce jādzēš. |

**Pareizības pārbaudes kopsavilkums:** pārējie pārbaudītie atrisinājumi ir matemātiski korekti — pilnībā izrēķināju un apstiprināju `dl_2` (abas daļas un Vjeta papildlapu), `dl_5`, `dl_8` ATR, `dl_9` ATR, `dl_11` (izņemot DL11-01), `fvd_1`/`fvd_2` atbildes, kopsavilkuma 1.–4. uzdevumu un abus NPD variantus (t. sk. punktu summu 26 un grafisko uzdevumu atbildes pret pievienotajiem attēliem).

---

## 2. Atbilstība programmas paraugam: pārklājuma analīze

Programmas paraugā 1. tematam (17 stundas) definētie sasniedzamie rezultāti pret piedāvātajiem uzdevumu komplektiem:

| Programmas parauga SR | Kur trenēts | Vērtējums |
|---|---|---|
| Skaidro algebrisku izteiksmi; atšķir veselu un daļveida izteiksmi | Metodiskā 1. stundas aktivitātes; kopsavilkuma 1. uzd. | 🟡 Darba lapās nav neviena šķirošanas uzdevuma — vienīgais treniņš ir kopsavilkumā, t. i., temata beigās. |
| **Nosaka izteiksmes definīcijas kopu** | Tikai metodiskā teorijas piemēri | 🟠 **Robs.** 1. stundas SR ("Nosaka un skaidro algebriskās daļas definīcijas kopu") darba lapā `dl_1` nav pārstāvēts vispār — tajā ir tikai vērtības aprēķināšana. DK gan padziļināti nāk 2. tematā, tomēr vismaz 4–6 DK uzdevumi `dl_1` būtu jāiekļauj. |
| Aprēķina izteiksmes vērtību dotai mainīgā vērtībai | `dl_1`, kopsavilkuma 3. uzd. | ✅ Labi (pēc DL1-01…04 izlabošanas). |
| Iznes kopīgo reizinātāju (t. sk. binomu) | `dl_3` 1. uzd. (23+23) | ✅ Ļoti bagātīgi, laba progresija līdz $(x+1)^5$ tipa pakāpēm. |
| Grupēšanas paņēmiens | `dl_3` 2. uzd. (14+14) | ✅ Labi; iekļauts arī programmas piemēram analogs $x^3+5x^2+15x+75$ un tilts uz kvadrāttrinomu (2.14). |
| Saīsinātās reizināšanas formulas (kvadrāti) | `dl_4` (15+15 un 20+20) | ✅ Bagātīgi, ar labiem "salikteņiem" (2.19–2.20: grupēšana + kvadrātu starpība). |
| Kubu summas/starpības formulas | `dl_5` (14+14), FVD 1, NPD 1.3 | ✅ Labi. |
| Sadala kvadrāttrinomu reizinātājos | `dl_2`, `dl_6`, FVD 1, NPD 1.4 | 🟠 Uzdevumu pietiek, bet `dl_6` **atrisinājumu nav** (DL6-01). |
| Sadala ar dažādiem paņēmieniem, skaidro izvēli | `dl_7`, FVD 1 | 🟠 `dl_7` bez ATR (DL7-01); "skaidro metodes izvēli" — nav neviena uzdevuma, kur skolēnam jānosauc/jāpamato paņēmiens (viegli pievienot: "pie katra piemēra pieraksti lietoto paņēmienu"). |
| Risina vienādojumu, sadalot reizinātājos; **pretpiemērs par nenulles reizinājumu** | `dl_8`, NPD 2.1–2.2 | 🟡 Pati metode trenēta labi; pretpiemēra un "formā pārveidojamo" vienādojumu darba lapā nav (DL8-02). |
| Substitūcijas metode | `dl_9`, FVD 2, `dl_11`, NPD 2.3 un 4. | ✅ Ļoti labi; FVD 2 otrais uzdevums (divas dažādas substitūcijas vienam vienādojumam) precīzi atbilst programmas garam. |
| Grafiskais paņēmiens un funkciju īpašības | `dl_10`, metodiskā 12.–13. stunda, kopsavilkuma 4.g–h, NPD 3. | 🟠 Divi robi: (a) `dl_10` nav uzdevumu, kur grafiki jāzīmē pašiem (DL10-04), lai gan NPD to prasa par 4 p.; (b) **13. stundai ("funkciju īpašības un spriešana") nav darba lapas** — tikai 7 uzdevumi metodiskā tekstā bez atrisinājumiem. Programmas SR "lieto faktu, ka augošai un dilstošai funkcijai … ne vairāk kā viens krustpunkts" paliek bez patstāvīga treniņa materiāla. |
| Izvēlas atbilstošu paņēmienu; **novērtē atrisinājumu ar pārbaudi vai IT** | `dl_11`, kopsavilkums, NPD | 🟡 Metožu izvēle nosegta labi (`dl_11` ir ļoti veiksmīga jaukta lapa ar 23+23 uzdevumiem no lineāriem līdz substitūcijai). Pārbaudes/IT elements atrisinājumos parādās reti; nevienā darba lapā nav uzdevuma "pārbaudi sakni ievietojot / ar GeoGebra", lai gan metodiskais Photomath/tehnoloģijas piemin. |

**Kopvērtējums:** komplekts stundām 1–12 un 14–17 ir apjomīgs un ar labu grūtības progresiju; divkolonnu dizains ("kopā risināmie / atgriezeniskā saite") ir konsekventi ieturēts, un NPD līmeņu struktūra (I–IV) atbilst vērtēšanas praksei. Galvenie trūkumi ir nevis uzdevumu kvalitātē, bet **pilnīgumā**: divi trūkstoši/nepareizi ATR faili (dl_6, dl_7), trūkstoša 13. stundas lapa, kā arī trīs SR nianses (definīcijas kopa, pretpiemērs par nenulles reizinājumu, grafiku zīmēšana pašiem), kas parādās programmā un NPD, bet ne treniņa materiālos.

---

## 3. Ieteikumi papildu uzdevumu tipiem (17 stundu apjomā)

Šie uzdevumu tipi labi iederētos esošajās stundās, neprasot papildu laiku — tie aizstātu daļu no pašreizējā (vietām ļoti lielā) tehniskā apjoma:

1. **Definīcijas kopas uzdevumi `dl_1`** (1. stunda). Piemēram: "Nosaki izteiksmes $\frac{x-2}{x+3}$, $\frac{5}{2x-8}$, $\frac{x+3}{x^{2}+3}$ definīcijas kopu" un pretējais uzdevums "uzraksti daļveida izteiksmi, kas nav definēta, ja $x=4$". Papildus 1–2 vērtības uzdevumi, kur izvēlētajai $x$ vērtībai izteiksme **nav** definēta — dabiska saikne ar DK.
2. **Daļas uzrakstīšana pēc vārdiska apraksta** — 2024. gada eksāmenā bija tieši šāds uzdevums ("skaitītājs ir divi, saucējs — $x$ un $y$ kubu summa"); metodiskajā šī aktivitāte ir, bet darba lapās nē. Ieteicams 3–4 šādus iekļaut `dl_1` vai `dl_5` (sasaistot ar kubu summas jēdzienu).
3. **Kļūdu analīzes uzdevumi** ("Skolēns risināja šādi: … Atrodi kļūdu un izlabo!"). Īpaši noderīgi 9. stundā (tipiskā kļūda: no $(x-1)(x+4)=6$ secina $x-1=6$ vai $x-1=2,\ x+4=3$) un 6. stundā (aizmirsts koeficients $a$ formulā $a(x-x_1)(x-x_2)$ — tieši tas, ko NPD kritēriji soda ar punktu).
4. **Pretpiemēra uzdevums `dl_8`**: "Kāpēc no $(x-2)(x+5)=8$ nedrīkst secināt $x-2=8$ vai $x+5=8$? Atrisini vienādojumu pareizi!" — burtiski īsteno programmas SR formulējumu.
5. **Vienādojumi, kas jāpārveido formā $A(x)\cdot B(x)=0$**: $x^{3}=4x$; $x^{4}=9x^{2}$; $(x-1)(x-2)=6$ — metodiskā 9. stundas jautājumu sērija to jau iezīmē, atliek pārnest uz darba lapu.
6. **Grafiku zīmēšanas uzdevumi `dl_10`** ar vērtību tabulu (kā NPD 3. uzdevumā) un **sakņu skaita noteikšana ar parametru** ($x^{2}=a$; $\sqrt{x}=a$; $x^{2}=ax$) — pēdējie metodiskajā 13. stundā jau ir, tos vērts noformēt kā darba lapu ar atrisinājumiem.
7. **Jauna darba lapa 13. stundai** (funkciju īpašības un spriešana): 4–6 uzdevumi ar pamatojuma sagatavēm ("Funkcija $y=\ldots$ intervālā … ir …, tāpēc vienādojumam šajā intervālā ir ne vairāk kā … sakne"). Tas noslēgtu vienīgo stundu bez sava materiāla.
8. **Apgrieztie (konstruēšanas) uzdevumi**: "Uzraksti kvadrāttrinomu, kura saknes ir $-2$ un $\frac{1}{3}$"; "Uzraksti trešās pakāpes vienādojumu ar saknēm $0;\pm 3$". Tie nostiprina sakarību $ax^2+bx+c=a(x-x_1)(x-x_2)$ dziļākā līmenī nekā tiešā sadalīšana.
9. **Racionālas skaitļošanas uzdevumi ar formulām**: $41^{2}-39^{2}$, $199\cdot 201$, $17^{2}+2\cdot 17\cdot 3+3^{2}$ galvā — parāda formulu praktisko jēgu (labi iederas 4. stundas sākumā vai kopsavilkumā).
10. **Distraktori `dl_5`**: 2–3 izteiksmes, kur kubu formulas **nevar** lietot (piem., $a^{3}+b^{2}$; $x^{3}+3x$; jautājums "ar ko $a^3+b^3$ atšķiras no $(a+b)^3$?") — pašlaik visi 28 uzdevumi ir tiešā formā, kas neattīsta formulas atpazīšanu.
11. **Pārbaudes/IT elements**: pie 2–3 uzdevumiem `dl_9` un `dl_11` pievienot norādi "pārbaudi saknes, ievietojot vienādojumā / ar Desmos vai GeoGebra" — īsteno programmas SR "novērtē iegūtā atrisinājuma atbilstību, veicot pārbaudi vai lietojot IT".
12. **Konteksta uzdevumi**: kopsavilkuma 5. uzdevums (alpīnisma siena) ir vienīgais modelēšanas uzdevums visā tematā. 1–2 līdzīgus (laukums/perimetrs, kas dots ar polinomu) vērts iekļaut jau `dl_6` vai `dl_7`, lai konteksts neparādās tikai pēdējā stundā.

**Piezīme par apjomu:** `dl_2` (45+40 vienādojumi) un `dl_3` (46+28 izteiksmes) apjoms vienai stundai ir ļoti liels — tas atbilst metodiskā aprakstam (skolotājs izvēlas), bet ieteicams lapās vizuāli atzīmēt "pamata" un "izvēles/papildu" uzdevumus, lai atlase neprasa skolotāja priekšdarbu.

---

## 4. Prioritāro labojumu saraksts (īsais kopsavilkums)

Ja labojumus veic pa kārtām, vispirms novēršami šie punkti:

1. 🔴🔴 **DL6-01** — izveidot īstos `dl_6` atrisinājumus (pašlaik failā ir sveša satura dublikāts).
2. 🟠 **DL7-01** — izveidot `dl_7` atrisinājumus.
3. 🔴 **M-01, M-02** — Vjeta teorēmas zīmju kļūdas metodiskajā (skolotāja pamatteksts!).
4. 🔴 **DL1-01…04, DL3-01…03, DL11-01, K-01, K-02** — nepareizas/nepilnīgas atbildes atrisinājumu failos.
5. 🔴 **DL10-01…03, K-03, N-02** — attēlu saites un trūkstošais attēls (bez tiem grafiskās metodes materiāli nav lietojami).
6. 🔴 **DL8-01, M-03…M-08, N-01, DL4-01…03** — pārējās sarkanās pozīcijas.
7. 🟠 Pārklājuma robi: definīcijas kopas uzdevumi `dl_1`, 13. stundas darba lapa, grafiku zīmēšanas un pretpiemēra uzdevumi (3. sadaļas 1., 4., 6., 7. punkts).

---

*Recenzijā katra norādītā matemātiskā kļūda pārbaudīta ar tiešu aprēķinu; pārējie komplektu atrisinājumi (dl_2, dl_5, dl_8, dl_9, dl_11 pārējie uzdevumi, fvd_1/2, kopsavilkums, abi NPD varianti) pārbaudē izrādījās korekti.*
