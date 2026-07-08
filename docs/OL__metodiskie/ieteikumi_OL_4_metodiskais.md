---
layout: default
title: "Ieteikumi par 4. tematu"
permalink: /OL__metodiskie/ieteikumi_OL_4_metodiskais/
---

# Labojumu un ieteikumu saraksts — „OL_4. Vienādojumu sistēmas" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_4__temats_metodiskais.md` (15 stundas).
**Salīdzināšanas avoti:** Matemātika I programmas paraugs (4. temats „Vienādojumu sistēmas", 15 stundas), pamatizglītības standarts (M.9.4.3.4., M.9.4.4.1.), projektā pieejamie darba lapu / vērtēšanas darbu faili (OL_4_dl_1 … OL_4_dl_5, OL_4_fvd_1, OL_4_fvd_2, OL_4_npd, OL_4_kopsavilkums, OL_4_eksamenu_uzdevumi).
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).

---

## 1. Matemātiski labojumi 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 1. stunda, 1. uzdevums, pārbaude pārim $(11;1)$ | $18 \neq 14$ | $19 \neq 14$ | $2 \cdot 11 - 3 \cdot 1 = 22 - 3 = 19$, nevis 18. Secinājums (pāris nav atrisinājums) nemainās, bet aprēķins paraugrisinājumā ir kļūdains. |
| 1.2 | 2., 3. stunda, 3. piemērs (daļveida vienādojums), definīcijas kopas noteikšana | $3y \neq 0$ **vai** $2 + 2y \neq 0$ | $3y \neq 0$ **un** $2 + 2y \neq 0$ | Reizinājums nav 0 tad un tikai tad, ja **abi** reizinātāji nav 0 — nosacījumi jāsaista ar konjunkciju „un". Ar „vai" nosacījumu apmierinātu arī $y = 0$. |
| 1.3 | 7.–9. stunda, Vjeta teorēmas piemērs $\left\{\begin{array}{l} x + y = 8 \\ xy = -20 \end{array}\right.$ | $\left\{\begin{array}{l} m_{1} \cdot m_{2} = -20 \\ m_{1} + m_{2} = -8 \end{array}\right.$; saknes $m_1 = -10$, $m_2 = 2$; Atbilde. $(-10;\,2)$ un $(2;\,-10)$ | $\left\{\begin{array}{l} m_{1} \cdot m_{2} = -20 \\ m_{1} + m_{2} = 8 \end{array}\right.$; saknes $m_1 = 10$, $m_2 = -2$; Atbilde. $(10;\,-2)$ un $(-2;\,10)$ | Vienādojumam $m^2 - 8m - 20 = 0$ ir $p = -8$, tātad $m_1 + m_2 = -p = 8$ (saskan ar sistēmas nosacījumu $x + y = 8$). Dokumentā dotā atbilde neapmierina sistēmu: $-10 + 2 = -8 \neq 8$. |
| 1.4 | 7.–9. stunda, grafiskā paņēmiena soļi | „Vienādojuma $f(x) = g(x)$ risināšana ar grafisko paņēmienu: … 3) nolasa grafiku krustpunktu $x$ koordinātas …" | Jāpārraksta soļi **vienādojumu sistēmai**: 1) no katra vienādojuma izsaka $y$ (ja iespējams); 2) vienā koordinātu plaknē uzzīmē abu vienādojumu grafikus; 3) nolasa krustpunktu **abas koordinātas** $(x;\,y)$ un veic pārbaudi; 4) uzraksta atbildi. | Ievietotā shēma attiecas uz viena vienādojuma $f(x)=g(x)$ risināšanu (acīmredzot pārnesta no iepriekšēja temata). Sistēmas atrisinājums ir skaitļu **pāris**, tāpēc nolasīt tikai $x$ koordinātas ir nepietiekami; shēma ir pretrunā ar tālāk dotajiem piemēriem, kuros nolasa abas koordinātas, piem., $(-3;\,7)$. |
| 1.5 | 7.–9. stunda, grafiskā paņēmiena 2. piemērs $\left\{\begin{array}{l} y - x^{2} = 1 \\ xy = 8 \end{array}\right.$ | $y = x^{2} - 1$; „krustpunkts ir aptuveni $(2{,}3;\ 3{,}4)$" | $y = x^{2} + 1$; krustpunkts ir aptuveni $(1{,}8;\ 4{,}4)$ | No $y - x^2 = 1$ izriet $y = x^2 + 1$, nevis $y = x^2 - 1$. Arī norādītais aptuvenais krustpunkts neatbilst nevienai no versijām (precīzāk: $x^3 + x - 8 = 0$, $x \approx 1{,}83$; $y \approx 4{,}37$). Alternatīva: mainīt sistēmas pirmo vienādojumu uz $y - x^2 = -1$, tad $y = x^2 - 1$ un krustpunkts $\approx (2{,}2;\ 3{,}7)$. Jebkurā gadījumā jāsaskaņo attēls (image5). |
| 1.6 | 10.–12. stunda, motorlaivas uzdevums | „Atrisinot sistēmu, iegūst, ka $x = \pm 3$ un $y = \pm 9$." … „Iegūtās negatīvās vērtības uzdevumam neatbilst." | „Atrisinot sistēmu, iegūst $y = 9$ un $x = \pm 3$." … „Vērtība $x = -3$ uzdevumam neatbilst, jo straumes ātrums nevar būt negatīvs ($x > 0$)." | Sistēmas atrisinājumi ir $(3;\,9)$ un $(-3;\,9)$ — vērtība $y = -9$ **nav** sistēmas atrisinājums (piem., $\frac{28}{-12} + \frac{28}{-6} = -7 \neq 7$). Pieraksts $x = \pm 3$ un $y = \pm 9$ kļūdaini ļauj domāt, ka der arī pāri ar $y = -9$. |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | 2., 3. stunda, 2. piemērs | „negatīva un pozitīva skaitļa kvadrāts ir viens un tas pats skaitlis" | „savstarpēji pretēju skaitļu kvadrāti ir vienādi, t. i., $(-a)^2 = a^2$" | Formulējums, kā uzrakstīts, ir aplams vispārīgā gadījumā (piem., $(-2)^2 \neq 3^2$); runa ir tieši par pretējiem skaitļiem. |
| 2.2 | 1. stunda, piemērs par sistēmu bez atrisinājuma | „jo, saskaitot divus vienādus skaitļus, nav iespējams iegūt dažādas summas" | „jo, saskaitot vienus un tos pašus divus skaitļus, nav iespējams iegūt divas dažādas summas" | „Divi vienādi skaitļi" nozīmētu $x = y$, kas no sistēmas $\left\{\begin{array}{l} x + y = 10 \\ x + y = 21 \end{array}\right.$ neizriet; jāsaskaita viena un tā pati summa $x + y$. |
| 2.3 | 2.–4. stundas sasniedzamie rezultāti | „Risina vienādojumu sistēmas ar diviem **nezināmajiem**…" | „…ar diviem **mainīgajiem**…" | Standarts, programmas paraugs un paša dokumenta plānojums konsekventi lieto „mainīgais"; stundu aprakstos parādās „nezināmais". Jāizvēlas viens termins visā dokumentā. |
| 2.4 | Temata plānojums (7.–9. st.), 10.–12. st. ievads | „izvēloties risināšanas **metodi**"; „lieto piemērotāko atrisināšanas **metodi**" | „izvēloties (piemērotāko) risināšanas **paņēmienu**" | Programmas paraugā SR formulēts „izvēloties atbilstošāko paņēmienu"; dokumentā jaukti lietoti „metode" un „paņēmiens". Ieteicams: ievietošanas/saskaitīšanas/grafiskais **paņēmiens**, substitūcijas **metode** (kā programmas jēdzienu sarakstā), bet izvēles SR — „paņēmiens". |
| 2.5 | 10.–12. stunda, jautājumi un komentāri pirms motorlaivas uzdevuma | „pirmajai **vienādībai**", „otro **vienādību**", „viena **vienādība** būs par esošo situāciju", „tekstuālajai **vienādībai**" | „pirmajam **vienādojumam**", „otro **vienādojumu**" utt. | Veidojot matemātisko modeli ar mainīgajiem, tiek sastādīti **vienādojumi**; „vienādība" šeit lietota neprecīzi un nekonsekventi ar pārējo tekstu. |
| 2.6 | 1. stunda, 4. uzdevums (pāris $(6;m)$) | „Drīkst izvēlēties jebkuru no vienādojumiem." | Papildināt: „…, bet iegūtā $m$ vērtība **jāpārbauda arī otrā vienādojumā** — pāris ir sistēmas atrisinājums tikai tad, ja tas apmierina abus vienādojumus." | Šajā piemērā abi vienādojumi dod $m = 4$, taču vispārīgi vērtības varētu atšķirties (tad tāda $m$ nav). Bez šīs piebildes skolēniem var veidoties maldīgs priekšstats. |
| 2.7 | 1. stunda, 3. uzdevums (taisnstūra perimetrs) | „…kuras atrisinājumi var būt šādi skaitļu pāri $(3;2)$ un $(2;3)$." | Norādīt, ka sistēmas otrais vienādojums $2(a+3) + 2(b+2) = 20$ pēc vienkāršošanas sakrīt ar pirmo ($2a + 2b = 10$), tāpēc sistēmai ir **bezgalīgi daudz atrisinājumu** — der jebkurš pāris ar $a + b = 5$ ($a, b > 0$), piem., arī $(4;1)$ vai $(2{,}5;\ 2{,}5)$. | Kā uzrakstīts, teksts liek domāt, ka atrisinājumi ir tikai divi konkrēti pāri. Situāciju vērts izmantot mērķtiecīgi — tā lieliski sasaistās ar iepriekš uzdoto jautājumu, kādos gadījumos sistēmai ir viens, neviens vai bezgalīgi daudz atrisinājumu (vai arī mainīt skaitļus, lai sistēmai būtu viens atrisinājums). |
| 2.8 | 4. stunda, ievada piemērs | „Ja vienādojuma (I) **koeficientus** sareizina ar 4 iegūst…" | „Ja vienādojuma (I) **abas puses** pareizina ar 4, iegūst…" | Jāreizina viss vienādojums (arī brīvais loceklis labajā pusē), nevis tikai koeficienti; risinājumā tas arī izdarīts ($8 \cdot 4$ nav, bet $2 \cdot 4 = 8$ ir). Trūkst arī komata pirms „iegūst". |
| 2.9 | Metodiskais komentārs par tematu (ievads) | „…padziļina prasmes jaunās situācijās, ja sistēmā ir daļveida vienādojumi." | „…padziļina prasmes jaunās situācijās, ja sistēmā ir **otrās pakāpes vai daļveida vienādojumi**." | Gan programmas paraugs, gan pats materiāls (piemēri ar $x^2 + y^2 = 41$ u. c.) jaunajās situācijās iekļauj arī otrās pakāpes vienādojumus; ievadā minēti tikai daļveida. |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 SR formulējumu saskaņošana plānojumā un stundu aprakstos.** Temata plānojumā SR sākas ar „**Atrisina**…", bet 2.–6. stundas aprakstos — ar „**Risina**…"; plānojumā „ar diviem mainīgajiem", aprakstos „ar diviem nezināmajiem" (sk. 2.3); plānojumā „izvēloties risināšanas metodi", 7.–9. stundas aprakstā „izvēloties risināšanas paņēmienu" (sk. 2.4). Ieteicams SR formulējumus padarīt burtiski identiskus abās vietās.

**3.2 🟠 Materiālu apraksta rindkopa par ieteikumiem skolotājam.** Teikumā „(dažādi metodiskie ieteikumi … programmas paraugā." atvērtā iekava netiek aizvērta, un nākamais teikums par pelēko rāmi „Nav standarta SR" iesākas bez pārejas. Jāsakārto interpunkcija un teikumu robežas. Turklāt tematā neviena sadaļa nav marķēta ar „Nav standarta SR" — vai nu šis apraksta fragments jāsvītro, vai (ieteicams) ar to jāmarķē padziļinājuma saturs, piemēram, Vjeta teorēmas lietošana sistēmu risināšanā (7.–9. stunda), kas pārsniedz programmas parauga SR.

**3.3 🟡 Substitūcijas metodes piemēra tabula (5., 6. stunda).** Sistēma $\left\{\begin{array}{l} 2m - n = 1 \\ 3m + 2n = 5 \end{array}\right.$ tabulā parādīta divas reizes pēc kārtas bez izmaiņām, un tikai trešajā solī redzama sistēma pēc reizināšanas ar 2. Otrajā attēlojumā jāpievieno pārveidojuma norāde (piem., „$| \cdot 2$" pie (I) vienādojuma) vai dublējošais bloks jādzēš.

**3.4 🟡 Vienots darbību pieraksts pie vienādojumiem.** Dokumentā jaukti lietoti apzīmējumi „$\mid :(-7)$", „$\mid \cdot 2$" un „$/:( - 7)$", „$/ \cdot (-1)$". Ieteicams visā materiālā (un darba lapās) lietot vienu pierakstu, piemēram, ar vertikālo svītru.

**3.5 🟡 Atsauce uz eksāmenu uzdevumu failu.** Projektā ir fails `OL_4_eksamenu_uzdevumi`, bet metodiskajā materiālā tas nekur nav pieminēts (atšķirībā no visiem pārējiem pavadmateriāliem). Ieteicams pievienot norādi, piemēram, kopsavilkuma stundā vai pie temata padziļinājuma iespējām.

**3.6 🟡 Ekvivalento pārveidojumu noteikumu precizēšana (1. stunda).** Noteikumos 2) un 3) vērts precizēt, ka: 2) vienādojums, no kura izteikts mainīgais, sistēmā jāsaglabā (formā $x = \ldots$); 3) ar vienādojumu summu drīkst aizstāt tikai vienu no saskaitāmajiem vienādojumiem, otru atstājot sistēmā nemainītu. Pretējā gadījumā ekvivalence var zust.

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts |
|---|---|---|---|
| 4.1 | Ievads | „jāprot lietot substitūcijas metode" | „jāprot lietot substitūcijas metodi" |
| 4.2 | 1. stunda, definīcija | „sauc visus tos sakārtotu skaitļu pārus" | „sauc visus tos sakārtotos skaitļu pārus" |
| 4.3 | 2., 3. stunda, 1. piemērs | „tāpēc no šīs vienādojuma ir viegli izteikt" | „tāpēc no šī vienādojuma ir viegli izteikt" |
| 4.4 | 2., 3. stunda, 1. piemērs | „darbības zīme, kuru neraksta algebriskās izteiksmēs ir reizināšana" | „darbības zīme, kuru neraksta algebriskajās izteiksmēs, ir reizināšana" |
| 4.5 | 2., 3. stunda, 2. piemērs | „jo (II) vienādojumā $x^{2}$ un $y^{2}.$" (nepabeigts teikums) | „jo (II) vienādojumā ir gan $x^{2}$, gan $y^{2}$." |
| 4.6 | 4. stunda, 1. piemērs | „ievieto vienā no dotās sistēma … vienādojumiem" | „ievieto vienā no dotās sistēmas … vienādojumiem" |
| 4.7 | 5., 6. stunda | „abos vienādojumus paliktu tikai jaunie mainīgie" | „abos vienādojumos paliktu tikai jaunie mainīgie" |
| 4.8 | 7.–9. stunda, salīdzinājuma tabula | „*Substitūcija metode*"; „t. i,." | „*Substitūcijas metode*"; „t. i.," |
| 4.9 | 7.–9. stunda | „Ja klase spējīga, tad iespējams var parādīt vēl kādu paņēmienu" | „Ja klase ir spējīga, iespējams parādīt vēl kādu paņēmienu" |
| 4.10 | 13. stunda, SR | „Veic tēmas apkopojumu" | „Veic temata apkopojumu" (konsekventi ar pārējo dokumentu) |
| 4.11 | 14., 15. stunda, SR | „Pārbauda zināšanas un prasmes tematā vienādojumu sistēmas." | „Pārbauda zināšanas un prasmes tematā „Vienādojumu sistēmas"." |
| 4.12 | Visā dokumentā | Konversijas artefakti: atsevišķi „**\\**" simboli, `<!-- -->` fragments 2. piemērā, paplašināšanas pieraksts ar augšrakstu, kas eksportā izskatās deformēts | Jāpārbauda gala formāta atveidojums un artefakti jāiztīra |
| 4.13 | Attēli (image1–image5) | Automātiski ģenerēti alt-teksti („A green rectangle with black text AI-generated content may be incorrect…", „Attēls, kurā ir teksts, ekrānuzņēmums…") | Jāaizstāj ar jēgpilniem aprakstiem latviešu valodā (piekļūstamība), piem., „Taisnstūris ar malām a un b" |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Atrisinājuma pārbaude pret definīcijas kopu.** Daļveida sistēmu piemēros definīcijas kopa tiek noteikta risinājuma sākumā (labi!), bet nobeigumā iegūtais atrisinājums pret to netiek eksplicīti pārbaudīts (piem., substitūcijas piemērā $(1;\,0)$ — pārliecināties, ka $x \neq y$ un $x \neq -y$; motorlaivas uzdevumā — ka saucēji nav 0). Ieteicams pievienot vienu teikumu par šo soli, jo tas veido programmas akcentēto ieradumu izvērtēt rezultātu.

**5.2 Grafiskajā daļā parādīt arī 0 un bezgalīgi daudzu atrisinājumu gadījumus.** 1. stundā skolēni tiek rosināti spriest, kad sistēmai nav atrisinājuma, bet grafiskā paņēmiena sadaļā apskatīti tikai krustošanās gadījumi. Vērtīgi pievienot paralēlu taišņu (nav atrisinājuma) un sakrītošu taišņu (bezgalīgi daudz atrisinājumu) piemērus — tas dabiski sasaistās arī ar 2.7 punktā minēto taisnstūra uzdevumu.

**5.3 Digitālo rīku izmantošana.** Grafiskā paņēmiena piemēros (īpaši sistēmai ar parabolu un hiperbolu) ieteicams tieši norādīt uz dinamiskās ģeometrijas rīkiem (piem., GeoGebra, Desmos) gan grafiku zīmēšanai, gan atrisinājumu skaita un aptuveno vērtību noteikšanai; pašlaik IT pieminēta tikai pārbaudes kontekstā.

**5.4 Vjeta teorēmas lietojuma precizēšana.** Nosakot saknes no summas un reizinājuma, faktiski tiek lietota Vjeta teorēmai **apgrieztā** teorēma. Vismaz vienā vietā (7.–9. stundā, kur tas jau daļēji pateikts ar „apgrieztā veidā") to vērts nosaukt korekti, lai skolotājam būtu skaidrs loģiskais pamatojums.

---

### Kopsavilkums

Dokuments kopumā ir labi strukturēts, pilnībā pārklāj programmas parauga sasniedzamos rezultātus (atrisinājuma jēdziens un pārbaude, ievietošanas un saskaitīšanas paņēmiens, substitūcijas metode, paņēmiena izvēle, vienādojumu sistēma kā matemātiskais modelis), un stundu sadalījums atbilst paredzētajām 15 stundām; teksta uzdevumu un paņēmienu salīdzināšanas piemēri ir metodiski vērtīgi.

Pirms publiskošanas obligāti jānovērš 1. sadaļā minētās sešas matemātiskās kļūdas — īpaši Vjeta teorēmas piemēra kļūdainā atbilde (1.3), grafiskā piemēra nepareizi izteiktā funkcija un neatbilstošais krustpunkts (1.5), kā arī motorlaivas uzdevuma atrisinājumu pieraksts (1.6), jo tie ir paraugrisinājumi, ko skolotāji var pārņemt tieši.

Ieteicams arī saskaņot terminoloģiju (mainīgais/nezināmais, paņēmiens/metode, vienādojums/vienādība), izlabot 2. un 3. sadaļā minētās precizitātes un konsekvences vietas un veikt pilnu valodas korektūru, iekļaujot konversijas artefaktu tīrīšanu un attēlu alt-tekstu latviskošanu.
