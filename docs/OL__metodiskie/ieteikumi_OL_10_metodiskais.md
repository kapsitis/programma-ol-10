---
layout: default
title: "Ieteikumi par 10. tematu"
permalink: /OL__metodiskie/ieteikumi_OL_10_metodiskais/
---

# Labojumu un ieteikumu saraksts — „OL_10. Trigonometriskie vienādojumi" (metodiskais materiāls)

**Pārskatītais dokuments:** `OL_10__Trigonometriskie_vienadojumi_metodiskais.md` (16 stundas).
**Salīdzināšanas avoti:** programmas paraugs (`MATEMATIKA_1_programmas_paraugs_19_maijs.md`, 10. temats), standarts (Matemātikas mācību joma VSK), projektā pieejamie temata faili `OL_10_dl_1…3, dl_5`, `OL_10_fvd_1…3 (UZD, KRIT)`, `OL_10_kopsavilkums`, `OL_10_npd_UZD_KRIT`, `OL_10_eksamenu_uzdevumi`.
**Prioritātes apzīmējumi:** 🔴 KRITISKS (matemātiska kļūda vai pretruna, jālabo obligāti) · 🟠 SVARĪGS (terminoloģija, precizitāte, konsekvence) · 🟡 IETEIKUMS (metodisks uzlabojums) · ⚪ REDAKCIONĀLS (valoda, noformējums).

---

## 1. Matemātiski labojumi 🔴 (jālabo pirms publiskošanas)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 1.1 | 1.–5. stunda, sadaļa „Vienādojums $tg\,x = a$", vingrinājums „Atrisini vienādojumu!", 2. piemērs | $tg\,x = -1$ … Atbilde. $x = -\frac{\pi}{6} + \pi n,\ n \in \mathbb{Z}$ | Atbilde. $x = -\frac{\pi}{4} + \pi n,\ n \in \mathbb{Z}$ | $tg\left(-\frac{\pi}{6}\right) = -\frac{\sqrt{3}}{3} \neq -1$, bet $tg\left(-\frac{\pi}{4}\right) = -1$. Jāpārbauda arī pievienotais TVR attēls (`media/image17.png`), vai tajā atlikts leņķis $-\frac{\pi}{4}$. |
| 1.2 | 6.–9. stunda, piemēri par formulu lietošanu, 4. piemērs | Nosacījums: $2\cos 3x \cdot \cos x + 2\sin 3x \cdot \sin x = \sqrt{3}$, ja $x \in \left(0; \frac{3\pi}{2}\right)$; risinājuma pirmā rinda: $\cos 2x \cos x + \sin 2x \sin x = \frac{\sqrt{3}}{2}$ | Nosacījumā rakstīt $2\cos 2x \cdot \cos x + 2\sin 2x \cdot \sin x = \sqrt{3}$ (tad viss tālākais risinājums un atbilde $x = \frac{\pi}{6}$ ir korekti) | Uzdevuma nosacījums (arguments $3x$) neatbilst risinājumam (arguments $2x$). Ja saglabā $3x$, tad $\cos(3x - x) = \cos 2x = \frac{\sqrt{3}}{2}$, $x = \pm\frac{\pi}{12} + \pi n$, un saknes dotajā intervālā ir $\frac{\pi}{12};\ \frac{11\pi}{12};\ \frac{13\pi}{12}$ — tad jāpārraksta viss risinājums. Vienkāršākais labojums — mainīt nosacījumu. |
| 1.3 | 6.–9. stunda, sadaļa „sadalot reizinātājos", 2. piemērs ($\sin 6x = \cos 3x$), zars $\cos 3x = 0$ | $3x = \frac{\pi}{2} + \pi$ | $3x = \frac{\pi}{2} + \pi n$ | Izlaists $n$; nākamā rinda $x = \frac{\pi}{6} + \frac{\pi n}{3}$ un gala atbilde ir korektas. |
| 1.4 | 6.–9. stunda, sadaļa „sadalot reizinātājos", 3. piemērs ($\sin x - 1 = \sin x\cos x - \cos x$) | Atbilde. $x = \frac{\pi}{2} + \pi n;\ \ x = 2\pi n,\ n \in \mathbb{Z}$ | Atbilde. $x = \frac{\pi}{2} + 2\pi n;\ \ x = 2\pi n,\ n \in \mathbb{Z}$ | Zara $\sin x = 1$ atrisinājums risinājuma gaitā uzrakstīts pareizi ($x = \frac{\pi}{2} + 2\pi n$), bet atbildē periods kļūdaini nomainīts uz $\pi n$ — tad atbildē iekļautos, piem., $x = \frac{3\pi}{2}$, kas nav vienādojuma sakne. |
| 1.5 | 10.–12. stunda, pēdējais piemērs ($\sin 3x - 3\cos 6x = 4$) | $t_1 = \frac{7}{6}$, $t_2 = -1$; $\sin 3x = \frac{7}{6}$ ($x \in \varnothing$), $\sin 3x = -1$; $3x = -\frac{\pi}{2} + 2\pi n$; Atbilde. $x = -\frac{\pi}{6} + \frac{2\pi n}{3}$ | $t_1 = 1$, $t_2 = -\frac{7}{6}$; $\sin 3x = -\frac{7}{6}$ ($x \in \varnothing$), $\sin 3x = 1$; $3x = \frac{\pi}{2} + 2\pi n$; Atbilde. $x = \frac{\pi}{6} + \frac{2\pi n}{3},\ n \in \mathbb{Z}$ | Kvadrātvienādojuma $6t^2 + t - 7 = 0$ saknēm samainītas zīmes ($D = 169$, $t = \frac{-1 \pm 13}{12}$). Pārbaude: $x = \frac{\pi}{6}$ dod $\sin\frac{\pi}{2} - 3\cos\pi = 1 + 3 = 4$ ✓, bet dokumentā dotā vērtība $x = -\frac{\pi}{6}$ dod $-1 + 3 = 2 \neq 4$. |
| 1.6 | 1.–5. stunda, ievadjautājums skolotājam (kursīvā) | *„Piemēram, ja funkcijas $y = \sin x$ vērtība ir $\frac{\pi}{6}$, nosaki atbilstošo argumenta vērtību."* | *„Piemēram, ja funkcijas $y = \sin x$ vērtība ir $\frac{1}{2}$, nosaki atbilstošo argumenta vērtību (piem., $x = \frac{\pi}{6}$)."* | Kā rakstīts, būtu jārisina $\sin x = \frac{\pi}{6} \approx 0{,}52$, ko bez ciklometriskajām funkcijām precīzi atrisināt nevar — sajaukta funkcijas vērtība ar argumenta vērtību, kas ir pretrunā ar piemēra nolūku (atsauce uz iepriekšējo tematu). |

