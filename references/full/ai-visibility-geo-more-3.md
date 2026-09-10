# AI Visibility / GEO — supporting (part 3 of 3)

22 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Replicate the 120-prompt citation study on your own category  `84.11`
*useful · concrete actions · source 84*

The study is a repeatable audit, and Grow & Convert lay out enough of the method to copy it. They analyzed over a hundred prompts across five industries, logged every citation the model used, categorized each prompt by funnel stage, then classified all 2,440 cited domains into industry, industry-adjacent and general. Results covered ChatGPT, Perplexity and Google AI Overview together rather than one engine. Running the same audit on your own category answers the only question that matters for off-site GEO budget: is my vertical served by vendors and trade press, or by mass-market publishers. The output is a ranked domain list plus a percentage split, and both are directly actionable.

> "we analyzed over a hundred prompts across five industries"

**Evidence:** Grow & Convert's own run: 120 prompts, five clients, 2,440 domains classified, plus a 20-prompt 542-domain comparison run on Peloton.

**How to do it**

1. Choose 4 to 6 topics that cover your commercial category.
2. Write about 20 prompts per topic in buyer language, weighted toward recommendation requests.
3. Run every prompt through ChatGPT, Perplexity and Google AI Overview and capture the full citation list.
4. Log one row per citation with prompt, funnel stage, engine, URL and domain.
5. Classify each domain as industry, industry-adjacent or general.
6. Compute the three-way percentage split overall and per funnel stage.
7. Compute the share of topics where your own domain was cited, as your baseline visibility number.
8. Rank third-party domains by citation frequency and hand the top of that list to outreach.
9. Repeat the whole run each quarter and compare the splits.

**Tools:** ChatGPT, Perplexity, Google AI Overview, Traqer

**Pitfall:** Running fewer than about twenty prompts per topic gives a domain ranking that is mostly noise, since each call resamples the citation set.

**Apply at Pabau:** David can run this audit on aesthetic practice management using a few hundred prompts, and use the resulting domain ranking as the outreach and content plan for the next quarter.

**Apply anywhere:** Run the same audit on your category: a few hundred prompts across your commercial topics, every citation logged and classified, then use the domain ranking as your outreach plan.

### 2. Replicate the fan-out overlap study for your own category  `87.6`
*useful · concrete actions · source 87*

Grow and Convert describe their method in enough detail to copy. They used 100 buying-intent prompts spanning B2B, B2C, software, services and physical products, ran them in the ChatGPT browser UI rather than the API so the data matched what a real user sees, recorded the 2-4 fan-out queries each prompt generated, and pulled Google SERPs for those queries with SerpAPI. Bing had to be run manually because the API returned unreliable results, which left a smaller Bing dataset. They then compared cited sources against the SERPs at prompt level, by category, and by domain match versus exact URL match. Running this on your own category tells you whether your niche behaves like their average or like the 20 prompts that had zero overlap.

> "We used the browser UI, not the API"

**Evidence:** Of 100 prompts, 83 triggered a web search; 20 prompts had zero cited sources in the fan-out SERPs, and only one had 100% overlap.

**How to do it**

1. Write 30-100 buying-intent prompts for your category, phrased the way buyers phrase them, such as best help desk software for small teams.
2. Run each in the ChatGPT browser UI, not the API, so you see what a real user sees.
3. Record whether a web search was triggered at all; expect roughly 17% to answer without searching.
4. Copy the 2-4 fan-out queries ChatGPT shows for each prompt.
5. Pull Google SERPs for each fan-out query with SerpAPI, going several pages deep.
6. Run Bing manually, since the API returns unreliable results.
7. Score overlap three ways: per prompt, by category, and by domain match versus exact URL.
8. Flag prompts with zero overlap and check whether those categories rely on app stores or Shopping data.

**Tools:** ChatGPT, SerpAPI

**Pitfall:** Using the API instead of the browser UI changes the retrieval behavior, so the results will not describe what your buyers actually see.

**Apply at Pabau:** David can run a smaller version, maybe 30 prompts about practice management and aesthetic clinic software, to see whether Pabau's category sits near the 40% average or at one of the extremes.

**Apply anywhere:** Run a scaled-down version of this study on 30 prompts in your own category before assuming the published averages apply to you.

### 3. Run GEO as an extension of pain-point SEO, not a separate program  `108.20`
*useful · best practices · source 108*

Grow and Convert's position on AI visibility is deliberately unglamorous. For most SaaS companies they recommend treating GEO as an extension of the SEO strategy rather than a separate initiative, on the grounds that a company doing pain-point SEO well is already building the foundation for AI visibility. The extra tactics they name, citation outreach and content structure optimization, amplify results but do not replace ranking in traditional search. Their citation outreach method is to identify which articles and sources appear most often in AI answers for topics relevant to the product, then approach those sources to get the product mentioned or included with accurate feature and use-case information. They explicitly describe this as the same concept as listicle inclusion for SEO, with the added benefit of influencing AI recommendations directly, which means it can run through the same outreach process and the same affiliate incentive.

