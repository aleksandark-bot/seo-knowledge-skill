# Internal Linking — supporting

8 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Automate internal linking with Link Whisper on every new post  `07.14`
*useful · best practices · source 07*

Internal linking is framed as commonly neglected despite driving concrete benefits: better crawlability/indexation for AI and traditional search engines, easier navigation for users and crawlers, faster indexing of brand-new pages (since they get discovered via links from already-indexed pages), and authority flow to deeper pages (authority diminishes the deeper a page sits in the link structure). The recommended ongoing mechanism is the WordPress plugin Link Whisper, which reads Google Search Console data and automatically proposes internal links every time a new post is published, removing the need to manually remember every linking opportunity. As a secondary mechanism, an AI content tool with a populated 'writer' knowledge base (site pages, tone of voice, offer details) can insert correct internal links automatically as it drafts new articles. The standing rule of thumb: any time you publish a subtopic post, link it back to the relevant main service/money page wherever it makes sense.

> "will do internal linking for you by looking at data"

**How to do it**

1. Install the Link Whisper plugin on your WordPress site.
2. Connect/authorize Link Whisper to your Google Search Console property so its suggestions are based on real query and landing-page data.
3. Every time you publish a new post, run Link Whisper's scan on it and review the internal link suggestions it generates.
4. Manually confirm each suggested link is contextually relevant before accepting it — don't accept all suggestions automatically.
5. For every new subtopic blog post, add at least one contextual link back to the relevant main service/money page.
6. If using an AI writing tool with a knowledge-base feature, populate its site-pages, tone-of-voice, and offer-details fields once so future AI-drafted articles auto-insert correct internal links.
7. Periodically audit older or deeply-nested pages to confirm they're still receiving some internal links, since link depth affects how much authority a page receives. (inferred)

**Tools:** Link Whisper, WordPress, Google Search Console, Datawise

**Pitfall:** Skipping internal linking because it feels less important than writing content or building backlinks — the creator calls it 'something really important that a lot of people miss out on,' directly affecting crawlability, new-page indexing speed, and authority distribution to deeper pages.

### 2. In low-engagement niches, blog posts can function as pure link vehicles  `08.15`
*useful · content insights · source 08*

