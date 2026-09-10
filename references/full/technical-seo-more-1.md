# Technical SEO — supporting (part 1 of 2)

20 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. "We don't like your content" may really mean no one links to you  `22.3`
*useful · content insights · source 22*

Addressing pages stuck in "Crawled – currently not indexed" or "Discovered – currently not indexed" in GSC, David Kaid notes Google's own videos this year (from the Google Switzerland team) attribute this to "we don't like your content" — but he infers this really means no one is linking to the page, with Google using that absent external validation as its proxy for "quality is no good," rather than a literal judgment on the writing. His supporting logic: requesting a manual crawl on the stuck page in GSC returns "I've read the page, this can be indexed" almost immediately, yet the page still isn't indexed — showing Google can technically parse and approve the content while still withholding indexing, pointing to an authority/linking gap rather than a readability defect.

> "no one's linking to you, therefore we think the quality"

**Evidence:** Google's own 2026 videos from the Switzerland/Google team citing "content quality" as the stated reason, contrasted with the described GSC manual-crawl behavior (instant "can be indexed" feedback with no actual indexing).

**Apply:** When troubleshooting a page stuck in "Crawled/Discovered – currently not indexed," check first whether the page or its topic has any inbound links or topical authority behind it before defaulting to rewriting the prose, since the indicated fix is building links/relevance, not polishing the writing.

### 2. After updating a page, bump its date and request reindexing  `31.4`
*useful · concrete actions · source 31*

Once the new sections and internal link are in place, reread the article's introduction and rewrite it if needed so it accurately reflects all the new content just added. Then update the page's published/updated date to reflect that a substantial content update just occurred, and finally use Google Search Console's URL Inspection ('inspect') tool on that URL to submit a request for indexing, prompting Google to recrawl the page rather than waiting for its normal schedule.

> "update your date published, because you literally just added"

**How to do it**

1. After finishing content additions, reread the article's introduction and rewrite it if needed so it accurately reflects all the new sections just added.
2. Update the page's published or last-updated date/metadata to reflect that a substantial content update just occurred.
3. In Google Search Console, open the URL Inspection ('inspect') tool on the specific URL you just updated.
4. Submit a request for indexing directly from the URL Inspection panel so Google is prompted to recrawl the page promptly.
5. Treat this three-step close-out (refresh intro, bump date, request reindex) as the standard final checklist for any substantial content update. (inferred)

**Tools:** Google Search Console

**Pitfall:** Making a substantial content update without also updating the visible published/updated date and requesting reindexing means Google may take much longer to recrawl and recognize the improvements, delaying any ranking benefit from the update.

### 3. Audit canonicals where one page is reachable through several URL patterns  `108.25`
*useful · concrete actions · source 108*

Grow and Convert flag canonicalization as a SaaS-specific issue because the same content is often reachable through several URL variations: with and without trailing slashes, with different query parameters, and over HTTP and HTTPS. Without correct canonical tags, search engines may split ranking signals across the versions or index the wrong one. They acknowledge most modern CMS platforms handle basic canonicalization automatically, so the work is auditing rather than implementing, and they name the three places it usually breaks: pagination, filtered views, and content that appears in more than one place on the site. Splitting signals is the quiet failure here. Nothing errors, the page simply performs below what its links should buy, which is easy to misdiagnose as a content or authority problem.

> "the same content can often be accessible through different URL variations"

**Evidence:** Grow and Convert name trailing slashes, query parameters and HTTP versus HTTPS as the URL variations that split SaaS ranking signals.

**How to do it**

1. Crawl the site and export every URL with its declared canonical.
2. Request each key page with a trailing slash, without one, over HTTP and over HTTPS, and confirm all four declare the same canonical.
3. Append a tracking parameter to a page and confirm the canonical still points at the clean URL.
4. Check paginated series so page two does not canonicalize to page one unless that is intended.
5. Check filtered or faceted views and confirm they canonicalize to the unfiltered page or are blocked.
6. Find content published in more than one location, such as a resource that also appears in a hub, and pick one canonical.
7. Fix any page that canonicalizes to itself while a near-duplicate does the same.
8. Re-crawl after the fixes and confirm the duplicate clusters have collapsed to one indexable URL each.

**Tools:** Screaming Frog, Google Search Console

