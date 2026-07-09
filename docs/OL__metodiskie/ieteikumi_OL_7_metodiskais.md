---
layout: default
title: "Ieteikumi par 7. tematu"
permalink: /OL__metodiskie/ieteikumi_OL_7_metodiskais/
---

# Labojumu un ieteikumu saraksts — „OL_7. Funkcija" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_7__funkcija_metodiskais.md` (21 stunda).
**Salīdzināšanas avoti:** programmas paraugs (MATEMATIKA_1_programmas_paraugs, 7. temats „Funkcija, tās īpašības un pārbīdes"), vidusskolas standarts (Matemātikas mācību joma VSK), projektā pieejamie darba lapu / vērtēšanas darbu faili (OL_7_dl_1…dl_9, OL_7_fvd_1, OL_7_fvd_2, OL_7_kopsavilkums, OL_7_npd).
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).

---

## 1. Matemātiski labojumi 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 1.–5. stunda, piemērs pēc simboliskā pieraksta $y = f(x)$ ieviešanas | „Aprēķini $x$, ja $f(x) = 10$." … $5x + 7 = 10 \Rightarrow 5x = 10 \Rightarrow x = 2$ | „Aprēķini $x$, ja $f(x) = 17$." … $5x + 7 = 17 \Rightarrow 5x = 10 \Rightarrow x = 2$ | No $5x + 7 = 10$ seko $5x = 3$ un $x = 0{,}6$, nevis $x = 2$. Visticamāk domāta vērtība 17, kas atbilst iepriekšējam „pamatskolas" piemēram (tur $y = 17$ dod $x = 2$) un saglabā abu pierakstu paralēli. Alternatīva — atstāt $f(x)=10$ un labot risinājumu ($5x = 3$, $x = 0{,}6$), bet tad zūd paralēle. |
| 1.2 | 1.–5. stunda, definīcijas kopas nosacījumu tabulas 9. un 10. piemērs un tiem sekojošais jautājums „Vai abām funkcijām sakrīt definīcijas kopa?" | „*Nē, 9. piemērā skaitītājs un saucējs vienlaicīgi var būt negatīvi, bet 10. piemērā neviena no izteiksmēm nedrīkst būt negatīva.*" | Nomainīt piemēru pāri, piemēram, uz $f(x) = \sqrt{\dfrac{x + 2}{x - 1}}$ un $f(x) = \dfrac{\sqrt{x + 2}}{\sqrt{x - 1}}$, saglabājot atbildi „Nē". | Dotajiem piemēriem ($1 - 2x$ saucējā) atbilde „Nē" ir **kļūdaina**: gadījums „abas izteiksmes negatīvas" prasa $x < -2$ un vienlaikus $x > 0{,}5$, kas nav iespējams, tāpēc abu funkciju definīcijas kopas **sakrīt**: $\lbrack -2; 0{,}5)$. Ieteiktajam pārim kopas atšķiras: $(-\infty; -2\rbrack \cup (1; +\infty)$ pret $(1; +\infty)$, un iecerētais didaktiskais akcents darbojas. |
| 1.3 | 12.–16. stunda, piemērs par funkcijas $f(x) = \frac{x + 2}{x + 1}$ grafiku | „*Piemēram, ja $x = 10000000$, tad izteiksmes $\frac{x + 1}{x + 2}$ vērtība būs gandrīz 1.*" | „…tad izteiksmes $\frac{x + 2}{x + 1}$ vērtība būs gandrīz 1." | Izteiksmē samainīti vietām skaitītājs un saucējs — tā neatbilst piemērā aplūkotajai funkcijai $f(x) = \frac{x + 2}{x + 1}$ (pats apgalvojums „gandrīz 1" gan paliek spēkā abām izteiksmēm, taču pretruna ar aplūkoto funkciju mulsina). |
| 1.4 | 8.–11. stunda, sadaļa „Lineāra funkcija" | „Lineāras funkcijas vērtību kopa ir visi reālie skaitļi, tas ir, $E(y) = \mathbb{R}$." … „krusto $x$ asi punktā $\left( -\frac{b}{k}; 0 \right)$" | Pievienot atrunu: „Ja $k \neq 0$, tad $E(y) = \mathbb{R}$ un grafiks krusto $x$ asi punktā $\left( -\frac{b}{k}; 0 \right)$. Ja $k = 0$, tad funkcija ir konstanta, $E(y) = \{ b \}$, un grafiks (ja $b \neq 0$) $x$ asi nekrusto." | Sadaļā dotā definīcija ($k$ un $b$ — jebkuri reāli skaitļi) un attēlu rinda pieļauj arī $k = 0$, taču apgalvojumi par vērtību kopu un krustpunktu ar $x$ asi šajā gadījumā nav spēkā — iekšēja pretruna. Turpat arī izteiksmē $-\frac{b}{k}$ dalīšana ar $k$ prasa $k \neq 0$. |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | 1.–5. stunda, pēc funkcijas definīcijas | „Funkcijas vērtību kopa $E(f)$ — kopa, kuras elementi ir visas funkcijas $y = f(x)$ vērtības $f(x)$, ja $x \in D(f)$, t. i., $E(f) = Y$." | Svītrot „t. i., $E(f) = Y$" vai aizstāt ar „$E(f) \subseteq Y$". | Pēc dotās definīcijas $Y$ ir kopa, no kuras elementi tiek piekārtoti, un nekas negarantē, ka izmantoti ir visi $Y$ elementi. Vienādība $E(f) = Y$ ir spēkā tikai tad, ja $Y$ ir tieši vērtību kopa. (Vienādība $D(f) = X$ turpretī no definīcijas izriet korekti.) |
| 2.2 | 8.–11. stunda, sadaļa „Lineāra funkcija" | „Funkciju $y = kx$ sauc par tiešo proporcionalitāti." | „Funkciju $y = kx$, kur $k \neq 0$, sauc par tiešo proporcionalitāti." | Ja $k = 0$, sakarība nav proporcionalitāte. Nosacījums $k \neq 0$ atbilst arī pamatskolā lietotajai definīcijai. |
| 2.3 | 1.–5. stunda, tabula „Nosaki funkcijas veidu" | 2. piemērs: „$f(t) = c \cdot t^{2} + 7$ — Kvadrātfunkcija, jo arguments $t$ ir otrajā pakāpē." (līdzīgi 1. un 5. piemērā) | Pievienot pie tabulas piezīmi, ka koeficienti $a$, $c$, $m$, $x$ šajos piemēros uzskatāmi par konstantēm, kas nav 0, vai atbildēs pievienot nosacījumus ($c \neq 0$ u. tml.). | Pēc paša materiāla kvadrātfunkcijas definīcijas ($a \neq 0$) atbilde 2. piemērā ir korekta tikai tad, ja $c \neq 0$; līdzīgi 5. piemērā, ja $x = 0$, funkcija ir konstanta. |
| 2.4 | 1.–5. stunda, vērtību kopas tabulas 7. piemērs | „$f(x) = \frac{\sqrt{(x-1)^{2}}}{x-1} = \frac{\vert x - 1 \vert}{x - 1} = \pm 1$" | Aizstāt „$= \pm 1$" ar gadījumu analīzi: „ja $x > 1$, tad $f(x) = 1$; ja $x < 1$, tad $f(x) = -1$". | Pieraksts „$= \pm 1$" nav korekta vienādība (izteiksmei katrai konkrētai $x$ vērtībai ir viena vērtība); gadījumu analīze arī labāk paskaidro, kāpēc $E(f) = \{-1; 1\}$. |
| 2.5 | 6.–7. stunda, sadaļa „Periodiska funkcija" | „Mazāko pozitīvo skaitli $T$ sauc par funkcijas periodu." un „$f(x \pm 2T) = f(x \pm 3T) = \ldots = f(x \pm kT) = f(x),\ kur\ k \in \mathbb{N}.$" | „Mazāko pozitīvo skaitli $T$, kuram izpildās vienādība $f(x + T) = f(x)$, sauc par funkcijas periodu." Vienādību virkni sākt ar $f(x \pm T)$: „$f(x \pm T) = f(x \pm 2T) = \ldots = f(x \pm kT) = f(x)$, kur $k \in \mathbb{N}$". | Teikums pašlaik nav loģiski piesaistīts definīcijas vienādībai. Virknē izlaists pats pirmais gadījums $\pm T$; jālabo arī formatējuma kļūda pieraksta beigās („$k\mathbb{\in N.}$" — punkts iekļuvis formulā). |
| 2.6 | 12.–16. stunda, pēc norādes uz OL_7_dl_9 | „*Pēc skolotāja ieskatiem no uzzīmētā grafika nosaka funkcijas $f(x) = n + \frac{m}{x + a}$ īpašības.*" | Svītrot „pēc skolotāja ieskatiem" vai pārformulēt, piemēram: „No uzzīmētā grafika nosaka funkcijas … īpašības (skat. SR)." | Īpašību noteikšana funkcijai $f(x) = n + \frac{m}{x+a}$ ir šīs stundu grupas **obligāts** sasniedzamais rezultāts (arī programmas paraugā), tāpēc formulējums „pēc skolotāja ieskatiem" ir pretrunā ar SR sarakstu. |
| 2.7 | 12.–16. stunda, piemērs $f(x) = \frac{x+2}{x+1}$ | „*Definīcijas kopa $x \in (-\infty; -1) \cup (-1; +\infty)$.*" | „*Definīcijas kopa $D(f) = (-\infty; -1) \cup (-1; +\infty)$.*" | Definīcijas kopa ir kopa, tāpēc korektāk to pierakstīt ar kopu vienādību, kā tas darīts pārējā dokumentā ($D(y)$, $D(f)$). |
| 2.8 | 1.–5. stunda (un citur) | „vienādzīmju intervāli" | Saskaņot ar programmas paraugu, kur lietots „vienādas zīmes intervāli" (vai vismaz pirmajā lietojumā dot abus terminus). | Abi termini sastopami praksē, bet materiālu komplektā vēlama vienota terminoloģija ar programmas paraugu. |
| 2.9 | 1.–5. stunda, funkcijas uzdošanas veidi (tabula) | „vienā rindā raksta argumentus (neatkarīgos mainīgos no definīcijas kopas) … bet otrā rindā raksta izrēķinātās funkcijas vērtības (mainīgos, kas atkarīgi no argumenta)" | „…raksta argumenta (neatkarīgā mainīgā) vērtības no definīcijas kopas … raksta atbilstošās funkcijas (atkarīgā mainīgā) vērtības" | Tabulā raksta mainīgo **vērtības**, nevis pašus mainīgos; pašreizējais formulējums jauc mainīgo ar tā vērtībām. |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 Temata plānojuma tabulā trūkst 7., 8. un 9. darba lapas.** Stundu grupai 12.–16. „Funkcijas grafika transformācijas" plānojuma tabulā norādīta tikai *6. darba lapa*, taču stundu aprakstā izmantotas arī OL_7_dl_7 (moduļa funkcijas transformācijas), OL_7_dl_8 (kvadrātsaknes funkcijas transformācijas) un OL_7_dl_9 (daļveida funkcijas transformācijas). Plānojuma tabula jāpapildina, lai tā pilnībā atspoguļotu izmantotos materiālus.