Blog posts in the home-services niche are described as effectively unread by real people ('no one's reading the post, sadly') yet are still produced in batches (e.g., 40 at a time, with images generated for each) purely because they carry internal links that redistribute ranking authority to money pages. This is presented matter-of-factly as the actual value proposition of that content in that specific context, not as a shortcoming to fix. It stands in direct tension with content strategies built around getting cited/mentioned by AI systems (which require genuinely useful, well-cited content), highlighting that 'why we publish this content' can differ sharply by niche and business model.

> "the internal links that shoot rankings up on the pages"

**Evidence:** Direct claim: 'No one's reading the post, sadly — they're not that important to the public, but they have the internal links that shoot rankings up on the pages,' describing blog posts published in batches of roughly 40 purely for their internal-linking value.

**Apply at Pabau:** This is a useful counter-data-point when weighing content investment, but it should not be read as a model to emulate for Pabau — Pabau's GEO strategy explicitly depends on content that does get read, cited, and mentioned by AI systems (content capsules, sourcing, E-E-A-T), so treat 'content as pure link plumbing' as the low floor this creator settles for in a low-differentiation niche, not a target to aim for.

**Apply anywhere:** This is a useful counter-data-point when weighing content investment, but it should not be read as a model to emulate for your own site — your GEO strategy explicitly depends on content that does get read, cited, and mentioned by AI systems (content capsules, sourcing, E-E-A-T), so treat 'content as pure link plumbing' as the low floor this creator settles for in a low-differentiation niche, not a target to aim for.

### 3. Link every new post to product pages and audit for orphans as volume grows  `121.14`
*useful · best practices · source 121*

Grow and Convert's internal linking rule for a SaaS blog has two halves, and most teams only do the second. The first is that every new post should link to your most important pages, which they name as product pages, cornerstone content and high-converting articles, so authority flows toward the pages that make money. The second is an ongoing audit that valuable pages are not orphaned with no internal links pointing to them at all. They add that as content volume grows you should go back to older posts and add links to newer, relevant content, which distributes authority across the site and helps newer posts gain traction faster. The context is a static marketing site where nobody owns the link graph, so orphans accumulate quietly rather than appearing all at once.

> "making sure valuable pages aren't orphaned"

**Evidence:** Grow and Convert's technical checklist for SaaS marketing sites, where relatively static sites accumulate orphaned pages as the blog grows.

**How to do it**

1. Name your money pages explicitly: product pages, cornerstone guides, and the articles that already convert.
2. Require at least one link from every new post to a page on that list, placed in body copy rather than a footer block.
3. Crawl the site quarterly with Screaming Frog and filter for pages with zero inbound internal links.
4. Fix each orphan by adding links from the two or three existing posts closest in topic.
5. When publishing a new article, search the site for older posts covering the same topic and add a link from each.
6. Keep the in-body link count restrained so authority is not split across dozens of destinations per page.
7. Re-crawl after each batch to confirm the new links are being found, not buried in JavaScript-rendered navigation.

**Tools:** Screaming Frog

**Pitfall:** Relying on a related-posts widget for internal links. Widgets are often JavaScript-rendered and topic-agnostic, so the pages you care about stay effectively orphaned while the crawl looks healthy.

**Apply at Pabau:** Every new Pabau article should carry a body link to a relevant feature or template page, and David should run a quarterly orphan crawl since pabau.com's older articles predate the current page set.

**Apply anywhere:** Make every new post link to your product and cornerstone pages, and crawl quarterly for pages with no inbound internal links at all.

### 4. Make a habit of adding links from old posts to each new article  `108.23`
*useful · concrete actions · source 108*

Grow and Convert list internal linking under technical SEO and call it one of the most overlooked aspects and one of the easiest to fix. Two instructions come out of it. First, link from newer blog posts to your most important pages: product pages, pillar content and high-converting articles, and make sure no valuable page is orphaned with no internal links pointing at it. Second, and the part teams skip, develop a habit of going back to older posts and adding links to newer relevant content as the library grows. They say this distributes authority through the site and can give newer posts a ranking boost. The second direction is the one that never happens by default, because the natural workflow only adds links forward in time, leaving every new article dependent on the handful of links it can earn externally.

> "develop a habit of going back to older posts"

**Evidence:** Grow and Convert's stated effect: adding links from older posts distributes authority through the site and can give newer posts a ranking boost.

**How to do it**

1. Crawl the site and list every page with zero internal inbound links.
2. Fix the orphans first by linking to them from the closest topical pages.
3. For each newly published article, search your own site for the target keyword and its close variants.
4. Pick three to five older posts that already rank and add a contextual link into the new article.
5. Prefer linking from pages that already rank, since a page that does not rank passes little authority.
6. Use descriptive anchors that describe the destination, and do not reuse the same anchor more than three times per article.
7. Add the backward-linking task to the publication checklist so it runs at publish time, not in a quarterly cleanup.
8. Recheck the new article's position four to six weeks later to see whether the links moved it.

**Tools:** Screaming Frog, Google Search Console

**Pitfall:** Only ever linking forward from new posts to old ones. New articles then launch with no internal authority, and the fix gets deferred to a site-wide audit that never gets scheduled.

**Apply at Pabau:** Pabau's publication checklist should include a step that finds three to five existing ranking articles and adds a contextual link into the new page, alongside the Continue your research block, which links outward rather than inward.

**Apply anywhere:** Add a step at publish time that finds three to five older, already-ranking posts and links them to the new article. Fix orphan pages first, and use descriptive anchors rather than repeating one phrase.

### 5. Orphaned pages may keep ranking once already indexed  `53.8`
*useful · content insights · source 53*

David Quaid raises an exploratory claim that runs counter to the standard assumption that every page must stay linked to avoid losing rankings: he says he has personally observed orphan pages, pages with no remaining internal links pointing to them, continue to rank, and even stay ranking. His reasoning is that internal linking's main purpose is to help spiders discover a page in the first place; once a page is already discovered and indexed, removing its internal links doesn't necessarily undo that indexed status, unless the page enters a competitive rotation phase where ongoing authority support matters more. He is explicit that this is not a settled rule — he flags it as something he'd need to test further rather than a confirmed, general finding.

> "I have seen orphan pages rank, yes, and stay ranking"

**Evidence:** David Quaid's direct, self-qualified claim: "I have seen orphan pages rank, yes, and stay ranking," reasoned from interlinking's core purpose being spider discovery rather than sustained ranking support, immediately followed by his own caveat that he'd need to test it.

**Apply:** Before assuming a page will lose its ranking the moment you remove its last internal link, e.g., while reallocating links via the corner-stoning tactic, check whether that page is in a stable position or a competitive rotation phase, and treat orphaning a low-competition, already-ranking page as a lower-risk move than the conventional wisdom suggests, while still verifying the outcome yourself, since even the source treats this as unconfirmed.

### 6. Rank a tiny micro-app using only your own domain's authority  `48.6`
*useful · content insights · source 48*

As a contrasting, lower-effort pattern to the viral-sharing model, the source references a case, Matt Diamante, discussed in full on a separate linked episode, of ranking a "35-word web app" at position one on Google without doing meaningful on-page SEO work. The only lever used was linking to the tiny web app from an existing, already-authoritative owned domain, his agency's website, suggesting that for a sufficiently narrow, well-matched micro-tool, borrowed authority from one link on your own high-authority domain can be enough to rank it, without needing the asset to go viral or attract third-party backlinks at all.

> "ranked number one on Google with a 35-word web app doing like"

**Evidence:** The source's summary of a separate case study: a "35-word web app" reached the number one Google ranking with "like no SEO," achieved solely by linking to it from the creator's existing agency domain and website.

**Apply at Pabau:** For narrow, low-competition micro-tool ideas relevant to Pabau, e.g., a simple appointment-no-show cost calculator, David could test ranking them purely via a single strong internal link from an already-authoritative Pabau page, rather than assuming every linkable asset needs to achieve viral, third-party backlink pickup to succeed.

**Apply anywhere:** For narrow, low-competition micro-tool ideas in your niche, such as a simple single-number cost calculator, you could test ranking them purely via a single strong internal link from an already-authoritative page of your own, rather than assuming every linkable asset needs viral third-party backlink pickup to succeed.

### 7. Session recordings show users enter mid-site, not the homepage  `16.12`
*useful · content insights · source 16*

Reviewing session-recording tool (Clarity) journeys, the speakers observe that visitors typically land directly on whatever specific page solves their problem rather than the homepage — reinforcing that a page targeted at solving one specific problem is what earns it relevance and ranking in the first place. On those landing pages, the recorded failure pattern is: the visitor scrolls the navigation up and down quickly, doesn't find what they need next, then clicks back to Google to search again, and that "pogo-sticking" back to Google is itself treated as a negative signal. Separately, when Clarity shows the same visitor returning in a later session, the cause is often not genuine multi-session research behavior but simply that the navigation or internal links failed to get them to the next thing they needed the first time.

> "people come in not on the homepage but on the page that's"

**Evidence:** Direct description of a recurring Clarity session-recording pattern: visitors land on the specific solving page (not the homepage), scroll the nav without finding a next step, then exit back to Google; return visits in Clarity are attributed to that same navigation/internal-linking failure rather than intentional research revisits.

**Apply:** When reviewing Clarity (or equivalent) recordings for high-traffic landing pages, specifically flag sessions where a visitor scrolls the navigation without clicking anything before leaving — that pattern pinpoints a missing internal link or next-step CTA on that exact page, a more targeted fix than a general navigation or IA redesign.

### 8. Stop over-linking once a page stabilizes; redirect equity to the next page  `51.4`
*useful · best practices · source 51*

Edward's internal-linking refinement (referencing his own earlier episode on internal linking) is that once a target page's rankings have stabilized at a consistently high position, with little fluctuation for its target keyword, you no longer need to keep pouring additional internal links into it from every other ranking page, as long as it isn't left as an orphan page. Instead, you redirect a stabilized page's own link equity toward a different, newer page that still needs help ranking, effectively graduating pages as they stabilize so each newly-ranking page becomes a fresh source to expand from. He describes this as a compounding, colony-like expansion model: every SEO page that ranks with satisfied clicks becomes its own colony to expand outward from, similar to a real-time-strategy game or the board game Risk.

> "Each SEO page that is ranking with satisfied clicks becomes a colony"

**How to do it**

1. For each internally-linked target page, track its ranking position over time in a rank tracker to determine when it has stabilized (little to no fluctuation at a high position for its target keyword).
2. Once a target page is confirmed stable, stop directing additional new internal links from other ranking pages toward it, as long as it still has at least one inbound internal link so it is not orphaned.
3. Identify a different, newer page on the site that still needs ranking help.
4. Redirect the internal-linking effort from your ranking PAA/FAQ pages toward that newer page instead.
5. Once that page's rankings stabilize with a good click-through rate and low pogo-sticking, treat it as a new 'colony' page and repeat the process, continually rotating link equity toward whichever page currently needs it most.

**Tools:** a rank tracker