**Pitfall:** Assuming the CMS handles it. Pagination, filtered views and syndicated-in-two-places content are the three cases where the default breaks, and the symptom is a page underperforming its link profile with no error reported anywhere.

**Apply at Pabau:** Pabau should run this check across the generated sections, since template, diagnostic-code and procedure-code pages are the most likely to be reachable through parameters or listed in more than one hub.

**Apply anywhere:** Audit canonicals rather than assume the CMS handles them. Test each key page with and without a trailing slash, with parameters, and over both protocols, then check pagination, filtered views and any content published in two places.

### 4. Audit hidden over-optimization in schema and meta, not just visible copy  `10.14`
*useful · best practices · source 10*

Keyword over-optimization often hides in places invisible on the rendered page, such as schema markup, meta tags, and table-of-contents anchor text, so auditing only what a visitor sees will miss it. Charles's concrete example is a page that appeared to have 54 variations of an exact-match anchor when viewed normally, but the raw source code contained 214 variations once schema and hidden markup were counted, a gap invisible without checking the code directly. His fix, repeated across many client audits, is to strip excess exact-match mentions out of schema markup and out of the table of contents specifically, bringing the true keyword-variant count down to what's actually needed rather than the 100-plus that over-optimizes the page under the hood.

> "it has 54 variations of an exact-match anchor"

**How to do it**

1. View the page normally as a visitor and count visible exact-match keyword or anchor variations in the copy.
2. View the page's raw source code, using the browser's View Source or DevTools, and separately count every exact-match keyword instance inside schema markup such as JSON-LD, meta tags, and the table of contents or anchor links.
3. Compare the two counts; a large gap, such as 54 visible versus 214 in source, signals hidden over-optimization.
4. Open the page's schema markup (JSON-LD block) and remove redundant exact-match keyword repetitions that aren't functionally necessary.
5. Open the table of contents or anchor-link structure and trim repeated exact-match anchor text down to natural variation.
6. Re-crawl or re-view-source the page after edits to confirm the hidden keyword count has dropped to a reasonable level relative to the visible copy.
7. Apply this same visible-versus-source audit across other high-priority pages, not just ones already suspected of over-optimization (inferred scaling step).

**Tools:** browser view-source / DevTools

**Pitfall:** Over-optimization audits that only look at the rendered page will miss the problem entirely — the worst stuffing can live entirely in schema, meta tags, and table-of-contents markup that's invisible unless you check the raw source code.

### 5. Audit robots.txt for staging rules that block the whole blog  `108.12`
*useful · concrete actions · source 108*

Grow and Convert report seeing robots.txt files left over from a staging environment that were blocking the entire blog, and cases where overly aggressive rules stopped search engines reaching key content. Their framing of the file is two-sided: confirm it is not blocking anything that should be indexed, such as the blog and landing pages, and confirm it is blocking what should not be, such as admin pages, internal search results and duplicate filtered views. For most SaaS sites the bigger risk is the first, since a staging disallow that survived launch produces a site that simply never ranks and offers no obvious symptom other than absent traffic. This is a five-minute check that should run after every deployment or platform migration, not once a year.

> "a robots.txt file left over from a staging environment"

**Evidence:** Grow and Convert have seen leftover staging robots.txt files block an entire blog at client sites.

**How to do it**

1. Open /robots.txt on the live domain and read every Disallow line.
2. Test your blog path, landing page paths and sitemap URL against the rules.
3. Remove any blanket Disallow that survived a staging or pre-launch configuration.
4. Confirm admin paths, internal search result URLs and filtered or faceted views are disallowed.
5. Confirm the sitemap URL is declared in the file.
6. Cross-check in Search Console that no important URLs report as blocked by robots.txt.
7. Add a post-deployment step that fetches /robots.txt and fails the release if a global disallow appears.
8. Re-run the whole check after any CMS or hosting migration.

**Tools:** Google Search Console

**Pitfall:** A staging disallow that ships to production gives no error anywhere. The only signal is traffic that never starts, which teams usually misread as a content problem.

**Apply at Pabau:** Add a robots.txt read to Pabau's release checklist, since /blog/, /templates/, /diagnostic-codes/ and /procedure-codes/ all need to stay crawlable and each ships through the same deployment path.

**Apply anywhere:** Read your live robots.txt line by line. Remove staging leftovers that block content sections, keep admin, internal search and filtered views blocked, and add a post-deploy check so a global disallow can never ship unnoticed.

