# Site Architecture

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Build a styled FAQ subfolder hub and submit it directly to GSC  `51.2`
*core · concrete actions · source 51*

Edward specifies an exact URL/site structure for turning grouped PAA questions into an FAQ hub: create a dedicated subfolder named after the topic (his example: /3d-printing-faq/), link that subfolder from the site footer under a 'resources' section using the plain topic name as anchor text, and build a hub page at that subfolder root listing all the grouped questions. Clicking a question on the hub page does not expand it in place — it navigates to its own dedicated page at a URL like /3d-printing-faq/[question-slug]/, each carrying the question as its H1 followed immediately by the cleaned-up Perplexity answer. He adds that the hub page itself should be visually structured with H2 headings and a proper template rather than left as a bare list of hyperlinks on a white background, and separately notes that if the site is new or low-authority and might not get crawled naturally, the whole FAQ subfolder can simply be submitted directly to Google Search Console to force discovery of every page inside it.

> "you would do a subfolder like /3d-printing-faq"

**How to do it**

1. Create a dedicated subfolder named for your topic, e.g., /3d-printing-faq/, to house all of the grouped PAA questions.
2. Add a link to this subfolder's hub page in your site footer, under a 'resources' (or similarly labeled) section, using the plain topic name as the anchor text.
3. Build the hub page at the subfolder root listing every grouped question, styled with H2 headings and a real visual template rather than a bare list of blue links.
4. Set up each individual question as its own separate page at a URL like /3d-printing-faq/[question-slug]/, not as an in-page expand/collapse element on the hub page.
5. On each individual question page, set the H1 to the exact question text, followed immediately by the cleaned, edited Perplexity answer.
6. Include the target question in the page title tag as well as the H1 and URL slug, so it appears in all three locations.
7. If the site is new or low-authority and might not get crawled naturally, go to Google Search Console and submit the FAQ subfolder directly so Google discovers every page inside it (inferred: via the sitemap/URL submission tools).

**Tools:** Google Search Console

**Pitfall:** Letting the hub page look like a plain, unstyled list of hyperlinks on a white background — Edward explicitly warns against this and says to style it properly with headings and a real template.

### 2. Build one pillar page per facet and link it both ways  `73.10`
*core · concrete actions · source 73*

Barnard's advanced layer is the pillar page system: every facet of an entity gets its own page. For himself that means one page listing every conference he has spoken at, one for every podcast he has appeared on, one for his books, one for his patents, one for his academic papers. The reason is capacity, not SEO folklore - putting all of it on the single About page overwhelms the machine and it cannot tell what is important. So the entity home keeps only the fundamental facts, then links out to each facet page, and each facet page links back to the entity home. Each facet then has its own mini entity home. He wants these pillar pages reachable from the top menu where possible; the footer works but he rates it significantly less important than the main navigation, because the top menu tells the machine which facets of the entity matter.

> "each aspect of a person has a pillar page"

**Evidence:** Barnard runs separate pillar pages for conferences, podcasts, books, patents and academic papers on his own site.

**How to do it**

1. List the facets of the entity: for a person, talks, podcasts, books, papers, patents; for a company, products, locations, leadership, press, customers.
2. Keep the entity home to fundamental facts only and move every list of items off it.
3. Build one page per facet, each page covering that facet completely and nothing else.
4. Link from the entity home to every facet page.
5. Link from every facet page back to the entity home, so each facet has its own mini entity home.
6. Put the facet pages in the top navigation menu where possible; use the footer only as a fallback.
7. Add new items to the relevant facet page rather than to the entity home, so the entity home never grows.
8. Review the top menu and ask which facets are listed that should not be, and which are missing.

**Pitfall:** Piling every credential, appearance and product onto the About page. Barnard says the machine is then overwhelmed and cannot judge importance, which undermines the entity home's only job.

**Apply at Pabau:** Pabau should treat template pages, procedure-code pages and diagnostic-code pages as facets: one hub page per facet linked from the About page and from the main navigation, with each hub linking back to About.

**Apply anywhere:** Give every facet of the entity its own pillar page, keep the entity home to fundamental facts only, and link entity home and facet pages to each other in both directions. Put the facet pages in the top menu, not just the footer.

### 3. Build the manual version first before automating or migrating platforms  `27.9`
*core · best practices · source 27*

Edward's team spent several months trying to vibe-code an entire SEO site's functionality as a WordPress replacement, and after about a month of that specific effort it was clear the better move was to simply use WordPress — a decision he still calls a wasted effort in hindsight, though Andrew frames the failed experiment itself as a necessary learning cost given how mature WordPress already is as a system. The same team applies a related pacing discipline to content growth on the site they kept on WordPress: rather than adding new bottom-of-funnel landing pages quickly, they deliberately get the pages they already have as good as possible, get them indexed, and wait until those pages are ranking well before adding more, specifically so they can observe how much authority is actually needed before scaling further. Both decisions reflect the same underlying discipline: validate a smaller, manual or already-proven approach before investing in automation or platform migration, rather than assuming a new AI-driven capability is worth building just because it's technically possible.

