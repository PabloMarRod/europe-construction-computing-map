# europe-construction-computing-map

Interactive map of European higher-education institutions offering programmes in digital construction, BIM, and construction informatics. Each institution is shown on an OpenStreetMap basemap with programme details, cost, accreditation, language, delivery mode, and research/PhD opportunities.

**Live map:** _(add your GitHub Pages URL here)_
**Licence:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contents

| File / folder | Purpose |
|---|---|
| `index.html` | The application (map UI, filters, search, tooltips). Contains no data. |
| `data.json` | The dataset: 309 institutions across 42 countries. Loaded at runtime. |
| `dataset-metadata.json` | Dataset-level provenance: version, sources of record, methodology (geocoding, graduate estimation, cost sourcing), verification-level distribution, and known limitations. Not consumed by the app; intended for reuse, review, and archival deposit (e.g. Zenodo). |
| `topic-vocabulary.json` | Controlled vocabulary for the `topics` field: 40 terms split into two facets — computing/digital topics (25) and domains/disciplines (15), each with a definition. New dataset entries should use these controlled terms only. |
| `tagging-rubric.md` | The rule governing how topics are assigned and verified (named course/module or explicit learning outcome; applied uniformly), plus the interpretation of tags as a confirmed-presence floor. Governs the ongoing verification census. |
| `vendor/` | Bundled [Leaflet](https://leafletjs.com/) 1.9.4 + Leaflet.markercluster 1.5.3 (CSS, JS, marker images). Vendored locally so the map has no external script dependency and works offline. |
| `ec3_logo.jpg` | EC3 branding used in the header. |

## Running locally

The page loads its data with `fetch('data.json')`, which browsers block over the `file://` protocol. **Opening `index.html` directly by double-clicking will not work** — you must serve the folder over HTTP:

```bash
# from the repository root
python -m http.server 8000
# then open http://localhost:8000 in a browser
```

Any static file server works (`npx serve`, VS Code Live Server, etc.). No build step is required.

## Deployment

Enable GitHub Pages on the repository (Settings -> Pages -> deploy from the `main` branch, root). GitHub Pages serves over HTTPS, so `fetch` works with no further configuration. The map tiles are loaded from OpenStreetMap at runtime and require an internet connection; everything else is self-contained.

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
| `mode` | string | Full-time / Part-time / Distance. |
| `delivery` | string | Presential / Online / Hybrid. |
| `cost` | string | Indicative annual fee in EUR. |
| `graduatesPerYear` | string | Estimated annual graduates where known. |
| `graduatesEstimated` | bool | Present and `true` only where the value was imputed from peer institutions (absent = as originally collected). |
| `graduatesEstimateBasis` | string | For imputed values: the peer group and sample size used (e.g. `peer median, country+type:Poland/technical (n=4)`). |
| `verificationLevel` | 1-3 | Data-confidence level (see below). |
| `website` | string | Institution homepage. |
| `lastChecked` | string \| null | ISO date the record's programme/fee data was last verified against source. `null` = not yet verified in this provenance system. |
| `x`, `y` | number | **Legacy.** Percentage positions used by the previous image-based map; retained for provenance and no longer used by the app. |

### `geoSource` (coordinate provenance)

| Value | Meaning |
|---|---|
| `nominatim:name+city` | Resolved to the named institution in its city (campus-level). |
| `nominatim:name` | Resolved to the named institution (institution-level). |
| `nominatim:city` | Fell back to the city centroid — **approximate, not the campus location**. |
| `nominatim:*(manual)` / `*(audited)` | Hand-verified or upgraded during a review pass. |

### `verificationLevel` (data confidence)

1. Recently collected, not yet validated against sources.
2. Cross-referenced with publicly available university sources.
3. Confirmed directly by the institution.

## Contributing / corrections

Additions and corrections are welcome. Open an issue or a pull request editing `data.json`. Please keep the field structure above and cite a source for new figures where possible.

## Attribution

If you use this dataset, please cite it under CC BY 4.0. Basemap (c) OpenStreetMap contributors.