> "we recommend treating GEO as an extension of your SEO strategy"

**Evidence:** Grow and Convert's worked example: if ChatGPT and Perplexity consistently cite one 'best project management software' article, getting your product added to that article improves AI visibility directly.

**How to do it**

1. Do not create a separate GEO workstream, budget or owner until the buying-intent keyword list is published.
2. Build a list of the product-recommendation prompts a buyer would actually type.
3. Run each prompt in ChatGPT and Perplexity and record every URL cited.
4. Count citation frequency across the prompt set and keep the domains cited three or more times.
5. Cross-reference that list against your existing listicle inclusion targets; expect heavy overlap.
6. Run one outreach process covering both, offering accurate product details and an affiliate commission where the site is monetized.
7. Re-run the prompt set quarterly to see whether the cited sources have shifted.
8. Keep ranking work as the primary effort, since the cited sources are drawn from search results.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Standing up a separate GEO program with its own budget while the bottom-funnel keyword list is still unworked. The AI answers are assembled from what ranks, so the separate program ends up funding tactics that depend on the work it displaced.

**Apply at Pabau:** Pabau should merge citation outreach into the existing listicle outreach list rather than running a separate GEO project. The aesthetics-software roundups cited by ChatGPT are largely the same pages that rank, so one outreach list covers both.

**Apply anywhere:** Treat GEO as an extension of your existing search work. Log the sources cited for your buyer prompts, merge them into your listicle outreach list, and keep ranking as the primary effort since AI answers are drawn from what ranks.

### 4. Sequence GEO as rank first, differentiate second, then buy citations  `81.18`
*useful · best practices · source 81*

Grow and Convert call their approach Prioritized GEO and it has a fixed order. Step one, identify bottom-of-funnel, high-intent keywords using their Pain Point SEO method. Step two, prioritize the lower-competition vertical variants using Underdog SEO so a weak domain can rank at all. Step three, publish highly differentiated content on your own site, sourced from expert interviews rather than desk research. Step four, secure brand mentions on the sites that already appear as citations for those prompts. The order matters more than any individual step, because steps three and four only pay once the page can be retrieved, and step four was not even started at Constitution Lending when the 50+ prompt results were achieved.

> "Our 4-Step AI Search Visibility Strategy"

**Evidence:** Constitution Lending reached top-three AI recommendations for 50+ bottom-of-funnel prompts on steps one to three alone, with citation outreach not yet begun.

**How to do it**

1. Build the bottom-of-funnel keyword list from jobs-to-be-done, category and competitor-alternative shapes.
2. Filter that list to the vertical and use-case variants your domain can realistically rank for now.
3. Interview internal experts and extract the recurring customer pain points before writing anything.
4. Publish one differentiated page per prioritized keyword, answering how you win, what you solve, who you serve and in which scenarios.
5. Wait until those pages rank on page one before judging AI visibility at all.
6. Only then scrape the domains cited for your prompts and pitch inclusion.
7. Measure per engine, since owned content carries AI Overviews and Perplexity while ChatGPT needs the third-party step.
8. Repeat the cycle on the next revenue line rather than broadening the first one.

**Tools:** Ahrefs, ChatGPT, Perplexity, Traqer

**Pitfall:** Starting at step four. Outreach for mentions before your own pages rank spends budget on placements that are working against a site the models cannot retrieve on the query anyway.

**Apply at Pabau:** Pabau should complete the ranking and differentiation steps on its vertical and comparison pages before commissioning any AI-citation outreach, and should not judge those pages on AI mentions until they hold page-one positions.

**Apply anywhere:** Run GEO in order: pick bottom-of-funnel keywords, narrow to the variants you can rank for now, publish differentiated content sourced from internal experts, and only then chase mentions on the sites already cited for those prompts.

### 5. Sort every GEO tactic by whether it exposes you or explains you  `79.16`
*useful · general insights · source 79*

Grow & Convert's organizing test for the whole field is that every GEO tactic works through one of two mechanisms: exposing your brand to LLMs, or helping LLMs understand your content once they reach it. Owned content and off-site mentions both do the first, and both do it through the same intermediary step, showing up in traditional Google or Bing results that the models search when grounding an answer. On-site tactics such as llms.txt, key takeaways, FAQs and question-worded headings only do the second. Their conclusion is that exposure is fundamentally more important, because if the models are not discovering your content while generating answers, no amount of on-site interpretation help matters. They add that LLMs already understand natural language, so reasonably well-written content that gets found will be understood.

> "Exposing your brand to LLMs"

