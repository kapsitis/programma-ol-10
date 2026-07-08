---
layout: default
title: "Ieteikumi par 1. tematu"
---

# Labojumu un ieteikumu saraksts — „OL_1. Sadalīšana reizinātājos un vienādojumu atrisināšanas metodes" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_1__sadalisana_reizinatajos_vienadojumi_metodiskais.md` (17 stundas).
**Salīdzināšanas avoti:** programmas paraugs (1. temats, 17 st.), standarta M.O. kodi, projektā pieejamie darba lapu / vērtēšanas darbu faili.
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).

---

## 1. Matemātiski labojumi 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 2. stunda, 5. paņēmiens „Vjeta teorēma vienādojumam $ax^2+bx+c=0$", vispārīgā formula | $x_{1} + x_{2} = \frac{b}{a}$ | $x_{1} + x_{2} = -\frac{b}{a}$ | Blakus esošie piemēri ($x_1+x_2=2{,}5$; $x_1+x_2=1{,}2$) ir rēķināti **pareizi**, t. i., ar mīnusa zīmi — kļūda ir tikai vispārīgajā rāmī. |
| 1.2 | 2. stunda, 6. paņēmiens „Lietojot palīgvienādojumu un Vjeta teorēmu", vispārīgais rāmis | $t_{1} + t_{2} = b$ | $t_{1} + t_{2} = -b$ | Palīgvienādojumam $t^2+bt+ac=0$ sakņu summa ir $-b$. Arī šeit abi piemēri ir izrēķināti pareizi ($t_1+t_2=-1$; $t_1+t_2=6$), kļūda tikai vispārīgajā formulā. |
| 1.3 | 2. stunda, 4. paņēmiens „Vjeta teorēma (reducētam…)", piemērs $x^{2}-4x=0$ | Ja $\{x_1+x_2=4;\ x_1\cdot x_2=0\}$, tad $x_{1} = -4$ un $x_{2} = 0$. | … tad $x_{1} = 0$ un $x_{2} = 4$. | Uzrakstītās vērtības ($-4$ un $0$) neapmierina pašu pierakstīto sistēmu (summa būtu $-4$, nevis $4$); rindā „Atbilde" saknes jau ir pareizas. |
| 1.4 | 2. stunda, 2. paņēmiens „Ar sakņu formulu", piemērs $x^{2}-16=0$ | $D = 0^{2} - 4 \bullet 1 \bullet 16 = 64$ | $D = 0^{2} - 4 \bullet 1 \bullet (-16) = 64$ | Rezultāts 64 ir pareizs, bet pierakstītā izteiksme, kā uzrakstīta, ir vienāda ar $-64$; koeficients ir $c=-16$. |
| 1.5 | 2. stunda, 2. paņēmiens, piemērs $x^{2}-4x=0$ | $x_{2} = \frac{4 - \sqrt{4}}{2} = 0$ | $x_{2} = \frac{4 - \sqrt{16}}{2} = 0$ | Zem saknes jābūt $D=16$ (iepriekšējā rindā $x_1$ rēķināts ar $\sqrt{16}$). |
| 1.6 | 4. stunda, „3. Starpības kvadrāts", 1. piemērs | $y^{2} - 8x + 16 = (y - 4)^{2}$ | $y^{2} - 8y + 16 = (y - 4)^{2}$ | Sajaukti mainīgie ($x$ un $y$ vienā izteiksmē). |
| 1.7 | 4. stunda, turpat, izvērstais pieraksts | $y^{2} - 8y + 16 = y^{2} - 2 \bullet 4 \bullet y + 4^{2} = y^{2} - 8y + 16.$ | $y^{2} - 8y + 16 = y^{2} - 2 \bullet 4 \bullet y + 4^{2} = (y - 4)^{2}.$ | Pārveidojumu ķēde noslēdzas „aplī" (atgriežas pie sākuma izteiksmes), nevis pie rezultāta $(y-4)^2$. |
| 1.8 | 7.–8. stunda, piemērs „Sadali izteiksmi $-m^{3}n + mn$ reizinātājos!" (otrā rinda) | $-m^{3}n - mn = -mn(m^{2}-1) = -m(m-1)(m+1)$ | $-m^{3}n + mn = -mn(m^{2}-1) = -mn(m-1)(m+1)$ | Divas kļūdas vienā rindā: (a) zīme pie $mn$ atšķiras no uzdevuma nosacījuma („$+mn$"); (b) gala sadalījumā pazudis reizinātājs $n$. |
| 1.9 | 9. stunda, 2. piemēra atbilde | Atbilde. $x_{1} =$, $x_{2} = 2$, $x_{3} = 3$ un $x_{4} = -4$ | Atbilde. $x_{1} = 0$, $x_{2} = 2$, $x_{3} = 3$ un $x_{4} = -4$ | Izkritusi pirmās saknes vērtība $0$. |
| 1.10 | 2. stunda: pilnā kvadrātvienādojuma piemēru saraksts pret izrēķināto piemēru „Ar sakņu formulu" | Sarakstā: $-3x^{2} + 4x + 10 = 0$; tabulā izrēķināts: $3x^{2} + 4x + 10 = 0$ ($D=-104$, nav reālu sakņu) | Saskaņot abas vietas, piemēram, abās lietot $3x^{2} + 4x + 10 = 0$ | Būtiski: ar mīnusa zīmi ($a=-3$) vienādojumam $D = 16+120 = 136 > 0$ un tam **ir** divas reālas saknes, tātad tabulas secinājums „nav reālu sakņu" atbilst tikai variantam bez mīnusa zīmes. |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | 5. stundas sasniedzamais rezultāts | „Zina un lieto saīsinātās reizināšanas formulas **(summas/starpības kubs)**, lai sadalītu izteiksmi reizinātājos." | „… formulas **(kubu summa un kubu starpība)** …" | „Summas kubs" $(a+b)^3$ un „kubu summa" $a^3+b^3$ ir **dažādas** formulas; stundā tiek mācīta tieši kubu summa/starpība. Temata plānojuma tabulā un programmā terminoloģija ir pareiza — kļūda ir tikai stundas SR formulējumā. |
| 2.2 | 4. stunda (kvadrātu starpības vārdiskais skaidrojums) un 5. stunda (abu kubu formulu skaidrojumi) — 3 vietas | „… viens no reizinātājiem ir šo izteiksmju starpība, bet **otrs reizinājums** ir …" | „… bet **otrs reizinātājs** ir …" | Jaukti jēdzieni „reizinātājs" un „reizinājums"; kļūda atkārtojas visos trīs vārdiskajos formulējumos. |
| 2.3 | 2. stunda, reducētā kvadrātvienādojuma piemēri | Kā reducētā vienādojuma piemērs dots $-(x+1)^{2} + 4 = 0$ | Aizstāt ar piemēru formā $x^2+px+q=0$ (piem., $x^{2}+2x-3=0$) **vai** pievienot pārveidojumu, kas parāda, ka vienādojums ir ekvivalents reducētam | Dotajā pierakstā vienādojums nav formā $ax^2+bx+c=0$, un pēc iekavu atvēršanas $a=-1\neq 1$ — piemērs ir pretrunā ar tekstā doto definīciju („kuram $a=1$"). |
| 2.4 | 12. stunda, piezīme „Ja grafiki krustojas …" | „Ja grafiki **krustojas** … Ja grafiki **nekrustojas**, tad vienādojumam nav atrisinājumu." | Lietot formulējumu „ja grafikiem ir … **kopīgi punkti**" | „Krustošanās" neietver saskares (pieskaršanās) punktus, taču arī tie ir vienādojuma atrisinājumi — paša materiāla 2. stundas grafiskajā piemērā $2x^{2}=0$ sakne $x=0$ ir tieši saskares punkts. |
| 2.5 | 12. stunda, piemēra $\frac{2}{x} = 0{,}125x^{3}$ pamatojums | „…, jo, ja $x > 2$, viena no funkcijām ir augoša un otra dilstoša un, ja $x < -2$, tad …" | Pamatojumu veidot pa intervāliem $(0;\,+\infty)$ un $(-\infty;\,0)$: katrā no tiem viena funkcija ir augoša, otra — dilstoša, tāpēc katrā ir ne vairāk kā viena sakne | Pašreizējie intervāli $x>2$ un $x<-2$ atstāj nepamatotus intervālus $(-2;0)$ un $(0;2)$ — pamatojums, ka citu sakņu nav, ir nepilnīgs. |
| 2.6 | 13. stunda, piemērs $\frac{2}{x} = x^{2}-2x+1$ | „Šo vienādojumu **nevar atrisināt** ar sadalīšanu reizinātājos vai substitūciju." | „Šo vienādojumu ar **līdz šim aplūkotajiem paņēmieniem tieši** atrisināt neizdodas / ir neērti; ērti ir izmantot funkciju īpašības un spriest." | Apgalvojums, kā uzrakstīts, ir matemātiski aplams: reizinot ar $x$ ($x\neq0$), iegūst $x^{3}-2x^{2}+x-2=0$, ko var sadalīt ar grupēšanu: $x^{2}(x-2)+(x-2)=(x-2)(x^{2}+1)$. |
| 2.7 | 9. stunda, vispārīgais secinājums | „… tad var secināt, ka **kāds no nezināmajiem lielumiem ir 0 vai visi ir vienādi ar 0**." | „… tad **vismaz viens no reizinātājiem** ir vienāds ar 0." | Formulējums „kāds … vai visi" ir lieks un mulsinošs; „vismaz viens" ir standarta, precīzs formulējums (tas ietver arī gadījumu „visi"). |
| 2.8 | 2. stunda, 4.–6. paņēmiens (Vjeta teorēma) | Sakņu **atrašana** no sistēmas tiek saukta „Vjeta teorēma" | Pievienot skolotāja piezīmi, ka sakņu atrašanai faktiski lieto Vjeta teorēmai **apgriezto** teorēmu | Neliela konceptuāla precizitāte; skolēniem pietiek ar esošo, bet skolotāja piezīme novērstu iespējamus pārmetumus recenzijās. |
| 2.9 | 6. stunda, 3. piemērs (secinājums pie $D<0$) | „Doto kvadrāttrinomu **nav iespējams sadalīt reizinātājos**." | Apsvērt precizējumu „… nav iespējams sadalīt **lineāros reizinātājos ar reāliem koeficientiem**" (vismaz skolotāja piezīmē) | Skolas konvencijai atbilstoši var atstāt kā ir, bet piezīme stiprinātu korektumu (piem., $4x^4+1$ tipa pretpiemēri augstākā līmenī). |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 Trūkst atsauces uz vidusskolas standarta (M.O.) kodiem.** Dokumentā ir citēti tikai pamatskolas standarta rezultāti (M.9.4.3.1., M.9.4.3.4.), bet ne reizi nav norādīti temata vidusskolas kodi, kurus min programma: *Izteiksmes sadalīšana reizinātājos* — M.O.1.1.2., M.O.1.2.2., M.O.2.2.2., M.O.4.4.1., M.O.4.4.2.; *Vienādojumu risināšanas metodes* — M.O.1.1.2., M.O.1.2.2., M.O.4.4.2., M.O.4.5.1. **Ieteikums:** pievienot šos kodus sadaļā „Metodiskais komentārs par tematu" (un/vai temata plānojuma tabulā pie stundu grupām) — tas nodrošina izsekojamību standarts ↔ programma ↔ metodiskais materiāls.

**3.2 🟠 Deklarētā konvencija „Nav standarta SR" tematā nav lietota.** Sadaļā „Materiālu apraksts" solīts: *„Saturs, kas pārsniedz standarta sasniedzamos rezultātus, ir pelēkā rāmī un apzīmēts Nav standarta SR."* Dokumenta pamattekstā šāds apzīmējums neparādās ne reizi, lai gan ir saturs, kas to prasītu, piemēram, 3. stundas piemērs $4x^{2}-8x-5$ (vidējā locekļa sadalīšana grupēšanai), kas pašlaik atzīmēts tikai ar frāzi „tas nav obligāti jāapgūst". **Ieteikums:** vai nu konsekventi lietot deklarēto konvenciju, vai precizēt „Materiālu apraksta" tekstu.

**3.3 🟠 Diagnosticējošais darbs ir ieteikts, bet nav nodrošināts.** Metodiskajā komentārā ieteikts noskaidrot skolēnu pamatskolas prasmju līmeni („ieteicams diagnosticējošais darbs"), taču materiālu komplektā šāda darba nav un stundu plānā tam nav paredzēts laiks. **Ieteikums:** pievienot gatavu diagnosticējošo darbu (vai atsauci uz esošu, piem., Skola2030) un norādi, kurā stundā / kā to organizēt (piem., 1. stundas daļa vai atsevišķa 0. stunda pārejas periodā).

**3.4 🟡 13. stundai nav darba lapas, un uzdevumu formulējums neatbilst stundas SR.** Temata plānojuma tabulā 13. stundai nav norādīts materiāls; stundas beigās dotie uzdevumi formulēti „Atrisini vienādojumu, **lietojot grafisko metodi**!", lai gan stundas SR ir „…lietojot **funkciju īpašības un spriežot**". **Ieteikums:** (a) izveidot atsevišķu darba lapu vai skaidru norādi, ka izmanto dokumentā iekļautos uzdevumus; (b) saskaņot uzdevumu formulējumu ar stundas SR (piem., „lietojot grafisko paņēmienu un/vai funkciju īpašības, pamato sakņu skaitu").

**3.5 🟡 Netiek izmantoti pieejamie materiālu varianti un eksāmenu uzdevumu fails.** Projektā ir faili `OL_1_dl_9_substitucija_UZD_ar_tuksumiem`, `OL_1_dl_11_dazadi_vienad_UZD_ar_tuks` (atbalsta/diferenciācijas varianti) un `OL_1_eksamena_UZD` (eksāmenu uzdevumi), bet metodiskajā materiālā uz tiem nav nevienas atsauces. **Ieteikums:** pieminēt „ar tukšumiem" variantus pie 10.–11. un 14. stundas kā atbalstu skolēniem, kam grūti sākt, un iekļaut atsauci uz eksāmena uzdevumiem 15. stundā (kopsavilkums) vai sadaļā „Literatūra un avoti" — tas stiprina saikni ar valsts pārbaudes darbu formātu.

**3.7 🟡 Digitālo rīku akcents tematā ir vājš.** Programmas deklarētais akcents „Digitālo rīku efektīva izmantošana" tematā parādās tikai netieši (Photomath ekrānuzņēmums 3. stundā; „pārbaudei var izmantot tehnoloģijas"). **Ieteikums:** 12.–13. stundā pievienot konkrētas norādes darbam ar GeoGebra/Desmos (grafiku zīmēšana, krustpunktu precizitātes diskusija — tas dabiski atbalsta piezīmi „no grafika nevar atšķirt 2 un 2,03"), kā arī CAS rīku pieminēt sadalīšanas pareizības pārbaudei. Photomath atsauci formulēt neitrālāk („dažas lietotnes, piemēram, …"), jo konkrēta komerciāla rīka izcelšana ātri noveco.

**3.8 🟡 Literatūras saraksta aktualitāte un pieejamība.** No 13 avotiem 11 ir izdoti 1995.–2012. gadā. **Ieteikums:** pārbaudīt, vai norādītās grāmatas skolām reāli ir pieejamas; kur iespējams, papildināt ar aktuāliem digitāliem avotiem (mape.gov.lv atsauces jau ir labs sākums).

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts |
|---|---|---|---|
| 4.1 | 1. stunda, ievads par izteiksmēm | „Ir skaitliskas **izteiktas**, algebriskas izteiksmes …" | „Ir skaitliskas **izteiksmes**, algebriskas izteiksmes …" |
| 4.2 | 1. stunda | „Aplūkojot dažādas situācijas rodas nepieciešamība …" | „Aplūkojot dažādas situācijas**,** rodas nepieciešamība …" |
| 4.3 | 1. stunda, 2. situācija | „… nobrauca ar ātrumu $a$ km/h" (trūkst pieturzīmes teikuma beigās) | „… nobrauca ar ātrumu $a$ km/h**.**" |
| 4.4 | 6. stunda | „Viena mainīgā otrās pakāpes polinomu **sauca** par kvadrāttrinomu." | „… **sauc** par kvadrāttrinomu." |
| 4.5 | 10.–11. stunda (atsauce uz Skola2030 materiālu) | „… materiālu, kurā **aprakstīt** algoritms …" | „… kurā **aprakstīts** algoritms …" |
| 4.6 | 10.–11. stunda, jautājumi skolēniem | „Vai to **par** prognozēt?" | „Vai to **var** prognozēt?" |
| 4.7 | 12. stunda, pamatojums | „… tad viena **funkcijas** ir augoša un otra ir dilstoša." | „… tad viena **funkcija** ir augoša …" |
| 4.8 | 12. stunda, piezīme par krustpunktiem | „divos punktos, tad **vienādojuma** ir divi atrisinājumi" | „… tad **vienādojumam** ir divi atrisinājumi" |
| 4.9 | 13. stunda, intervālu analīze | „… funkcijas $y=x^{2}-2x+1$ ir intervālā $[0;1)$ …" | „… funkcijas $y=x^{2}-2x+1$ **vērtības** ir intervālā $[0;1)$ …" |
| 4.10 | 4., 7.–8. stunda (Skola2030 atsauces, 3 vietas) | „Kā izmanto izteiksmju sadalīšanu **reizinājos**?" | Pārbaudīt pret oriģinālā materiāla nosaukumu; ja tur ir „reizinātājos", labot citātu |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Tipisko kļūdu akcentēšana.** Programmas princips paredz akcentēt „jautājumus, kuros skolēni raksturīgi kļūdās". Tematā tas daļēji darīts (piem., maldīgais priekšstats par daļveida izteiksmēm 1. stundā — ļoti labs piemērs). Ieteicams līdzīgus „tipisko kļūdu" blokus pievienot arī: zīmju kļūdas, lietojot kvadrāttrinoma formulu $a(x-x_1)(x-x_2)$ (koeficienta $a$ aizmiršana — tekstā jau pieminēts, var izcelt vizuāli); 
$\sqrt{x^2}= \lvert x \rvert$ tipa kļūdas; saknes „pazaudēšana", dalot vienādojumu ar $x$ (9. stundā piemērs $x^3=4x$ to netieši parāda — vērts pateikt tieši).

**5.2 Vēl viena „izpratnes" saruna 2. stundā.** Pie grafiskās metodes trīs piemēriem ($D>0$, $D=0$, $D<0$ situācijas) ieteicams pievienot jautājumu par saistību starp diskriminantu, sakņu skaitu un grafika novietojumu — tas sagatavo 6. stundas secinājumus par $D$ un sadalīšanu reizinātājos un atbilst programmas akcentam „sakarību saskatīšana".

**5.3 Saskaņot 15. stundas aprakstu ar failu komplektu.** Kopsavilkuma stundai norādīts tikai `OL_1_kopsavilkums`; ja paredzēts izmantot arī eksāmenu uzdevumus (sk. 3.5), to skaidri pateikt.

---

### Kopsavilkums

Dokuments kopumā ir metodiski spēcīgs (labi sarunu scenāriji, vairāki risinājumu veidi, pārbaudes ieraduma veidošana), taču **pirms publiskošanas obligāti jānovērš 1. sadaļas 10 matemātiskie labojumi** (īpaši 1.1, 1.2, 1.8 — kļūdas vispārīgajās formulās un paraugrisinājumā, ko skolotāji var pārnest uz tāfeles) un 2.1–2.2 terminoloģijas kļūdas. Ieteicams arī pievienot M.O. kodu izsekojamību (3.1) un izpildīt paša dokumenta deklarētās konvencijas (3.2, 3.6).
