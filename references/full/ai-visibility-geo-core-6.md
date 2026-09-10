# AI Visibility / GEO — core (part 6 of 6)

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Treat AI visibility as per-topic, with no transfer between topics  `85.3`
*core · general insights · source 85*

Grow and Convert argue AI search visibility has no real-world brand-level equivalent, unlike domain authority, which stands for something real: how much weight Google's algorithm gives a domain, so a high-authority site outranks a low-authority one all else equal. AI visibility has no such carry. Based on the data they have seen, strong visibility on one topic is not correlated with visibility on another. Their client Mirascope has strong visibility for prompt engineering tools and far less for context engineering platform, two adjacent topics in the same product space. The planning consequence is that GEO cannot be funded as one program with one score. Each topic is its own campaign with its own content, its own citation outreach and its own baseline.

> "that visibility isn't correlated, based on any data we have seen"

**Evidence:** Mirascope, a Grow and Convert client, shows strong Traqer visibility for prompt engineering tools and far less for the adjacent topic context engineering platform.

**Tools:** Traqer

**Pitfall:** Assuming a win on your strongest topic will lift adjacent ones. Teams stop investing after the first topic breaks through and then find the adjacent topic never moved.

**Apply at Pabau:** Pabau should not assume visibility won for practice management software carries into aesthetic clinic EMR or patient booking. Budget content and outreach per topic and expect each to need its own set of articles and third-party citations.

**Apply anywhere:** Do not assume visibility won on your strongest topic carries into adjacent ones. Budget content and outreach separately per topic and expect each to need its own articles and third-party citations.

### 2. Treat GEO as bottom-funnel ranking, not a separate AI tactic list  `181.5`
*core · content insights · source 181*

Grow and Convert's position is that GEO needs no separate strategy. Their reasoning is mechanical: LLMs like ChatGPT and Perplexity search Google when a user asks for a product recommendation, so what the model reads is what ranks. They built what they call a Prioritized GEO framework around ranking for bottom-of-funnel keywords, and claim one strategy then delivers both organic conversions from Google and recommendations inside AI search, without chasing random AI tactics. This lines up with the base's existing doctrine that GEO is mostly classic SEO and that on-site schema tweaks barely move anything, but it adds a sharper selection rule: the keywords worth ranking for GEO are the same commercial ones a buyer would type, because those are the queries that trigger a recommendation fan-out in the first place.

> "LLMs like ChatGPT and Perplexity search Google when users ask for product recommendations"

**Evidence:** Grow and Convert built their Prioritized GEO framework on bottom-funnel keyword rankings and claim it delivers both Google conversions and AI recommendations from one strategy.

**How to do it**

1. List the product-recommendation prompts a buyer would actually type into ChatGPT, such as 'best software for X' and 'alternatives to Y'.
2. Run each prompt and record which URLs get cited, then check where those URLs rank in Google for the matching query.
3. Prioritize the bottom-funnel keywords whose SERPs feed those citations, rather than building separate AI-only assets.
4. Rank-stack: get your own page onto page one for those queries, and get listed on the third-party comparison pages already being cited.
5. Skip the low-yield on-site work (schema-only changes, llms.txt) until the ranking work is done.
6. Re-run the prompt basket monthly and track citation share by topic, not by a single prompt check.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Running a separate AI-visibility workstream with its own tactics duplicates spend for little gain. If your GEO plan contains no ranking work, it is not a plan.

**Apply at Pabau:** David should keep Pabau's AI-visibility work inside the normal SEO plan: rank the comparison and category pages, and get Pabau listed on the third-party practice-management roundups that ChatGPT cites, rather than building AI-specific pages.

**Apply anywhere:** Treat AI visibility as a byproduct of ranking for commercial queries: rank your own comparison pages and get listed on the third-party roundups models already cite, instead of running a separate AI tactic list.

### 3. Treat GEO as less predictable than SEO and plan around three unknowns  `78.8`
*core · content insights · source 78*

Grow and Convert open with the conclusion of a year of AI search work: GEO is far less predictable than SEO. SEO is a closed loop, where you pick a keyword, publish, build links and can see exactly where you stand. AI search has uncertainty at three points. You do not know the prompts, because users have long unique conversations rather than short repeatable keywords. You cannot reproduce the context, because user history and memory personalize the answer. And you cannot rely on repeatability, because the same user asking the same prompt gets different responses and citations each time. Their resolution is the one fact that stays fixed: LLMs still run on content. So the strategy shifts from tracking positions to covering topics.

> "GEO is far less predictable than SEO"

**Evidence:** Grow and Convert state this as the clear conclusion of a year of AI search client work.

**Pitfall:** Running GEO with an SEO reporting model, expecting a rank-equivalent number that moves reliably. Teams that do this either declare victory on noise or kill a working program after a bad week.

**Apply at Pabau:** David should set expectations internally that Pabau's AI visibility reporting is directional and topic-level. Do not promise a position number for a prompt the way a keyword rank is promised.

