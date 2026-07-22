---
layout: default
title: "Atsauksme par pamatskolas_standartu"
permalink: /OL__metodiskie/atsauksme_programmas_paraugs_4_6_klase/
---
# Atsauksme par programmas parauga "Matemātika 1.–9. klasei" 4.–6. klases daļu

**Analizētais materiāls:** `programmas_paraugs_Matematika_1_9_klase.md`, 3243.–6767. rindiņa (sadaļa "Mācību satura apguves secība 4.–6. klasei", temati 4.1–6.9).
**Salīdzināšanas bāze:** `pamatskolas_standarts.md`, kolonna "Beidzot 6. klasi" (76 sasniedzamie rezultāti M.6.x.x.x).
**Prioritāšu kodi:** 🔴 kritiski, 🟠 svarīgi, 🟡 ieteikti, ⚪ redakcionāli.

---

## 1. Kopsavilkums

Programmas parauga 4.–6. klases daļa ir saturiski blīvs un lielākoties labi izstrādāts materiāls ar spēcīgu, konsekventu **skaitļu mācības spirāli** (naturālie skaitļi → daļas jēdziens → daļu darbības → decimāldaļas → procenti → attiecība un proporcionalitāte → negatīvie skaitļi → racionālo skaitļu kopa) un metodiski vērtīgiem piemēriem, kas seko labajai praksei "konkrētais → attēls → abstrakcija" (sloksnīšu modeļi, laukuma modeļi, skaitļu ass).

Formāli **visi 76 standarta SR "Beidzot 6. klasi" ir citēti** vismaz vienā temata blokā. Tomēr detalizēta pārbaude parāda, ka vairākiem standarta SR citēšana ir tikai formāla — **saturs, kas tos īsteno, tekstā neparādās**. Galvenās konstatācijas:

| Nr. | Konstatācija | Prioritāte |
|---|---|---|
| 1 | **Varbūtības propedeitika (M.6.5.2.1) nav īstenota** — vārdi "varbūtība", "biežums" 4.–6. klases saturā neparādās nevienā SR vai piemērā | 🔴 |
| 2 | **Līdzīgu figūru izpēte (M.6.6.3.3) nav īstenota** — "līdzīg-" saturā neparādās, lai gan kods citēts 7 reizes | 🔴 |
| 3 | **Digitālie rīki neparādās vispār** — "digitāl-" 4.–6. klases sadaļā sastopams 0 reižu, lai gan standarts tos tieši prasa ≥ 8 SR | 🔴 |
| 4 | Citēti **2 standartā neeksistējoši kodi** (M6.6.4.4, M6.4.3.3) un ≥ 10 kļūdaini/nokniebti kodu pieraksti | 🔴 |
| 5 | Vairākas **matemātiskas kļūdas piemēros** (48:8 = …, x·12 = 125, ¼ km = 250 g u. c.) | 🔴 |
| 6 | 6. klases stundu budžets (188–208 st.) pārsniedz reāli pieejamo un neatstāj rezervi vērtēšanai | 🟠 |
| 7 | Kodu "inflācija" bloku virsrakstos (līdz 20 kodiem blokā) mazina pārklājuma izsekojamību | 🟠 |
| 8 | Tematu SR formulējumu gramatika un kompetenču (ARG…MK) marķējums nekonsekvents | 🟡 |

Kopumā: **saturiskais kodols ir gatavs lietošanai**, bet pirms publicēšanas nepieciešama (a) trūkstošo standarta SR "iedzīvināšana" konkrētās satura vienībās, (b) kodu revīzija un (c) piemēru korektūra.

---

## 2. Standarta pārklājuma pārskats

### 2.1. Pārklājums pa mācību jomām (M.Li.1–M.Li.6)

| Joma | SR skaits standartā | Substantīvi nosegti | Daļēji / formāli | Nav nosegti | Piezīmes |
|---|---|---|---|---|---|
| M.Li.1 Valoda, attēlojumi (M.6.1.x) | 7 | 6 | 1 | – | M.6.1.2.1 daļēji: koku diagrammas un Eilera–Venna diagrammas saturā neparādās |
| M.Li.2 Spriešana, modelēšana, pierādīšana (M.6.2.x) | 16 | 11 | 5 | – | Sk. 2.2. — "pilnā pārlase", "pretpiemērs", "patiess/aplams" leksika nav saturā |
| M.Li.3 Skaitļi (M.6.3.x) | 11 | 11 | – | – | Spēcīgākā joma; pilns un pakāpenisks pārklājums |
| M.Li.4 Sakarības, algebra (M.6.4.x) | 14 | 13 | 1 | – | M.6.4.2.2 (formula, grafiks) nosegta 5.9/6.5; laba proporcionalitātes līnija 6.3 |
| M.Li.5 Dati, varbūtība, mērīšana (M.6.5.x) | 12 | 8 | 3 | 1 | **M.6.5.2.1 (varbūtība) nav**; M.6.5.1.1, M.6.5.3.2, M.6.5.3.4 daļēji |
| M.Li.6 Ģeometrija (M.6.6.x) | 16 | 14 | 1 | 1 | **M.6.6.3.3 (līdzīgas figūras) nav**; M.6.2.3.4 sasaiste ar kuba izklājumiem daļēja |

