---
layout: default
title: Curriculum Review Plan (Claude)
permalink: /review_plans/review_plan_claude/
---
# Matemātika I Draft Curriculum — Review & Validation Action Plan

**Scope of review:** `MATEMATIKA_1_programmas_paraugs_19_maijs.md` (programme document, 22 topics, 420 h), the per-topic methodological materials (`OL_x__*_metodiskais.md`), and the supporting materials ecosystem (darba lapas / UZD, atrisinājumi / ATR, vērtēšanas kritēriji / KRIT, formative works / FVD, summative works / NPD, kopsavilkumi).
**Reference frame:** MK noteikumi Nr. 416 (2019) standard — matemātikas mācību jomas plānotie SR, optimālais līmenis (M.O.x.x.x codes), plus the programme's own declared intentions.
**Goal:** before the draft goes to teachers and other stakeholders, establish with documented evidence that the curriculum (1) formally complies with the standard, (2) actually delivers what its own introduction promises, and (3) stands up against international best practice — and produce a prioritised findings register that drives one revision cycle.

---

## 1. Review architecture — three lenses, one traceability spine

Every stage below examines the same corpus through one of three lenses, and all findings hang off a single **traceability matrix** built in Stage 0:

| Lens | Question it answers | Primary evidence |
|---|---|---|
| **A. Formal compliance** | Does the programme cover, and only claim, what the standard requires? | Standard (M.O. codes) ↔ programme SR tables |
| **B. Fidelity to declared intent** | Does the body of the programme deliver what its own IEVADS, MĒRĶIS UN UZDEVUMI and vērtēšanas sections promise? | Programme introduction ↔ topic frameworks ↔ OL materials ↔ assessments |
| **C. External quality** | Is this good curriculum by the standards of the field? | Corpus ↔ benchmark curricula and research-based design criteria |

**Division of labour principle.** LLMs do exhaustive, mechanical, cross-document work (extraction, cross-referencing, coverage matrices, first-pass classification, independent re-solving of every task); humans do everything that requires judgement, accountability, or classroom knowledge (didactic quality, cognitive-demand adjudication, benchmarking conclusions, sign-off). **No LLM finding enters the findings register as "confirmed" until a human has verified it; no human sign-off happens on a category the LLM sweep has not covered exhaustively.** The two are complementary filters, not substitutes.

**Multi-model / multi-pass protocol for LLM work.** Run each automated check with at least two independent passes (different model or different prompt framing); reconcile disagreements manually. Keep every prompt, output and reconciliation decision in the audit trail so the review itself is reviewable.

---

## 2. Stage 0 — Corpus preparation and traceability infrastructure (LLM + script work; ~1 week)

The single highest-leverage investment. Everything later becomes cheap once the corpus is machine-readable.

**0.1 Normalise the sources.**
- Re-OCR / verify the standard document (`Matemātikas_mācību_joma_VSK.pdf` is in fact a ZIP of scanned page images with an OCR text layer that contains ligature defects, e.g. "�" for "ti"). Produce a clean, verified text of all M.V. / M.O. / M.A. statements, human-proofread against the page images and cross-checked against the authoritative likumi.lv text of MK Nr. 416.
- Extract from the programme every SR row: topic №, temata vienums, SR text, cited codes, piemēri/skaidrojumi text, orange-marked (beyond-standard) flag.
- Extract from each `OL_x__*_metodiskais.md`: lesson plan rows (lesson №, topic, SRs, referenced worksheets/assessments), literature list.
- Inventory all UZD/ATR/KRIT/FVD/NPD files and their internal cross-references (e.g. `OL_1_dl_11`, `OL_1_npd`).

**0.2 Build the traceability matrix** (spreadsheet or database), one row per SR:

`M.O. code(s) ⇄ programme topic & SR ⇄ OL lesson(s) ⇄ worksheet(s) ⇄ formative assessment item(s) ⇄ summative assessment item(s) ⇄ criteria`

**0.3 Define the finding taxonomy** used by all subsequent stages: *Blocker* (standard non-compliance, mathematical error in student-facing material), *Major* (intent–delivery gap, misaligned assessment, broken progression), *Minor* (inconsistency, unclear wording), *Editorial* (typos, formatting), each with location, evidence, proposed fix, owner.

