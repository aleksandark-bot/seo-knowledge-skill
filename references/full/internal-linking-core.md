# Internal Linking — core

20 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Cap any single anchor text at 3 uses per article  `03.10`
*core · best practices · source 03*

As a standing internal-linking rule, the same anchor text should never repeat more than three times within a single piece of main content. The stated purpose is threefold: preserving anchor diversity, strengthening contextual uniqueness, and providing clearer originality signals across the site's internal linking structure — all of which matter because internal links transfer ranking signals from outer/informational pages into core/commercial pages, and identical anchor text repeated everywhere looks templated and provides less semantic differentiation than varied, contextually-appropriate anchors.

> "avoid repeating the same anchor text more than three times"

**How to do it**

1. Before publishing or during editing, list every internal link in the article along with its anchor text.
2. Count how many times each exact anchor-text string repeats within that single piece of content.
3. Where any anchor text string appears more than three times, rewrite the third-and-beyond instances to a varied but still relevant anchor (a synonym, a longer descriptive phrase, or a related sub-topic phrase) instead of repeating the identical string.
4. Apply this cap consistently across every new article going forward as a standing editorial rule, not just as a one-time cleanup. (inferred)
5. When auditing older content for internal-linking cleanup, run the same three-repeat check retroactively and fix any article that exceeds it. (inferred: use a site crawl with anchor-text extraction, such as Screaming Frog's All Anchor Text export, to find repeats at scale)

**Tools:** Screaming Frog

### 2. Cap in-body links at five, or two on low-authority sites  `53.9`
*core · concrete actions · source 53*

David Quaid draws a sharp distinction between link placements: navigation and footer links are very, very devalued, with whatever value they do carry coming only from sheer repetition ("brute force") rather than editorial weight, so real internal-linking strategy should focus on in-body, in-content links instead. His rule of thumb there is to limit in-body links pointing at any one target to around five, meaning five blog posts each linking to a page gives it up to 25 total in-body links, but for a very low-authority site with few backlinks, he recommends trimming that down to as few as two. When reallocating links away from a page that already ranks, per the corner-stoning/malinvestment logic, he still keeps at least its least-authoritative remaining source page linking in, specifically to prevent the target from becoming a fully orphaned page and risking exit from the index.

> "my rule of thumb is to limit them to five"

**How to do it**

1. Audit a target page's inbound internal links and separate them into navigation/footer links versus in-body, in-content, links, since only in-body links are treated as carrying real weight.
2. Count the in-body links currently pointing at the target page.
3. If the site has decent authority and backlinks, cap in-body links to that target at around five sources.
4. If the site is very low authority with few backlinks, cap it lower, around two sources, instead.
5. When trimming excess in-body links from a ranking page to reallocate authority elsewhere, per the corner-stoning tactic, always leave at least one link in place, ideally from the least-authoritative remaining source page.
6. Re-check the target page's index/ranking status in Google Search Console after trimming to confirm it hasn't dropped out (inferred verification step).

**Tools:** Google Search Console

**Pitfall:** Removing every internal link to a page while reallocating authority elsewhere risks turning it into a fully orphaned page and losing it from the index — always leave at least one in-body link in place, from the least-authoritative available source page, rather than trimming to zero.

### 3. Chain harvested link authority into bottom-of-funnel landing pages  `48.2`
*core · concrete actions · source 48*

Once a linkable asset has consolidated significant backlink authority onto a page, e.g., sleepyti.me's sleep-cycle calculator redirecting to sleepopolis.com/calculators/sleep, which alone drew 35,000 backlinks from 4,500 unique domains, that page is treated as a lead magnet whose accumulated SEO authority can be deliberately funneled further into the site. The described method is to add an internal link from that authority-rich page to a valuable "hub" page, and from that hub page down into bottom-of-funnel SEO landing pages that are actually designed to bring in customers, users, or leads, deliberately routing SEO authority through a chain rather than leaving it stranded on the standalone tool page. The stated payoff is that this same chain also helps the business rank for more lucrative, competitive commercial keywords that the tool page itself was never trying to target.

> "transferring it with an internal link to a hub page"

**How to do it**

1. Identify the page where your linkable asset's backlink authority now lives, its redirect target or hosted page.
2. Identify or build a relevant hub page in the same topical area that can act as a bridge between the tool page and your commercial content.
3. Add an internal link from the linkable-asset page to that hub page.
4. On the hub page, add internal links down into your bottom-of-funnel SEO landing pages, the pages actually designed to convert visitors into customers, users, or leads.
5. Confirm in Google Search Console that the bottom-of-funnel target pages' rankings improve over time for their competitive commercial keywords, attributing gains partly to this authority chain (inferred verification step).

**Tools:** Google Search Console

**Pitfall:** Leaving a high-authority linkable-asset page as a dead end, with no internal link chain toward commercial pages, wastes most of the SEO value it generates — the authority needs to be deliberately routed to hub and bottom-of-funnel pages to convert into rankings for lucrative keywords.

### 4. Channel satisfied-click authority from ranking FAQ pages into commercial pages  `51.3`
*core · concrete actions · source 51*

Edward describes a specific mechanism for why a ranking PAA/FAQ page becomes a genuine internal-linking asset: when a page ranks and visitors are not pogo-sticking back to the search results (meaning they're satisfied with the answer), that satisfied-click behavior itself generates the page's own topical authority, independent of any backlinks it has. The concrete action is to take that self-generated authority and channel it via an internal link into bottom-of-funnel commercial landing pages (pages targeting purchase-intent keywords), because those commercial pages target searchers who are actively looking to convert but don't yet know the brand, giving them extremely high conversion rates once they can rank. His example high-intent keywords are things like 'voice note recorder for dentists,' 'handmade artisan ceramic mugs,' and 'emergency laundry and repair Boston.'

> "take this authority and channel it with an internal link"

**How to do it**

1. Monitor your published PAA/FAQ question pages in Google Search Console and a rank tracker to identify which ones are ranking well.
2. Check engagement signals (e.g., low bounce-back rate, decent time on page) as a proxy for low pogo-sticking on each ranking PAA page (inferred: via GA4 engagement metrics or GSC click trends).
3. Identify your bottom-of-funnel commercial landing pages, specifically ones targeting purchase-intent keywords where the searcher wants to convert but may not know your brand yet.
4. Add a contextual internal link from each ranking, satisfied-click PAA page to the most relevant commercial landing page.
5. Use anchor text on that internal link that reflects the commercial page's target high-intent keyword, not generic text like 'click here.'
6. Track the commercial landing page's rankings and conversion rate after adding these links to confirm the authority transfer is helping it rank and convert (inferred verification step).

**Tools:** Google Search Console, a rank tracker

### 5. Corner-stone: chain internal links from ranking pages to new ones  `53.4`
*core · concrete actions · source 53*

Once a page is ranking and earning clicks with healthy engagement, meaning visitors aren't pogo-sticking back to the search results, David Quaid says that ranking performance itself generates authority, with no backlink required. The tactic, which he calls corner-stoning, is to internal-link from that authority-generating page to a new or non-ranking page, which channels some of that authority over and can move the new page from crawled-but-not-indexed into actually ranking. Once the new page starts ranking in turn, you repeat the move, linking from it to a third page, and so on, building a chain of "assets" that each generate their own authority and can be strategically re-pointed at whichever page most needs a boost. The explicit caveat is not to overload any one ranking page with too many outgoing links at once — he compares it to a circuit with a fixed number of batteries, where each additional light dims the others, so a heavily-linked source page in a competitive, high-rotation keyword space can lose its own ranking if pushed too far; the safer pattern is securing one ranking "beachhead" before expanding further, and confirming each new target's traffic in Analytics, not just its ranking, as a secondary check.

> "take that authority and channel some of it to other pages"

**How to do it**

1. Identify a page on your site that is already ranking and getting clicks with healthy engagement (low pogo-sticking) — this is your first authority-generating asset page.
2. Add an in-body internal link from that asset page to a target page that is not yet ranking, e.g., crawled but not indexed, or ranking poorly.
3. Wait and monitor the target page in Google Search Console until it moves into indexed/ranking status.
4. Once the target page is ranking and stable, treat it as a new asset page and repeat the process: internal-link it to the next page that needs a boost.
5. Continue building this chain, asset A links to B, B links to C, and so on, creating a network of authority-generating pages you can strategically re-point at whichever page needs help.
6. Before adding another outgoing link from any asset page, check that it isn't already carrying so many outbound links that its own authority is getting diluted, applying the roughly 50-link ceiling from the expense-account rule.
7. For a competitive or highly volatile keyword, secure that page's ranking as a stable beachhead before linking out further from it, rather than expanding indefinitely at once.
8. Cross-check each target page's real-world performance in Analytics, not just its Search Console ranking, to confirm it's actually receiving traffic before treating the chain as successful.

**Tools:** Google Search Console, Google Analytics

**Pitfall:** Overloading a single ranking page with too many outgoing links dilutes the authority it can pass to any one target, like adding too many bulbs to a fixed-power circuit, and in a competitive, high-rotation keyword space this can cost the source page its own ranking rather than just weakening the boost.

### 6. Find internal link candidates with a site: plus topic search operator  `139.6`
*core · concrete actions · source 139*

Brandon's method for deciding which pages should link to which was a single Google search operator: site:[your website] + topic. Running it returns every page on the site that discusses that topic, and those pages are the ones that should be linked together. He used 'home office deduction' as the worked example. His model is the standard one, that each page holds a quantity of link value and internal links pass it, and he used the operator to concentrate that value on the pages he wanted to rank. For the '1099 tax calculator' page, which was a top converter, he pointed a large number of blog posts and pages at it, on the reasoning that a genuinely important page would be linked from many pages on the site. He calls internal linking a huge part of his success.

> "A simple way of knowing what pages should be linked together"

**Evidence:** Brandon credits internal linking as responsible for getting Keeper Tax's conversion-focused pages ranking higher, on a site that reached top 10 for 996 keywords.

**How to do it**

1. List the target pages you actually want to rank, starting with the ones that convert.
2. For each target, run site:yourdomain.com plus the topic phrase in Google.
3. Open every returned URL and confirm it genuinely discusses that topic in the body.
4. Add a contextual in-body link from each of those pages to the target page.
5. Prioritize linking from pages that already rank, since they have value to pass.
6. Point the largest number of links at the highest-converting page, such as a calculator or pricing tool.
7. Repeat the operator search after each publishing batch to catch newly eligible source pages.
8. Recheck the target page's position two to four weeks later before adding more links.

**Tools:** Google Search

**Pitfall:** The operator returns pages that merely mention the phrase in passing. Linking from those adds noise; open each result and confirm the page is about the topic before linking.

**Apply at Pabau:** Pabau should run site:pabau.com plus each core topic before publishing, and route links from the topical cluster into the money pages such as booking software and the template downloads.

**Apply anywhere:** Use a site: plus topic search to list every page on your site covering a subject, then link them all to the one page you want ranking, prioritizing sources that already rank.

### 7. Give every keyword its own page near the homepage  `41.4`
*core · concrete actions · source 41*

Edward's alternative to homepage keyword-stuffing is straightforward: give every keyword you want to rank for its own dedicated page, positioned one to two clicks away from the homepage in your site structure, rather than trying to make the homepage itself rank for it. To still pass authority to these dedicated pages without diluting the homepage, he recommends building backlinks to a hub page, such as a blog index, that internally links out to the individual keyword-targeting articles or pages; those backlinks accumulate on the hub page and then flow down through internal links to the specific pages that need the ranking boost. The same pattern applies to a services business: build backlinks to a services hub or index page, and that authority flows down to the individual dedicated service pages, which is what actually helps each specific service page rank for its corresponding keyword.

> "give dedicated pages for these keywords and have these pages"

**How to do it**

1. List every keyword or keyword cluster you currently want to rank for and confirm each has its own dedicated page, rather than being folded into homepage H1/H2 sections.
2. Position each dedicated keyword page within one to two clicks of the homepage in your site's navigation and internal linking structure.
3. Identify or create a relevant hub page for each content vertical, such as a blog index for articles or a services index page for individual service pages.
4. Internally link every dedicated keyword page from its corresponding hub page, and link the hub page prominently from the homepage.
5. When pursuing digital PR or guest-post backlinks, target the hub page, blog index or services index, as the link destination rather than always defaulting to the homepage, since the hub page then passes authority down to the individual keyword pages via internal links.
6. Continue building some backlinks directly to the homepage as well, since this approach doesn't mean abandoning homepage link building entirely, just adding hub-page and dedicated-page targets as additional destinations.
7. Periodically audit whether newly published keyword-targeting pages are within the intended one-to-two-click distance from the homepage and properly linked from their hub page (inferred).

### 8. Link to the reader's next logical step, not the homepage  `36.8`
*core · best practices · source 36*

Internal linking is commonly done wrong because people default to linking to home pages and category pages, since that feels safe, rather than linking to whatever the reader's actual next logical step should be after finishing the piece they are currently reading. The reframe offered is to think about where the reader's head is after finishing the content, not what the site's architecture looks like, meaning internal link targets should be chosen based on the reader's likely next question or action, not based on a tidy hierarchical sitemap structure.

> "Link to the next logical step for someone who just read"

**How to do it**

1. For each published article, identify what a reader would most plausibly want to know or do immediately after finishing it, such as a deeper guide, a comparison, a related tool, or a demo.
2. Link to that specific next-step page or resource directly within the body content, rather than defaulting to a link back to the relevant category or home page.
3. Avoid treating internal links as a site-map or hierarchy exercise and instead treat each link as a reader-journey decision.
4. When auditing existing content's internal links, flag any article whose primary internal links go only to home or category pages and replace at least one with a genuine next-step link. (inferred)
5. Revisit this mapping periodically as new content is published, since a better next-logical-step page may not have existed when the original article was written. (inferred)

**Pitfall:** Defaulting to home-page and category-page internal links because it feels safe, instead of linking to the specific page that matches what the reader actually wants to do next.

### 9. Migration volatility is rare (1-2%) but almost always cannibalization  `45.10`
*core · content insights · source 45*

David quantifies how often careful migrations actually go wrong: assuming URLs, content, and metadata all stay the same and only the CMS/HTML changes, major post-migration volatility happens in only about 1-2% of cases. But when it does happen, the cause is consistently the same: internal cannibalization triggered by the re-indexing process itself, not the CMS change directly. His concrete example: on a 500-page site, just three pages ended up destroying overall traffic because they started cannibalizing other pages once re-indexed, showing that even a tiny fraction of a site can cause outsized damage if those pages compete with a page that carries significant traffic, such as an 'about us' page that isn't targeting a needed keyword but ends up cannibalizing a top-traffic page anyway.

> "On a 500-page site, I've had three pages destroy traffic"

**Evidence:** Direct example: on a 500-page site, three pages destroyed overall traffic due to cannibalization triggered by re-indexing order; David's estimated overall volatility rate across his migrations is about 1-2% of cases when canonicalization and cannibalization risks are managed carefully beforehand.

**Apply:** You should treat internal-link/content overlap (cannibalization), not CMS choice or HTML changes themselves, as the actual mechanism to defend against in any Pabau migration — specifically auditing lower-profile pages like an about-us page for keyword overlap with top-traffic pages before migrating, since a tiny number of overlooked pages can offset an otherwise clean, low-volatility migration.

### 10. Only credit a linking page with authority once it ranks  `53.2`
*core · best practices · source 53*

The central myth being corrected is that any internal link from a blog post to a money page automatically helps that money page, regardless of whether the blog post itself is ranking. David Quaid's analogy is that you can't open a business account and start writing checks until your invoices land, meaning a page that isn't itself ranking has no real authority to pass on through its internal links, so linking from it isn't doing any good yet. The practical rule this produces is that a genuine SEO SOP (standard operating procedure) should include a recurring check of whether each page you're relying on as a link source is actually ranking, before crediting its outbound internal links with helping anything.

> "you can't open a business account and start writing checks until your"

**How to do it**

1. List every page that currently links internally to a target or money page you care about.
2. For each linking page, check in Google Search Console (Performance > Pages) whether that page is actually ranking and getting impressions/clicks for its own relevant queries.
3. Mark any linking page that isn't ranking as a non-contributing link source for now.
4. Prioritize getting those non-ranking linking pages to rank first, e.g., via their own on-page optimization or additional links from pages that do rank, rather than assuming their existing links to the target page are already helping.
5. Add this ranking-status check to your recurring internal-linking SOP so it's reviewed on an ongoing basis, not just once.
6. Once a linking page starts ranking, treat its outbound internal links as now genuinely passing value, and reassess the target page's performance accordingly (inferred verification step).

**Tools:** Google Search Console

**Pitfall:** Assuming an internal link is helping simply because it exists is the core mistake — if the linking page itself isn't ranking, "they're not doing any good," no matter how many blog posts you point at your money page.

### 11. Pick a winner page by rank, clicks, and backlinks, then 301  `49.4`
*core · concrete actions · source 49*

When consolidating cannibalizing pages, choose the surviving page using ranked tiebreaker criteria: best existing ranking position for the target keyword, most clicks in the last 90 days, most backlinks pointing to it, and — as a final tiebreaker when pages are close on all of that — fewer existing internal links to update, purely to reduce cleanup work. Then merge in any unique content from the losing pages, set them to draft or delete them, 301-redirect their URLs to the winner, and update every internal link across the site that pointed to a losing page, since the 301 redirect specifically is what transfers the ranking authority.

> "A proper 301 is what moves the authority"

**How to do it**

1. List every page currently competing for the target keyword.
2. Compare each page's best-ever ranking position for that keyword.
3. Pull each page's click count over the last 90 days from Google Search Console.
4. Check each page's backlink count using a backlink tool.
5. If two or more pages are close on rank, clicks, and backlinks, break the tie by choosing whichever page has fewer existing internal links pointing to it.
6. Read through every losing page and copy any genuinely unique information into the winning page.
7. Set each losing page to draft status or delete it outright.
8. Set up a 301 redirect from every losing page's URL to the winning page's URL.
9. Find and update every internal link sitewide that currently points to a losing page, repointing it to the winner.

**Tools:** Google Search Console

**Pitfall:** Skipping or under-prioritizing the 301 redirect is the mistake to avoid — the redirect is specifically what transfers the ranking authority from the losing page to the winner, so consolidating content without it leaves the SEO value behind.

### 12. Rank easy keywords first, then internal-link their authority uphill  `23.2`
*core · concrete actions · source 23*

For a new site with no authority, Edward's rule is to deliberately target under-targeted, bottom-of-funnel keywords first, because you cannot yet compete for the highest-volume terms your competitors already own. Once a page targeting one of these easier keywords starts ranking and accumulating its own authority, the specific next move is to internal-link FROM that now-ranking page TO other pages on the site that target more competitive, more valuable keywords, deliberately funneling the new page's earned authority uphill toward money pages rather than treating each ranking win as standalone.

> "you're going to be doing a lot of targeting for under-targeted keywords"

**How to do it**

1. Run competitor keyword-gap research to find keywords competitors rank for that have low apparent competition relative to your new site's authority (inferred tool: a keyword-gap tool).
2. Prioritize under-targeted, bottom-of-funnel, and easy top-of-funnel keywords for your first wave of pages rather than head/high-volume terms.
3. Publish content targeting these easier keywords first and track their ranking progress in a rank tracker.
4. Once a page begins ranking and earning organic traffic, identify which more competitive, higher-value keyword/page on your site would benefit most from an authority boost.
5. Add a contextual internal link from the now-ranking page to that more competitive target page, using descriptive anchor text relevant to the competitive keyword.
6. Repeat this pattern systematically as each new page starts ranking, treating internal linking as an active mechanism for funneling authority rather than a one-time setup task.
7. Monitor whether the linked-to competitive pages show ranking improvement in GSC/rank tracker after receiving these internal links, to confirm the authority flow is working (inferred verification step).

**Tools:** Google Search Console, a rank tracker

### 13. Reallocate links to striking-distance pages via a 7-day GSC filter  `53.10`
*core · concrete actions · source 53*

When a page is chasing a keyword it realistically can't win, David Quaid's example is a local Connecticut web-design agency's blog post trying to rank nationally for "web design" at a 92% keyword-difficulty score with only 10 backlinks, where it might move from page 16 to page 15 at best, the fix is to stop investing further internal links there and redirect that link equity toward pages that are actually close to ranking. The exact method: in Google Search Console, open the Pages tab, set the date range to the last 7 days specifically, not 90, since a 90-day window accumulates too many ranking peaks and drags the average down, then filter to show pages or keywords sitting above roughly position seven. Those surfaced pages are "striking distance" keywords, close enough that a small authority boost from a reallocated internal link can push them onto page one, and because this requires no new content, just an internal-link adjustment, it can show ranking movement in as little as a few days, his framing is "by Monday."

> "go to Search Console, look at your Pages tab, look at the"

**How to do it**

1. Identify a page currently investing internal links toward a keyword it has little realistic chance of ranking for, e.g., very high keyword difficulty relative to your domain's backlink count.
2. Stop adding further internal links to that malinvested page or keyword.
3. In Google Search Console, open the Pages tab (Performance > Pages).
4. Set the date filter to the last 7 days specifically, not 90 days, since a 90-day window smooths over too many ranking peaks and shifts the average out.
5. Apply a filter to show pages or keywords ranking above roughly position 7, i.e., positions 8 and better, close to page one.
6. Treat the pages that pass this filter as striking-distance opportunities needing only a little more authority.
7. Add internal links, respecting the in-body link cap and judicious-linking rules, from your ranking asset pages to these striking-distance pages instead of the malinvested one.
8. Check rankings again within a few days, the source's framing is "by Monday," to confirm the striking-distance pages are moving up, since this requires no new content, only an internal-link change (inferred verification step).

**Tools:** Google Search Console

**Pitfall:** Continuing to send internal links to a page chasing a keyword far beyond your domain's realistic reach, e.g., 92% keyword difficulty on 10 backlinks, is a malinvestment — that link equity should go to already-close, striking-distance pages instead, which is the fix this exact GSC filter is built to surface.

### 14. Repoint hundreds of cannibalizing internal links with one AI prompt  `16.14`
*core · ai workflows · source 16*

For "de-cannibalization" — fixing internal links that point to the wrong page across a large site — the described AI workflow replaces manual link-auditing (or teaching someone MySQL) with a single natural-language instruction to Claude Code, given direct access to the site's files or database: identify the anchor phrases used for the losing page, then tell Claude to repoint every matching link across the site to the intended canonical page. On the example site mentioned (700 pages, a New York litigation site), this collapses what the speaker frames as a week of manual work into one instruction executed in one pass. The same bot-driven approach extends to repairing broken internal links generally: when a slug changes or a link breaks, the bot is taught to find the next-best replacement page rather than just flagging the 404.

> "all the links that say conveyancing or property litigation, change them"

**How to do it**

1. Identify a set of pages competing for the same or similar keyword/topic (cannibalization) across the site.
2. Decide which single page should be the canonical target for that term or topic going forward.
3. Note the anchor-text phrase(s) currently used site-wide for linking to the losing page (e.g., "conveyancing" or "property litigation").
4. Give Claude Code direct access to the site's files or database (run WordPress locally with Claude working in the files, or connect Claude Code directly to the server/database) (inferred setup step from the source's broader WordPress-access discussion).
5. Prompt Claude Code in plain language naming the anchor phrase(s) and the source and destination pages, e.g. "all the links that say X or Y, change them from this page to this page."
6. Let Claude Code find every matching internal link across all pages and repoint them to the designated canonical URL in one pass.
7. Spot-check a sample of the changed pages to confirm the links now point to the intended canonical page and render correctly (inferred verification step).
8. Apply the same approach to broken internal links generally, having the bot find and substitute the next-best page when a slug changes.

**Tools:** Claude Code, MySQL (manual alternative), WordPress

**Prompt / template:**

```text
hey, all the links that say conveyancing or property litigation, change them from this page to this page
```

**Pitfall:** Doing this manually on a large site (the source's example is 700 pages) means either finding someone to hand-audit every internal link or teaching a non-technical person MySQL — both far slower than giving Claude Code direct file/database access and one plain-language repoint instruction.

### 15. Spend on on-page and internal linking, the only levers you fully control  `67.22`
*core · best practices · source 67*

Asked for the alternative to building drop-catching infrastructure, Dirk's first answer is not another acquisition tactic. He says on-page is the aspect you have the most control over, so it should be constantly checked and optimized, and that internal linking is the strongest factor you have, explicitly contrasting both with backlinks, which you do not control. He makes the same point twice in the interview, first when explaining what separated the survivors of the 2025 update and again here. His framing is that a domain, an exact match, or a caught drop is one building block among many, and that the blocks you own outright deserve the standing investment. This aligns with the base's existing position on internal linking but arrives from an unusual direction, from a practitioner whose main discipline is domain acquisition.

> "your internal linking is the strongest factor you have"

**Evidence:** Dirk names on-page and internal linking as the survivors' common trait after the 2025 update, and repeats it as his recommended alternative to building drop-catching infrastructure.

**How to do it**

1. Audit the on-page of your highest-value pages on a fixed schedule rather than at launch only.
2. Map the internal links into each money page and confirm every one comes from a page that itself ranks.
3. Fix the on-page and internal linking before commissioning any off-site acquisition or link work.
4. Treat any domain, exact match or acquisition as one building block, and budget it after the on-page work.
5. Recheck internal linking after every publishing sprint, since new pages change the distribution.
6. Track which pages gained position after an internal-link change, so the audit earns its own budget.

**Pitfall:** Chasing an acquisition tactic while the on-page and internal linking are unaudited. Dirk says the operators who survived the updates were the ones whose on-page was clean and whose internal linking was correct, not the ones with the best domains.

**Apply at Pabau:** Before Pabau spends on any off-site acquisition or link tactic, put the same budget into a standing on-page and internal-link audit of the blog and template pages, since that is where the controllable gain sits.

**Apply anywhere:** Before spending on any off-site acquisition tactic, put the budget into a standing on-page and internal-link audit. Those are the only two levers you fully control, and they are what separated the survivors of recent updates.

### 16. Treat every internal link as an expense, cap pages at 50  `53.3`
*core · concrete actions · source 53*

David Quaid frames every internal link as a costed investment, saying to think of it as an expense account since every time you create a link, it's expensive, meaning each one should be deliberately justified rather than added by habit. His clear anti-pattern threshold is a page carrying around 50 outbound links, which he states plainly you can be pretty sure isn't helping — that many links dilutes whatever authority the page could pass to any single destination. He explicitly distrusts automated internal-linking tools for this reason, saying that when he inherits a project using one, the first job is to carefully but quickly strip it out, since automation tends to add links indiscriminately rather than judiciously.

> "if you put 50 links on a page, you can be pretty"

**How to do it**

1. Audit a sample of your site's pages for total outbound in-body link count using a crawler such as Screaming Frog (inferred tool for the mechanical count).
2. Flag any page carrying around 50 or more outbound internal links as over-invested and unlikely to be passing meaningful authority to any single destination.
3. For each link on a flagged page, ask explicitly what target page it's investing in and whether that target actually needs or can use the help.
4. Remove or consolidate links that aren't deliberately justified, rather than leaving them because a template or automated tool originally added them.
5. If any automated internal-linking plugin or tool is active on the site, audit and strip its output first, carefully but quickly, before doing further manual internal-link work.
6. Going forward, add new internal links one at a time with a stated reason, rather than batch-adding them across many pages at once.

**Tools:** Screaming Frog

**Pitfall:** Believing internal links function as "free authority" that can't hurt you leads directly to link-spam pages — David Quaid is explicit that heavily-linked pages, his benchmark is around 50 links, are a sign the links aren't judiciously chosen and aren't helping.

### 17. Use Claude to place internal links that boost other pages  `31.3`
*core · ai workflows · source 31*

Once a page is ranking and earning its own clicks, it generates its own authority that can be intentionally funneled to other pages via internal links. The workflow: start a brand-new Claude chat (separate from the editing chat), paste in the full updated high-ranking article, and confirm receipt; then paste in the page you want to boost and either dictate a rough explanation (speech-to-text works fine) of how to link them, or use a structured prompt asking Claude to find the most natural place in the first article to add a link, returning only the insertion point, the exact sentence/H2, and the anchor text, kept concise and in your voice. If the high-ranking article has nothing genuinely related to the page you want to boost, add a short new H2 section first to create real topical relevance before placing the link.

> "Find the most natural place in the first article"

**How to do it**

1. Identify your just-updated, high-ranking page and a second page on your site that you want to boost using that page's accumulated authority.
2. Start a brand-new Claude chat (separate from the one used to edit the article) and paste in the full, updated text of the high-ranking first article.
3. Use the prompt "This is my page, just confirm you received it" so Claude has the full first article loaded as context.
4. Paste in the full text of the second page you want to boost.
5. Either dictate a rough, conversational explanation of how you want to boost this second page, or use the structured prompt: "This is the page I want to boost. Find the most natural place in the first article to add an internal link to it. Give me only where to add it, the sentence or H2 section to insert, and the anchor text. Keep it concise and in my voice."
6. Review Claude's suggested insertion point, sentence/section, and anchor text before adding it to the live article.
7. If the first article doesn't currently contain any content genuinely related to the page you want to boost, add a short new H2 section specifically to create a topically relevant place for the internal link to live.
8. Insert the internal link using the suggested anchor text and location so it reads as topically relevant rather than forced.

**Tools:** Claude

**Prompt / template:**

```text
Prompt 1 (load the first article): "This is my page, just confirm you received it." Prompt 2 (request the link placement): "This is the page I want to boost. Find the most natural place in the first article to add an internal link to it. Give me only where to add it, the sentence or H2 section to insert, and the anchor text. Keep it concise and in my voice."
```

**Pitfall:** Adding an internal link to a boosted page in a spot with no genuine topical connection makes the link feel forced to readers and less valuable to the page being boosted - if the high-ranking article has nothing truly related to the target page, add a short new H2 section first to create real topical relevance before placing the link.

### 18. Use a /uses or /tools hub page to redistribute link equity  `56.20`
*core · concrete actions · source 56*

The structural trick Cody offers for software companies: create a hub page at /uses listing all the use cases of the software (he also uses /tools). Each bottom-of-funnel SEO landing page links to the hub page, and the hub page distributes the equity out to every use-case page beneath it. Edward confirms doing the same. In his experience this structural move outperforms anything you can do on the written-content side. It combines with the concentration point: instead of link equity landing on scattered blog posts, it flows through a single hub that pushes it back down to the pages that convert.

> "you have a uses hub"

**How to do it**

1. Create a hub page at a predictable path - /uses or /tools - that lists every use case or tool your product covers.
2. Give each use case its own bottom-of-funnel landing page, targeting the keyword for that use case.
3. Link from every use-case landing page up to the hub page.
4. Link from the hub page down to all of the use-case pages, so the hub redistributes what it receives.
5. Point external link building at the hub and at your strongest use-case pages rather than at the blog.
6. Add new use-case pages into the hub as they're created, so the structure grows without rewiring.

**Pitfall:** A hub page that is only a link list with no substance is a thin page - it needs to justify its own existence as an overview of what the product does, or it becomes the weak link in the structure.

**Apply at Pabau:** Pabau has the natural version of this already in its feature and use-case structure - the actionable part is making sure every bottom-of-funnel page links up to that hub and the hub links back down to all of them, so link equity circulates rather than pooling.

**Apply anywhere:** If you already have a feature or use-case structure, the actionable part is making sure every bottom-of-funnel page links up to the hub and the hub links back down to all of them, so link equity circulates rather than pooling.

### 19. Vary internal anchor text across synonyms to net related keywords  `139.7`
*core · concrete actions · source 139*

Rather than repeating one exact-match anchor, Brandon pointed internal links at his 'what happens if you miss a quarterly estimated tax payment' page using a spread of synonymous phrasings: 'penalty for not paying quarterly taxes', 'what happens if you pay quarterly taxes late', 'paying quarterly taxes late', and 'what happens if you don't pay quarterly taxes'. The page then ranked not only for its primary target but for each of those synonymous queries too. His explanation is that varied anchors tell Google the page covers a cluster of same-intent phrasings, not a single string. He treated this as a systematic pass, going back through all blog posts to optimize the anchor text on existing internal links rather than only setting anchors on new ones. Note this contradicts nothing in the base about capping any single anchor, and supplies the reason to vary: extra keyword coverage.

> "I used anchor texts with synonyms like"

**Evidence:** Keeper Tax's quarterly payment page ranked for its primary keyword plus 'what happens if you pay quarterly taxes late', 'what happens if you don't pay quarterly taxes' and 'paying quarterly taxes late' after the anchor variation pass.

**How to do it**

1. Pick a target page and pull the cluster of same-intent query variants from Ahrefs or Search Console.
2. Write out four to six anchor phrasings covering those variants, including negated and rephrased forms.
3. Run the site: plus topic search to list the pages that should link to the target.
4. Assign a different anchor from your list to each linking page, so no single phrase repeats across the site.
5. Go back through existing internal links to the target and rewrite their anchors to fill gaps in the variant list.
6. Keep each anchor reading naturally in the sentence rather than dropped in as a phrase.
7. Cap any one anchor at a small number of uses so the profile stays varied.
8. Check after a few weeks which variants the page now ranks for and add anchors for the ones still missing.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Using the identical exact-match anchor on every internal link wins one query and leaves the synonym cluster to competitors. The signal you have hit it is a page ranking well for its head term and nowhere for obvious rephrasings.

**Apply at Pabau:** Pabau's internal links into a page like online booking should rotate through the real query variants practices type rather than repeating one anchor, and existing links should be rewritten in the same pass.

**Apply anywhere:** Point internal links at a target page using four to six synonymous anchor phrasings drawn from its query cluster, and rewrite existing links to fill the gaps.

### 20. When a refresh fails, write the supplementary article and link down to it  `56.2`
*core · concrete actions · source 56*

The second half of Cody's loop handles the case where the refresh doesn't work. If, after modifying the page, it still hasn't reached page one for the target keyword, he treats that as a signal the parent page can't carry the term - so he writes a dedicated supplementary article for that keyword and links to it from the parent page. What he observes is that the parent page then starts to rank for the keyword it previously couldn't hold, because the link relationship passes the topical signal along. It's a deliberate two-step: try to absorb the keyword into an existing ranking asset first, and only create a new URL when absorption fails.

> "I need to do like a supplementary article"

**How to do it**

1. After a refresh, wait long enough for the change to be reflected (he works on a monthly cadence) and re-check the target keyword's position.
2. If the page still isn't on page one for that keyword, stop trying to force it onto the parent page.
3. Write a supplementary article dedicated to that single keyword, treating the parent page's topic as the umbrella.
4. Link from the parent page to the new supplementary article, in-body and in context, not from a related-posts widget.
5. Track both URLs for the keyword - in his experience the parent page often starts ranking for it, which is the outcome you want.
6. Only escalate to a third asset if neither URL moves; otherwise the cluster is doing its job.

**Tools:** Google Search Console

**Pitfall:** Creating the supplementary article first, before trying to absorb the keyword into the existing page, is the wrong order - you end up with two thin URLs competing for the same term instead of one strong one.

**Apply at Pabau:** For Pabau, treat a failed refresh as the trigger for a new article rather than the default: only spin up a new URL for a feature or treatment keyword after the existing page has demonstrably failed to hold it, and always link down to the new page from the parent.

**Apply anywhere:** Treat a failed refresh as the trigger for a new article rather than the default: only spin up a new URL after the existing page has demonstrably failed to hold the keyword, and always link down to the new page from the parent.
