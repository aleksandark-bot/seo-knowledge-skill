# Technical SEO — core (part 1 of 2)

17 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. 301 redirects no longer cause PageRank loss — Google confirmed it twice  `34.1`
*core · content insights · source 34*

The long-standing SEO belief that 301 redirects lose a percentage of link equity or PageRank is outdated: in 2013, Matt Cutts, then head of web spam at Google, confirmed that 301 redirects did cause a 15% loss of PageRank at that time. But in 2016, Google's Gary Illyes tweeted that 30x redirects no longer lose PageRank at all, and when directly asked whether there was even a smaller "dampening factor" applied, he replied plainly, "For PageRank, no." Google's own Search Central documentation on how to move a site still states today, in 2026, that "301 and other permanent redirects don't cause a loss in PageRank," meaning this isn't just an old tweet but current, standing official guidance.

> "confirmed that 301 redirects resulted in a 15% loss of PageRank"

**Evidence:** Direct citations: Matt Cutts (2013) confirmed a 15% PageRank loss from 301 redirects at that time; Gary Illyes (2016) tweeted that 30x redirects don't lose PageRank, explicitly ruling out even a partial dampening factor ("For PageRank, no"); and Google's current Search Central documentation on site moves states "301 and other permanent redirects don't cause a loss in PageRank."

**Apply at Pabau:** Pabau's team should stop treating 301 redirects, such as URL restructuring or domain consolidation or fixing legacy URLs, as an authority-losing operation to be minimized or avoided; redirects should be used whenever there's a real information-architecture or migration reason, since the current, official Google position is that permanent redirects carry link equity through cleanly.

**Apply anywhere:** Your team should stop treating 301 redirects, such as URL restructuring or domain consolidation or fixing legacy URLs, as an authority-losing operation to be minimized or avoided; redirects should be used whenever there's a real information-architecture or migration reason, since the current, official Google position is that permanent redirects carry link equity through cleanly.

### 2. A sitemap is a crawl-priority queue signal, not a control list  `45.13`
*core · content insights · source 45*

David directly corrects a widespread misconception among engineers: an XML sitemap is not a 'control list' that tells Google what to index — sitemap crawlers don't even fetch the listed pages themselves, they only forward the URLs into a crawl-priority queue, and your top (already-authoritative) pages will get crawled from that queue while lower-priority ones might not. Submitting or resubmitting a sitemap does not force Google to move any page out of a low-priority crawl pool (which might only get refreshed monthly) into a high-priority one; for a new or lower-authority site, updating the sitemap 'isn't going to do much' since Google might not re-read it for another week regardless. The one thing a sitemap is genuinely useful for is diagnostic: comparing how many URLs your CMS believes it has published against how many Search Console reports as actually indexed reveals gaps caused by UTM-parameter URLs, ghost pages, typo pages, and deleted pages inflating your apparent URL count.

> "a lot of engineers think a sitemap is a control list"

**Evidence:** David's claim, drawn from experience including time on Google's own support desk as a volunteer: sitemap crawlers forward URLs to a crawl-priority queue rather than fetching/indexing them directly; example of a site owner expecting '26 pages' but Search Console reporting '156 URLs' due to UTM/ghost/typo/deleted pages.

**Apply at Pabau:** David should stop treating XML sitemap submission/resubmission as a lever to force faster indexing on pabau.com, and instead use it purely as a diagnostic (compare submitted URL count vs. indexed percentage in GSC) — and should prioritize an HTML sitemap linked from the site footer, since David states that page carries real authority and context that a bare XML URL list cannot provide.

**Apply anywhere:** You should stop treating XML sitemap submission/resubmission as a lever to force faster indexing on your main domain, and instead use it purely as a diagnostic (compare submitted URL count vs. indexed percentage in GSC) — and should prioritize an HTML sitemap linked from the site footer, since David states that page carries real authority and context that a bare XML URL list cannot provide.

### 3. Audit for exact keywords repeated 3x in a row that silently de-index pages  `38.6`
*core · concrete actions · source 38*

Kalin describes an old, still-active Google penalty from the 2005-era keyword-stuffing crackdown: if the exact same keyword appears three or more times consecutively in a page's rendered code (not just visible text), the page gets de-indexed — even if the repetition is an innocent template artifact, like a breadcrumb reading 'Toys,' followed by a category label 'Toys,' followed by a product title starting with 'Toys.' He verified this on a poorly built real-estate CMS where every listing photo shared identical alt text: listings with up to three photos (so the alt text repeated up to three times) stayed indexed, but listings with more photos, repeating that same alt text more than three times, were automatically de-indexed. This is described as exactly the kind of 'extremely mundane' technical cause that gets missed because SEOs look for big explanations (algorithm updates, content quality) instead of literal code-level repetition.