**Apply anywhere:** Accept that AI search cannot be tracked like keyword rank: prompts are unknown, context is personalized and responses are not repeatable. Plan around topic coverage and report directionally rather than chasing a per-prompt position.

### 4. Treat GEO as unpredictable by design, not as SEO with new keywords  `87.11`
*core · general insights · source 87*

Grow and Convert argue the SEO mental model, write a quality article for keyword X, get on-page right, build links, rank for X, does not transfer to LLM answers. They stack the sources of variance: SparkToro's research showing different users entering the identical prompt get different brand lists in different orders; users phrasing the same question in wildly different ways; the model folding in deeply personal context per user; different fan-out queries generated for the same prompt on different runs; the model sometimes not searching at all; the weight given to search versus training data varying run to run; and model capability differing between free and paid accounts. All of that variance governs only about 40% of cited sources. Their conclusion is that a strategy built on ranking for specific queries to win citations is impractical and will be ineffective.

> "LLM answers are way too unpredictable"

**Evidence:** SparkToro found brand recommendations from LLMs are wildly inconsistent in both membership and order for the same prompt.

**Pitfall:** Selling GEO as a deterministic service with per-prompt deliverables. The variance sources compound and the results will not hold up.

**Apply at Pabau:** Pabau should not commission articles aimed at named ChatGPT prompts. Commission topic coverage and measure citation share across a basket over quarters.

**Apply anywhere:** Do not commission content aimed at named AI prompts. Commission topic coverage and measure citation share across a prompt basket over quarters.

### 5. Treat grounding as the whole mechanism, so AI visibility is downstream of rankings  `81.13`
*core · general insights · source 81*

Grow and Convert state their strategy rests on one reality: all major LLMs search the web to formulate responses, a process called grounding. Google AI Overviews is literally an SEO summarizer, an overview of the results below it, so it is directly influenced by traditional rankings. OpenAI says ChatGPT searches the web whenever it determines a user could benefit from web information, not only when the search button is clicked, and in practice it almost always shows 'Searching the web' for product recommendation prompts. Perplexity lists sources that typically correlate with articles ranking on Google's first page. Their conclusion is that on-site tactics like llms.txt files, key takeaways blocks and 300-word posts have no hard data behind them, while ranking does.

> "all major LLMs search the web to help formulate responses"

**Evidence:** Grow and Convert base this on data from 20+ clients and show ChatGPT, Perplexity and Google AI Overviews all searching the web for recommendation queries.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Spending the GEO budget on on-site formatting tweaks. Grow and Convert say they see no hard data that llms.txt, key takeaways or short posts move AI visibility, while ranking demonstrably does.

**Apply at Pabau:** Pabau should treat AI visibility work as ranking work for bottom-of-funnel terms first, and rank any llms.txt or markup project below that in priority until there is evidence it moves mentions.

**Apply anywhere:** Assume AI answers are grounded in live web results and that rankings therefore decide most of your AI visibility. Fund ranking work for buying-intent queries before on-site formatting tweaks aimed at LLMs.

### 6. Treat third-party mentions on G2, Reddit and roundups as a promotion channel  `107.13`
*core · concrete actions · source 107*

Grow and Convert add a newer promotion layer to social, paid and links: third-party brand mentions for LLM visibility. When ChatGPT, Perplexity, Gemini or Claude generate a recommendation for a B2B product, they pull from sources indexed and cited in training and live retrieval. The categories they name are industry publications, listicles, comparison roundups, and third-party reviews on G2, Capterra and Reddit. They call getting mentioned in those sources one of the highest-leverage promotion activities available now, because a single mention in a frequently cited source can drive recommendations across millions of queries. This reframes promotion work from driving clicks to placing your name where models retrieve. They track the resulting mentions weekly with their own tool, Traqer.ai, across ChatGPT, Perplexity and Google AI Overviews.

> "one of the highest-leverage promotion activities you can do"

**Evidence:** Grow and Convert monitor client mentions weekly across ChatGPT, Perplexity and Google AI Overviews with Traqer.ai.

**How to do it**

1. Ask the models the ten buying prompts your prospects would use and record every source they cite.
2. Build a target list from those cited sources rather than from a generic outreach database.
3. Prioritize the comparison roundups and best-of listicles that appear repeatedly across prompts.
4. Get your product listed and reviewed on G2 and Capterra, and keep the category and feature tags accurate.
5. Pitch the industry publications on that list for inclusion in their existing roundups, not for new guest posts.
6. Participate in the relevant subreddits with genuine answers rather than promotional posts, since Reddit is a named retrieval source.
7. Re-run the prompt set weekly and track whether your brand appears, using a mention monitor.

**Tools:** Traqer.ai, ChatGPT, Perplexity, G2, Capterra, Reddit

**Pitfall:** Chasing generic link placements instead of the specific sources the models actually cite means the outreach never reaches the retrieval set that decides recommendations.

**Apply at Pabau:** Pabau should map which sources ChatGPT and Perplexity cite when asked for practice management software for clinics, then prioritize inclusion in those specific roundups and keep the G2 and Capterra listings current. That work sits alongside, not inside, the blog calendar.

