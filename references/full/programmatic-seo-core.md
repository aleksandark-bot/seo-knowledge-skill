# Programmatic SEO — core

14 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. At scale, audit for damage other teams cause and fix fast  `23.8`
*core · best practices · source 23*

At the established-site stage, Edward warns the SEO's job becomes substantially about catching damage other teams cause at scale: content marketers, agencies, and other SEOs on a large team will put up meaningless or cannibalizing pages, make technical mistakes, run programmatic SEO plays, or publish large batches of AI-generated pages, and separately, configuration mistakes will accidentally block search engine bots or prevent important pages from being indexed. His prescribed response is constant monitoring for exactly this class of problem, with immediate removal or correction of the offending pages or subfolders the moment they're found, framing 'everything will go wrong' as the normal operating condition at this scale rather than an exception.

> "content marketers, agencies, SEOs, and other people who put up"

**How to do it**

1. Set up a recurring full-site crawl using a tool like Screaming Frog specifically to catch new pages added by other teams since the last crawl (inferred cadence: weekly or biweekly).
2. Check the crawl output for signs of programmatic SEO batches or bulk AI-generated pages that other departments may have published without SEO review.
3. Audit robots.txt and any page-level or plugin-level no-index settings for accidental blocks on important pages or subfolders introduced by other teams.
4. Cross-check newly discovered pages against your existing keyword/topic map to identify any that are cannibalizing established ranking pages.
5. When a problem is found, remove, no-index, or fix the offending pages or subfolders immediately rather than batching the cleanup for later.
6. Communicate the specific mistake back to the team that caused it to reduce recurrence, alongside the immediate technical fix (inferred).

**Tools:** Screaming Frog

**Pitfall:** Assuming a large, established site with dedicated teams is less exposed to basic mistakes — Edward states the opposite: 'everything will go wrong' at this scale precisely because more people can independently publish pages, change technical configs, and run programmatic content plays without central SEO review.

### 2. BrowserStack lost 70% of traffic after 2,000 AI articles in one day  `25.3`
*core · content insights · source 25*

Koray cites BrowserStack as an outlier proving that even massive authority signals don't protect against mass AI publishing: the domain has 23,000 referring domains (described as unique, valuable, non-spammy) and 300,000 branded search demand, both of which his own topical-authority framework normally treats as protective against spam-algorithm hits. Despite that profile, BrowserStack published over 2,000 AI-generated articles in a single day and subsequently lost roughly 70% of its organic traffic. Koray flags this as evidence that Google, since around December 2025, has become less tolerant of scaled/mass-produced content regardless of a site's prior authority or branded-query safety net. Publishing velocity itself (many pages in a very short window, especially AI-authored) can trigger a penalty-like traffic collapse even on an objectively strong domain.

> "published over 2,000 articles in a single day"

**Evidence:** BrowserStack: 23,000 referring domains, 300,000 branded search demand, published 2,000+ AI-generated articles in one day, then lost roughly 70% of organic traffic afterward (cited by Koray from his Manchester/Kajaas workshop talk).

**Apply at Pabau:** Avoid publishing large batches of AI-assisted articles in a single day or short window on pabau.com, even with Pabau's decent brand authority — pace programmatic or AI-assisted content launches over weeks, not days, to avoid resembling the scaled-content pattern Google is now penalizing.

**Apply anywhere:** Avoid publishing large batches of AI-assisted articles in a single day or short window on your main domain, even with your decent brand authority — pace programmatic or AI-assisted content launches over weeks, not days, to avoid resembling the scaled-content pattern Google is now penalizing.

### 3. Build a query-template matrix, then apply the Query-Deserves-a-Page test  `03.5`
*core · concrete actions · source 03*

The Query Deserves a Page (QDP) principle is a two-part test for whether a query variation earns its own page or should be folded into an existing one: open a new page only if that query's search demand exceeds a meaningful threshold, and the query involves a different entity or pattern with low semantic similarity to existing pages. Applied to a query template's individual variations, the same logic works at the predicate level: if a specific variation's predicates (the actions/words associated with it, such as download versus share) differ meaningfully from the template's other variations, that signals a new page is warranted; if predicates are highly similar but the core entity differs, it should still be a separate page. This keeps a content network's page count driven by genuine semantic or demand differences rather than giving every keyword variation its own page, or cramming too many distinct entities onto one page.

