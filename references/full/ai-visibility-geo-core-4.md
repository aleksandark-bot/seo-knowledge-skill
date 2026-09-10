# AI Visibility / GEO — core (part 4 of 6)

24 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Low-DR exact-match domains appear to earn more AI citations than high-DR ones  `67.10`
*core · content insights · source 67*

Asked whether exact-match domains still matter now that AI search is taking over, Dirk reports something he is careful to label unofficial. From his own tests and from practitioners he talks to, an exact-match domain with little to no DR is being picked up and cited by AI more than a much higher-DR domain is, provided the content is good, the structured data is in place and the on-page holds up. He repeats the caveat twice: nothing official, but it looks promising for now. He pairs it with a hard condition at the end of the interview, that without your own pages and proper structured data you will not be cited at all, whatever the domain says. This is a useful counterweight to the base's existing position that third-party authority scores are entertainment metrics: here the low score is not merely irrelevant, it appears to cost nothing.

> "more benefit that they're seeing from having an exact match with little to no DR"

**Evidence:** Dirk stresses twice that this is unofficial and drawn from his own tests and conversations with other practitioners, not from any Google or vendor statement.

**Pitfall:** Reading this as permission to launch a keyword domain with thin content. Dirk conditions the whole claim on good content, proper structured data and on-page parity, and says without your own pages and structured data you will not be cited at all.

**Apply at Pabau:** Pabau should not read a low DR on a niche microsite as a reason not to build it for AI visibility. What matters is structured data and genuinely owned content on the page, which is where the effort should go.

**Apply anywhere:** Do not dismiss a low-authority niche domain for AI visibility. Practitioner tests suggest an exact-match name with weak authority can be cited more often than a high-authority one, provided the page has real content and correct structured data.

### 2. Make every passage self-contained so chunking cannot orphan it  `76.1`
*core · best practices · source 76*

The AEO paper argues that because retrieval and ranking happen at the passage level, not the page level, a passage that opens with a back-reference breaks when it is chunked out of the document. It names the failure directly: a passage beginning with 'As mentioned above' or 'Building on the previous point' has introduced a dependency that may not survive chunking, and once retrieved in isolation it reads as incomplete or ambiguous, so the model deprioritizes it. The consequence the authors draw is uncomfortable for long-form writers: a well-structured document with a poorly structured passage still underperforms a less-structured document that contains a few strong self-contained paragraphs. Documents are chunked into semantically coherent segments of roughly 256 to 512 tokens, each independently embedded and indexed, so a long article does not compete as a whole. It competes as a series of independent passages.

> "has introduced a dependency which may not survive the chunking process"

**Evidence:** The paper states documents are chunked into segments of roughly 256-512 tokens, each independently embedded and indexed, so a long article 'competes as a series of independent passages'.

**How to do it**

1. Read each section of a draft alone, with the rest of the page hidden, and ask whether it still answers a question by itself.
2. Delete every opener that back-references: 'as mentioned above', 'building on the previous point', 'as we saw'.
3. Restate the entity name in the first sentence of each section instead of using a pronoun that points outside the chunk.
4. Keep each section near the 256 to 512 token chunk window so a natural chunk boundary falls on your section boundary.
5. Move any definition a section depends on into that section, even if it repeats a definition given earlier.
6. Re-read the weakest section last: one broken passage drags the page even when the rest is strong.

**Pitfall:** Writers optimize the document arc and leave individual sections dependent on earlier context. The signal is a section that reads as a non-sequitur when you paste it alone into a blank document.

**Apply at Pabau:** Pabau's long blog guides are the exposed asset here. Audit each H2 section on the biggest guides for back-referencing openers and rewrite the first sentence of each to name the entity and answer its own question.

**Apply anywhere:** Long guides are the exposed asset here. Audit each H2 section of your biggest guides for back-referencing openers and rewrite the first sentence of each to name the entity and answer its own question.

### 3. Map AI citations across 40 keywords and 10 LLMs  `08.18`
*core · ai workflows · source 08*

To find exactly which third-party sources drive a brand's AI visibility, an AI agent (Manus, generalizable to any agent-capable model) is run across roughly 40 target keywords against the top 10 LLM/AI answer surfaces, analyzing why the business does or doesn't appear in each response and compiling a report of which citations/directories are actually responsible for that visibility. That report is then used to prioritize which specific third-party directories need better rankings or links next. Uniquely, this can be interrogated conversationally — directly asking ChatGPT 'how did you come to this conclusion, what did you look at, why did you look at that' reliably returns its actual reasoning and sources, a transparency the source contrasts with the opacity of a traditional Google ranking algorithm.

> "find all the citations for every single one"

**How to do it**

1. Compile a list of roughly 30-50 target keywords/queries relevant to your brand's visibility, mixing brand-name and category/service queries.
2. Set up an AI agent capable of multi-model querying (the source uses Manus; equivalents include Claude with agent/computer-use tooling, or a custom script hitting multiple LLM APIs).
3. Run each keyword against each of the top LLM/AI answer engines you care about (e.g., ChatGPT, Google AI Overviews, Perplexity).
4. Instruct the agent to record, for each query/model combination, whether your business appears and which sources/citations the model used to decide that.
5. Have the agent compile a consolidated report ranking which third-party directories/sites are most frequently the source of your AI citations.
6. Manually sanity-check the report for noise, discarding any clearly irrelevant or random sites it surfaces.
7. Prioritize link-building and review-generation effort toward the directories the report identifies as most influential rather than treating all listed platforms equally.
8. Separately, spot-check specific answers by directly asking the AI system 'how did you come to this conclusion, what did you look at, why did you look at that' for a given query.
9. Feed any newly discovered high-influence directory back into your directory link-building workflow to reinforce it. (inferred closing-the-loop step)

