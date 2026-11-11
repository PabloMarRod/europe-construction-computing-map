# Topic tagging rubric

This rubric governs how the `topics` field (and its `computingTopics` / `domains` facets) is populated and verified. It exists to keep tagging **consistent across all institutions**, so that differences in the data reflect real differences in provision — not differences in how well an institution documents itself online.

## The rule

Assign a controlled-vocabulary topic to an institution **if and only if** the institution's own pages provide **either**:

- **(a)** a named course / module whose content matches the term, **or**
- **(b)** an explicit programme learning outcome or stated competency naming it.

Apply this identical threshold to every institution.

## Does NOT qualify

- A single passing mention in marketing prose ("...using digital tools...") with no named course or outcome.
- A research group / lab activity that is not part of the taught curriculum.
- Inference from institutional reputation ("it's a top school, so it must teach X").
- A single student thesis topic (evidence of one project, not of curriculum).
- Third-party aggregators, rankings sites, or directory listings as the sole source.

## Record-level inclusion (applied from October 2026)

- A record needs at least one qualifying computing topic. **CAD, programming, GIS or 3D visualisation/rendering on their own do not qualify**; a record with only these is removed. They may still be tagged alongside a qualifying topic.
- Qualifying topics include BIM (including a named Revit/ArchiCAD course), nD BIM, openBIM, ISO 19650, energy performance simulation, parametric and generative design, digital fabrication, digital construction/VDC, construction informatics, data management, IoT, VR/AR, AI, robotics and digital twins.
- Evidence comes from compulsory courses, electives or explicit learning outcomes in the official curriculum. Research activity counts only at doctoral level.
- Records are per institution. A failing programme is removed from the record without removing the institution if another programme qualifies; qualifying programmes found during review are added.
- `programLinks` point to the programme's own page (not a homepage, a general list or a PDF) wherever one exists.
- Fees are taken from the institution's own pages, or an official national source where the institution publishes none (never third-party aggregators), and recorded as a yearly figure.
- CPD and professional courses count only with a dedicated course page and evidence that they recur (not a one-off offering).
- A programme that no longer exists is removed. Where the institution's site cannot be reached but official programme or course evidence exists (e.g. a programme document found elsewhere on the institution's servers), the record may be kept at `verificationLevel` 1.

- An approved programme document (curriculum, course programme, scheme of studies) remains valid evidence until it is superseded by a newer version or the programme closes, whatever its intake year.
- A course counts only where an official source ties it to a named programme. A course list that does not say which programme it belongs to is not sufficient.
- Where a national standard or model curriculum defines a degree (e.g. Russia's ФГОС ВО codes such as 08.04.01, Pakistan's BS/B.E. Civil Engineering Technology schemes), the code alone is not evidence: each institution's own profile, scheme or course document must show the computing content.
- Generic AI courses (not applied to construction) are tagged AI & Machine Learning alongside other qualifying evidence, but do not qualify a programme on their own: a programme whose only computing evidence is generic AI is removed.
- Each record must carry at least two computing tags supported by its evidence.
- `verificationLevel` reflects confidence in the record's data (whether it was checked against the institution's own sources), not the amount or strength of computing evidence; content strength decides inclusion, never the level.
- Doctoral programmes may qualify through the institution's own doctoral research (e.g. a dissertation defence or PhD project on BIM); staff research alone does not qualify a programme.
- Where state-funded or grant places exist alongside paid places, the fee range starts at 0 (`0 - X`).
- Searches use the formats `<INSTITUTION> bim or computing in construction programs` (programmes) and `<INSTITUTION> tuition per year for <PROGRAMME>` (fees), one search per institution, followed by the institution's own fee or admissions pages and a local-language search before a fee is left as `-`.

## Sources of record

The institution's own programme, module/course-catalogue, and department pages. Where these are unavailable or in a language that cannot be verified, mark the record **unverifiable** and leave existing tags unchanged (do not guess, do not delete).

## Facets

Every controlled term is either a **computing topic** (digital/computational subject matter) or a **domain** (built-environment context). See `topic-vocabulary.json`. `computingTopics` and `domains` are derived from `topics` — do not hand-edit them.

## Interpretation of the tags

Verified tags represent **confirmed curriculum presence — a floor, not an exhaustive measure.** Because documentation depth varies by institution, absence of a tag means "not confirmed from public sources," not "not taught." Any analysis must treat topic counts as lower bounds and disclose documentation bias as a limitation.

## Provenance on each checked record

- `lastChecked`: ISO date the record was assessed against source under this rubric.
- `verificationLevel`: 2 once cross-referenced with public institutional sources under this rubric (3 only if confirmed directly by the institution).
- Coordinate provenance (`geoSource`) and graduate-estimate provenance (`graduatesEstimated`) are recorded separately.

## Known bias direction

A pilot sample (see `dataset-metadata.json` → `validation`) found under-tagging in ~52% of verified records and **zero** over-tagging, concentrated in lightly-tagged records (100% of single-tag records were under-tagged). Correcting under a consistent threshold therefore raises confirmed counts; it does not inflate them.