**Deliverables:** clean standard text; SR extraction tables; traceability matrix v1; findings-register template.

---

## 3. Stage 1 — Formal compliance and mechanical consistency (LLM-heavy sweep, human spot-check; ~1–2 weeks)

**1.1 Standard coverage audit (forward).** For every M.O.x.x.x in the standard: is it addressed at least once? In which topic(s)? Is the *depth* of the programme SR consistent with the level of the standard formulation (optimal, not silently downgraded to vispārīgais or inflated to augstākais)? Flag any M.O. code with zero or only tangential coverage. Special check: verify apparent numbering gaps in the standard itself (e.g. whether a 4.3 strand exists at optimal level at all, or is an OCR/extraction artefact) before concluding anything about coverage.

**1.2 Citation validity audit (reverse).** For every code cited in the programme: (a) does the code exist in the standard; (b) is it formatted consistently (a rapid pass already found `M.5.3.3.` — missing the "O" — in the Statistics topic alongside correct `M.O.5.3.x.` forms); (c) does the SR under that heading *semantically* belong to the cited code (LLM does a claim-by-claim entailment check; humans adjudicate borderline cases)?

**1.3 Beyond-standard content audit.** Verify that every SR exceeding the optimal level is actually orange-marked (per the programme's own convention) and that nothing orange-marked is in fact required by the standard. Cross-check with the "Nav standarta SR" grey-box convention in the OL materials — the two conventions must identify the same content.

**1.4 Arithmetic and internal consistency sweep.** Automatable checks: per-topic hour figures identical in the summary table and in the topic section headers (rapid pass: the table shows Atkārtojums = 30 h, summing to 420, while the topic 22 header states 20 stundas — one of them is wrong); topic titles identical between table and sections (rapid pass: topic 12 is "Līnijas plaknē…" in the table vs "LĪNIJAS VIENĀDOJUMS…" as the section heading); hour totals; lesson counts in OL plans vs declared topic hours; every referenced worksheet/assessment file exists; every worksheet has an ATR; every FVD/NPD has KRIT; grammar-level slips ("22 stunda", the incomplete sentence in the topic 22 goal "sistematizēt un apkopot apgūtos.").

**1.5 Terminology and notation consistency.** Build a concept glossary from all "Jēdzieni" lists; check each term is used with one meaning and one notation across all 22 topics and all worksheets (e.g. definīcijas kopa, interval notation, quartile labels Q₀–Q₄).

**1.6 Regulatory checklist.** Confirm the programme states everything MK Nr. 416 requires of a programmas paraugs (aims, content, assessment forms, organisation, ±10 %/25 % flexibility clause, the seven vērtēšanas pamatprincipi rendered accurately).

**Deliverables:** coverage matrix (M.O. × topics) with gap list; citation-error list; consistency findings; regulatory checklist — all fed into the findings register.

---

## 4. Stage 2 — Fidelity to declared intentions (LLM-assisted analytics, human-led judgement; ~2 weeks)

The introduction makes five explicit "mācību satura un pieejas akcenti" and a strong assessment philosophy ("vērtēšana, lai uzlabotu mācīšanos"). This stage tests whether the body of the curriculum honours them — the core of "matches its declared intentions."

**2.1 Accent-by-accent delivery audit.** For each declared accent, define observable indicators and measure their presence per topic:

| Declared accent | Observable indicators to count/inspect |
|---|---|
| Izpratne (understanding), not only prasmes | Share of SRs using *skaidro / pamato / spriež / atšķir / novērtē* verbs; presence of "explain why" tasks in worksheets and NPD, not only "compute" tasks |
| Problem-solving strategies as explicit learning outcomes | SRs of the form "izvēlas paņēmienu un pamato izvēli"; tasks requiring strategy choice among ≥2 taught methods; transfer tasks in new situations |
| Multiple representations | Tasks/lessons that move between symbolic ↔ graphic ↔ tabular ↔ verbal; graphical method presence beyond the dedicated lessons |
| Effective digital tools | Distribution of "t. sk. izmantojot IT" markers; whether IT use is *epistemically meaningful* (exploration, checking, visualisation) vs decorative; concrete tool guidance in OL materials |
| Seeing & formulating sakarības starp lielumiem | Per-topic presence of relationship-formulation tasks; generalisation prompts ("Vai var izdarīt vispārīgu secinājumu?") |

LLM produces the per-topic heatmap; a didactics expert judges whether thin cells are genuine gaps or acceptable (some accents legitimately concentrate in some topics).

**2.2 Constructive-alignment audit (goals → SR → activities → assessment).** For a sample of topics — and exhaustively for the two fully-materialised topics (1–2) — trace each SR through the matrix: is it taught (lesson + worksheet), practised, formatively checked, and summatively assessed? Flag: SRs taught but never assessed; assessed but never taught; assessed at lower cognitive demand than formulated (a "skaidro/pamato" SR tested only by a routine computation item).

**2.3 Cognitive demand profile of assessments.** Classify every NPD and FVD item with a recognised framework (Smith & Stein task-demand levels, or a Bloom/SOLO mapping): memorisation / procedures without connections / procedures with connections / doing mathematics. Compare the resulting distribution against the declared emphasis on izpratne and against the point weights in KRIT. Two humans independently rate a calibration sample first; LLM then classifies the rest; humans adjudicate disagreements.

**2.4 Assessment-system integrity.** Parallel-variant equivalence of the two NPD variants (item-by-item demand and point match); KRIT criteria actually discriminate understanding vs mechanics; formative works positioned where the OL plan claims and covering the SRs claimed; diagnostic-assessment guidance for the 10th-grade transition present and usable (the introduction makes this a priority).

**2.5 Learning-progression / dependency analysis.** Build the prerequisite graph across the 22 topics (LLM proposes; mathematician verifies): does the declared sequence respect dependencies (e.g. topic 1 factoring → topics 2–3 fractions/equations → topic 5 inequalities; topic 7 functions → 8–10 trigonometry; 13 → 14–15)? Do entry expectations of each topic match exit outcomes of earlier ones and the stated pamatskolas prerequisites? Is spaced revisiting of core skills planned, or does everything rely on topic 22 Atkārtojums?

**Deliverables:** accent heatmap; alignment gap list; cognitive-demand distribution report; assessment-integrity findings; dependency graph with any sequencing risks.

---

## 5. Stage 3 — Mathematical correctness and task quality (human experts with LLM as exhaustive first-pass screener; ~2–3 weeks, parallelisable with Stage 2)

**3.1 Independent re-solving.** An LLM (ideally two, independently) solves **every** task in every UZD/FVD/NPD file from scratch and diffs its results against the provided ATR/answers. Every discrepancy goes to a human mathematician — the human decides who is wrong. This catches both answer-key errors and ill-posed tasks (missing constraints, ambiguous wording, tasks with unintended extra solutions — extraneous roots in fraction equations, domain issues, etc.).

**3.2 Rigour and precision review (human mathematician).** Definitions, statements offered to students as facts (e.g. monotonicity ⇒ at most one root arguments in the graphical method), edge cases (definīcijas kopa handling, equivalence vs non-equivalence of transformations, sign-change conventions in algebraic fractions), and correctness of all "Piemēri un skaidrojumi".

**3.3 Didactic task-quality review (experienced teachers + didactics expert).** Difficulty gradation within worksheets; variation quality (systematic variation vs near-duplicates); treatment of documented misconceptions (the programme *promises* attention to typical errors — check each topic actually names and addresses them); authenticity and age-appropriateness of contexts; balance of routine vs non-routine work; solution write-ups as models of mathematical communication (an explicit uzdevums of the programme).

**3.4 Language and accessibility edit.** Professional Latvian-language edit of student-facing texts; readability; consistent instruction verbs across worksheets ("Sadali reizinātājos!", "Atrisini!" etc.).

**Deliverables:** verified answer keys; mathematical-error list; task-quality report per topic; language edit.

---

## 6. Stage 4 — External benchmarking against world best practice (human-led, LLM-assisted comparison; ~2 weeks)

**4.1 Assemble a benchmark corpus** of 4–6 reference curricula for the same age band and course type, e.g.: Estonia (gümnaasium, kitsas/lai matemaatika — closest system, PISA leader), Finland (LOPS 2019 MAA/MAB modules), Singapore (H1/H2 or O/A-level syllabi — exemplary coherence and problem-solving framing), NCTM *Catalyzing Change* + a Common-Core-aligned pathway, IB DP Mathematics AA/AI SL (exemplary assessment design and use of technology), and the PISA mathematical-literacy framework (2022+, with its reasoning and 21st-century-skills emphasis).

**4.2 Structured comparison** on: topic coverage and hour weighting (e.g. the share given to data/statistics/probability vs the international shift toward data literacy; the weight of trigonometric technique vs modelling); depth vs breadth (count of discrete SRs per hour — a proxy for overload risk); placement and role of proof and reasoning; integration of technology (whether benchmarks embed CAS/GeoGebra/spreadsheets more deeply); modelling-cycle presence; how benchmarks handle the basic-school→secondary transition.

**4.3 Research-based design criteria checklist.** Score the draft (with brief evidence) against: backward design / constructive alignment (Wiggins & McTighe; Biggs); curricular focus, rigour and coherence (Schmidt et al.); formative assessment integration (Black & Wiliam — the programme's own declared philosophy, so lens B and C converge here); cognitive activation and productive struggle; spaced practice and interleaving (is retrieval of earlier topics designed in?); differentiation (support for weaker students *and* stretch for STEM-bound students — the OL materials' "Nav standarta SR" boxes are the current mechanism; is it sufficient and systematic?); big-ideas architecture actually visible to the teacher at topic level (are the six Li referenced per topic, or only in the introduction?).

**4.4 Verdict memo.** For each benchmark dimension: *at par / above / below*, with a recommendation. Guard against false positives: differences from benchmarks are only findings if they conflict with the programme's own goals or the standard's intent — national context legitimately differs.

**Deliverables:** benchmark comparison matrix; design-criteria scorecard; prioritised recommendations memo.

---

## 7. Stage 5 — Usability and implementation validation (human-led; ~2–3 weeks, can start after Stage 3 clears topics 1–2)

**5.1 Cold-read teacher walkthrough.** 3–4 practising teachers (mixed school types, incl. a valsts ģimnāzija and a smaller regional school) who have *not* seen the materials plan and "teach" one topic on paper: can they navigate programme → OL → worksheets without the authors present? Where do they need information that isn't there? Structured think-aloud protocol, not a questionnaire.

**5.2 Time-realism audit.** Teachers estimate real classroom time per lesson plan against the allocated hours (17-hour topics with 15 content lessons + NPD + analysis leave zero slack — is that intentional?), including time for the diagnosticējošais darbs recommended at the start of topic 1, differentiation, and error-analysis lessons.

**5.3 Micro-pilot (if the calendar allows).** 2–3 teachers actually teach topic 1 (the only fully-materialised one) with real classes: collect lesson timings, student error patterns against the predicted "typical errors", worksheet completion rates, NPD score distributions and item statistics (facility, discrimination) on the two variants. Even a single-topic pilot converts many Stage 2–4 hypotheses into data.

**5.4 Inclusion and load check.** Iekļaujošais princips in practice: are there guidance and material variants for adapted assessment conditions? Homework/workload implications of 6 h/week? Availability of the cited literature (several referenced textbooks are from 1995–2012 — are they actually accessible to schools, and is dependence on them acceptable?).

**Deliverables:** usability report; time-realism table; pilot data pack; inclusion checklist.

---

## 8. Stage 6 — Synthesis, revision loop and release gate (~1 week + revision time)

1. **Consolidate** all findings into the single register; de-duplicate; severity-rank; assign owners.
2. **Author revision cycle** on Blockers and Majors; Minors/Editorial batched.
3. **Regression verification:** re-run the *automated* Stage 1 sweep and the affected Stage 2–3 checks on the revised text (this is where the Stage 0 infrastructure pays for itself a second time).
4. **Release gate checklist** — go to stakeholder discussion only when: 100 % of optimal-level M.O. codes covered or an explicit documented rationale exists; zero unresolved mathematical errors in student-facing materials; zero internal contradictions (hours, titles, codes); accent-delivery gaps either fixed or listed as known limitations; benchmark memo appended.
5. **Prepare the stakeholder package:** revised draft + a short "known issues & design rationale" annex (teachers respect a draft more when its authors show they know where it is thin) + the questions on which teacher input is genuinely wanted (e.g. time-realism, sequencing of topics 6–7, differentiation mechanism).

---

## 9. Roles, effort and sequencing at a glance

| Stage | Lead | LLM role | Human effort (indicative) |
|---|---|---|---|
| 0 Corpus & matrix | Technical editor | Extraction, structuring | 3–5 person-days |
| 1 Formal compliance | Standards reviewer | Exhaustive sweeps | 3–4 pd verification |
| 2 Intent fidelity | Didactics expert | Heatmaps, classification | 8–10 pd |
| 3 Maths & tasks | Mathematician + teachers | Re-solving, screening | 10–12 pd |
| 4 Benchmarking | Curriculum expert | Comparison drafting | 6–8 pd |
| 5 Usability/pilot | Teacher panel lead | Instrument drafting | 8–10 pd + pilot classes |
| 6 Synthesis & gate | Review coordinator | Regression re-runs | 3–4 pd |

Stages 2, 3 and 4 run in parallel after Stage 1; total calendar time ≈ 6–8 weeks without pilot, 8–10 with a one-topic pilot.

---

## Appendix A. Illustrative findings from a rapid pilot pass (to be verified — they demonstrate what Stage 1 will catch at scale)

1. **Hour inconsistency:** the summary table allocates 30 h to topic 22 Atkārtojums (and only then sums to 420), while the topic 22 section header states "(20 stundas)".
2. **Code-format defect:** the Statistics topic cites `M.5.3.3.` (missing "O") amid otherwise correct `M.O.5.3.x.` citations.
3. **Title mismatch:** topic 12 is "Līnijas plaknē, nevienādības ar diviem mainīgajiem" in the hours table but "LĪNIJAS VIENĀDOJUMS, NEVIENĀDĪBAS AR DIVIEM MAINĪGAJIEM" as the section heading.
4. **Editorial slips:** "(22 stunda)" (topic 13); truncated goal sentence "sistematizēt un apkopot apgūtos." (topic 22).
5. **Standard-side check needed:** the extracted M.O. code list jumps from 4.2.7 to 4.4.1 — confirm against the authoritative text whether a 4.3 strand exists at the optimal level (OCR gap vs genuine structure) before running the coverage audit.
6. **Source-file integrity:** `Matemātikas_mācību_joma_VSK.pdf` is not a valid PDF but a ZIP of page scans + OCR text with ligature defects — Stage 0 must produce a verified standard text before any coverage conclusions are drawn.

## Appendix B. Traceability-matrix column template

`topic_no | topic_title | vienums | SR_text | orange_flag | MO_codes_cited | MO_codes_validated | OL_lessons | worksheets | FVD_items | NPD_items | KRIT_ref | accent_tags (izpratne / strategies / representations / IT / sakarības) | cognitive_demand | status | findings_ids`

## Appendix C. LLM check-prompt patterns (Stage 1–3)

- *Coverage:* "Here is standard statement M.O.x.x.x and all programme SRs citing it. For each, state whether it fully / partially / does not operationalise the standard statement, quoting the deciding phrase."
- *Semantic citation check:* "Does this SR plausibly belong under code M.O.x.x.x, whose text is …? Answer yes/borderline/no with a one-sentence reason."
- *Re-solving:* "Solve the following task completely, stating the domain and checking for extraneous roots, before you are shown the official answer." (Diff afterwards.)
- *Demand classification:* "Classify this assessment item using the Smith–Stein levels; justify with the specific student action required."
- *Variant equivalence:* "Compare item 2.3 of variant 1 and variant 2 on mathematical demand, expected solution length, and error-proneness."

All LLM outputs are advisory; the findings register records the human verifier for each accepted finding.
