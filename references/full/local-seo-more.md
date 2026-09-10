# Local SEO — supporting

13 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Add local-qualified BOFU terms when the company has offline history  `140.10`
*useful · concrete actions · source 140*

ADA Compliance Pros had spent over a decade serving California businesses on physical premises compliance before the website service existed. When the client raised local targeting, Lewis did keyword research specifically for high-intent local variants of the new service, and reports the resulting article was one of the highest converting they have. The mechanism worth taking from this is that an existing offline footprint gives a local page real substance and credibility the national competitors cannot claim. It is not a generic city page. The prerequisite is that the company genuinely operated in that geography, which is what makes the page more than a template swap. She kept the same bottom-of-funnel filter on the local list rather than chasing local informational terms.

> "it turned out to be one of the highest converting articles"

**Evidence:** ADA Compliance Pros had a decade of California local compliance work, and the local high-intent article became one of the campaign's highest converting pieces.

**How to do it**

1. Check whether the company has real operating history in a named state, city or region.
2. Take the bottom-of-funnel terms that already work and add the geography as a qualifier.
3. Search each local variant and confirm the ranking pages are national competitors with no local presence.
4. Write the local page around the actual local history: years served, local clients, local regulation specifics.
5. Cite the local legal or regulatory detail that differs from the national picture, since that is what a local searcher is checking.
6. Keep the same conversion offer as the national bottom-of-funnel pages, not a softer local one.
7. Track conversions on the local page separately before building more geographies.

**Pitfall:** Spinning up city pages with no operating history behind them produces thin duplicates that neither rank nor convert. The signal is a page that would read identically with the city name swapped.

**Apply at Pabau:** David should build local bottom-of-funnel pages only where Pabau has real clinic density, and write them around the local regulatory detail aesthetic practices actually face there. A UK page and a US page must differ in substance, not just spelling.

**Apply anywhere:** If the business has genuine operating history in a region, add that geography as a qualifier to your bottom-of-funnel terms. Write the page around the real local history and the local regulatory specifics, keep the same conversion offer as the national pages, and only expand to more geographies after one converts.

### 2. Build NAP-consistent local citations, outsourcing past 3 sites  `07.16`
*useful · concrete actions · source 07*

For any local/service-area business, the recommended first backlink layer (before any paid link-building) is local citations — directory listings such as Nextdoor Business, Foursquare, and Better Business Bureau (BBB should always be claimed). These can be sourced quickly by asking ChatGPT/Claude for a location-specific directory list, but the critical execution detail is NAP consistency: Name, Address, and Phone number must be entered identically across every directory, since inconsistency undermines local SEO value. For agencies or teams handling three or more sites, manual entry doesn't scale, so the creator delegates to BrightLocal's local citation building service at roughly $3.20 per citation (cheaper in bulk, e.g. ~$100 for 20 citations on one site) rather than risking low-quality marketplace gigs like Fiverr's '$5 for 300 citations' listings, which carry high risk of inconsistent or low-quality data.

> "around $3.20 per citation for the most part"

**How to do it**

1. For each business/location, ask ChatGPT or Claude: 'show me all the free online listing directories for businesses in [city, state]', including the business type for a more targeted list.
2. Cross-check the suggested directories manually; expect core ones like Nextdoor Business, Foursquare, and BBB to appear, and always prioritize claiming the BBB listing.
3. Create a master reference document with the business's canonical Name, Address, and Phone number formatted exactly as it should appear everywhere. (inferred, to prevent drift)
4. Create a free account on each directory that offers one.
5. Enter the NAP information exactly as written in the master reference on every single listing, with zero formatting variation.
6. If handling citations for three or more businesses/sites, stop doing this manually and use a paid service such as BrightLocal's local citation building service instead.
7. Budget approximately $3.20 per citation through BrightLocal (lower per-unit cost at bulk volume), e.g., roughly $100 for 20 citations on a single site.
8. Avoid ultra-cheap marketplace citation services, since NAP accuracy and directory quality are unreliable at that price.
9. After a few weeks, spot-check a sample of the new listings to confirm they're live and NAP-consistent. (inferred verification step)

