# Technical SEO — supporting (part 2 of 2)

19 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Parasite pages don't index themselves - drip-ping plus social links  `58.5`
*useful · concrete actions · source 58*

Jesper is direct that these pages typically won't index automatically, and describes a two-part routine. First, indexing services: he names IndexBin, Nowspeedlinks, Rapid URL Indexer and Synite, and if it's something he really wants indexed he submits the same link to five indexing services at once. Cody's equivalent is SpeedyIndex, which he notes is a Telegram-based service. Second, external links: he keeps a batch of X profiles and posts the link across five of them, so the page has real inbound links pointing at it. His honest caveat is that sometimes a page simply won't index no matter what you do - but if it can index, indexing services plus social links will get it there. Facebook posts and YouTube videos work as the link source too.

> "won't typically won't index automatically"

**How to do it**

1. Publish the page and wait to see whether it indexes on its own - Jesper's baseline is that these typically won't, but confirming saves the spend.
2. Submit the URL to several indexing services simultaneously. He names IndexBin, Nowspeedlinks, Rapid URL Indexer and Synite, and submits to five at once for anything he really wants indexed; Cody's equivalent is SpeedyIndex, a Telegram-based service.
3. Understand what you are buying: per source 59, these services maintain sites that trap Google's crawler in an internal loop, then add an outbound link to your submitted URL so the crawler is forced to follow it.
4. In parallel, post the URL from a batch of X profiles - he uses five - so the page has genuine inbound links rather than only a submission.
5. Extend the same treatment across the other properties you control: Facebook posts and YouTube videos both work as link sources in his testing.
6. Daisy-chain them, per his X Articles routine: publish a long-form X Article on the topic and link out from it to each of the parasite assets, which he reports raises the indexing rate and looks natural because a profile plausibly would link there.
7. Re-check indexation after a few days with a site: query or an exact-phrase search.
8. Accept the failure case - he says plainly that some pages simply won't index no matter what you do, and that if it can index, services plus social links will get it there.

**Tools:** SpeedyIndex, Rapid URL Indexer

**Pitfall:** Paid indexing services manipulate Google's crawl scheduling and sit outside its guidelines. The honest read from both practitioners is that they only accelerate what would eventually index anyway - they cannot force an unindexable page in, so persistent failure is information about the page, not about the service.

**Apply at Pabau:** The legitimate version for Pabau is the boring one: submit new URLs through Search Console, make sure they're linked from a crawlable page on the site, and treat a page that won't index as a signal about the page rather than a submission problem.

**Apply anywhere:** The legitimate version is the boring one: submit new URLs through Search Console, make sure they're linked from a crawlable page on the site, and treat a page that won't index as a signal about the page rather than a submission problem.

### 2. Pop-under traffic and the Chrome clickstream question  `57.22`
*useful · content insights · source 57*

A short but consequential exchange. Cody raises an Ahrefs video from two days earlier arguing that Chrome is feeding clickstream data into ranking factors, and connects it to the Reddit-to-Google relationship: his hypothesis is that Google leans on user-generated content and clickstream signals rather than building a chat product, because that data tells it what content is genuinely valuable. Jackie's response is that he considers it confirmed - Google definitely uses Chrome data, and it appeared in an algorithm leak within the previous couple of months. He then says he is running tests with pop-under traffic and that it's working well, which is the operational implication: if clickstream is a ranking input, cheap purchased traffic to a URL is an attempt to forge that input. This is the same mechanism Jackie later productises as Browser Blast, described as mimicking virality on the basis that driving a lot of traffic to a single URL alongside other positive signals moves rankings two or three pages at a time.

> "pop-under traffic"

**How to do it**

1. Treat clickstream as a plausible ranking input rather than a settled one - the evidence cited here is an algorithm leak and a practitioner video, not documentation.
2. If you are diagnosing an inexplicable competitor gain, purchased traffic is now on the list of explanations alongside links and content.
3. Look for the signature: a sharp traffic increase to a single URL with no corresponding referral source, engagement, or conversion, and no social or link activity to explain it.
4. Recognise that the legitimate version of the same mechanism is simply real traffic - which is why every practitioner in this collection ends up recommending owned channels that drive people to search and click.
5. Do not buy pop-under or bot traffic: it is served through adware and malware-adjacent networks, it pollutes your own analytics irrecoverably, and Google's spam policies treat it as ranking manipulation.

**Pitfall:** Pop-under inventory is largely delivered by adware and hijacked browsers, so buying it funds that ecosystem and puts unattributable junk traffic permanently into your analytics history. Jackie's own framing is that it's a test he's running, not an established tactic.

**Apply at Pabau:** For Pabau this is a diagnostic note: if a competitor's rankings move without any change in links or content, purchased traffic is a live explanation - and the legitimate route to the same signal is the owned-channel branded-search play in this collection.

