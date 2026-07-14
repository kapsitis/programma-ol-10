---
layout: default
title: "Kā no Markdown iegūt DOCX (Pandoc + Python)"
permalink: /review_plans/md_to_docx_howto/
---
# Kā no Markdown iegūt MS Word dokumentu (.docx)

Kā no `OL_1_npd_ATR.md` (pārbaudes darba atrisinājumi ar formulām un
attēliem) iegūst noformētu `.docx` failu. Konvertēšana notiek divos slāņos:
**Pandoc** pārvērš Markdown par `.docx` (arī `$$...$$` formulas kļūst par rediģējamām
Word/OMML formulām), pēc tam **Python skripts `scripts/md_to_docx.py`** 
ar `python-docx` pievieno lapai header/footer,
lapas izmēru, atrisinājumu fona krāsojumu.

> Rezultāts (atsauces paraugs) jau ir repozitorijā:
> `docs/OL_1_reizinataji_vienadojumi/OL_1_npd_ATR.docx` — ar to var salīdzināt.

Repozitorijs: <https://github.com/kapsitis/programma-ol-10>
Raw saknes URL (ērti `curl`/pārlūkam): `https://raw.githubusercontent.com/kapsitis/programma-ol-10/refs/heads/main/`

---

## 1. Savākt izejas failus

Vajadzīgi 1 Markdown *divi* tajā izmantotie PNG plus
konvertēšanas **skripts**. Markdown un PNG jābūt vienā direktorijā. 

| Fails | Ceļš repozitorijā |
|---|---|
| Markdown | `docs/OL_1_reizinataji_vienadojumi/OL_1_npd_ATR.md` |
| Attēls A | `docs/OL_1_reizinataji_vienadojumi/OL_1_npd_ATR.A.png` |
| Attēls B | `docs/OL_1_reizinataji_vienadojumi/OL_1_npd_ATR.B.png` |
| Skripts | `scripts/md_to_docx.py` |

Var klonēt visu repozitoriju: 

```powershell
git clone https://github.com/kapsitis/programma-ol-10.git
cd programma-ol-10
```

---

## 2. Uzstādīt Pandoc uz Windows 11

Pandoc var uzstādīt šādi:

```powershell
winget install --id JohnMacFarlane.Pandoc
```

Var arī MSI instalatoru no <https://pandoc.org/installing.html>.

**Atver JAUNU termināļa logu** (lai atjaunotos `PATH`) un pārbauda:

```powershell
pandoc --version
```


---

## 3. Python bibliotēkas un skripts

Vajadzīgs **Python 3.9+** (pārbaudīts ar 3.14).
Pievieno nestandarta bibliotēkas:

```powershell
python -m pip install --upgrade pip
python -m pip install python-docx pyyaml
```

Skripts `scripts/md_to_docx.py` jau ir savākts 1. solī.

```powershell
python scripts\md_to_docx.py --help
```

---

## 4. Palaišana (Command Prompt vai PowerShell)

Ja kloneja repozitoriju, tad no projekta saknes direktorijas:

```powershell
python scripts\md_to_docx.py `
  docs\OL_1_reizinataji_vienadojumi\OL_1_npd_ATR.md `
  docs\OL_1_reizinataji_vienadojumi\OL_1_npd_ATR.docx
```

**Neobligātie karodziņi** (pārraksta "front-matter" vērtības), piem.:
`--header "..."`, `--header-right "..."`, `--footer "..."` (var vairākkārt),
`--font "Times New Roman"`, `--fontsize 12`, `--math-align left|center|right`,
`--title "..."` (redzams virsraksts; pēc noklusējuma paslēpts), `--reference-doc ref.docx`.

Biežākā kļūda: **"pandoc failed" vai trūkst attēlu** — pārliecinieties, 
ka abi PNG ir tajā pašā mapē, kur `.md`, un ka 
`pandoc --version` strādā jaunā logā.

---

## 5. Sagaidāmais rezultāts (DOCX)

