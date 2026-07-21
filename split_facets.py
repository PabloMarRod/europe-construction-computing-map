#!/usr/bin/env python3
import json, sys
from collections import Counter

COMPUTING = [
    "BIM", "BIM Software", "openBIM & IFC", "ISO 19650", "nD BIM", "Infrastructure BIM",
    "Heritage BIM", "Digital Construction", "Construction Informatics", "Digital Twins",
    "AI & Machine Learning", "Parametric & Generative Design", "GIS & BIM Integration",
    "Data Management", "VR/AR", "3D Modeling & Scanning", "Digital Fabrication",
    "Robotics & Automation", "CAD/CAM", "Digital Design", "Programming", "IoT",
    "Collaborative Workflows", "Energy Performance", "Smart Cities & Buildings",
]
DOMAINS = [
    "Architecture", "Civil Engineering", "Structural Engineering", "Construction Engineering",
    "Infrastructure Engineering", "Construction Management", "Project Management",
    "Facility & Asset Management", "Procurement & Contracts", "Risk & Safety Management",
    "Lean & Integrated Delivery", "Sustainability", "Timber Construction",
    "Prefabrication & Modular Construction", "Innovation & Entrepreneurship",
]

facet = {t: "computing" for t in COMPUTING}
for t in DOMAINS:
    if t in facet:
        sys.exit(f"term in both facets: {t}")
    facet[t] = "domain"

d = json.load(open("data.json"))
used = {t for u in d for t in u.get("topics", [])}
missing = used - set(facet)
if missing:
    sys.exit(f"UNCLASSIFIED topics present in data: {sorted(missing)}")
print(f"all {len(used)} used topics classified ({len(COMPUTING)} computing, {len(DOMAINS)} domain)")

# Rebuild each record: drop topicCategories, add computingTopics + domains right after topics
for u in d:
    ct = [t for t in u.get("topics", []) if facet.get(t) == "computing"]
    dm = [t for t in u.get("topics", []) if facet.get(t) == "domain"]
    new = {}
    for k, v in u.items():
        if k in ("topicCategories", "computingTopics", "domains"):
            continue
        new[k] = v
        if k == "topics":
            new["computingTopics"] = ct
            new["domains"] = dm
    u.clear(); u.update(new)

json.dump(d, open("data.json", "w"), ensure_ascii=False, indent=2)
open("data.json", "a").write("\n")

# Controlled-vocabulary file: two facets, full 40-term list preserved
vocab = {
    "name": "Construction-Computing Education Topic Vocabulary",
    "version": "2.0.0",
    "description": "Controlled vocabulary for the `topics` field, organised into two facets: "
                   "computing/digital topics (the subject of this map) and domains/disciplines "
                   "(the built-environment context in which they are taught). Each record's "
                   "`topics` are also split into `computingTopics` and `domains`. New dataset "
                   "entries should use these controlled terms only.",
    "facets": {
        "computingTopics": {
            "definition": "Digital and computational methods, tools, standards and technologies "
                          "for the built environment — the core subject of this map.",
            "terms": COMPUTING,
        },
        "domains": {
            "definition": "Built-environment disciplines, application domains and management "
                          "areas that provide the context for the computing topics.",
            "terms": DOMAINS,
        },
    },
}
json.dump(vocab, open("topic-vocabulary.json", "w"), ensure_ascii=False, indent=2)
open("topic-vocabulary.json", "a").write("\n")

# coverage report
cc = Counter(); cd = Counter()
for u in d:
    if u["computingTopics"]: cc["has_computing"] += 1
    if u["domains"]: cd["has_domain"] += 1
comp_assign = sum(len(u["computingTopics"]) for u in d)
dom_assign = sum(len(u["domains"]) for u in d)
print(f"records with >=1 computing topic: {cc['has_computing']}/{len(d)} | with >=1 domain: {cd['has_domain']}/{len(d)}")
print(f"topic assignments: {comp_assign} computing, {dom_assign} domain")
