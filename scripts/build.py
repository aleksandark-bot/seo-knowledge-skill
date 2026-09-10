#!/usr/bin/env python3
"""Rebuild this skill from the knowledge base (paths in scripts/config.json).

Writes:
  data/insights.jsonl          one merged insight per line — what kb.py queries
  data/sources.json            manifest + insight counts
  references/sources.md        human-readable source list
  references/full/*.md         whole-theme write-ups (deep dives only; kb.py is the default path)
  SKILL.md                     refreshes the auto-managed counts + theme table in place

Never hand-edit data/ or references/. Run via rebuild-all.sh after an ingest.
"""
import json, os, re, sys, collections, unicodedata, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CFG = json.load(open(os.path.join(HERE, "config.json")))
DATA = os.path.join(ROOT, "data")
REF = os.path.join(ROOT, "references")
FULL = os.path.join(REF, "full")

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60]   # must match the HTML builder's slug — override keys are truncated to 60

def norm(t):
    """Normalise a Pabau implication for comparison with the universal one."""
    t = t or ""
    t = re.sub(r"\bDavid\b", "You", t)
    t = re.sub(r"\b(Pabau|pabau)('s)?\b", "", t)
    t = re.sub(r"\b(the practice-management|practice management|clinic|aesthetic|medspa|med-spa|healthcare)\b", "", t, flags=re.I)
    t = re.sub(r"[^a-z0-9 ]+", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()

def nice(theme):
    t = theme.title()
    for a, b in [("Seo", "SEO"), ("Gsc", "GSC"), ("Geo", "GEO"), ("Ai", "AI"),
                 ("Eeat", "E-E-A-T"), ("Ugc", "UGC"), ("Serp", "SERP"),
                 ("Youtube", "YouTube"), ("Pr", "PR")]:
        t = re.sub(r"\b%s\b" % a, b, t)
    return t

# ---------------------------------------------------------------- load + merge
man_list = json.load(open(CFG["manifest"]))
man = {m["file"]: m for m in man_list}
by_id = {m["id"]: m for m in man_list}
raw = json.load(open(CFG["raw"]))["transcripts"]
ov = json.load(open(os.path.join(CFG["universal_dir"], "universal-overrides.json")))
ex = json.load(open(os.path.join(CFG["universal_dir"], "universal-extras.json")))

KEEP = ("category", "theme", "importance", "title", "detail", "evidence", "quote",
        "steps", "tools", "prompt", "pitfall", "implication", "lines")

rows = []
for t in raw:
    src = man[t["file"]]
    for k, i in enumerate(t["insights"], 1):
        uid = "%s:%s" % (src["id"], slug(i["title"]))
        r = {"id": "%s.%d" % (src["id"], k), "uid": uid, "sid": src["id"],
             "source_title": src["title"], "source_file": t["file"], "edition": "both"}
        for f in KEEP:
            if i.get(f) not in (None, "", [], {}):
                r[f] = i[f]
        u = ov.get(uid, {}).get("implication")
        if u and r.get("implication") and norm(u) != norm(r["implication"]):
            r["implication_universal"] = u
        elif u and not r.get("implication"):
            r["implication"] = u
        rows.append(r)

per_src_extra = collections.Counter()
for i in ex:
    sid = str(i.get("source", "??")).zfill(2)
    per_src_extra[sid] += 1
    src = by_id.get(sid, {})
    r = {"id": "%s.e%d" % (sid, per_src_extra[sid]), "uid": "%s:%s" % (sid, slug(i["title"])),
         "sid": sid, "source_title": src.get("title", ""), "source_file": src.get("file", ""),
         "edition": "universal"}
    for f in KEEP:
        if i.get(f) not in (None, "", [], {}):
            r[f] = i[f]
    rows.append(r)

dups = [k for k, n in collections.Counter(r["id"] for r in rows).items() if n > 1]
assert not dups, "duplicate ids: %r" % dups[:5]

# ---------------------------------------------------------------- data/
os.makedirs(DATA, exist_ok=True)
with open(os.path.join(DATA, "insights.jsonl"), "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
cnt = collections.Counter(r["sid"] for r in rows)
srcs = [dict(m, insights=cnt.get(m["id"], 0)) for m in sorted(man_list, key=lambda m: m["id"])]
json.dump(srcs, open(os.path.join(DATA, "sources.json"), "w"), ensure_ascii=False, indent=0)

# ---------------------------------------------------------------- references/full
def render(r, n):
    L = ["### %d. %s  `%s`" % (n, r["title"], r["id"]),
         "*%s · %s · source %s%s*" % (
             {3: "core", 2: "useful", 1: "context"}.get(r.get("importance", 2), "useful"),
             (r.get("category") or "").replace("-", " "), r["sid"],
             " · universal-edition only" if r["edition"] == "universal" else ""),
         "", r.get("detail", "").strip(), ""]
    if r.get("quote"):
        L += ['> "%s"' % r["quote"].strip().strip('"'), ""]
    if r.get("evidence"):
        L += ["**Evidence:** " + r["evidence"].strip(), ""]
    if r.get("steps"):
        L += ["**How to do it**", ""] + ["%d. %s" % (j, s.strip()) for j, s in enumerate(r["steps"], 1)] + [""]
    if r.get("tools"):
        L += ["**Tools:** " + ", ".join(r["tools"]), ""]
    if r.get("prompt"):
        L += ["**Prompt / template:**", "", "```text", r["prompt"].strip(), "```", ""]
    if r.get("pitfall"):
        L += ["**Pitfall:** " + r["pitfall"].strip(), ""]
    p, u = r.get("implication"), r.get("implication_universal")
    if p and u:
        L += ["**Apply at Pabau:** " + p.strip(), "", "**Apply anywhere:** " + u.strip(), ""]
    elif p:
        L += ["**Apply:** " + re.sub(r"^David should", "You should", p.strip()), ""]
    return "\n".join(L)

themes = collections.OrderedDict()
for r in rows:
    themes.setdefault(r["theme"], []).append(r)
order = sorted(themes.items(), key=lambda kv: (-len(kv[1]), kv[0]))

files = []
for theme, items in order:
    items.sort(key=lambda r: (-r.get("importance", 2), r["title"]))
    base = slug(theme)
    approx = sum(len(json.dumps(r)) for r in items)
    if approx > 60000:
        core = [r for r in items if r.get("importance", 2) == 3]
        rest = [r for r in items if r.get("importance", 2) != 3]
        if core and rest:
            files.append((theme, base + "-core.md", core, " — core"))
            files.append((theme, base + "-more.md", rest, " — supporting"))
            continue
    files.append((theme, base + ".md", items, ""))
chunked = []
for theme, fn, items, note in files:
    approx = sum(len(json.dumps(r)) for r in items)
    if approx > 90000 and len(items) > 28:
        parts = (len(items) + 24) // 25
        size = (len(items) + parts - 1) // parts
        for k in range(parts):
            sub = items[k * size:(k + 1) * size]
            if sub:
                chunked.append((theme, fn.replace(".md", "-%d.md" % (k + 1)), sub,
                                "%s (part %d of %d)" % (note, k + 1, parts)))
    else:
        chunked.append((theme, fn, items, note))
files = chunked

os.makedirs(FULL, exist_ok=True)
produced = set()
for theme, fn, items, note in files:
    body = ["# %s%s" % (nice(theme), note), "",
            "%d insights from the %s (both editions), core-first. Prefer `scripts/kb.py`; "
            "this file exists for deliberate whole-theme reads only." % (len(items), CFG["label"]), ""]
    body += [render(r, n) for n, r in enumerate(items, 1)]
    open(os.path.join(FULL, fn), "w").write("\n".join(body).rstrip() + "\n")
    produced.add(os.path.join(FULL, fn))

src_md = ["# Sources", "",
          "%d primary sources — talks, podcasts, videos and articles — behind every insight." % len(srcs),
          "Full transcripts: `%s/` (markdown) and `%s/` (line-numbered HTML mirrors, the line" % (
              CFG["transcripts_md"], CFG["transcripts_html"]),
          "numbers insights cite). `kb.py source NN` lists one source's insights.", ""]
for m in srcs:
    src_md.append("- **%s** — %s (%s, %d insights)  \n  %s" % (
        m["id"], m["title"], m.get("type", ""), m["insights"], m.get("source", "")))
open(os.path.join(REF, "sources.md"), "w").write("\n".join(src_md) + "\n")
produced.add(os.path.join(REF, "sources.md"))

removed = 0
for path in glob.glob(os.path.join(REF, "*.md")) + glob.glob(os.path.join(FULL, "*.md")):
    if path not in produced:
        os.remove(path)
        removed += 1

# ---------------------------------------------------------------- SKILL.md auto blocks
skill_path = os.path.join(ROOT, "SKILL.md")
if os.path.exists(skill_path):
    s = open(skill_path).read()
    n_ins, n_src = len(rows), len(srcs)
    core_c = collections.Counter(r["theme"] for r in rows if r.get("importance") == 3)
    tbl = ["| Theme | Insights | Core | `--theme` value |", "|---|---|---|---|"]
    for theme, items in order:
        tbl.append("| %s | %d | %d | `%s` |" % (nice(theme), len(items), core_c[theme], theme))
    block = "<!-- kb:auto:themes -->\n%s\n<!-- /kb:auto -->" % "\n".join(tbl)
    s2 = re.sub(r"<!-- kb:auto:themes -->.*?<!-- /kb:auto -->", block, s, flags=re.S)
    s2 = re.sub(r"\b[\d,]+ insights from [\d,]+ practitioner sources",
                "{:,} insights from {:,} practitioner sources".format(n_ins, n_src), s2)
    s2 = re.sub(r"\b[\d,]+ insights mined from [\d,]+ primary sources",
                "{:,} insights mined from {:,} primary sources".format(n_ins, n_src), s2)
    s2 = re.sub(r"\(the [\d,]+ sources with URLs", "(the {:,} sources with URLs".format(n_src), s2)
    if s2 != s:
        open(skill_path, "w").write(s2)
        print("SKILL.md: counts + theme table refreshed")

# ---------------------------------------------------------------- report
print("%s: %d insights (%d both-editions, %d universal-only) · %d sources · %d dual implications" % (
    CFG["skill"], len(rows), sum(r["edition"] == "both" for r in rows),
    sum(r["edition"] == "universal" for r in rows), len(srcs),
    sum(1 for r in rows if r.get("implication_universal"))))
print("data/insights.jsonl %.1f KB · references/full: %d files%s" % (
    os.path.getsize(os.path.join(DATA, "insights.jsonl")) / 1024, len(files),
    " · removed %d stale" % removed if removed else ""))
if "-v" in sys.argv:
    for theme, fn, items, note in files:
        print("  %-28s %-34s %3d %8.1f KB" % (theme, fn, len(items), os.path.getsize(os.path.join(FULL, fn)) / 1024))