Savāc MS Word failu, lejuplādējot to no 
[GitHub](https://github.com/kapsitis/programma-ol-10/blob/main/docs/OL_1_reizinataji_vienadojumi/OL_1_npd_ATR.docx)


---

## 6. Uzvedne: no PDF izveidot līdzīgu Markdown

Ja ir pārbaudes darba PDF (ieskenēts vai eksportēts, ar uzdevumiem un atrisinājumiem),
to var augšupielādēt **Claude Pro Web UI** (vai pievienot Claude projektam) un lūgt
uzģenerēt Markdown, kas atbilst šī repozitorija konvencijām. Ieteicams stiprāks modelis
(piem. `Opus 4.x` / `Fable 5`, effort level `High`/`Extra`).

```
Pievienotais PDF ir matemātikas pārbaudes darbs ar atrisinājumiem. Lūdzu izveido
LEJUPLĀDĒJAMU Markdown failu (latviešu valodā), kas atbilst šādām konvencijām, lai
to vēlāk ar Pandoc + python-docx varētu pārvērst par .docx (skat. md_to_docx.py):

FRONT-MATTER (faila sākumā, starp ---):
  layout: default
  title: "<temata nosaukums> (atrisinājumi)"
  lang: lv
  geometry: "a4paper, top=2.5cm, bottom=2.5cm, left=2cm, right=2cm"
  permalink: /.../<faila-nosaukums>/
  docx_header: "<temata pilnais nosaukums — lapas galvas kreisā puse>"
  docx_header_right: "Matemātika I"
  docx_footer:
    - "© Valsts izglītības attīstības aģentūra | ESF+ projekts Nr. 4.2.2.3/1/24/I/001"
    - "Pedagogu profesionālā atbalsta sistēmas izveide"
  docx_font: "Calibri"
  docx_fontsize: 11
  docx_math_align: left

SATURA NOTEIKUMI:
  1. NELIETO Markdown virsrakstus (#, ##, ###). Uzdevuma numuru raksti kā treknu
     tekstu: "**2.** (\_\_\_/9 punkti) <instrukcija>" un apakšpunktu — "**2.1.** (2 p.) ...".
  2. Matemātiku raksti LaTeX pierakstā: iekļautu (inline) starp $...$, izceltu (display)
     starp $$...$$. Displeja formulas paliek pa kreisi izlīdzinātas.
  3. DALĪTAIS izkārtojums: uzdevuma nosacījumu liec iekļautajā formā uz atsevišķas
     rindas (uz balta fona), piem. "**1.1.** (1 p.) $5a^3b^2-15ab^3 =$", bet ATRISINĀJUMU
     liec atsevišķā displeja formulā, IETINOT to \color{blue}{...}:
        $$\color{blue}{5ab^2(a-3b)}$$
     (Katra $$...$$ formula, kas satur \color, .docx failā automātiski iegūst zilu fonu.)
  4. Ja atrisinājumā ir teksts, TABULA vai ATTĒLS, ietin VISU atrisinājumu blokā:
        ::: solution
        ... formulas, teksts, tabulas, attēli ...
        :::
     lai viss tiktu iekrāsots vienādi. Tabulas veido ar Markdown "pipe" sintaksi
     (| ... | ... |), nevis LaTeX, lai .docx redzētu īstas robežas.
  5. Ja darbam ir vairāki varianti, starp tiem ievieto lapas pārtraukumu:
        ```{=openxml}
        <w:p><w:r><w:br w:type="page"/></w:r></w:p>
        ```
  6. Attēlus (grafikus) atsaucies ar relatīvu ceļu, piem. ![](DARBS.A.png), un
     atsevišķi uzskaiti, kuri attēli jāizgriež no PDF (nosaukums + lappuse).

Sāc ar īsu sarakstu, kādi attēli/PNG būs jāizgriež no PDF, tad izvadi pilnu .md saturu
viena koda bloka veidā, ērti kopēšanai/lejuplādei.
```

Pēc atbildes: var saglabāt `.md`, izgriez/pārsauc minētos PNG blakus 
tam un palaist 4. soli.