> "same keyword three times in a row in your content"

**How to do it**

1. Crawl the site with Screaming Frog, exporting page titles, H1s, breadcrumb trail text, category/tag labels, and every image's alt attribute. (inferred: use Screaming Frog's Internal tab plus a custom extraction for alt text)
2. For each template type (category pages, product/listing pages, blog posts), check whether any single exact keyword or phrase appears three or more times consecutively in the rendered HTML.
3. Pay special attention to breadcrumb trails, auto-generated category/tag labels, and templated image alt text that repeats the same keyword across multiple images on one page.
4. Cross-check any suspect URL against Google Search Console's URL Inspection tool and the Index Coverage/Pages report to see if it is actually excluded from the index.
5. Where the 3x-consecutive pattern is confirmed, rewrite the template logic so consecutive instances vary (synonyms, added modifiers, more specific descriptions) instead of repeating an identical string.
6. After fixing, resubmit the affected URLs via GSC URL Inspection > Request Indexing and monitor whether they get indexed within the following days.
7. Add this exact-repetition check to standard QA for any new templated page type (new listicle format, product category, image gallery) before mass-publishing. (inferred)

**Tools:** Screaming Frog, Google Search Console

**Pitfall:** Assuming an indexing failure must have a 'big' cause like an algorithm update or thin content, when it can be caused by a literal, mechanical trigger — the exact same keyword string appearing three-plus times in a row in the page's code, a leftover rule from 2005-era keyword-stuffing penalties.

### 4. Audit log files against sitemap dates to find crawl-starved stale content  `25.2`
*core · concrete actions · source 25*

Koray runs a freshness audit by pulling server log files alongside the XML sitemap's lastmod dates, segmenting URLs by site section, then calculating what percent of each segment is older than six months versus updated in the last 30 days. He compares Googlebot's crawl frequency between those two buckets as a proxy for how stale Google currently perceives a section to be, since younger-than-30-day URLs are consistently crawled more often and prioritized. The point isn't just to observe the split but to deliberately shift it by refreshing/publishing enough recent content in a segment to change Google's crawl priority and trigger reassessment of rankings or SERP features for that segment. He frames it as a repeatable 'weapon' to check on a recurring cadence per site section, not a one-off audit.

> "what percentage of the site is older than six months"

**How to do it**

1. Export your site's raw server access logs for at least the last 30-90 days, or load them into a log analyzer such as Screaming Frog Log File Analyser (inferred).
2. Filter the log data to isolate hits from the Googlebot user-agent string only, excluding other bots and human traffic (inferred).
3. Pull your XML sitemap (e.g., sitemap.xml or sitemap_index.xml) and extract the lastmod date for every listed URL into a spreadsheet.
4. Tag each URL with its site segment (e.g., blog, glossary, product pages, comparison pages) in a new column.
5. Add a column calculating days-since-lastmod for every URL, then flag each row as 'older than 6 months' or 'younger than 30 days.'
6. In the log data, sum Googlebot hit counts per URL, then roll up totals per segment over the audit window.
7. Build a pivot table comparing average Googlebot crawl frequency for the 'older than 6 months' bucket versus the 'younger than 30 days' bucket, per segment.
8. Identify segments where the stale bucket is large (e.g., over half of URLs) and its crawl frequency is disproportionately low.
9. Refresh or republish a portion of the stale bucket in that segment (update content, change dates, resubmit to the sitemap) to shift Google's crawl priority.
10. Re-run the log pull 2-4 weeks later to confirm crawl frequency and ranking/SERP-feature visibility improved for the refreshed segment (inferred verification step).

**Tools:** Screaming Frog Log File Analyser (or similar log analyzer), XML sitemap, Spreadsheet (Excel/Google Sheets)

**Pitfall:** Relying on sitemap lastmod dates that aren't trustworthy — Koray explicitly caveats 'if your last-mod data is accurate, do that,' implying many sites have stale or fake lastmod timestamps that would corrupt the audit.

### 5. Build a bot that verifies your full conversion path  `16.11`
*core · concrete actions · source 16*

