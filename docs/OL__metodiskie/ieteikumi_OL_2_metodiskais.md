---
layout: default
title: "Ieteikumi par 2. tematu"
permalink: /OL__metodiskie/ieteikumi_OL_2_metodiskais/
---

# Labojumu un ieteikumu saraksts — „OL_2. Algebriskas daļas" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_2__algebriskas_dalas_metodiskais.md` (14 stundas).
**Salīdzināšanas avoti:** programmas paraugs (`MATEMATIKA_1_programmas_paraugs_19_maijs.md`), matemātikas mācību jomas standarts (VSK), projektā pieejamie `OL_2_*` faili (formatīvās vērtēšanas darbi, kopsavilkums, NPD kritēriji, eksāmena uzdevumi) un salīdzinājumam — 1. temata metodiskais materiāls.
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).

*Piezīmes.* Konvertācijas artefakti (lappušu pārtraukumu zīmes `**\**`, `{.mark}` marķējums, formulu paplašināšanas atzīmes u. tml.) nav uzskatīti par kļūdām un sarakstā nav iekļauti. 5.–6. stundas piemēru risinājumi, kas dokumentā ievietoti kā attēli (`media/image1–8`), šajā pārskatā nebija pārbaudāmi — tos ieteicams pārbaudīt atsevišķi (skat. arī 5.2).

---

