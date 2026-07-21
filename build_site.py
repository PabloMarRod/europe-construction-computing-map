#!/usr/bin/env python3
"""Build a self-contained index.html from index.template.html + data.json.

The dataset is embedded in a <script type="application/json"> block so the
viewer needs no fetch() and no separate files. Leaflet is loaded from a CDN,
so there is no vendor/ folder to preserve. Result: a single file you can drag
into a GitHub repo; enable Pages and it works.

Run:  python3 build_site.py
"""
import json, pathlib, base64

root = pathlib.Path(__file__).parent
template = (root / "index.template.html").read_text(encoding="utf-8")
data = json.load(open(root / "data.json", encoding="utf-8"))

# Inline the EC3 logo as a data URI so no separate image file is needed.
logo = root / "ec3_logo.jpg"
if logo.exists():
    b64 = base64.b64encode(logo.read_bytes()).decode()
    template = template.replace('src="ec3_logo.jpg"', f'src="data:image/jpeg;base64,{b64}"')

# Compact JSON, escaped so it cannot terminate the <script> block or start a comment.
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")

assert "__DATASET__" in template, "placeholder __DATASET__ missing from template"
html = template.replace("__DATASET__", payload)

(root / "index.html").write_text(html, encoding="utf-8")
print(f"built index.html — {len(data)} records embedded, {len(html):,} bytes, self-contained")