**Apply anywhere:** Find the sources LLMs actually cite for your buying prompts, then work to be mentioned in those specific roundups, review platforms and communities, and monitor the mentions weekly.

### 7. Triage every fan-out sub-query before adding a heading for it  `180.1`
*core · concrete actions · source 180*

Grow and Convert warn that agencies now run a superficial version of query fan-out. They pull sub-queries out of an LLM optimization tool, then bolt a heading or an FAQ block onto an existing article for each one. Grow and Convert say the missing step is intent triage. For each sub-query you have to decide whether it warrants its own article, whether it can be integrated naturally into an existing page, whether it needs one new section, or whether it needs comprehensive coverage across several pages. Their example is that 'best project management software' fans out into 'project management for remote teams', 'PM software integrations' and 'project management pricing'. Skipping the decision produces thin, fragmented content stuffed where it does not belong, which helps nobody and does not perform in AI search.

> "simply add headings or FAQ sections for each one"

**Evidence:** Grow and Convert say they have started seeing agencies take this superficial approach after working with clients who came from those agencies.

**How to do it**

1. Pull the fan-out sub-queries for your target term from an LLM optimization tool or from AI Mode itself.
2. For each sub-query, run the actual search and read the intent: is the answer a definition, a comparison, a price, or a use case?
3. Mark it 'own article' if the SERP for it is dominated by dedicated pages rather than sections inside broader guides.
4. Mark it 'integrate' if your existing article already covers the ground and only needs the phrasing and an explicit answer.
5. Mark it 'one new section' only when the sub-query is a genuine sub-topic of the parent page's intent.
6. Drop any sub-query that is a different intent entirely rather than forcing it into the parent article.
7. Write the integrated ones as real prose that continues the argument, not as an appended FAQ list.
8. Re-check the parent article after the edits: if it now reads as a list of disconnected headings, you over-integrated.

**Pitfall:** Adding an FAQ block per sub-query. It looks like coverage in an audit tool but produces fragmented content that neither users nor AI engines reward, and it dilutes the parent page's intent match.

**Apply at Pabau:** When David runs fan-out research inside /SEO for a Pabau article, add a triage column to the sub-query list. Sub-queries like 'aesthetic clinic software pricing' deserve their own page; 'how does it handle consent forms' belongs inside the existing article as prose.

**Apply anywhere:** Before you act on a fan-out sub-query list, decide per query whether it needs its own page, a paragraph inside an existing one, or nothing. Appending an FAQ heading for every sub-query creates thin, fragmented pages.

### 8. Turn one case study into many force-indexed content pieces  `26.2`
*core · concrete actions · source 26*

Dooley's team runs a specific amplification flywheel: take one strong case study or review, publish it as a guest post, write a social post about that guest post, then submit each resulting URL to a rapid/force-indexing tool so Google and Bing crawl it fast — he says indexing a URL this way costs 'less than a penny.' Each indexed piece can then be turned into another new piece of content (a press release mention, a second social post, a PDF), repeating the loop so one proof point compounds into dozens of independently indexed, citable URLs. He calls skipping the indexing step 'criminal' because most marketers post daily on LinkedIn/Twitter but never force-index those URLs, so the content sits uncrawled and never reaches Bing, Google, or the LLMs that scrape indexed search results.

> "for less than a penny you can index that actual URL"

**How to do it**

1. Produce one strong proof asset: a customer case study, testimonial, or review.
2. Publish it as a guest post on a relevant third-party site.
3. Write a short social post (LinkedIn, X/Twitter, Facebook) that references or summarizes the guest post, linking back to it.
4. Publish the social post, then copy its URL.
5. Submit both the guest-post URL and the social-post URL to a rapid-indexing tool (e.g., Indexical) for force-indexing — budget under a penny per URL submitted.
6. Confirm each URL is indexed by searching a site: query for the exact URL in Google, or by checking the indexer's own confirmation dashboard. (inferred)
7. Once indexed, repurpose the same proof point into a new piece (press release line, LinkedIn Pulse article, PDF one-pager) and repeat the publish-and-index steps.
8. Track over 4-8 weeks whether ChatGPT, Gemini, Claude, or Google AI Overviews start citing the case study or brand claim when asked about the topic. (inferred)

**Tools:** Indexical, Google, Bing, ChatGPT, Gemini, Claude

**Pitfall:** Publishing daily on LinkedIn or Twitter without ever force-indexing those URLs means the posts are never crawled — Dooley calls this 'criminal' because it's the single cheap step (under a penny per URL) that lets Bing, Google, and the LLMs actually discover and cite the content.

### 9. Understand why the two SEO hacks that work on Google do not work on ChatGPT  `89.5`
*core · general insights · source 89*

Grow and Convert lay out why Google is easier to force your way into. Google links to other people's pages and weights them heavily by backlinks, so two hacks are available: pay a site already ranking on page one to list you, which is exactly what G2 and Capterra placements are, or do standard SEO on your own page and slip your product into it. They say plainly that they have ranked many clients on page one for terms like 'best CRM' who were nowhere near market leaders. Neither hack transfers. ChatGPT writes the answer itself rather than linking, so there is no page of yours it can send people to and no page you can stuff. And its model has no obvious controllable input equivalent to a backlink. You have to actually be written about.

