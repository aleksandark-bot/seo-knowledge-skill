---
name: SEO-knowledge
description: The distilled SEO knowledge base — 2,491 insights from 181 practitioner sources (talks, podcasts, videos, articles), covering keyword research, on-page and content strategy, technical SEO, migrations, internal linking, link building, digital PR, AI visibility / GEO, GSC measurement, local, programmatic, e-commerce, video, conversion, content-team hiring and outsourcing, attribution and CAC, positioning, and team ops. Read this skill for ANY SEO-related task — keyword research or selection, content briefs and outlines, writing or refreshing an article for search, on-page optimization, title/meta work, technical or on-page audits, indexing and crawl problems, migrations and redirects, cannibalization, internal-link planning, backlink or PR strategy, AI Overview / AI Mode / LLM citation work, GSC or rank analysis, local SEO and GBP, programmatic SEO, SERP or competitor analysis, or any question about how ranking works.
---

# SEO knowledge base

2,491 insights mined from 181 primary sources and written up with the mechanism, the
evidence, the step-by-step, the tools, the exact prompts and the pitfall. Both editions
of the underlying knowledge base are folded in: the Pabau-tailored one and the
vendor-neutral "SEO Playbook". Where the two differ in what to *do*, the insight carries
both — **Apply at Pabau** and **Apply anywhere**.

## How to use this skill (read this — it is what keeps the skill cheap)

The base is far too big to read. **Never open a whole theme file.** Query it:

```bash
KB=~/.claude/skills/SEO-knowledge/scripts/kb.py
python3 $KB search "<what the task is about>" -n 10        # ranked hits, one line + apply snippet each
python3 $KB search "<query>" --theme "<theme>" --core      # narrow: theme substring, core-only
python3 $KB show 53.12 74.3 --brief                        # title + apply + pitfall (~150 tokens each)
python3 $KB show 53.12                                     # the full write-up: steps, tools, prompt, evidence
python3 $KB theme "<theme>"                                # every title in a theme, one line each
python3 $KB grep "<regex>"                                 # exact term across titles and bodies
python3 $KB source 74                                      # one source's title, URL and insights
```

Protocol for a task:
1. **Read the doctrine below first.** For most questions it already holds the answer.
2. **Run 1–3 searches** phrased as the problem ("title query mismatch striking distance"),
   then `--theme`/`--core` to narrow. Read the snippets; they name the rule and the source.
3. **`show --brief` the 3–8 insights you will act on.** Escalate to full `show` only
   when you need the steps, the prompt or the numbers — that is where the specificity
   lives, so never answer a how-to from memory when a hit covers it.
4. **Cite as "source NN"** (`kb.py source NN` gives title + URL). Load-bearing claims can
   be checked in the transcript path each `show` prints.

Budget: about 3K tokens of retrieval per task is normal; 10K is a deep dive. `references/full/`
holds whole-theme files (40–75 KB each) for a deliberate end-to-end read of a *small*
theme only — check the size first, and never for content quality, content production,
keyword research or strategy. Insights are marked **core** (act on it, `***`), **useful**
(`**`), or **context** (`*`); ids are `NN.k` (source NN, k-th insight).

**A site's Domain Rating: always the Ahrefs API.** Whenever a task needs DR (link or PR
prospects, competitor or SERP strength, a velocity forecast), fetch it live:
`python3 ~/.claude/skills/SEO-knowledge/scripts/ahrefs_dr.py dr a.com b.com` (`-f list.txt --csv`
for bulk). Never estimate DR, quote it from memory or a source, or swap in DataForSEO rank or
Semrush Authority Score. On a key error, stop and say so (setup: README). The doctrine still
decides how much DR counts. Anything published credits "Domain Rating by Ahrefs", linked to ahrefs.com.

This skill is knowledge, not house style. It does **not** replace the Pabau content
guides in `~/.claude/factcheck-flow/guides/` — those own voice, block markup, visuals
and the Pabau facts, and they still win on any conflict about *how Pabau content is
written*. This skill decides *what to do for search*. Nor does it replace `/SEO` and
`/fact`; it is the reasoning those commands should draw on. Its sibling
**Editorial-knowledge** holds the same content-quality / production / conversion /
team insights on their own, for tasks that are editorial rather than search-driven.

## The doctrine

**Ranking model**
- Ranking reduces to relevance plus authority, and relevance is measured as distance in
  vector space, strictly linearly — Google does not make associative leaps for you.
