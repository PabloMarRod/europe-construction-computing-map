# Construction Computing Map

Interactive map of global higher-education institutions offering programmes in digital construction, BIM, and construction informatics. Each institution is shown on an OpenStreetMap basemap with programme details, cost, accreditation, language, delivery mode, and research/PhD opportunities.

**Live map:** _https://pablomarrod.github.io/europe-construction-computing-map/_

**Licence:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contents

| File / folder | Purpose |
|---|---|
| `index.html` | **The map viewer.** Map UI, filters, search and tooltips, with Leaflet loaded from a CDN. Loads `data.json` at runtime, so it must be served over HTTP (GitHub Pages, or `python3 -m http.server` for a local preview); opening the file directly from disk will not load the data. |
| `data.json` | **The canonical dataset.** Currently 773 institutions in 58 countries (Europe 324, South America 327, North America 82, Oceania 40) and the single source of truth. The viewer reads it directly at runtime; also intended for citation, reuse, and archival deposit. |
| `dataset-metadata.json` | Dataset-level provenance: version, sources of record, methodology (geocoding, graduate estimation, cost sourcing), verification-level distribution, and known limitations. Not consumed by the app; intended for reuse, review, and archival deposit. |
| `topic-vocabulary.json` | Controlled vocabulary for the `topics` field: 40 terms split into two facets — computing/digital topics (25) and domains/disciplines (15), each with a definition. New dataset entries should use these controlled terms only. |
| `tagging-rubric.md` | The rule governing how topics are assigned and verified (named course/module or explicit learning outcome; applied uniformly), plus the interpretation of tags as a confirmed-presence floor. Governs the ongoing verification census. |
| `ec3_logo.jpg` | EC3 branding used in the header. |

## Data schema

`data.json` is an array of institution objects. Fields:

| Field | Type | Notes |
|---|---|---|
| `name`, `city`, `country` | string | Institution identity. |
| `lat`, `lon` | number | Geographic coordinates (WGS84). |
| `geoSource` | string | How the coordinates were derived — see below. |
| `programs`, `programLinks` | string[] | Programme names and their URLs. |
| `topics` | string[] | All topics covered, from the controlled vocabulary in `topic-vocabulary.json`. |
| `computingTopics` | string[] | Subset of `topics` that are computing/digital topics (the subject of this map). Derived. |
| `domains` | string[] | Subset of `topics` that are built-environment domains/disciplines (context, e.g. Architecture). Derived. |
| `accreditation` | string[] | Accrediting/professional bodies. |
| `language` | string | Language(s) of instruction. |
| `mode` | string | Full-time / Part-time / Distance / Apprenticeship, combined with ` / ` (e.g. `Full-time / Part-time`). |
| `delivery` | string | Presential / Online / Hybrid, combined with ` / ` (e.g. `Presential / Online`). |
| `cost` | string | Indicative annual fee in the record's `costCurrency`. Ranges run lowest to highest published fee. `0` = no tuition; `-` = fee not published by the institution. |
| `graduatesPerYear` | string | Estimated annual graduates where known. |
| `graduatesEstimated` | bool | Present and `true` only where the value was imputed from peer institutions (absent = as originally collected). |
| `verificationLevel` | 1-3 | Data-confidence level (see below). |
| `website` | string | Institution homepage. |
| `costCurrency` | string | ISO currency code for `cost`. |
| `lastChecked` | string \| null | ISO date the record's programme/fee data was last verified against source. `null` = not yet verified in this provenance system. |

### `geoSource` (coordinate provenance)

| Value | Meaning |
|---|---|
| `nominatim:name+city` | Resolved to the named institution in its city (campus-level). |
| `nominatim:name` | Resolved to the named institution (institution-level). |
| `nominatim:name (audited)` | Institution-level geocode checked by hand during a review pass. |
| `nominatim:city` | Fell back to the city centroid — **approximate, not the campus location**. |
| `manual:campus` | Campus coordinates entered by hand from an official or map source. |
| `manual:campus (audited)` | Manual campus coordinates checked during a review pass. |
| `manual:city` | City (or regional capital) coordinates entered by hand — **approximate, not the campus location**. |

### `verificationLevel` (data confidence)

1. Recently collected, not yet validated against sources.
2. Cross-referenced with publicly available university sources.
3. Confirmed directly by the institution.

## Contributing / corrections

Additions and corrections are welcome. Open an issue or a pull request editing `data.json`. Please keep the field structure above and cite a source for new figures where possible.

## Attribution

If you use this dataset, please cite it under CC BY 4.0. Basemap (c) OpenStreetMap contributors.