> "you can hack your way onto Google's first page in two notable ways"

**Evidence:** Grow and Convert state they have ranked non-market-leader clients on page one for 'best CRM' and 'accounting software' through SEO alone, and that ChatGPT returned only 7 to 8 tools where Google page one listed over 100.

**Tools:** G2, Capterra

**Pitfall:** Assuming a paid G2 or Capterra placement buys AI visibility the way it buys Google page-one presence. It buys one mention on one site, which is a single data point in a training corpus.

**Apply at Pabau:** Pabau's paid directory spend should be judged on the referral leads it produces, not on AI visibility. The AI-visibility budget belongs in earning genuine editorial mentions across aesthetic-industry publications.

**Apply anywhere:** Judge paid directory spend on the referral leads it produces, not on AI visibility. Put the AI-visibility budget into earning genuine editorial mentions across your industry's publications.

### 10. Use Google AI Mode to reverse-engineer winning attribute combinations  `25.5`
*core · ai workflows · source 25*

Koray's method for winning AI Overviews/AI Mode results for commercial queries: first query Google AI Mode with a prompt like 'what are the most important attributes for a [target service, e.g., personal injury lawyer]' to get a list of roughly 80 candidate attributes AI Mode considers relevant. Then test attribute combinations directly, e.g., 'give me the best personal injury lawyers in Houston according to these three attributes,' cycling through different three-attribute combinations to see which brands surface for each one — this reveals which specific attribute clusters AI models associate with which competitors. He then builds an 'external topical map': a coordinated set of semantically-optimized content published across multiple different domains (not just his own site) designed to repeatedly associate his brand with the winning attribute combinations, so AI models and LLMs start treating that brand as a top answer for that specific attribute set.

> "what are the most important attributes for a personal injury lawyer"

**How to do it**

1. Open Google AI Mode and enter a prompt naming your exact service or category, e.g., 'what are the most important attributes for a [your service category].'
2. Record the full list of attributes returned (Koray reports getting around 80 for 'personal injury lawyer').
3. Pick combinations of three attributes at a time from that returned list.
4. Query AI Mode again with a comparison prompt naming your target geography/category and the three chosen attributes, e.g., 'give me the best [service] in [city] according to [attribute 1], [attribute 2], [attribute 3].'
5. Record which brands/competitors appear for each attribute-combination query, noting which combinations your brand does not yet appear for.
6. Track every combination tested and its result in a spreadsheet so you can systematically map the full space of attribute clusters and current winners (inferred).
7. For attribute combinations where your brand is absent, publish new semantically-optimized content that explicitly addresses that exact combination of attributes.
8. Distribute this content across multiple domains you control or can publish on, not only your primary site, to build the 'external topical map.'
9. Re-run the same AI Mode queries after publishing (e.g., after 4-8 weeks) to check whether your brand now appears for the target attribute combinations (inferred verification step).

**Tools:** Google AI Mode

**Prompt / template:**

```text
what are the most important attributes for a personal injury lawyer / Give me the best personal injury lawyers in Houston according to these three attributes
```

**Pitfall:** Testing only one attribute combination and concluding your brand 'doesn't do well in AI results' — results change every time the combination of attributes changes, so a single test isn't representative; the map only becomes useful once many combinations have been tested systematically.

### 11. Use cheap monthly press releases to seed AI citations  `33.8`
*core · concrete actions · source 33*

The guest treats press releases as an AI/LLM-citation play rather than a backlink or traffic play: cheap distribution through a service like AB Newswire (a $500/year package advertised around $6/release, roughly 83 releases/year) reliably shows up influencing AI Overviews and ChatGPT answers, even though the underlying pages rarely deliver lasting backlink/ranking value and tend to die out for organic purposes after 6-8 months. The recommended cadence is monthly, non-duplicate releases sustained for at least 6-8 months to build a narrative arc (e.g. month 1: business launch, month 2: new service area, month 3: new tool, month 4: multilingual site update). A concrete example given: a subject built his release's H1 and site title around the exact phrase "LLM SEO expert," distributed it via GlobeNewswire, then built backlinks to that release from his own articles about SEO for LLMs — and it still surfaces for that phrase and its variants months later.

> "these ones literally influence AI Overviews and ChatGPT"

**How to do it**

1. Sign up for a low-cost press release distribution service — the source names AB Newswire specifically ($500/year, ~$6/release, ~83 releases/year), with GlobeNewswire or PRLog.org as pricier alternatives.
2. Treat this channel as an AI/LLM-citation tactic, not a backlink or traffic tactic, since cheap releases typically stop delivering ranking value after 6-8 months.
3. Publish on a monthly, non-duplicate cadence for at least 6-8 months, building a narrative arc about the brand rather than repeating the same announcement.
4. If targeting a specific entity/phrase for AI visibility, put that exact phrase in the release's H1 and page title.
5. Build backlinks from your own topically-relevant articles into the press release page itself to extend how long it stays live/indexed.
6. Periodically check whether your releases are surfacing in AI Overviews or an LLM answer for your target phrases to confirm the tactic is working. (inferred verification step)