### 6. Clear six recurring SaaS technical faults before content spend  `181.4`
*useful · best practices · source 181*

Grow and Convert run a fixed technical checklist upfront on SaaS sites, on the argument that these issues undermine results regardless of content quality. The six they name are: a blog hosted on a subdomain instead of a subfolder, JavaScript rendering problems, incorrect canonical tags, missing XML sitemaps, slow page speed, and poor Core Web Vitals. The list is worth treating as a SaaS-specific starting audit because these faults cluster in that market: marketing sites are often built on a JavaScript framework by a product team, and blogs are often bolted on with a hosted platform on a subdomain. They then monitor for the same issues on an ongoing basis rather than treating the audit as a one-off, so a later replatform does not silently reintroduce a fault.

> "blog hosted on subdomain instead of subfolder"

**Evidence:** Grow and Convert name these six as the issues that undermine SaaS companies regardless of content quality, and monitor them on an ongoing basis.

**How to do it**

1. Check whether the blog sits on a subdomain, and if it does, plan the move to a subfolder before commissioning articles.
2. Fetch key templates rendered and unrendered to confirm the main content and links exist without JavaScript execution.
3. Crawl the site and list every page whose canonical points somewhere other than itself, then confirm each of those is intentional.
4. Confirm an XML sitemap exists, is current, is referenced in robots.txt and is submitted in Search Console.
5. Run Core Web Vitals on the field data in Search Console rather than lab scores alone, and fix the failing template rather than individual pages.
6. Put the same six checks on a recurring monthly crawl so a redeploy cannot reintroduce them unnoticed.

**Tools:** Google Search Console, Screaming Frog

**Pitfall:** Treating the technical audit as a one-time project. SaaS marketing sites get replatformed and redeployed often, and a fixed canonical or a subfolder blog can silently revert.

**Apply at Pabau:** David should run this six-point check across pabau.com on a monthly crawl, with particular attention to canonical tags on template and code-reference pages, where near-duplicate templates make wrong canonicals easy to introduce.

**Apply anywhere:** Run a fixed six-point technical check (subfolder blog, JS rendering, canonicals, sitemap, page speed, Core Web Vitals) before content spend, and repeat it monthly so redeploys cannot reintroduce a fault.

### 7. Clear technical blockers before publishing, then close the workstream  `179.11`
*useful · concrete actions · source 179*

Grow and Convert describe the sequencing they use rather than the volume of technical work. Every client engagement opens with an SEO audit checking for technical issues that could hurt ranking. They then either fix those issues or hand the fixes over to the client, and this happens before any publishing starts. The framing they attach matters more than the audit itself: technical work is something to get out of the way so the content can rank for the high-value keywords, not something to extend for as long as possible to keep charging the client. Link building follows the same subordinate logic, done throughout the engagement only as much as necessary to get the target content ranking. Both are explicitly secondary to the two priorities they say take 90% of their time.

> "not something to extend for as long as possible"

**Evidence:** Grow and Convert spend 90% of their time on buying-intent keyword selection and dedicated page production, with technical SEO and link building explicitly in service of those two.

**How to do it**

1. Run one technical audit at engagement start and scope it to issues that could block ranking, not to a full checklist.
2. Split findings into blockers and non-blockers, and only treat blockers as prerequisites to publishing.
3. Fix or assign every blocker with a named owner and a due date before the first article goes live.
4. Declare the technical workstream closed once blockers are cleared, and move the hours to keyword work and page production.
5. Reopen technical work only when a specific target page fails to rank for a reason the audit explains.
6. Start link building only after target pages are published, and point links at those pages rather than at the site generally.
7. Stop link building on a page once it ranks in positions one to three for its target keyword.

**Pitfall:** Letting technical remediation run as a standing monthly line item. Most fixes are one-time, so an open-ended technical workstream consumes the budget that should be buying pages targeting revenue keywords.

**Apply at Pabau:** For pabau.com, technical work should be batched into a pre-publishing sprint with a completion date rather than run alongside content month after month. Reopen it only when a specific page's ranking failure points back to a technical cause.

**Apply anywhere:** Run one technical audit at the start, separate blockers from non-blockers, fix the blockers before publishing, then close the workstream and move those hours into keyword selection and page production. Reopen it only when a specific page fails to rank for a reason the audit explains. Do the same with links: build them at published target pages, and stop once the page reaches the top three.

