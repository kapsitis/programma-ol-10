---
layout: default
title: Curriculum Review Roadmap (Programmas pārskatīšanas plāns)
---
## Curriculum Review Roadmap

Please design a short roadmap how to proceed with reviewing a draft curriculum (details in the attached file "index.md"). 
The roadmap should not exceed a few pages - so that it is easy to review by humans and converted into future LLM requests. 
It should outline stages with their activities and gateway conditions - appropriate for future LLM requests. 
The Draft Curriculum to review is for the Grade 10, Latvian secondary education (some relevant documents are attached to this project). 

The standard for grades 1-9 is in "Matematika_G.pdf". The standard for grades 10-12 is in "Matemātikas mācību joma_VSK.pdf"  - 
the middle column "Optimālais apguves līmenis". Please note that our draft curriculum does not need to cover all of it - 
as some topics can also be covered in grades 11 or 12. (We want to cover about 1/2 of the standard; as some classes 
also cover topics from a more advanced standard - "Augstākais apguves līmenis"). The remaining files in this project - 
is a single topic (from a list of 12 topics). See "OL_1_reizinataji_vienadojumi". 
The Markdown files (...ATR.md) in this project were obtained by OCR of scanned handwriting; they are problems with solutions.

Your roadmap can be structured as a downloadable Markdown document. Please pay attention to the technical aspects 
(file formats; formal validation; precise conditions - gateways and validations to ensure quality and actionability 
when there are many "moving parts").



# Curriculum Evaluation Roadmap

We ask you for a Curriculum Review Roadmap as a curriculum-review planning agent with expertise 
in mathematics education, assessment design, Latvian curriculum standards, document analysis, 
and project management.

Your task is NOT to perform the full curriculum review yet.
Your task is to produce a detailed, practical ROADMAP for how such a review should be carried out, 
including stages, subgoals, milestones, outputs, quality gates, dependencies, risks, 
and the firm guidelines to be observed at each stage and gateways to other stages. 

The final actionable feedback in the eventual review must be usable by Latvian curriculum authors, 
so document-specific action items should be formulated in Latvian. However, this roadmap may be 
written in English unless otherwise useful.

## What the Curriculum is About

Latvian educational can pick any of the 3 levels to teach math to the grades 10-12 (ages 16-19):
Lowest/General level (Vispārīgais līmenis), Medium/Optimal level (Optimālais līmenis), Extensive/Highest level (Padziļinātais līmenis). 
This project contains a draft curriculum for the optimal level for Grade 10.

We need a roadmap to review this draft curriculum ("matemātikas mācību programmas paraugs") - it is a sequence of topics, worksheets, 
problemsets for exams arranged in multiple files. The curriculum must correspond to a nationwide standard of 
teaching mathematics listing the scope of the required topics - it is for the entire age interval (grades 10-12), 
there are no separate requirements for Grade 10. Thus the curriculum has some flexibility regarding the topic 
ordering, means of instruction, choice of problems, exercises and the exposition of required background knowledge.


## What Inputs are Available (where we are now)

The program currently contains these files:
1. "MATEMATIKA_1_programmas_paraugs_19_maijs.docx" - an overview document on how to use the draft curriculum, what 
   are the main challenges teaching mathematics at this level; the objectives for teaching; overview of the content 
   to be covered; the evaluation framework explained; and finally - a high-level overview of all the topics and 
   the knowledge items covered there. It also explains how to use all the other files.
