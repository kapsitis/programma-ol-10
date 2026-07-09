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
* Vieglāk konvertējamie faili (uzdevumi, vērtēšanas kritēriji) no DOCX pārvērsti par Markdown. 
  Vairums atrisinājumu un darba lapu nav pārvērsti. 
* Projekta faili ievietoti jaunā Claude projektā (nepieciešams Claude Pro konts).
* Valodu modelim (Claude Fable 5) pārlūka sesijā ieraksta promptu/uzvedni ar lūgumu caurskatīt 
  kārtējo dokumentu (sk. zemāk). 
* Iegūtās atsauksmes apkopo GitHub pages sadaļā "Ieteikumi".

**Uzvednes piemērs:** 

```
Lūdzu izveidojiet labojumu/ieteikumu sarakstu NN.temata metodiskajam dokumentam
"OL_NN__pilns_nosaukums.md" - kā lejuplādējamu Markdown failu latviešu valodā.
Labākai izsekojamībai (traceability) projektā iekļauti ar tematu saistītie faili "OL_NN_*".
Atsauci vislabāk noformēt atbilstoši pievienotajam failam "atsauksmes_paraugs.md".
```

Sk. [atsauksmes_paraugs.md](https://raw.githubusercontent.com/kapsitis/programma-ol-10/refs/heads/main/docs/OL__metodiskie/atsauksmes_paraugs.md)

## Programmu pārveidošana

Izmantotais prompts:

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


## Tālākas darbības

Zemāk minētās darbības vēl nav veiktas; visticamāk abi plāni jāsapludina, lai 
varētu veidot pārskata darbības atbilstoši Claude plānam (6 posmos) vai 
arī GPT plānam (9 posmos). 

* [Claude plāns]({{ '/review_plans/review_plan_claude/' | relative_url }})
* [GPT plāns]({{ '/review_plans/review_plan_gpt/' | relative_url }})