- PageRank is per-topic now, not one global number, and Google's index is stratified into
  authority tiers that decide crawl priority and re-index speed.
- Third-party DA/DR are entertainment metrics *as a quality signal*. Judge any page —
  yours or a link target's — by whether it ranks and whether it passes real traffic.
  Grow & Convert (153, 141) keep DR as a *velocity* forecast only: their 40-client data
  splits at DR 50, and low DR delays a ranking without capping it. Never a threshold.
- Cost of retrieval is real: quality alone does not earn ranking if crawling and serving
  the page costs more than the click is worth.
- Google runs CTR competitions and actively tests new pages (base rank vs test rank) for
  roughly two weeks; do not read a fresh position as settled.

**Content**
- Match intent before anything else. Front-load the exact keyword in title, URL, H1 and
  the first sentence, then answer the query in the first sentence or two. Answering late
  causes pogo-sticking, and pogo-sticking — not AI detection — is why AI content dies.
- Google penalizes thin content, not AI-written content — but "thin" is contested.
  David Quaid (74), reading Google's own starter guide, says thin content is not a real
  thing: no minimum word count exists, and what gets called a thin-content penalty is
  cannibalization from slug/title/H1 overlap. Grow & Convert (97, 99) blame content that
  is *undifferentiated*, not short. Treat length as a non-signal; diagnose overlap and
  sameness instead. But unedited scaled AI output
  produces the "Mount AI" curve every time: fast rankings, then a crash below baseline.
  Ceiling is 50–100 articles a month, humanized or not, and a human pass is mandatory.
- Write bottom- and middle-funnel; top-of-funnel is what AI extraction takes first. Move
  genuinely top-funnel material to Reddit, social and video instead of the blog. On a
  buying-intent page the product *is* the content — "don't be salesy" is backwards there.
  Give the product half or more of the body, with a contextual plain-text CTA written for
  that article. Fix the keyword's intent before any CRO tweak; no A/B test returns what a
  keyword swap does (143, 144, 145).
- Keep 60–70% of an article in 20–25-word capsule answers, with a TL;DR above the fold
  and the CTA directly beneath it. Write in semantic triples — name the entity, skip the
  pronoun.
- Refreshing declining pages beats publishing new ones, and unmaintained content goes to
  zero — that is the base's refresh-led majority. Grow & Convert (153) dissent on the
  *scheduled* half: update only when the keyword's intent changes or you have real news,
  because updating on a calendar does not reliably pay for itself. Both agree on
  refreshing pages that are actually declining; the disagreement is about cadence.
- Fix cannibalization before publishing more: >70% SERP overlap means merge; pick the
  winner by rank, clicks and backlinks, then 301. That governs *accidental* overlap
  already competing. Before publishing, the opposite rule applies: one valuable keyword
  gets one dedicated page (Grow & Convert, 107, 108, 115, 179). You get one title, one H1
  and one meta per page, so a bundled page reaches the top three for neither term. Their
  split test is the top-ten results — identical SERPs, one post; 3–5 shared, judge;
  different, two posts.
- **Substance comes from a recorded expert interview, not from reading the SERP.** A
  writer who researches by reading page one produces a "Google research paper": fluent,
  generic, never converts. Judge a draft on the second read — generic copy and AI output
  both read well once, and a model predicts the likeliest next token, so its arguments
  are by construction the web's average. Polish is not a quality signal (163, 164, 174, 178).

**Keywords and measurement**
- **Conversions per URL are the verdict; traffic and rank are supporting reads.** Measure
  per page, never as a blog-level blend — conversion rate tracks keyword type, not page
  design (alternatives/competitor ~8.4%, category ~4.9%, JTBD ~2.4%, top-funnel ~0.1–0.5%).
  Without page-level conversion data the only visible metric is traffic, so the strategy
  becomes a traffic strategy whatever the brief said. Report first-click as a floor
  (142, 143, 150, 151).
- Positions 2–15 first: striking-distance keywords, page-2/3 harvests, and title/query
  mismatches beat net-new targets. Grow & Convert (116) qualify the "always" — sort by
  rank *and* conversion history, and work the two proven buckets first (converters that
  slipped; top-three pages whose conversions fell). A page ranking 2–15 that never
  converted moves the total very little. A post's real footprint is its secondary-keyword
  tail, so diff today's ranked-keyword list against the best-converting month before
  touching a page that holds its target rank while results fall.