**Tools:** AB Newswire, GlobeNewswire, PRLog.org

**Pitfall:** Expecting cheap press releases to deliver long-term backlink or ranking value — the source is explicit that the real value is AI/LLM citation, and the underlying pages typically stop delivering ranking value within 6-8 months regardless of cost.

### 12. Use the Ayima extension to see the searches ChatGPT actually runs  `60.5`
*core · concrete actions · source 60*

The single most practical tool tip in the episode. Joe describes a Chrome extension by Ayima: type a prompt into ChatGPT, click the extension, and it shows you under the hood what searches ChatGPT is making on Google or Bing and what sources it's using. His worked example: type 'best CRM' and the extension reveals it is searching 'best CRM reviews', 'best CRM comparisons', 'best CRM 2025'. That directly informs the titles FATJOE commissions - they use exactly those keyword combinations ('the best five CRM platforms reviewed', 'best CRM platforms 2025') because those are the combinations ChatGPT is actually using to search. It converts AI visibility from guesswork into a keyword list.

> "there's an extension called"

**How to do it**

1. Install the Ayima Chrome extension.
2. Enter the head prompt your buyers would actually type into ChatGPT.
3. Open the extension and record every underlying search query it shows, plus the sources returned.
4. Repeat for each of your priority prompts and build a keyword list from the underlying queries, not the prompts.
5. Use those exact keyword combinations as the titles of the content you commission or publish.
6. Cross-reference the source URLs it returns with your citation target list.
7. Re-run periodically, since the query patterns change as the models change.

**Tools:** ChatGPT, Ayima extension

**Pitfall:** The underlying queries are model- and moment-specific - a keyword list built from one run will drift, so treat it as a snapshot rather than a permanent target list.

**Apply at Pabau:** Running Pabau's core prompts through this extension would produce the actual query list the engines use - almost certainly review, comparison and year-qualified variants - which is a far better content brief than guessing at prompt wording.

**Apply anywhere:** Running your core prompts through this extension produces the actual query list the engines use - almost certainly review, comparison and year-qualified variants - which is a far better content brief than guessing at prompt wording.

### 13. Visual semantics: concentrate target keywords inside one large UI element  `25.4`
*core · concrete actions · source 25*

Koray's 'visual semantics' technique, demonstrated on his Audioread.com case study (a single-page site that grew from 5 to 8,000 clicks/day in 8 months and now outranks ElevenLabs, Vio, and Cielo for transcription queries), is to place the single most important interactive element as a large, prominent component in the above-the-fold 'centerpiece annotation' area, and load the key n-grams you want to rank for (e.g., 'voice to text,' 'MP3 to text') as text inside or around that large element rather than in headings or body copy. His stated mechanism: a bigger HTML/engagement element makes any text inside it carry disproportionately more relevance weight than the same text in a small element or a heading, so he deliberately skips building a separate page or heading for each keyword variation (unlike ElevenLabs, which builds a dedicated page per file format) and still outranks them by concentrating relevance into one large visual element. He also designs for 'agentic retrieval reasoning' by removing distracting elements (e.g., a login button) so an AI agent crawling the page immediately infers core facts like 'free to sign up, free to use' from the layout alone.

> "even a small amount of text within that element becomes way heavier"

**How to do it**

1. Identify the single highest-value action/keyword-entity combination your page should own (e.g., a specific tool function or an 'X-to-Y' conversion query).
2. Design the above-the-fold area around one large, visually dominant interactive element (button, upload field, calculator) tied to that action, not a generic hero image or headline.
3. Place your target n-grams/entities as the literal label, placeholder, or immediately adjacent copy on that large element rather than burying them in a heading or paragraph further down the page.
4. Remove or de-emphasize competing UI elements that could confuse an AI agent's read of the page's purpose (Koray removed a login button so agents infer 'free to use').
5. Avoid creating a separate dedicated page or heading for every keyword variation you target; let one large visual element carry relevance for several related query variations at once.
6. Test the page by running an AI agent (e.g., via Claude Code) against the URL and asking it to state what actions/functions the page enables, confirming the intended n-grams and function are being picked up (inferred).
7. Monitor Google Search Console query-level clicks/impressions for the target 'X-to-Y' style variations over the following weeks to confirm relevance is being credited to the page (inferred verification step).

**Tools:** Google Search Console, Claude Code

**Pitfall:** Assuming more text or more dedicated headings always helps relevance — Koray deliberately keeps text minimal and skips per-variation dedicated pages/headings that competitors like ElevenLabs build, because adding words dilutes the importance of each one on the page.

### 14. Web search is the only lever you can pull  `12.3`
*core · general insights · source 12*