### 2.2. Detalizēts trūkumu saraksts

| # | Standarta SR | Situācija programmā | Ieteikums | Prioritāte |
|---|---|---|---|---|
| P1 | **M.6.5.2.1** "Modelē notikumus, lietojot atbilstošus digitālos rīkus, un … skaidro, kas ir biežums, notikuma varbūtība" | Kods citēts 3× (5.4, 5.8, 6.5 bloku virsrakstos), bet neviena SR rinda un neviens piemērs neattiecas uz notikumiem, biežumu vai varbūtību. Turklāt pašas programmas ievadā (7. klases uzsākšanas priekšnosacījumi, ~98.–110. r.) prasīts, lai skolēni 4.–6. klasē būtu "raksturojuši notikuma biežumu un iespējamību/varbūtību, noteikuši to eksperimentāli, arī ar digitāliem rīkiem" — programma pati sev šo priekšnosacījumu nenodrošina | Pievienot varbūtības propedeitikas bloku (4–6 stundas), loģiskākā vieta — 6.4 (kopā ar sektoru diagrammu un %) vai atsevišķs mini-temats 5. klasē: eksperimenti ar kauliņu/monētu, biežuma tabulas, simulācija ar digitālu rīku | 🔴 |
| P2 | **M.6.6.3.3** "Ar zīmuli vai ar digitāliem rīkiem zīmē, pēta, raksturo līdzīgu plaknes figūru lielumus (malu garumi, leņķi, laukumi)" | Kods citēts 7× (temati 4.4, 5.6), bet neviena SR rinda par figūru palielināšanu/samazināšanu un lielumu attiecību izpēti nav. Tuvākais saturs — mērogs (6.3) — attiecas uz kartēm, ne figūru izpēti | Pievienot SR 6.3 tematā ("Mērogs" blokā vai aiz tā): figūras palielināšana rūtiņu tīklā k reizes, malu, leņķu un laukuma izmaiņu izpēte (labi sasaistās ar 6.9 SR par kuba lielumu izmaiņām) | 🔴 |
| P3 | **Digitālie rīki** (M.6.5.1.1, M.6.5.1.4, M.6.5.2.1, M.6.3.2.3, M.6.3.2.6, M.6.5.3.1, M.6.5.3.4, M.6.6.3.3) | Vārds "digitāls" 4.–6. klases sadaļā **neparādās nevienu reizi** (1.–3. klases sadaļā parādās). Standarts tieši prasa digitālas aptaujas, sensorus, kalkulatorus mērvienību pārveidošanai, digitālus rīkus aprēķinu pārbaudei un zīmēšanai | Sistemātiski iestrādāt vismaz: 4.2/6.4 (digitāla aptauja, izklājlapa diagrammai), 5.1/6.8 (kalkulators rezultāta pārbaudei, aptuvenā vērtība galvā *pirms* rīka), 5.9/6.5 (grafiku rīks), 6.9 (ķermeņu 3D skati) | 🔴 |
| P4 | **M.6.5.3.2** "…ātruma mērvienības km/h, **m/s**" | km/h lietots (4.9, 5.9), m/s neparādās | 5.9 blokā "Ceļš, laiks, ātrums" pievienot m/s un vienkāršu km/h ↔ m/s salīdzinājumu (bez formālas pārveidošanas) | 🟠 |
| P5 | **M.6.5.3.4** "…saliktās mērvienības (arī praktiskās, piemēram, degvielas patēriņš), lieto dažādus kalkulatorus mērvienību pārveidošanai, kas pieejami tīmeklī" | Mērvienību pārveidojumi nosegti plaši, bet saliktās praktiskās mērvienības (patēriņš l/100 km, cena €/kg) un tīmekļa kalkulatori neparādās | Pievienot 1–2 SR 6.3 (attiecība!) vai 6.4 kontekstā — cena par vienību, patēriņš; tas pastiprinātu arī M.6.4.2.4 | 🟠 |
| P6 | **M.6.2.3.3** "Izveido pretpiemēru … piemēram, izvērtē apgalvojumu 'taisnstūriem ar vienādu perimetru arī laukumi ir vienādi'" | Vārds "pretpiemērs" saturā neparādās; kods citēts 7× | Pievienot tieši standarta piemēru 4.8 vai 5.6 laukuma blokā (vienāds perimetrs ≠ vienāds laukums) — tas ir gatavs, pārbaudīts uzdevums | 🟠 |
| P7 | **M.6.2.3.4** "…lieto pilno pārlasi, … piemēram, pētot iespējamos kuba izklājumus" | Kods citēts 6×, bet pilnā pārlase kā paņēmiens nekur nav nosaukta; 6.9 kuba izklājums tikai jāuzzīmē pēc izmēriem, nevis jāpēta visi varianti | 6.9 pievienot kuba izklājumu izpēti (kuri no dotajiem izklājumiem saliekami kubā; cik izklājumu iespējams) — klasisks, pieejams uzdevums | 🟠 |
| P8 | **M.6.2.1.4** kopu valoda ("kopa, apakškopa, kopas elements", "eksistē", "katrs", "un/vai/vai nu–vai") un **M.6.1.2.1** (koku diagrammas, Eilera–Venna diagrammas) | "Kopa" parādās tikai kā skaitļu kopu nosaukums (6.5, 6.8 jēdzienos); loģikas leksika un diagrammas informācijas strukturēšanai neparādās | Pievienot 5.1 ("Lielie skaitļi" / skaitļu grupēšana) vai 5.2 (dalāmība — Eilera–Venna diagramma skaitļiem, kas dalās ar 2 un ar 3) | 🟠 |
| P9 | **M.6.5.1.1** pētījuma cikls | Pilns pētījuma cikls tikai 4.2 (9–11 st.) — pirms skolēni apguvuši vidējo (5.7) un procentus (5.8/6.4), un bez digitāliem rīkiem; 6. klasē pētījums pieminēts tikai 6.9 mērķī | Paredzēt otru, "briedušāku" pētījuma iterāciju 6.4 (aptauja → tabula → sektoru diagramma → % → vidējais → secinājumi), sasaistot ar P1 un P3 | 🟠 |
| P10 | **M.6.5.1.5** aritmētiskais vidējais | Viena SR rinda 5.7 iekš bloka "Decimāldaļu reizināšana un dalīšana ar veselu skaitli"; datu kontekstā vairs neatgriežas | Vismaz atkārtot 6.4 datu blokā (vidējais + diagrammu analīze = M.6.5.1.6) | 🟡 |
| P11 | **M.6.2.3.1** "Lieto jēdzienus 'patiess/aplams apgalvojums'" | Kods citēts 12×, bet pati leksika "patiess/aplams" saturā neparādās | Ieviest jēdzienus vienā konkrētā vietā (piem., 5.1 salīdzināšana vai 5.6) un turpmāk lietot uzdevumu formulējumos | 🟡 |