Beyond a standard crawl-based technical audit (Semrush or Screaming Frog producing an error list that then becomes manual tickets), the speakers describe building a dedicated bot that actively tests whether the site's real conversion mechanics still work: it fills in the site's own lead forms on a schedule and confirms GA4 fires the expected key event and that the lead actually lands in the CRM (HubSpot is named), catching failures like "a week's worth of leads went missing" that a link-status crawl would never surface. The same bot concept extends to checking external links to authoritative sources for breakage, and to internal links, automatically finding a next-best replacement page when a slug changes rather than just flagging a 404. It also covers spam filtering on inbound forms and brand/partner-content proofing, and is framed as buildable "right now" on an existing WordPress site with no CMS migration required.

> "quality bots that test pages, make sure GA4 fired a key event"

**How to do it**

1. Run your normal technical crawl in Screaming Frog or a Semrush Site Audit to get the standard broken-link/error baseline.
2. Build (or have Claude Code build) a script that additionally checks your outbound external links, including references to authoritative sites, for broken status.
3. Have the bot flag any broken external link for removal or replacement and automatically open a ticket rather than requiring a manual write-up.
4. Extend the same bot to internal links: when a slug changes or a link 404s, have it locate and suggest a next-best replacement page instead of only reporting the break.
5. Add a synthetic-conversion check: have the bot submit the site's own lead/contact forms on a schedule and verify GA4 records the expected key event and the lead reaches HubSpot or your CRM.
6. Add spam-detection logic on form submissions so junk entries are identified and blocked before they pollute analytics, ad platforms, and CRM data.
7. Add a brand/partner-content proofing check that flags misspelled brand names or off-message partner copy sitewide (inferred grouping of the source's brand-consistency point into an automatable check).
8. Route every flagged issue automatically into your existing ticketing system so nothing depends on a human remembering to log it.
9. Start this on your current WordPress site specifically, since the source notes it is buildable today without a CMS migration.

**Tools:** Screaming Frog, Semrush, Claude Code, GA4, HubSpot

**Pitfall:** Relying only on periodic manual crawls means a broken lead form or dead citation link can go unnoticed for a week or more of lost leads — the fix is a bot that continuously verifies the actual form-to-GA4-to-CRM conversion path, not just HTTP status codes.

### 6. Bulk 301 redirects over ~100 without mirrored URLs get devalued  `38.7`
*core · concrete actions · source 38*

Kalin argues Google almost certainly implements redirect-equity rules as blunt numeric if/else thresholds rather than any 'effort' or intent-sensing evaluation. He reasons a Google engineer would code something like 'if there are more than 100 redirects, devalue those redirects, unless they're mirror redirects to a mirrored URL' — meaning meticulously hand-mapping hundreds of individual old URLs to their most relevant new-site equivalents (e.g., pulling 300 linked pages from Ahrefs and manually pairing each one) still hits the same devaluation threshold and passes no equity, despite feeling like careful, high-quality work. Separately, the single worst redirect pattern is mass-redirecting every old page to the homepage, which Google flags as a lazy black-hat signal that passes no power through (though it won't actively penalize the destination site for it).

> "if there are more than 100 redirects, devalue those redirects"

**How to do it**

1. Before executing a large-scale domain migration or redirect project, count the total number of 301 redirects being applied in that batch.
2. If the batch will exceed roughly 100 redirects, check whether the old-path-to-new-path mapping is a structurally consistent 'mirror' pattern across the whole set, since mirrored redirects may be exempt from the devaluation threshold.
3. Do not rely on painstaking manual one-to-one URL mapping as a way to preserve equity at this scale — treat it as likely to still trigger the same rule-based devaluation.
4. Never mass-redirect all old URLs straight to the homepage; Google treats this as a lazy/black-hat signal and passes no link equity through it.
5. Where a migration must involve more than ~100 non-mirrored redirects, consider splitting it into smaller batches deployed over time instead of one mass redirect event. (inferred)
6. After migrating, monitor the destination URLs' rankings and indexing status in Google Search Console (Performance and Index Coverage reports) to verify whether equity actually passed through, rather than assuming careful manual mapping guarantees it. (inferred)

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Believing that meticulous, individually-mapped 301 redirects will be rewarded for 'attention to detail' — Google's actual implementation is described as a blunt numeric threshold, so careful manual mapping at scale can still result in zero equity passed through.