> "we open a new page only if the query's search demand exceeds"

**How to do it**

1. List every query-template variation targeted for a topic, broken into component slots (e.g., for a QR code generator: [contextual noun such as PDF or Facebook] + QR Code + [tool synonym such as Generator or Maker]). (inferred structure)
2. For each variation, pull search demand via Google Keyword Planner, Ahrefs, or DataForSEO Keyword Data and note whether it clears a meaningful volume threshold for the niche. (inferred tool)
3. For each variation, identify its typical predicates: the verbs/actions users associate with it (e.g., download clusters with PDF-related queries; share or follow clusters with Facebook-related queries).
4. Compare the predicate set of a new variation against the predicate sets of existing pages' target queries.
5. If predicates differ meaningfully from existing pages and demand clears the threshold, create a new dedicated page for that variation.
6. If predicates are nearly identical to an existing page's query but the core entity differs, still create a separate page rather than merging.
7. If neither condition is met, fold that query variation into the existing page instead of creating a new one.
8. Periodically re-run this test as search demand shifts, since a variation that didn't clear the threshold before may later justify its own page. (inferred)

**Tools:** Google Keyword Planner, Ahrefs, DataForSEO

**Pitfall:** Opening a new page for every keyword/query variation regardless of demand or semantic distinctiveness, which raises the site's cost of retrieval and dilutes ranking signal per page instead of concentrating it.

### 4. Build keyword-driven taxonomy tag pages for e-commerce  `47.3`
*core · concrete actions · source 47*

A developer-turned-SEO's reported result: building out taxonomy and tag pages on large e-commerce sites, meaning dedicated landing pages for specific tag combinations people actually search for, produces a consistent 20-30% traffic uptick across the projects they've worked on. The method is to identify actual search terms for tag combinations, both brand-plus-product-type tags such as 'Levi's jeans' or 'Levi's jumper' for a store carrying Levi's, and non-brand descriptive tags such as 'white dresses,' 'dresses,' or 'sale,' then generate a dedicated landing page per tag or combination. The commenter flags the main risk explicitly: this is hard to get right and not be spammy, meaning thin, auto-generated, near-duplicate tag pages can look like spam to Google even while driving real traffic when done well.

> "Finding tags for what people search for and creating landing pages"

**How to do it**

1. Pull your e-commerce site's actual product catalog and identify the brands, product types, attributes such as color and size, and occasions customers search for.
2. Run keyword research, using a tool such as Google Keyword Planner, Ahrefs, or Semrush, to confirm real search volume exists for specific tag combinations before building a page for them (inferred).
3. Build both brand-plus-product-type tag pages, such as '[Brand] [Product Type]', and non-brand descriptive tag pages, such as 'white dresses' or 'sale', as their own indexable landing pages.
4. Ensure each tag page has a genuinely distinct, non-duplicate set of products and at least some unique on-page content, such as intro copy or filtering options, rather than being an empty template with just a product grid.
5. Set up an internal linking structure connecting related tag pages to each other and to relevant category or product pages so search engines can discover and understand the full taxonomy.
6. Monitor organic traffic before and after launching a batch of new taxonomy pages to confirm the reported 20-30% uplift pattern holds for your own site (inferred).
7. Prune or noindex any tag pages that end up thin, near-duplicate, or non-performing after a few months, rather than leaving low-quality taxonomy pages live indefinitely (inferred).

**Pitfall:** This tactic is explicitly described as hard to get right and not be spammy - generating large volumes of thin, near-duplicate taxonomy or tag pages purely to capture search volume risks a spam-pattern penalty, so each tag page needs genuine product-set distinctness and real search demand behind it, not just programmatic generation for its own sake.

### 5. Don't scale templated pages from public or competitor data  `66.30`
*core · concrete actions · source 66*