### 2.3. Kodu tehniskā revīzija

Programmas parauga 4.–6. klases daļā citēti 77 dažādi "M6…" kodi; standartā ir 76. Atšķirību veido **neeksistējoši kodi**:

| Kods | Vieta (rindiņa oriģinālā) | Problēma | Ieteikums |
|---|---|---|---|
| **M6.6.4.4** | 4407 (4.8 laukuma bloks), 5357 (5.6 laukuma bloks) | Standartā 6.4. apakšjomā "Beidzot 6. klasi" ir tikai M.6.6.4.1–M.6.6.4.3 | 🔴 Dzēst vai aizstāt (visticamāk domāts M.6.6.4.3) |
| **M6.4.3.3** | 6313 (6.5 bloks "Reālu procesu grafiskais attēlojums") | Standartā 4.3. apakšjomā "Beidzot 6. klasi" ir tikai M.6.4.3.1 | 🔴 Aizstāt; pēc satura blokam atbilst M.6.4.2.2 un M.6.5.1.4 |
| M6.5.2.1 | 5026, 5511, 6313 | Eksistē, bet pievienots blokiem, kuru SR ar varbūtību nesaistās | 🟠 Dzēst no šiem blokiem; sk. P1 |

**Nokniebti / kļūdaini pieraksti** (jāizlabo, jo automātiska pārklājuma pārbaude tos neatpazīst):