## 1. Matemātiski labojumi 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 1. stunda, piemērs par izteiksmes $\frac{x-2}{x^{2}+1}$ vērtību aprēķinu | Ja $x = 2$, tad $\frac{2-2}{0+1} = \frac{0}{1} = 1$. | Ja $x = 2$, tad $\frac{2-2}{4+1} = \frac{0}{5} = 0$. | Divas kļūdas vienā rindā: saucējā jābūt $2^{2}+1=5$ (nevis $0+1$), un rezultāts ir $0$, nevis $1$ (arī pierakstītais $\frac{0}{1}$ nav vienāds ar $1$). Pārējie vērtību aprēķini ($x=1$; $x=-1$) ir pareizi. |
| 1.2 | 1. stunda, vērtību tabula izteiksmei $\frac{x-2}{x^{2}+1}$ | Pie $x = 2$ tabulā norādīta vērtība $1$. | Pie $x = 2$ vērtība ir $0$. | Kļūda izriet no 1.1 un jālabo abās vietās saskaņoti. Pārējās tabulas vērtības ($-\frac{1}{2}$; $-1\frac{1}{2}$; $-\frac{4}{5}$) ir pareizas. |
| 1.3 | 7.–9. stunda, sadaļa „Saskaiti daļas!", 1. piemērs | $\frac{13}{24} + \frac{3}{24} = \frac{13+3}{24} = \frac{16}{24} = \frac{3}{8}$ | $\frac{13}{24} + \frac{3}{24} = \frac{13+3}{24} = \frac{16}{24} = \frac{2}{3}$ | Saīsinot $\frac{16}{24}$ ar $8$, iegūst $\frac{2}{3}$; rezultāts $\frac{3}{8}$ ir kļūdains (izskatās pēc apmainīta skaitītāja un saucēja). Kļūda īpaši pamanāma, jo piemērs demonstrē pamatprasmi, uz kuras balstīta analoģija ar algebriskām daļām. |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | 2. stunda, identiski vienādu izteiksmju definīcija | „Algebriskas izteiksmes sauc par identiski vienādām, ja ar jebkurām mainīgo vērtībām šo izteiksmju atbilstošās vērtības ir vienādas." | „... ja ar visām pieļaujamām (izteiksmju definīcijas kopai piederīgām) mainīgo vērtībām šo izteiksmju atbilstošās vērtības ir vienādas." | Daļveida izteiksmēm precizējums ir būtisks: piemēram, $\frac{x^{2}}{x}$ un $x$ definīcijas kopas ietvaros ir identiski vienādas, lai gan pie $x=0$ pirmā nav definēta. Bez precizējuma definīcija nonāk pretrunā ar visu turpmāko daļu saīsināšanas praksi. |
| 2.2 | 2. stunda, ievads pirms zīmju maiņas likuma | „Lai daļveida racionālai izteiksmei iegūtu tai pretējo izteiksmi, jāievēro likums par zīmju maiņu." (seko likums „Daļas vērtība nemainās, ja divās vietās maina zīmi...") | Pārformulēt ievadu, skaidri nošķirot abus gadījumus, piem.: „Zīmju maiņa daļā: mainot zīmi vienā vietā (skaitītājam, saucējam vai daļas priekšā), iegūst dotajai daļai pretēju izteiksmi; mainot zīmi divās vietās, iegūst dotajai daļai identiski vienādu izteiksmi (daļas vērtība nemainās)." | Loģiska neatbilstība: ievadteikums sola pretējās izteiksmes iegūšanu, bet tam sekojošais likums apraksta vērtības nemainīšanos (identiski vienādu daļu). |
| 2.3 | Turpat | „daļveida racionālai izteiksmei" | „algebriskai daļai" | Termins „daļveida racionāla izteiksme" dokumentā parādās tikai šajā vietā un iepriekš nav ieviests; jāvieno ar pārējā tekstā (un programmas paraugā) lietoto terminoloģiju. Skat. arī 5.1 par algebriskas daļas definīcijas iekļaušanu. |
| 2.4 | 3.–4. stunda, daļu paplašināšana | „Jebkuru algebrisku daļu var paplašināt, tās skaitītāju un saucēju reizinot ar vienu un to pašu izteiksmi (jebkuru nenulles skaitli vai polinomu)." | „... ar vienu un to pašu izteiksmi — nenulles skaitli vai polinomu, kas nav identiski vienāds ar nulli." | Precizitāte: polinoms atsevišķām mainīgā vērtībām var pieņemt vērtību $0$; formāli pietiek prasīt, lai tas nebūtu nulles polinoms, jo (kā dokumentā pamatoti norādīts citviet) pārveidojumus veic, ievērojot izteiksmes definīcijas kopu. Šo piebildi var atkārtot arī šeit. |
| 2.5 | 5.–6. stunda, daļu reizināšanas likums | „Ja $\frac{A}{B}$ un $\frac{C}{D}$ ir algebriskas daļas, kur $A$, $B \neq 0$, $C$ un $D \neq 0$ ir polinomi, tad ..." | „... kur $A$, $B$, $C$ un $D$ ir polinomi un $B \neq 0$, $D \neq 0$, tad ..." | Pašreizējais pieraksts ir grūti lasāms un divdomīgs (nosacījumi $\neq 0$ sajaukti ar uzskaitījumu). Ieteicams arī vienot ar 2.4 („nav identiski vienāds ar nulli"). |
| 2.6 | 3.–4. stunda, saīsināšanas skaidrojums | „Lai saīsinātu algebrisku daļu, kuras skaitītājā vai saucējā ir monoms, ir jāatrod kopīgie reizinātāji." | „Lai saīsinātu algebrisku daļu, kuras skaitītājs un saucējs ir monomi, ..." | Saiklis „vai" rada pārpratumu: ja monoms ir tikai vienā no tiem, otrs (polinoms) tik un tā jāsadala reizinātājos. Piemērs a) atbilst tieši gadījumam „monomi abās vietās", un teikums simetriski sasaucas ar nākamo („ja tās skaitītājā un saucējā ir polinoms"). |
| 2.7 | 5.–6. stunda, dalīšanas 3. piemērs $\frac{x^{2}-6x+9}{6x} : (x^{2}-9)$ | „Dalot daļas, pirmo daļu reizina ar otrās daļas apgriezto daļu." | Papildināt, piem.: „Dalītājs šeit ir polinoms, ko var uzlūkot kā daļu $x^{2}-9 = \frac{x^{2}-9}{1}$; tās apgrieztā daļa ir $\frac{1}{x^{2}-9}$." | Piemērā dalītājs nav daļa, tāpēc bez šī starpsoļa formulējums „otrās daļas apgrieztā daļa" skolēnam var būt neskaidrs (tieši šis pārejas solis ir tipiska kļūdu vieta). |
| 2.8 | 1. stunda, piezīme pirms kopu starpības pieraksta | „... var skolēniem rādīt intervālu pierakstu, izmantojot kopu starpību." | „... var skolēniem rādīt definīcijas kopas pierakstu, izmantojot kopu starpību." | $\mathbb{R}\backslash\{3\}$ nav intervālu pieraksts — tieši otrādi, tas piedāvāts kā alternatīva intervālu apvienojumam. |
| 2.9 | 5.–6. stunda, piezīme par pierakstu reizinot | „... kopīgos reizinātājus skaitītājā un saucējā var saīsināt tikai tad, ja tie ir vienas un tās pašas daļas skaitītājā un saucējā ..." | Formulēt kā pieraksta vienošanos, nevis matemātisku aizliegumu, piem.: „Vienojamies vispirms uzrakstīt vienu daļu, kuras skaitītājā ir abu skaitītāju reizinājums un saucējā — abu saucēju reizinājums, un tikai tad saīsināt." | Matemātiski „šķērssaīsināšana" daļu reizinājumā ir korekta (reizinājums ir viena daļa); pašreizējais kategoriskais formulējums var nonākt pretrunā ar citos avotos redzamiem pareiziem risinājumiem. Didaktiskā prasība pēc vienota pieraksta ir pamatota — to tikai jāpasniedz kā vienošanos. |
| 2.10 | 2. stunda, pretējo izteiksmju definīcija | „Divas izteiksmes sauc par pretējām izteiksmēm, ja to summa ir 0." | „... ja to summa ir identiski vienāda ar nulli." | Saskaņā ar 2.1: izteiksmju (ne skaitļu) gadījumā vienādībai jābūt spēkā ar visām pieļaujamām mainīgo vērtībām. |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 Stundu skaits neatbilst programmas paraugam.** Metodiskajā materiālā tematam atvēlētas **14 stundas**, bet programmas paraugā tematam „Algebriskas daļas" paredzētas **17 stundas** (1. temata metodiskais materiāls programmas paraugam atbilst — 17 stundas). Ieteicams vai nu saskaņot stundu skaitu un plānojumu ar programmas paraugu, vai metodiskajā komentārā īsi pamatot atšķirību (piemēram, atlikušās stundas paredzētas diferenciācijai, nostiprināšanai vai temata padziļinājumam).

**3.2 🟠 Plānojuma tabulas un stundu aprakstu formulējumi nesakrīt.** Raksturīgākās vietas: a) plānojumā 2. stundas temats ir „Izteiksmes identiskie pārveidojumi un zīmju maiņa algebriskajā daļā", bet stundas virsrakstā — „Identiskas izteiksmes un zīmju maiņa algebriskā daļā"; b) plānojumā 10.–11. stundas SR ir „Izpilda darbības ar algebriskām daļām", bet stundas aprakstā — „Veic visas darbības (saskaitīšanu, atņemšanu, reizināšanu un dalīšanu) ar algebriskām daļām" (programmas paraugā — „Veic darbības ar algebriskām daļām"); c) tekstā mijas noteiktā un nenoteiktā galotne: „algebriskas daļas / algebriskās daļas", „algebriskā daļā / algebriskajā daļā". Ieteikums: vienot formulējumus, par pamatu ņemot programmas paraugu.

**3.3 🟠 Nav atspoguļots programmas SR par izteiksmes vērtības aprēķināšanu pēc pārveidojumiem.** Programmas paraugā sadaļā „Darbības ar algebriskām daļām" ir SR „Aprēķina izteiksmes skaitlisko vērtību noteiktai mainīgā skaitliskajai vērtībai, vispirms veicot algebriskus pārveidojumus" ar skaidrojumu „tai skaitā arī pierāda, ka izteiksmes vērtība nav atkarīga no mainīgā vērtības". Temata plānojumā un stundu aprakstos šāds SR neparādās (kopsavilkuma 2. uzdevums vērtību aprēķina bez iepriekšējas vienkāršošanas, tātad to sedz tikai daļēji). Ieteicams šo SR iekļaut 10.–11. stundā vai kopsavilkumā, pievienojot atbilstošus piemērus.

**3.4 🟡 1. stundas nosaukums neatspoguļo saturu.** Stundas temats „Algebriskas izteiksmes" ir plašāks par stundas faktisko saturu (daļveida izteiksmes vērtība un definīcijas kopa); turklāt algebriskas izteiksmes vispārīgi jau aplūkotas 1. tematā. Precīzāks nosaukums būtu, piemēram, „Daļveida izteiksmes un to definīcijas kopa".

**3.5 🟡 Piezīme par definīcijas kopas nerakstīšanu atkārtojas piecas reizes.** Teikums „Veicot algebrisko daļu pārveidojumus, tiek uzskatīts, ka visi pārveidojumi tiek veikti, ievērojot izteiksmes definīcijas kopu, tāpēc definīcijas kopu neraksta" burtiski atkārtojas 3.–4., 5.–6. (divreiz) un 7.–9. stundā (divreiz). Apsvērt to vienreiz izcelt (piemēram, rāmī pie pirmās lietošanas reizes) un tālāk lietot īsu atgādni/atsauci.

**3.6 🟡 Dublēta piezīme par saīsināšanas neizdevīgumu.** Piezīme par to, ka daļu $\frac{2(x-1)}{2(x+2)}$ nav izdevīgi saīsināt, gandrīz burtiski atkārtojas 3.–4. stundā un 7.–9. stundas 1. uzdevuma atrisinājumā. Ja atkārtojums nav apzināts didaktisks paņēmiens, otrajā vietā pietiek ar atsauci.

**3.7 🟡 Materiālu aprakstā solītais „Nav standarta SR" marķējums dokumentā nav sastopams.** Aprakstā teikts, ka saturs, kas pārsniedz standarta SR, ir pelēkā rāmī ar norādi „Nav standarta SR", taču tekstā šāds fragments nav atrodams. Ja kopu starpības pieraksts ($\mathbb{R}\backslash\{3\}$) 1. stundā ir domāts kā padziļinājums, to ieteicams noformēt atbilstoši aprakstam; ja padziļinājuma satura tematā nav, teikumu materiālu aprakstā var dzēst.

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 4.1 | Metodiskais komentārs | „darbības ar algebriskā daļām" | „darbības ar algebriskajām daļām" | Galotnes kļūda. |
| 4.2 | Metodiskais komentārs | „... būs nepieciešamas nākamajos tematos, piemēram, daļveida vienādojumi un daļveida nevienādības." | „... būs nepieciešamas nākamajos tematos, piemēram, tematos „Daļveida vienādojumi" un „Daļveida nevienādības"." | Locījumu saskaņa; tematu nosaukumus ieteicams likt pēdiņās. |
| 4.3 | Materiālu apraksts | „īpaši tiem, skolēniem, kas plāno studēt STEM jomā" | „īpaši tiem skolēniem, kuri plāno studēt STEM jomā" | Lieks komats. |
| 4.4 | 1. stunda (divu mainīgo piemērs) | „visi reāli skaitļu pāri" | „visi reālu skaitļu pāri" | Locījums. |
| 4.5 | 1. stunda (kopu starpības piemērs) | „izņemot skaitļu $-7$ un 5" | „izņemot skaitļus $-7$ un $5$" | Locījums. |
| 4.6 | 2. stunda | „ir gūts priekštats par identiskām skaitliskām izteiksmēm" | „ir gūts priekšstats ..." | Pareizrakstība. |
| 4.7 | 3.–4. stunda | „lai varēti daļas saskaitīt vai atņemt" | „lai varētu daļas saskaitīt vai atņemt" | Pareizrakstība. |
| 4.8 | 3.–4., 5.–6., 7.–9. stunda (5 vietās) | „tiek uzskatīts, ka visi pārveidojumu tiek veikti" | „tiek uzskatīts, ka visi pārveidojumi tiek veikti" | Locījuma kļūda atkārtojas visās piecās vietās (skat. arī 3.5). |
| 4.9 | 7.–9. stunda, 1. saskaitīšanas piemērs | „Lai saskatītu šīs daļas, kurām saucēji ir vienādi, saskaita šo daļu skaitītājus un saucēju nemaina." | „Lai saskaitītu daļas, kurām saucēji ir vienādi, saskaita šo daļu skaitītājus un saucēju nemaina." | Pārrakstīšanās („saskatītu" → „saskaitītu") sagroza teikuma jēgu. |
| 4.10 | 7.–9. stunda | „lai daļām, kuras saskaita vai atņem būtu vienādi saucēji" | „lai daļām, kuras saskaita vai atņem, būtu vienādi saucēji" | Trūkst komata aiz palīgteikuma. |
| 4.11 | 7.–9. stunda, 2. uzdevuma atrisinājums | „var veikt daļu atņemšanu, t.i. atņemt" | „... t. i., atņemt" | Saīsinājumu rakstība; vienot arī „t.sk." → „t. sk." visā dokumentā. |
| 4.12 | 7.–9. stunda, atņemšanas 3. piemēra komentārs | „Atņemot daļu skaitītājus, ir jāatņem visi skaitītāja locekļi" | „Atņemot daļas, jāatņem viss otrās daļas skaitītājs (visi tā locekļi)" | Precīzāks formulējums — runa ir tieši par atņemamās daļas skaitītāju. |
| 4.13 | Literatūras 3. ieraksts | „D. Kriķis „Matemātiska 10. klasei Skolotāja grāmata"" | „D. Kriķis „Matemātika 10. klasei. Skolotāja grāmata"" | Pareizrakstība nosaukumā. |
| 4.14 | Literatūras 4. ieraksts | „Uzdevumi.lv 5. tematu Daļveida funkcija un algebriskas daļas" | „Uzdevumi.lv 5. temats „Daļveida funkcija un algebriskas daļas"" | Locījums; nosaukums pēdiņās. |
| 4.15 | Literatūras 8.–9. ieraksts | „E. Slokenberga, Inga France, Ilze France" | Vienot autoru pierakstu ar pārējiem ierakstiem | Ja pilnie vārdi lietoti, lai atšķirtu Ingu un Ilzi Franci, tad tos pašus principus vajadzētu piemērot arī 1. ierakstam („I. France" tur ir divdomīgs). |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Pievienot algebriskas daļas definīciju.** Termins „algebriskā daļa" ir temata nosaukumā un programmas parauga jēdzienu sarakstā, taču dokumentā tas nekur netiek definēts — netieša definīcija parādās tikai reizināšanas likuma pierakstā (5.–6. stundā). Ieteicams 1. vai 2. stundā iekļaut skaidru definīciju (piemēram: algebriska daļa ir izteiksme $\frac{A}{B}$, kur $A$ un $B$ ir polinomi un saucējs $B$ satur mainīgo) un īsi paskaidrot tās saistību ar jēdzienu „daļveida izteiksme".