### 7. CMS migration playbook that added 1M clicks in 3 months  `03.3`
*core · concrete actions · source 03*

A QR-code-generator site migrated from WordPress to Next.js with Sanity as the back-end CMS while keeping content, layout, and URLs identical, gaining over 1 million extra clicks in three months from the combination of microsemantic changes and technical improvements. The two governing migration rules are to change only one thing at a time and to never leave any URLs or resources behind, since any asset left unmapped or un-redirected gives the search engine a slower, costlier reason to distrust the new setup. Every asset type was mapped one-to-one across the migration (image-to-image, HTML-to-HTML, CSS-to-CSS, JavaScript-to-JavaScript), non-indexed URLs were pruned from the crawl profile, response times were improved, structured data was updated, and the core interactive tool was kept renderable without requiring JavaScript.

> "Change only one thing at a time"

**How to do it**

1. Before migrating, inventory every existing asset type on the site (HTML pages, images, CSS, JavaScript files) and build a 1:1 mapping from each old asset to its new-stack equivalent. (inferred: use a crawler such as Screaming Frog to generate the full pre-migration URL/asset list)
2. Change only one variable per migration phase (e.g., migrate the CMS backend without also changing URL structure, content, or layout at the same time) so any ranking impact can be attributed to a single cause.
3. Redirect every single old URL and resource to its new equivalent; do not skip lower-priority pages or assets to save time.
4. Treat image and video URLs as the highest-risk asset type to change; avoid altering them at all if possible, since they are the slowest and most costly resource type for a search engine to re-index and re-trust.
5. Remove all non-indexed URLs from the site during the migration to prune the crawl profile down to only what matters.
6. Improve server response times as part of the migration to increase crawl efficiency.
7. Update structured data to match the new stack.
8. Ensure the site's centerpiece interactive tool or main functional element renders without requiring JavaScript, so it stays crawlable.
9. After launch, monitor Google Search Console's Crawl Stats and Performance reports by URL type (HTML vs. image vs. other) to confirm crawl budget is shifting toward productive HTML pages. (inferred)
10. If any asset type, especially images, shows both falling crawl requests and falling rankings together after migration, treat this as a signal of an incomplete redirect map for that asset type and prioritize fixing it next.

**Tools:** Next.js, Sanity CMS, Google Search Console, Screaming Frog

**Pitfall:** Partially redirecting image or video URLs (redirecting only the most important ones instead of all of them) causes measurable ranking losses, because these resource types are far more costly and slower for a search engine to re-index and re-trust than HTML — the case study's own migration lost image rankings specifically because not all image URLs were redirected.

### 8. Case study: HTTP-to-HTTPS + new-domain migration saw traffic rise, not fall  `34.3`
*core · content insights · source 34*

SEO Cyrus Shepard ran what he called an unintentional real-world test of Google's newer 3xx PageRank rules: migrating a small site simultaneously from HTTP to HTTPS and to an entirely new domain, while keeping every other element of the site, page titles, content, and images, exactly the same, isolating the redirect itself, plus the protocol and domain change, as the only variables. Going into the migration, he fully expected to see a traffic decline consistent with the previously-rumored 15% PageRank loss from redirects. Instead, traffic actually increased after the migration, which Shepard notes could possibly be partly attributed to the modest ranking boost Google is known to give HTTPS sites, though that couldn't be confirmed with certainty.

> "traffic actually saw a boost after the migration"

**Evidence:** Cyrus Shepard's 2016 case study: migrated a small site's URLs from HTTP to a new HTTPS domain while holding titles, content, and images constant, expecting a 15%-PageRank-loss-driven traffic decline; traffic instead rose after the migration.

**Apply at Pabau:** This gives Pabau a concrete precedent for any future domain, protocol, or URL-structure migration: a well-executed migration that changes only the URL, keeping content, titles, and structure otherwise identical, should not be expected to cause a traffic drop from redirect-related authority loss, and may even see a modest lift.

**Apply anywhere:** This gives your site a concrete precedent for any future domain, protocol, or URL-structure migration: a well-executed migration that changes only the URL, keeping content, titles, and structure otherwise identical, should not be expected to cause a traffic drop from redirect-related authority loss, and may even see a modest lift.

### 9. Diagnose de-indexing via GSC property spikes, then recover fast  `54.2`
*core · concrete actions · source 54*