**Apply anywhere:** A diagnostic note: if a competitor's rankings move without any change in links or content, purchased traffic is a live explanation - and the legitimate route to the same signal is the owned-channel branded-search play in this collection.

### 3. Reject the one-size-fits-all 50-page technical audit as manufactured value  `179.4`
*useful · concrete actions · source 179*

Grow and Convert single out the boilerplate technical audit as a specific agency pattern to watch for. Some agencies run every new client through the same checklist regardless of the site's actual situation and deliver a 50-page audit full of recommendations, many of which have minimal impact on rankings or are already implemented on the site. They describe this as creating the appearance of value without delivering much of it. The test they propose is not whether an agency audits, but whether it can triage: a good agency explains which technical issues actually matter for your specific site and which are low priority. They add the underlying reason the audit should not dominate a retainer, which is that most technical fixes are one-time tasks.

> "the one-size-fits-all technical audit"

**Evidence:** Grow and Convert describe 50-page audits filled with recommendations that have minimal ranking impact or are already addressed on the client's site.

**How to do it**

1. Ask the agency to send a redacted technical audit they delivered to another client before you sign.
2. Compare its structure against a generic crawler export; if the section order matches a Screaming Frog or Semrush report tab for tab, it is a checklist.
3. Ask them to rank the findings for your site into must-fix, worth-fixing, and ignore, with a reason for each ignore.
4. Check how many findings are already resolved on your site; a high count means they did not look before writing.
5. Ask which findings are one-time and which need ongoing work, and require the recurring list to be short.
6. Agree that technical fixes are completed before content publishing starts, not spread across the retainer.
7. Move the hours freed by a short technical list into keyword research and page production in the same contract.

**Tools:** Screaming Frog, Semrush

**Prompt / template:**

```text
Which of these technical issues actually matter for our specific site, which are low priority, and why?
```

**Pitfall:** Paying by audit length. Page count correlates with crawler defaults, not with impact, and a long audit gives the agency months of billable remediation on issues that were never costing rankings.

**Apply at Pabau:** If Pabau buys a technical audit for pabau.com, require the deliverable to be a ranked list with an explicit ignore column and a fixed completion date, so the work does not become a permanent retainer line item.

**Apply anywhere:** Treat a long, generic technical audit as a warning rather than a deliverable. Ask the agency to triage findings for your specific site into must-fix, worth-fixing and ignore, with reasons, and check how many items are already handled. Most technical fixes are one-time, so agree a completion date and move the remaining hours into keyword and content work.

### 4. Route traffic to top pages first and audit footer link text  `45.6`
*useful · best practices · source 45*