---

## 2. Terminoloģijas un matemātiskās precizitātes labojumi 🟠

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts / ieteikums | Komentārs |
|---|---|---|---|---|
| 2.1 | Metodiskais komentārs par tematu, 2. rindkopa | „vispirms uzraksta vienādojuma vispārīgo vienādojumu un pēc tam nosaka, kuras saknes atrodas dotajā intervālā" | „vispirms uzraksta vienādojuma **vispārīgo atrisinājumu** un pēc tam…" | Termina kļūda; programmas paraugā jēdziens ir „vispārīgais atrisinājums". |
| 2.2 | 1.–5. stunda, piezīme pirms pamatvienādojumu apskata | *„Vienādojumu $ctg\,x = a$ neaplūko, jo to var pārveidot par vienādojumu $tg\,x = \frac{1}{a}$."* | Papildināt: „…par vienādojumu $tg\,x = \frac{1}{a}$, **ja $a \neq 0$**; ja $a = 0$, tad $ctg\,x = 0 \Leftrightarrow x = \frac{\pi}{2} + \pi n$." | Ja $a = 0$, izteiksme $\frac{1}{a}$ nav definēta, tāpēc apgalvojums bez nosacījuma nav korekts. |
| 2.3 | 1.–5. stundas sadaļa „Sasniedzamie rezultāti", 2. punkts | „…un $tg\ x = a$, lietojot **atrisinājumu** trigonometrisko vienības riņķi" | „…un $tg\ x = a$, lietojot trigonometrisko vienības riņķi" | Lieks vārds „atrisinājumu" (plānojuma tabulā tas pats SR uzrakstīts korekti). Vienādot abus formulējumus. |
| 2.4 | Piezīme „!!!" dokumenta sākumā un pirms sadaļas „Vienādojums $tg\,x = a$" | „Iekļauti arī vienādojumi ar tangensu, kas nav optimālā līmeņa saturs, tāpēc tos skolotājs var nemācīt…" | Precizēt tvērumu, piem.: „Vienādojumi formā $tg(ax+b) = c$ pārsniedz programmas paraugā minēto SR apjomu; pamatvienādojums $tg\,x = a$ programmā ir iekļauts." Vai arī atbilstošās daļas noformēt ar materiāla aprakstā pieteikto marķējumu „Nav standarta SR". | Programmas paraugā SR skaidri iekļauj pamatvienādojumu $tg\,x = a$ („Atrisina noteiktā intervālā trigonometriskos pamatvienādojumus $\sin x = a$, $\cos x = a$ un $tg\,x = a$…"); tikai pārveidojamā forma programmā minēta vienīgi ar $\sin$ un $\cos$. Arī valsts pārbaudes darbos tangensa pamatvienādojumi ir bijuši (sk. `OL_10_eksamenu_uzdevumi`: 2022. g. CE $tg\,x = \sqrt{3}$; NPD 1.3.). Pašreizējā vispārīgā piezīme ir pretrunā gan ar programmu, gan ar paša materiāla vērtēšanas darbiem. |