Facing a sudden full de-indexing with no manual action visible yet, Glenn's method was to open every Search Console property and compare their graphs, which surfaced a huge one-day spike in the domain property that the canonical property never showed. Filtering that property by page isolated the exact URL responsible (the non-canonical https-www homepage), and pulling its ranking queries revealed they were all gambling-related - confirming the page had been hacked and was redirecting to a gambling site, on a site in a YMYL niche. Once identified, the client fixed the vulnerability within about an hour, filed a reconsideration request explaining the hack and cleanup, and the site reappeared in the live SERPs (confirmed via a direct site: search) the very next morning.

> "The site jumped to nearly 12,000 clicks per day"

**How to do it**

1. When a site is unexpectedly and completely de-indexed, first confirm it directly with a 'site:yourdomain.com' search in Google rather than relying on a rank tracker alone.
2. Check Google Search Console for an existing manual action or security issue, but don't assume the absence of one means you're safe - manual actions can be delayed.
3. Open every Search Console property you have (domain property, each protocol/www URL-prefix property, directory properties) and compare their performance graphs against each other.
4. Look for a sudden, anomalous spike or drop in clicks/impressions on a single day in any property, especially the domain property, which aggregates all variants.
5. When you find an anomalous spike, filter that property's report by page to identify exactly which URL is responsible.
6. Pull the search queries that specific page is ranking for during the spike window - queries wildly unrelated to your site's actual topic indicate the page has been hacked or hijacked.
7. Cross-check with a rank-tracking/visibility tool's historical SERP snapshots, if available, to see the hacked page's altered title, snippet, and favicon during the hack window.
8. Notify whoever controls the technical infrastructure immediately with the specific evidence (screenshots, queries, URL) so they can fix the vulnerability and remove the hacked redirect as fast as possible.
9. File a reconsideration request as soon as the underlying issue is fixed, explaining plainly what happened and what was done to resolve it.
10. Recheck via a direct site: search rather than waiting on Google's official notification, since real-world reinstatement can happen hours before the formal approval message arrives.

**Tools:** Google Search Console, a rank-tracking/visibility tool

**Pitfall:** Assuming the absence of a manual action notice in Search Console means there's no problem is a mistake - manual actions can be delayed well after a site is already being impacted in search results, so an unexplained full de-indexing still requires immediate investigation across every property.

### 10. Diagnose non-indexed pages as accessibility issues or duplicates  `29.10`
*core · concrete actions · source 29*

When a page isn't indexed despite the SEO's expectation, Hank's triage is binary: it's either an accessibility problem or a content problem. To check accessibility, verify the page renders correctly, that internal links actually point to it, that it's present in the XML sitemap, and that no incorrect canonical tag is redirecting its authority elsewhere. If accessibility checks out clean, move to the content question: search for near-duplicate pages on your own site answering the same query (often the same page with only the title or URL slug differing), and force yourself to write out the actual distinction between them. If no real distinction can be articulated, Hank's advice is to stop spending resources trying to force indexing and accept it as expected, rather than treating every non-indexed page as a bug to fix.

> "the number-one thing to check is accessibility"

**How to do it**

1. When a specific page isn't indexed, first classify the cause as either accessibility/technical or content/duplication.
2. Check accessibility by confirming the page renders correctly, is actually linked to internally, appears in the XML sitemap, and has no incorrect canonical tag pointing elsewhere.
3. If accessibility checks all pass, search your own site for near-duplicate pages answering the same query, often differing only in title or URL slug.
4. For any near-duplicate found, write out explicitly what the real distinction between the two pages is and whether it adds genuine value.
5. If no real distinction can be articulated, stop spending further resources trying to force that page to index.
6. If a genuine distinction exists, rewrite the page to make that distinction explicit in the title, intro, and structure rather than leaving it implicit.
7. Log this two-bucket triage outcome for each ticket so the team isn't re-investigating the same root causes repeatedly. (inferred)

**Pitfall:** Chasing indexing on a page that is technically accessible but substantially duplicates another page on your own site wastes effort - if no real distinction can be articulated, non-indexing is the expected, correct outcome, not a bug.

### 11. Fix HTTP 499 errors to unlock AI crawling  `20.11`
*core · concrete actions · source 20*