Devesh simplifies LLM knowledge into exactly two input sources: their 'training data,' which he calls parametric memory, the baked-in model of the world formed during training and periodic retraining, and live web search performed during a conversation. Getting baked into training data so a brand is automatically associated with its product category, the way ChatGPT will reflexively mention Salesforce for any CRM question asked with web search off, would be the ideal outcome, but he stresses this is a black box: vendors don't disclose retraining frequency or inclusion criteria, and the process is already entangled in copyright lawsuits over what training data was scraped. Since training-data inclusion isn't something a marketing team can directly engineer, and is really just the eventual payoff of long-term brand building, he concludes that live web search is 'the major lever' marketers can actually pull today.

> "it leaves web search as the major lever"

**Evidence:** Devesh's Salesforce example: asked for CRM recommendations with web search switched off, an LLM will mention Salesforce with near-certainty purely from training-data saturation, which he calls the ideal but unattainable outcome since vendors don't disclose retraining frequency, inclusion criteria, or how they handle the copyright lawsuits over scraped training data.

**Apply at Pabau:** Stop looking for a way to directly edit an LLM's training data - it's opaque and not purchasable or engineerable by a marketing team; the only lever Pabau's SEO/content team can pull today is winning the live web-search results an LLM triggers mid-conversation, which puts GEO strategy back onto ranking real content on the open web, the same mechanism as traditional SEO.

**Apply anywhere:** Stop looking for a way to directly edit an LLM's training data - it's opaque and not purchasable or engineerable by a marketing team; the only lever your SEO/content team can pull today is winning the live web-search results an LLM triggers mid-conversation, which puts GEO strategy back onto ranking real content on the open web, the same mechanism as traditional SEO.

### 15. Weight the first three SERP pages when chasing AI citations  `87.3`
*core · content insights · source 87*

Of the cited sources that did appear in Google's results for the fan-out queries, Grow and Convert found page one alone accounted for a third of all matches, and the top three pages held roughly 66%, with a sharp decline after that. They went ten pages deep; ChatGPT mostly does not. This gives a usable threshold: a page sitting past Google position 30 for the relevant fan-out query is contributing very little citation probability from live retrieval. It also confirms, in their words, what SEOs had hoped, that ranking higher improves the chance of citation. The lever is ordinary ranking work on pages already in striking distance, not new pages aimed at queries you cannot verify.

> "page 1 alone accounted for a third of all matches"

**Evidence:** Page 1 held a third of matches; pages 1-3 held ~66%.

**How to do it**

1. List the pages you want cited and their current Google positions for the closest commercial query.
2. Split them into positions 1-10, 11-30, and past 30.
3. Put refresh and internal-link effort into the 11-30 group first, since that is the band that crosses into the top three pages.
4. Treat pages past position 30 as contributing near-zero live-retrieval citation probability.
5. Re-check citation rate after positions move, not before.
6. Do not create new pages for fan-out queries while existing pages sit outside the top three pages.

**Tools:** Google Search Console

**Pitfall:** Assuming deep-ranking pages still get sampled. Beyond page three the match rate falls off hard, so effort spent on a position-60 page returns almost nothing in citations.

**Apply at Pabau:** Pull Pabau pages ranking 11-30 for aesthetic practice-management queries out of GSC and refresh those first. They are the ones that can cross into the band that actually feeds ChatGPT.

**Apply anywhere:** Pull the pages ranking 11-30 for your commercial queries and refresh those first. That band is what crosses into the top three SERP pages, where two thirds of AI citation matches sit.

### 16. Who should invest in AI search now, and who genuinely shouldn't  `60.2`
*core · best practices · source 60*

Joe gives an unusually direct answer on scope. The companies that should invest now are the ones with subjective buyers - anything where the product isn't a commodity and someone has to actually research it: does it have this feature, does it have that feature. Some e-commerce qualifies, using his laptop-processor example. The companies that shouldn't yet: anything commodity ('brown leather shoes'), where he says if you have good SEO you don't need to worry about AI because you'll get recommended anyway - 'SEO and AI kind of look like the same thing when you zoom out'. And the group he sees no path for at all is the content business - the old affiliate operators and people running ads on content: they might get sourced, but he doesn't think it's a good play for them. His long answer short: anyone in a commercial business should be looking at AI from now. Cody's agreement extends the affiliate point - if it's general knowledge without deep expertise, people will just ask Perplexity Labs and have a voice conversation with the result. The one affiliate model Cody thinks survives is aggregating data nobody else has: his example is a friend scraping Google Maps review data for parks to build a database of which have shade or benches, which an LLM isn't going out and doing.

> "companies that have got some more subjective buyers"

**How to do it**

1. Classify your product: is the purchase subjective and feature-comparison driven, or commodity?
2. If subjective, start now; if commodity, keep investing in conventional SEO, which he says carries you anyway.
3. If your business is content monetised by ads or affiliate commissions, don't expect AI visibility to replace the traffic.
4. If you are in content, look for a data asset an LLM can't assemble itself - aggregated, scraped, structured, proprietary.
5. Re-evaluate as the surfaces mature; he thinks every commercial business gets there eventually.

