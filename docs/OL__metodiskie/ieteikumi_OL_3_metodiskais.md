---
layout: default
title: "Ieteikumi par 3. tematu"
permalink: /OL__metodiskie/ieteikumi_OL_3_metodiskais/
---

# Labojumu un ieteikumu saraksts — „OL_3. Daļveida vienādojumi" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_3__Dalveida_vienad_metodiskais.md` (18 stundas).
**Salīdzināšanas avoti:** programmas paraugs (`MATEMATIKA_1_programmas_paraugs_19_maijs.md`, 3. temats — 18 stundas), projektā pieejamie darba lapu un vērtēšanas darbu faili (`OL_3_dl_1` … `OL_3_dl_7`, `OL_3_fvd_1`, `OL_3_fvd_2`, `OL_3_npd`, `OL_3_kopsavilkums`).
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).

---

## 1. Matemātiski labojumi un kritiskas pretrunas 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 5.–7. stunda, uzdevumu tabula (1. vienādojums) | $\frac{4}{x + 1} - \frac{x + 1}{x - 1} = \frac{x^{2} - 3}{x^{2} - 1}$ | $\frac{x + 1}{x - 1} - \frac{4}{x + 1} = \frac{x^{2} - 3}{x^{2} - 1}$ | Uzdevuma formulējums nesakrīt ar atrisinājumu — atrisinājuma tabulā risināts vienādojums ar apmainītiem locekļiem. Uzdevumā dotajā formā vienādojums noved pie $x^{2} - x + 1 = 0$ ($D < 0$), t. i., tam **nav reālu sakņu**, un atbilde $x = 4$ neder. Jālabo uzdevuma pieraksts (vai atbilstoši jāpārstrādā atrisinājums). |
| 1.2 | 5.–7. stunda, substitūcijas ievadpiemērs $\left( \frac{x + 1}{x} \right)^{2} - 6\left( \frac{x + 1}{x} \right) - 27 = 0$ | $t_{1} = -3;\ \ t_{2} = 6$ | $t_{1} = -3;\ \ t_{2} = 9$ | Vienādojuma $t^{2} - 6t - 27 = 0$ saknes ir $-3$ un $9$ (summa $6$, reizinājums $-27$); vērtība $t = 6$ nav sakne ($36 - 36 - 27 \neq 0$). |
| 1.3 | Turpat, tālākie soļi | $\frac{x + 1}{x} = 6$; $\ x + 1 = 6x$; $\ -5x = -1$; $\ x_{2} = \frac{1}{5}$ | $\frac{x + 1}{x} = 9$; $\ x + 1 = 9x$; $\ -8x = -1$; $\ x_{2} = \frac{1}{8}$ | Seko no 1.2 labojuma. Pārbaude: $\frac{1/8 + 1}{1/8} = 9$ un $9^{2} - 6 \cdot 9 - 27 = 0$. (Sakne $x_{1} = -\frac{1}{4}$ ir pareiza.) |
| 1.4 | 2. stunda, kopīgi risināmo piemēru tabula, 4. piemērs $\frac{x(2x - 8)}{3x + 12} = 0$ | Risinājums beidzas ar $2x = 8$; $\ x = 4$ | Papildināt ar noslēdzošu rindu: $x_{1} = 0;\ \ x_{2} = 4$ (abas vērtības pieder definīcijas kopai) | Atšķirībā no pārējiem piemēriem, kur pēdējā rinda ir galīgā atbilde, šeit pieraksts beidzas ar $x = 4$ un rada iespaidu, ka sakne ir tikai viena. Arī $x = 0$ ir vienādojuma sakne, un tā jāiekļauj atbildē. |
| 1.5 | 8.–10. stunda, teksts pēc kustības parauguzdevuma | „Risina uzdevumus par kustību (skat. **OL_3_dl_4**)" | „… (skat. **OL_3_dl_5**)" | Pretruna ar temata plānojumu (*5. darba lapa*) un failu nosaukumiem: `OL_3_dl_4` ir substitūcijas darba lapa, kustības uzdevumi ir `OL_3_dl_5_Kustiba`. |
| 1.6 | 11.–12. stunda, teksts pēc celtnieku parauguzdevuma | „Risina uzdevumus par kopīgo darbu (skat. **OL_3_dl_5**)" | „… (skat. **OL_3_dl_6**)" | Pretruna ar plānojumu (*6. darba lapa*): kopīgā darba uzdevumi ir failā `OL_3_dl_6_Kopigais_darbs`. |
| 1.7 | 13.–14. stunda, teksts pēc Kārļa parauguzdevuma | „Risina uzdevumus par plānoto un esošo (skat. **OL_3_dl_6**)" | „… (skat. **OL_3_dl_7**)" | Pretruna ar plānojumu (*7. darba lapa*): plānotā un esošā uzdevumi ir failā `OL_3_dl_7_Plan_un_esosais`. Atsauces 1.5–1.7 sistemātiski nobīdītas par vienu numuru — ieteicams pārbaudīt visas atsauces vēlreiz pēc labošanas. |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | 1. stunda, atbilde uz jautājumu „Ko nozīmē atrisināt vienādojumu?" | „Atrisināt vienādojumu nozīmē atrast visas tā saknes un pierādīt, ka vienādojumam citu sakņu nav." | „… atrast visas tā saknes un pamatot, ka citu sakņu nav, **vai pierādīt, ka vienādojumam sakņu nav**." | Pašreizējais formulējums neaptver gadījumu, kad sakņu nav vispār (šāds gadījums tematā parādās, piem., 2. stundas 5. piemērā, kur $x \in \varnothing$). |
| 2.2 | 1. stunda, atbilde uz jautājumu „Kas ir vienādojums?" | „Par algebrisku vienādojumu sauc jebkuru divu algebrisku izteiksmju vienādību." | Ieteikums: „Vienādību, kas satur mainīgo (nezināmo), sauc par vienādojumu; ja abās pusēs ir algebriskas izteiksmes, to sauc par algebrisku vienādojumu." | Bez mainīgā pieminēšanas definīcijai formāli atbilst arī skaitliska vienādība (piem., $2 + 3 = 5$). Turklāt jautājums ir par vienādojumu vispār, bet atbilde definē tikai algebrisku vienādojumu — vēlams tos saskaņot. |
| 2.3 | 8.–10. stunda (kustība), 11.–12. stunda (kopīgais darbs), 13.–14. stunda (plānotais/esošais, I veids) | „Abas vienādojuma puses reizina ar $6x(x - 3) > 0$, jo $x$ ir ātrums, kas ir pozitīvs lielums" (analoģiski „$x(x - 5) > 0$, jo $x$ ir dienas…", „$x(x - 1) > 0$, jo $x$ ir lappušu skaits…") | Precizēt pamatojumu, piem.: „…jo pēc uzdevuma jēgas $x > 3$ (abu braucēju ātrumi ir pozitīvi)"; attiecīgi $x > 5$ un $x > 1$ pārējos uzdevumos | No $x > 0$ vien neizriet, ka $x - 3 > 0$ (resp. $x - 5 > 0$, $x - 1 > 0$). Pozitivitāte izriet no tā, ka arī **otra** objekta lielums (ātrums, dienu vai lappušu skaits) ir pozitīvs. II veida piemērā ($y(y + 10) > 0$) pamatojums ir korekts un labojums nav vajadzīgs. |
| 2.4 | 2. stunda („Var formulēt spriedumu, ja $\frac{f(x)}{g(x)} = 0$, tad $f(x) = 0$ un $g(x) \neq 0$") un 3.–4. stunda / 5.–7. stunda („daļas ar vienādiem no nulles atšķirīgiem saucējiem ir vienādas, ja ir vienādi to skaitītāji") | Formulējumi tikai vienā virzienā („ja …, tad …") | Formulēt kā ekvivalenci: „$\frac{f(x)}{g(x)} = 0$ **tad un tikai tad**, ja $f(x) = 0$ un $g(x) \neq 0$"; „daļas ar vienādiem, no nulles atšķirīgiem saucējiem ir vienādas **tad un tikai tad**, ja vienādi to skaitītāji" | Risinot vienādojumu, faktiski tiek lietots pretējais virziens (no daļu vienādības secina skaitītāju vienādību), tāpēc pāreja jāpamato kā ekvivalents pārveidojums — tas atbilst arī programmas parauga akcentam par ekvivalentiem pārveidojumiem. |
| 2.5 | 2. stundas piemēru tabula | 1. piemērā lietots saīsinājums „$D.k.$", 2. piemērā — „$D.a.$" | Vienot apzīmējumu (ieteicams „D.k." — definīcijas kopa, kā pārējā dokumentā) | Divi dažādi saīsinājumi vienā tabulā vienam un tam pašam jēdzienam var mulsināt; pirmajā lietojumā saīsinājumu vēlams atšifrēt. |
| 2.6 | Temata plānojums (3.–4. stunda) un 3.–4. stundas teksts | Plānojumā $\frac{f(x)}{g(x)} = \frac{h(x)}{p(x)}$, tekstā $f(x) : g(x) = h(x) : r(x)$ | Vienot funkciju apzīmējumus (visur $p(x)$ vai visur $r(x)$) | Konsekvences jautājums; skolēni/skolotāji materiālu lasa kopā ar plānojumu. |
| 2.7 | Attēli (substitūcijas shēma `image1.png`, kustības formulas trijstūris `image2.png`) | Alternatīvie teksti ir automātiski ģenerēti: „Attēls, kurā ir teksts… Mākslīgā intelekta ģenerēts saturs var būt nepareizs." un otram attēlam — **krievu valodā** („Изображение выглядит как линия, треугольник…") | Aizstāt ar jēgpilniem alternatīvajiem tekstiem latviešu valodā (piem., „Substitūcijas metodes soļu shēma", „Ceļa, ātruma un laika sakarības trijstūris $s = v \cdot t$") | Automātiskie alt teksti (īpaši krievu valodā un ar MI atrunu) publiskā valsts mācību materiālā nav pieļaujami; korekti alt teksti nepieciešami arī piekļūstamībai. |
| 2.8 | 1. stunda, padziļinājuma jautājums „Cik sakņu varētu būt daļveida vienādojumam?" | „Jebkāds nenegatīvs vesels skaitlis, t. i., $0;1;2;3;\ldots$ Piemēram, $\frac{(x - x_{1})(x - x_{2})\ldots(x - x_{n})}{x} = 0$." | Papildināt: (a) piemērā jānorāda nosacījums $x_{i} \neq 0$; (b) pieminēt, ka sakņu var būt arī **bezgalīgi daudz** (piem., $\frac{x^{2} - x}{x} = x - 1$ tipa vienādības, kas izpildās visā definīcijas kopā) | Ja kāds $x_{i} = 0$, piemērs nedod $n$ saknes. Tā kā jautājums paredzēts padziļinātai izpratnei, atbildei jābūt matemātiski pilnīgai; skolotājam vismaz piezīmē vērts zināt arī bezgalīgu sakņu kopas gadījumu. |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 Temata plānojuma 18. stundas rindā nav sasniedzamā rezultāta.** Plānojuma tabulā rindā „18. Noslēguma pārbaudes darba analīze" SR šūna ir tukša, lai gan 17.–18. stundas aprakstā SR ir formulēts („Analizē noslēguma pārbaudes darba kļūdas."). Ieteicams SR ierakstīt arī tabulā, lai plānojums būtu pilnīgs.