**Tools:** Manus, ChatGPT

**Prompt / template:**

```text
how did you come to this conclusion, what did you look at, why did you look at that?
```

**Pitfall:** Treating every site an AI agent surfaces as equally important — the report will sometimes include 'random sites in the mix' that aren't actually meaningful, so output needs a manual sanity-check pass before acting on it.

### 4. Map a query's fan-out branches and cover every sub-question  `76.11`
*core · concrete actions · source 76*

The paper describes fan-out as the structural change that most enlarges the competitive space. Rather than executing a single lookup, answer engines decompose a query into multiple synthetic sub-queries representing different facets of user intent, citing King, and Google's patents show LLMs analyzing the query alongside initial grounding results to generate diverse reformulations. Its worked example: 'best running shoe' may trigger parallel retrieval around comfort, durability, price, injury prevention and review quality, with each sub-query initiating a separate retrieval event. The consequence the authors stress is that brands now compete across a distributed set of latent sub-questions, many of which are never directly visible to the marketer, and a brand that ranks well for one sub-query but poorly on another may not be seen by the LLM at all. Partial coverage is not partial credit.

> "decompose a query into multiple synthetic sub-queries"

**Evidence:** King is cited for fan-out; the paper reports each sub-query returns roughly 20-50 candidate passages, so each branch is a separate competition.

**How to do it**

1. Take a target buying question and list the attribute facets an engine would split it into, using price, durability, comfort, risk and review quality as the pattern.
2. Add the facets specific to your category that a generalist list would miss.
3. Check which facets you already have a dedicated passage for and which you have none.
4. Write a passage per uncovered facet rather than one section that gestures at all of them.
5. Run the original query through several engines and read which facets the answer actually addresses, then compare with your list.
6. Prioritize the facets where the answer currently cites a competitor and you are absent, since one missing branch can drop you from the whole answer.

**Pitfall:** Assuming strong coverage of the main query carries the sub-queries. The paper is explicit that ranking well for one sub-query while doing poorly on another can mean the LLM never sees you.

**Apply at Pabau:** For queries like choosing clinic software, Pabau should hold a dedicated passage for each facet a clinic owner weighs: pricing, onboarding, compliance, hardware, integrations and support, rather than one overview section.

**Apply anywhere:** For a buying query, hold a dedicated passage for each facet the buyer weighs rather than one overview section that touches all of them.

### 5. Never build a dedicated article to win one narrow tracked prompt  `83.8`
*core · best practices · source 83*

Grow and Convert flag this as the specific failure mode of prompt-level dashboards. Trying to game the system and show up for a single very specific prompt does not make sense, because nobody is going to ask that exact prompt. Producing a dedicated article for one narrow prompt and then showing up for it will look good inside AI visibility tracking software, so a client or management team may be pleased. But if no real person has that exact exchange with an LLM, the page does nothing in a real scenario. The distortion is a reporting artifact: the dashboard rewards a metric that has a real-world frequency of roughly zero. Judge a proposed page by whether it covers a situation, not by whether it wins a tracked string.

> "trying to game the system and show up for a single really specific prompt"

**Evidence:** Grow and Convert say a dedicated article for one narrow prompt may look good in tracking software and please management while nobody actually has that exchange.

**How to do it**

1. Require every content brief to name the specific customer situation the page serves.
2. Reject any brief whose only justification is a missing row in an AI visibility tool.
3. Check the proposed prompt against your collected customer chats before approving the page.
4. Cap narrow single-prompt pages at zero and fold that material into a broader situation page instead.
5. Report topic-basket presence to stakeholders rather than individual prompt wins.
6. Audit existing pages for ones built only to satisfy a tracked prompt and merge them into fuller pages.
7. Re-measure the topic basket after merging to confirm coverage did not drop.

**Pitfall:** The dashboard turns green while pipeline does not move, and the team keeps commissioning narrower pages because the reported metric keeps improving.

**Apply at Pabau:** Pabau should not commission a blog post because a tracking tool shows a missing prompt. Ask instead whether the page covers a real practice situation, and reject the brief if the only justification is the dashboard row.

**Apply anywhere:** Do not commission a page because a tracking tool shows a missing prompt. Require that the page cover a real customer situation, and reject briefs whose only justification is filling a dashboard row.

### 6. No agency has cracked AI ranking consistently - and the tools are just rank trackers  `59.12`
*core · content insights · source 59*

Jackie's warning is the most useful counterweight in the episode. He says be careful with agencies claiming they know how to rank in AI: 'if I figure out a way to rank on AI, I'ma monetize the hell out of it. If your boy has been sitting on his hands and has not claimed a way to rank successfully across all these LLMs, then most people probably haven't figured it out consistently.' What he does see: results pulling from popular subreddits, and Google AI Overviews pulling from press releases - but not a reliable if-you-do-X-then-Y. His best one-line summary of what does work is brand mentions, specifically getting press releases done that are structured as listicles ('best Vancouver SEO company') with you at the top, which he finds gets picked up in AI Overviews; being number one in the biggest SEO subreddit gets you into ChatGPT; Perplexity he hasn't cracked. He did a case study on a physio clinic in Vancouver and could get the press release cited for some queries like 'best physio Vancouver 2025', but not consistently. Cody's complementary observation is that every AI-visibility tool he interrogates turns out to be a visibility tracker built on synthetic data - 'literally just a rank tracker' - not something that influences rankings. And their shared conclusion on what actually matters: are you on pages one through three for that keyword, included in some of those listicle articles. Cody says he does not see PBN-style approaches work for this at all.

