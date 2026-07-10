---
layout: default
title: Programmas parauga pārskatīšana (Ievads)
permalink: /review_plans/index/
---
# Programmas parauga pārskatīšana (Ievads)

Pašreiz izmantotais plāns domāts pārsvarā teksta dokumentiem. 
Tajā ir šādi soļi: 

* Pamatskolas un vidusskolas standarti no PDF pārvērsts par Markdown. 
* Programmas parauga ievaddokuments un metodiskie no DOCX pārvērsti par Markdown.
  Izmantots rīks "pandoc" ar apmēram šādu komandrindu:
  ```bash
  pandoc <dokuments.docx> -o <dokuments.md>
  ```
* Vieglāk konvertējamie faili (uzdevumi, vērtēšanas kritēriji) no DOCX pārvērsti par Markdown. 
  Vairums atrisinājumu un darba lapu nav pārvērsti. 
* Projekta faili ievietoti jaunā Claude projektā (nepieciešams Claude Pro konts).
  Sk. [Claude projekti](https://claude.ai/projects) informāciju par šo Anthropic pakalpojumu. 
* Valodu modelim (`Fable 5`, effort level `Extra`) pārlūka sesijā ieraksta promptu/uzvedni 
  ar lūgumu caurskatīt kārtējo dokumentu. Uzvedņu piemērus sk. zemāk. 
* Iegūtās atsauksmes apkopo GitHub pages sadaļā "Ieteikumi".

## Uzvedne atsauksmei par pamatskolas standartu

```
Lūdzu uzrakstiet savu atsauksmi par projektā esošo dokumentu `pamatskolas_standarts.md` 
(matemātikas kursā apgūtie temati 1.-9.klasē), ja zināms, ka tas ir priekšnoteikums
pirms mācīt `MATEMATIKA_1_programmas_paraugs_19_maijs.md` (projektā atrodama detalizēta 
programma ar vidusskolas 10.-12.kl. mācāmajiem matemātikas tematiem). Var pieņemt, 
Būtu svarīgi zināt, kādi izaicinājumi 10.klasē sagaida tos, kuri labāk vai sliktāk 
pirms tam apguvuši pamatskolas standartu.

Atsauksmē atrodamās sadaļas atbildē var izvēlēties patstāvīgi, lai rastos loģiski 
sakārtots dokuments. Atsauksmei par `pamatskolas_standarts.md` būtu jāpieskaras šādiem atspektiem: 
pamatskolas standarta iekšējās struktūras konsekvence; atbilstība pasaules labajai 
praksei (matemātikas mācīšanā no 7 līdz 15 gadu vecumam); satura apjoms atbilst 
matemātikai atvēlētajām stundām; standartā ietilpstošās tēmas var veidot loģisku 
secību, iegūtās zināšanas un prasmes ir saprotami kā var mērīt. Un, protams, arī 
"gap analysis", zinot 10.klasē mācāmo programmas paraugu: Vai pamatskolā ir temati, 
kuri nav pietiekami uzsvērti, bet 10.klases programmā parādās? Vai pamatskolā ir 
temati, kuri vēlāk vidusskolas klasēs netiek pietiekami nostiprināti? Vai ir 
ieteikumi izglītības politikas veidotājiem - kā būtu ieteicams pamainīt vai 
attīstīt pamatskolas standartu, lai tas (nemainot priekšmeta stundu skaitu 
pamatskolā) labāk atbilstu vidusskolā mācītajam saturam "Matemātika 1" programmas paraugā. 

Jūsu atbildē izveidojiet lejuplādējamu Markdown dokumentu latviešu valodā. 
Ja tas noder jūsu ieteikumu izklāstam, varat pievienot izklāstam tabulas, 
diagrammas un literatūras atsauces.
```

Sk. rezultātu: [Atsauksme par pamatskolas standartu]({{ '/OL__metodiskie/atsauksme_pamatskolas_standarts/' | relative_url }})

## Uzvedne atsauksmei par vidusskolas standartu

```
Lūdzu uzrakstiet savu atsauksmi par projektā esošo dokumentu `vidusskolas_standarts.md`
(vidusskolas 10.-12. klasēs apgūstamie temati, kas sakārtoti 3 kolonnās 
Vispārīgais/Optimālais/Augstākais - atkarībā no matemātikas kursa apgūšanas līmeņa). 
Ir zināms, ka Optimālajam līmenim (vidējai kolonnai visās tabulās) atbilst kurss "Matemātika 1", 
kura programmas paraugs "MATEMATIKA_1_programmas_paraugs_19_maijs.md" arī atrodams 
šajā projektā.  Parasti programmas paraugu (curriculum) ar noteiktu tematu izklāsta secību, 
mācīšanas metodēm un piemēriem veido atbilstoši standartam, bet šoreiz lūdzam Jūsu 
atsauksmi veidot par standartu, jo programmas paraugs izveidots vēlāk, lai atspoguļotu 
matemātikas mācīšanas labās prakses skolās, kur ir augsti kvalificēti skolotāji. 
Mūs interesē, kā tālāk attīstīt pirms 7 gadiem apstiprināto standartu, lai tas labāk 
atbilstu matemātikas mācīšanai reālajā dzīvē.  Matemātikā un dabaszinātnēs 
nespecializētās vidusskolās parasti māca optimālo līmeni visās vidusskolas klasēs, 
bet daudzās ģimnāzijās ir arī kurss "Matemātika 2" ar augstākā līmeņa tēmām, 
kurš šajā jautājumā netiek skarts.

Atsauksmē atrodamās sadaļas atbildē var izvēlēties patstāvīgi, lai rastos loģiski 
sakārtots dokuments. Atsauksmei būtu jāiekļauj standarta iekšējās struktūras 
konsekvence; atbilstība pasaules labajai praksei, mācot matemātiku 16-19 gadus 
veciem jauniešiem - vai varbūt arī citi tematu akcenti, kas izplatīti citās valstīs. 
Jāiekļauj arī satura apjoma atbilstība atvēlētajām stundām; tematu savstarpējo 
atkarību problēmas, iegūto zināšanu un prasmju izmērāmība. Kā arī tās jomas, 
kuras standartā būtu labi ieviest vai citādi akcentēt, lai tas būtu labāk saskaņots 
ar "Matemātika 1" programmas paraugu: Vai ir kādi citi ieteikumi izglītības 
politikas veidotājiem Latvijā, lai priekšmeta "Matemātika 1" mācīšanai būtu 
sakārtots normatīvais pamats? 

Atbildē izveidojiet lejuplādējamu Markdown dokumentu latviešu valodā.  
Ja tas noder jūsu ieteikumu izklāstam, varat pievienot izklāstam tabulas, 
diagrammas un literatūras atsauces uz ārējiem avotiem.
```

Sk. rezultātu: [Atsauksme par vidusskolas standartu]({{ '/OL__metodiskie/atsauksme_vidusskolas_standarts/' | relative_url }})



## Uzvedne metodisko ieteikumiem

```
Lūdzu izveidojiet labojumu/ieteikumu sarakstu NN.temata metodiskajam dokumentam
"OL_NN__pilns_nosaukums.md" - kā lejuplādējamu Markdown failu latviešu valodā.
Labākai izsekojamībai (traceability) projektā iekļauti ar tematu saistītie faili "OL_NN_*".
Atsauci vislabāk noformēt atbilstoši pievienotajam failam "atsauksmes_paraugs.md".
```

Sk. [atsauksmes_paraugs.md](https://raw.githubusercontent.com/kapsitis/programma-ol-10/refs/heads/main/docs/OL__metodiskie/atsauksmes_paraugs.md)

Sk. 12 tematu metodisko ieteikumus sadaļā "Ieteikumi". 


## Uzvedne standarta ekrānattēlu pārveidošanai Markdown (OCR uzdevums)

Ievades faili: 

* [Pamatizglītības standarts (no Skola 2030)](https://skola2030.lv/admin/filemanager/files/1/Matematika_G.pdf)
* [Vidusskolas standarts (no Skola 2030)](https://skola2030.lv/admin/filemanager/files/2/Matem%C4%81tikas%20m%C4%81c%C4%ABbu%20joma_VSK.pdf)

Sk. arī [https://skola2030.lv/lv/skolotajiem/macibu-prieksmeti/matematika](https://skola2030.lv/lv/skolotajiem/macibu-prieksmeti/matematika).

*Piebilde:* Droši vien labāk būtu izmantot gabalus no 
[MK noteikumi Nr. 747](https://likumi.lv/ta/id/303768-noteikumi-par-valsts-pamatizglitibas-standartu-un-pamatizglitibas-programmu-paraugiem)
un [MK noteikumi Nr. 416](https://likumi.lv/ta/id/309597-noteikumi-par-valsts-visparejas-videjas-izglitibas-standartu-un-visparejas-videjas-izglitibas-programmu-paraugiem),
jo tur standarts jau ir HTML formā (nevajag OCR). 

Izmantotā uzvedne (šeit pietiek ar vienkāršu modeli, piemēram `Sonnet 5`, effort level `Medium`):

```
Please convert the screenshot to markdown. Convert the green header
cell into H2 (## ...), and the leftmost cell into H3 (### ...).
Encode the remaining three columns into a simple Markdown table
using pipe syntax. Math formulas (typically shown in italics) 
should be written in LaTeX notation and enclosed between $s. 
Leave empty cells in your table whenever you
see them in the screenshot, but ensure that every column in your
table has the same number of cells (merge cells vertically,
if they appear to be finely split in some column).
If there are multiple cells in the leftmost column, add more H2
headings and split the table. Make the resulting Markdown easy
to download or copy to the clipboard.
```

**Rezultāti:**

* [Pamatskolas standarts]({{ '/pamatskolas_standarts/' | relative_url }})
* [Vidusskolas standarts]({{ '/vidusskolas_standarts/' | relative_url }})


## Tālākas darbības

Zemāk minētās darbības vēl nav veiktas; visticamāk abi plāni jāsapludina, lai 
varētu veidot pārskata darbības atbilstoši Claude plānam (6 posmos) vai 
arī GPT plānam (9 posmos). 

* [Claude plāns]({{ '/review_plans/review_plan_claude/' | relative_url }})
* [GPT plāns]({{ '/review_plans/review_plan_gpt/' | relative_url }})


