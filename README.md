# SEO-knowledge — a Claude Code skill

2,400+ SEO insights mined from 180+ practitioner sources (talks, podcasts, videos, articles),
each with the mechanism, the evidence, the step-by-step, the tools, the exact prompts and the
pitfall. Claude queries it on demand instead of reading it, so a task costs a few thousand
tokens of retrieval.

## Install

**The normal route: the factcheck-flow install command David sends the team.** It installs
this skill alongside /fact and /SEO, and its auto-updater then keeps the skill current on
its own — at most once an hour, when Claude Code starts. Nothing else to run.

On its own, with the read token David gives out (needed once this repo is private):

```bash
export PABAU_REPO_TOKEN=<token>
curl -fsSL -H "Authorization: Bearer $PABAU_REPO_TOKEN" -H "Accept: application/vnd.github.raw" \
  https://api.github.com/repos/aleksandark-bot/seo-knowledge-skill/contents/install.sh \
  -o /tmp/sk-install.sh && bash /tmp/sk-install.sh
```

`install.sh` clones the repo to `~/.claude/skills/SEO-knowledge`, or fast-forwards an existing
clone. It reads the token from `$PABAU_REPO_TOKEN`, else from
`~/.claude/factcheck-flow/.repo-token` (where the factcheck-flow installer saves it), and
sends it as a one-off header, so it is never written into the clone's `.git/config`. While
the repo is public, a plain `git clone https://github.com/aleksandark-bot/seo-knowledge-skill.git ~/.claude/skills/SEO-knowledge`
also works.

Then restart Claude Code. The skill appears as **SEO-knowledge**; Claude picks it up for any
SEO-shaped task. To make it fire every time, add to your `~/.claude/CLAUDE.md`:

> Invoke the **SEO-knowledge** skill at the start of any SEO-related task, before planning
> or writing anything. Query it with its `scripts/kb.py`, never by reading whole reference files.

## Update

Automatic if you installed factcheck-flow: its session-start updater fast-forwards this clone
at most hourly. It never touches a clone with local changes or unpushed commits. By hand, run
`install.sh` again (`bash ~/.claude/skills/SEO-knowledge/install.sh`); it picks up the saved
token the same way. The repo is republished automatically whenever the base gains new
sources, so an update always gets the latest doctrine and insights.

## Using it by hand

```bash
KB=~/.claude/skills/SEO-knowledge/scripts/kb.py
python3 $KB search "crawled currently not indexed" -n 10     # ranked hits, one line + apply snippet
python3 $KB search "anchor text" --theme "internal linking" --core
python3 $KB show 10.12                                       # the full write-up
python3 $KB show 10.12 53.9 --brief                          # title, gist, apply, pitfall
python3 $KB theme                                            # themes with counts
python3 $KB source 74                                        # one source, its URL and insights
python3 $KB grep "striking distance"
```

Python 3 only, no dependencies.

## What is in here

| Path | What |
|---|---|
| `SKILL.md` | The instructions Claude loads: a short doctrine of load-bearing rules plus the retrieval protocol |
| `scripts/kb.py` | The query tool |
| `data/insights.jsonl` | Every insight, one per line (generated) |
| `data/sources.json`, `references/sources.md` | The sources with URLs (generated) |
| `references/full/*.md` | Whole-theme write-ups for a deliberate deep read (generated) |
| `scripts/build.py`, `scripts/config.json` | Maintainer-only: regenerate from the private base |

Insights carry two "apply" lines where they differ: **Apply at Pabau** (the base is maintained
by Pabau's content team) and **Apply anywhere** (vendor-neutral). Transcript paths printed by
`show` point at the maintainer's local copies; the source URL from `kb.py source NN` is the
public reference.