> "careful with the agencies out there claiming"

**How to do it**

1. When evaluating an AI visibility vendor, ask directly whether they influence rankings or only measure them - Cody says they all eventually admit it's measurement.
2. Ask for a consistent, repeatable method across multiple LLMs; inconsistency across engines is the norm, not a failure of your account.
3. Focus effort where both agree it works: getting your brand into the listicle-style articles that rank on pages one through three.
4. Use press releases structured as listicles with your brand at the top, which Jackie finds gets picked up in Google AI Overviews.
5. For ChatGPT specifically, target visibility in the largest relevant subreddit.
6. Don't invest in PBN-style link networks for AI visibility - Cody reports seeing no effect.
7. Re-test quarterly rather than assuming any finding holds.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Both hosts are describing an unsettled field. Any vendor offering consistent cross-LLM ranking is, on Jackie's logic, either wrong or would be monetising it differently.

**Apply at Pabau:** Pabau should hold AI visibility vendors to the measure-versus-influence question, and put the actual effort into the one thing both practitioners agree on: being present, well-described and well-positioned in the third-party listicles that rank for practice-management software queries.

**Apply anywhere:** Hold AI visibility vendors to the measure-versus-influence question, and put the actual effort into the one thing both practitioners agree on: being present, well-described and well-positioned in the third-party listicles that rank for your category's queries.

### 7. Open the About page with a plain, non-promotional value proposition  `69.2`
*core · best practices · source 69*

Smarty's first structural rule: start the About page by explaining what you do in a very clear, non-promotional way. The same statement has to be consistent with what you say everywhere else, including social media profile bios and directory listings. The reason is mechanical rather than stylistic. An LLM reading your About page alongside your LinkedIn bio and your directory entries is looking for a stable description it can repeat. If the three disagree, none of them is reinforced. A promotional opener also wastes the position on the page where the model is most likely to extract a definition of the business.

> "in a very clear, non-promotional way"

**How to do it**

1. Write one sentence naming what the business does, for whom, and in what category, with no adjectives of quality.
2. Put that sentence as the first line of the About page body, above any history or founder narrative.
3. Copy the same sentence verbatim into the LinkedIn, X and Facebook bios.
4. Copy it into every directory and review-platform listing you control.
5. Keep a single canonical file of that sentence and require any change to propagate to every listing on the same day.
6. Re-audit the listings quarterly for drift.

**Tools:** LinkedIn

**Pitfall:** Marketing rewrites the homepage tagline and never updates the directories, so the descriptions drift apart. The signal is an AI assistant describing you using an old positioning line you retired a year ago.

**Apply at Pabau:** Pabau should fix one canonical sentence describing the product for aesthetic and healthcare practices, then push it to the About page, LinkedIn, Capterra, G2 and every software directory listing at once.

**Apply anywhere:** Fix one canonical sentence describing what the business does, place it first on the About page, and mirror it verbatim across every social bio and directory listing you control.

### 8. Owned content beats off-site mentions beats on-site tweaks  `12.4`
*core · best practices · source 12*

Devesh's tiered GEO framework ranks three types of work by actual impact: tier one, the most foundational, is owned content on your own site that ranks for terms directly relevant to your product space, since this is what an LLM's live web search can actually surface when someone asks for recommendations. Tier two is earned off-site mentions, meaning appearing in other people's content that itself ranks for those same relevant terms. Tier three, and least important despite getting the most online attention, is on-site technical tweaks such as schema and llms.txt, which only help crawlers digest content that's already there rather than making a brand known or associated with anything new.

> "content on your site that ranks for relevant terms"

**How to do it**

1. Rank your current or planned GEO work items into three tiers: owned content that ranks for product-relevant search terms, earned mentions in third-party content ranking for those same terms, and on-site technical tweaks such as schema, llms.txt, and FAQ formatting.
2. Allocate the majority of your GEO budget and time to tier one, owned content, since it is the foundational layer determining whether an LLM's live web search ever surfaces your brand at all.
3. Allocate secondary effort to tier two: off-site mentions, PR, and guest content on industry-relevant ranking pages.
4. Treat tier three, on-site technical tweaks, as optional low-priority polish, implemented only after tiers one and two are well resourced.
5. Before adding any specific on-site tweak such as an llms.txt file, check for actual evidence a given LLM vendor consumes it rather than assuming it's worthwhile because it's commonly recommended (inferred).
6. Periodically re-audit your GEO task list against this three-tier ranking to confirm effort hasn't drifted toward easy, low-impact tier-three tactics at the expense of tier-one content production.

**Pitfall:** The online GEO narrative is heavily skewed toward tier-three, on-site crawler-comprehension tactics because they're easy and specific to recommend - don't let ease of implementation substitute for actual impact; Devesh says his clients get great AI visibility results without using any tier-three tactics at all.

### 9. Phrase headers as the sub-questions likely to retrieve the chunk  `76.4`
*core · best practices · source 76*