---

## 3. Struktūras un satura konsekvences ieteikumi 🟠 / 🟡

**3.1 🟠 Trūkst 4. darba lapas.** Metodiskajā ir divas atsauces uz `OL_10_dl_4` (1.–2. uzdevums un 3. uzdevums) un plānojumā 6.–9. stundai norādīta „4. darba lapa", taču temata failu komplektā ir tikai `dl_1`, `dl_2`, `dl_3` un `dl_5`. Jāpievieno trūkstošais fails vai jālabo atsauces (nosaukumu nepārtrauktība svarīga izsekojamībai).

**3.2 🟠 Tangensa uzdevumu statuss vērtēšanas darbos.** FVD 1 (1.4. $tg\,x = 0$ — 1 p.; 2.3. $tg(x-\frac{\pi}{3}) = \sqrt{3}$ — 2 p.) un NPD (1.3. — 2 p.; 2.3. daļa — 1 p.) iekļauj tangensa vienādojumus bez jebkāda marķējuma. Ja skolotājs seko piezīmei „!!!" un tangensu nemāca, punktu sadalījums un maksimālais punktu skaits jāpārstrādā. Pēc piezīmes precizēšanas (sk. 2.4) ieteicams vērtēšanas darbos atzīmēt tikai tos uzdevumus, kas patiešām pārsniedz SR.

**3.3 🟠 (saistītajā failā `OL_10_npd_UZD_KRIT`) 2. uzdevuma punktu virsraksts.** Abos variantos virsrakstā norādīts „2. (\_\_\_/4 *punkti*)", bet apakšuzdevumu summa ir 3 + 4 + 4 = **11 p.** (kritēriju tabulas kopsumma 38 p. ir rēķināta ar 11 p.). Jālabo uz „\_\_\_/11 punkti". Ieteicams sakārtot arī apakšuzdevumu izkārtojumu (šobrīd secība 2.1., 2.3. / 2.2.).

**3.4 🟡 Nav atsauces uz eksāmenu uzdevumu failu.** Fails `OL_10_eksamenu_uzdevumi_UZD` projektā ir, bet metodiskajā tas nekur nav pieminēts. Ieteicams pievienot norādi (piem., kopsavilkuma stundā vai avotu sadaļā), lai skolotājs zina par pieejamo resursu.

**3.5 🟡 Nelietots marķējums „Nav standarta SR".** Materiālu aprakstā pieteikts, ka saturs virs standarta SR ir „pelēkā rāmī un apzīmēts Nav standarta SR", taču tematā šāds noformējums nav sastopams (tangensa daļām lietots „!!!"). Vienādot konvenciju visos temata materiālos.

**3.6 🟡 Darba lapu atrisinājumu pieejamība.** Materiālu aprakstā teikts „Visām darba lapām ir doti atrisinājumi", taču pārskatītajā failu komplektā `OL_10_dl_*` atrisinājumu (ATR) failu nav. Pirms publiskošanas pārliecināties, ka atrisinājumi tiešām ir sagatavoti un pievienoti.

---

## 4. Valodas un redakcionālie labojumi ⚪ (raksturīgākie; ieteicama pilna korektūra)

| Nr. | Vieta dokumentā | Oriģinālais teksts | Labotais teksts | Komentārs |
|---|---|---|---|---|
| 4.1 | Metodiskais komentārs, 2. rindkopa | „Trigonometrisko vienādojumu atrisinājumu **noteikšanu** jāsaista arī ar…" | „…atrisinājumu **noteikšana** jāsaista arī ar…" | Debitīvā konstrukcijā (jāsaista) teikuma priekšmets ir nominatīvā. |
| 4.2 | Piezīme „!!!" pirms sadaļas „Vienādojums $tg\,x = a$" | „Vienādojumi ar tangensu**,** nav optimālā līmeņa saturs" | „Vienādojumi ar tangensu nav optimālā līmeņa saturs" | Lieks komats starp teikuma priekšmetu un izteicēju. |
| 4.3 | $\sin x = 0$ intervālu tabula, c) gadījums | „*Var ievērot ,ka katra nākamā vērtība…*" | „*Var ievērot, ka katra nākamā vērtība…*" | Komata atstarpe. Blakus tabulās vienādot arī jautājuma formu: „Kā **iegūst**…" / „Kā **iegūt**…". |
| 4.4 | Plānojuma tabula (6.–9. un 10.–12. stunda) | „*4.darba lapa*", „*5.darba lapa*" | „*4. darba lapa*", „*5. darba lapa*" | Atstarpe aiz kārtas skaitļa punkta (1.–3. darba lapa uzrakstītas korekti). |
| 4.5 | Viscaur dokumentā | $tg$ vietām slīprakstā (kā mainīgo reizinājums $t \cdot g$) | Funkciju nosaukumus rakstīt stāvrakstā: `\mathrm{tg}` / `\operatorname{tg}` (analoģiski `ctg`) | Matemātiskās tipogrāfijas konvencija; tagad pieraksts nekonsekvents (`${tg}x$`, `$tg\ x$`, `$tg(ax+b)$`). |
| 4.6 | Literatūras saraksts (4.–6., 8. pozīcija) | „10.\*\*--\*\*12.klasei", „195.\*\*--\*\*241. lpp.", „36.--48.lpp." | „10.–12. klasei", „195.–241. lpp.", „36.–48. lpp." | Treknraksta artefakti ap domuzīmēm; trūkstošas atstarpes. |