Content that creates many templated pages from facts anyone can access, without unique first-party data, expert judgement or a genuinely different task on each URL. The framework's verdict is that scale multiplies duplication, maintenance and quality risks and does not create real value. It covers location, definition, specification, pricing or entity pages generated from third-party or public datasets without first-party data, expert judgement or a distinct user task. It scores Low on all five value dimensions at High effort — the only type in the worksheet with that combination, and therefore the worst investment the framework identifies. Its mirror image is the prioritized scalable type, and the three missing ingredients are exactly what separates them: first-party data, expert judgement, or a distinct user task on each URL. Any one of the three, applied genuinely across the whole set rather than the first few pages, is the difference between the best-scoring scalable type and the worst-scoring one at identical build cost.

> "creates many templated pages from facts anyone can access"

**How to do it**

1. Inventory every templated page set on the site with its page count, its data source, and its clicks and conversions per page.
2. For each set, ask the three questions: is there first-party data per page, is there expert judgement per page, and does each URL serve a genuinely different user task?
3. Sample the tail rather than the top of the set, since differentiation usually holds for the first pages and collapses across the rest.
4. For sets that fail on all three, stop expanding immediately — High effort with Low value compounds with every page added.
5. Decide the fix by whether a differentiator is reachable: if you can attach first-party data or genuine expert judgement across the whole set, do that; if you cannot, consolidate the set into a smaller number of genuinely useful pages.
6. When consolidating, keep the pages with real demand, merge the rest into hubs or category pages, and redirect.
7. Where a competitor's or third party's data is the only differentiator, treat the set as unfixable in place, since public facts cannot produce proprietary advantage.
8. Check the crawl and index footprint the set consumed, and confirm the consolidation frees it toward pages that convert.
9. Add the three-question gate to the intake process for any future page set, before the template is built.

**Tools:** Screaming Frog, Google Search Console, Ahrefs

**Pitfall:** Judging the set from its best pages. The top of a programmatic set usually has real data and a real task; the tail is templated public facts, and the tail is most of the set — which is what gets assessed.

**Apply at Pabau:** Any Pabau page set built from public treatment facts, third-party specs or competitor pricing is this type — High effort, Low value on every dimension. Either attach Pabau's own data and judgement across the whole set, or consolidate it into a smaller number of genuinely useful hubs.

**Apply anywhere:** Any page set built from public facts, third-party specs or competitor pricing is this type — High effort, Low value on every dimension. Either attach your own data and judgement across the whole set, or consolidate it into a smaller number of genuinely useful hubs.

### 6. Exact-match domains, one per service-and-city, still work  `58.9`
*core · concrete actions · source 58*

Both hosts report exact-match domains working unusually well right now, at two different scales. Jesper's rank-and-rent model in Denmark: buy the exact-match domain for servicename-city as one word with no hyphen, then build out the entire site with pages for every small city name or district within that city, each a variation of one article. He dominates page one for all the variations, and says it doesn't matter that the terms show zero or ten monthly searches because his contact form proves people are searching them - he forwards the leads to agencies he works with. He has been doing this for six or seven years. Cody's SaaS version: a friend's API product buys exact-match domains for every long-tail use case, builds a single-page lander per domain with no functionality, throws about ten DA50 links at each, and gets to page one. One example: a keyword at roughly 2,500 monthly searches, exact-match .com, ten links, position three within 45 days, with direct referral attribution for signups and revenue. Cody's own version of it: tool-type domains like x-scraper.com with 10-15 links reaching page one within 60 days. They're vibe-coded with Claude Code and deployed to Vercel by a script.

> "exact match domains are working extremely well"

**How to do it**

1. Identify the long-tail commercial term - service plus city for local, or use case plus modifier for software.
2. Buy the exact-match .com as one word with no hyphen.
3. Build a single focused page (or a small site of variations, for local) rather than a full content site.
4. Get the homepage ranking for its own name first - a small number of authoritative links is what both describe.
5. For local, expand into every district and neighbourhood name as variations of the one article.
6. Set up crawling and indexing properly and keep the pages fast - Cody's are static and deployed at the edge.
7. Link back to the core site so the traffic has somewhere commercial to go, and track referral attribution.
8. Judge success on enquiries and referral revenue, not on the keyword tool's volume estimate.

**Tools:** Claude Code, Vercel

**Pitfall:** The link acquisition both describe (buying DA50 links) is what makes these rank quickly, and it's a paid-link scheme. Without it, an exact-match single-page site is just a thin site.