**Evidence:** The GEO Priorities Pyramid: Tier 1 owned content, Tier 2 off-site mentions, Tier 3 on-site tactics, derived from the exposure versus understanding split.

**Pitfall:** The field's tactic churn hides this split, so teams treat an understanding tactic and an exposure tactic as equivalent line items on the same checklist.

**Apply at Pabau:** Give David a one-line test for any new GEO tactic that lands in his inbox: does it get Pabau found, or does it only help a model read a page it already found? Only fund the first until the commercial pages rank.

**Apply anywhere:** Apply a one-line test to any new GEO tactic: does it get you found, or does it only help a model read a page it already found? Fund the first until your commercial pages rank.

### 6. Stack every AI-visibility signal in a kitchen sink  `40.8`
*useful · best practices · source 40*

When it's unclear which specific signal - reviews, fan-out query coverage, YouTube presence, case studies, or testimonials - is driving AI Overview citation for a given topic, Kasra's standing rule is to deploy all of them simultaneously rather than betting on one, calling it the 'kitchen-sink approach.' He frames it as a reliable fallback: even if you currently rank for zero AI Overview queries on a topic, throwing every signal type at it at once will put you in 'a much better position' than you're in now. This follows directly from his broader point that 'nobody knows the exact formula' for AI Overviews, so stacking every plausible signal hedges against guessing wrong about which one matters most.

> "Try to get the query fan-out, try to get the reviews"

**How to do it**

1. For each priority product or topic, build a checklist of signal types: query fan-out page coverage, review platform presence and volume, YouTube video coverage, published case studies, and testimonials.
2. Audit current coverage against the checklist and mark which signal types are completely missing for that topic.
3. Prioritize filling the zero-coverage gaps first rather than further optimizing a signal type you already cover.
4. Treat 'we don't rank for any AI Overview queries on this topic' as the trigger to deploy the full kitchen-sink checklist at once, rather than testing one signal type at a time.
5. Re-audit coverage quarterly as new signal types or new AI platforms emerge, and add them to the checklist.

**Pitfall:** Don't wait to identify the single 'correct' ranking factor before acting - since even experienced practitioners are guessing at the exact AI Overview formula, betting everything on one signal type risks missing citation opportunities that a broader, simultaneous approach would catch.

### 7. Target product recommendation prompts because they carry the buying intent  `89.10`
*useful · content insights · source 89*

Grow and Convert justify studying product recommendations rather than informational questions. Their whole service is built on bottom-of-funnel product-related queries being the highest-ROI searches a brand can appear for, and they argue the logic transfers directly to AI. When someone asks a model for product recommendations, they are already motivated to buy, so appearing in that list is worth far more than appearing in an explainer answer. That makes the recommendation prompt set the right place to start any AI-visibility measurement, ahead of broad topical prompts. It also sets the format of the prompt: natural language questions like 'What are the best CRM options?' rather than the keyword forms people type into Google.

> "they are very motivated to buy"

**Evidence:** Grow and Convert selected six bottom-funnel B2B SaaS recommendation queries for the study on the grounds that these are the highest-ROI searches, and rephrased each into natural language for ChatGPT.

**Tools:** ChatGPT

**Prompt / template:**

```text
What are some of the best heatmapping tools?
```

**Pitfall:** Building the tracked prompt set out of top-of-funnel questions because they are easier to appear for. High appearance rates on explainer prompts do not convert.

**Apply at Pabau:** Pabau's tracked prompt basket should lead with buying prompts such as 'What is the best software for running an aesthetic clinic?' rather than treatment or procedure explainer prompts, which belong to the blog's traffic goals not its pipeline goals.

**Apply anywhere:** Lead your tracked prompt basket with buying prompts rather than explainer prompts, which serve traffic goals rather than pipeline goals.

### 8. Test other popularity proxies against AI recommendations, not just page-one counts  `89.11`
*useful · concrete actions · source 89*

Grow and Convert close by naming the follow-up studies they did not run, and each one is a testable correlation you can run yourself. They suggest domain rating or domain authority, since those largely measure backlink volume and so proxy how likely a model is to encounter the product in training text. They suggest Reddit popularity, on the grounds that Reddit is a known training source described in OpenAI's own GPT-2 paper. And they suggest company size, to check whether models bias toward large or public companies that get written about more in general literature. Running these against your own category tells you which lever actually predicts recommendation in your market rather than assuming page-one mentions are the only one.

> "Domain rating or domain authority"

**Evidence:** Grow and Convert name domain rating, Reddit popularity and company size as the three untested proxies for popularity worth correlating against ChatGPT recommendations.

**How to do it**