David stresses that during a migration, the order pages get crawled and re-indexed matters, not just whether they eventually get crawled, because pages with similar content can start cannibalizing each other, and this only becomes visible once re-indexing happens in the wrong order. He gives a first-hand example: switching from www to non-www caused his own number-one page (a glossary page) to stop getting indexed because other, lower-priority pages with similar paragraph content got processed first. His mitigation is to deliberately route more visible traffic (e.g., via a big email campaign) to the most important pages first so crawl signals prioritize them, and separately, to run a full site health check about a month out (he names Bing's free health check and Screaming Frog) to fix broken links and tighten footer link text so similar wording isn't pointing at two different pages.

> "You want your most important pages crawled first."

**How to do it**

1. About one month before migration, run a full technical health check using a tool such as Screaming Frog or Bing's free site health check.
2. Fix every broken link and broken page identified by the health check before migration.
3. Audit your site footer specifically for repeated or overly similar anchor text pointing to two different pages, and tighten/differentiate that wording.
4. Identify your single most important page(s) that must not lose its index position.
5. Prepare a large email campaign or other high-visibility push timed to drive a spike of visits to those top-priority pages first during the migration window.
6. Launch that traffic push around migration go-live so visits help signal those pages for priority crawling ahead of lower-priority pages.
7. After migration, check whether your top priority page(s) retained their index status and rankings, and investigate immediately if a top page drops out (inferred verification step).

**Tools:** Screaming Frog, Bing Webmaster Tools (free health check)

**Pitfall:** Assuming that if a page eventually gets crawled, order doesn't matter — David's own glossary page (his number-one page) stopped getting indexed purely because other pages with similar paragraph content were processed first during a www-to-non-www switch.

### 5. Schema is only mandatory for structured verticals  `18.8`
*useful · content insights · source 18*

Schema.org markup is described as genuinely mandatory only for specific structured verticals: job listing sites cannot appear in Google Jobs without schema because Google reads the structured data directly rather than text-scraping at that volume (the example given: an unstructured string like '4pm at EWR flying to Stansted, lands 6:15pm' is ambiguous without markup to show where the departure/arrival fields start and stop) — the same logic applies to Google Merchant, flights, and hotels. Outside those verticals, schema is characterized as 'a catalyst or requirement,' not a direct ranking factor: in a test of 10 sites where 9 had job schema and 1 didn't, the schema-less site failing to rank for job listings is 'technically an SEO failure,' but among the 9 that did have it, schema wasn't differentiating rankings between them. The wider claim made elsewhere in the discussion is that roughly 99% of typical content/informational sites don't need schema at all, and FAQ-schema rich results in particular no longer deliver the ranking/CTR boost they once did.

> "you absolutely 1,000% need schema"

**Evidence:** Job listing sites cannot appear in Google Jobs without schema (Google reads structured data rather than scraping ambiguous text like flight times); in a 10-site test, only the one site missing job schema failed to rank for job listings, while schema made no differentiating difference among the 9 that had it.

**Apply at Pabau:** Audit which of Pabau's content types actually sit in a schema-mandatory vertical (e.g. any careers/jobs pages, product/pricing comparison pages) and limit schema effort to those, rather than treating schema markup as a general ranking lever across ordinary blog/informational content.

**Apply anywhere:** Audit which of your content types actually sit in a schema-mandatory vertical (e.g. any careers/jobs pages, product/pricing comparison pages) and limit schema effort to those, rather than treating schema markup as a general ranking lever across ordinary blog/informational content.

### 6. Schema ties up loose ends, doesn't drive citations  `40.10`
*useful · content insights · source 40*

Kasra's schema testing led him to conclude schema 'does help with AI Overviews, but not in the way people think' - he doesn't believe it's a direct ranking factor for AI citation, but says it 'ties up a lot of loose ends' instead. His example: updating a site's 'sameAs' schema from pointing at a declining review platform (Trustpilot) to a new one (Feefo) seemed to indirectly prompt Google to re-evaluate and boost the new platform's ranking faster than it otherwise would have. Conversely, in a controlled test he added false schema to a bakery website claiming 'this is a website about cats,' and Google did not pick up or act on the false categorization at all. His main personal reason for using schema is unrelated to AI Overviews entirely - he uses it specifically to help secure and maintain a Google Knowledge Panel.

> "does help with AI Overviews, but not in the way people think"

**Evidence:** Kasra's own single-variable schema tests: updating 'sameAs' schema from Trustpilot to Feefo appeared to indirectly help Feefo's ranking move up, e.g. from position 19 upward; conversely, inserting false schema on a bakery site claiming 'this is a website about cats' had zero measurable effect.

**Apply:** Use schema, including 'sameAs,' as a maintenance and consistency signal - keep it current whenever you change review platforms, social profiles, or brand associations - rather than as a lever expected to directly move AI-citation rankings on its own; pair schema updates with the real underlying change rather than expecting schema alone to carry the signal.

### 7. Serve HTML server-side so crawlers and LLMs never have to render your page  `74.12`
*useful · best practices · source 74*

David Quaid reads the starter guide's 'check whether Google sees the page the same way you do' step and says what it really asks is whether you are using client-side or server-side rendering. He credits Gagan Ghotra for sharing that platforms like Lovable now use server-side rendering. The benefit he states is that both Googlebot and LLMs get the page as HTML and process it directly, without downloading and rendering it, which takes more time. The failure mode is specific: if the crawler makes a mistake, does not download everything, or cannot handle the JavaScript version in use, it cannot see the text on the page at all. He separately notes that sites built on Wix, Webflow or Lovable already have this handled, so the concern is mostly for custom builds.

> "are you using client side rendering or serverside rendering"

**Evidence:** David, crediting Gagan Ghotra, notes Lovable now uses server-side rendering so bots and LLMs receive processable HTML.

**How to do it**

1. Fetch a key page with curl or view-source and check whether the body copy is present in the raw HTML.
2. Run the same URL through GSC's URL Inspection live test and compare the rendered HTML to the raw response.
3. If the main content only appears after JavaScript executes, move that content to server-side rendering or static generation.
4. Prioritize the templates that carry your ranking content: articles, product pages and reference pages.
5. Re-test after the change with the raw fetch, not just the rendered view.
6. Repeat the raw-fetch check after any framework upgrade, since a JavaScript version change can silently break it.

**Tools:** Google Search Console

**Pitfall:** Passing the rendered-view test in GSC and assuming you are fine. The risk David names is the crawler failing to render at all, which the successful render test does not reveal.

**Apply at Pabau:** Pabau's WordPress pages are server-rendered by default, so this is a check rather than a project. David should run a raw-fetch test on any page type using client-side components and confirm body copy appears in the source.

**Apply anywhere:** Confirm your main body copy appears in the raw HTML response, not just the rendered view, and move any JavaScript-dependent content server-side.

### 8. Ship a lean Organization schema with seven named properties  `69.8`
*useful · concrete actions · source 69*

Smarty is deliberately conservative on schema depth. She says how detailed schema should be is a matter of a lot of debate and recommends erring toward clarity rather than too much detail. Her list of what to include is specific: the business name as given in the official documentation, an alternative business name based on how searchers may refer to the business, address and contact details, logo, foundation date, founder's name with an embedded Person schema for more detail, and sameAs properties linking to official social profiles. That is a short, checkable set. The alternateName recommendation is the least common of these and the one that maps directly to branded query variants.

> "based on how searchers may refer to your business"

**How to do it**

1. Add Organization schema to the About page covering name, alternateName, address, contactPoint, logo, foundingDate and founder.
2. Set name to the legal or official business name used in your own documentation.
3. Pull the alternateName values from the branded queries in Search Console, including misspellings and shortened forms searchers actually use.
4. Embed a nested Person schema on the founder rather than giving a bare string.
5. List every official social profile URL under sameAs, and only profiles you actually control.
6. Keep the markup facts identical to the visible copy on the page.
7. Validate in the Rich Results Test and resist adding properties beyond this set.

**Tools:** Google Search Console, Schema.org

**Pitfall:** Over-stuffing the markup with every available property until the core facts are buried, or letting sameAs point to abandoned profiles that contradict the current positioning.

**Apply at Pabau:** Pabau's Organization schema should carry the legal entity name, alternateNames drawn from GSC branded queries, the founding date, the founder with nested Person schema, and sameAs links to the profiles Pabau actively maintains.

**Apply anywhere:** Mark up the About page with a deliberately short Organization schema: name, alternateName from real branded queries, address, contact, logo, founding date, founder as nested Person, and sameAs for controlled profiles only.

### 9. Show a last updated date beside the publish date in article schema  `119.8`
*useful · concrete actions · source 119*

Grow and Convert close their best practices with this tip. Add the last updated date alongside the original publishing date, in the article schema and on the page. Their stated reasoning is twofold: showing both dates helps Google catch the update more easily, and it signals to readers that the content is current. They report from their own work that displaying a last updated date can encourage an immediate boost in keyword rankings for older pages that have just been refreshed. They note the change is normally made in the content management system rather than by hand. Note this is a display and markup change that supports a real update, not a substitute for one, and the base elsewhere warns against date-bumping a page you have not actually rewritten.

> "displaying the "Last Updated" date can encourage an immediate boost"

**Evidence:** Grow and Convert report seeing an immediate keyword ranking boost on older pages after adding the last updated date to recently refreshed content.

**How to do it**

1. Check whether your CMS already emits dateModified in the Article schema and whether it is visible on the page.
2. Configure the template to output both datePublished and dateModified in the structured data.
3. Surface both dates in the byline area so readers can see the original and the update.
4. Make sure dateModified only changes when the body copy genuinely changes, not on every save.
5. Validate a refreshed URL in the Rich Results Test to confirm both dates parse.
6. Request indexing for the refreshed URL so the new date is picked up quickly.
7. Watch the keyword for the following few weeks to see whether the boost lands.

**Tools:** Google Search Console

**Pitfall:** Wiring dateModified to any template or plugin save. Every page then shows a fresh date, the signal becomes noise, and you have date-bumped a library you did not update.

**Apply at Pabau:** Pabau's /blog/ and /templates/ templates should print both dates and emit dateModified only on real content edits. David should confirm the WordPress theme is not touching dateModified on unrelated saves.

**Apply anywhere:** Emit both datePublished and dateModified in your article schema and show both on the page, but only let the modified date move when the content actually changes.

### 10. Small/new sites face a real stochastic 'luck factor' in ranking  `38.5`
*useful · content insights · source 38*

Kalin describes repeated real-world experiments — publishing near-identical rewritten content with matching link profiles across five to ten brand-new domains — that consistently produce inconsistent outcomes: some domains rank, others don't, with no theoretical SEO explanation for the split, and the pattern repeats every time the test is run. He attributes this to a deliberately stochastic component in Google's algorithm (speculatively likened to hashing the domain) designed to resist reverse-engineering, which affects small or new sites far more than giant authoritative ones like CNN or Fox News, where the 'luck factor' becomes statistically negligible. A supporting anecdote: a friend who exited an iGaming SEO affiliate business for 'mid-eight-figures' then launched a brand-new, fully white-hat SaaS whose homepage simply refused to index for two to three months, prompting a four-figure bounty just to find out why.

> "Every time, some rank and some don't"

**Evidence:** Described experiment pattern: 'get five or ten domains, put up absolutely analogous content... with the same links, and try to rank them. Every time, some rank and some don't.' Plus the SaaS-homepage-non-indexing anecdote with a four-figure bounty offered to explain it.

**Apply:** Don't always assume a ranking or indexing failure has a discoverable root cause (content quality, a Google update, brand trust) — especially on small or newer sites, some variance may be structurally random, so hedge by diversifying pages/domains rather than pouring indefinite effort into 'fixing' one stuck URL.

### 11. Stop answering every indexing question with 'submit a sitemap'  `74.24`
*useful · best practices · source 74*

David Quaid describes a specific organizational failure pattern. Web teams pull SEO tickets or inherit SEO work, do their own research, and someone joining a new project puts up a sitemap. Hundreds of pages then get indexed and the team concludes the sitemap caused it. His correction is that you have to understand how sitemaps actually work, and that on low-authority sites they just do not. He says the development guide itself tells small sites with no authority that they do not need a sitemap. His instruction, repeated for what he says is the hundredth time, is that answering any question about content not being indexed with 'sitemap' is not helpful. He contrasts it with high-authority sites, where sitemap URLs land in the highest-priority crawl queue and get indexed reliably, which is why the belief keeps getting reinforced by people who worked on big sites.

> "anytime somebody asks a question about content not being indexed and you just say sitemap that's not very helpful"

**Evidence:** David notes Google's own development guide tells small sites with no authority they do not need a sitemap.

**How to do it**

1. When a page is not indexed, check first whether any already-crawled page links to it.
2. Second, check whether the content is reachable in the raw HTML without JavaScript rendering.
3. Third, check whether another URL on your site targets the same slug, title or H1 and is winning instead.
4. Only then look at the sitemap, and treat it as a diagnostic on URL counts rather than a fix.
5. On a low-authority site, add internal links from ranking pages instead of resubmitting the sitemap.
6. Record which action actually preceded indexation, so the team stops attributing it to the sitemap by default.

**Tools:** Google Search Console

**Pitfall:** Attributing a wave of indexation to a newly submitted sitemap when the real cause was the pages finally being linked from crawled pages. The wrong lesson then gets applied to every future indexing problem.

**Apply at Pabau:** David should write the indexing triage order into the Pabau process: internal links first, rendering second, slug and title collisions third, sitemap last. That stops the default sitemap answer from absorbing the investigation.

**Apply anywhere:** Triage non-indexed pages in this order: internal links from crawled pages, raw-HTML accessibility, slug and title collisions, then the sitemap last.

### 12. Stop treating heading order and valid HTML as ranking factors  `74.13`
*useful · best practices · source 74*

David Quaid points out that the starter guide's non-factors list now includes the number and order of headings. Having headings in semantic order does not matter. You can run H1, H3, H2, H1, H4 and it makes no difference. Google used to list this and changed it. His stated mechanism is that the web in general is not valid HTML, so Google cannot depend on semantic meaning hidden in markup. He calls the belief that code quality is a Google factor a fabricated myth in the web development world, and pushes back on the standard rebuttal that you could publish a broken page. A broken page, he says, is not the same as having quality signals; there is no code-quality signal. He adds there is no ideal number of headings either, with the only test being that if you think it is too much, it probably is.

> "You can have H1, H3, H2, H1, H4, it just doesn't matter"

**Evidence:** Google's own starter guide lists number and order of headings as something not to focus on; David notes it used to be listed differently and was changed.

**How to do it**

1. Remove heading-order violations from your SEO audit template and your dev ticket backlog.
2. Remove HTML validation errors from the SEO scoring; keep them in the accessibility and rendering backlog where they belong.
3. Keep one clear H1 per page for user comprehension and snippet clarity, not because the order is scored.
4. Fix only markup errors that actually break rendering or hide text from a crawler.
5. Redirect the reclaimed dev time toward internal linking and page-speed work that has a stated mechanism.
6. When a tool flags heading structure, check whether the flag comes with a mechanism before actioning it.

**Pitfall:** Auditing tools generate large heading-hierarchy and HTML-validity reports that look actionable. Working through them consumes developer time without a stated ranking mechanism behind it.

**Apply at Pabau:** David should drop heading-order and HTML-validation findings from the Pabau on-page audit unless they break rendering. Keep the article block contract as a house-style requirement, not as an SEO one.

**Apply anywhere:** Drop heading-order and HTML-validity items from your SEO audit unless they break rendering, and reallocate the time to internal linking.

### 13. Treat .com-to-.ai domain migration as high SEO risk, low reward  `46.10`
*useful · best practices · source 46*

Travis reports fielding a wave of clients wanting to migrate their entire site from a .com to a .ai ccTLD purely for the PR and marketing optics of 'going all-in on AI,' which he notes tends to bump stock price or funding-round perception. His standing advice: any URL or domain change is inherently risky because backlinks and internal links pointing at old URLs never pass 100% of their link equity through a redirect, and crawlers need extra steps to process the change, so he only recommends this kind of move when a page or whole site is already so underperforming there's nothing left to lose. Even done well with proper redirects, he expects a real short-term business impact that only 'levels out' after six to 12 months, so the real question for executives is whether the migration is worth that measurable revenue risk just for brand optics that may not matter in a couple of years.

> "anytime you're doing URL redirects"

**How to do it**

1. Whenever a domain, subdomain, or major URL-structure change is proposed, first document the current backlink count and top linked URLs via a backlink tool as a before-baseline (inferred).
2. Ask explicitly whether the current domain or page is already 'way underperforming' — if not, treat that as the default reason not to proceed.
3. If proceeding anyway, map every legacy URL to its exact new-domain equivalent and implement 301 redirects at the individual-page level rather than a blanket domain-level redirect (inferred).
4. Communicate the decision to executives in dollar terms, framing it as a specific business risk for a specific number of months, rather than an abstract SEO objection.
5. Set expectations explicitly: measurable negative impact in the short run, with recovery typically only by the 6-12 month mark if redirects are implemented correctly.
6. Re-verify rankings and traffic recovery at the 6-month and 12-month marks post-migration and keep the redirect map live indefinitely.

**Pitfall:** Executives are motivated to make this move by the PR and stock-price optics of publicly 'going all-in on AI,' not by SEO logic, so the SEO team must proactively reframe the conversation in revenue-risk terms before the decision is made, not after.

### 14. Treat SaaS technical SEO as a one-time audit plus monitoring, not a retainer  `108.13`
*useful · best practices · source 108*

Grow and Convert draw a line between site types. Ongoing technical SEO support is genuinely needed in ecommerce, where hundreds of product pages target long-tail queries and the template surface keeps changing. For SaaS companies with largely static marketing sites, technical SEO is about getting the fundamentals right at the start and then monitoring that nothing breaks. They say it can usually be handled with a one-time audit plus occasional follow-up. The trigger for reopening it is a sudden ranking drop spotted in Ahrefs or Semrush, at which point you investigate whether a technical cause is behind it. Their conclusion is that most SaaS companies should not obsess over technical SEO or hire a dedicated specialist, and should put the remaining energy into content and links. This cuts against agency proposals that price technical work as a permanent monthly line.

> "technical SEO for SaaS websites can usually be taken care of"

**Evidence:** Grow and Convert contrast SaaS marketing sites with ecommerce sites carrying hundreds of long-tail product pages that do need continuous technical work.

**How to do it**

1. Run one full technical audit covering canonicals, sitemap, rendering, robots.txt, speed and internal links.
2. Fix everything the audit surfaces in a single project rather than spreading it across months.
3. Set up rank tracking in Ahrefs or Semrush for every target keyword.
4. Set alert thresholds so a sudden multi-keyword drop reaches someone the same week.
5. Only reopen technical work when an alert fires or a platform change ships.
6. Recheck the sitemap and Search Console errors on a fixed monthly cadence, which takes minutes.
7. Redirect the freed budget to content production and link building.
8. Re-audit in full only after a redesign, replatform or migration.

**Tools:** Ahrefs, Semrush, Google Search Console

**Pitfall:** Paying an ongoing technical retainer on a 40-page static marketing site produces monthly reports about trivial issues while the keyword list sits unworked. The opposite risk is skipping monitoring entirely and missing a breakage for months.

**Apply at Pabau:** Pabau sits between the two, since template and code-reference pages are generated at scale. Run the one-time audit on the marketing site, but keep continuous crawl monitoring on the programmatic sections where template changes hit thousands of URLs at once.

**Apply anywhere:** On a mostly static marketing site, do one thorough technical audit, fix everything, then monitor with rank tracking and monthly Search Console checks. Reserve continuous technical work for sites with large generated page sets.

### 15. Treat llms.txt as a proposal with no adopter, not a standard  `86.11`
*useful · best practices · source 86*

Grow & Convert give the provenance of llms.txt so teams can judge it properly. It is a proposed standard from Jeremy Howard, developer and founder of fast.ai, intended to help LLMs crawl and understand a site, conceptually like robots.txt but for AI crawlers. It sounds logical, but there is no evidence that OpenAI, Anthropic or any other major provider actually consumes it. Howard proposed it as an idea he thought the industry should adopt; adoption never followed. Grow & Convert's own tests over the past year found no measurable difference in AI visibility, and they say plainly they do not recommend spending time on it. They apply the same verdict to rewriting headings as questions, arguing that the whole point of an LLM is natural-language understanding, so it does not need your content reformatted to parse it.

> "there's no evidence that OpenAI, Anthropic, or other major LLM providers actually use it"

**Evidence:** Grow & Convert's year of testing found llms.txt made no measurable difference, matching other public tests; llms.txt originated as a proposal by Jeremy Howard of fast.ai with no documented uptake by OpenAI or Anthropic.

**How to do it**

1. Before adopting any AI-crawler standard, check whether a named model provider has publicly documented that it consumes the file.
2. If no provider has, classify it as a proposal and put it behind Tier 1 and Tier 2 work.
3. If you still want to test llms.txt, ship it to a subset of the site and hold a matched subset as control.
4. Track AI mention rate for both subsets over at least four weekly measurement cycles.
5. Drop the tactic unless the test subset separates from the control by more than normal week-to-week variance.
6. Apply the same evidence test to question-shaped headings, FAQ blocks and AI-targeted schema before rolling them out sitewide.

**Pitfall:** These tactics are easy to justify because they sound mechanically sensible, and because nothing bad happens when you ship them. The cost is the roadmap time taken from ranking work that does move mentions.

**Apply at Pabau:** David should not add llms.txt to pabau.com or rewrite existing H2s into questions for AI reasons. Pabau's house block contract already includes key takeaways and FAQ blocks for reader and Google reasons, which is a fine reason to keep them; just don't count them as AI visibility work.

**Apply anywhere:** Don't add llms.txt or rewrite headings into questions for AI reasons. Keep FAQ and takeaway blocks if they serve readers and Google, but don't count them as AI visibility work.

### 16. Treat on-page SEO as a publish checklist, not a ranking strategy  `153.10`
*useful · best practices · source 153*

Grow and Convert classify on-page SEO as a ticket to entry rather than a competitive edge. Their list is specific: keyword in the title, a meta description, internal links, keyword in the URL, relevant keywords through the body, relevant headers, and a clear crawlable site structure. Their point is that these are straightforward compared to analyzing search intent and writing content that converts, so they should be checked off for everything you publish and then dropped as a topic of debate. The implication for planning is that time spent optimizing on-page elements past the checklist is time not spent on the factors that actually differentiate: topical relevance, intent match and unique content.

> "basic "tickets to entry" for your site or your pre-publication checklist"

**Evidence:** Grow and Convert's position from 80+ clients: on-page items are prerequisites that every published page passes, while intent match and unique content are where the ranking difference comes from.

**How to do it**

1. Write the seven on-page items into a single pre-publication checklist in your CMS or brief template.
2. Require the exact keyword in the title, the URL slug and the H1 before anything is queued for publishing.
3. Require a written meta description rather than letting the CMS generate one.
4. Require at least one relevant internal link in and one out on every new page.
5. Check headers describe the section rather than repeating the keyword.
6. Confirm the page is reachable from a navigational path and appears in the sitemap.
7. Once the checklist passes, stop optimizing on-page and move the remaining hours to intent and originality work.
8. Audit the checklist quarterly across the library rather than revisiting it page by page.

**Tools:** Screaming Frog

**Pitfall:** Teams that keep re-tuning keyword density, header wording and meta descriptions on already-optimized pages. The checklist is binary and the effort past it returns nothing.

**Apply at Pabau:** Fold the seven items into Pabau's pre-publish gate so they are verified once and never revisited. David should keep the /SEO command's on-page work bounded to that checklist and spend the saved time on intent and originality.

**Apply anywhere:** Turn on-page SEO into a seven-item pre-publish checklist — keyword in title, URL and headers, a written meta description, internal links in and out, and a crawlable path — then stop. Past the checklist, the returns are in intent and originality.

### 17. Treat schema as supporting evidence, not the mechanism  `73.13`
*useful · best practices · source 73*

Barnard uses sameAs schema and recommends it for any new website, but he is firm about its weight. Adding schema to the entity home is helpful but not necessary, and you do not have to freak out if you have not got it. Schema markup is supporting evidence, not the be-all and end-all a lot of people believe. He backs it with a case: one client refused schema markup outright and got a knowledge panel anyway. The one common sameAs mistake he names is pointing at a URL that does not agree with your entity home - if you have a profile you cannot control that says something that does not corroborate what you are saying, do not link to it at all. He also offers a practical shortcut: in WordPress you can paste schema into an HTML block in the middle of the page, where it will not render to people but the machine will read it, so no plugin is needed.

> "Schema markup is supporting evidence"

**Evidence:** Barnard reports a client who refused schema markup entirely and still got a knowledge panel; he separately calls the simplest possible schema the most solid.

**How to do it**

1. Get clarity and consistency on the entity home and across the footprint before spending any time on markup.
2. Generate simple Organization or Person schema, keeping it to the simplest possible form rather than an elaborate graph.
3. List in sameAs only the profiles whose stated facts agree with the entity home.
4. Remove from sameAs any profile you cannot control that contradicts your facts, rather than trying to outweigh it.
5. In WordPress, paste the JSON-LD into an HTML block mid-page instead of installing a schema plugin; it stays invisible to readers and readable by crawlers.
6. Keep the schema values byte-identical to the visible copy on the entity home.
7. Do not delay the rest of the entity work while waiting for developer time on markup.

**Tools:** Kalicube Pro, WordPress, Schema.org

**Pitfall:** Listing every profile you own in sameAs. A profile whose facts disagree with the entity home actively adds ambiguity, and Barnard's advice is to drop the link rather than include it.

**Apply at Pabau:** Pabau's Organization schema should list only profiles whose descriptions match the About page. Audit the current sameAs list and drop any stale profile rather than correcting it later.

**Apply anywhere:** Use simple Organization or Person schema with a sameAs list restricted to profiles that agree with your entity home. Treat it as supporting evidence: get the copy and the footprint right first, since entities get built without markup.

### 18. Validate schema strictly — one error breaks everything  `09.6`
*useful · best practices · source 09*

Google is described as far less forgiving of schema errors than of broken HTML: Googlebot tolerates malformed HTML by pattern-matching around it (the source jokes there are "16 flavors of HTML" it accounts for), but a single mistake in schema can make the whole structured-data block fail, as the source demonstrates by mis-adding schema via the Data Highlighter tool and getting a parsing error that silently removed the expected profile-page result. On site types where schema is functionally mandatory (the source's example: job listing sites), a schema mistake can even trigger a manual action — which does roll back automatically, but the source notes that can take up to a year, making upfront validation far cheaper than waiting it out.

> "once you make a mistake in schema, everything breaks down"

**How to do it**

1. After adding or editing schema markup, validate it (e.g. via Google's Data Highlighter tool or Search Console's rich-result testing) rather than assuming it rendered correctly.
2. Check Google Search Console for a parsing error and confirm the expected enhancement (e.g. a profile-page result) is actually appearing.
3. Remember schema has no error tolerance the way HTML does — a single mistake can fail the entire structured-data block rather than degrade gracefully.
4. On site types where schema is functionally mandatory (e.g. job listing sites), treat validation as higher-stakes, since a mistake there can trigger an actual manual action.
5. If a manual action does occur from a schema error, expect it can roll back automatically but may take up to a year, so prioritize prevention over waiting it out.
6. Re-validate after every schema edit, not just on first publish, since edits can reintroduce parsing errors.

**Tools:** Google Search Console, Data Highlighter

**Pitfall:** Treating schema like forgiving HTML — a single structural mistake can silently remove an entire expected feature (like a profile page) or, on schema-mandatory site types such as job boards, trigger a manual action that can take up to a year to automatically roll back.

### 19. Why citation listings don't get seen, and how indexers force the crawl  `59.3`
*useful · concrete actions · source 59*

Cody raises a real problem: citation directories are massive sites, so a new listing on one often never gets crawled. Jackie's answer is SpeedyIndex, and his explanation of the mechanism is the interesting part. It's a SaaS product built inside Telegram, and what it does is maintain a set of sites whose only purpose is to trap Google crawlers - there's an entrance to the site and it keeps pinging itself internally, so a crawler that enters keeps crawling. When someone submits a link to be indexed, the trap site gains an outbound link to it, so the crawler is forced to go there and crawl it. Cody's analogy is the infinite staircase in Inception, with an exit added.

> "we use something called SpeedyIndex"

**How to do it**

1. After creating citations, check indexation rather than assuming it - a new listing on a huge directory frequently never gets crawled, which is the problem Cody raises.
2. Collect the listing URLs into a list; you need the specific listing URL, not the directory's homepage.
3. For pages on domains you control, use Search Console URL Inspection and request indexing - the sanctioned route, and the only one available for your own site.
4. For third-party listings you cannot submit through Search Console, use an indexing service. Jackie uses SpeedyIndex, which runs as a Telegram bot rather than a conventional web app.
5. Understand the mechanism so you can judge it: the service maintains sites whose only purpose is to trap Google's crawler in an internal loop, and when you submit a URL the trap site gains an outbound link to it, forcing the crawler to follow. Cody's analogy is the infinite staircase in Inception with an exit added.
6. Submit in batches and re-check after a few days with an exact-URL search.
7. Where a listing still won't index, treat that as a signal about the directory's own value and stop submitting to it.
8. Layer social links to the important listings as a second route, per the parasite-indexing entry - profile posts pointing at the listing URL give the crawler an organic path.

**Tools:** Google Search Console, SpeedyIndex

**Pitfall:** Crawler-trap indexing services manipulate Google's crawl scheduling and sit outside its guidelines. The diagnostic value is what transfers regardless: an unindexed listing on a very large directory is the normal outcome, not a mistake you made, so it should not be read as a problem with your NAP data.

**Apply at Pabau:** For Pabau, the practical takeaway is to verify indexation of new pages via Search Console rather than assuming publication equals indexing, and to treat directories whose listings never index as not worth the submission time.

**Apply anywhere:** The practical takeaway is to verify indexation of new pages via Search Console rather than assuming publication equals indexing, and to treat directories whose listings never index as not worth the submission time.
