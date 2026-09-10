# SEO-knowledge — a Claude Code skill

2,400+ SEO insights mined from 180+ practitioner sources (talks, podcasts, videos, articles),
each with the mechanism, the evidence, the step-by-step, the tools, the exact prompts and the
pitfall. Claude queries it on demand instead of reading it, so a task costs a few thousand
tokens of retrieval.

## Install

```bash
git clone https://github.com/aleksandark-bot/seo-knowledge-skill.git ~/.claude/skills/SEO-knowledge
```

Then restart Claude Code. The skill appears as **SEO-knowledge**; Claude picks it up for any
SEO-shaped task. To make it fire every time, add to your `~/.claude/CLAUDE.md`:

> Invoke the **SEO-knowledge** skill at the start of any SEO-related task, before planning
> or writing anything. Query it with its `scripts/kb.py`, never by reading whole reference files.

## Update

```bash
git -C ~/.claude/skills/SEO-knowledge pull
```

`install.sh` in this repo does clone-or-pull for you. The repo is republished automatically
whenever the base gains new sources, so a pull always gets the latest doctrine and insights.

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