**Tools:** ChatGPT, Claude, BrightLocal

**Prompt / template:**

```text
show me all the free online listing directories for businesses in [location]
```

**Pitfall:** Buying cheap bulk citation packages from marketplaces like Fiverr (e.g., '300 USA local citations... for $5') — inconsistent NAP data across low-quality directories can actively hurt local SEO rather than help it.

### 3. Gate review requests behind a private satisfaction check first  `08.3`
*useful · concrete actions · source 08*

To avoid generating negative public reviews, the recommended flow never sends a customer straight to a public review link. Instead, an automated post-job text/email routes the customer to an intermediate 'were you satisfied?' page: a 'yes' answer forwards to the real review link, while a 'no' answer routes to a private feedback form so the complaint can be resolved directly instead of becoming a public review. The stated principle is that avoiding a negative review is worth almost any cost, including full refunds, because of how heavily average star rating affects ranking.

> "you want to send them to another page first"

**How to do it**

1. Set up (or use your existing CRM/CMS's built-in feature for) an automated post-job text and/or email trigger sent to every completed customer.
2. Route that message to an intermediate 'were you satisfied?' landing page first — never link directly to the public review platform.
3. If the customer selects 'yes,' redirect them immediately to the actual public review link (Google, Yelp, Facebook, etc.).
4. If the customer selects 'no,' redirect them to a private feedback/contact form instead so the complaint reaches your team directly rather than becoming a public review.
5. Follow up personally on every 'no' response to resolve the underlying issue, up to and including a full refund if needed, since preventing a public negative review is treated as worth that cost.
6. For staff who consistently fail to generate positive reviews or generate negative ones, treat it as a performance issue requiring correction or removal from customer-facing work.
7. For higher-consideration or emotionally sensitive services, use multiple follow-up contact attempts (e.g., both email and text) after the engagement closes rather than a single ask, since customers in that situation are less naturally forthcoming with reviews.

**Pitfall:** Sending customers straight to the public review link without a satisfaction filter first — this risks capturing avoidable negative reviews publicly instead of routing dissatisfaction to a private channel where it can be fixed.

### 4. Layer semantic and local signals onto local-intent pages  `47.9`
*useful · concrete actions · source 47*

A Reddit commenter describes a before/after content-optimization technique combining NLP, natural language processing or semantic keyword enrichment, with local-intent signals, illustrated with a 'best dentist in Hoboken' example. The before version is generic, repeating only the exact-match keyword phrase mechanically across a few short sentences with no semantic depth. The after version keeps the exact primary keyword in the first sentence, but layers in semantically related terms such as 'dentist near me,' 'dental clinic,' and 'teeth whitening,' explicit local signals such as 'Hoboken, New Jersey' and 'near downtown Hoboken,' and topical depth about the actual services and credentials such as preventative, cosmetic, and emergency care and a licensed team, all written in natural, readable language rather than robotic keyword repetition. The commenter reports this combined approach measurably boosted their website traffic once applied after first fixing the site's technical SEO issues.

> "You're adding topical depth, like services and licensed team"

**How to do it**

1. Identify your primary local-intent keyword phrase for a given page, following the pattern of service plus location, such as 'best dentist in Hoboken'.
2. Keep that exact primary keyword phrase in the page's first sentence, unchanged.
3. Brainstorm a list of semantically related terms a real searcher would also use or expect, such as 'dentist near me' or 'dental clinic,' and weave several of them naturally into the body copy.
4. Add explicit local signals beyond just the city name, such as the state or nearby neighborhood references.
5. Add genuine topical depth about your actual services and credentials, such as specific treatment types and staff qualifications, rather than a vague one-line service list.
6. Write all of the above in natural, human-readable language rather than mechanically repeating the exact keyword phrase over and over.
7. Fix any underlying technical SEO issues on the site before or alongside this content optimization, since the reported traffic gain only appeared after both technical fixes and content optimization were done.

### 5. Local EMD playbook: 50 pages, one service, one week  `15.5`
*useful · concrete actions · source 15*

For local lead generation, James says an exact-match domain can work within about a week if scoped narrowly: pick one core service and cover it across roughly 50 location pages rather than trying to cover multiple services at launch, with genuinely useful (not thin) content on each page. Using a domain that already has an existing Google Business Profile adds extra local trust versus a completely fresh domain. The expected early return is modest - roughly £300-500 a month - which gets reinvested into building a second and third microsite on the same model, and only once a given vertical or client 'pays nicely' does it graduate into a bigger, more brandable, multi-service site.

> "you can make an EMD work within a week"

**How to do it**

1. For a local service business, pick one core service and scope the site to that single service across roughly 50 location pages rather than covering multiple services at launch.
2. Write genuinely useful, non-thin content for each of the 50 location pages.
3. Where possible, use or acquire a domain that already has an existing Google Business Profile attached for extra local trust.
4. Expect this scoped local approach to start ranking and earning within about a week, versus months for competitive national terms.
5. Set an initial revenue benchmark of roughly £300-500 a month per microsite rather than expecting a large number immediately.
6. Reinvest that early revenue into building a second and then a third microsite using the same one-service, many-locations model.
7. Once a specific vertical or client consistently converts and pays well, graduate it into a bigger, more brandable, multi-service site rather than keeping it as a single-service microsite indefinitely.

**Tools:** Google Business Profile

### 6. Local sponsorship benchmarks: $350-500 a placement, 5-10 to start, hold for a year  `30.e2`
*useful · general insights · source 30 · universal-edition only*

Ellen gives unusually concrete numbers for local sponsorship link building. Pricing is driven by market saturation rather than city size, and by the size of your link gap against competitors' target URLs — if rivals have three or four hundred more backlinks to a page, that page may be the wrong place to start, versus one where the gap is only about ten links. Her typical pilot campaign runs about $2,000 including fee for four backlinks to local organizations, and location links overall run $350 to $500 per link including fee. She stresses you do not need hundreds of these per month, because local plus contextual relevance is strong enough that most businesses see movement without high volume; what matters more is consistency, with a one-year minimum visibility commitment. Starting at five to 10 sponsorships is her recommendation. She also cites her own research survey with the caveat that she cannot yet call it statistically firm: most businesses sponsor one to 10 organizations a year, but among those sponsoring 10 or more, 83% reported a stronger, major impact on visibility.

> "location links, across the board, including our fee, run $350 to $500 per link"

**Evidence:** Operator pricing from a company that brokers local sponsorship placements ($2,000 pilot for four links; $350-500 per placement including fee; one-year minimum), plus a self-run survey of sponsoring businesses in which 83% of those at 10-plus sponsorships a year reported major visibility impact — explicitly flagged by the speaker as not yet statistically firm.

**Apply:** Use these as planning benchmarks rather than a promise: budget roughly $350-500 per local placement, start with five to 10 rather than a large campaign, and commit to about a year before judging the result. Choose the target page by link gap — a page where you trail by around ten links is a far better first target than one where competitors are hundreds ahead.

### 7. Manufactured navigation signals: the rideshare and step-app variants  `59.15`
*useful · general insights · source 59*

Click-through and navigation to the Business Profile is the third of Jackie's ranking factors, and he describes two ways of forging it. The manual version: take an Uber to your own business from a few blocks away, setting the destination to your Google Business Profile, and offer the driver a five-dollar tip for a five-star review on arrival - 'an Uber ride is a CTR if you guys didn't know'. The industrialised version is the one covered separately in this collection, where CTR vendors partner with gamified step-counting apps and route their users to the locations of paying clients. What makes this section worth keeping together is the mechanism it reveals: the signal Google is reading is a real human, on a real device, navigating to a real address, which is why the manipulation is effective and why detecting it is genuinely hard. Cody's field test of one such vendor moved a location from outside the map pack to inside it in about 30 days, and the vendor enforced area exclusivity - one HVAC company per territory - which is itself the tell that the supply is engineered rather than organic.

> "An Uber ride is a CTR"

**How to do it**

1. When a competitor's map-pack position moves without a corresponding change in reviews, citations or content, add manufactured navigation to the list of explanations.
2. Look for the vendor tells Cody identifies: an area-exclusivity clause, and a ranking guarantee scoped to the smallest possible radius - often one the business already ranks in.
3. Ask any vendor offering guaranteed map-pack placement how the engagement is generated, and get the answer in writing, because the profile suspension risk sits with the business.
4. Build the legitimate version of the same signal instead: make the profile's directions, call and website actions work correctly, post to the profile weekly, and drive real customers to find you through Maps rather than through a bookmarked URL.
5. Track profile actions - direction requests, calls, website clicks - in the Business Profile performance report, so you can see your own genuine engagement trend and judge whether it plausibly supports your position.
6. Understand that because the manipulated signal is real people on real devices, Google's countermeasure tends to be pattern-level and delayed - which is why operators get months of benefit before enforcement arrives.

**Tools:** Google Business Profile

**Pitfall:** Both variants breach Google's prohibited-content and fake-engagement policies, and the second one - routing the users of a fitness app to a paying client's premises without telling them why - deceives people who believe they are playing a walking game. This entry sets out how the mechanism works and how to spot it rather than how to operate it.

**Apply at Pabau:** For Pabau's clinic customers the useful output is a short list of questions to ask a local SEO vendor - how is the engagement generated, is there an exclusivity clause, what radius does the guarantee cover - because the answers separate a legitimate provider from one putting the clinic's profile at risk.

**Apply anywhere:** The useful output is a short list of questions to ask any local SEO vendor - how is the engagement generated, is there an exclusivity clause, what radius does the guarantee cover - because the answers separate a legitimate provider from one putting the business's profile at risk.

### 8. Only add a city modifier when the answer actually varies by location  `11.15`
*useful · best practices · source 11*

Gotch's filter for local keyword expansion: before adding a city or location modifier to a query, check whether the underlying answer genuinely differs by geography. His test case is a supplement company considering 'what is creatine in St. Louis' — a wasted target because creatine is chemically identical everywhere, so the query has no real location variability, versus 'how much does an SEO consultant cost,' which legitimately varies by market and is worth localizing. Slapping a city name onto a query without this variability check is, in his words, 'literally trying to manipulate the algorithms,' and real searchers won't phrase queries that way, so it produces pages that don't actually match how people search.

> "You want to keep only queries that have variability"

**How to do it**

1. For every candidate query being considered for local-modifier expansion, ask whether the true answer would meaningfully differ from one city or region to another.
2. If the answer is universal, such as a product definition or fixed technical fact, reject the local-modifier version regardless of how easy it would be to produce.
3. If the answer plausibly varies by market, such as pricing, regulation, or local competition, proceed to build the localized query and page.
4. Sense-check the final localized query by asking whether a real person would plausibly type it that way, not just whether it's grammatically valid.

**Pitfall:** Adding a location modifier to every query mechanically to scale a local-SEO program — Gotch calls this manipulating the algorithm rather than serving a real searcher, since no one actually searches a location-invariant fact with a city attached.

### 9. Phony Business Profiles propped up by citation networks  `59.16`
*useful · general insights · source 59*

A short aside from Jackie with an important structural point behind it. He notes that once you have a citation layer built, you can use it to register phony Google Business Profiles, because the citations send the entity-confirmation signals Google looks for - and if Google's objection is that there's no Business Profile for an entity it can see referenced across many directories, adding a missing place claim makes the new profile 'more sticky' than registering it cold. The mechanism is the inverse of the legitimate one: instead of citations confirming a real business, a directory footprint is manufactured first and the profile is created to match it. It's worth documenting because it explains a common pattern in competitive local markets - lead-generation profiles at addresses with no premises, feeding calls to a single operator - and because the countermeasure is available to anyone: Google's redressal process accepts evidence-backed reports of profiles at non-existent locations.

> "register phony Google business profiles"

**How to do it**

1. Recognise the pattern in your market: multiple profiles in the same category at addresses that are residential, virtual offices, or mailbox services, often with similar phone number ranges.
2. Check whether the address resolves to real premises in Street View, and whether the profile has any photographs of an actual location.
3. Look for the citation footprint that supports it - a profile with 100+ directory listings created in a short window and no other web presence is manufactured rather than established.
4. Check whether the phone numbers forward: lead-generation profiles typically route to one central operator.
5. Report confirmed fake listings through Google's Business Redressal Complaint Form with the evidence attached, which is the mechanism designed for exactly this.
6. For your own business, keep the legitimate version of the signal intact - a genuine address, real photographs, and consistent citations - since that is what makes your own profile resilient when Google sweeps a category.

**Tools:** Google Business Profile

**Pitfall:** Registering a Business Profile for a location where the business does not have a genuine presence, or where it does not meet customers, breaches Google's Business Profile guidelines and constitutes misrepresentation - in regulated categories it can also breach advertising and consumer-protection rules. Documented here as a pattern to recognise and report, not a procedure to run.

**Apply at Pabau:** Worth Pabau being able to explain to clinic customers: in competitive treatment categories, fake lead-generation listings are common, they can be reported through Google's redressal form with evidence, and reporting them is usually faster than trying to outrank them.

**Apply anywhere:** Worth being able to explain to any local business you advise: in competitive categories fake lead-generation listings are common, they can be reported through Google's redressal form with evidence, and reporting them is usually faster than trying to outrank them.

### 10. Remove clustered negative reviews to unstick a stalled ranking  `08.2`
*useful · concrete actions · source 08*

When a listing was inexplicably stuck despite having more links and a stronger profile than competitors, the cause turned out to be 80 one-star reviews dragging down the average, even though the business had thousands of positive reviews and competitors had under a thousand reviews total. Hiring a paid review-removal service (Removify) to remove roughly four of the worst offending reviews caused an instantaneous ranking jump, confirming the average star rating — not just review count — was the actual blocker. The specialist tracks this by scanning ranking/review data every 3-5 days (via BrightLocal) specifically so he can pinpoint the exact date any rating shift happens and tie it to ranking movement.

> "they removed about four of those negative reviews, and it shot up"

**How to do it**

1. When a listing's ranking is inexplicably stuck despite strong links and on-page work, pull its review data and check the average star-rating trend over time, not just total review count.
2. Use a rank/review tracking tool (e.g., BrightLocal) to scan the profile every 3-5 days rather than monthly, so you can pinpoint the exact date any rating shift occurred and correlate it with ranking movement.
3. If you find a cluster of 1-star reviews weighing down an otherwise strong review base, first attempt self-service removal by reporting each offending review through the main business account.
4. Also report the same reviews through any additional local-guide accounts you or teammates have access to, adding more total reports against the same reviews.
5. If self-reporting fails to get the reviews removed, engage a paid review-removal service such as Removify to escalate removal.
6. After removal, re-check rankings within days; expect a fast, sometimes instantaneous ranking recovery if the negative reviews were the actual blocker.
7. Budget for the fact that offsetting a single negative review typically requires roughly 40-50 new positive reviews, so treat negative-review prevention as higher leverage than raw positive-review volume.
8. Build review-rating monitoring into a recurring 3-5 day cadence going forward, since Google itself can periodically purge or reinstate reviews and shift your average without any action on your part.

**Tools:** BrightLocal, Removify, Google Business Profile

**Pitfall:** Only tracking total review count and assuming more reviews always helps — average star rating is 'just as important as the amount of reviews, by far,' so a large positive review base can still be neutralized by a small cluster of unaddressed 1-star reviews.

### 11. Use city-level 'sell my house fast [city]' style prompts as the underdog entry point  `81.11`
*useful · concrete actions · source 81*

When Constitution Lending expanded into buying houses for cash, Grow and Convert did not target the national term. They published city-level bottom-of-funnel content and within a few months the brand was being recommended in AI answers for prompts like 'sell my house fast Waterbury' and 'sell my house fast Bristol', while the broader 'sell my house fast Connecticut' still showed almost nothing. The mechanism is the same Underdog SEO logic applied to geography. A small city query has thin, mostly untailored competition, so a page written for that city ranks quickly, and the ranking is what makes the brand available to an LLM grounding a local request. State-level and national terms take longer because the incumbents are already there.

> "sell my house fast Waterbury"

**Evidence:** Constitution Lending was recommended for 'sell my house fast Waterbury' and 'sell my house fast Bristol' within a few months of starting the content, while 'sell my house fast Connecticut' showed little visibility.

**How to do it**

1. List every city and town you genuinely serve, not the whole state.
2. Rank them by population and by how many local competitors already have a dedicated page.
3. Start with the towns where no competitor has a tailored page, even if volume looks negligible.
4. Publish one page per town covering the local specifics: typical timelines, local process, named neighborhoods.
5. Include the differentiator claims from your customer interviews on every town page rather than only on the hub.
6. Add each town prompt to your AI tracker in the natural phrasing a resident would use.
7. Once several town pages rank, build the state-level page and link it to them.
8. Only attempt the national term after the state page ranks.

**Tools:** Traqer

**Pitfall:** Spinning near-identical town pages with only the place name swapped. That is a thin-content pattern, and it also gives an LLM nothing local to say about you.

**Apply at Pabau:** Pabau's location pages should follow this order: start with the specific cities where clinics cluster and no competitor has a tailored page, and only build the country-level page once those rank.

**Apply anywhere:** For a geographic service, start with the smallest towns you actually serve rather than the state or country term. Publish a genuinely local page per town, then work upward to the state and national terms once those rank.

### 12. A reviewed GBP outranks on-page changes to its linked landing page  `08.5`
*context · content insights · source 08*

Adding reviews to a Google Business Profile is described as having more ranking impact on the linked website page than direct changes made to that landing page itself. In a concrete example, a city page stuck around position 40-50 moved into the top 10 purely from attaching a GBP and accumulating five to fifteen reviews, with no additional link building or internal linking involved. The relationship isn't symmetric, though — strong organic rankings on a page (top 2-5 for its keyword) were observed to have little to no reciprocal effect on the attached GBP's own performance, and some GBPs won purely on review strength even with no website attached at all.

> "you've got the best link in the world"

**Evidence:** Worked example: 'you could have been sitting at 40 or 50, and now you're sitting in the top 10 in a lot of cases without any extra links or internal links, instantaneously' after attaching a GBP and adding reviews.

**Apply at Pabau:** This is most directly transferable to any of Pabau's local-presence or partner/reseller listing assets rather than the core SaaS site — where a location-tied profile exists, treat accumulating reviews on it as a stronger lever on that page's ranking than further on-page editing of the page itself.

**Apply anywhere:** This is most directly transferable to any of your local-presence or partner/reseller listing assets rather than the core SaaS site — where a location-tied profile exists, treat accumulating reviews on it as a stronger lever on that page's ranking than further on-page editing of the page itself.

### 13. Pick precise GBP categories and city-only service areas  `08.4`
*context · best practices · source 08*

Rather than maximizing every possible category, categories should be chosen for the exact service intent wanted — a personal injury lawyer listing generic categories like 'attorney' or 'law firm' invites broader, lower-quality leads and can dilute ranking for the specific service actually wanted. Competitor category-matching is discouraged too, since competitors most likely rank due to reviews and on/off-page SEO, not their category selection, unless they have an outright wrong category (rare). For the business description, include target keywords plus the city name; for service areas, list only the exact home city, since Google applies its own radius regardless of any additional cities listed.

> "I don't believe in maxing out every category"

**How to do it**

1. Choose GBP categories based on the exact service/intent you want leads for, not on maximizing category count.
2. Avoid generic top-level categories (e.g., 'attorney') if they would attract broader, lower-intent leads than your actual specialty.
3. Do not copy a competitor's full category list on the assumption it explains their ranking — check whether their success is more likely driven by reviews and on/off-page SEO first.
4. Only treat a competitor's category as something to fix if it's flatly wrong for their business type.
5. Write the GBP business description with target service keywords plus the city name included.
6. For service-area settings, list only the exact home city rather than a long list of surrounding cities, since Google applies its own radius automatically.
7. Periodically re-check assigned categories since Google appears to rotate or reset them over time, and correct them back if they drift.
8. Continue publishing periodic GBP posts even without observed ranking impact, as a hedge in case Google changes how that signal is weighted in the future.

**Pitfall:** Over-indexing on category-maximization or copying a competitor's category setup as the explanation for their rankings, when reviews and on/off-page SEO are the far more likely actual cause.