Under the heading 'chunk relevance', the paper defines the concept as how well a passage serves the specific sub-query likely to retrieve it, and gives concrete formatting rules. Headers should be phrased as questions aligned with anticipated query patterns. Section boundaries should be drawn at logical chunk points. Statistics and citations should sit inside the passage rather than being collected in footnotes. Sentence structures should be direct, and each passage should resolve a question rather than advance a narrative. The authors are explicit that this is a departure from human readability: human readers benefit from narrative arc, contextual buildup and rhetorical structure, while LLMs reward clarity, explicit attribution and logical segmentation. Kopp is cited for that distinction. The practical test is whether the header names the query the passage answers.

> "headers phrased as questions aligned with anticipated query patterns"

**Evidence:** Kopp is cited for the distinction between LLM readability and human readability; the paper lists three principles, self-containment, semantic density and chunk relevance, as jointly determining whether a passage survives retrieval.

**How to do it**

1. Collect the real question phrasings from People Also Ask, forum threads and support tickets.
2. Rewrite each H2 and H3 as one of those questions, in the searcher's words.
3. Move the section break to fall where the answer to that question ends.
4. Pull every footnote and endnote citation up into the sentence it supports.
5. Cut the narrative connective tissue between sections that only exists to make the article flow.
6. Check the first sentence under each header directly answers the header before any setup.

**Pitfall:** Optimizing headers for human scannability alone. A header like 'Getting started' names no query, so the chunk under it has nothing for the retriever to match against.

**Apply at Pabau:** Convert vague H2s on Pabau blog and template pages into the exact question phrasings clinic owners use, and make the first sentence under each an answer rather than a lead-in.

**Apply anywhere:** Convert vague H2s into the exact question phrasings your audience uses, and make the first sentence under each an answer rather than a lead-in.

### 10. Plan for seven or eight slots in AI answers against a hundred on page one  `89.12`
*core · best practices · source 89*

The sharpest number in the Grow and Convert study is the ratio of available slots. Google page one gave them over 100 distinct tools across 8 to 10 results for a single category query. ChatGPT gave 7 to 8. That is roughly a twelvefold cut in how many brands the answer will hold. Two consequences follow. The competitive bar rises sharply, because being the fortieth-best-known tool in a category still gets you onto Google page one somewhere and gets you nowhere in an AI answer. And the tactic of publishing your own roundup that satisfies Google while quietly including your product stops working, because the model is not linking to your page, it is writing its own. Planning has to shift from being present to being top eight.

> "whereas there were over 100 tools listed in the 8"

**Evidence:** Grow and Convert measured 7 to 8 tools recommended per ChatGPT query against over 100 tools listed across the 8 to 10 results on Google page one for the same query.

**How to do it**

1. Count how many brands your category's AI answer actually holds by sampling the prompt ten times and taking the median list length.
2. List every brand that appears in any of those runs; that is your real competitive set, not the page-one list.
3. Rank yourself against that set on third-party mention count, not on your own ranking positions.
4. If you are outside the set, set a twelve-month target of entering it rather than a quarterly ranking target.
5. Stop counting self-published roundups as AI-visibility work and reclassify them as Google-ranking work.
6. Reallocate the difference into earning placements inside other people's roundups.

**Tools:** ChatGPT

**Pitfall:** Carrying over a Google mindset where appearing anywhere on page one counts as a win. In an eight-slot answer there is no long tail to sit in.

**Apply at Pabau:** Pabau's own comparison and 'best software' pages still earn Google traffic and should stay, but they should not be counted as AI-visibility work in reporting. The AI target is entering the eight-name set for aesthetic practice software.

**Apply anywhere:** Your own comparison pages still earn Google traffic and should stay, but do not count them as AI-visibility work. The AI target is entering the short recommended set for your category.

### 11. Plan for the effective prompt, not the literal prompt users type  `83.2`
*core · content insights · source 83*

Grow and Convert draw a distinction they say is the whole point: the literal prompt is what the user types, the effective prompt is that text plus everything the model already knows about them. Their example is a lead typing 'find me a good content marketing agency' while the effective prompt is closer to a 1000-word essay on her business size, budget, industry, what she has already tried and who is on her team, ending with 'and so taking all that into account, what would be a good agency for me?'. They stress this is not a wording problem. Tracking 'what are some good content agencies' alongside 'find me the best content agencies' does not cover it, because the personalization layer sits underneath every phrasing. Content planning therefore has to target the essay, not the phrase.

> "the difference between the literal prompt and the effective prompt"

**Evidence:** Grow and Convert describe the literal prompt 'find me a good content marketing agency' expanding into an effective prompt they characterize as a 1000-word essay on the user's business situation.

**Tools:** ChatGPT, Claude, Gemini

**Pitfall:** Teams respond to this by adding more prompt phrasings to their tracking tool and declaring coverage. The tell is a tracking sheet that grows in rows while the content plan never changes.

**Apply at Pabau:** When Pabau plans a page, write down the 300-word situation a real practice owner would have already told ChatGPT, then make sure the page answers that situation, not just the short keyword. That is what turns a generic 'best clinic software' page into one an LLM can match.

**Apply anywhere:** Before planning a page, write out the paragraph of context a real buyer would already have shared with an AI tool, then make sure the page speaks to that situation rather than only to the short query.

### 12. Plan on a search volume of one for most AI prompts  `83.11`
*core · general insights · source 83*

Devesh states the planning assumption bluntly: we are moving to a world where the search volume of most people's prompts is one. His reasoning is that the effective prompt includes an unpredictable amount of personal context, so two users typing the same words are not making the same request. That breaks the SEO habit of treating prompts as keywords each with a volume. The consequence for strategy is that prediction is off the table and coverage replaces it. You stop asking which prompt to target and start asking which situations you have failed to describe anywhere on your site. He is explicit that this is not trackable in the SEO style marketers are used to, and that no tool, including the ones selling chat panel data, changes it.