**3.2 🟠 Plānā minētā „Prezentācija" stundu aprakstā neparādās.** 6.–7. stundas plānojuma ailē norādīta *Prezentācija*, bet 6.–7. stundas aprakstā atsauces uz prezentācijas failu nav (ir tikai OL_7_dl_3). Jāpievieno norāde uz prezentāciju atbilstošajā stundas apraksta vietā (piemēram, pie periodiskas funkcijas grafiku aplūkošanas) vai ieraksts jāsvītro no plāna.

**3.3 🟠 1.–5. stundas SR saraksts neaptver visu mācīto saturu.** Stundu grupā tiek mācīta funkcijas monotonitāte (augoša, dilstoša, konstanta funkcija, monotonitātes intervāli), vienādas zīmes intervāli un (kā papildu uzdevums) vērtību kopas noteikšana, taču SR sarakstā minēta tikai definīcijas kopa, nulles un krustpunkti ar asīm. Tā kā šīs īpašības vēlāk tiek lietotas gan FVD 1, gan transformāciju SR („raksturo to īpašības"), ieteicams SR sarakstu (plānā un stundas sākumā) papildināt vai skaidri norādīt, kurš saturs ir atkārtojums/papildinājums.

**3.4 🟡 Temata nosaukums atšķiras no programmas parauga.** Dokumenta virsraksts ir „7. Funkcija", bet programmas paraugā temats saucas „7. Funkcija, tās īpašības un pārbīdes" (21 stunda — stundu skaits sakrīt). Ieteicams saskaņot nosaukumu.

**3.5 🟡 Nekonsekventi parametru apzīmējumi.** (a) Ievada komentārā daļveida funkcija pierakstīta kā $f(x) = \frac{ax + b}{x + c}$, bet SR sarakstos — $f(x) = \frac{ax + b}{x + d}$; (b) SR formulējumā transformācija ir $y = a \cdot f(x)$, sadaļas virsrakstā — $y = m \cdot f(x)$, bet programmas paraugā — $y = k \cdot f(x)$; arī pārbīde SR pierakstīta ar $a$ ($y = f(x + a)$), bet sadaļā ar $b$ ($y = f(x + b)$). Vēlams visā dokumentā (un, ja iespējams, saskaņā ar programmas paraugu) lietot vienotus burtus.

**3.6 🟡 Kubiskā parabola $y = x^{3}$ nav starp standarta SR minētajām funkcijām.** SR uzskaitījumā (gan plānā, gan programmas paraugā) elementārās funkcijas ir $ax + b$, $\sqrt{x}$, $\vert x \vert$, $ax^{2} + bx + c$, $\frac{k}{x}$. Ja kubiskā parabola ir domāta kā papildsaturs, jāpārliecinās, ka galīgajā (docx) versijā tā ir ievietota pelēkajā rāmī ar marķējumu „Nav standarta SR" (Markdown konvertācijā šis marķējums nav redzams).

**3.7 🟡 17. un 18. stundai nav piedāvāti uzdevumi.** Stundām „Argumenta pieaugums un funkcijas pieaugums" un „Salikta funkcija" doti tikai literatūras avoti, bet nav ne darba lapu, ne uzdevumu piemēru (atšķirībā no pārējām stundu grupām). Ieteicams pievienot vismaz dažus uzdevumu paraugus vai īsu teorijas kopsavilkumu ar piemēriem, lai materiāls būtu pašpietiekams.

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts |
|---|---|---|---|
| 4.1 | Vērtību kopas tabulas 4. piemērs | „Atbild. $E(f) = \lbrack 6; +\infty)$" | „Atbilde. $E(f) = \lbrack 6; +\infty)$" |
| 4.2 | Piemērs $f(x) = \frac{x+2}{x+1}$ | „t. .i., $x + 2 = x + 1$" | „t. i., $x + 2 = x + 1$" |
| 4.3 | Pēc definīcijas kopas nosacījumu tabulas | „*Uzsvērt atšķirību 9. un 10 piemērā.*" | „*Uzsvērt atšķirību 9. un 10. piemērā.*" |
| 4.4 | Tabula „Funkcija $y = \vert x \vert$" | „Funkcija ir augoša, ja ,$\ x \in (0; +\infty)$." | „Funkcija ir augoša, ja $x \in (0; +\infty)$." (dzēst lieko komatu) |
| 4.5 | Sadaļa „Lineāra funkcija" | Teikums „Funkcija ir augoša, ja $k > 0$, un dilstoša, ja $k < 0$" atkārtots divreiz; arī $D$ un $E$ norādīti divreiz ar atšķirīgu pierakstu ($D(y) = \mathbb{R}$ un vēlāk $D(f) = (-\infty; +\infty)$) | Atstāt katru apgalvojumu vienu reizi un lietot vienotu pierakstu |
| 4.6 | 18. stunda | „**Sasniedzamais rezultāts**" (seko divi SR) | „**Sasniedzamie rezultāti**" |
| 4.7 | Ievads, materiālu apraksts | „apzīmēts Nav standarta SR" | „apzīmēts „Nav standarta SR"" (pievienot pēdiņas) |
| 4.8 | 12.–16. stunda (divās vietās) | „Principā funkcijas grafiks tiek paralēli pārbīdīts par vektoru…" | „Citiem vārdiem, funkcijas grafiks tiek paralēli pārbīdīts par vektoru…" (izvairīties no sarunvalodas „principā") |
| 4.9 | Temata ievada pirmais teikums | „Tematā atkārto un papildina (apgūst jēdzienus pāra un nepāra funkcija, periodiska funkcija) zināšanas par funkciju…" | Pārformulēt, piemēram: „Tematā atkārto un papildina zināšanas par funkciju (no jauna apgūst jēdzienus pāra funkcija, nepāra funkcija, periodiska funkcija), uzsvaru liekot uz…" |
| 4.10 | Periodiskas funkcijas vērtību tabulas 5. piemērs | „$f(15) = f(13) = f(9) = f(7)$" | „$f(15) = f(13) = f(9) = f(7) = 2$" (pievienot gala vērtību, kā pārējos piemēros) |
| 4.11 | Funkcijas uzdošanas veidu uzskaitījums | Punkts „ar tabulu — …" beidzas ar punktu, pārējie — ar semikolu | Vienādot interpunkciju uzskaitījumā |
| 4.12 | Visā dokumentā | Konvertācijas/noformējuma artefakti: „**\\**", „{.mark}", atsevišķi „\\*" (piem., pie $y = x^{2} - 4$ *un* $y = x^{2} - 4x + 3$), „$\bullet$" reizināšanas zīmes vietā virsrakstos | Notīrīt artefaktus galīgajā versijā; reizināšanai konsekventi lietot „$\cdot$". Ja artefakti radušies tikai docx→md konvertācijā, avota failā tie jāpārbauda izlases veidā |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Pilnveidot pamatojumu gadījumos „nav pāra, nav nepāra".** Tabulas 4. un 8. piemērā ($f(x) = 6x + 8$; $g(x) = x^{6} - x^{2} + 3x$) izrēķināts tikai $f(-x)$, bet secinājums prasa salīdzinājumu gan ar $f(x)$, gan ar $-f(x)$. Ieteicams parādīt pilnu spriedumu (piemēram, ar konkrētu kontrpiemēru: $f(1) = 14$, $f(-1) = 2 \neq \pm 14$), lai skolēniem veidotos korekts pierādīšanas paradums — šī ir tipiska kļūdu vieta.

**5.2 Papildināt transformāciju $y = m \cdot f(x)$ aprakstu.** Aprakstīts tikai gadījums $m > 0$ ($m > 1$ — izstiepšana, $m \in (0;1)$ — saspiešana); ieteicams (a) precizēt, ka $m \in (0;1)$ gadījumā grafiku saspiež $\frac{1}{m}$ reizes, un (b) piebilst, ka $m < 0$ gadījumu iegūst, kombinējot stiepi ar simetriju pret $Ox$ asi (nākamā apakšsadaļa). Var arī pieminēt saikni ar homotētijas jēdzienu, kas minēts programmas parauga SR.

**5.3 Precizēt periodiskas funkcijas definīcijas piemērošanas nosacījumus.** Definīcijā klusējot pieņemts, ka līdz ar $x$ arī $x + T$ pieder definīcijas kopai; vismaz skolotājam adresētā piezīmē to vērts pieminēt (noderēs 8. tematā pie tangensa funkcijas, kuras definīcijas kopa nav visa $\mathbb{R}$).

**5.4 Izvairīties no apzīmējuma $D$ dubultlietojuma.** Kvadrātfunkcijas sadaļā $D$ apzīmē diskriminantu, bet visā pārējā dokumentā — definīcijas kopu $D(f)$. Lai novērstu pārpratumus, diskriminantu var apzīmēt citādi vai lietot vārdu „diskriminants" tekstā.

**5.5 Precizēt Uzdevumi.lv atsauci literatūras sarakstā.** 9. avots norāda uz portāla „5. tematu «Daļveida funkcija un algebriskas daļas»", kas var mulsināt (šis ir 7. temats). Ieteicams paskaidrot, ka numerācija ir portāla, un, ja iespējams, pievienot arī tiešāk atbilstošo portāla sadaļu par funkciju un tās īpašībām.

---

### Kopsavilkums

Dokuments kopumā ir saturiski bagāts, labi strukturēts un atbilst programmas parauga 7. temata apjomam (21 stunda) un akcentiem: pakāpeniska pāreja no pamatskolas satura, simboliskā pieraksta $y = f(x)$ ieviešana, pārdomāti skolotāja jautājumi un norādes uz darba lapām visām galvenajām stundu grupām.

Pirms publiskošanas obligāti jānovērš četri 🔴 līmeņa trūkumi: aritmētiskā kļūda piemērā $f(x) = 10$, kļūdainā atbilde par definīcijas kopu sakritību 9./10. piemērā (kopas faktiski sakrīt — jāmaina piemēri), samainītais skaitītājs un saucējs daļveida funkcijas piemērā, kā arī lineāras funkcijas īpašību apgalvojumi, kas nav spēkā gadījumā $k = 0$.

Ieteicams arī saskaņot plānojuma tabulu ar faktiski izmantotajām darba lapām (7.–9. dl) un prezentāciju, papildināt 1.–5. stundas SR sarakstu ar monotonitāti un vienādas zīmes intervāliem, vienādot parametru apzīmējumus ar programmas paraugu un veikt pilnu teksta korektūru (konvertācijas artefakti, interpunkcija, dublējumi).