---

## 5. Metodiski ieteikumi kvalitātes celšanai 🟡 (nav obligāti, bet stiprina atbilstību programmas akcentiem)

**5.1 Precizēt substitūcijas metodes motivāciju.** 10.–12. stundas ievadā apgalvots, ka vienādojumu $2\cos^2 x - 5\cos x + 2 = 0$ „ar iepriekšējām metodēm atrisināt nevar". Tas nav gluži precīzi — kvadrāttrinomu var arī tieši sadalīt reizinātājos $(2\cos x - 1)(\cos x - 2)$, kas ir jau 1. tematā apgūta metode. Precīzāks formulējums: „vienādojums nav pārveidojams formā $\cos(ax+b) = c$, tāpēc izdevīgi ieviest jaunu mainīgo", pieļaujot arī sadalīšanu reizinātājos kā alternatīvu.

**5.2 Definīcijas apgabala akcents reizinājumos ar tangensu.** Piemērā $(tg\,7x + 1)\left(2\sin\frac{x}{3} - \sqrt{3}\right) = 0$ (un NPD 2.3. uzdevumā) ieteicams pievienot skolotāja piezīmi, ka otrā reizinātāja saknēm jāpārbauda, vai $tg\,7x$ eksistē (šajā piemērā nosacījums izpildās). Tas veido labu paradumu, kas būs svarīgs arī daļveida vienādojumu kontekstā.

**5.3 Modelēšanas uzdevumu konsekvence.** Fizikas (svārstību) piemērā funkcija definēta kā „novirze", bet jautājumā prasīts „augstums" — vienādot terminu. Ieteicams abos fizikas piemēros nosacījumu $t \geq 0$ minēt jau modeļa izveides solī (riteņa piemērā tas ir, svārstību piemērā parādās tikai netieši, izvēloties $n = 0$).

**5.4 Atrisinājuma eksistences spriešana pamatstundās.** Programmas paraugā pie pamatvienādojumu SR ir piemērs „spriež par vienādojuma atrisinājuma eksistenci" (piem., $\sin x + 2\cos x = 5$). Metodiskajā šis akcents parādās vienā piemērā ($\cos x = -\sqrt{2}$) un kopsavilkuma 4. uzdevumā; ieteicams 1.–5. stundā pievienot vēl 1–2 īsus spriešanas piemērus (piem., $\sin x = \frac{7}{6}$ saistībā ar 10.–12. stundas piemēru).

---

### Kopsavilkums

Dokuments kopumā ir loģiski strukturēts, atbilst 16 stundu plānojumam un programmas parauga sasniedzamajiem rezultātiem, piedāvā secīgu metodiku (grafiks → TVR → vispārīgais atrisinājums → saknes intervālā) un labus jautājumu paraugus skolotājam.

Pirms publiskošanas **obligāti** jānovērš 1. sadaļas matemātiskās kļūdas — īpaši nepareizā atbilde vienādojumam $tg\,x = -1$ (1.1), nosacījuma un risinājuma nesakritība argumentu saskaitīšanas piemērā (1.2) un kvadrātvienādojuma sakņu zīmju kļūda ar tai sekojošo nepareizo atbildi (1.5) —, kā arī jāatrisina 4. darba lapas trūkums (3.1) un tangensa satura statusa pretruna starp piezīmi „!!!", programmas paraugu un vērtēšanas darbiem (2.4, 3.2).

Ieteicams arī veikt pilnu teksta korektūru, sakārtojot Word→Markdown konvertēšanas artefaktus (klejojošie simboli, LaTeX pieraksti $n \in \mathbb{Z}$, funkciju nosaukumu stāvraksts), un papildināt materiālu ar atsauci uz eksāmenu uzdevumu failu.