> "the search volume of most people's prompts is one"

**Evidence:** Grow and Convert argue personalization makes each effective prompt unique, so prompt volume converges on one per user.

**Pitfall:** Reporting frameworks built on prompt volume will keep producing confident numbers that describe nothing real. The signal is a forecast that assumes prompt frequency behaves like keyword frequency.

**Apply at Pabau:** Pabau's GEO reporting should not carry per-prompt volume forecasts. Report topic coverage and topic-level presence instead, and judge the content plan by how many practice situations have a page.

**Apply anywhere:** Drop per-prompt volume forecasts from your AI reporting. Report topic coverage and topic-level presence, and judge the content plan by how many customer situations have a page describing them.

### 13. Plan roughly two buying-intent prompts of coverage per target keyword  `82.3`
*core · concrete actions · source 82*

Grow and Convert give a planning ratio from the Level AI engagement: 50 or more targeted keywords produced visibility in over 100 related high buying-intent prompts. That is about two prompts of coverage per ranking keyword, and it is the number to size a GEO program with. It reframes the unit of work. You do not write a page per prompt, because prompts are not addressable; you write a page per keyword and inherit the prompt cluster around it. The programme also ran over roughly a year, starting in 2024 on classic buying-intent SEO and expanding into AI search in 2025, so the ratio is the output of a sustained content run rather than a one-quarter push.

> "we've targeted 50+ keywords for Level AI so far"

**Evidence:** Level AI: 50+ targeted keywords produced brand mentions in 100+ high buying-intent prompts, work running from 2024 into 2025.

**How to do it**

1. Build a target list of bottom-of-funnel keywords in your category, sized at roughly half the number of prompts you want to be visible for.
2. Filter the list to keywords with clear product-purchase intent, such as category, tool-comparison and use-case terms.
3. Write one thorough article per keyword rather than one per prompt phrasing.
4. For each keyword, log the two to five prompts you expect it to cover and add them to your tracked basket.
5. Check rankings first: a keyword that is not on page one does not count toward the prompt total yet.
6. Report progress as prompts covered out of prompts targeted, not as pages published.
7. Re-forecast the ratio from your own data after 20 ranked keywords, since a crowded category will return fewer prompts each.

**Tools:** Traqer, Ahrefs

**Pitfall:** Counting prompts you appear in on a single check overstates coverage, because AI answers vary by run. Only count a prompt as covered when it holds across repeated checks.

**Apply at Pabau:** Pabau should size its blog and template roadmap against a prompt target. If David wants visibility on 60 buying-intent prompts about clinic and medspa software, that implies roughly 30 ranked bottom-funnel keywords, not 30 published pages.

**Apply anywhere:** Size a GEO content roadmap against a prompt target using roughly two covered prompts per ranked keyword. Count only keywords that actually reach page one.

### 14. Point link building and mention building at the newly published bottom-funnel pieces  `103.11`
*core · concrete actions · source 103*

Grow and Convert do not treat promotion as a site-wide activity. Once the first batch of bottom- and middle-funnel pieces is published, they build backlinks to those specific pieces, and separately work on getting mentions on the domains that ChatGPT and Perplexity cite most often when answering product recommendation queries. The two efforts serve one goal: the same pages rank in traditional search and get recommended directly by the AI tools when someone asks for software in the client's category. The sequencing matters. Promotion starts after the conversion pages exist, so the authority lands on pages that can turn a visit into a signup, not on a homepage or a top-funnel guide.

> "domains that AI engines like ChatGPT and Perplexity frequently cite"

**Evidence:** Grow and Convert run this as the standard post-publication step in a SaaS engagement, aimed at both traditional rankings and LLM recommendations.

**How to do it**

1. Wait until the first batch of category and comparison pages is live before starting promotion.
2. List the target pages and treat each as its own link-building campaign with its own prospect list.
3. Run your category's product recommendation prompts through ChatGPT and Perplexity and record every domain cited.
4. Rank those domains by how often they appear across the prompt set.
5. For the top domains, find the route to inclusion: review profile, roundup listing, contributed piece, or a data submission.
6. Get the brand named on those domains with the same positioning wording used on your own pages.
7. Recheck the prompt set after the mentions go live to see whether the brand now appears.
8. Keep link building and mention building as separate lines in the plan, with separate reporting.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Building links before the target pages exist. The authority lands on generic pages, and the pieces that could convert launch with nothing pointing at them.

**Apply at Pabau:** After Pabau publishes a comparison or vertical category page, promotion should target that URL specifically, plus placements on the review and industry sites that AI engines cite for practice management software.

**Apply anywhere:** Publish the bottom-funnel pages first, then run link building per page, and separately chase mentions on the domains AI engines cite for your category's recommendation prompts.

### 15. Prediction: AI Overviews to exceed 80% of queries  `29.14`
*core · general insights · source 29*

Asked for a single SEO prediction for the coming year, Hank forecasts that AI Overviews will appear on more than 80% of Google queries, up from what he cites as Rand Fishkin's team measuring roughly 68% at the time of the conversation. This is a specific, quantified forecast meant to set planning expectations for how much of the SERP will carry an AI-generated answer layer within about a year.

> "AI Overviews are now going to be 80%-plus"

**Evidence:** Hank cites 'Rand's team' (Fishkin's research) measuring AI Overviews present on roughly 68% of tracked queries at the time of the conversation, and predicts that share will exceed 80% within the next 12 months.