| Rindiņa | Pieraksts tekstā | Jābūt |
|---|---|---|
| ~3786–3788 (4.4) | `M6.4.1., M6.4.3.` | pilni kodi (M6.4.1.x, M6.4.3.1) |
| ~4634 (5.1) | `M6. 2.3.5.` | `M6.2.3.5.` |
| 5357 (5.6) | `M6.4.2.,` | pilns kods |
| 6113 (6.4) | `M65.1.6.` | `M6.5.1.6.` |
| 6381–6382 (6.6) | `M62.2.5.`, `M6, 3.2.1.` | `M6.2.2.5.`, `M6.3.2.1.` |
| 6439 (6.6), 6468 (6.7) | `M63.3.1` | `M6.3.3.1.` |
| 6468 (6.7) | `M6..2.2.6.` | `M6.2.2.6.` |
| 6516 (6.7) | `M.2.2.2.` | `M6.2.2.2.` |
| 6672–6673 (6.9) | `M 6.6.1.7.`; M6.6.1.5 un M6.6.1.8 katrs divreiz vienā sarakstā | atstarpe; dublējumi jādzēš |
| 3523 (4.3), 3948 (4.5) | M6.2.2.5 divreiz vienā sarakstā | dublējums jādzēš |
| 4673 (5.1), 5511 (5.8) | M6.3.2.6 / M6.3.2.1 divreiz vienā sarakstā | dublējums jādzēš |

⚪ **Notācijas konsekvence:** standarts lieto pierakstu ar punktu aiz M (`M.6.1.1.1.`), programma — bez (`M6.1.1.1.`), vietām jaukti (`M.6.2.2.2.` 5.4 blokā). Ieteicams visā dokumentā pāriet uz standarta pierakstu `M.6.x.x.x.` un vienoties par atsauces formātu uz 3. klases SR (pašlaik `M3.3.1.1` un `M3.1.1.1.` mijas ar/bez beigu punkta).

---

## 3. Satura kļūdas un nepilnības piemēros

| Rindiņa | Teksts | Problēma | Labojums | Prioritāte |
|---|---|---|---|---|
| 3527 | `48:8 = 40 :4 + 8:4 = 12` | Dalītājs piemēra gaitā mainās no 8 uz 4; arī rezultāts neatbilst virsrakstam (48:8 = 6) | `48:4 = 40:4 + 8:4 = 12` | 🔴 |
| 4013 | `x ⸱ 12 = 125` | Vienādībai nav naturāla atrisinājuma; 4. klasē pirms daļu dalīšanas tas nav risināms | piem., `x · 12 = 132` | 🔴 |
| 4285 | `¼ km = 250 g` | Mērvienību sajaukums (garums → masa) | `¼ km = 250 m` | 🔴 |
| 3865 | `4503 :10 = 450;A 3` | Bojāts pieraksts (konversijas artefakts) | `4503 : 10 = 450, atl. 3` | 🟠 |
| ~3548–3585 | Divas identiskas SR rindas "Dala divciparu skaitli ar viencipara skaitli, izmantojot dalīšanu rakstos" (4.3) | Dublējums; abu rindu piemēri jāapvieno | apvienot vienā SR | 🟡 |
| ~3611 | Bloka "Trīsciparu … reizināšana" pirmā SR ir par **divciparu** skaitli | SR neatbilst bloka virsrakstam (pieder iepriekšējam blokam) | pārcelt | 🟡 |
| ~3800, 3812 (4.4) | "Uzzīmē figūru, kas sastāv no 3 stariem…" un "Uzzīmē leņķi, kuru veido 3 stari…" | Divas gandrīz identiskas SR vienā blokā | apvienot | 🟡 |
| 5749 (6.1) | `3/4 : 6/7 = … = 21/24` | Rezultāts nav saīsināts (7/8) tematā, kur saīsināšana ir apgūta prasme | pievienot saīsināšanas soli | 🟡 |
| vairākviet (piem., 3389, 3620, 4741) | `= =` dubultas vienādības zīmes; `203·5 = (200+3)·5 = 200·5+35` (izlaists solis) | Pieraksta paraugam programmā jābūt nevainojamam, jo tas modelē skolēna pierakstu | korektūra | 🟡 |
| 6549–6605 (6.8) | Tukši piemēri: "Piemēram, … vai …", "Jāaizstāj ar darbību …" bez formulām; tukša tabula pie `0:8` / `8:0` | Konvertējot dokumentu, pazudušas formulas/attēli — bloki nav lietojami | atjaunot saturu | 🟠 |
| 5128 | Temata nosaukums "Jauktu skaitļu **skaitīšana** un atņemšana" | Jābūt "saskaitīšana"; arī "parastu Daļu" lielo burtu kļūda | korektūra | 🟡 |
| 5499, 6453 | "(14-15stundas)", "(18-22stundas)" | Trūkst atstarpes | korektūra | ⚪ |
| 4347 u. c. | Reizināšanas zīme mijas: `\bullet`, `⸱`, `۰` | Vienādot simbolu visā dokumentā | korektūra | ⚪ |