A little-known HTTP status code, 499 (Nginx-originated, adopted by most CDNs), signals that a requesting client gave up waiting because a page loaded too slowly. This matters for AI visibility specifically because unlike Google (which crawls and indexes in advance), ChatGPT requests pages in real time during its query fan-out — so a 499 means ChatGPT simply gives up and never sees that content at all. In a real client case, diagnosing high 499 volumes via log-file analysis and fixing them by caching content at the edge produced roughly a 300% visibility improvement within three months, with the site not feeling slow to human users at all, since single-page-application loading patterns create a perceived-speed illusion for humans that doesn't apply to a bot's raw real-time request.

> "we improved visibility over three months by about 300%"

**How to do it**

1. Pull your server/CDN log files for the pages you most want visible in AI search.
2. Search the logs specifically for HTTP 499 status codes rather than just the standard 4xx/5xx codes.
3. For every URL showing a meaningful volume of 499s, treat it as a real-time-timeout problem affecting live requesters, including AI crawlers performing query fan-out.
4. Compare page-speed metrics (especially time to first byte) between your underperforming pages and pages from competitors performing well in AI answers.
5. Prioritize time-to-first-byte specifically, since bots evaluating a page in real time don't benefit from perceived-speed tricks (progressive/below-the-fold loading) that make a page feel fast to a human.
6. Implement edge caching for the affected content so requests are served instantly with no origin-server timeout risk.
7. Re-check the log files after the fix to confirm the 499 volume has dropped for the affected URLs.
8. Track AI-visibility metrics (citation rate, appearance in target prompts) over the following 30-90 days — the source's case saw roughly 300% improvement within three months, with initial gains visible within about 30 days.

**Pitfall:** Assuming a site 'feels fast' to a human visitor means it's fast enough for AI crawlers — the source's case felt normal to users while still generating a large volume of 499 timeouts against ChatGPT's real-time fan-out requests, since bot experience and perceived human experience of speed are not the same thing.

### 12. Four-step fix for "Crawled – currently not indexed" pages  `10.12`
*core · concrete actions · source 10*

For a newer or midsize site where a page shows "Crawled – currently not indexed" in Google Search Console, first use GSC's URL Inspection tool to request indexing or "ping" the URL, which alone often triggers reindexing. Second, run a render check to confirm Googlebot is actually seeing the same page a human sees, using the free Chrome extension "Render Diff," which shows what Google renders versus what a real browser renders, exposing JS-blocking or conditional-rendering problems. Third, rule out a hosting or CDN issue, since Cloudflare firewall rules commonly block images and other assets, and fourth, check for CMS-level quirks, since WordPress and especially Magento are named as commonly causing indexing issues. At enterprise scale, treat mass crawled-not-indexed pages, such as 39,000 pages at once, as a technical or foundational problem rather than a per-page fix: open Chrome DevTools to inspect the live connection and rendering, check the page source for conflicting tags or JS blocking, check for firewall or CDN blocks, and set up ongoing automated monitors, because a fix one person makes can get silently reverted by another team member later.

> "There's a free Chrome extension called Render Diff"

**How to do it**

1. Open the affected URL's report in Google Search Console under Page Indexing or URL Inspection.
2. Click "Request Indexing" to ping the URL directly, which alone often resolves the issue.
3. Install the free "Render Diff" Chrome extension and run it on the live page to compare what Googlebot renders versus what a user sees.
4. If the render check shows a mismatch, inspect the page for JavaScript that blocks content from appearing in the initial render.
5. Check whether your CDN or firewall, such as Cloudflare, is blocking any page resources like images.
6. Check for CMS-specific quirks known to cause indexing problems, such as WordPress plugin conflicts or Magento configuration issues.
7. For large-scale or enterprise crawled-not-indexed issues affecting many URLs at once, open Chrome DevTools (F12, then the Network tab) on a sample page to inspect the actual connection and rendering behavior.
8. View the page's raw source code to check for conflicting meta robots tags, canonical tags, or blocked JS resources.
9. Set up an ongoing automated monitor on critical page templates so you're alerted immediately if indexability breaks again after a deploy (inferred use of a monitoring tool).
10. If a critical revenue page breaks, escalate immediately to the responsible stakeholder with the specific traffic or revenue impact at stake.

**Tools:** Google Search Console, Render Diff (Chrome extension), Chrome DevTools

**Pitfall:** At enterprise scale a fix is fragile, because with many people working on the same site, someone else can flip a setting back and silently re-break indexing a week later, so ongoing monitoring rather than a one-time fix is required.

### 13. Get new pages linked from existing crawled pages instead of relying on a sitemap  `74.3`
*core · concrete actions · source 74*