1. Take the list of products ChatGPT recommends across ten runs of your category prompt.
2. Add every product Google's page one names for the same query, so you have recommended and not-recommended groups.
3. Pull each product's domain rating in Ahrefs Batch Analysis and record it.
4. Search each product name on Reddit with a site: query and record mention count and total upvotes on the top threads.
5. Record each company's headcount from LinkedIn and whether it is public or private.
6. Compare the mean of each variable between the recommended group and the not-recommended group.
7. Rank the variables by separation and invest against whichever one separates most cleanly in your category.
8. Re-run the comparison in six months to check the relationship holds.

**Tools:** Ahrefs, Reddit, ChatGPT, LinkedIn

**Pitfall:** Reading a single correlation as the mechanism. Domain rating, Reddit presence and company size all move together for big brands, so a raw correlation with any one of them may just be measuring size.

**Apply at Pabau:** David can run this comparison across the aesthetic and healthcare software vendors that appear in AI answers to see whether Pabau's gap is backlinks, Reddit presence or sheer company size. That decides where the next budget goes.

**Apply anywhere:** Run this comparison across the vendors that appear in AI answers for your category to see whether your gap is backlinks, community presence or company size. That decides where the next budget goes.

### 9. The AI visibility tools are all bad, and there's a structural reason  `60.6`
*useful · content insights · source 60*

Joe is blunt: he has tried Profound, PromptWatch, Ahrefs' LLM tooling and others, and 'they're all pretty bad. They're not very good.' The structural reason he gives is that the format is conversational - Google is easy because everyone uses roughly the same keywords, but you can't vectorise a conversation. You could extract some keywords and report visibility on those, but it's very unique and personal. He thinks it matters for agencies who have to report to clients and hopes the engines eventually ship webmaster tools for it. Cody's position is different and worth recording as the counterweight: he doesn't care how he's viewed in these because he knows how to influence it, so he'd rather spend the time doing that than observing it. He also points out that if you know your brand you know the ten things people are likely searching to find you, and the personalisation from chat history makes per-individual reporting impossible anyway. Their shared conclusion on what an agency deliverable should be: not a visibility score, but 'we made ten blog posts that include your product and try to influence this'.

> "I've tried Profound"

**How to do it**

1. Don't buy an AI visibility tool expecting reliable trend data - both hosts say the numbers aren't dependable yet.
2. If you need reporting, define the ten to twenty prompts your buyers would actually use and track those manually.
3. Accept that personalisation makes universal visibility reporting impossible, and report on your prompt set rather than 'visibility'.
4. Spend the budget on influence - placements and context seeding - rather than on measurement.
5. Define the deliverable as work done and placements secured, not as a score.

**Tools:** Profound, PromptWatch, Ahrefs

**Pitfall:** Many of these tools generate synthetic prompt sets and report your presence in them, which measures your visibility in their invented question set rather than in real user behaviour.

**Apply at Pabau:** Pabau shouldn't buy an AI visibility platform to justify the work - define the twenty prompts a clinic owner would actually type, check them manually on a cadence, and put the budget into the placements instead.

**Apply anywhere:** Don't buy an AI visibility platform to justify the work - define the twenty prompts your buyer would actually type, check them manually on a cadence, and put the budget into the placements instead.

### 10. Treat LLMs as fan-out retrieval, not as search engines that understand content  `74.22`
*useful · best practices · source 74*

David Quaid pushes back on what he calls ivory tower SEOs claiming large numbers of LLMs are doing extensive research on content. His position is that LLMs do not really understand content, calling it a smoke-and-mirrors trick, and that anyone still thinking of LLMs as search engines should search for query fan-out, which he expects will be an eye opener. He connects this to the vague-title problem: if a query works in an LLM despite an unclear page title, that is because the model already knows your brand, not because the model inferred your industry from context. He also uses it against the claim that everything has changed because of AI, saying the reason practitioners keep doing the same SEO is that it is the same SEO, and if it had changed they would change it. The instruction that follows is to plan for retrieval over fanned-out queries rather than for comprehension.

> "please do a search for query fan out"

**Evidence:** David points to query fan-out as the mechanism, and argues nothing fundamental has changed: 'the reason that we keep doing the same SEO is because it's the same SEO.'

**How to do it**

1. Read up on query fan-out and list the sub-queries an assistant would generate for your main topic.
2. Write a page that answers each of those sub-queries explicitly, with the entity named rather than implied.
3. Make sure your brand name is attached to the claim you want repeated, since the model matches on tokens rather than inference.
4. Keep your classic SEO programme running unchanged; do not rebuild the strategy around AI commentary.
5. Check where you actually appear across a basket of prompts on a topic, not on a single prompt.
6. Re-test after four weeks, because citation is sampled rather than a position you hold.

**Pitfall:** Rebuilding a working SEO programme on the assumption that models read and comprehend the whole site. David's view is that they do not, and the vague page that works in an LLM only works because the model already knows the brand.

**Apply at Pabau:** Pabau should keep its classic SEO programme intact and add explicit, entity-named answers for the sub-questions an assistant fans out to on practice management topics. Do not rewrite the /blog/ strategy around AI comprehension assumptions.