**Apply at Pabau:** Build Pabau's SEO reporting and forecasting around the assumption that AI Overviews will sit on top of the large majority of tracked queries within a year - track AI-citation presence alongside traditional rank tracking, since a growing share of 'ranking #1' won't correspond to being the first thing a searcher sees.

**Apply anywhere:** Build your SEO reporting and forecasting around the assumption that AI Overviews will sit on top of the large majority of tracked queries within a year - track AI-citation presence alongside traditional rank tracking, since a growing share of 'ranking #1' won't correspond to being the first thing a searcher sees.

### 16. Prefer owned content over off-site mentions on algorithm-risk grounds  `84.7`
*core · best practices · source 84*

Grow & Convert give three reasons owned content sits above off-site mentions in their pyramid, and the third is the one most often missed. First, your own pages give you room to explain who the product helps, in what scenarios and how, which matters because ChatGPT personalizes recommendations from what it knows about the user, so more specific content is more likely to be cited at the right moment. Second, the same content pays out twice, driving traditional SEO results and LLM visibility from one asset. Third, owned content carries less algorithm-update risk: one update can remove an entire third-party site from an engine's citation set, and they point to what happened to Reddit on ChatGPT, whereas LLMs will always keep pulling from the broader web including individual brand sites.

> "One algorithm update can nix an entire third-party site"

**Evidence:** Grow & Convert cite Reddit's fall in ChatGPT citations as the example of a single third-party dependency being switched off by one change.

**How to do it**

1. Put owned content first in the GEO plan, before any off-site mention work.
2. Write product pages that state explicitly who the product suits, in which scenarios, and how, rather than generic feature lists.
3. Target the same product-intent keywords for SEO and GEO so one asset serves both.
4. Treat any single third-party platform as a rentable channel, and never let more than a minority of your citation surface depend on one.
5. Track the citation share coming from each third-party domain so a sudden drop is visible.
6. Spend off-site budget only on the domains your own prompt data shows are cited.

**Pitfall:** Teams build a GEO strategy around one platform because it dominates the current citation charts, then lose the whole channel when the engine changes how it weights that platform.

**Apply at Pabau:** Pabau should keep the majority of its AI citation surface on pabau.com pages rather than on any one directory or review platform, so a single engine change cannot remove the channel.

**Apply anywhere:** Keep the majority of your AI citation surface on pages you own. Third-party platforms can be dropped from an engine's citation set by a single update, while brand sites keep getting pulled from the open web.

### 17. Prioritize Claude for B2B GEO, ChatGPT for B2C GEO  `35.2`
*core · best practices · source 35*

Charles suggests that AI-visibility optimization is not a single undifferentiated task across all models: businesses in B2B niches should prioritize being well-represented in Claude's outputs, while B2C or more generic consumer niches should prioritize ChatGPT. For a B2B SaaS company like Pabau, this means spreading GEO effort evenly across every AI model likely wastes budget compared to concentrating first on the model most used by the actual buyer persona (practice owners and managers researching software), then treating other models as secondary checks.

> "if you're in B2B, maybe you should optimize for Claude"

**How to do it**

1. Confirm whether your core buyer is B2B (practice managers/clinic owners evaluating software) or B2C/generic consumer, since the source ties model priority to this distinction.
2. If B2B, make Claude the primary model for testing and improving brand visibility on category buying-research queries (e.g., 'best practice management software for med spas').
3. If B2C or a broad consumer niche, make ChatGPT the primary model for the same testing and optimization work instead.
4. Run the actual target buyer-research queries manually in the prioritized model on a recurring cadence (e.g., weekly or monthly) and log whether and how the brand is mentioned or recommended. (inferred)
5. Note which sources the prioritized model cites for those queries and prioritize digital PR or content placement on those specific sources. (inferred)
6. Still periodically spot-check secondary models (ChatGPT, Perplexity, Gemini, Google AI Overviews) so a shift in the broader AI-search landscape isn't missed, but treat the primary model's results as the main KPI. (inferred)
7. Revisit the B2B/B2C model-priority assumption periodically since model usage patterns by audience type can change as tools evolve. (inferred)

**Tools:** Claude, ChatGPT, Perplexity, Gemini

**Pitfall:** Treating 'optimizing for AI search' as one undifferentiated task spread evenly across every model, instead of recognizing that B2B and B2C audiences default to different AI tools and should be prioritized accordingly.

### 18. Queries cited in AI Mode are getting almost no clicks  `02.4`
*core · content insights · source 02*

After classifying likely AI Mode queries and cross-referencing them against click data, the finding was that there were no clicks at all for many of those AI Mode queries despite the site's content being cited within the AI Mode conversation, with the explicit caveat that some (but not all) of that zero-click traffic is explained by automated tracking-tool queries rather than real users. This is flagged as something every site owner should specifically check in their own data, since a citation inside an AI Mode answer does not appear to reliably translate into any measurable click-through.

> "There are no clicks at all for those AI Mode queries"

**Evidence:** Direct observation from the exported and classified data: 'There are no clicks at all for those AI Mode queries... Some of those queries are clearly from automated tracking tools, but others aren't. And I'm not seeing many clicks there.'

**Apply at Pabau:** When reporting on Pabau's AI visibility, distinguish being cited/mentioned in AI Mode from actually driving traffic — track citation appearances and click-through separately, and expect the click-through rate on AI Mode citations to run far below traditional organic results.

**Apply anywhere:** When reporting on your AI visibility, distinguish being cited/mentioned in AI Mode from actually driving traffic — track citation appearances and click-through separately, and expect the click-through rate on AI Mode citations to run far below traditional organic results.