---

## 4. Plūdums (flow) un uzkrājamo priekšzināšanu ķēde

### 4.1. Stiprās puses

Skaitļu mācības ķēde ir izcili loģiska, un katrs posms tiešām balstās iepriekšējā: 4.6 (daļas jēdziens, vienādi saucēji) → 5.3 (pamatīpašība, kopsaucējs, salīdzināšana) → 5.4 (daļu rēķinu trīs pamattipi) → 5.5 (jaukti skaitļi, × ar veselu) → 6.1 (daļa × daļa, dalīšana, apgrieztie skaitļi) → 6.2 (decimāldaļu ×, :, parastās ↔ decimāldaļas) → 6.8 (sistematizācija racionālo skaitļu kopā). Atsevišķi izceļams: daļu salīdzināšana 4.6 ar **spriešanas** paņēmieniem (etalons ½, "cik pietrūkst līdz 1") un tikai 5.3 ar kopsaucēja algoritmu — tas atbilst labākajai praksei (izpratne pirms algoritma). Tāpat labi izkārtota koordinātu plaknes līnija: 5.9 (1. kvadrants, dati un kustības grafiki) → 6.5 (pilna plakne, figūras, simetrijas) un mērīšanas līnija 4.8 (laukums) → 5.6 (kombinētas figūras) → 6.9 (virsma, tilpums).

### 4.2. Riski un neatbilstības

| # | Risks | Skaidrojums | Ieteikums | Prioritāte |
|---|---|---|---|---|
| F1 | **Stundu bilance 6. klasē** | Tematu summas: 4. kl. 157–175 st., 5. kl. 163–175 st., 6. kl. **188–208 st.** (kopā 508–558 pret plānotajām 560). Pie 5 st./nedēļā (~175 st. gadā) 6. klases maksimums neietilpst, un nevienā klasē nav rezervēta laika diagnostikai un nobeiguma vērtēšanai | Samazināt 6. klases tematu augšējās robežas (kandidāti: 6.3 24–26 → 22–24; 6.8 21–24 → 18–20, jo tas ir sistematizācijas temats) un eksplicīti norādīt rezervi vērtēšanai (~10 %) | 🟠 |
| F2 | **Dalāmības pazīmes 4.3** | Pazīmes ar 3, 4, 9 prasa spriešanu par ciparu summu — kognitīvi smagas 4. klasē un pilnā apjomā atkārtojas 5.2 | 4. klasē atstāt 2; 5; 10 (novērojumu līmenī), pazīmes ar 3, 4, 9 pārcelt uz 5.2, kur tās kalpo skaitļa sadalīšanai reizinātājos (arī atbilstoši M.6.2.1.3 "formulē dalāmības pazīmes") | 🟡 |
| F3 | **4.2 novietojums un vientulība** | Datu temats (9–11 st.) iesprausts starp divām aritmētikas kāpnēm (4.1 → 4.3); tas pats par sevi ir pieļaujami ("elpas pauze"), bet datu virziens pēc tam pazūd līdz 5.7/6.4, un pilnais pētījums notiek tikai šeit | Sk. P9: dalīt datu apguvi divās iterācijās (4.2 pamati, 6.4 pilns cikls) un 4.2 mērķī pieteikt šo perspektīvu | 🟠 |
| F4 | **6.5 heterogenitāte** | Temats "Negatīvi un pozitīvi skaitļi" satur pilnu ģeometrijas apakškursu (koordinātu plakne, figūru vienādība, aksiālā un centrālā simetrija, pagriezieni, procesu grafiki) — nosaukums slēpj ~⅓ satura, kas apgrūtina plānošanu un vērtēšanu | Pārdēvēt (piem., "Negatīvi un pozitīvi skaitļi. Koordinātu plakne") vai atdalīt ģeometrijas daļu atsevišķā tematā; ja saglabā — temata mērķī nosaukt abas līnijas (mērķis to jau daļēji dara) | 🟡 |
| F5 | **Vienreizējas ekspozīcijas riski** | Aksiālā simetrija (M.6.6.3.2) un pagriezieni koordinātu plaknē parādās tikai 6.5 beigu daļā; ja gads saspiests (sk. F1), tieši šīs SR izkrīt. Līdzīgi — riņķa līnijas garums (≈ 3 diametri) 5.6 vairs neatgriežas | Pagriezienu propedeitika 4.4 (rūtiņu tīklā) jau ir — pievienot atpakaļatsauci; riņķa līnijas attiecību var atkārtot 6.3 kā attiecības piemēru (vienlaikus π propedeitika) | 🟡 |
| F6 | **Nezināmā locekļa aprēķināšanas atkārtojumi** | SR "nosaka nezināmo darbības locekli" parādās 4.1, 4.5, 5.1, 5.7, 6.2, 6.6, 6.7, 6.8 gandrīz identiskā formulējumā | Tas ir apzināts spirālveida elements — bet ieteicams katrā nākamajā vietā formulēt **pieaugumu** (jauns skaitļu apgabals, jauns pieraksta veids), citādi izskatās pēc dublēšanās | ⚪ |
| F7 | **4.6 ↔ 5.3 bloku dublēšanās izskats** | Bloku "Daļu salīdzināšana" virsraksti un kodu saraksti 4.6 un 5.3 ir identiski, lai gan saturs atšķiras (spriešana vs. algoritms) | Bloku virsrakstos norādīt tvēruma atšķirību ("… spriežot, bez kopsaucēja" / "… vienādojot saucējus") | ⚪ |
| F8 | **Proporcijas jēdziena atlikšana** | 6.3 piezīme "Proporcijas jēdzienu ievieš 7. klasē" ir laba, skaidra robežšķirtne — atzīmējams kā paraugs, kā formulēt tvēruma robežas; šādas piezīmes ieteicams pievienot arī citur (piem., 6.5 par darbībām ar negatīviem skaitļiem, kuras sākas tikai 6.6) | pārnest praksi | ⚪ |