### 8. Clear the Ahrefs Site Audit health score before pushing new content  `139.12`
*useful · concrete actions · source 139*

Alongside the content work, Brandon cleaned the site's technical issues, on the reasoning that a strategy built on capturing organic traffic needs a clean structure so Google can discover and navigate the site, and that a cleaner structure lifts both old and new pages. His method was deliberately simple and he says anyone can run it without being an SEO specialist: open Ahrefs, click Site Audit, read the Health Score and the list of technical issues, then work through the pages flagged and follow Ahrefs' own instructions for resolving each. Devesh notes in the article that Grow and Convert do these technical cleanups for agency clients but do not teach them in the content marketing course, so this sits alongside the content method rather than inside it.

> "you can get a quick "Health Score" grade"

**Evidence:** Brandon ran this cleanup as part of the program that took Keeper Tax from ~10,000 monthly visitors to 400% growth in 3.5 months.

**How to do it**

1. Set up the site as a project in Ahrefs and run Site Audit before the content program starts.
2. Read the Health Score and sort the issue list by severity.
3. Work top-down through the errors, opening the affected URLs and applying Ahrefs' stated fix for each.
4. Prioritize anything blocking crawling or indexing over cosmetic warnings.
5. Re-crawl after the fixes and confirm the Health Score has moved.
6. Schedule the audit to re-run on a recurring basis so new issues surface as content ships.
7. Fix regressions from each publishing batch before starting the next one.

**Tools:** Ahrefs

**Pitfall:** Treating the health score as the goal leads to hours spent on low-severity warnings. Fix the crawl and index blockers, then get back to content.

**Apply at Pabau:** Pabau should keep a scheduled Site Audit running and clear crawl and index errors before each batch of new /blog/ or /templates/ pages goes live, so the new pages inherit a clean structure.

**Apply anywhere:** Run a site audit crawl before starting a content program, fix the crawl and index blockers first, and re-run it on a schedule as new pages ship.

### 9. Crawl the site with Screaming Frog, audit plugins for empty pages  `23.4`
*useful · concrete actions · source 23*

Edward includes basic technical health checks as a recurring new-site task: confirm the site is crawlable and fast, and specifically review SEO metadata across the whole site as a list rather than page by page, to catch inconsistencies. His named tools are Screaming Frog, which he calls 'excellent,' for a full site crawl, and testing individual pages directly in Google Search Console; he also flags checking CMS plugins specifically to make sure they aren't auto-generating empty or useless pages, such as archive pages that serve no purpose for users or SEO.

> "You can use Screaming Frog — Screaming Frog is excellent"

**How to do it**

1. Run a full Screaming Frog crawl of the site to check crawlability, page speed indicators, and site-wide technical issues.
2. Export all page titles and meta descriptions into a single spreadsheet/list view to scan for duplicates, missing tags, or inconsistent patterns.
3. Use Google Search Console's URL Inspection tool to test a sample of individual pages for indexing/crawlability issues.
4. Review your CMS's active plugins to check whether any are creating empty or low-value pages such as bare archive pages.
5. Disable or reconfigure any plugin found to be auto-generating empty/thin pages, and no-index or remove the resulting pages (inferred remediation step).

**Tools:** Screaming Frog, Google Search Console

### 10. Do not fund open-ended technical SEO work before BOFU pages exist  `105.10`
*useful · general insights · source 105*

Grow and Convert take a deliberately unfashionable position on technical SEO for lead generation. They accept that bad UX and poor page performance hurt ranking chances, but say most modern websites are already fine for SEO. Their advice is to check site speed, confirm the site uses basic modern web design, and stop there. They then report client experience directly: many clients described endless investments in technical SEO and audit work before working with them that did not do much, and they tell readers to be wary of budget going into never-ending technical projects. The sequencing argument is the load-bearing part. If your bottom-of-funnel keywords are not defined and you have no dedicated articles targeting them, no volume of audits or speed work will get you ranking for your highest-converting terms.

> "Be wary of spending budget on never-ending technical SEO projects"

**Evidence:** Grow and Convert report many clients arrived having spent heavily on technical SEO and audit work beforehand that did not move results, based on work with dozens of companies over 10+ years.

**Pitfall:** Technical audits generate long finding lists that always look urgent, so the work never ends and never gets sequenced against content. The signal is a site with a clean audit score and no page targeting its most commercially valuable query.