> "After about a month it was very clear: let's just use WordPress"

**How to do it**

1. Before committing to a platform migration or a new automated build-out, time-box a small proof-of-concept, the source's example ran about a month, rather than committing months upfront.
2. At the end of that time-box, honestly assess whether the new approach is actually faster or better than the mature tool it would replace, in the source's case WordPress.
3. If the mature tool wins, stop the migration attempt and revisit the decision on a fixed schedule, the source rechecks this specific decision annually, rather than never reconsidering it.
4. For content scaling specifically, fully optimize and index the pages you already have before publishing additional ones.
5. Wait until that existing page set is ranking well, then use the authority/ranking level observed to estimate how much more content the site can support (inferred metric: treat current ranking performance as the signal for how fast to add new pages).
6. Only then add the next batch of pages, repeating the get-good, get-indexed, get-ranking sequence rather than publishing on a fixed calendar.

**Tools:** WordPress, Elementor

**Pitfall:** Automating or migrating before you understand what you're actually trying to do wastes real time — the source lost a month building a vibe-coded WordPress replacement before concluding the mature platform was already the better tool for the job.

### 4. Cap new-site launches at 10 pages, then check indexing  `16.4`
*core · best practices · source 16*

When scaling any new satellite, resource, or programmatic site, the described rule is to publish a small initial batch of pages — "ten pages or fewer" — and confirm those pages get indexed before publishing the next batch, rather than publishing "hundreds of articles a day." This throttle is presented as the core safeguard that lets AI-assisted sites scale quickly without triggering spam or quality scrutiny: growth is paced to indexing capacity, not to how fast content can be produced. The explicit stated philosophy is simply "don't outpace the index," and it is applied consistently across their honeypot sites, third-party resource sites, and EMD builds as a general operating rule rather than a one-off tactic for a single site type.

> "start with a small website, ten pages or fewer"

**How to do it**