---

## 5. Ieteikumi par mācību gaitu un zināšanu pārbaudes formām

Programmas vispārīgajā daļā (404.–600. r.) vērtēšanas principi aprakstīti labi (formatīvās vērtēšanas prioritāte, atklātības, iekļaušanas, izaugsmes principi), taču **4.–6. klases tematos šie principi nav operacionalizēti**: nevienam tematam nav norādīti (a) nobeiguma vērtēšanas objekts ("ko skolēns demonstrē temata beigās"), (b) formatīvie pieturas punkti, (c) laiks vērtēšanai stundu budžetā.

Ieteikumi:

1. 🟠 Katram tematam pievienot īsu sadaļu "Vērtēšana" ar 2–3 nobeiguma SR (atlasītiem no temata SR saraksta kā "lielajiem") un 1–2 formatīvām pārbaudēm; tas arī atrisinātu SR hierarhijas problēmu (sk. 6. sadaļu).
2. 🟠 Rezervēt stundas: pie tematu apjoma 9–26 stundas prakse ir ~1–2 stundas vērtēšanai tematā; pašreizējās stundu robežas to neparedz (sk. F1).
3. 🟡 Projektā vidusskolas tematiem (OL_1…OL_12) jau ir izstrādāti UZD + KRIT pāri ar snieguma līmeņu aprakstiem — pamatskolas programmas paraugā ieteicams vismaz norādīt, ka analoģiski kritēriju paraugi tiks pievienoti, un vietturi "[Saite vai norāde uz metodiskā materiāla atbilstošo daļu]" papildināt ar vietturi vērtēšanas materiāliem.
4. 🟡 Tematos, kuru mērķī pieteikts pētījums (4.2, 6.9 "Veic pētījumu par telpiskiem ķermeņiem"), norādīt, ka vērtēšanas forma ir snieguma vērtēšana ar kritērijiem (nevis rakstisks darbs) — pašlaik 6.9 mērķa teikums par pētījumu SR sarakstā tālāk neparādās.

---

## 6. SR tvēruma (scope) piezīmes stundu līmenī