**Apply anywhere:** Plan for query fan-out by answering each sub-question explicitly with the entity named, and keep your existing SEO programme rather than rebuilding it around AI comprehension claims.

### 11. Treat SEO traffic as an input to AI mentions through the people it reaches  `89.9`
*useful · general insights · source 89*

Grow and Convert propose a specific causal chain rather than a direct one: rank on Google, people search and find you, some of those people go on to write about you, that writing enters the training corpus, and the model then mentions you. Google is still the dominant portal by their figure of 93 percent share against 3 percent for Bing, so ranking exposes you to the largest possible pool of potential writers. They are careful to say SEO is one route among several. Paid ads, influencer work and podcast appearances all put you in front of people who might write about you. What SEO adds is precision on the exact terms and free traffic for as long as the ranking holds.

> "Rank on Google > People Google and find you"

**Evidence:** Grow and Convert cite Google at roughly 93 percent of search against 3 percent for Bing, and lay out the five-step chain from ranking to AI mention.

**Pitfall:** Expecting the chain to close quickly. Each hop takes time, so the mention effect of a ranking gain shows up quarters later, not weeks.

**Apply at Pabau:** Pabau should keep investing in rankings for bottom-funnel aesthetic-software terms on the explicit basis that the audience it reaches includes the writers and consultants who produce the roundups AI models read.

**Apply anywhere:** Keep investing in rankings for bottom-funnel category terms on the basis that the audience you reach includes the writers who produce the roundups AI models read.

### 12. Treat general-site citation share as a category property you cannot change  `84.13`
*useful · content insights · source 84*

The comparison between Climb Hire and Peloton is the cleanest evidence in the study that citation mix is set by the ecosystem, not by the brand. Climb Hire is B2C but sits in a narrow, expertise-driven niche around career training, certifications and early tech careers, and general sites made up only about 15% of its citations, close to the B2B clients. Peloton, in a mass-market consumer category, saw just under 60% general citations even though its prompt set was almost entirely product-focused, 15 bottom-of-funnel and 5 mid-funnel with no top-of-funnel prompts at all. The mechanism Grow & Convert propose is supply-side: general publishers rarely cover trucking software or IT training programs in California because the audiences are small, so when the model searches the web Google surfaces the niche sites that do cover them.

> "niche companies operate in niche content ecosystems"

**Evidence:** Climb Hire, B2C but niche, ~15% general citations. Peloton, mass-market, just under 60% general from 542 domains across 20 product-focused prompts.

**Tools:** Traqer

**Pitfall:** Chasing a Wirecutter or CNET style placement in a niche B2B vertical is usually wasted, because those publishers do not cover the topic and so are not in the retrieval set at all.

**Apply at Pabau:** Pabau will not move its citation mix toward mainstream media by trying harder, because mainstream outlets do not publish on aesthetic practice management. Effort belongs on trade titles and owned pages.

**Apply anywhere:** Your general-site citation share is set by whether mainstream publishers cover your category at all. In a niche vertical, chasing mainstream placements puts you outside the retrieval set entirely.

### 13. Treat grounding as the reason vendor blogs get cited at all  `84.18`
*useful · content insights · source 84*

Grow & Convert give the mechanism behind every number in the study: LLMs ground their responses in regular web results because the models know their training data alone is not enough to guarantee accurate or up-to-date answers, especially for questions about the best products in a category or how to solve a specific problem. So the citation set is downstream of what Google surfaces. They make this explicit when explaining the niche pattern: it is not that the models recognize niche sites, it is that when they search the web, Google surfaces the niche sites that do cover trucking software or IT training in California. For Peloton the same mechanism produces the opposite result, because Google surfaces Wirecutter, PCMag, CNET, YouTube and Reddit for 'best exercise bike for home'.

> "Google surfaces the niche sites that do cover trucking software"

**Evidence:** Grow & Convert show the Google SERP for 'best exercise bike for home' filled with general sites and match it to Peloton's just-under-60% general citation share.

**Pitfall:** Optimizing for the model rather than for the SERP it reads produces schema and llms.txt work that does not change the retrieval set.

**Apply at Pabau:** To predict which sources will be cited for a Pabau prompt, David can simply read the Google SERP for the equivalent query. Changing the citation set means changing that SERP.

**Apply anywhere:** To predict which sources an engine will cite for a prompt, read the Google SERP for the equivalent query. Changing the citation set means changing what ranks there.

### 14. Treat high-intent Google rankings as the route into AI citations  `117.13`
*useful · content insights · source 117*

