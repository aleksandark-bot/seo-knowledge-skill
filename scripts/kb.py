#!/usr/bin/env python3
"""Query the knowledge base without reading it whole.

  kb.py search "<query>" [-n 10] [--theme T]... [--core] [--source NN] [--titles]
  kb.py show ID [ID...] [--brief]          full write-up(s); --brief = title, gist, apply + pitfall where present
  kb.py theme [NAME] [--core]              list themes, or every title in one theme
  kb.py source [NN]                        list sources, or one source + its insights
  kb.py grep "<regex>" [--titles-only]     exact/regex match over titles (+ body)
  kb.py stats

IDs look like 53.12 (source 53, 12th insight) or 53.e1 (universal-only extra).
`show` also accepts a unique prefix of the long id, e.g. 53:cap-in-body.
Every command prints only what it is asked for — that is the point of this tool.
"""
import sys, os, re, json, math, argparse, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
CFG = json.load(open(os.path.join(HERE, "config.json")))

# ------------------------------------------------------------------ loading
def load():
    rows = []
    with open(os.path.join(DATA, "insights.jsonl")) as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    sources = json.load(open(os.path.join(DATA, "sources.json")))
    return rows, sources

STOP = set("""a an and are as at be by for from has have in is it its of on or that the this to was
were will with you your we our they their not can do does if then than into over under about
should would could also more most any all one two how what when which who why""".split())

def stem(w):
    if len(w) <= 4:
        return w
    for suf in ("ities", "ies", "ings", "ing", "ers", "edly", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            base = w[: -len(suf)]
            if suf == "ies":
                base += "y"
            return base
    return w

def toks(s):
    return [stem(w) for w in re.findall(r"[a-z0-9][a-z0-9\-\.']*", (s or "").lower())
            if w not in STOP and len(w) > 1]

FIELDS = (("title", 4.0), ("tools", 2.0), ("pitfall", 1.5), ("implication", 1.5),
          ("implication_universal", 1.0), ("evidence", 1.0), ("detail", 1.0),
          ("steps", 1.0), ("theme", 1.0), ("prompt", 0.5))

def doc_text(r, field):
    v = r.get(field)
    if isinstance(v, list):
        return " ".join(v)
    return v or ""

# ------------------------------------------------------------------ search
def bm25(rows, query, k1=1.2, b=0.75):
    q = toks(query)
    if not q:
        return []
    tfs, lens = [], []
    df = collections.Counter()
    for r in rows:
        tf = collections.Counter()
        for field, w in FIELDS:
            for t in toks(doc_text(r, field)):
                tf[t] += w
        tfs.append(tf)
        lens.append(sum(tf.values()))
        for t in set(tf):
            df[t] += 1
    N = len(rows)
    avg = sum(lens) / max(N, 1)
    qlow = query.lower().strip()
    out = []
    for r, tf, L in zip(rows, tfs, lens):
        s = 0.0
        hit = 0
        for t in q:
            if t not in tf:
                continue
            hit += 1
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            f = tf[t]
            s += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * L / avg))
        if not hit:
            continue
        if len(q) > 1:
            s *= 0.6 + 0.4 * hit / len(q)          # reward covering more query terms
        if qlow in r["title"].lower():
            s *= 1.6
        elif len(qlow) > 6 and qlow in (doc_text(r, "detail") + doc_text(r, "steps")).lower():
            s *= 1.2
        s *= {3: 1.15, 2: 1.0, 1: 0.85}.get(r.get("importance", 2), 1.0)
        out.append((s, r))
    out.sort(key=lambda x: -x[0])
    return out

def stars(r):
    return {3: "***", 2: "** ", 1: "*  "}.get(r.get("importance", 2), "   ")

def apply_line(r):
    imp = r.get("implication") or r.get("implication_universal") or ""
    imp = re.sub(r"^David should", "You should", imp.strip())
    return imp

def clip(s, n):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"

def one_line(r, snippet=True, width=170):
    head = "%-7s %s %s  [%s · src %s]" % (r["id"], stars(r), r["title"], r["theme"], r["sid"])
    if not snippet:
        return head
    a = apply_line(r) or r.get("pitfall") or r.get("detail", "")
    return head + "\n        ↳ " + clip(a, width)

