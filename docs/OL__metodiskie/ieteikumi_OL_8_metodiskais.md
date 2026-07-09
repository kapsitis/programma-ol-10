---
layout: default
title: "Ieteikumi par 8. tematu"
permalink: /OL__metodiskie/ieteikumi_OL_8_metodiskais/
---

# Labojumu un ieteikumu saraksts — „OL_8. Trigonometriskās funkcijas" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_8__Trigonometriskas_funkcijas_metodiskais.md` (20 stundas).
**Salīdzināšanas avoti:** programmas paraugs (`MATEMATIKA_1_programmas_paraugs_19_maijs.md`, 8. temats), standarts `Matemātikas_mācību_joma_VSK.pdf`, projektā pieejamie temata faili `OL_8_dl_2` … `OL_8_dl_6`, `OL_8_fvd_1`, `OL_8_fvd_2`, `OL_8_kopsavilkums`, `OL_8_npd`, `OL_8_eksamenu_uzdevumi`.
**Piezīme par izsekojamību:** vietas dokumentā norādītas gan pēc sadaļas/stundas, gan pēc aptuvenā rindas numura (r.) `.md` failā.
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).


KĀ ATRAST RINDU NUMURUS? Ieteikumos norādīti 
rindu numuri pārskatāmajā dokumentā; tās nav MS Word oriģināla, 
bet pārveidotā Markdown faila rindas. 
Sk. <a href="https://raw.githubusercontent.com/kapsitis/programma-ol-10/refs/heads/main/docs/OL_8_Trigonometriskas_funkcijas/OL_8__Trigonometriskas_funkcijas_metodiskais.md">OL_8__Trigonometriskas_funkcijas_metodiskais.md</a>. Lai redzētu rindu numurus, šis fails jāsavāc 
un jāpārlūko ar parastu teksta redaktoru, piemēram, 
Visual Studio Code vai Notepad++.

*Piezīme: rindu numuri var nedaudz atšķirties.*

---