Grow and Convert's position on AI visibility in healthcare is deliberately unglamorous. ChatGPT, Perplexity and Google AI Overviews pull from content that already ranks in traditional search, so the same Pain Point SEO approach that earns Google rankings improves the odds of being cited when a patient asks a tool for a recommendation. They note this matters more in healthcare than elsewhere because these tools are increasingly where patients start their research and they are summarizing medical information and recommending providers or treatments. The implied instruction is that there is no separate AI content workstream: rank for the high-intent terms and you are in the pool the model draws from. It is a consensus view in the base, but stated here with the healthcare provider-recommendation angle.

> "These tools pull information from content that is already ranking"

**Evidence:** Grow and Convert observe patients increasingly starting research in AI tools that summarize medical information and recommend providers.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Building a separate GEO content track while the underlying high-intent pages do not rank produces no citations, because the models are sampling the same SERP you are absent from.

**Apply at Pabau:** Pabau's AI-visibility work should be the same work as ranking the direct-service and pain-point pages. Check whether those specific URLs get cited when you ask an assistant to recommend practice management software.

**Apply anywhere:** Do not run a separate AI-visibility content track. Rank for the high-intent commercial terms and you enter the pool the assistants sample when recommending providers or products.

### 15. Treat llms.txt as unproven and stop spending time on it  `79.10`
*useful · best practices · source 79*

Grow & Convert put on-site tactics at the least important tier and are most dismissive of llms.txt specifically. They describe it as a proposed idea from Jeremy Howard, developer and founder of fast.ai, about how sites could help LLMs crawl. There is no evidence OpenAI or others use it, their own tests suggest it makes no difference, and they do not recommend spending time on it. On key takeaways, FAQs and question-worded headings they are more cautious: they do not have clear data yet and are still testing. What they do have is multiple clients showing up in LLM answers with content that has none of these tactics applied. So the claim is not that these formats hurt, only that they are demonstrably not necessary. Their rule is not to let any GEO tactic get in the way of content that impresses real customers and converts.

> "This doesn't seem to help at all"

**Evidence:** Their own tests on llms.txt showed no difference; multiple clients appear in LLM answers using content with none of these tactics applied.

**How to do it**

1. Do not build or maintain an llms.txt file as a visibility tactic.
2. Keep key takeaways, FAQs and question headings only where they genuinely help a reader.
3. Before adopting any new on-site GEO format, check whether pages already winning citations use it.
4. If you do test one, ship it on a subset of pages and compare citation rates against a matched control set.
5. Kill any format that makes the page worse for a buyer, regardless of what it does for a crawler.

**Pitfall:** On-site tactics are cheap and feel productive, which is exactly why teams do them instead of the expensive work of ranking. The tell is a full checklist of AI formatting on pages that do not rank.

**Apply at Pabau:** Pabau's block contract already includes Key takeaways and FAQ blocks for editorial reasons, so nothing changes there. What changes is expectation: David should not count those blocks as GEO work or expect them to move citations.

**Apply anywhere:** Keep the AI-friendly formats you already use for reader reasons, but stop counting them as GEO work. Do not build llms.txt expecting a visibility gain.

### 16. Treat the LLM as your first salesperson and brief it accordingly  `82.10`
*useful · general insights · source 82*

Grow and Convert's framing for why detail matters is that LLMs act like your first salesperson. The model summarizes your differentiators, value propositions and arguments, and uses them to educate a buyer on what makes you different and why they should choose you. That reframes the content job. You are not writing to be indexed, you are writing the brief a salesperson would need before a first call: who the product is for, the use cases, the features and benefits, the pain points it solves, and how it compares with the alternatives. Anything you leave out, the model either omits or invents from consensus. It also means the buyer often arrives having already heard your pitch, which is consistent with the wider finding that AI-sourced traffic converts better because it arrives pre-sold.

> "LLMs act like your first salesperson"

**Evidence:** Grow and Convert's stated core principle, illustrated by ChatGPT reproducing Level AI's product arguments almost verbatim.

**Pitfall:** If public content omits a qualifying detail, such as who the product is not for, the model fills the gap from competitor consensus and sends you unqualified buyers.

**Apply at Pabau:** Pabau should audit its main product and comparison pages against a sales-call checklist: fit, use cases, benefits, pain points, and the honest comparison. Gaps there become gaps in what models tell prospective clinic owners.

**Apply anywhere:** Audit your public product content against what a salesperson needs for a first call. Any gap gets filled by the model from competitor consensus.

### 17. Use one keyword list for conversions and AI visibility, not two  `113.10`
*useful · content insights · source 113*

Grow and Convert argue the high conversion intent keywords they already target also drive visibility in ChatGPT, Perplexity and Google's AI Overviews. Their mechanism: when someone asks an AI what the best project management software for construction companies is, the AI pulls from content ranking for that exact high-intent query. So the same keyword strategy that drives conversions from Google positions you to appear in AI answers, and no separate GEO keyword list is needed. They frame their whole practice as SEO plus getting clients to show up in AI searches for high-buying-intent topics and prompts, treating the two as the same job. This is a plain rejection of running a parallel prompt-led content plan alongside the SEO plan.