**Apply at Pabau:** Pabau should spend on technical work only where a real problem is measured, and treat missing bottom-funnel pages as the higher priority. David should check that every high-intent term has its own dedicated page before commissioning another site-wide audit.

**Apply anywhere:** Run a basic site speed and modern-design check, fix real measured problems, then stop. Before funding another audit, confirm every high-converting buying-intent keyword already has a dedicated page targeting it, because audits cannot rank a page that does not exist.

### 11. Don't add a CDN below 300 clicks/30 days  `18.13`
*useful · best practices · source 18*

The rule of thumb given is concrete: a page needs roughly 300 clicks within a rolling 30-day window before it can even populate a Chrome UX Report (CrUX), the real-user-performance data set that would justify a speed intervention. Below that threshold (the source's example: 'three clicks a day'), adding a CDN is framed as pure cost, time, and engineering overhead that 'won't deliver anything' and can even slow the site down due to the added network hops. The source (a former head of marketing at a load-balancing company that scaled from 20 million to 250 million dollars in six years) argues speed only becomes a real ranking/UX lever at genuine scale and for specific usage contexts like mobile users on the go, not for a brand-new low-traffic site.

> "you need around 300 clicks in 30 days"

**How to do it**

1. Before investing in a CDN or deep page-speed engineering work, check whether the site/page can generate data in the Chrome UX Report (CrUX).
2. Pull current traffic for the pages in question from Google Search Console or Analytics to see if they clear roughly 300 clicks in a rolling 30-day window. (inferred check via GSC/GA)
3. If traffic is well below that threshold, deprioritize CDN adoption and speed engineering, treating it as cost/time/engineering burden with no measurable payoff at that traffic level.
4. If the site does clear the threshold and has real scale, evaluate CDN adoption on its merits, weighing the extra network hops it introduces against the performance gain.
5. Reserve serious speed optimization for sites/pages with real scale and mobile-heavy usage patterns, since that's the context where speed genuinely affects user behavior.
6. Revisit this decision as traffic grows rather than treating 'add a CDN' as a default best practice for every new site.

**Tools:** Chrome UX Report (CrUX), Google Search Console

**Pitfall:** Adding a CDN to a brand-new, low-traffic site as a default 'best practice' — this adds engineering/cost burden and extra network hops while delivering no measurable benefit below the ~300-clicks/30-days threshold, and can even slow the site down.

### 12. Fix a very poor PageSpeed score, then stop working on speed  `153.11`
*useful · best practices · source 153*

Grow and Convert's position on page speed is a floor, not a target. Check the site with Google PageSpeed Insights. A high or green score is not necessary for most sites to rank well, but if the score is very poor, make improvements. Beyond that, do not obsess. They allow one exception: speed matters for extremely competitive commercial keywords, and their example is 'buy flowers online'. For most companies targeting a wide range of keywords, topical relevance, intent match and content quality matter far more. Their instruction on where to redirect the attention is specific: whether the content fulfills search intent, and how many links it has.

> "Just don't obsess over page speed"

**Evidence:** Grow and Convert, from 80+ clients since 2017: a green score is unnecessary for most sites, with speed only mattering on extremely competitive terms such as 'buy flowers online'.

**How to do it**

1. Run the site's main templates through Google PageSpeed Insights once.
2. Only act if a score is very poor, rather than chasing a green score.
3. Fix the largest single cause first, usually uncompressed images or render-blocking scripts.
4. Re-test, confirm the score is no longer in the poor band, and close the work.
5. Confirm the site is navigable, modern-looking and works on both desktop and mobile.
6. Exempt only your most competitive commercial pages, where speed is worth further tuning.
7. Redirect the remaining engineering time to intent match and link acquisition.
8. Re-check the templates once a year rather than monitoring continuously.

**Tools:** Google PageSpeed Insights

**Pitfall:** Chasing green Core Web Vitals scores on a blog. It absorbs engineering weeks and moves nothing, because the SERP is decided on relevance and links.

**Apply at Pabau:** Pabau should set a one-time floor on the /blog/ and /templates/ templates and then leave speed alone. David should not let performance work displace intent and originality work in the content roadmap.

**Apply anywhere:** Run your templates through PageSpeed Insights once, fix anything scoring very poor, confirm the site works on mobile and desktop, then stop. Only your most competitive commercial pages justify further speed tuning.

### 13. Fix the subdomain blog while the new content is still ranking up  `136.14`
*useful · concrete actions · source 136*

The traffic recovery at Leadfeeder was not from content alone. Grow and Convert say the rebound after the post-switch dip was aided largely by a technical SEO fix: moving the blog from blog.leadfeeder.com to leadfeeder.com/blog/. From there, they report that traffic and conversion metrics accelerated and new posts ranked with greater and greater ease. The sequencing point is the useful part, and it is not covered by the subdomain entries already in the base. They made the move during the transition, while the bottom-funnel posts were young and still climbing, so every new page published afterwards inherited the main domain's authority rather than needing the migration repeated later. Over the following year organic traffic passed 21,000 monthly visitors.

> "aided largely by a technical SEO fix of moving the Leadfeeder blog"

**Evidence:** Leadfeeder's move from blog.leadfeeder.com to leadfeeder.com/blog/ was credited with the traffic rebound after the strategy switch; organic traffic later passed 21,000 monthly visitors.

**How to do it**

1. Check whether the blog sits on a subdomain rather than a subfolder before planning any content program.
2. If it does, schedule the move to /blog/ at the start of the content push, not after a year of publishing.
3. Map every existing post URL to its new subfolder URL one-to-one, with no chained redirects.
4. Implement server-side 301s and keep them permanently, not for a fixed period.
5. Add both the subdomain and the root domain as separate Search Console properties before the move so you can compare.
6. Update internal links, sitemaps and canonical tags to the new URLs rather than relying on the redirects.
7. Expect rankings to settle over roughly a month and traffic over about three, and do not publish structural changes in the same window.
8. Publish all new pain point posts to the subfolder from day one.

**Tools:** Google Search Console

**Pitfall:** Leaving the move until the program is working. You then migrate a large set of ranking commercial pages, which is a far riskier operation than moving a small blog early.

**Apply at Pabau:** Pabau's blog already sits at pabau.com/blog/, so the transferable rule is to keep every new content type in a subfolder of pabau.com. Template and code-reference pages should never be launched on a separate subdomain or a marketing microsite.

**Apply anywhere:** If your blog sits on a subdomain, move it to a subfolder at the start of a content program rather than after it works. New pages then inherit the main domain's authority instead of needing a riskier migration later.

### 14. Google triages crawled URLs into authority-based crawl pools  `53.1`
*useful · general insights · source 53*

David Quaid describes how Google's crawler doesn't simply read a sitemap and crawl every URL in it; the bot that reads your sitemap instead adds those URLs to a separate crawl list, which then gets triaged into a number of authority-based "pools" — he says it used to be three pools and is now more like five, though the exact number isn't published. Pages with no authority land in a more diluted pool that gets crawled less frequently, since more pages are assigned per crawl-bot visit there, so each individual page gets hit less often, while higher-authority pages sit in pools with fewer pages per bot, meaning they get crawled faster and more often. This reframes "getting crawled" as a page-level authority competition rather than a simple, uniform sitemap-driven crawl, which is the myth he opens the episode by debunking.

> "there's basically a number of pools — it's triage"

**Evidence:** David Quaid's direct description: "there's basically a number of pools — it's triage. Used to be three, now it's more like five," with lower-authority pages going into a diluted pool that gets fewer bot visits per page, and higher-authority pages getting crawled faster.

**Apply:** When prioritizing technical SEO or new-page indexing efforts, David should think in terms of which authority pool a page likely sits in rather than assuming sitemap submission alone guarantees prompt, frequent crawling — building a page's authority through internal linking from pages that already rank is what moves it into a faster-crawled pool.

### 15. Link-equity calculation and query-time ranking are separate Google systems  `38.4`
*useful · general insights · source 38*

Kalin explains a common misconception: that earning backlinks and ranking well are part of one unified process. In his description, Google first computes PageRank for the entire web as a massive batch calculation (too computationally heavy to run in real time), distributing link juice everywhere; only afterward, at query time, does Google filter candidate pages by whether they clear a PageRank threshold and then rank within that filtered set by relevancy and other signals. Because of this two-stage structure, a link from a PBN (or any site) passes its calculated equity regardless of whether that PBN or its target ever ranks for anything — the only way to actually lose link equity is if the linking domain itself is flagged as toxic (e.g., a domain otherwise, not just topically, associated with spam).

> "ranking and getting link juice are somehow part of the same algorithm"

**Evidence:** Direct explanation: 'The PageRank algorithm distributes all the PageRank, basically gives link juice to everyone, and then when a user does a search query, Google filters websites by PageRank... These calculations are way too big to happen in real time.'

**Apply:** When evaluating whether a link placement or internal linking change 'worked,' remember ranking movement and link-equity transfer are not the same signal — a page can fail to rank for reasons unrelated to whether the links pointing at it passed value, so don't diagnose backlink quality solely from whether the linked page currently ranks.

### 16. Manual actions hit the whole site for one hacked page  `54.4`
*useful · content insights · source 54*

Even though the investigation proved only a single URL (the non-canonical www homepage) had actually been compromised, the manual action Google issued the next morning was for 'major spam problems' and explicitly stated it 'affects all pages' of the site, describing 'aggressive spam techniques such as scaled content abuse, cloaking, scraping content from other websites, and/or repeated or egregious violations.' Glenn notes it's notable that Google used that broad, severe language and site-wide scope when the underlying cause was one hijacked homepage variant, not a pattern across the site's actual content.

> "it was for 'major spam problems' impacting the entire site"

**Evidence:** Glenn Gabe's diagnosis traced the entire manual action back to a single hacked URL (the https-www homepage redirecting to a gambling site), yet Google's notice was issued at the whole-site level, labeled 'major spam problems,' and explicitly said 'Affects all pages.'

**Apply:** Don't take a manual action's stated scope or severity language as a precise diagnosis - treat labels like 'major spam problems' and 'affects all pages' as Google's generic, site-level enforcement wrapper, and always do your own page-by-page GSC investigation to find the actual, possibly much narrower, root cause before deciding what to fix or how to word a reconsideration request.

### 17. Manual-action and recovery status both lag real index state  `54.5`
*useful · content insights · source 54*

After the reconsideration request was filed, Glenn checked with a direct site: search the next morning and found every page already back in the SERPs - hours before his client had received any official word back from Google. The formal 'reconsideration request approved, manual action lifted' message only showed up in Search Console and via email a few hours later. This mirrors the earlier lag in the opposite direction: the site had already been de-indexed and the hacked page was already redirecting traffic before any manual action notice existed in GSC, which didn't arrive until the following morning.

> "showing back up in the SERPs via site query"

**Evidence:** Glenn's own timeline: pages reappeared in live Google search results (confirmed via a manual site: query) before Google's official reconsideration-approved notification reached Search Console and email a few hours later; the initial manual action itself had similarly arrived only after the site was already being impacted.

**Apply:** Don't wait for an official Search Console or email notification to know your real-world index status in either direction - proactively re-check with a direct site: search (or rank tracker) after making a fix and filing reconsideration, since actual reinstatement in the SERPs can precede Google's formal confirmation by several hours, letting you inform stakeholders sooner.

### 18. Never run interstitial or pop-up ads; Google will derank the site  `74.9`
*useful · best practices · source 74*

David Quaid flags the starter guide's line about avoiding distracting advertisements, especially interstitial pages, and says Google has a whole page dedicated to it that is worth reading. His instruction is unambiguous: if you are running a pop-up ad, stop doing it, because Google will absolutely derank your site. He raises it early in the walkthrough as one of the few things in the guide that is genuinely penalizable, contrasting it with the long list of things people worry about that are not. It sits alongside his framing that the document listing what is actually penalizable is one of the two primary references anyone should read. He distinguishes the ad interstitial from ordinary site features; the problem is the ad that blocks the content the searcher arrived for.

> "If you're doing a pop-up video, stop doing it, right? Sorry, pop-up ad"

**Evidence:** David: Google has a whole page about interstitials and will 'absolutely derank your site' for pop-up ads.

**How to do it**

1. Load ten of your top landing pages on a mobile device from a Google result, not from a bookmark.
2. Note every overlay that appears before the main content is readable, including ad interstitials and full-screen promos.
3. Remove any overlay that covers the content on arrival from search.
4. Move newsletter and demo prompts to inline blocks or exit-intent behaviour instead of an entry interstitial.
5. Read Google's dedicated page on intrusive interstitials and check your remaining overlays against its examples.
6. Re-test after the change on both mobile and desktop, since mobile is where interstitials are judged most harshly.

**Pitfall:** Assuming a small cookie or age-gate banner is the same as an ad interstitial. The deranking risk is about ads that block the content a searcher clicked through for.

**Apply at Pabau:** Pabau's demo-booking prompts should stay inline or exit-intent on /blog/ and /templates/ pages. David should check the mobile experience of a search click landing on a blog post and remove anything that covers the opening prose run.

**Apply anywhere:** Remove any ad overlay that blocks content on arrival from search, and check the mobile experience by clicking through from a real Google result.

### 19. On-site schema and llms.txt tweaks barely move the needle  `12.9`
*useful · best practices · source 12*

Devesh's take on tier-three, on-site GEO tweaks, meaning schema, llms.txt, FAQ-format headings, and bullet-point summaries, is that they 'don't seem to be really necessary' - the majority of Grow & Convert's clients get great AI visibility without using any of them, because LLMs 'don't need help reading.' His analogy is that these models can pass the US bar-equivalent LSAT and solve complex physics problems without content being dumbed down into bullet points and FAQs first, so a normal, well-written marketing page is already perfectly parseable to them. His caveat is not an outright ban: doing these tweaks is low-effort and there's no evidence they hurt, so they're fine as optional polish, but his warning is specifically against treating them as your entire GEO strategy.

> "They pass the LSAT, they can do complex physics"

**How to do it**

1. Deprioritize schema markup, llms.txt files, FAQ-format headings, and bullet-point summaries as GEO-specific initiatives - don't schedule dedicated sprints for these ahead of owned bottom-of-funnel content production.
2. Before implementing any specific on-site tweak such as llms.txt, check for current, credible evidence a major LLM vendor actually consumes it, rather than assuming a commonly-repeated recommendation means all vendors act on it.
3. If your team has spare low-effort capacity, implement these tweaks as harmless polish, since there's no evidence they cause damage.
4. Never let on-site tweaks substitute for building bottom-of-funnel owned content and earning off-site mentions - audit your GEO roadmap to confirm tier-three items are a minority of total effort, not the plan itself.
5. Write marketing and product pages in normal, clear human language rather than over-engineering them into fragmented bullet or FAQ formats purely for machine consumption, since well-written prose is already within LLM reading comprehension.

**Pitfall:** If your entire GEO strategy consists of on-site tweaks like llms.txt, schema, and FAQ formatting, Devesh's blunt assessment is 'good luck' - these tweaks help LLM crawlers parse content that's already there, but do nothing to make an LLM aware of or associate your brand with your product category in the first place.

### 20. Page-level authority decides how fast a changed page gets re-indexed  `45.7`
*useful · content insights · source 45*

David describes, using his own informal term 'index manager' (which he explicitly says he made up), a two-gate mechanism Google appears to apply when deciding how quickly to reprocess a page after a CMS switch changes its underlying HTML: first an overall file-size-change check, then a CRC check that evaluates the structural change to the document. Pages belonging to sections with very high authority get to jump the queue and be reprocessed quickly regardless of how much the HTML changed, but authority is calculated at the individual page level, not the whole domain — so a site where 90% of traffic flows through only 5 of 250 pages will treat those other 245 pages as low-authority, meaning when their HTML changes significantly they pass through the size/CRC gates with less scrutiny and get bulk re-indexed essentially as if for the first time in a long while.

> "The next is a CRC check, which is more about the structure"

**Evidence:** David's description of a file-size-change check followed by a CRC (structural) check gating re-indexing speed, with authority calculated at the page level, illustrated by a 250-page site where only 5 pages carry 90% of traffic.

**Apply at Pabau:** David should recognize that a CMS migration doesn't re-index all of Pabau's pages equally — the small set of pages already carrying most of the site's traffic/authority get reprocessed fast regardless of HTML changes, while the large majority of lower-traffic pages are effectively re-discovered from scratch, creating real risk that some of them start cannibalizing each other or a top page once their HTML is substantially restructured.

**Apply anywhere:** You should recognize that a CMS migration doesn't re-index all of your pages equally — the small set of pages already carrying most of the site's traffic/authority get reprocessed fast regardless of HTML changes, while the large majority of lower-traffic pages are effectively re-discovered from scratch, creating real risk that some of them start cannibalizing each other or a top page once their HTML is substantially restructured.