**Pitfall:** The advice 'if you've got good SEO you don't have to worry about AI' is specific to commodity products - for subjective, comparison-driven categories both hosts treat it as urgent.

**Apply at Pabau:** Pabau sits squarely in the invest-now category - a feature-comparison purchase with a long research cycle - which is the case Joe says benefits most from this work.

**Apply anywhere:** Feature-comparison purchases with long research cycles are the case Joe says benefits most from this work; commodity purchases can wait and content-only businesses shouldn't expect it to replace their traffic.

### 17. Write bottom-of-funnel product content, not top-of-funnel guides  `12.5`
*core · concrete actions · source 12*

Devesh's central content-strategy claim is that only product-related conversation queries or topics between a user and an LLM get brand mentions, meaning classic top-of-funnel informational content such as 'ultimate guide to X' essentially never triggers a brand mention, no matter how well it ranks in traditional Google, because an LLM only searches the web and cites brands once the conversation has moved to an explicitly product- or vendor-seeking stage. His example: if a prospective client asks ChatGPT how to get started with content marketing, it answers directly without mentioning any agency, because the person hasn't asked about agencies yet; only once the conversation shifts to something like needing to delegate does a brand-recommending response with a live web search get triggered. He demonstrates the same pattern with a tennis-racket example, where asking how to improve a swing gets answered directly with no search, but asking afterward for a new racket triggers a live web search and product recommendations, and he notes this pattern holds for both B2C and B2B, product and service queries alike.

> "Only product-related conversation queries or topics between user and LLM"

**How to do it**

1. Audit your existing content library and classify every piece as either top-of-funnel/informational (e.g. 'ultimate guide to X') or bottom-of-funnel/product-related (content that directly addresses which product or vendor to use for a specific situation).
2. Stop prioritizing new top-of-funnel informational content specifically for GEO purposes - keep it for traditional Google SEO if it already performs there, but don't expect it to earn LLM brand mentions.
3. For every core product, feature, and use case, write dedicated bottom-of-funnel content that explicitly answers which vendor or tool to use for that specific situation, matching the phrasing a buyer would use once past the informational stage.
4. Test your own content's bottom-of-funnel coverage by asking an LLM the informational version of a question, then following up in the same conversation with the product-seeking version, and checking whether your brand surfaces once web search triggers.
5. Prioritize content production budget toward filling gaps in bottom-of-funnel coverage over adding more top-of-funnel informational pieces, since only the former category is eligible for LLM brand mentions per this framework.

**Pitfall:** Don't assume an extensive library of high-ranking top-of-funnel informational content is contributing to GEO/AI visibility just because it performs well in traditional Google - this content type essentially never gets cited in the product-recommendation stage of an LLM conversation, regardless of how well it ranks.

### 18. Write for the refined follow-up turn, not the opening broad query  `80.3`
*core · best practices · source 80*

Grow and Convert describe how an AI conversation actually unfolds. Someone opens with 'what is the best SaaS content marketing agency', gets a list, then refines by adding who they are, their company size, budget, what they have already tried, and asks for the best fit given all of it. In Google that context existed in the user's head but was never typed, so the searcher had to click in and out of results scanning for a page that understood them. In an LLM the context is stated, so the model can filter on it. The practical consequence is that the winning page is not the one optimized for the opening query but the one containing the detail that survives the second and third turn of the conversation.

> "But with AI search, people do give it their context"

**Evidence:** Grow and Convert walk through a ChatGPT conversation that starts at 'What is the best SaaS marketing agency?' and ends recommending a specific niche agency after the user adds startup context.

**How to do it**

1. Take your main category query and write out three realistic follow-up turns a buyer would type, each adding a constraint like size, budget, industry or prior tooling.
2. For each constraint, check whether any published page of yours states your position on it in plain words.
3. Where nothing exists, add a section to the relevant page naming that constraint and your answer to it, using the buyer's phrasing.
4. Name the customer situation explicitly in the copy rather than implying it through benefits language.
5. Run the full conversation in ChatGPT and Perplexity and note at which turn you drop out of the answer.
6. Fix the page that should have covered the turn where you dropped out, then re-run the same conversation a week later.
7. Repeat for each distinct buyer segment, since the constraints differ per segment.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Optimizing only for the head query gets you into the first list and then dropped as soon as the user adds a constraint. The signal is being named in turn one of a test conversation and absent by turn three.

**Apply at Pabau:** Pabau pages should state the constraints a practice owner names out loud: single-room clinic versus multi-site, whether they need medical records, budget level, and what they are migrating from. Those sentences are what keeps Pabau in the answer after the follow-up turn.

**Apply anywhere:** Map the follow-up turns a buyer adds after the opening query, then make sure a published page states your answer to each constraint in the buyer's own words.

### 19. Write the product snippet yourself for every third-party mention  `82.7`
*core · best practices · source 82*