**Apply:** Worth knowing rather than copying: if a Pabau competitor appears from nowhere at position three for a specific long-tail term on an exact-match domain, this is the playbook - a single page and a handful of bought links, not a content programme.

### 7. Feed a 'keyword universe' from five automatic sources  `50.1`
*core · ai workflows · source 50*

Instead of doing keyword research as a one-off project, the system continuously populates a single "keyword universe" database from five automatic sources: Ahrefs and DataForSEO for volume and competitive data, Google Search Console performance data, scraped forum content to surface pain-point language, scraped and analyzed product/service page data from the client's own site, and an AI-seed source that scans the business's own site content, turned into a vector database, to guess additional relevant topics. Everything that comes in is automatically clustered into topic groups, then each cluster gets mapped either to an existing page, turned into a brief for a brand-new page, or discarded if it scores as insufficiently relevant to the business. This replaces periodic keyword-research sprints with an always-on pipeline that keeps expanding and pruning itself as new SERP, forum, and product data arrives.

> "keywords flowing in via five different sources automatically"

**How to do it**

1. Stand up a central keyword database, a "universe," that every keyword source writes into, rather than keeping keyword lists in separate spreadsheets per project.
2. Connect an API-based keyword/rank data source such as Ahrefs and/or DataForSEO to pull volume and competitive metrics automatically on a schedule.
3. Connect Google Search Console's API to pull query and page performance data into the same database.
4. Build or commission a scraper for relevant industry forums/communities to extract pain-point language and candidate topics (inferred: needs a scheduled scraping job and a target forum list).
5. Scrape and structure your own site's product/service pages as a distinct data source so commercial-page topics feed the universe too.
6. Convert your own site's page content into embeddings, a vector database, so an AI-seed process can guess additional relevant topics directly from what you already publish.
7. Set every incoming keyword/topic to run through automatic clustering into topic groups as soon as it's ingested.
8. Build a mapping step that assigns each cluster to an existing page, flags it as a candidate for a new page, or discards it if irrelevant.
9. Schedule the whole pipeline to run continuously, such as on a cron job, rather than as a one-time research pass, so the universe keeps growing and pruning itself (inferred scheduling mechanism).

**Tools:** Ahrefs, DataForSEO, Google Search Console, a web scraper, a vector database

### 8. Localize programmatic content per market to avoid scaled-content penalties  `28.12`
*core · best practices · source 28*

Scaling content across 12 country and language domains risked being flagged as scaled content abuse, content that looks machine-generated, doesn't satisfy intent, or reads as untrustworthy AI content that makes people bounce. The team's defense was making each domain's content genuinely, not superficially, different: the same underlying problem produces different search queries, different SERP landscapes, and different needed content depending on the market — France skews B2B, the US is almost exclusively B2C, other countries skew toward school use cases, and even a proven query like 'Does Duolingo have ASL?' doesn't translate to the UK, with no meaningful search volume there, even though the same query works in France. The rule is to run a fresh SERP and intent analysis per country rather than translating one master content set, since genuinely different content per market is what keeps scaled multi-market production from reading as thin or duplicated.

> "Good content in India really does look qualitatively different"

**How to do it**

1. For each target country or language market, run an independent SERP and search-intent analysis for your core topics rather than assuming the same queries apply (inferred: use a SERP data tool or manual search per locale).
2. Identify the market-specific angle for each topic, such as B2B versus B2C emphasis or school versus individual-consumer framing, before drafting content, not after.
3. Explicitly test whether a query that performs well in one market actually has search volume or demand in another before porting it over, since a query can work in one country and have zero relevance in another despite a shared language.
4. Brief content creation, human or AI-assisted, with the market-specific SERP findings and cultural context, rather than issuing a direct translation of a source-market article.
5. Review a sample of published multi-market content periodically for signs of superficial genericness, such as identical structure copy-pasted with only nouns swapped, that would risk a scaled-content-abuse flag.

**Tools:** DataForSEO

**Pitfall:** Treating multi-market expansion as a translation problem — content that is directly translated rather than independently re-researched per market is exactly the pattern others in the SEO community have reported getting penalized as scaled content abuse.

### 9. Prioritize internal links to the highest-demand programmatic entries  `03.8`
*core · concrete actions · source 03*