2. For each topic there is a predictable set of files; we explain the first topic - subdirectory 
   "OL_1_reizinataji_vienadojumi" (Factorization and Equations). The structure in other directories is similar:

   A. "OL_1__sadalisana_reizinatajos_vienadojumi_metodiskais.docx" - didactic notes on how to approach the topic; 
      suggested lesson plans with their subgoals and examples.
   B. "OL_1_eksamena_UZD.docx" - Problem examples from past exams.
   C. "OL_1_fvd_1_sadalisana_reizin_UZD.docx" - Problemset for subtopic 1.1 - for "formative assessments" 
      that provide early feedback to the students)  and "OL_1_fvd_1_sadalisana_reizin_ATR.questions.pdf" 
      (solutions for the problems - scanned document with solutions filled in neat handwriting). 
      Such documents exist for multiple subtopics.
   D. "OL_1_kopsavilkums_UZD.docx" (a problemset for a single summary lesson near the end of the topic - all subtopics); 
      also with scanned solutions.
   E. "OL_1_npd_UZD_KRIT.docx" (the final "summative assessment" at the very end of the topic; includes criteria 
      for evaluation). Summative assessments typically are written once, but they may have multiple variants - 
      to reduce cheating or to cover students who have missed the class.
   F. Occasionally there are handouts with basic facts, presentations with nice pictures, visualizations or projects - 
      to support some activities throughout the lessons for this topic.
   G. Worksheets (typically - just problemsets) for each lesson. They also have scanned solutions in handwriting.



## Output Suggestions for the Curriculum Review (Where we want to get to)

Your output should be a roadmap document, not the review itself.
The roadmap must include:

1. A staged plan with some 5-10 major stages.
2. For each stage explain its purpose, inputs and other dependencies, 
   activities and some note on effort needed, outputs, gateway conditions. 
3. Consider suggesting change-request taxonomy as short tags. 
   For each change-request (review item) indicate its reason:

   - legal/standard alignment;
   - mathematical correctness and problem validity;
   - sequencing/prerequisites,
   - additional note for teachers or learners,
   - formatting or usability.
   - good practices of exam design and its variants,

4. A proposed severity/priority rubric.
5. A proposed evidence model as the LLM writes change-requests: How the roadmap will refer to files, how will it 
   deal with OCR issues, what evidence is included with each change-request.
6. A template for author-facing action items in Latvian.
7. The roadmap should be practical enough that another agent could follow it step by step.


## Guidelines (Unstructured)

As we evaluate the draft curriculum, there are multiple things to achive:

1. The draft curriculum needs to match the legal requirements (nationwide standard for teaching mathematics).

2. The draft curriculum needs to support sound pedagogical approach. Try to infer it from the material itself. 
   The aproach may or may not include items such as:
    
   - conceptual understanding;
   - procedural fluency;
   - problem solving;
   - mathematical reasoning;
   - communication;
   - formative feedback;
   - gradual release of responsibility;
   - appropriate scaffolding;
   - differentiation for varied learner readiness.

3. The curriculum should arrange topics (and subtopics for each lesson within a topic) in a coherent and teachable sequence,
4. The problems in problemsets need to be mathematically correct, relevant to the topic, appropriate in difficulty, 
   solvable with knowledge available to learners at that point, and sufficiently representative of the topic.
5. Focus on exam questions (for formative and summative evaluations) - do they reflect the taught material; do they cover 
   an appropriate range of cognitive demand and SOLO taxonomy levels. 
   Exam variants should be equivalent in difficulty but not mechanically identical. 
   Grading criteria should be clear, fair, and aligned to the intended learning outcomes
6. Document consistency and traceability - lower level topic and subtopic documents match top-level 
   outlines, problemsets and solutions match, literature references should be valid, file naming and 
   external references should be consistent. 
7. A system-wide consistency - is the approach for each topic is consistent with the overall curriculum, 
   consistent formatting, assessment design, usability for teachers. 
8. Apply international best practice in mathematics education, and separate clearly several issues:

   - compliance issues with the existing standard;
   - improvement suggestions within the current standard;
   - possible policy-level suggestions for improving the standard itself.

9. Produces actionable feedback:

   - linked to specific documents, sections, pages, tasks, or filenames;
   - written in Latvian when intended for curriculum authors;
   - prioritized by severity and effort;
   - distinguishing between required fixes, recommended improvements, optional enhancements, and policy-level observations.


You can also include additional review dimensions - in particular, if they can 
be automated by LLMs and if they lead to actionable feedback. 
If they are just nice-to-have (or would involve lots of human work or testing in a live classroom) drop them. 
For example:

