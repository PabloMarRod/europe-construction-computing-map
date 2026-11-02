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
- Fees are taken only from the institution's own pages (never third-party aggregators) and recorded as a yearly figure.
- A programme that no longer exists, or whose site cannot be reached, is removed rather than kept unverified.

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