## 1. Matemātiski labojumi 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 1.–3. stunda, sadaļa „Loka un leņķa lielums radiānos" (r. 358–361) | „Lai pārveidotu **radiānus par grādiem**, izmanto sakarību $180^\circ=\pi$ rad, no kuras izriet, ka $1^\circ=\frac{\pi}{180}$ rad …" | „Lai pārveidotu **grādus par radiāniem**, izmanto sakarību $180^\circ=\pi$ rad, no kuras izriet, ka $1^\circ=\frac{\pi}{180}$ rad …" | Pārveidošanas virziens sajaukts: formula $n^\circ=n\cdot\frac{\pi}{180}$ rad pārveido grādus radiānos, un arī tai sekojošais uzdevums ir „Pārveido radiānos!". Pretējais virziens jau korekti aprakstīts iepriekš (r. 324). |
| 1.2 | Turpat, piemēri „Pārveido grādos ar precizitāti līdz tūkstošdaļām!" (r. 351–356) | „$-4\ rad \approx -229{,}184^\circ$"; „$5{,}2\ rad \approx 297{,}939^\circ$" | „$-4\ rad \approx -229{,}183^\circ$"; „$5{,}2\ rad \approx 297{,}938^\circ$" | Noapaļošanas kļūdas: rezultāts iegūts, reizinot ar jau noapaļoto vērtību $57{,}296^\circ$. Precīzi: $4\cdot\frac{180}{\pi}=229{,}18312\ldots$; $5{,}2\cdot\frac{180}{\pi}=297{,}93805\ldots$ Ja prasa precizitāti līdz tūkstošdaļām, jānoapaļo tikai gala rezultāts (1. piemērs $114{,}592^\circ$ ir korekts). |
| 1.3 | 4.–8. stunda, piemēri „Aprēķini leņķa lielumu … lietojot IT" (r. 704) | „$\arcsin\left(\frac{3}{4}\right)\approx 46{,}9^\circ$" | „$\arcsin\left(\frac{3}{4}\right)\approx 48{,}6^\circ$" | $\arcsin 0{,}75 = 48{,}59^\circ$. Kļūda ir pretrunā arī ar tā paša piemēra radiānu vērtību: $0{,}848\ rad \approx 48{,}6^\circ$. Pārējie trīs piemēri ir korekti. |
| 1.4 | 9.–10. stunda, sinusoīdas konstruēšana (r. 752–754) | „Veicot šī intervāla pārnesi **paralēli $y$ asij** par $2\pi k$, $k\in\mathbb{Z}$, iegūst funkcijas $y=\sin x$ grafiku." | „Veicot šī intervāla pārnesi **paralēli $x$ asij** par $2\pi k$, $k\in\mathbb{Z}$, iegūst funkcijas $y=\sin x$ grafiku." | Periodiskais atkārtojums ir pārbīde argumenta ($x$ ass) virzienā; pārnese paralēli $y$ asij būtu vertikāla pārbīde. |
| 1.5 | 13.–16. stunda, transformāciju tabula, rinda $y=k\cdot f(x)$ (r. 974–981) | „Grafiku izstiepj $k$ reizes, ja $k>1$. Grafiku **saspiež $k$ reizes, ja $k<1$**." | „Grafiku izstiepj $k$ reizes, ja $k>1$. **Ja $0<k<1$, grafiku saspiež $\frac{1}{k}$ reizes.**" | Ja, piemēram, $k=\frac{1}{2}$, grafiku saspiež 2 (nevis $\frac{1}{2}$) reizes — tā tas korekti formulēts arī 6. piemērā ($y=-\frac{1}{2}\cos x$ „saspiežot 2 reizes"). Turklāt nosacījums „$k<1$" nekorekti ietver arī $k\le 0$; gadījums $k<0$ tabulā aprakstīts atsevišķi. |
| 1.6 | Turpat, rinda $y=f(kx)$ (r. 999–1008) | „Ja $0<k<1$, tad funkcijas grafiku **izstiepj $k$ reizes** pa $x$ asi. Periods **palielinās $k$ reizes**." | „Ja $0<k<1$, tad funkcijas grafiku **izstiepj $\frac{1}{k}$ reizes** pa $x$ asi. Periods **palielinās $\frac{1}{k}$ reizes** (jaunais periods ir $\frac{2\pi}{k}$)." | Ar $k=\frac{1}{2}$ grafiku izstiepj 2 reizes — tieši tā formulēts dokumenta 7. piemērā ($y=\sin\frac{1}{2}x$). Pašreizējais tabulas formulējums ir matemātiski kļūdains un pretrunā ar piemēriem. |
| 1.7 | Turpat, rinda $y=k\cdot f(x)$ (r. 983–986) un 17. stundas 1. piemērs (r. 1210–1213) | „…citos mācību priekšmetos lieto jēdzienu **amplitūda — starpība starp funkcijas lielāko un mazāko vērtību**"; „…funkcijas amplitūda jeb starpība starp lielāko un mazāko vērtību ir 2, tad $\frac{y_{max}-y_{min}}{2}=1$" | „…amplitūda — funkcijas **lielākā novirze no vidusstāvokļa jeb puse no starpības** starp funkcijas lielāko un mazāko vērtību"; 17. stundā: „…starpība starp lielāko un mazāko vērtību ir 2, tāpēc $k=\frac{1-(-1)}{2}=1$" (svītrojot vārdus „amplitūda jeb"). | Fizikā (svārstības, viļņi) funkcijas $y=k\cos x$ amplitūda ir $\lvert k \rvert$, t. i., puse no starpības $y_{max}-y_{min}$; funkcijai $y=\cos x$ amplitūda ir 1, nevis 2. Dotā definīcija ir pretrunā gan ar fizikas kursu, gan ar dokumentā lietoto formulu $k=\frac{y_{max}-y_{min}}{2}$ (un pašā teikumā amplitūda „2" tiek pielīdzināta $k=1$). |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | 1.–3. stunda, uzdevums „Uzraksti leņķi formā $\alpha+360^\circ\cdot n$" (r. 294–296) | „…$\alpha$ ir pozitīvs leņķis intervālā $[0^\circ;180^\circ]$" | „…$\alpha$ ir leņķis intervālā $[0^\circ;360^\circ)$" (vai citādi saskaņot nosacījumu ar piemēriem) | Divas neprecizitātes: (a) $0^\circ$ nav pozitīvs leņķis; (b) ar $\alpha\in[0^\circ;180^\circ]$ šādā formā nav izsakāms jebkurš leņķis (piem., $300^\circ$). Dotie trīs piemēri nosacījumam atbilst, bet vispārīgais formulējums ir maldinošs. |
| 2.2 | 9.–10. stunda (r. 749–751) | „…negatīvām $x$ vērtībām, kas atrodas intervālā $[-\pi;0]$, būs negatīvas sinusa vērtības" | „…negatīvām $x$ vērtībām, kas atrodas intervālā $(-\pi;0)$, būs negatīvas sinusa vērtības" | Galapunktos $x=-\pi$ un $x=0$ sinusa vērtība ir $0$, tāpēc intervālam jābūt vaļējam. |
| 2.3 | 12. stunda, tangensa īpašību tabula, 2. īpašība (r. 894) | „Vērtību kopa $E(f)=(-\infty+\infty)$" | „Vērtību kopa $E(f)=(-\infty;+\infty)$" | Formulā izlaists semikols; pašreizējais pieraksts izskatās pēc summas. |
| 2.4 | 4.–8. stunda, sadaļa par $\arcsin$, $\arccos$, $\mathrm{arctg}$ (r. 664–684) | „ja $\sin x=a$, tad $x=\arcsin a$" (analoģiski $\cos$, $\mathrm{tg}$) | „ja $\sin x=a$, tad **viens no šādiem leņķiem** ir $x=\arcsin a$" (+ īsa piezīme, ka visus leņķus atradīs 10. tematā) | Vienādojumam $\sin x=a$ ir bezgalīgi daudz atrisinājumu, tāpēc implikācija šādā formā ir nekorekta. Kursīvā piezīme par vienkāršojumu jau ir, bet pamatteksta formulējumu vērts precizēt, lai neveidotu maldīgu priekšstatu pirms trigonometrisko vienādojumu temata. |
| 2.5 | Plānojums (r. 121–123) un 4.–8. stundas SR (r. 412–413) | „Salīdzina viena un tā paša leņķa vai divu dažādu leņķu **sinusus un kosinusus**, lietojot TVR." | „Salīdzina viena un tā paša leņķa vai divu dažādu leņķu **sinusus, kosinusus un tangensus**, lietojot TVR." | Programmas paraugā attiecīgais SR ietver arī tangensus („…sinusus, kosinusus un tangensus, izmantojot trigonometrisko vienības riņķi"), un arī `OL_8_dl_2` 4. uzdevumā ir tangensu salīdzināšana (piem., $\mathrm{tg}\,16^\circ$ un $\mathrm{tg}\,88^\circ$). SR formulējums šaurāks nekā reālais saturs. |
| 2.6 | 4.–8. stunda, definīciju izvedums TVR (r. 426–431) | „Aplūkojot taisnleņķa trijstūri $BCO$, var uzrakstīt…" | Pirms tam pievienot teikumu, piem.: „No punkta $B$ velk perpendikulu pret $x$ asi; tā pamatu apzīmē ar $C$." | Punkts $C$ tekstā nekur nav definēts (redzams tikai attēlā); lasītājam bez attēla izvedums nav izsekojams. |
| 2.7 | 4.–8. stunda, vispārīgās definīcijas ar rādiusu $R$ (r. 465–477) | „Par leņķa $\alpha$ sinusu sauc punkta $B$ ordinātas $y$ attiecību pret rādiusu $R$…" | Pirms definīcijām precizēt: „$B$ — pagrieziena leņķa $\alpha$ kustīgās malas un riņķa līnijas (ar centru $O$ un rādiusu $R$) krustpunkts." | Pārejot no TVR ($R=1$) uz vispārīgo definīciju, punkts $B$ un rādiuss $R$ netiek no jauna definēti; nav pateikts, ka definīcija nav atkarīga no $R$ izvēles. Iesakām arī apsvērt citus burtus tangensa ass izklāstā (r. 486–497), kur $A$ un $B$ tiek pārdefinēti ar citu nozīmi ($A=(1;0)$, $B$ uz tangensa ass) nekā iepriekšējā izklāstā. |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 Darba lapu numerācijas neatbilstība un, iespējams, trūkstoša 1. darba lapa.** Temata plānojumā minētas „1.–6. darba lapa", bet projektā pieejami tikai faili `OL_8_dl_2` … `OL_8_dl_6`. Teksta atsauce 1.–3. stundas beigās (r. 397–399) — „Pārveido leņķu mērvienības, attēlo pagrieziena leņķi vienības riņķī un nosaka, kurā kvadrantā atrodas pagrieziena leņķis (skat. OL_8_dl_2)" — pēc satura **neatbilst** failam `OL_8_dl_2` (tajā ir vērtību aprēķināšana, leņķu konstruēšana pēc dotas vērtības, salīdzināšana un IT aprēķini, bet nav mērvienību pārveides un kvadrantu noteikšanas uzdevumu). Jāpārbauda, vai komplektā netrūkst faila `OL_8_dl_1` (pagrieziena leņķis, mērvienības, kvadranti), vai arī jālabo atsauce r. 399 un plānojuma numerācija, lai „N. darba lapa" viennozīmīgi atbilstu failam `OL_8_dl_N`.

**3.2 🟠 Kļūdainas atsauces transformāciju sadaļā: `OL_8_dl_3` vietā jābūt `OL_8_dl_6`.** 13.–16. stundas tekstā abas atsauces — „skat. OL_8_dl_3 1. uzdevumu" (r. 1095–1097) un „skat. OL_8_dl_3 2. uzdevumu" (r. 1140–1141) — norāda uz sinusa funkcijas darba lapu, kurā šādu uzdevumu nav. Saturs (1. uzd. — viena transformācija, 2. uzd. — vairākas transformācijas) precīzi atbilst failam `OL_8_dl_6_trig_funkciju_transformacijas`.

**3.3 🟠 Formatīvās vērtēšanas darbi un eksāmenu uzdevumi nav piesaistīti stundām.** Materiālu aprakstā solīti „daži rakstiski formatīvās vērtēšanas darbi", taču tekstā nav nevienas atsauces uz `OL_8_fvd_1` (trigonometriskās sakarības) un `OL_8_fvd_2` (trigonometriskās funkcijas), tāpat nekur nav pieminēts fails `OL_8_eksamenu_uzdevumi`. Ieteicams pievienot norādes: `OL_8_fvd_1` — pēc 4.–8. stundu bloka, `OL_8_fvd_2` — pēc funkciju grafiku/transformāciju apguves (piem., pēc 16. stundas), bet eksāmenu uzdevumu apkopojumu pieminēt kopsavilkuma stundā vai avotu sarakstā.

**3.4 🟠 Jāpārbauda attēlu atbilstība piemēriem.** Fails `media/image33.png` dokumentā izmantots 7 dažādos piemēros (leņķa konstruēšana pēc $\sin$, $\cos$, $\mathrm{tg}$ vērtības un četri salīdzināšanas piemēri) — visos piemēros redzams viens un tas pats attēls, kas diez vai ir iecerēts. Arī `media/image19.png` atkārtojas divās pēc satura atšķirīgās vietās (biežāk lietoto leņķu riņķis r. 395 un tangensa ass izklāsts r. 484). Papildus pēc teikuma „Ja leņķis $\alpha$ ir lielāks nekā $90^\circ$…" (r. 455–463) ir konvertācijā izjaukta tabula ar izmētātiem apzīmējumiem $\alpha$, $A(x;y)$, $x$, $y$ — jāsalīdzina ar oriģinālo izkārtojumu.

**3.5 🟡 „Nav standarta SR" rāmji pieteikti, bet dokumentā to nav.** Materiālu apraksts sola, ka saturs, kas pārsniedz standarta SR, būs „pelēkā rāmī un apzīmēts Nav standarta SR", taču tekstā neviena šāda rāmja nav. Kandidāti marķēšanai: vertikālo asimptotu piezīme pie tangensa (r. 922–924), kotangensa definīcija, papildu uzdevums $y=\sin(2x+\frac{2\pi}{3})-3$ un funkcijas $y=\sin(mx+a)$ transformācija. Ja marķēšana nav paredzēta, attiecīgi jāprecizē apraksts.

**3.6 🟡 Kotangenss tikai definēts, bet tālāk netiek lietots.** Programmas temata mērķī kotangenss ir minēts, taču jēdzienu sarakstā un SR tabulā tā nav; metodiskajā materiālā $\mathrm{ctg}\,\alpha$ parādās vienīgi definīcijā (r. 476–477) — nav ne vērtību piemēru, ne īpašību. Ieteicams vai nu pievienot īsu piemēru/komentāru (piem., ka padziļināti kotangenss tiks lietots 9. tematā), vai definīciju marķēt kā papildsaturu.

**3.7 🟡 Terminu un saīsinājumu konsekvence.** Dokumentā paralēli lietoti „trigonometriskā riņķa līnija (TRL)", „vienības riņķa līnija" un „trigonometriskais vienības riņķis (TVR)"; saīsinājumi TVR un IT plānojuma tabulā (r. 123, 131) parādās, pirms tie tekstā definēti/atšifrēti. Ieteicams izvēlēties vienu pamatterminu (programmas paraugā — „trigonometriskais vienības riņķis") un saīsinājumus atšifrēt pirmajā lietošanas reizē.

**3.8 🟡 Novērojums saistītajā failā (izsekojamībai).** `OL_8_dl_4_kosinusa_funkcija_UZD` tekstā palikusi kopēšanas kļūda no sinusa lapas: „…izvēlies vēl kādu leņķa vērtību un aprēķini atbilstošo **sinusa** vērtību!" — jābūt „**kosinusa** vērtību". Ieteicams izlabot vienlaikus ar metodiskā materiāla labojumiem.

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts |
|---|---|---|---|
| 4.1 | 1.–3. stunda (r. 230–232) | „Kustīgais stars pēc pilna apgrieziena var turpināt rotācijas kustību, tāpēc **tā** lielums var būt jebkurš reāls skaitlis no intervāla $(-\infty;+\infty$)." | „…, tāpēc **pagrieziena leņķa** lielums var būt jebkurš reāls skaitlis no intervāla $(-\infty;+\infty)$." *(vietniekvārds „tā" formāli attiecas uz staru; sakārtojams arī iekavu pieraksts)* |
| 4.2 | 1.–3. stunda (r. 236) | „…pulksteņa rādītāju kustības virzienam **, bet**…" | „…pulksteņa rādītāju kustības virzienam**, bet**…" *(atstarpe pirms komata)* |
| 4.3 | Plānojums (r. 118–119) un 4.–8. stundas SR (r. 410) | „Konstruē leņķi, ja **dotas** šī leņķa trigonometriskās funkcijas **vērtība**." | „Konstruē leņķi, ja **dota** šī leņķa trigonometriskās funkcijas **vērtība**." *(skaitļa saskaņojums; kļūda abās vietās)* |
| 4.4 | 12. stunda, 10. īpašības piezīme (r. 922–924) | „Tangensa funkcijas vērtības **tiecās** uz $+\infty$ vai $-\infty$, kad funkcijas arguments **tiecās** uz šīm vērtībām." | „…vērtības **tiecas** uz $+\infty$ vai $-\infty$, kad funkcijas arguments **tiecas** uz šīm vērtībām." *(tagadnes forma; ieteicams arī precizēt beigas: „…tiecas uz punktiem $x=\frac{\pi}{2}+\pi k$")* |
| 4.5 | 17. stunda, 2. piemērs (r. 1228–1229) | „Koeficients $k$ **ir** vertikālā deformācija, **kas** šajā gadījumā **ir nolasāms** no grafika…" | „Koeficients $k$ **nosaka** vertikālo deformāciju; šajā gadījumā **to var nolasīt** no grafika…" *(dzimtes saskaņojums un precīzāks formulējums)* |
| 4.6 | 11. stunda (r. 818) | „**Līdzīgi spriežot skolēni** patstāvīgi var uzzīmēt…" | „**Līdzīgi spriežot, skolēni** patstāvīgi var uzzīmēt…" |
| 4.7 | 1.–3. stunda (r. 279–280) | „Ja pagrieziena leņķis **pārsniedz $360^\circ$ vai $-360^\circ$**…" | „Ja pagrieziena leņķa **lielums pēc moduļa pārsniedz $360^\circ$**…" |
| 4.8 | Visā dokumentā | Konvertācijas artefakti: „\*\*\\\*\*" (lappušu pārtraukumu paliekas ~11 vietās, piem., r. 82, 523, 602), klaiņojošs saraksta marķieris „- " pēc plānojuma tabulas (r. 195), „kuriem\\\*" (r. 567), tukšu tabulu rāmji (r. 240–242, 272–277) | Veikt pilnu tehnisko korektūru pēc konvertācijas — dzēst artefaktus, atjaunot tabulu izkārtojumu. |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Iekļaut programmas pēdējo SR — fizikālu lielumu modelēšanu ar lietotnēm.** Programmas paraugā 8. temata pēdējais SR paredz: „Izmantojot dotas lietotnes, pēta un matemātiski raksturo fizikālus lielumus, kas raksturo skaņu, mehāniskās svārstības u. tml., ja sakarību starp tiem raksturo funkcija $y=a\cdot\sin(bx+c)$…". Metodiskajā materiālā fizika pieminēta tikai vienā vispārīgā rindkopā (r. 801–804). Ieteicams 17. stundā pievienot vismaz vienu praktisku aktivitāti/piemēru (piem., skaņas svārstību ieraksta vai simulācijas analīze, nosakot amplitūdu un periodu), kas šo SR īsteno.

**5.2 Piezīme pie parametru formulām 17. stundā.** Formula $k=\frac{y_{max}-y_{min}}{2}$ dod $\lvert k \rvert$; vērts pievienot piezīmi, ka $k$ zīmi nosaka no grafika (piem., vai maksimums atrodas tur, kur pamatfunkcijai $\cos$ ir maksimums, vai simetriski pretī).

**5.3 Saikne ar 9. tematu piemērā $y=4\sin\left(x+\frac{\pi}{2}\right)$.** Pēc grafika konstruēšanas vērts pamanīt, ka iegūtais grafiks sakrīt ar $y=4\cos x$ — tas dabiski sagatavo redukcijas formulu ideju 9. tematā un stiprina izpratni, ka viena funkcija var būt pierakstīta dažādos veidos.

**5.4 Raksturīgo kļūdu akcenti pie leņķa izteikšanas formā $\alpha+360^\circ\cdot n$.** Piemērā $-1345^\circ=-4\cdot360^\circ+95^\circ$ vērts pievienot skolotāja piezīmi par tipisko kļūdu negatīviem leņķiem (skolēni bieži iegūst $-1345^\circ=-3\cdot360^\circ-265^\circ$ un apstājas) un parādīt algoritmu ar dalīšanu ar $360^\circ$; līdzīga labā prakse (kursīva piezīme par raksturīgu kļūdu) dokumentā jau ir transformāciju sadaļā.

---

### Kopsavilkums

Dokuments kopumā ir saturiski bagāts, labi strukturēts pa stundu grupām un atbilst programmas parauga 8. temata apjomam (20 stundas) un sasniedzamajiem rezultātiem; īpaši vērtīgas ir skolotāja piezīmes kursīvā un pilnie transformāciju piemēri.

Pirms publiskošanas obligāti jānovērš 1. sadaļas matemātiskie labojumi — pārveidošanas virziena kļūda (1.1), skaitliskās kļūdas piemēros (1.2, 1.3), sinusoīdas pārneses virziens (1.4), deformācijas koeficienta „$k$ reizes / $\frac{1}{k}$ reizes" formulējumi transformāciju tabulā (1.5, 1.6) un amplitūdas definīcijas pretruna ar fizikas terminoloģiju (1.7) — kā arī jāsakārto atsauces uz darba lapām (3.1, 3.2), jo tās skolotāju noved pie nepareizā faila.

Ieteicams arī papildināt tekstu ar norādēm uz formatīvās vērtēšanas darbiem un eksāmenu uzdevumu apkopojumu (3.3), pārbaudīt attēlu atbilstību pēc konvertācijas (3.4) un veikt pilnu redakcionālo korektūru (4. sadaļa).