A. On mathematical correctness (terminology and notation, edge cases, hidden assumptions etc.)
B. On cognitive demand and depth (classifying tasks and detecting blind spots)
   - routine procedural tasks;
   - conceptual explanation tasks;
   - transfer tasks;
   - non-routine problems;
   - modelling and application;
   - proof/reasoning where age-appropriate.
C. Assessment validity, reliability, and fairness
D. Inclusion and differentiation (scaffolds, language accessibility, support for students with gaps in prerequisite knowledge)
E. Teacher usability (lesson goals, time allocation, distinguishing mandatory and optional parts, clarification of common 
   misconceptions). 
F. Student learning experience (predictable structure, from intuitive to formal, self-checks), 
G. Workload and feasibility (scope and lesson count aligned, clarity of what is homework/classwork, assessment frequency 
   and grading burden, feasibility for average schools). 
H. Document production quality. 
I. Academic integrity and assessment security (quality of variants, reuse of problems, make-up assessment strategy). 


## Gateway Conditions

Here are some gateway conditions that could make sense from the curriculum 
developers' perspective. Your roadmap can include them (or their combinations) as transitions between 
states, if needed. You can also elaborate or split them, or suggest new gateway conditions or drop these.

1. Inventory gate - check, if all the expected files are of correct format and 
   are listed in a manifest.
2. Extraction gate - extract text+formulas (sometimes PNG images) from the DOCX/PDF/PPTX
   when needed.
3. Standard-compliance gate - does it identify the outcomes and cross reference with the standard.
4. Curriculum-model or internal-alignment gate - are the topics adhering to the announced plan; 
   all lessons/subtopics correctly identified. 
5. Pedagogy gate - issues of sequencing and prerequisites, cognitive-demand progression, 
   common misconceptions are noted in the curriculum.
6. Problem-validation gate - are the solutions checked, are the solutions consistent. 
7. Exam/Assessment validity gate - assessments map to learning outcomes, variants compared, 
   grading criteria checked, SOLO/cognitive-demand distribution summarized.
8. Synthesis gate - merge duplicate issues, assign severity, draft document-specific 
   action items in Latvian. Apply fixes in batches observing their dependencies; 
9. Review verification/QA gate. Claims are traceable, uncertainties pointed out, 
   actions at correct level (local fixes, structural redesign, policy/standard change suggestions). 


## Guidelines

1. The resulting roadmap has to be short and high-level when possible - 
   a few pages that can be thoroughly reviewed by humans; each stage 
   explained concisely.
2. The roadmap needs to have clear structure; can use tables or checklists 
   if helpful. 
3. Any action items for the curriculum authors would need to be based on 
   Latvian original text (and the fixes would also be in Latvian). 
   Also we would prefer didactic examples and pedagogical jargon specific to Latvia and Eastern Europe.
4. Curriculum creation procedure - its roadmap, individual stages, prompts are in English.
5. Do not begin the actual curriculum review; just provide the roadmap. 
6. Base your suggestions on the actual files in this project. 
7. Do not invent findings about the files. You may refer to the example filenames only as examples of expected file types.
8. Provide a checklist of preparatory steps that humans should do before the actual review can begin.

-----

# Roadmap: Review of the Draft Grade 10 Mathematics Curriculum (Optimālais līmenis)