> "the AI pulls from content ranking for that exact high-intent query"

**Evidence:** Grow and Convert have run this as one practice for nearly a decade of SEO work and more recently for GEO and AEO placements for the same clients.

**Pitfall:** Building a separate GEO content calendar around prompts nobody would type into Google. Grow and Convert's position is that the ranking pages for the commercial query are what the model reads, so the second calendar duplicates work.

**Apply at Pabau:** David should not maintain a separate AI-visibility content plan for Pabau. Rank-stack the commercial queries, such as best practice management software for medspas, and treat AI citations as a second output of the same pages.

**Apply anywhere:** Do not run a separate GEO content calendar. The pages ranking for your commercial queries are what the models read, so target those queries once and treat AI citations as a second output.

### 18. Use tables and structured markup to raise tokens-per-fact density  `76.5`
*useful · best practices · source 76*

The paper's second retrieval principle is dense semantic encoding: every retrievable unit should carry maximum informational value in minimum token space. It names the mechanisms that force that density, HTML tables, structured data markup and concise factual statements, and says they let models extract structured facts while remaining token efficient, citing Blyskal. The authors then point at Google's own documentation, which confirms that snippet extractability, whether a passage can be lifted cleanly into a synthesized answer, is a primary filter during the aggregation phase. The practical reading is that prose padding is not neutral. It dilutes the fact density of the chunk it sits in and reduces the chance the chunk is lifted whole. A table beats the same content written as a paragraph, because the table survives extraction intact.

> "maximum informational value in minimum token space"

**Evidence:** Blyskal is cited on structured formats as forcing functions for density; Google's documentation is cited confirming snippet extractability is a primary filter in the aggregation phase.

**How to do it**

1. Find every paragraph in a page that is really a comparison, a spec list or a price list.
2. Convert each into an HTML table with a header row naming the compared attributes.
3. Add the matching structured data markup for the content type, at minimum organization schema on brand pages.
4. Cut hedging and setup clauses so each remaining sentence states one checkable fact.
5. Test extractability by copying a passage alone and asking whether it reads as a complete answer with no edits.
6. Keep the table inside the section it belongs to rather than pooling all tables at the end.

**Pitfall:** Adding schema markup while leaving the visible prose padded. Snippet extractability is judged on the passage, so markup alone does not rescue a chunk that has one fact spread over 200 words.

**Apply at Pabau:** Pabau's listicle pricing tables already do this well. Extend the same treatment to feature comparisons and procedure-code reference pages, which currently carry facts in prose.

**Apply anywhere:** Extend table treatment beyond pricing to feature comparisons and reference pages that currently carry their facts in prose.

### 19. Verify each target keyword with a three-artifact evidence loop  `82.11`
*useful · concrete actions · source 82*

Every keyword example in the Level AI case study is reported the same way, and the pattern is a reusable verification loop. First the Google ranking, taken from Ahrefs or the live SERP. Then the LLM visibility for prompts about that topic, taken from Traqer across ChatGPT, Perplexity and Google AI Overviews. Then a screenshot of an actual AI answer citing the article and naming the brand as a solution. Grow and Convert do all three for AI call center monitoring, call center real time reporting, call center analytics software and call center quality assurance tools. Reporting all three together is what lets them claim the causal chain rather than a coincidence, and it gives a client something to look at that a dashboard number does not.

> "Here's an example of Google citing our article and listing Level AI as a solution"

**Evidence:** Grow and Convert report all four Level AI keywords with the same three artifacts: Ahrefs ranking, Traqer visibility, and a live AI Overview or Perplexity answer.

**How to do it**

1. Confirm the Google position for the target keyword in Ahrefs and note the date.
2. Run the topic's prompt basket across ChatGPT, Perplexity and Google AI Overviews.
3. Record brand mention rate and citation count for the article across the basket.
4. Capture one screenshot of an AI answer that both cites the article and names the brand as a solution.
5. Store the three artifacts together against the keyword in a tracking sheet.
6. Repeat the loop monthly and flag any keyword where the ranking held but the mentions fell.
7. For keywords with a ranking but no mentions after 60 days, review the page for missing differentiator detail rather than chasing links.

**Tools:** Ahrefs, Traqer, ChatGPT, Perplexity

**Pitfall:** A single screenshot proves nothing on its own because AI answers vary by run. It is evidence only when paired with a basket-level mention rate from the same period.

**Apply at Pabau:** Pabau should keep this three-artifact record per optimized page. It makes the case for the SEO work internally and catches the ranked-but-not-recommended state early.

**Apply anywhere:** Record three artifacts per target keyword: the Google ranking, the basket-level LLM visibility, and one live AI answer citing you. Refresh monthly.