David Quaid reads Google's line that most pages are found and added automatically as crawlers explore the web, and says this undermines most indexing advice. The mechanism he describes: Google opens a page it already trusts, finds a link to a new page, carries authority and context from that link, hands it to the indexing service, and the page gets indexed. Sitemaps work at high authority — he says a CNN sitemap URL will land in the highest-priority crawl queue — but at low authority they do very little. He is blunt that answering every indexing question with 'submit a sitemap' is unhelpful. He also says he can get content into Google in a couple of minutes, but that if he does not link it from his own content and only posts it on X, sharing it a hundred times will not get it indexed, especially on a new topic.

> "you want your new page to be found in a link from an old page"

**Evidence:** David: he can get content into Google in minutes when it is linked from his own content, but sharing an unlinked new-topic page 100 times on X does not get it indexed.

**How to do it**

1. Before publishing, pick two or three existing pages that already rank and already get crawled, and identify where a contextual link to the new page fits.
2. Add the internal links to those pages in the same session you publish, not weeks later.
3. Prefer linking from pages in the same topical folder, since they carry the closest context.
4. Add the new URL to the sitemap as normal, but do not treat submission as the indexing action.
5. Check indexation with a site: query plus a distinctive phrase from the page rather than watching the sitemap report.
6. If the page is still not indexed after a week, add another link from a higher-authority page rather than resubmitting the sitemap.
7. Stop counting social shares as an indexing tactic; David says a hundred shares on X will not index an off-topic new page.

**Tools:** Google Search Console

**Pitfall:** Publishing an orphan page and then resubmitting the sitemap repeatedly. On a low-authority site the URL sits in a low-priority crawl pool and no amount of resubmission moves it.

**Apply at Pabau:** Pabau's publishing process for /blog/ and /templates/ pages should require at least two contextual internal links from already-ranking pages before a post goes live. Treat that as a blocking step in the checklist, not a follow-up task.

**Apply anywhere:** Make 'linked from at least two already-ranking pages at publish time' a hard requirement for every new URL, and stop treating sitemap submission as an indexing lever.

### 14. Google treats every URL as its own authority-bearing "canon"  `22.2`
*core · content insights · source 22*

David Kaid's framing: Google treats every URL as "the canon" (he links the term to Catholic canon law, a definitive singular law), meaning each specific URL is a unique entity that accumulates its own topical authority, separate from any other URL even when the content is identical. He pushes back on the phrase "I changed my URL," arguing you technically introduced a brand new URL and pointed the old one to it via 301 — and crucially, "even if you 301 it, it's still a newer URL," so the original authority judgment doesn't automatically carry over; the new canon gets a fresh evaluation. This is offered as the mechanistic reason republishing under a new slug can succeed where the original URL stayed permanently stuck, even with unchanged content.

> "the canon has all of the topical authority"

**Evidence:** Presented as David Kaid's own conceptual explanation, given as an excerpt from an earlier podcast appearance, not a documented Google study.

**Apply:** When a Pabau page is stuck in "Crawled – currently not indexed" for a long time despite being relevant and well-optimized, don't rely only on re-requesting indexing on the same URL — treat a deliberate new-slug-plus-301 republish as a distinct lever that gives the content a genuine fresh evaluation, reserved for cases where real topical authority/links have also been built since the original publish.

### 15. Google's cost of retrieval means quality alone doesn't earn ranking  `03.2`
*core · general insights · source 03*

Google favors structural similarity between queries and documents (query templates) simply because it is cheaper to compute and serve. The article frames Google as primarily designed to save computational cost rather than to serve the objectively best result, so ranking chance is a function of quality relative to the cost of retrieving and evaluating a page — a website with quality 6 out of 10 but a retrieval cost of 7 out of 10 is not worth retrieving even if its quality exceeds many competitors'. Query templates help Google satisfy more users and drive more clicks while organizing more sources at lower computational cost, and when a page satisfies one query, Google tests it against similar queries as a re-ranking trigger, which is the mechanical basis for building a semantic content network of interlinked documents covering a shared query network.

> "quality is 6/10 and its cost is 7/10, it's not worth retrieving"

**Evidence:** The article's stated cost-of-retrieval formula, that the cost of ranking a site cannot exceed the cost of not ranking it, illustrated with an explicit numeric example: quality 6/10 against cost 7/10 nets out as not worth retrieving.