**5.2 Attēlos ievietotos risinājumus aizstāt ar formulu pierakstu.** 5.–6. stundas piemēru risinājumi ir ievietoti kā attēli (`media/image1–8`), kamēr pārējā dokumentā risinājumi ir formulu tekstā. Vienots pieraksts atvieglo labošanu, nodrošina konsekventu izskatu un pieejamību (ekrānlasītāji); pašreizējie attēlu alternatīvie teksti ir automātiski ģenerēti („Apraksts ģenerēts automātiski") un saturiski neko nepasaka. Ja attēlus saglabā, tie matemātiski jāpārbauda atsevišķi un jāpievieno jēgpilni alt-teksti.

**5.3 Pievienot norādi uz eksāmena uzdevumu apkopojumu.** Projektā ir temata eksāmena uzdevumu fails (`OL_2_eksamena_UZD`), taču metodiskajā materiālā tas nav pieminēts. Ieteicams kopsavilkuma stundā vai materiālu aprakstā pievienot norādi uz valsts pārbaudes darbu uzdevumu apkopojumu — tas labi atbilst programmas akcentam par gatavošanos noslēguma vērtēšanai.

**5.4 SR formulējumos lietot darbības vārdus un programmas parauga redakciju.** Piemēram, „Zina, kas ir identiskas izteiksmes" aizstāt ar „Skaidro, kas ir identiskas izteiksmes" (novērojama darbība; sasaucas ar programmas „Skaidro matemātisku izteiksmju identiskos pārveidojumus"), bet „Uzraksta daļveida izteiksmes definīcijas kopu" tuvināt programmas formulējumam „Nosaka algebriskās daļas definīcijas kopu".

**5.5 Nostiprināt saikni ar 1. temata jēdzieniem.** 1. stundā pie piemēra $\frac{a+2}{3}$ ieteicams tieši nosaukt, ka tā ir **vesela** algebriska izteiksme, jo saucējā nav mainīgā (programmas paraugā ir tieši šāds piemērs: izteiksmes $\frac{x+2}{3}$ koeficienti ir daļskaitļi, bet tā nav daļveida izteiksme). Tas palīdz novērst tipisku maldīgu priekšstatu „ja ir daļsvītra, tad ir daļveida izteiksme".

---

### Kopsavilkums

Dokuments kopumā ir loģiski strukturēts, konsekventi izmanto pēctecību no pamatskolas (analoģija starp parastajām un algebriskajām daļām) un labi sasaucas ar programmas parauga akcentiem; risinājumu soļi ir izvērsti un skolotājam viegli izmantojami.
Pirms publiskošanas obligāti jānovērš trīs matemātiskās kļūdas (1. sadaļa — izteiksmes vērtības aprēķins un tabula 1. stundā, daļu summas saīsināšana 7.–9. stundā), kā arī jāatrisina stundu skaita neatbilstība programmas paraugam (3.1) un jāizlabo loģiskā neatbilstība zīmju maiņas ievadā (2.2).
Ieteicams arī vienot SR un tematu formulējumus ar programmas paraugu, pievienot algebriskas daļas definīciju, atsevišķi pārbaudīt attēlos ievietotos risinājumus un veikt pilnu teksta korektūru (4. sadaļā uzskaitītas raksturīgākās, bet ne obligāti visas valodas kļūdas).