def filt(rows, args):
    if getattr(args, "theme", None):
        want = [t.lower() for t in args.theme]
        rows = [r for r in rows if any(w in r["theme"].lower() for w in want)]
        matched = sorted({r["theme"] for r in rows})
        if not matched:
            print("!! no theme matches %s — run `kb.py theme` for the list." % ", ".join(repr(t) for t in args.theme))
        elif len(matched) > 1:
            print("themes matched: %s" % ", ".join(matched))
    if getattr(args, "core", False):
        rows = [r for r in rows if r.get("importance") == 3]
    if getattr(args, "source", None):
        rows = [r for r in rows if r["sid"] == args.source.zfill(2)]
    return rows

def cmd_search(args):
    rows, _ = load()
    rows = filt(rows, args)
    hits = bm25(rows, args.query)
    if not hits:
        print("no hits — try fewer or different words, or `kb.py theme` to browse.")
        return
    for s, r in hits[: args.limit]:
        print(one_line(r, snippet=not args.titles))
    if len(hits) > args.limit:
        print("(%d more hits — raise -n or narrow with --theme/--core)" % (len(hits) - args.limit))
    print("\nnext: kb.py show <id> [--brief] for the procedure.")

# ------------------------------------------------------------------ show
def render(r, brief=False):
    L = []
    tag = " · universal-edition only" if r.get("edition") == "universal" else ""
    L.append("### %s — %s" % (r["id"], r["title"]))
    L.append("*%s · %s · %s · source %s: %s%s*" % (
        {3: "core", 2: "useful", 1: "context"}.get(r.get("importance", 2), "useful"),
        r["theme"], (r.get("category") or "").replace("-", " "), r["sid"],
        clip(r.get("source_title", ""), 70), tag))
    L.append("")
    if brief:
        L.append(clip(r.get("detail", ""), 320))
        L.append("")
        if not r.get("pitfall") and not r.get("implication") and r.get("steps"):
            L.append("**First step:** " + r["steps"][0].strip())
            L.append("")
    else:
        L.append(r.get("detail", "").strip())
        L.append("")
        if r.get("quote"):
            L.append('> "%s"' % r["quote"].strip().strip('"'))
            L.append("")
        if r.get("evidence"):
            L.append("**Evidence:** " + r["evidence"].strip())
            L.append("")
        if r.get("steps"):
            L.append("**How to do it**")
            L.append("")
            for j, s in enumerate(r["steps"], 1):
                L.append("%d. %s" % (j, s.strip()))
            L.append("")
        if r.get("tools"):
            L.append("**Tools:** " + ", ".join(r["tools"]))
            L.append("")
        if r.get("prompt"):
            L.append("**Prompt / template:**\n\n```text\n%s\n```\n" % r["prompt"].strip())
    if r.get("pitfall"):
        L.append("**Pitfall:** " + r["pitfall"].strip())
        L.append("")
    imp_p, imp_u = r.get("implication"), r.get("implication_universal")
    if imp_p and imp_u:
        L.append("**Apply at Pabau:** " + imp_p.strip())
        L.append("")
        L.append("**Apply anywhere:** " + imp_u.strip())
    elif imp_p or imp_u:
        L.append("**Apply:** " + apply_line(r))
    while L and L[-1] == "":
        L.pop()
    L.append("")
    L.append("Transcript: %s/%s (lines %s)" % (CFG["transcripts_md"], r.get("source_file", ""),
             "-".join(str(x) for x in (r.get("lines") or [])) or "?"))
    return "\n".join(L)

def resolve(rows, key):
    key = key.strip()
    m = re.match(r"^(\d{1,2})([.:].*)$", key)
    if m:
        key = m.group(1).zfill(2) + m.group(2)
    exact = [r for r in rows if r["id"] == key or r["uid"] == key]
    if exact:
        return exact
    if ":" in key:                       # NN:fragment — any insight of source NN whose slug contains it
        sid, frag = key.split(":", 1)
        sid = sid.zfill(2)
        return [r for r in rows if r["sid"] == sid and frag.lower() in r["uid"]]
    return [r for r in rows if r["id"].startswith(key + ".")]