### 19. Query ChatGPT directly with customer questions to check AI visibility  `30.10`
*core · concrete actions · source 30*

Since standard website metrics don't capture AI-answer presence, Ellen's practical way of checking whether a visibility campaign is working is to manually type real customer-style questions into ChatGPT and see whether the client shows up — she validated the Dial One Plumbing case study this way, confirming the business appeared as one of the top three local plumbing businesses when she entered queries like 'emergency plumbing' or '[service] near me.'

> "just go into ChatGPT, put in search queries and questions"

**How to do it**

1. List 5-10 real customer-phrased questions or search queries relevant to the business or product.
2. Open ChatGPT in a fresh session to reduce personalization bias. (inferred)
3. Enter each query exactly as a prospective customer would phrase it.
4. Record whether the brand is mentioned at all, its position or order among any brands listed, and whether a link or citation is included.
5. Repeat the same query set on a regular cadence (e.g., monthly) to track whether visibility is improving or declining.
6. Cross-reference any spikes or drops in AI-answer visibility with recent content, PR, or link-building activity to infer what's driving the change.

**Tools:** ChatGPT

**Pitfall:** Judging a visibility campaign only by traditional website metrics (traffic, keyword rank) misses AI-answer presence entirely, since, as Ellen notes, those hard metrics aren't what AI systems are drawing on.

### 20. Rank for product-intent keywords because LLMs cited clients in 88% of topics  `84.6`
*core · content insights · source 84*

The single strongest result in the study is that LLMs cited Grow & Convert's own clients' content in 88% of the product-specific topics analyzed across the five brands, often referencing blog posts the agency wrote for them. They attribute this to their Prioritized GEO order: when your site ranks on Google for product-intent keywords, you are positioned for LLM exposure because the models search the web to ground their answers, especially for product questions. The screenshots in the study show the same domains ranking for traditional SEO queries that the models then discover. This is why owned content sits at Tier 1 of their GEO pyramid, above off-site mentions at Tier 2 and on-site tactics at Tier 3, rather than being treated as a separate discipline from SEO.

> "LLMs cited our clients' content in 88% of the topics we analyzed"

**Evidence:** Across five clients and 120 prompts, client content appeared in 88% of the analyzed product-specific topics.

**Pitfall:** The 88% is measured on clients the agency already ranks well, so it describes the payoff of ranking, not a shortcut around it. A site that does not rank sees none of this.

**Apply at Pabau:** Pabau's fastest route into AI answers is ranking pabau.com for product-intent queries clinic owners ask, not adding schema or llms.txt. Every ranking gain on a comparison page doubles as a GEO gain.

**Apply anywhere:** Ranking your own pages for product-intent keywords is the most reliable route into AI answers, because the models ground product questions in live web results. Treat GEO as an outcome of rankings, not a parallel program.

### 21. Rank the head term and let query fan-out cover the variants  `79.4`
*core · best practices · source 79*

Grow & Convert's rule for keyword selection under GEO is to rank in the top few spots for the head bottom-of-funnel term first, because that naturally captures a range of long-tail variations. Their reasoning is query fan-out: an LLM may phrase its search for a topic in many different ways, so a page that only matches one exact phrasing gets found on one branch. A page holding the top spots for the head term shows up across the spread. They show this with InnovationCast, whose piece on innovation management software ranks in top positions for a group of related traditional keywords, which they describe as the natural fan-out that foundational SEO content produces. The practical instruction is to resist building a separate thin page per long-tail phrasing and instead make one page strong enough to hold the cluster.

> "Focus on ranking for the head term first"

**Evidence:** InnovationCast's innovation management software article ranks in top spots across a set of related traditional keywords, which the authors present as natural fan-out.

**How to do it**

1. Pick the single head bottom-of-funnel term for the topic, for example 'innovation management software'.
2. Pull the long-tail variants around it and treat them as sections in one page, not as separate pages.
3. Write one deep page targeting the head term and covering the variants inside it.
4. Check rankings for the whole variant set, not just the head term, once the page settles.
5. Add a new page only where a variant has clearly different intent and its own SERP.
6. Re-check the variant rankings after each refresh to confirm the cluster is still consolidating on one URL.

**Pitfall:** Splitting the long tail into separate thin pages produces cannibalization and none of them hold a top spot, which loses every fan-out branch at once.

**Apply at Pabau:** On pabau.com this argues for consolidating near-duplicate practice-management-software pages into one strong page per head term, then covering variants as H2s inside it. David should audit for split variants before commissioning anything new in that cluster.

**Apply anywhere:** Consolidate near-duplicate pages into one strong page per head term and cover the variants as sections inside it. Audit for split variants before commissioning anything new in the cluster.

### 22. Rank-stack the ten most-cited URLs, not the most citations  `56.15`
*core · concrete actions · source 56*

The refinement both hosts arrive at is that citation count is the wrong metric - citation frequency across the query fan-out is the right one. When a prompt triggers a fan-out, the same article may appear as a citation a very large number of times across the expanded query set; Cody's example is an article appearing 180 times in one fan-out corpus. In a given niche there might be 300 citations that exist, but the top 10 that are referenced most often are where the leverage is: get into those and he says you see an immediate lift in traffic. Edward's version is the same - look at the query fan-outs, find the articles cited most across many prompts, and buy your way into the top spot at whatever it costs. The framing to take away is prioritisation: 'it's not about the amount of citations you have, it's the citation relevance of how often is this being pulled into the query fan-out.'