- Judge demand from several signals, not volume alone — a real customer question proves
  demand at zero volume, and CPC is the commercial-intent filter.
- Industry jargon rarely matches how customers search. Generate candidates from your own
  product copy and from what already ranks.
- GSC lags 24–72h, is a sample, hides data behind double filtering, and never separates
  AI Mode from normal search. Verify a drop across both 30- and 90-day windows before
  reacting, and check impressions before trusting an average position.

**Technical**
- Server-side 301s, no chains, relevant destination: confirmed twice not to lose
  PageRank. But bulk redirects past ~100 without mirrored URLs get devalued, and
  no-index-then-confirm-removal before 301-ing a changed slug.
- Sitemaps are a crawl-priority signal, not a control list, and never force indexing.
- "Crawled – currently not indexed" is an accessibility or duplication problem. Use
  Bing/IndexNow as a proxy signal, and republish a genuinely stuck page at a new URL.
- Migrations are the biggest single risk in the base: freeze structure and settle
  canonicalization a month out, set up every GSC property variant, warm a new domain for
  two months, and never let a domain change go unannounced.

**Links and authority**
- Relevance beats volume — three great links can outrank a thousand. Test every prospect
  with: would this link exist if Google didn't? Would it send a real visitor?
- Unlinked brand mentions now rival backlinks for visibility, and heavy brand mentions
  can outweigh the link graph. Build "mention building" as its own bucket.
- One genuinely simple interactive tool out-earns most link budgets; generic calculators
  no longer cut it. Point paid placements at the link magnet, not the money page.
- E-E-A-T in practice is the real-company footprint: transparency pages, named authors,
  external proof for every on-site claim, a consistent who/what/why repeated everywhere,
  and entity disambiguation down to a Wikidata item.
- Internal links are an expense — cap in-body links (five, two on weak sites), cap any
  anchor at three uses per article, and chain authority from pages that already rank into
  the ones that need it. A linking page only passes authority once it ranks itself.

**AI visibility / GEO**
- GEO is mostly classic SEO: owned content beats off-site mentions beats on-site tweaks,
  and on-site schema/llms.txt tweaks barely move anything. Model choice is not a strategy.
- LLMs answer with consensus, not verified truth, and within what they do pull from search
  they read roughly the first two or three pages. Rank-stacking the most-cited URLs is the
  cheapest lever and still works (page-one pages hit 77–82% mention rates, 86). But the
  ceiling is real: Grow & Convert (87), across 100 buying prompts, found only ~40% of
  ChatGPT citations appeared anywhere in ten pages of Google or Bing, and 17% of prompts
  triggered no web search at all. Chasing individual fan-out branches is impractical;
  build product-centric depth and make every mention say the same thing about you.
- **Plan for the effective prompt, not the prompt.** What the user types is that text plus
  memory, history and agent context, so most prompts have a search volume of one. Cover
  situations, never build a page to win one tracked prompt, and report AI visibility as a
  count of topics by band — a blended mentions-over-prompts percentage falls the moment
  you add an aspirational topic, punishing ambition and making the trend unreadable
  (78, 82, 83, 85, 87).
- **Under AI search a page supplies the pitch, not just the click.** Models paraphrase your
  published wording into their recommendation, so being cited is necessary and not
  sufficient — generic pages get cited and then described exactly like every rival. Write
  the sentences you want repeated back, sourced from internal interviews (81, 82, 86, 92).
- Citations are token-sampled probability, not a position you hold. Track them as prompt
  baskets by topic across engines, never as a single-prompt check.
- Comparison listicles and third-party industry sites drive most citations. Claude skews
  B2B, ChatGPT B2C. Review platforms and their rankings decide AI sentiment.
- The great decoupling is the planning assumption: impressions up, clicks down — but AI
  traffic converts 2–3× organic because it arrives pre-sold. Add citations and mentions
  as KPIs, and ask "how did you hear about us" to catch what attribution misses.

**Strategy and risk**
- Brand-first beats keyword-first long-term; branded search is the trailing indicator for
  everything you can't attribute, and a moat competitors can only rent.
- Irreplaceable value — a tool, a transaction, a service — predicts surviving updates.
- **SEO cannot fix product-market fit or positioning.** Right traffic that does not convert
  is a product or positioning signal, not a content one. Before scaling, check the company
  has closed a cold audience at least once; if it has not, run content as an asset with no
  conversion target attached (160, 181, 183).