### 20. Vet a GEO tool on whether its primary view is topic-level  `85.8`
*useful · best practices · source 85*

Grow and Convert say the topic-level recommendation stands regardless of tool: use theirs, use another, or track visibility manually in a spreadsheet. What matters is that the primary unit is the topic. They built Traqer this way deliberately, and they also keep brand-level metrics at the top, but expressed as counts of topics at low, medium and high rather than one collapsed number. Their stated aim is that a team can add ten, fifty or a hundred new topics without hurting the score. Since they sell the tool, treat the product claim as disclosed advocacy and evaluate the criterion instead: does the tool's default report let you add prompts without the headline number falling.

> "track visibility manually in a spreadsheet, our recommendation"

**Evidence:** Grow and Convert state you can add 10, 50 or 100 new topics or prompts in Traqer without hurting the overall score.

**How to do it**

1. When trialling a GEO tool, add ten prompts you have no visibility for and watch what the headline number does.
2. Reject or reconfigure any tool where that action lowers the primary reported metric.
3. Check whether prompts can be grouped into named topics natively, or whether you will be exporting to a spreadsheet every month.
4. Check whether the export includes per-prompt, per-engine mention results, since that is what lets you rebuild topic bands yourself.
5. If no tool fits, run it in a spreadsheet: one row per prompt, columns for topic, engine and mention, and a pivot by topic.
6. Document your chosen definition of a topic and its basket size so the metric survives a change of tool or of staff.

**Tools:** Traqer, Peec, Profound

**Pitfall:** Vendor-published methodology posts double as sales arguments. Grow and Convert's case here is sound but it also concludes in their own product, so test the criterion against your own data before switching tools.

**Apply at Pabau:** If Pabau evaluates Peec, Profound or Traqer, run the ten-dead-prompts test during the trial and pick on that behavior rather than on engine coverage alone.

**Apply anywhere:** If you are evaluating an AI visibility tool, add ten prompts you have no visibility for during the trial and pick on how the headline number behaves, not on engine coverage alone.

### 21. Write Instagram Reel descriptions around target keywords, since AI reads them too  `23.10`
*useful · concrete actions · source 23*

Edward flags a specific, easy-to-miss tactic once a site is diversifying its marketing: Instagram Reels should be treated as a keyword-targetable content format, not just a branding channel, because Reels rank well organically within social search and, separately, the text descriptions written for a Reel are read by AI systems, meaning Reel descriptions function as another surface for shaping how AI describes or recommends a brand. His direct instruction is that whoever manages video/Reels content should be actively targeting specific keywords in Reel descriptions, coordinating with the same keyword strategy the SEO team uses elsewhere.

> "reels can and should be targeting keywords because Instagram reels rank"

**How to do it**

1. Share your current priority keyword list with whoever manages Instagram Reels/short-form video content for the brand.
2. For each new Reel, write the on-screen caption/description to explicitly include a specific target keyword or phrase relevant to the video's topic, rather than a generic caption.
3. Treat Reel description keyword targeting as part of the same editorial calendar/process as blog content keyword targeting, not a separate siloed activity (inferred).
4. Periodically check how Reels are performing both for social engagement and for any signal of appearing in AI tool answers or citations related to your brand/keywords (inferred verification step).

**Tools:** Instagram Reels

### 22. Plan against roughly 30% of search interactions being AI-mediated  `76.23`
*context · general insights · source 76*

The paper sets the scale of the shift with figures worth quoting in a business case. ChatGPT processes over two billion queries per day with roughly 800 million weekly active users, citing Chatterji et al. Google's Gemini has surpassed 750 million monthly active users. Perplexity, Claude and a widening set of specialized assistants are fragmenting the landscape. By early 2026, AI-mediated search accounted for roughly 30 percent of search interactions, up from a marginal share only a few years earlier, citing First Page Sage. The authors' framing is that the search market is no longer converging around a single gateway but fragmenting into a few general-purpose platforms alongside specialized assistants. Against a digital advertising ecosystem worth over $600 billion annually built on the premise that the search engine is a passthrough, that fragmentation is the structural problem, not the interface change.

> "AI-mediated search accounted for roughly 30 percent of search interactions"

**Evidence:** First Page Sage cited for roughly 30% of search interactions being AI-mediated by early 2026; Chatterji et al. for ChatGPT's two billion daily queries and 800 million weekly actives; Gemini above 750 million monthly actives.

**Pitfall:** Using a single AI-share figure without its date and source. These numbers move fast and an undated 30% claim in a deck will be wrong within months.

**Apply at Pabau:** When Pabau makes the internal case for AEO work, cite these figures with their sources and dates, and plan for visibility across several assistants rather than optimizing for one.

**Apply anywhere:** When making the internal case for AEO work, cite figures with their sources and dates, and plan for visibility across several assistants rather than optimizing for one.