> "you can start to rank stack those"

**How to do it**

1. Collect the query fan-outs for your priority prompts, not just the visible answer.
2. Log every cited URL per fan-out query, so one prompt yields many citation observations.
3. Count occurrences per URL across the whole corpus to get a frequency ranking rather than a list.
4. Take the top ten most-frequently-cited URLs in your niche and treat them as your target list.
5. Work them in order of frequency, securing inclusion in the highest-frequency source first.
6. Rank-stack: once you're in the top sources, work down the long tail of the remaining citations.
7. Re-measure frequency periodically, since the cited set shifts as the engines change.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Chasing a large number of low-frequency citations is the mistake this insight corrects - 300 citations in a niche is not 300 equal opportunities.

**Apply at Pabau:** Build the Pabau citation target list by frequency across query fan-outs, then work it top down - a placement in the one article that gets pulled into every fan-out is worth more than a dozen placements that get pulled into none.

**Apply anywhere:** Build the citation target list by frequency across query fan-outs, then work it top down - a placement in the one article pulled into every fan-out is worth more than a dozen that get pulled into none.

### 23. Re-run a lead's real prompt in incognito to size your personalization gap  `83.3`
*core · concrete actions · source 83*

Devesh describes a test worth repeating. After a client shared the chat where ChatGPT recommended Grow and Convert first, he opened an incognito ChatGPT window, typed her exact prompt, and even substituted 'our kind of space' with 'the business loans and funding space' to help the model along. The answer was completely different and did not mention Grow and Convert at all, let alone as the top option. That delta is the measurable size of the gap between what your tracking tool sees and what a logged-in customer sees. Run it on every shared chat you collect. A large delta means personalized context is carrying the recommendation, which tells you to invest in situation-specific content rather than in chasing the tracked prompt.

> "I opened an incognito ChatGPT window and typed in her prompt"

**Evidence:** Grow and Convert's incognito re-run of a client's exact prompt, with the industry spelled out, produced a completely different answer that never mentioned the agency.

**How to do it**

1. Take the literal prompt text from a chat a real customer shared with you.
2. Open a logged-out incognito ChatGPT window so no memory or history applies.
3. Paste the prompt verbatim and record whether your brand appears and in what position.
4. Re-run it a second time with the vague parts replaced by explicit context, such as naming the industry the customer works in.
5. Record whether the substitution brings your brand back into the answer.
6. Log three fields per test: appeared in the real chat, appeared cold, appeared cold with context added.
7. Treat any prompt that wins in the real chat but loses cold as evidence that personalization, not phrasing, decided it.
8. Route those cases to the content plan as a missing situation, not to the tracking tool as a missing keyword.

**Tools:** ChatGPT

**Prompt / template:**

```text
What are the best SEO companies in your opinion who have driven massive results with endless leads for people in our kind of space?
```

**Pitfall:** People run the cold test once, see themselves missing, and conclude their GEO work has failed. The cold result is not your real visibility, it is the control condition.

**Apply at Pabau:** Whenever a Pabau lead shares an AI chat, have someone repeat the prompt cold in incognito and log the difference. A wide gap says the fix is more use-case content on pabau.com, not more prompts in the tracking dashboard.

**Apply anywhere:** Whenever a customer shares an AI chat, repeat their exact prompt in a logged-out incognito window and log the difference. A wide gap means personalization decided the recommendation, so the fix is more situation-specific content, not more tracked prompts.

### 24. Rebuild the About page as your primary AI citation asset  `69.1`
*core · concrete actions · source 69*

Ann Smarty says that in her GEO audits the business About page is consistently one of the most cited pages for target prompts. ChatGPT and Gemini check official About pages to verify whether a brand is worth recommending at all, so the page acts as a verification gate before a recommendation is made. Most SEO teams still treat About as a boilerplate page written once at launch. Smarty's argument is that it now earns the same treatment as a money page: a deliberate structure of value proposition, verifiable credibility signals, use cases and consistent terminology, plus Organization schema. Her closing rule for the whole page is to prioritize clarity, factual detail, and visible connections to trusted known entities.

> "one of the most cited pages for target prompts"

**Evidence:** Smarty reports the About page as one of the most cited pages for target prompts across her GEO audits.

**How to do it**

1. Run your top 20 target prompts through ChatGPT, Gemini and Perplexity and log which of your URLs get cited.
2. If the About page appears, treat it as a ranking page and give it a full rewrite brief; if it does not, assume it failed the verification check.
3. Restructure it in Smarty's order: plain value proposition, credibility signals, use cases, consistent terminology.
4. Replace every unverifiable marketing claim with a fact that carries a number, a date, or an outbound link.
5. Add Organization schema covering name, alternate name, address, contact, logo, founding date, founder and sameAs.
6. Re-run the same prompt basket 30 days later and compare citation counts for the About URL.

**Tools:** ChatGPT, Gemini, Perplexity

**Pitfall:** Teams keep the About page as a founder's story with no checkable facts. The signal you have hit this is an AI assistant describing your company in vague category terms it could have written without reading your site.

**Apply at Pabau:** Pabau's About page should be rewritten as a GEO asset, not brand copy. It needs the customer count, the founding year, the markets served, named certifications relevant to healthcare data, and links to named publications that have covered Pabau.

**Apply anywhere:** Treat the About page as a ranking and citation page rather than brand filler. Rewrite it around checkable facts, credibility proof and use cases, then measure whether AI assistants start citing that URL for your target prompts.