- Scale in cycles: a few pages, get them ranking, then more. On testing cadence the base
  splits: the experimentation-led sources say log 3–4 hypotheses a month; Grow & Convert
  (175, 176) gate testing on failure instead, calling a standing quota the mechanism of
  shiny-object syndrome — you switch before the current bet has had time to work. Either
  way, design the test before spending, and write the trip-wire that would declare the
  current method broken. A tool accelerates a process that works; it never supplies one.
- Penalties only lift at the next core update. If it feels spammy, it is.
- **Gray-hat material is documented here operationally on purpose** (paid placements,
  parasite properties, link exchanges, indexing services, press-release velocity,
  subreddit farming). Treat it as intelligence: know the mechanism, name the risk,
  and don't recommend it for Pabau without saying what it costs if it goes wrong.
  Four items — fabricated/paid reviews, purchased votes, contact-form spam, manufactured
  navigation signals — are recorded as fraud with their detection signatures and the
  statute that covers them, not as playbooks. Never operationalize those.

## Themes (`--theme` takes any substring)

<!-- kb:auto:themes -->
| Theme | Insights | Core | `--theme` value |
|---|---|---|---|
| Content Quality | 362 | 204 | `content quality` |
| Content Production | 351 | 197 | `content production` |
| Keyword Research | 272 | 173 | `keyword research` |
| SEO Strategy | 263 | 115 | `seo strategy` |
| Conversion & Monetization | 227 | 124 | `conversion & monetization` |
| AI Visibility / GEO | 207 | 141 | `ai visibility / geo` |
| Measurement & GSC | 200 | 102 | `measurement & gsc` |
| Link Building | 118 | 59 | `link building` |
| Digital PR | 79 | 48 | `digital pr` |
| Technical SEO | 73 | 34 | `technical seo` |
| E-E-A-T & Authority | 66 | 33 | `eeat & authority` |
| AI Workflows & Agents | 63 | 36 | `ai workflows & agents` |
| SEO Careers & Industry | 37 | 7 | `seo careers & industry` |
| Internal Linking | 28 | 20 | `internal linking` |
| Local SEO | 23 | 10 | `local seo` |
| Programmatic SEO | 21 | 14 | `programmatic seo` |
| Site Architecture | 21 | 12 | `site architecture` |
| Video & YouTube | 20 | 11 | `video & youtube` |
| Reddit & UGC | 19 | 10 | `reddit & ugc` |
| Branded Search | 17 | 8 | `branded search` |
| SERP Features | 10 | 4 | `serp features` |
| Team & Agency Ops | 9 | 4 | `team & agency ops` |
| Ecommerce SEO | 5 | 1 | `ecommerce seo` |
<!-- /kb:auto -->

## Task → themes (use as `--theme` values)

- **Keyword research / selection** — `keyword research`, then `serp features`, `measurement & gsc`.
- **New article or brief** — `content production`, `content quality`, `keyword research`; add
  `ai visibility` if the target is an AI-cited query.
- **Refresh or rescue a declining page** — `content quality`, `measurement & gsc`, `internal linking`.
- **On-page / title / meta** — `content production`, `serp features`, `conversion`.
- **Audit or indexing problem** — `technical seo`, `site architecture`, `measurement & gsc`.
- **Migration or redirect plan** — `technical seo`, `site architecture`. Highest-risk work in the
  base: this is the one case where reading `references/full/technical-seo-core-*.md` end to end is right.
- **Cannibalization** — `content quality`, `internal linking`, `keyword research`.
- **Links / PR** — `link building`, `digital pr`, `eeat`.
- **AI Overviews, AI Mode, LLM citations** — `ai visibility`, then `eeat`, `branded search`, `video`.
- **Local / GBP** — `local seo`, then `eeat`.
- **Templates, integrations, directory-style pages at scale** — `programmatic seo`, `site architecture`, `ecommerce`.
- **Automating SEO work** — `ai workflows` (agent design, prompts, guardrails).
- **Landing pages, CTAs, forms** — `conversion & monetization`.

## Maintaining this skill

`data/`, `references/` and the table above are **generated**; SKILL.md's prose is hand-written.
Source of truth is the SEO-Insights base. After any ingest run the single command
`~/Desktop/temp/seo-universal/rebuild-all.sh` — it re-derives the Editorial split, rebuilds all
four HTML editions, both skills' data and refreshes the counts here. Never hand-edit `data/` or
`references/`. Details: `~/Desktop/temp/seo-universal/README-kb.md`.