**Apply at Pabau:** Pabau should treat technical efficiency (crawl efficiency, response times, clean URL/asset structure, pruned low-value pages) as directly competing with content quality for ranking chances — a technically expensive-to-crawl site full of good content can still lose to a technically cheaper, well-structured competitor, so cost-reduction work is part of the same ranking equation as content quality.

**Apply anywhere:** You should treat technical efficiency (crawl efficiency, response times, clean URL/asset structure, pruned low-value pages) as directly competing with content quality for ranking chances — a technically expensive-to-crawl site full of good content can still lose to a technically cheaper, well-structured competitor, so cost-reduction work is part of the same ranking equation as content quality.

### 16. Google's index is stratified into four link-equity tiers  `20.1`
*core · content insights · source 20*

The Google API leak revealed the index isn't one undifferentiated database but is stratified into four tiers — high, medium, low, and a separate 'fresh docs' bucket — and link equity is applied on a sliding scale depending on which tier the linking page lives in, not as a flat, uniform value. This directly contradicts the old assumption that a link's value is independent of whether the linking page itself ranks or gets traffic. The proxies for identifying which bucket a page sits in are whether it's an editorial/news-style site, and whether the page itself ranks well and gets real traffic — a page buried on page 52 of results likely sits in the cheapest, lowest-value storage tier and passes minimal link equity regardless of its raw backlink profile.

> "the index is stratified into four different buckets"

**Evidence:** Direct claim from analysis of the leaked API documentation, DOJ antitrust testimony, and Mark Williams Cook's discovered API access: 'seeing that there's also a sliding scale of link equity was a new piece of information for me,' with editorial/news sites and pages that rank-and-get-traffic given as the practical proxies for tier membership.

**Apply at Pabau:** When evaluating a potential link source for Pabau, David should weight whether the specific linking page itself ranks and gets real traffic far more heavily than any DA/DR score, since the leak confirms link equity is scaled by which index tier that page lives in, not distributed uniformly.

**Apply anywhere:** When evaluating a potential link source for your own site, you should weight whether the specific linking page itself ranks and gets real traffic far more heavily than any DA/DR score, since the leak confirms link equity is scaled by which index tier that page lives in, not distributed uniformly.

### 17. Inspect rendered HTML on JavaScript-built SaaS marketing sites  `108.11`
*core · concrete actions · source 108*

Grow and Convert flag JavaScript rendering as a SaaS-specific risk because so many SaaS marketing sites run on custom platforms or React-based frameworks. When content loads dynamically, Google may not see or index it, and no amount of content quality compensates. Their check is Search Console's URL Inspection tool, which shows how Google actually renders the page. If the rendered HTML is missing content you expect to be there, that is a rendering problem, and they name three fixes: implement server-side rendering, use dynamic rendering for search engine bots, or restructure how the content loads. This is worth running as a first-week check on any site whose front end was built by a product team rather than on a standard CMS, since the failure is invisible in a browser.

> "many SaaS marketing sites are built on custom platforms, React-based frameworks"

**Evidence:** Grow and Convert's stated remedies: server-side rendering, dynamic rendering for search engine bots, or restructuring how content is loaded.

**How to do it**

1. List every template on the marketing site: homepage, feature page, solutions page, blog post, listing page.
2. Run one representative URL per template through Search Console URL Inspection and open the live test.
3. Read the rendered HTML, not the screenshot, and search it for your H1, body copy and internal links.
4. Flag any template where expected content is absent from the rendered HTML.
5. Repeat for a page whose main content loads behind a tab, accordion or infinite scroll.
6. Hand failures to engineering with the specific missing elements quoted.
7. Choose the fix per template: server-side rendering, dynamic rendering for bots, or moving the content into the initial HTML.
8. Re-inspect after deployment and confirm the content now appears in rendered HTML.
9. Add this check to the release checklist so a future front-end change cannot silently reintroduce it.

**Tools:** Google Search Console

**Pitfall:** The page looks perfect in a browser, so nobody checks. The tell is a page that gets crawled and indexed but ranks for nothing, because the indexed version is a shell.

**Apply at Pabau:** Pabau should run URL Inspection across one URL per template, including template pages and code-reference pages, and confirm the tables and body copy appear in the rendered HTML rather than only in the browser view.

**Apply anywhere:** On any JavaScript-heavy marketing site, run one URL per template through Search Console's URL Inspection and read the rendered HTML. If expected content is missing, fix it with server-side rendering or by moving the content into the initial HTML.