In a pure programmatic SEO vertical (the example: word-unscrambling tools, competing against 1.82 million results for a single query, where every competitor site shows essentially the same underlying information), the topical map's core section is split by demand tier rather than commercial-vs-informational: most-common-and-popular words versus less-popular words. The 1,000 most important, evergreen-demand words are deliberately given the majority of internal links and are linked directly from the homepage, so they receive more crawl priority and link equity than competitors give their equivalent pages, out-competing on distribution even when the underlying information is identical to everyone else's. Differentiation then comes down to two remaining levers: superior visual and textual microsemantics on each page, and lowering cost of retrieval further by removing unnecessary pages and fixing technical SEO issues that dilute ranking signal.

> "receive the majority of the internal links, are linked directly"

**How to do it**

1. In a large programmatic content set, pull search demand data for every entry the template covers (every word, city, or product variant).
2. Rank all entries by search demand and segment them into a small top tier (the source's example: the top 1,000) versus the long tail.
3. Link directly from the homepage to the top-tier entries, or to a hub page that itself links to them prominently, rather than burying them at the same depth as the long tail.
4. Give the top-tier entries the majority share of internal links sitewide, deliberately imbalancing the internal link graph in their favor instead of distributing links evenly.
5. For every page, audit whether the actual textual/visual content is meaningfully different from competitors' equivalent pages, since this is often the only remaining differentiator in commoditized programmatic niches.
6. Remove low-demand or redundant pages using the Query-Deserves-a-Page test, and fix technical SEO issues that dilute ranking signal, to keep overall cost of retrieval low relative to competitors. (inferred: use a crawler or log-file analysis to find and prune such pages)

**Tools:** Google Search Console, Screaming Frog

**Pitfall:** Distributing internal links evenly across every programmatic page regardless of demand, instead of deliberately concentrating link equity and homepage-level links on the highest-demand subset.

### 10. Product-led SEO: the template library is the keyword strategy  `62.1`
*core · content insights · source 62*

The organising idea in Cody's Canva research is that the product itself is the SEO strategy rather than something the SEO team writes about. Canva's template library is structured like a well-organised e-commerce store, with categories and subcategories for every conceivable need, so each template functions as its own mini landing page for its own keyword. The granularity is the point: they target the broad term (invitation templates) and the incredibly niche ones (Christmas invitation templates, baby shower invitations, save the dates) from the same structure. Their 'create' pages work the same way - landing pages for resumés, posters, social posts - built on the insight that when someone needs something visual they Google 'how to make a X', so Canva anticipates the search and provides the working tool before signup, which is both the answer and the conversion mechanism. Cody's framing in the intro is that this is almost a defining factor of the product: hundreds of thousands of landing pages on long-tail keywords, creating enormous surface area for discovery, with the product team having to think about it constantly.

> "It's their use of product-led SEO"

**How to do it**

1. List the units of value your product already contains - templates, tools, calculators, presets, integrations.
2. Give each unit its own URL rather than hiding them behind an app interface or a search box.
3. Organise them into a category and subcategory hierarchy that maps to how people search, not to your internal taxonomy.
4. Cover both the broad category term and the long-tail variants from the same structure.
5. Let the visitor use the thing before signing up, so the page satisfies the search and demonstrates the product at once.
6. Treat new units of product value as new SEO assets, which means product and SEO planning happen together.

**Pitfall:** This only works where the product genuinely contains many discrete units of value - applied to a product with one workflow, generating pages per keyword produces thin pages rather than product-led ones.

**Apply at Pabau:** Pabau's template library is the direct analogue: every consent form, policy template and clinic document should be its own indexable page in a searchable hierarchy, usable before signup - that's the structure Canva's growth is built on.

**Apply anywhere:** If your product contains a library of discrete assets - templates, forms, presets, calculators - each one should be its own indexable page in a searchable hierarchy, usable before signup. That's the structure Canva's growth is built on.

### 11. Real per-page data is what separates programmatic SEO from abuse  `16.13`
*core · general insights · source 16*

The speakers draw a clear line between legitimate programmatic SEO and "scaled content abuse" using a referenced example (Dave Faro's site) that runs millions of job listings, where a bot automatically pulls real job-spec data, generates the pages, and categorizes them — explicitly compared to AWS and Indeed as the same category of legitimate programmatic SEO. This is contrasted against the abuse pattern of instructing a bot to "write 5,000 articles on skateboards, or car lights" with no distinct underlying data per page — content invented to fill a quota of pages rather than generated from real, unique per-page source data. The determining test isn't automation itself (both patterns are heavily automated) but whether each individual page is backed by genuine unique data.

> "it's got millions and millions of job listings"

**Evidence:** Dave Faro's programmatic job-listing site, cited as having "millions and millions of job listings," each auto-generated by a bot from real job-spec data and auto-categorized, versus the named abuse example of prompting a bot to write "5,000 articles on skateboards, or car lights" with no real per-page data source.

**Apply at Pabau:** When Pabau considers programmatic pages (e.g., specialty, location, or integration-comparison pages), apply this same test before building: each page must be generated from genuinely distinct underlying data rather than being AI-invented filler text assembled to hit a page-count target, since the former is the defensible pattern and the latter is what the speakers expect Google's upcoming enforcement to target.

**Apply anywhere:** When you consider programmatic pages (e.g., specialty, location, or integration-comparison pages), apply this same test before building: each page must be generated from genuinely distinct underlying data rather than being AI-invented filler text assembled to hit a page-count target, since the former is the defensible pattern and the latter is what the speakers expect Google's upcoming enforcement to target.

### 12. Scale pages only where each one shows different owned data and serves a different task  `66.22`
*core · concrete actions · source 66*

The framework's one licence to publish at scale, and it carries two conditions. Content that provides a useful page for each real entity, product, location or integration, because every page shows uniquely different owned data and serves a different task. Its role is scalable coverage of genuine, useful, relevant insights for the brand's audience — not publishing keyword variants or templating public facts. It covers entity, product, location and integration pages featuring unique and useful metrics, availability, change history, comparisons and context from owned data, with editorial quality assurance. It scores High on citation potential, business value and proprietary advantage at High effort, with Medium click resilience. Compare it to the deprioritized programmatic type — templated pages from public or competitor data — and the difference is exactly the two conditions: owned data that differs per page, and a distinct user task per URL. Fail either and the same build becomes the deprioritized pattern, with the High effort intact and every value score dropping to Low.

> "because every page shows uniquelly different owned data and serves"

**How to do it**

1. List the entities you could publish a page for — products, models, locations, integrations — and keep only those that are real things a user looks up by name.
2. For each entity, name the owned data that differs page to page: your metrics, your availability, your change history, your measurements, your operating context.
3. Test both conditions before building: if two pages would show the same data, or serve the same user task, they fail and must be one page.
4. Test the second condition against the deprioritized type too: if the differing data is public — a competitor's price, a third party's spec — it is not owned data and the build is the deprioritized pattern.
5. Design one template whose distinctive content comes from the data rather than from spun prose, and let pages with thin data render as short pages instead of padded ones.
6. Wire the data to its live source, and include a change history where you have one, since that is both useful and citable.
7. Add editorial quality assurance as a gate, not a review: a threshold of data richness below which the page is not published at all.
8. Give each page an internal linking role — from the hub, from siblings, from the relevant documentation — rather than leaving the set orphaned.
9. Monitor the set per page for impressions and engagement, and prune the tail that never earns either.
10. Cap the set at what your data and your QA can actually support, since High effort here is mostly maintenance and QA cost.

**Tools:** Screaming Frog, Google Search Console, Schema.org

**Pitfall:** Launching the full set before checking the data density per page. The two conditions hold at the top of the set and fail in the tail, and a set that is 20% genuinely differentiated pages and 80% templated public facts gets judged as the deprioritized type — including by the quality systems that assess the site as a whole.

**Apply at Pabau:** This is the test for any Pabau page set built at scale — integration pages, location pages, treatment pages. Each must show data Pabau owns that genuinely differs page to page and serve a different task, with a data-density gate before publication. A set templated from public treatment facts is the deprioritized pattern at the same build cost.

**Apply anywhere:** This is the test for any page set built at scale — integration pages, location pages, product pages. Each must show data you own that genuinely differs page to page and serve a different task, with a data-density gate before publication. A set templated from public facts is the deprioritized pattern at the same build cost.

### 13. Turn product features/templates into dedicated high-intent landing pages  `37.1`
*core · concrete actions · source 37*

Jotform's single biggest SEO lever, per the video, is converting product features and templates into standalone landing pages built for high-intent searches like 'contract template,' 'job application form,' or 'AI quiz generator' - each page is a lightweight product in itself. Its paystub template page (jotform.com/pdf-templates/pay-stub-template) gets nearly 11,000 clicks a month from just 66 backlinks across 17 referring domains: the template sits above the fold with no scrolling required, the title and H1 both read 'Free paystub PDF template,' and body copy is deliberately minimal because visitors want the deliverable, not an article about it. These pages become linkable assets in their own right, earning backlinks that Jotform then funnels via internal links to strengthen other pages, and the same pattern repeats across subfolders like /form-templates/, /surveys/, and a fast-growing /ai/ subfolder (e.g., jotform.com/ai/quiz-generator gets 11,000 clicks/month ranking for 263 keywords).

> "This page has nearly 11,000 clicks per month"

**How to do it**

1. Identify a specific feature, template, or micro-tool your product already offers that maps directly to a high-intent search query.
2. Give that single feature/template its own dedicated URL in a clearly-labeled subfolder rather than burying it inside a general product page.
3. Put the actual deliverable (the template, tool, or generator itself) directly above the fold so the visitor gets it without scrolling.
4. Match the page title and H1 to the exact phrase searchers use.
5. Keep body copy minimal - strip explanatory text down to what's strictly necessary, since visitors searching this query type want the deliverable, not an article.
6. Build many of these single-purpose pages across your product's feature set rather than one generic hub page, so each can independently earn backlinks and rank for its own query.
7. Internally link from these high-traffic, link-earning template/feature pages to other relevant pages on your site so the authority they accumulate helps those pages too.
8. Prioritize this pattern over writing blog posts for the same high-intent, product-shaped queries.

**Pitfall:** Newer SEOs often try to target inherently product-shaped, high-intent queries (like 'pay stub template' or 'contract template') with blog posts - that's not what searchers want for these terms; they want the actual deliverable, so a lightweight, functional template/tool page will outperform an article every time for this query type.

### 14. Use Promptfoo to find what LLMs get wrong  `29.2`
*core · ai workflows · source 29*

Hank's critique of most programmatic SEO (e.g., city pages built from Wikipedia-level facts) is that it is 'lowest common denominator' content that adds nothing an LLM doesn't already know, so it can't differentiate from the thousands of similar pages competitors have already generated the same way. His fix, which he calls 'LLM correct,' is to build a testing harness with Promptfoo that queries LLMs on the same topic as a page and diffs the model's baseline answer against the page's current content to find where the AI is wrong, hedging, or simply thin. Those gaps get filled with specific, hard-to-find, human-nuanced information a model can't fabricate, and the corrected template is then applied at full programmatic scale so the whole page cluster - not just one hero page - becomes distinct from competitors' commodity versions. He frames this as operating in a 'correction economy': the value in programmatic content now comes from correcting or completing what AI already assumes, not from restating it.

> "how do we build a harness through something like Promptfoo"

**How to do it**

1. Identify a set of programmatic pages (e.g., city pages, comparison pages, template pages) at risk of being commodity content.
2. Set up a Promptfoo test harness that can send the same topic/entity query to one or more LLMs.
3. Prompt the LLM to output everything it 'knows' about that topic in roughly the same structure as your page. (inferred)
4. Diff the LLM's baseline answer against your current page content section by section.
5. Flag every point where the LLM is wrong, hedging/unsure, generic, or thin - this is the 'correction economy' signal.
6. Research and write specific, hard-to-find, human-nuanced content that corrects or fills each flagged gap.
7. Rewrite the page so the corrective information is foregrounded rather than restating what the LLM already knows.
8. Apply the corrected template across the entire page cluster, not just a single hero page, so the whole set differentiates from competitors' programmatic pages.
9. Publish the corrected pages live and compare their performance against the un-corrected version of the template. (inferred)

**Tools:** Promptfoo

**Pitfall:** Programmatic pages built only from the lowest common denominator of publicly available facts (e.g., scraped Wikipedia-level info) add no non-commodity value, so they can't differentiate from the many other programmatically generated pages already saying the same thing.