**3.2 🟡 „Nav standarta SR" satura pārbaude.** Materiālu aprakstā minēts, ka saturs, kas pārsniedz standarta SR, ir „pelēkā rāmī un apzīmēts Nav standarta SR", taču dokumenta pamattekstā šāds apzīmēts saturs nav atrodams. Ja tematā padziļinājuma bloku tiešām nav, teikumu vēlams precizēt vai svītrot (vai — ja bloki pazuduši konvertēšanas gaitā — tos atjaunot); ieteicams arī apzīmējumu likt pēdiņās: „Nav standarta SR".

**3.3 🟡 8.–10. stundā minētā mācību grāmata nav literatūras sarakstā.** Tekstā ieteikts izmantot „Matemātika 7. klasei" (I. France, G. Lāce, E. Slokenberga, Lielvārds, 2016, 86. un 90. lpp.), bet temata beigu literatūras sarakstā šis avots nav iekļauts. Ieteicams to pievienot sarakstam, lai visi tekstā minētie avoti būtu vienuviet.

**3.4 🟡 „Risināšanas plāns" (5.–7. stunda) saraksta vienotība.** Piezīme slīprakstā („Var nenoteikt definīcijas kopu, bet tādā gadījumā obligāti jāveic iegūto vērtību pārbaude…") pašlaik ievietota starp pirmo un otro plāna soli un sarauj numurēto/aizzīmju sarakstu. Ieteicams piezīmi pārcelt pirms vai pēc visa plāna (līdzīga piezīme jau ir pie 2. stundas piemēriem — abas var saskaņot arī redakcionāli).

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts |
|---|---|---|---|
| 4.1 | 8.–10. stunda | „Var **izmatot** mācību grāmatu…" | „Var **izmantot** mācību grāmatu…" |
| 4.2 | 8.–10. stunda, piezīme par mērvienībām | „jo ir gan stundas , gan minūtes" | „jo ir gan stundas, gan minūtes" (lieka atstarpe pirms komata) |
| 4.3 | 8.–10. stunda, piezīme „!!! Obligāts nosacījums…" | „ieviešot nezināmo jābūt skaidri norādītam…"; „…nav saprotams, **kādu** mašīnas **īpašība** vai lielums ir domāts" | „ieviešot nezināmo**,** jābūt skaidri norādītam…"; „…nav saprotams, **kāda** mašīnas īpašība vai **kurš** lielums ir domāts" |
| 4.4 | 3.–4. stunda | „Izteiksmes $g(x)$ un $h(x)$ proporcijas vidējie locekļi, bet izteiksmes $f(x)$ un $r(x)$ proporcijas malējie locekļi." | „Izteiksmes $g(x)$ un $h(x)$ **ir** proporcijas vidējie locekļi, bet izteiksmes $f(x)$ un $r(x)$ **ir** proporcijas malējie locekļi." |
| 4.5 | 1. stunda, piezīme par kopu starpības pierakstu | Formulas pieraksts sabojāts: `$x\mathbb{\in R \smallsetminus}\{4\}$` | Labot uz $x \in \mathbb{R} \smallsetminus \{4\}$ (komanda `\mathbb` attiecināma tikai uz burtu R) |
| 4.6 | 11.–12. stunda | „…reizina ar $x(x - 5) > 0$, jo $x$ ir **dienas**, kas ir pozitīvs lielums" | „…jo $x$ ir **dienu skaits**…" (saskaņot ar 2.3 labojumu) |
| 4.7 | Literatūras saraksts, 3. avots | „E. Slokenberga, I. France, I. France "Matemātika 10. klasei**'**, Lielvārds, 2009, 200.**\-\-**202. lpp." | Saskaņot pēdiņas (aizverošās dubultpēdiņas) un noņemt treknrakstu domuzīmei: „…"Matemātika 10. klasei", Lielvārds, 2009, 200.–202. lpp." (analoģiski treknā domuzīme 7. avotā „34.**\-\-**49. lpp.") |
| 4.8 | Literatūras saraksts, 8. un 10. avots | „80.--81.**lpp.**"; „64.--73.**lpp.**" | „80.–81. lpp."; „64.–73. lpp." (atstarpe pirms „lpp.") |
| 4.9 | Literatūras saraksts, 12. avots | „D. Čivžele "Uzdevumi matemātikas ieskaitēm 10.--12. klasei", Pētergailis, 25.--27. lpp." | Pievienot izdošanas gadu (vienīgais avots bez gada) |
| 4.10 | Vairākās vietās (pēc materiālu apraksta, pēc 1. stundas, pirms 11.–12. stundas, pirms 17.–18. stundas u. c.) | Konvertēšanas artefakti `**\**` (lappuses pārtraukumu paliekas) | Dzēst vai aizstāt ar korektu lappuses pārtraukumu galīgajā formātā |
| 4.11 | 5.–7. stunda, piezīme pie substitūcijas atkārtojuma | „*Kopīgi atkārto risināšanas soļus. (MK)*" | Atšifrēt vai dzēst saīsinājumu „(MK)" — lasītājam tas nav saprotams (iespējams, iekšēja piezīme, kas palikusi tekstā) |
| 4.12 | 1. stunda, piezīme „!!!" | „Domāt par vienādojuma … definīcijas kopu **ir jākļūst** par ieradumu." | Piem.: „Domāšanai par … definīcijas kopu **jākļūst** par ieradumu." vai „Jāizveido ieradums domāt par … definīcijas kopu." |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Piezīme pie piemēra $4x^{4} - 3x^{2} + 1 = 0$ (substitūcijas ievads).** Pēc substitūcijas $x^{2} = t$ iegūtajam vienādojumam $4t^{2} - 3t + 1 = 0$ ir negatīvs diskriminants, t. i., ne palīgvienādojumam, ne sākotnējam vienādojumam nav reālu sakņu. Tā kā uzdevumā prasīts tikai ieviest jaunu mainīgo, tas nav kļūda, taču ieteicams vai nu pievienot piezīmi skolotājam (ja skolēni mēģinās risināt līdz galam, viņi iegūs tukšu atrisinājumu kopu — to var izmantot kā mācību momentu), vai izvēlēties piemēru ar reālām saknēm.

**5.2 Liekās informācijas apzināta izmantošana Kārļa uzdevumā (13.–14. stunda).** Uzdevuma tekstā iekļautā informācija par teātra izrādi un „1 stundu katru darba dienu" risinājumā netiek izmantota. Ja tas ir apzināts paņēmiens (mācīt atlasīt būtisko informāciju — kas atbilst programmas modelēšanas akcentiem), ieteicams to skaidri pateikt piezīmē skolotājam; pretējā gadījumā tekstu vērts vienkāršot, lai skolēni nemēģinātu stundu skaitu iekļaut modelī.

**5.3 Vienota piezīme par reizināšanu ar izteiksmi.** Vienādojuma (atšķirībā no nevienādības) abas puses drīkst reizināt ar jebkuru izteiksmi, kas **nav nulle** — zīmei nozīmes nav. Ieteicams pievienot īsu piezīmi skolotājam, ka teksta uzdevumos akcentētā pozitivitāte ($> 0$) šeit kalpo konteksta novērtēšanai, bet matemātiski pietiek ar nosacījumu $\neq 0$; tas palīdzēs nodalīt argumentāciju, kas būs kritiski svarīga 5. tematā (daļveida nevienādības), kur reizinātāja zīme maina nevienādības zīmi.

**5.4 Atbilžu pieraksta paraugu vienotība 2. stundā.** Piemēros dažādi noformēts secinājums par saknes derīgumu ($-5 \in D.k.$; $-5 \notin D.a.$; „(neder)"; sistēmas pieraksts). Tā kā šī ir pirmā stunda, kurā skolēni apgūst daļveida vienādojuma atrisinājuma noformējumu, ieteicams vienā piemērā parādīt „etalona" pierakstu un pārējos apzināti komentēt kā pieļaujamas variācijas — tas atvieglos arī vērtēšanas kritēriju piemērošanu formatīvajos darbos.

---

### Kopsavilkums

Dokuments kopumā ir saturiski bagāts, labi strukturēts pa stundu grupām un atbilst programmas paraugam (18 stundas, visi temata SR pārklāti, iekļauti pat tie paši programmas piemēri substitūcijas metodei); īpaši vērtīgas ir skolotāja piezīmes ar jautājumiem izpratnes padziļināšanai un pilnie teksta uzdevumu atrisinājumu paraugi divos noformējuma veidos.

Pirms publiskošanas obligāti jānovērš 1. sadaļas kļūdas: substitūcijas piemēra nepareizā sakne ($t_{2} = 9$, nevis $6$, ar izrietošo $x_{2} = \frac{1}{8}$), uzdevuma un atrisinājuma nesakritība 5.–7. stundas 1. vienādojumā, nepilnā atbilde 2. stundas 4. piemērā, kā arī trīs secīgi nepareizās atsauces uz darba lapām (dl_4→dl_5, dl_5→dl_6, dl_6→dl_7), kas skolotāju aizvedīs pie nepareizā materiāla.

Ieteicams arī precizēt pamatojumus par reizinātāja pozitivitāti teksta uzdevumos, formulēt atslēgas spriedumus kā ekvivalences, nomainīt attēlu automātiski ģenerētos (t. sk. krievu valodas) alternatīvos tekstus un veikt pilnu korektūru atbilstoši 4. sadaļas paraugiem.
