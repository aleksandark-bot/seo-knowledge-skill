#!/usr/bin/env python3
"""Ahrefs free Domain Rating API client (APIv3 public endpoints, free since Jun 2026).

Key: a free APIv3 key from a free Ahrefs account (Account settings -> API keys),
stored as AHREFS_API_KEY in ~/.pabau-ahrefs/.env or exported in the shell.
Keyless calls are dead: no key -> 403 Forbidden, bad key -> 401 (verified 29 Sep 2026).

The SEO-knowledge skill's one source for a site's DR: never estimate it or substitute
another vendor's authority score.

Usage:
  ahrefs_dr.py check                       # verify the key works (DR of ahrefs.com)
  ahrefs_dr.py dr pabau.com zenoti.com     # DR for one or more domains/URLs
  ahrefs_dr.py dr -f domains.txt --csv     # one target per line, CSV to stdout
  ahrefs_dr.py top --from 1 --to 100       # top domains by DR (max 250k rows/request)

Attribution: any published use must credit "Domain Rating by Ahrefs" with a link to
ahrefs.com (https://ahrefs.com/legal/domain-rating-license).
"""
import argparse, csv, json, os, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

BASE = "https://api.ahrefs.com/v3/public"
ENV_FILE = Path.home() / ".pabau-ahrefs" / ".env"


def api_key():
    key = os.environ.get("AHREFS_API_KEY")
    if not key and ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.strip().startswith("AHREFS_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"\'')
    if not key:
        sys.exit(f"No AHREFS_API_KEY. Put it in {ENV_FILE} (AHREFS_API_KEY=...) or export it.")
    return key


def get(path, params, key, retries=4):
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}",
                                               "Accept": "application/json",
                                               "User-Agent": "seo-knowledge-ahrefs-dr/1.0"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")[:300]
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt * 2)
                continue
            raise SystemExit(f"HTTP {e.code} for {params}: {body}")


def domain_rating(target, key):
    res = get("domain-rating-free", {"target": target, "output": "json"}, key)
    return res["domain_rating"]["domain_rating"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    p_dr = sub.add_parser("dr")
    p_dr.add_argument("targets", nargs="*")
    p_dr.add_argument("-f", "--file")
    p_dr.add_argument("--csv", action="store_true")
    p_top = sub.add_parser("top")
    p_top.add_argument("--from", dest="frm", type=int, default=1)
    p_top.add_argument("--to", type=int, default=100)
    a = ap.parse_args()
    key = api_key()

    if a.cmd == "check":
        print(f"OK - ahrefs.com DR {domain_rating('ahrefs.com', key)}")
    elif a.cmd == "dr":
        targets = list(a.targets)
        if a.file:
            targets += [l.strip() for l in Path(a.file).read_text().splitlines() if l.strip()]
        if not targets:
            sys.exit("Give targets or -f file.")
        w = csv.writer(sys.stdout) if a.csv else None
        if w:
            w.writerow(["target", "domain_rating"])
        for t in targets:
            dr = domain_rating(t, key)
            w.writerow([t, dr]) if w else print(f"{t}\t{dr}")
    elif a.cmd == "top":
        res = get("domain-rating-top-domains", {"from": a.frm, "to": a.to, "output": "json"}, key)
        w = csv.writer(sys.stdout)
        w.writerow(["rank", "domain", "domain_rating"])
        for d in res["domains"]:
            w.writerow([d["rank"], d["domain"], d["domain_rating"]])


if __name__ == "__main__":
    main()