def cmd_show(args):
    rows, _ = load()
    for k in args.ids:
        m = resolve(rows, k)
        if not m:
            print("!! no insight matches %r" % k)
        elif len(m) > 1 and not k.replace(".", "").isdigit():
            print("!! %r is ambiguous (%d matches):" % (k, len(m)))
            for r in m[:12]:
                print("   " + one_line(r, snippet=False))
        else:
            for r in m:
                print(render(r, brief=args.brief))
                print()

# ------------------------------------------------------------------ browse
def cmd_theme(args):
    rows, _ = load()
    if not args.name:
        c = collections.Counter(r["theme"] for r in rows)
        cc = collections.Counter(r["theme"] for r in rows if r.get("importance") == 3)
        print("%-30s %5s %5s" % ("theme", "all", "core"))
        for t, n in c.most_common():
            print("%-30s %5d %5d" % (t, n, cc[t]))
        return
    args.theme = [args.name]
    rows = filt(rows, args)
    if not rows:
        return
    rows.sort(key=lambda r: (-r.get("importance", 2), r["title"]))
    print("%d insights · %s" % (len(rows), ", ".join(sorted({r["theme"] for r in rows}))))
    for r in rows:
        print(one_line(r, snippet=False))

def cmd_source(args):
    rows, sources = load()
    if not args.nn:
        cnt = collections.Counter(r["sid"] for r in rows)
        for s in sources:
            print("%s  %-70s %3d  %s" % (s["id"], clip(s["title"], 70), cnt.get(s["id"], 0), s.get("type", "")))
        return
    nn = args.nn.zfill(2)
    s = next((x for x in sources if x["id"] == nn), None)
    if not s:
        print("no source", nn)
        return
    print("%s — %s\n%s\ntype: %s · transcript: %s/%s\n" % (s["id"], s["title"], s.get("source", ""),
          s.get("type", ""), CFG["transcripts_md"], s.get("file", "")))
    for r in [r for r in rows if r["sid"] == nn]:
        print(one_line(r, snippet=False))

def cmd_grep(args):
    rows, _ = load()
    try:
        rx = re.compile(args.pattern, re.I)
    except re.error as err:
        print("!! bad regex: %s" % err)
        return
    n = 0
    for r in rows:
        blob = r["title"] if args.titles_only else " ".join(
            doc_text(r, f) for f, _ in FIELDS)
        if rx.search(blob):
            n += 1
            if n <= args.limit:
                print(one_line(r, snippet=False))
    if n > args.limit:
        print("(%d more — narrow the pattern or raise -n)" % (n - args.limit))
    if not n:
        print("no matches")

def cmd_stats(args):
    rows, sources = load()
    print("%s: %d insights · %d sources · %d universal-only extras" % (
        CFG["label"], len(rows), len(sources), sum(1 for r in rows if r.get("edition") == "universal")))
    print("core %d · useful %d · context %d" % tuple(
        sum(1 for r in rows if r.get("importance") == k) for k in (3, 2, 1)))

# ------------------------------------------------------------------ main
def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("search"); a.add_argument("query"); a.add_argument("-n", "--limit", type=int, default=10)
    a.add_argument("--theme", action="append"); a.add_argument("--core", action="store_true")
    a.add_argument("--source"); a.add_argument("--titles", action="store_true"); a.set_defaults(fn=cmd_search)
    a = sp.add_parser("show"); a.add_argument("ids", nargs="+"); a.add_argument("--brief", action="store_true"); a.set_defaults(fn=cmd_show)
    a = sp.add_parser("theme"); a.add_argument("name", nargs="?"); a.add_argument("--core", action="store_true"); a.set_defaults(fn=cmd_theme)
    a = sp.add_parser("source"); a.add_argument("nn", nargs="?"); a.set_defaults(fn=cmd_source)
    a = sp.add_parser("grep"); a.add_argument("pattern"); a.add_argument("--titles-only", action="store_true")
    a.add_argument("-n", "--limit", type=int, default=40); a.set_defaults(fn=cmd_grep)
    a = sp.add_parser("stats"); a.set_defaults(fn=cmd_stats)
    args = p.parse_args()
    args.fn(args)

if __name__ == "__main__":
    main()