1. 🟠 **Granularitāte kopumā laba** (viena SR ≈ viena mācību epizode), bet nav hierarhijas: temata SR sarakstā līdzās stāv "lielie" rezultāti (piem., "Iegūst un formulē algoritmu decimāldaļu reizinājumam", 6.2) un tehniski apakšsoļi (piem., "Uzzīmē perpendikulāras taisnes baltā lapā, izmantojot uzstūri", 4.4). Ieteikums: bloku līmenī izcelt 1–2 "vadošos" SR, pārējos marķēt kā soļus — tas tieši atbalstītu vērtēšanu (5. sadaļa).
2. 🟠 **Atkārtojuma un jaunā satura nošķīrums.** 4.1 un 5.1 lielu daļu aizņem atkārtojums (4.1 pirmais bloks pat nosaukts "atkārtojums un padziļinājums") — tas ir pareizi, bet atkārtojuma SR būtu marķējami atsevišķi (piem., kursīvā vai ar "[A]"), lai skolotājs tos var izmantot diagnostikai, nevis mācīt no jauna.
3. 🟠 **Kodu saraksti bloku virsrakstos jāatslogo.** Piemēram, 5.1 blokam "Skaitļu ass un skaitļu salīdzināšana" piesaistīti 20 kodi, 5.4 blokam — 23; caurviju kodi M.6.2.2.x (modelēšanas soļi) pievienoti gandrīz katram blokam. Tas padara neiespējamu atbildi uz jautājumu "kur šis standarta SR tiek *apgūts*, nevis tikai *lietots*". Ieteikums: divu līmeņu kodēšana — **treknrakstā** primārie (šeit apgūst), parastā rakstā atbalsta kodi; vai arī caurviju kodus norādīt vienreiz temata galvā.
4. 🟡 **Formulējumu gramatika.** Lielākā daļa SR ir 3. personas īstenības izteiksmē ("Reizina…", "Skaidro…"), bet ir arī nenoteiksmes ("Modelēt daļu saskaitīšanu…", "Izmantot daļu rēķinus…", 5.3/5.4) un nominālas frāzes ("Parastās daļas saīsināšana un paplašināšana", 5.3; "Nezināmā darbības locekļa aprēķināšana", 6.8). Vienādot uz īstenības izteiksmi ar skolēnu kā darītāju.
5. 🟡 **Kompetenču marķējums (ARG, PR, MM, ATT, FP, MK).** Klasifikācijas sistēma pati par sevi ir laba (atbilst Nisa/KOM kompetenču ietvaram), bet lietojums nekonsekvents: (a) MK piešķirts gandrīz katrai SR, tāpēc zaudē atšķirtspēju; (b) PR un MM lietoti reti un neprognozējami — piemēram, kustības uzdevumi 5.9 ar shematisko modelēšanu marķēti PR/ATT, bet analoģiskie 4.9 — tikai MK; (c) vietām vairāki kodi vienā šūnā bez atdalītāja ("ARG MK", "MK ATT"), vietām kolonna tukša (4.3 sadalāmības īpašība). Ieteikums: marķēt ne vairāk kā 2 dominējošās kompetences uz SR un veikt izlases konsekvences pārbaudi pret dokumenta sākumā dotajām definīcijām.
6. ⚪ **Jēdzienu saraksti tematu galvās** kopumā precīzi, bet vietām iekļauj frāzes, kas nav jēdzieni ("viss daudzumu, ja zināma tā daļas vērtība" 5.4 — gramatiski bojāts), un 6.9 jēdzienos nav konusa/lodes, kaut SR tos min.

---

## 7. Atbilstība starptautiskajai programmu veidošanas labajai praksei

| Prakses princips | Vērtējums | Komentārs |
|---|---|---|
| **Saskaņotība (coherence) un spirālveida progresija** (CCSSM, 2010; NCTM, 2014) | Labi | Skaitļu virziens veido skaidras mācīšanās trajektorijas; daļa × daļa un negatīvie skaitļi 6. klasē atbilst starptautiskam izvietojumam (CCSSM 5.NF/6.NS) |
| **Konkrētais–attēls–abstrakcija (CPA)** (Singapūras pieeja; Bruner) | Ļoti labi | Konsekvents modeļu lietojums: sloksnīšu/joslu modeļi daļu rēķinos (5.4), laukuma modeļi daļu un decimāldaļu reizināšanai (6.1, 6.2), skaitļu ass negatīvajiem skaitļiem (6.6) — tā ir programmas izceļamā stiprā puse |
| **Procedūru izpratne pirms algoritma** (NRC "Adding It Up", 2001) | Labi | Daudzviet SR secība ir "modelē → secina → formulē algoritmu → lieto" (piem., 6.2 decimāldaļu reizināšana); saglabāt šo šablonu arī 6.7, kur zīmju likumi pašlaik doti deklaratīvi, bez izpratnes veidošanas soļa 🟡 |
| **Datu un varbūtības īpatsvars** (TIMSS 2023 ietvars; GAISE II, 2020) | Vāji | Datiem 4.–6. klasē atvēlēts ~2 % stundu (9–11 no ~560), varbūtībai — 0; TIMSS 4. klases ietvarā datu domēnam ir ~7 %, un standarts pats prasa vairāk (sk. P1, P9) 🔴/🟠 |
| **Tehnoloģiju integrācija** (NCTM, 2014) | Vāji | Sk. P3 🔴 |
| **Atpakaļvērstā plānošana (backward design)** (Wiggins & McTighe, 2005) | Daļēji | Tematu mērķi formulēti, bet vērtēšanas pierādījumi nav definēti (sk. 5. sadaļu) |
| **Rezultātu izsekojamība pret standartu** (OECD curriculum alignment prakse) | Daļēji | Kodēšana ir izveidota — tas ir liels pluss —, bet kodu inflācija un tehniskās kļūdas pašlaik neļauj to izmantot auditam (sk. 2.3) |