1. Before launching a new site or a new section of pages, set the first batch size to 10 pages or fewer.
2. Publish that first batch and wait rather than immediately queuing the next batch.
3. Open Google Search Console for the property and check the Page Indexing / URL Inspection report to confirm those specific URLs are indexed (inferred: use GSC's Pages report to see indexed vs. not-indexed count).
4. Only once that batch shows as indexed, publish the next small batch of pages.
5. Repeat the publish-then-verify-indexed cycle for each subsequent batch, slowing down or pausing if indexing visibly lags behind publishing.
6. Treat "hundreds of articles a day" as the explicit failure threshold to never approach, regardless of how fast content can be produced.
7. Apply the same throttle to new sub-sections added to an existing large site, not only to brand-new domains (inferred).

**Tools:** Google Search Console

**Pitfall:** Publishing in large daily batches — the source's explicit red flag is "hundreds of articles a day" — before earlier pages are confirmed indexed is the pattern to avoid, since it signals mass automated production rather than natural growth.

### 5. Consolidate FAQ and keyword-variant URLs that serve one intent  `66.25`
*core · concrete actions · source 66*

Pages that distribute one user need across different URLs because the questions or keywords are worded differently, not because the answer really changes. The framework's instruction is to consolidate them into the relevant canonical product, policy, support or transaction page, with a specific exception list: unless a location, audience, regulation, platform or task creates a genuinely different answer. It covers single-question FAQ URLs and near-duplicate pages created for wording, keyword or minor audience variations that one stronger canonical page can satisfy. It scores Low on click resilience, brand mention potential, business value and proprietary advantage at Low effort, with Medium citation potential. The test is precise and worth applying literally: two URLs are justified when the answer differs, and unjustified when only the question's phrasing differs. Applied honestly it usually collapses a large FAQ estate into a handful of canonical pages — and the five exceptions are exactly the cases that justify the pages worth keeping.

> "distribute one user need across different URLs because the questions or keywords are worded differently"

**How to do it**

1. Crawl the site and group FAQ and near-duplicate URLs by the answer they give, not by the question they ask.
2. Within each group, write out the answers side by side. Where the answers are the same, the group collapses to one page.
3. Check each group against the five exceptions — location, audience, regulation, platform, task — and keep separate pages only where one of them genuinely changes the answer.
4. Pick the canonical destination by role rather than by current ranking: the relevant product, policy, support or transaction page that owns the need.
5. Merge the useful content of each variant into that page as clearly labelled sections covering the different phrasings.
6. 301 every collapsed URL to the canonical page, and update internal links to point at it directly.
7. Confirm in Search Console which variants held the impressions, and watch the canonical page absorb them over the following weeks.
8. Add the retained phrasings to the canonical page's on-page copy, so the consolidation does not lose the query coverage that justified the variants.
9. Change the process that created them: route new questions to the canonical page as a section rather than to a new URL.

**Tools:** Screaming Frog, Google Search Console

**Pitfall:** Consolidating by keyword similarity instead of by answer. Two similarly worded questions can have genuinely different answers for different markets or plans, and merging those loses a real distinction — the exception list exists precisely to catch this.

**Apply at Pabau:** Group Pabau's FAQ and near-duplicate pages by the answer, then keep separate URLs only where the market, the regulation, the platform or the practice type actually changes it. Everything else folds into the feature, pricing or support page that owns the need, with redirects.

**Apply anywhere:** Group FAQ and near-duplicate pages by the answer, then keep separate URLs only where the market, the regulation, the platform or the customer type actually changes it. Everything else folds into the product, pricing or support page that owns the need, with redirects.

### 6. Freeze structural changes and settle canonicalization a month out  `45.1`
*core · concrete actions · source 45*

David Quaid's first rule for a planned site migration is to impose a content freeze roughly one month before the move — not a ban on publishing new blog posts or edits, but specifically a ban on last-minute structural changes like rejigging the site footer on the morning of the move. In that same pre-migration window, settle any unresolved canonicalization issue (e.g., trailing slash vs. no trailing slash) at least a month ahead, since Google treats any ASCII-level difference in a URL as a completely different URL, not a variant of the same one. His stated result from following this discipline consistently is getting post-migration ranking chaos down to about 1% of what it would otherwise be.

> "Put a freeze on the site a month before you migrate."

**How to do it**

1. Set a firm date one month before the planned migration and treat it as a structural freeze point for the current site.
2. Communicate the freeze to all content/dev/marketing stakeholders: no footer changes, no navigation restructuring, no template edits after this date — new blog posts and minor content edits are still fine.
3. Audit the current site for any unresolved canonicalization inconsistency, specifically whether URLs are served consistently with or without a trailing slash.
4. Pick one canonical format (trailing slash or not) and make sure every internal link, redirect rule, and canonical tag matches it before the freeze date.
5. Check for and resolve any other ASCII-level URL inconsistencies (e.g., www vs non-www, http vs https) during this same pre-freeze window.
6. Hold the freeze until the migration is complete and has stabilized, resisting the urge to make last-minute structural tweaks right before go-live.

**Pitfall:** Making structural changes (like editing the footer) on the actual day of the move — David specifically calls out doing this at '11:00 in the morning of the move' as the kind of last-minute change the freeze is meant to prevent.

### 7. GitHub's cannibalization cleanup drove a 400% traffic increase  `46.5`
*core · content insights · source 46*

On Microsoft's GitHub site, Brainlabs found blog content directly competing against commercial pages (pricing pages, sign-up pages) for the same keywords, so the blog would rank instead of the page GitHub actually wanted to convert on. The fix was a large-scale cannibalization project: regrouping and recategorizing page types across the site, including adding new categories for AI content as AI began appearing in search results, and reworking the entire blog navigation so it was clearer to both users and search engines which page should own which topic. The result, according to Travis, was a 400% increase in organic traffic for GitHub. Edward reinforces that this kind of cannibalization audit matters most once a site has hundreds or thousands of ranking pages, not for small sites, and gets even messier once international or regional language variants are layered on top.

> "led to a 400% increase in traffic for GitHub"

**Evidence:** Case study Travis presented at MozCon: Brainlabs' work for Microsoft's GitHub, where blog pages were outranking intended pricing/sign-up pages for the same keywords; recategorizing pages and reworking blog navigation, including new AI-specific categories, produced a reported 400% traffic increase.

**Apply at Pabau:** On a large site like Pabau's, run a periodic cannibalization audit of which pages rank for which money keywords, and make sure category/blog navigation clearly separates commercial pages from educational blog content — the risk and the payoff both scale with site size, so this matters more as Pabau's content library grows, not less.

**Apply anywhere:** On a large site like your, run a periodic cannibalization audit of which pages rank for which money keywords, and make sure category/blog navigation clearly separates commercial pages from educational blog content — the risk and the payoff both scale with site size, so this matters more as your content library grows, not less.

### 8. Give every FAQ its own page for KD90+ terms  `18.9`
*core · concrete actions · source 18*

The mechanism cited is Google's relevance model rewarding documents whose title/URL is maximally specific to the query — a page titled exactly 'What is a ribeye steak' is judged close to 100% relevant to that query, whereas the same content buried as FAQ item twelve on a broader 'meat market' page is only tenuously relevant. For keywords the site doesn't yet have enough authority to win as a head term (framed here as keyword-difficulty 90-plus), the tactic is to break out every individual FAQ-style question onto its own dedicated page rather than an FAQ accordion at the bottom of one page. The speaker reports a reader who applied this 'PAA hack' emailed a screenshot showing a new page ranked within 24 hours; the explicitly named failure mode is bundling multiple FAQ questions onto the same page, which dilutes topical relevance.

> "put every FAQ on its own page"

**How to do it**

1. Run your target head term through a keyword-difficulty tool (inferred: any KD tool, or an in-house tool like the one described in this source) and flag terms scoring roughly 90+ ('very high difficulty').
2. For that high-difficulty topic, pull the individual FAQ-style sub-questions people ask, e.g. from Google's People Also Ask box.
3. Instead of adding these as an FAQ accordion at the bottom of the existing high-difficulty page, create a separate standalone page/URL for each individual question.
4. Set the new page's title tag, H1, and URL slug to match the exact question as closely as possible, so the document's topical relevance to that query is as close to 100% as possible.
5. Do not bundle multiple unrelated FAQ questions onto the same standalone page — the source names this as the common mistake that blocks the tactic from working.
6. Internally link each new standalone FAQ page back to the main high-difficulty pillar page. (inferred)
7. Publish and monitor Google Search Console for the new page's indexing and ranking; the source's own example reportedly ranked within 24 hours.
8. Reserve the 'FAQs at the bottom of the same page' approach for pages that are already ranking/competing reasonably well, where it can still lift CTR through overlapping phrase strings.

**Tools:** Google Search Console

**Pitfall:** Putting all FAQ questions on the same page for a term you can't yet rank for — this dilutes the page's topical relevance and is described as 'one problem people have' that blocks the tactic from working.

### 9. Group related pages into topic folders instead of a flat URL structure  `74.4`
*core · concrete actions · source 74*

David Quaid says Google is a Unix-based system that looks at file names and folders, and that a flat folder structure hurts you a lot. His example: if you run a financial CRM app and want to answer many compliance questions, put them all in a compliance FAQ folder. The stated mechanism is that when a term appears on one page and a related page in the same folder discusses it, Google will look at those pages together. He pairs this with breadcrumbs, noting from a conversation with Edward Sturm that the parent folder name does not have to appear in the slug, which is the document name reference. So the folder is doing topical grouping work while the slug stays clean. He is emphatic on the payoff: 'Trust me, it'll do a lot better.'

> "If you take if you have a flat file system, a flat folder system, you're hurting yourself a lot"

**Evidence:** David's mechanism claim: pages grouped in a folder get evaluated together when a term on one page also appears on a sibling page.

**How to do it**

1. List every URL on the site and tag each with the topic cluster it belongs to.
2. Define one folder per cluster, named for the topic as a searcher would say it, not as the company org chart says it.
3. Move each page into its cluster folder and 301 the old URL server-side, with no redirect chains.
4. Keep the slug as the document name only; do not repeat the parent folder word in the slug.
5. Set breadcrumbs to reflect the folder so the snippet shows the topic path.
6. Cross-link pages inside a folder to each other so the cluster reads as one body of work.
7. Before adding a new page type, decide its folder first, so the structure scales instead of flattening again.

**Pitfall:** Restructuring folders without server-side 301s, or duplicating the folder word inside the slug so the URL reads as keyword repetition.

**Apply at Pabau:** Pabau already separates /blog/, /templates/, /diagnostic-codes/ and /procedure-codes/. David should push the grouping one level deeper inside /blog/ where clusters are large, so compliance, marketing and clinical-workflow posts sit in their own folders rather than one flat blog root.

**Apply anywhere:** Give each topic cluster its own URL folder, 301 legacy flat URLs into it, and keep the slug free of the parent folder's word.

### 10. One forgotten subdomain suppressed brand visibility for nine months  `45.11`
*core · content insights · source 45*

David describes a migration problem that stumped multiple agencies for nine months: a fintech company changed its root domain but left its old subdomain, which was running live applications, active on the old domain. Because the subdomain was still live, Google continued to retain and recognize the old parent domain rather than fully shifting authority and brand recognition to the new domain, so the company couldn't understand why it wasn't appearing in search for its own brand name — the old domain was effectively cannibalizing the new domain's branded search visibility. The fix was simple once diagnosed: the moment they finally shut down the last remaining subdomain on the old domain, the new domain's brand visibility began to correct itself. He also notes that for any domain-to-domain migration, Google Search Console's dedicated domain-change tool should be used, since it expedites transferring backlink/traffic authority, rather than the older link-by-link 301 approach he doesn't recommend unless you're already experienced with it.

> "showing up for their brand name, and this went on for nine"

**Evidence:** A fintech company's migration where an old subdomain, still running live applications, was left active on the old domain after a root-domain change, causing the old domain to cannibalize the new domain's branded search visibility for nine months, resolved only once the last subdomain was fully shut down.

**Apply at Pabau:** For any future Pabau domain change, David must inventory and fully retire every subdomain on the old domain, not just the main site, since even one forgotten live subdomain can suppress the new domain's brand visibility in search for many months, and should use Google Search Console's domain-change tool rather than relying only on 301 redirects.

**Apply anywhere:** For any future your site domain change, you must inventory and fully retire every subdomain on the old domain, not just the main site, since even one forgotten live subdomain can suppress the new domain's brand visibility in search for many months, and should use Google Search Console's domain-change tool rather than relying only on 301 redirects.

### 11. Plan a new site's sub-folder structure for scale, not just today's keyword  `23.1`
*core · best practices · source 23*

Edward's framework for a brand-new site starts with information architecture: before writing content, plan the sub-folder structure and internal linking pattern based on keyword research, with an explicit eye toward the site becoming a major brand rather than just ranking for one exact-match term. Concretely, this means deciding which sub-folders to launch with and how they will interlink from day one, specifically to support scaling later, and enforcing a zero-orphan-page rule so every page, especially keyword-targeting pages, has at least one internal link pointing to it from the moment it is published.

> "thinking of the information architecture, the internal linking, the sub folder structure"

**How to do it**

1. Before publishing content on a new site, map out the full sub-folder/URL structure based on your initial keyword research (e.g., /services/, /blog/, /locations/).
2. For each planned sub-folder, decide in advance which other sub-folders or pages will link into it, rather than adding internal links reactively after publishing.
3. Design the sub-folder structure with room to scale, leaving space for new categories to be added later without restructuring the whole site.
4. Maintain a running crawl (e.g., via Screaming Frog) of every published page and confirm each one has at least one internal link pointing to it, to avoid orphan pages (inferred).
5. Revisit the sub-folder plan whenever you enter a new topic area, checking it still supports the long-term brand vision rather than only the immediate keyword target (inferred).

**Tools:** Screaming Frog

**Pitfall:** Building information architecture around only the immediate exact-match keyword target rather than the site's future scale — Edward contrasts this with an EMD-style single-keyword site, warning that if the goal is to grow into a major brand, the structure needs to be planned for that scale from day one.

### 12. Stop expecting feature and solutions pages to rank for category keywords  `108.1`
*core · best practices · source 108*

Grow and Convert give three structural reasons a SaaS feature or solutions page loses to blog posts and review sites on software category keywords. First, ranking for a competitive term usually needs 50-plus supporting keywords worked in naturally, and a product page has nowhere near that much heading and body space. Second, the page exists to explain features, so there is a hard limit on how far you can bend it toward search intent. Third, category searchers want a list of options, and no vendor lists competitors on its own product page, so G2, Capterra and competitor listicles win the intent match. They stress this is not proof that Google refuses to rank you. They say several clients came to them convinced they simply could not rank, which they call untrue and a shame. Optimize those pages, but do not make them the whole strategy.

> "Core website pages have limited space to include relevant SEO keywords"

**Evidence:** Grow and Convert report multiple SaaS clients concluded Google 'just won't rank us' after agencies spent months optimizing core pages for category keywords.

**How to do it**

1. List every home, feature and solutions page and the category keyword each currently targets.
2. Search each target keyword and record the page type of the top ten results.
3. Drop the keyword from that page's plan wherever six or more results are listicles or review-site pages.
4. Keep the keyword on a core page only when landing pages already rank for it.
5. Count the supporting terms a tool suggests for the keyword; if the page cannot carry roughly 50 naturally, move the target.
6. Reassign every displaced keyword to a dedicated blog post or long-form landing page.
7. Leave the core page optimized for the term it can realistically hold, usually a narrower feature phrase.
8. Recheck the SERP page-type mix every six months, since format expectations shift.

**Tools:** Ahrefs, Semrush

**Pitfall:** Teams keep pouring links and rewrites into a solutions page for a category term the SERP has already decided should be a listicle. The signal is a page stuck outside the top 20 for a year while its blog competitors churn.

**Apply at Pabau:** Pabau should not expect its features or solutions pages to win 'clinic management software' style terms. Those SERPs are listicles and review sites. Move the category terms to blog listicles and keep the product pages targeting narrower feature phrases.

**Apply anywhere:** Do not expect product or solutions pages to rank for competitive category keywords. They lack the space for supporting terms, they exist to explain features rather than match intent, and they cannot list competitors when the SERP is full of listicles. Move those keywords to dedicated content.

### 13. Assign exactly one primary keyword per URL, tag the rest  `11.10`
*useful · best practices · source 11*

Gotch's on-page methodology requires identifying a single core or primary topic per existing or planned page — his example: a URL already ranking for 'blue shoes,' 'best blue shoes,' 'blue and green shoes,' and more has 'blue shoes' as its one core topic, identifiable from the URL slug when structure is clean — then classifying every other ranking query on that page as either a 'keyword variant' (a close variant that stays on the same page, no dedicated page needed) or a 'secondary keyword' (a distinct, specific topic ranking weakly, e.g. position 67, because the existing page is too broad for it, which signals building a dedicated new page for that topic). The primary keyword then drives on-page optimization, placed in the URL, meta description, title tag, H1, and first sentence, and becomes the one topic tracked in the rank tracker for that page.

> "A secondary keyword is a topic that's ranking on this page"

**How to do it**

1. For each existing ranking page, export all queries it ranks for using the GSC Performance report filtered by page.
2. Identify the single core topic among those queries, using the URL slug as a shortcut if it's already descriptive (inferred: a slug like /blue-shoes/ signals the core topic is 'blue shoes').
3. Mark that core topic as the page's one Primary Keyword in the tracking sheet; this is the only keyword tracked for ongoing rank monitoring on this page.
4. For every other query the page ranks for, classify it as a Keyword Variant (a close variant staying on this page, no action needed) or a Secondary Keyword (a specific topic ranking poorly because this page is too broad for it).
5. For every query tagged Secondary Keyword, mark it as a clustering opportunity requiring a new dedicated page built around that topic.
6. On the existing page, place the Primary Keyword in the URL, meta description, title tag, H1, and first sentence, then use natural variants throughout the rest of the body copy.

**Tools:** Google Search Console

**Pitfall:** Trying to optimize one page for multiple unrelated core topics instead of splintering off a dedicated page for any query that's clearly too specific for the existing broad page to rank for.

### 14. Build navigation from what customers search for, not a products and services menu  `74.25`
*useful · best practices · source 74*

David Quaid observes that most sites coming out of design still ship a products menu and a services menu, and points out that Microsoft, Apple, Uber and Amazon do not. Those companies get straight into what they actually do. Every company has products and every company has services, so the labels carry no information for the visitor. He ties this to Google's opening line in the starter guide: Google does not care how you build and structure your site, is not looking for an about-us page, and is not looking for a contact page. Those are things companies do for themselves. What Google needs is to be able to find your files, which it does by finding links on other pages, and it does not need a site map drawn out for it. His conclusion is that navigation is a user and intent decision, so name the things you sell in the words customers use.

> "Google doesn't really care that much about your structure as long as it can find your files"

**Evidence:** David's examples: Microsoft, Apple, Uber and Amazon do not use products-and-services menus, while most design-led company sites do.

**How to do it**

1. List your current top-level navigation labels and mark any that are pure category words, such as products, services or solutions.
2. Replace each with the specific thing you sell, named as a customer would say it.
3. Check the label against real search demand so the navigation word matches a query people use.
4. Confirm every important page is reachable through a text link from another crawled page.
5. Judge each nav item on its measured clicks after 30 days and remove the ones nobody uses.
6. Do not add pages just because competitors have them; require a query or a conversion behind each one.

**Pitfall:** Copying a competitor's navigation structure. It imports their internal org chart into your site and buries the pages your customers actually search for.

**Apply at Pabau:** Pabau's navigation should name the jobs practices search for, such as booking, charting or payments, rather than grouping under generic software category words. David should check nav labels against real query data before the next site refresh.

**Apply anywhere:** Replace generic navigation labels like products and services with the specific things you sell, named in the words customers search with.

### 15. Convert top landing pages to static HTML before a CMS switch  `45.9`
*useful · concrete actions · source 45*

In a real migration David worked on (moving a company from a 1990s-era CMS to Drupal), the team identified their top 30-36 landing pages and converted just those to static plain HTML files before the migration, because the old CMS happened to publish pages with a literal .html extension, meaning these top pages could be removed from the CMS and served as pure static files without changing their URLs or content at all. The remaining 98% of pages (worth only about 20% of total traffic combined) migrated into the new CMS on schedule, while the static HTML versions of the top pages, including their internal link structure, were kept completely unchanged and watched until the new site stabilized; only then were those top pages themselves converted into the new CMS and the original URLs 301-redirected to their final destinations.

> "converted the top landing pages, somewhere around 30 to 36 of them,"

**How to do it**

1. Identify your top-traffic landing pages as a discrete list using an analytics traffic report (David's case: 30-36 pages).
2. Confirm whether your current CMS can output or export those specific pages as static HTML files without changing their URLs (inferred: check if URLs already end in .html or can be exported as static files).
3. Convert just that top-page list to static HTML files and remove them from the CMS being retired, keeping their URLs, content, and internal links completely identical.
4. Migrate the remaining bulk of pages into the new CMS/domain on your planned schedule.
5. Leave the static HTML top pages running unchanged and monitor their rankings/traffic through the migration and stabilization period.
6. Once the new site's rankings and indexing have stabilized, convert the static HTML top pages into the new CMS as well.
7. 301-redirect the original static-HTML URLs to their new CMS-hosted equivalents and monitor for a further stabilization period (inferred).

### 16. Define your ontology, then taxonomy, then navigation — in that order  `29.e2`
*useful · concrete actions · source 29 · universal-edition only*

Azarian describes catching himself as 'the cobbler's son': he preaches information architecture everywhere while his own site had none, having accumulated 35 distinct experimental routes and page types over a six-month content explosion that never connected back to the site proper. His remedy is an explicit ordered sequence. First build the ontology — what the entity is, what services it holds, and what those services relate to. Then derive the taxonomy — the specific words used, with a definition behind each one, and how they should be integrated into a user flow. Only then build the presentational layer: cards from the taxonomy, and site navigation from those. He names this kind of cross-functional work as what makes a successful SEO now, and mentions doing the rebuild as a WordPress-to-Astro/Svelte migration.

> "I preach information architecture everywhere I go, yet my site had zero information architecture."

**How to do it**

1. Inventory every page and route that exists, including experiments that were never linked into the site.
2. Write the ontology first: what this entity is, what services or offerings it holds, and how those relate to each other.
3. Derive the taxonomy from it — the actual vocabulary, with a written definition for each term.
4. Decide how each term should appear in a user flow before designing any component.
5. Build the card or module patterns from the taxonomy.
6. Build site navigation last, out of the taxonomy rather than out of habit.
7. Connect the orphaned experimental routes into the resulting structure, or retire them.

**Tools:** Spreadsheet (Sheets/Excel), Screaming Frog

**Pitfall:** Publishing a run of experimental pages that never get wired into the site's architecture — they accumulate as disconnected routes, which is exactly the disconnect he found on his own site.

### 17. Hybrid entity-attribute plus query-template coverage builds strongest authority  `03.1`
*useful · content insights · source 03*

There are two distinct methodologies for building topical authority, and combining them is described as the strongest approach. The first is entity-attribute coverage: processing every entity within a shared class through the same set of attributes (every entity in the food class shares the attribute calorie, just as every entity in the disease class shares the attribute symptom) signals comprehensive topic coverage to the search engine. The second is query-template coverage, which requires no topical relevance between variations at all: WikiHow holds authority for the entire how-to query format, letting it rank across completely unrelated topics simply because it consistently satisfies that query format. The hybrid methodology combines both, covering every entity in a class with all of its attributes across every query-template variation, uniting topical depth with query-format breadth in one content network.

> "allows it to rank across many unrelated topics at the same time"

**Evidence:** Two named real-world examples: calorie as a shared attribute across the food entity class (symptom across disease), and WikiHow's cross-topic ranking authority attached specifically to the how-to query format rather than any single topic.

**Apply:** When planning a Pabau topic cluster, ask both whether every relevant entity/feature is covered AND whether every query-format variation users apply to that topic (how-to, comparison, pricing, troubleshooting) is covered — building both dimensions together is the stronger structural approach to topical authority.

### 18. Put every page inside a category and only the homepage at root  `73.11`
*useful · best practices · source 73*

Asked whether pillar pages should be nested in a hub or sit off the root domain, Barnard gives a flat answer: his number one rule is everything in a category, and the only page that belongs at the root is the homepage. He rejects flat architecture outright. He separates two things people conflate: the URL structure of the site is ontological, meaning it is how you organize your information into categories, while the top menu is about what is important and how someone navigates. The two do not need to match, and he says the URLs you have do not map to the menu at the top. People do not navigate down through category after category; they jump straight to the part they want. The categories exist to place each page in a context of ontology and categorization, which is the machine-facing job.

> "my number one rule is everything in a category"

**Evidence:** Barnard says he has told clients for years that the top menu is not the same thing as the structure of the website, and that people react with 'oh yeah, of course' once he says it.

**How to do it**

1. Define the ontology first: the categories that describe how your information actually divides, independent of navigation.
2. Place every URL inside one of those categories, leaving only the homepage at the root.
3. Build the top menu separately, choosing what is important and what the main facets of the entity are, not mirroring the folder tree.
4. Let the menu link straight to deep pages rather than forcing users through category-index hops.
5. Audit the current top menu for items that are there and should not be, and facets that are missing and should be there.
6. Check which choices in the menu were driven by your own categorization rather than by importance, and correct those.
7. Keep category paths stable, since changing them later means redirects across the ontology.

**Pitfall:** Building the menu as a mirror of the URL tree. The menu then advertises your filing system instead of the entity's important facets, and users get made to click through category indexes to reach what they wanted.

**Apply at Pabau:** pabau.com should keep every page under a category path (/blog/, /templates/, /procedure-codes/, /diagnostic-codes/) and design the top navigation around the facets buyers care about, not around those same folders.

**Apply anywhere:** Keep only the homepage at the root and put every other page inside a category that reflects how the information genuinely divides. Design the top menu separately, around what is important, and link it straight to deep pages.

### 19. Warm up a new domain in GSC for two months first  `45.14`
*useful · concrete actions · source 45*

For a root-domain-only change, David recommends a deliberate warm-up phase starting about two months before the actual migration: get the new domain verified in Google Search Console and sitting there for at least a month before go-live, since GSC itself takes 24-36 hours just to start picking up a newly added property, and build some real links pointing to the new domain even before it has any live content, since backlinks to an empty domain are entirely valid and do still count. He explicitly endorses buying age/trust-signal verification for a new domain (citing a roughly $89 example) as part of this warm-up. Once warmed up, the migration should be executed via Google Search Console's dedicated Change of Address tool rather than a blanket whole-domain 301, because GSC's tool is specifically built to expedite transferring the accumulated backlink and traffic authority from the old domain to the new one.

> "try to warm up the new domain as much as possible"

**How to do it**

1. About two months before a planned domain-only migration, register and verify the new domain as a property in Google Search Console.
2. Leave the new domain sitting verified in Search Console for at least a month before migration to get past GSC's own 24-36 hour initial pickup delay.
3. During this warm-up window, build a small number of real backlinks pointing to the new domain even though it has no live content yet.
4. Optionally purchase domain-age/trust verification services for the new domain during this same window (David cites a roughly $89 example service).
5. When ready to migrate, use Google Search Console's domain Change of Address tool, which requires domain-level/admin access to both properties, rather than relying solely on a blanket domain-wide 301.
6. In parallel, directly email partners and other sites linking to you, asking them to update their links to point at the new domain rather than relying only on the old domain's 301 to carry the authority through.
7. After initiating the GSC migration tool, expect a period of ranking up-and-down movement and monitor it rather than expecting an instant, clean transition (inferred expectation-setting step).

**Tools:** Google Search Console (Change of Address tool)

**Pitfall:** Believing you can't or shouldn't build backlinks to a domain that has no content on it yet — David explicitly says people repeat this as a myth ('you can't buy backlinks to an empty domain') when it is in fact fine and part of a proper warm-up.

### 20. Bake the location into service-page URLs for local sites  `30.8`
*context · concrete actions · source 30*

For local businesses, Ellen recommends drilling location directly into the target URL rather than linking to a generic service page or homepage — e.g., localdentist.com/invisalign/brooklyn-new-york — because tying the location into the actual URL being linked to is important for local relevance to register; at the enterprise level the recommendation flips back to plain service pages without location folders. On the page itself, she also recommends speaking directly to conditions in that specific area (e.g., referencing flooding for a New Orleans plumber) rather than generic service copy.

> "tying the location into the actual target"

**How to do it**

1. For each priority local market, create a dedicated page combining the service and the location in the URL path (e.g., /service-name/city-state).
2. Point all sponsorship, directory, and partnership links for that market to this combined service+location page rather than the homepage or a generic service page.
3. On the page itself, add at least one paragraph referencing conditions specific to that area (local weather patterns, local regulations, local seasonal issues) rather than generic service description.
4. For enterprise or multi-location brands operating at a broader level, default back to plain service pages without per-location folders unless a specific local page is warranted.
5. Repeat this pattern for every additional local market being targeted rather than consolidating multiple cities onto one page.

**Pitfall:** Linking sponsorship or partnership placements to a generic service page or homepage instead of a location-specific URL forfeits some of the local-relevance signal that Ellen says AI and search engines pick up on.

### 21. State the keyword once in a URL; always add state  `30.9`
*context · concrete actions · source 30*

When structuring location-page URLs, Ellen recommends stating a qualifying term only once rather than repeating it across both the subfolder and the slug (e.g., prefer dentist.com/williamsburg/emergency-dentist over the redundant dentist.com/williamsburg/emergency-dentist-williamsburg). She also insists on including both city AND state, because a large number of U.S. towns and cities share the exact same name in different states, so state-level specificity is needed to disambiguate for both users and search engines, not just the city name alone.

> "there are a tremendous number of cities with the same name"

**How to do it**

1. Audit existing location-based URLs for a keyword or city name repeated in both the subfolder and the slug.
2. Consolidate so the location or service term appears only once per URL path.
3. Add the state (not just the city) to the page's title tag, H1, and body copy even if the URL itself only carries the city name.
4. Before finalizing a new location page's URL or copy, check whether other U.S. towns share the exact same city name to confirm disambiguation is needed. (inferred)
5. For highly competitive markets, build separate combined service+location URLs per priority service; for low-competition small towns, a single consolidated location page can be sufficient.

**Pitfall:** Repeating the same keyword twice in a URL path is redundant, and omitting the state can create real ambiguity given how many identically-named cities and towns exist across different U.S. states.