**Object of review:** "Matemātikas mācību programmas paraugs" — Matemātika I (Grade 10, optimal level), organized as 1 overview document + 12 topic folders (each: methodical notes, per-lesson worksheets `*_dl_*_UZD`, formative assessments `*_fvd_*_UZD` + criteria `*_KRIT`, summary lesson `*_kopsavilkums`, summative assessment `*_npd_UZD_KRIT`, past-exam problems `*_eksamena_UZD`, scanned handwritten solutions OCR'd to `*_ATR.md`).
**Reference norms:** national standard, Grades 10–12, column "Optimālais apguves līmenis" (`Matemātikas_mācību_joma_VSK.pdf`); Grades 1–9 standard (`Matematika_G.pdf`) as the prerequisite baseline. The draft intentionally covers ≈½ of the 10–12 standard; the rest is deferred to Grades 11–12.
**Execution model:** each stage below is designed as one or more self-contained LLM work orders with fixed inputs, a machine-readable output schema, and a human-checkable gateway. Prompts and stage artifacts are in English; author-facing action items are in Latvian.

---

## 0. Preparatory checklist (humans, before any review runs)

- [ ] **P1. Provide original binaries.** The current project copies of `.docx` files are lossy text conversions (formulas flattened, e.g. fractions rendered as `1+xx`). Supply the original `.docx`/`.pdf`/`.pptx` binaries, or a conversion pipeline that preserves math (OMML→LaTeX, e.g. via pandoc), for **all 12 topics** (only Topic 1 is present now).
- [ ] **P2. Freeze a corpus snapshot.** One versioned folder per topic; no edits during review. Record version/date.
- [ ] **P3. Build the manifest skeleton.** CSV of every file: path, topic, doc-type code (`metodiskais / dl / fvd / kopsavilkums / npd / eksamena / ATR / KRIT / handout`), format, checksum.
- [ ] **P4. Scope declaration.** Authors mark which standard outcome codes (SR codes) are *intended* for Grade 10 vs. deferred to 11–12 vs. belonging to the Augstākais līmenis. Without this, "coverage gaps" cannot be adjudicated.
- [ ] **P5. OCR ground-truth kit.** Keep the scanned solution images alongside the `*_ATR.md` OCR; nominate a human contact for OCR disputes.
- [ ] **P6. Conventions note.** File-naming convention, abbreviations (UZD/ATR/KRIT/fvd/npd/dl), hour allocations per topic, grading scale in use.
- [ ] **P7. Named human reviewers** for two sign-offs: a mathematician (spot-check of re-solved problems) and a curriculum author (scope/standard interpretation).

---

## 1. Staged plan

### S1 — Inventory & manifest
| | |
|---|---|
| **Purpose** | Know exactly what exists; detect missing/extra/misnamed files before any content work. |
| **Inputs** | Frozen corpus (P2), manifest skeleton (P3), naming conventions (P6). |
| **Activities** | Auto-scan files; classify each by the doc-type taxonomy; verify format validity (is a `.docx` a real DOCX zip? is a PDF text-based or scanned?); check per-topic completeness against the expected set (every `UZD` has an `ATR`? every assessment has `KRIT`?); flag orphans and duplicates. *Effort: small, fully automatable; 1 LLM+script pass.* |
| **Outputs** | `manifest.csv` (file → topic → type → format → status), gap list. |
| **Gateway G1 (Inventory gate)** | ≥ agreed threshold (recommend 100%) of expected files present and format-valid **or** every gap explicitly waived by the owner. Every file has a stable **file ID** used in all later citations. |

### S2 — Extraction & normalization
| | |
|---|---|
| **Purpose** | Produce one canonical, citable text corpus with faithful mathematics. |
| **Inputs** | Manifest (S1), original binaries (P1), OCR files + scans (P5). |
| **Activities** | Extract text + formulas to Markdown/LaTeX per file; assign stable locators (heading path + task number, e.g. `OL_1_npd / 1. variants / uzd. 2.3` — *not* page numbers, which do not survive conversion); run a **formula-fidelity check** (sample formulas compared against source rendering); run an **OCR verification pass** on `*_ATR.md` files (mark suspect tokens — handwriting OCR typically mangles names and symbols) producing per-span confidence flags. *Effort: medium; scriptable + 1 LLM verification pass per file.* |
| **Outputs** | Canonical corpus `corpus/*.md`; `extraction_log.csv` (file ID → fidelity status: `VERIFIED / CONVERSION-LOSSY / OCR-UNCERTAIN` per section). |
| **Gateway G2 (Extraction gate)** | Every in-scope file has a canonical version; every math-bearing section has a fidelity status; sampled formulas match source at agreed rate (recommend ≥98%); unresolved OCR spans are flagged, not silently "fixed". |

### S3 — Standard compliance mapping
| | |
|---|---|
| **Purpose** | Legal alignment: map curriculum content to the standard's Optimālais līmenis outcomes. |
| **Inputs** | Canonical corpus (S2); standard SR-code tables from `Matemātikas_mācību_joma_VSK.pdf` (middle column) extracted into a code list; scope declaration (P4); Grades 1–9 standard as prerequisite baseline. |
| **Activities** | Harvest the SR codes cited in the overview and topic documents; build a two-way **coverage matrix**: (a) every cited code exists in the standard and is quoted correctly; (b) every standard code is classified `covered-G10 / deferred-11-12 (per P4) / above-level (Augstākais) / MISSING`. Check that claimed prerequisites exist in the 1–9 standard. *Effort: medium; 1 LLM pass over overview + 1 per topic.* |
| **Outputs** | `coverage_matrix.csv`; compliance change-requests (tag `STD`). |
| **Gateway G3 (Standard-compliance gate)** | 100% of cited codes resolved against the standard; 100% of standard codes classified; all `MISSING` items confirmed against P4 before being raised as findings. Human sign-off by curriculum author on the classification. |

### S4 — Internal alignment (curriculum model)
| | |
|---|---|
| **Purpose** | Traceability inside the draft: overview ↔ methodical notes ↔ lessons ↔ assessments tell the same story. |
| **Inputs** | Canonical corpus; manifest. |
| **Activities** | Per topic: check topic name, hour allocation, subtopic list and outcome list in the overview vs. the `metodiskais` document; check every planned lesson has a worksheet (`dl`) and every subtopic with formative assessment has `fvd + ATR (+KRIT)`; verify cross-references and terminology are consistent; verify each `UZD` ↔ `ATR` pair covers the same tasks in the same order. *Effort: medium; 1 LLM pass per topic.* |
| **Outputs** | Per-topic traceability table; change-requests (tags `SEQ`, `FMT`). |
| **Gateway G4 (Internal-alignment gate)** | Every lesson/subtopic uniquely identified and linked to its files; all mismatches logged as change-requests (none silently ignored). |

### S5 — Pedagogy & sequencing review
| | |
|---|---|
| **Purpose** | Judge the didactic design against the approach the curriculum itself announces (conceptual understanding, procedural fluency, reasoning, formative feedback, misconception work) and regional good practice. |
| **Inputs** | Canonical corpus; internal-alignment tables (S4). |
| **Activities** | Per topic: infer the intended pedagogical model from the `metodiskais` document; check prerequisite ordering across lessons (nothing used before taught — within the topic and across the 12-topic sequence); check cognitive-demand progression (intuitive → formal, gradual release); check misconception coverage ("kur skolēni raksturīgi kļūdās") is actually reflected in worksheets; check scaffolding/differentiation signals; check workload plausibility against declared hours. *Effort: medium-high; 1–2 LLM passes per topic + 1 cross-topic pass.* |
| **Outputs** | Pedagogy findings per topic; change-requests (tags `SEQ`, `PED`). |
| **Gateway G5 (Pedagogy gate)** | Every lesson has an explicit prerequisite verdict (OK / gap / uncertain); every finding cites concrete text; opinions without textual anchor are excluded. |

### S6 — Problem & solution validation
| | |
|---|---|
| **Purpose** | Mathematical correctness and fitness of every task and solution. |
| **Inputs** | Canonical corpus with fidelity flags (S2); prerequisite map (S5). |
| **Activities** | For each task: **independently re-solve** (LLM, with tool/CAS checking where possible), then compare with the provided `ATR` solution; classify discrepancies as (i) solution error, (ii) task defect (ambiguous, unsolvable, multiple answers), (iii) OCR/extraction artifact — the last only via the scan or original file, never by guessing; check solvability *with knowledge available at that lesson*; check terminology/notation (Latvian conventions, e.g. decimal comma, `Vjeta teorēma` naming) and hidden assumptions/edge cases (domains, zero denominators). Any claim about a `CONVERSION-LOSSY` or `OCR-UNCERTAIN` span must be verified against the source before filing. *Effort: high — the largest stage; 1 LLM work order per problemset.* |
| **Outputs** | `problem_audit.csv` (task ID → verdict → evidence); change-requests (tags `MAT`, `SRC`). |
| **Gateway G6 (Problem-validation gate)** | 100% of tasks have a verdict (`OK / defect / solution-error / source-uncertain`); every non-OK verdict includes an independent re-derivation; human mathematician (P7) spot-checks an agreed sample (recommend ≥10% + all high-severity items). |

### S7 — Assessment validity & exam design
| | |
|---|---|
| **Purpose** | Formative (`fvd`) and summative (`npd`) assessments measure the intended outcomes fairly. |
| **Inputs** | Problem audit (S6); coverage matrix (S3); `KRIT` criteria documents; past-exam file (`eksamena_UZD`). |
| **Activities** | Map each assessment task to taught outcomes (no untaught content in `npd`); classify each task by cognitive demand / SOLO level and summarize the distribution per assessment; compare **variants** of summative works for equivalence in content, difficulty, and point allocation while checking they are not mechanically identical; audit `KRIT` grading criteria for clarity, point-sum consistency, partial-credit fairness, alignment to outcomes; check alignment of curriculum tasks with the style/level of the past-exam problems; assess variant supply for make-up sittings and item-reuse risk (integrity). *Effort: medium-high; 1 LLM work order per assessment + 1 comparison order per variant pair.* |
| **Outputs** | Per-assessment validity report + SOLO distribution table; change-requests (tag `ASM`). |
| **Gateway G7 (Assessment-validity gate)** | Every assessment has an outcome map, a demand distribution, and a criteria audit; every variant pair has an equivalence verdict with per-task justification. |

### S8 — Synthesis & change-request register
| | |
|---|---|
| **Purpose** | Turn all findings into a deduplicated, prioritized, author-usable register. |
| **Inputs** | All change-requests from S3–S7. |
| **Activities** | Merge duplicates (same root cause across files → one CR with multiple locators); assign severity and effort (rubric §3); order by dependency (e.g., fix the overview table before dependent worksheets); draft the **author-facing action item in Latvian** for every CR (template §5); split the register into: required fixes / recommended improvements / optional enhancements / policy-level observations (the last kept in a separate annex, since they target the standard, not the draft). *Effort: medium; 1 LLM synthesis pass + human triage meeting.* |
| **Outputs** | `change_requests.csv` + Latvian action-item document per topic + policy annex. |
| **Gateway G8 (Synthesis gate)** | No duplicate CRs; every CR has: ID, tag, severity, effort, evidence, Latvian action text, dependency links; every `S1` (blocker) CR reviewed by a human. |

### S9 — QA & verification of the review itself
| | |
|---|---|
| **Purpose** | Make the review trustworthy before delivery. |
| **Inputs** | Change-request register (S8); canonical corpus; extraction log. |
| **Activities** | Traceability audit: random sample of CRs re-checked against source files (does the quoted text exist? is the locator correct? does the math claim hold?); verify uncertainty flags survived synthesis; verify each CR sits at the right level (local fix vs. structural vs. policy); verify Latvian action items are self-contained (an author can act without reading the English internals); compile the final review report. *Effort: small-medium; 1 LLM audit pass + human sign-off.* |
| **Outputs** | QA report; final deliverable package. |
| **Gateway G9 (QA gate)** | Sampled CR accuracy ≥ agreed bar (recommend ≥95%, with any failure class re-audited in full); zero CRs with missing evidence; both P7 sign-offs recorded. |

**Dependencies:** S1→S2→{S3,S4}→S5→S6→S7→S8→S9. S3 and S4 can run in parallel after G2. S6 can start per-topic as soon as that topic passes G4/G5 (pipelining by topic is recommended — 12 topics × the S4–S7 chain).

---

## 2. Change-request taxonomy (tags)

| Tag | Reason | Examples |
|---|---|---|
| `STD` | Legal / standard alignment | Missing or misquoted SR code; content above declared level |
| `MAT` | Mathematical correctness & problem validity | Wrong solution; unsolvable/ambiguous task; notation error |
| `SEQ` | Sequencing / prerequisites | Concept used before taught; illogical lesson order |
| `PED` | Didactic note for teachers/learners | Missing misconception warning; scaffolding gap |
| `ASM` | Assessment & exam-design practice | Variant inequivalence; criteria/point mismatch; SOLO blind spot |
| `FMT` | Formatting / usability / traceability | Naming inconsistency; broken reference; UZD↔ATR mismatch |
| `SRC` | Source/extraction uncertainty | OCR-suspect solution step; formula lost in conversion |
| `POL` | Policy-level observation (annex only) | Suggestion to amend the standard itself |

---

## 3. Severity × effort rubric

| Severity | Meaning | Delivery class |
|---|---|---|
| **S1 Blocker** | Standard non-compliance; mathematically wrong task/solution/criteria; unsolvable assessment item | Required fix |
| **S2 Major** | Materially harms teaching/assessment (prerequisite gap, inequivalent variants, unclear criteria) | Required fix |
| **S3 Minor** | Quality issue with workaround (inconsistent notation, missing note) | Recommended improvement |
| **S4 Cosmetic/Idea** | Polish or enhancement | Optional enhancement |
| **S0 Policy** | Outside the draft's control | Policy annex |

Effort: **E1** trivial (single edit), **E2** moderate (rework a task/lesson), **E3** structural (reorder/redesign across files). Priority = severity first, then lowest effort first within a severity class; dependency links may override.

---

## 4. Evidence model (mandatory for every change-request)

Each CR carries:
1. **File ID + locator** from the manifest — `fileID :: heading path :: task number` (page numbers only for PDFs that keep pagination, e.g., the standard).
2. **Verbatim quote** of the original Latvian text (short — enough to relocate it), taken from the canonical corpus.
3. **Source-fidelity flag** inherited from S2: `VERIFIED / CONVERSION-LOSSY / OCR-UNCERTAIN`. CRs about lossy/uncertain spans must state that the claim was confirmed against the original binary or scan; otherwise they are filed as `SRC` (verify source) rather than `MAT` (math error). *This rule exists because the current working corpus demonstrably flattens formulas and the `ATR` files come from handwriting OCR.*
4. **Reasoning artifact** for math claims: the independent re-derivation (or CAS check) that contradicts or confirms the source.
5. **Confidence** (`high / medium / low`) — low-confidence items are questions to authors, never assertions.

---

## 5. Author-facing action item template (Latvian)

```
CR-{ID}  [{TAG}] [{S-līmenis}/{E-līmenis}]
Dokuments:   {faila nosaukums}, {sadaļa / uzdevuma nr.}
Citāts:      "{oriģinālteksta fragments}"
Problēma:    {īss problēmas apraksts latviski — kas un kāpēc neatbilst}
Ierosinājums:{konkrēta veicamā darbība latviski; ja iespējams — gatavs
              labojuma teksts vai pārstrādāts uzdevums}
Pamatojums:  {atsauce uz standartu (SR kods) / matemātisku izvedumu /
              didaktisku principu}
Statuss:     {obligāts labojums | ieteicams uzlabojums | izvēles papildinājums}
Piezīme:     {ja avots ir OCR/konvertēts — norāde pārbaudīt oriģinālu}
```

---

## 6. Key risks and mitigations

| Risk | Mitigation |
|---|---|
| Formula loss in DOCX→text conversion produces false "math errors" | P1 original binaries; S2 fidelity flags; §4 rule 3 |
| Handwriting-OCR errors in `*_ATR.md` misread as solution errors | OCR verification pass (S2); scan-backed confirmation before filing `MAT` |
| Coverage "gaps" that are actually deliberate deferral to Grades 11–12 | P4 scope declaration; G3 human sign-off |
| LLM over-claiming / hallucinated findings | Evidence model §4; G9 traceability sampling; low-confidence → questions |
| Only 1 of 12 topics currently available | G1 blocks full review; pipeline per topic once folders arrive |
| Review drift across 12 topics (inconsistent standards applied) | Fixed per-stage work-order prompts + shared rubrics; cross-topic consistency pass in S5/S8 |