---

## 8. Prioritizēts darbību saraksts programmas veidotājiem

| Prior. | Darbība | Kur |
|---|---|---|
| 🔴 | Pievienot varbūtības propedeitikas saturu (biežums, eksperiments, digitāla simulācija) | jauns bloks 5. vai 6. klasē (ieteicams pie 6.4) |
| 🔴 | Pievienot līdzīgu figūru izpētes SR | 6.3 (pie mēroga) |
| 🔴 | Iestrādāt digitālo rīku lietojumu vismaz 6 vietās | 4.2, 5.1, 5.9, 6.4, 6.8, 6.9 |
| 🔴 | Izlabot neeksistējošos kodus M6.6.4.4 un M6.4.3.3 | 4407, 5357, 6313 |
| 🔴 | Izlabot skaitliskās kļūdas piemēros | 3527, 4013, 4285 |
| 🟠 | Kodu tehniskā revīzija (nokniebtie, dublētie, atstarpes) un pāreja uz standarta pierakstu M.6.x.x.x | sk. 2.3 tabulu |
| 🟠 | Atjaunot 6.8 zudušos piemērus un tabulas | 6549–6605 |
| 🟠 | Pārskatīt 6. klases stundu budžetu un rezervēt laiku vērtēšanai | 6.3, 6.8 u. c. |
| 🟠 | Pievienot m/s, saliktās praktiskās mērvienības, pretpiemēra un pilnās pārlases uzdevumus | 5.9, 6.3, 4.8/5.6, 6.9 |
| 🟠 | Ieviest divu līmeņu kodēšanu bloku virsrakstos (primārie / atbalsta kodi) | visā sadaļā |
| 🟠 | Katram tematam pievienot vērtēšanas sadaļu (nobeiguma SR + formatīvie punkti) | visā sadaļā |
| 🟡 | Pārcelt dalāmības pazīmes ar 3, 4, 9 no 4.3 uz 5.2 | 4.3, 5.2 |
| 🟡 | Pārdēvēt/pārstrukturēt 6.5; vienādot SR gramatiku; sakārtot kompetenču marķējumu; ieviest patiess/aplams leksiku | 6.5 u. c. |
| ⚪ | Korektūra: "= =", reizināšanas simboli, "skaitīšana"→"saskaitīšana" (5128), atstarpes stundu norādēs, bloku virsrakstu tvēruma precizējumi 4.6/5.3 | visā sadaļā |

---

## 9. Literatūra un atsauces

1. MK noteikumi Nr. 747 (27.11.2018.) "Noteikumi par valsts pamatizglītības standartu un pamatizglītības programmu paraugiem" — sasniedzamo rezultātu kolonna "Beidzot 6. klasi" (projekta fails `pamatskolas_standarts.md`).
2. National Research Council (2001). *Adding It Up: Helping Children Learn Mathematics.* Washington, DC: National Academies Press.
3. NCTM (2014). *Principles to Actions: Ensuring Mathematical Success for All.* Reston, VA.
4. Common Core State Standards Initiative (2010). *Common Core State Standards for Mathematics* — salīdzinājumam par daļu un negatīvo skaitļu izvietojumu 5.–7. klasē.
5. Mullis, I. V. S., et al. (2021). *TIMSS 2023 Assessment Frameworks.* Boston College — datu un varbūtības domēna īpatsvars sākumskolā.
6. Bargagliotti, A., et al. (2020). *Pre-K–12 Guidelines for Assessment and Instruction in Statistics Education II (GAISE II).* ASA/NCTM.
7. Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (2nd ed.). ASCD — atpakaļvērstā plānošana un vērtēšanas pierādījumi.
8. Niss, M., & Højgaard, T. (2019). Mathematical competencies revisited. *Educational Studies in Mathematics*, 102, 9–28 — ARG/PR/MM/ATT/FP/MK klasifikācijas teorētiskais pamats.

---

*Piezīme par metodi: pārklājuma analīze veikta, automātiski izgūstot visus M-kodu citātus 3243.–6767. rindā, salīdzinot tos ar pilno standarta kodu sarakstu un pēc tam manuāli pārbaudot, vai citētajiem kodiem atbilst substantīvs saturs SR rindās un piemēros. Rindiņu numuri atsauksmē norādīti pēc faila `programmas_paraugs_Matematika_1_9_klase.md`. Dokumentā sagaidāmās nepabeigtās atsauces ("[Saite vai norāde uz metodiskā materiāla atbilstošo daļu]") nav uzskatītas par trūkumiem.*