Grow and Convert name two mistakes in citation outreach, and the second is failing to control the narrative on other people's sites. Their strong advice is to write the product snippet yourself and be specific about your value propositions and differentiators, rather than letting an editor summarize you from your homepage. The reason is mechanical. Models read your brand across multiple sources, and if each source describes you differently, there is no consistent claim for them to repeat. If every source uses your wording, you have fed the model the exact positioning you want it to hand to a buyer. This turns outreach from a link request into a messaging distribution job, and it means the differentiator sheet you use for your own articles is the same asset you send out.

> "writing the product snippet yourself and being specific"

**Evidence:** Grow and Convert list uncontrolled narrative as one of two named citation-outreach mistakes, alongside pitching sites indiscriminately.

**How to do it**

1. Write one 60 to 90 word product snippet from your agreed differentiator sheet, stating who it is for and two contrasts with alternatives.
2. Write a shorter 25 word variant for listicle table cells and roundup entries.
3. Include both variants in every outreach email rather than offering to answer questions.
4. Supply the exact product name spelling, the category label you want to be filed under, and one figure.
5. Ask for the snippet to be used as written and offer a fact-check pass if the editor rewrites it.
6. Keep a log of every live third-party mention and the wording used.
7. Audit that log quarterly for drift, and email editors to correct any description that contradicts your positioning.
8. Reuse the same snippet on review-platform profiles so paid and earned sources agree.

**Pitfall:** Editors will paraphrase from your homepage if you do not supply copy, which produces generic wording that makes you sound like every other name in the list.

**Apply at Pabau:** Pabau should keep a standing approved snippet in the outreach template, using the guide-compliant wording, and check every live directory or roundup entry against it each quarter.

**Apply anywhere:** Supply a pre-written product snippet with every outreach request, in long and short variants, and audit live third-party descriptions quarterly for drift.

### 20. Write the sentences you want an LLM to repeat, because it copies your phrasing  `81.5`
*core · content insights · source 81*

Grow and Convert show a side-by-side where ChatGPT describes Constitution Lending in language nearly identical to a passage in the company's own blog post. Their framing is that AI effectively acts like a salesperson: it consumes your content when grounding and uses it to communicate your value props and differentiators to the user. That makes the phrasing itself an asset. A vague sentence gets paraphrased into generic category language, while a specific, self-contained claim survives into the answer largely intact. It also means the wording that appears in an answer can be steered, which is a different job from earning the citation in the first place.

> "using nearly identical language to what we published in our article"

**Evidence:** Grow and Convert publish the ChatGPT output next to the Constitution Lending blog passage it mirrors.

**How to do it**

1. Write down the exact sentence you want an LLM to say about you, in under 25 words.
2. Make it self-contained: name the brand, the differentiator and the qualifier, with no pronouns depending on earlier sentences.
3. Place that sentence early in the relevant page and repeat the same formulation on the other pages that cover the topic.
4. Attach a number or a specific mechanism so the claim is not interchangeable with a rival's.
5. Prompt ChatGPT, Perplexity and Google AI Overviews with the buying query and copy the exact wording each returns.
6. Diff the returned wording against your target sentence and note which words survived.
7. Rewrite the on-page sentence to close the gap, then re-test after the page is recrawled.
8. Keep a one-page list of approved formulations so every writer uses the same wording.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Varying the wording across pages for stylistic reasons. Inconsistent formulations give the model several candidate descriptions and it will settle on the blandest one.

**Apply at Pabau:** Pabau should fix a small set of canonical sentences about what it does and who it serves, and repeat them verbatim across blog, template and product pages rather than rewriting the positioning each time.

**Apply anywhere:** Decide the exact sentence you want AI answers to say about you, keep it self-contained and specific, and repeat that same formulation across every page on the topic. Models tend to reuse published phrasing rather than invent their own.

### 21. Write to beat one named competitor passage, since ranking is pairwise  `76.12`
*core · content insights · source 76*

The paper's retrieval description ends with a mechanism that changes how you edit. Each sub-query returns roughly 20 to 50 candidate passages, which are reranked by a cross-encoder that iteratively scores each passage against the original query until a complete ranking emerges, likely through a pairwise heapsort algorithm, citing Qin et al. from Google's patents and related research. The authors' conclusion is that this makes ranking inherently comparative rather than absolute. A passage is not judged on whether it is good; it is judged against a specific competitor passage in a head-to-head. That is why they say substance dominates stylistic variation in retrieval environments: a passage restating widely available information in slightly different language offers no marginal value in a comparison, while one carrying a verifiable data point, a named source or a concrete example offers something the other lacks. Practitioners call this information gain.

> "This makes ranking inherently comparative rather than absolute"

**Evidence:** The paper attributes the pairwise heapsort reranking description to Google's patents and Qin et al., with 20-50 candidate passages returned per sub-query.

**Pitfall:** Editing against a style guide instead of against a rival. A passage can be clean, on-brand and still lose every head-to-head because it adds no fact the competing passage does not already have.

**Apply at Pabau:** When Pabau refreshes a page, pull the passage an AI answer currently cites for that question and edit until Pabau's version carries a fact, figure or named source the cited one lacks.

**Apply anywhere:** When refreshing a page, pull the passage an AI answer currently cites for that question and edit until yours carries a fact, figure or named source the cited one lacks.
