# AI Visibility / GEO — supporting (part 2 of 3)

22 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Expect competing vendors' own blogs to be your main citation rivals  `84.9`
*useful · content insights · source 84*

The finding buried in the numbers is that direct vendors dominate. Across Toro TMS topics, about 95% of top-cited domains were direct vendors such as AMCS Group, Transvirtual and Toro TMS itself, with the remaining 5% from one industry-adjacent publication, Transport Topics. For Wrike, 97% of top-cited domains came from within the project management industry, about a quarter of those referencing Wrike directly alongside Asana, Monday and Atlassian, with Reddit the only general site at roughly 3%. For ServiceTitan, roughly 90% were direct vendors like ServiceTitan, Jobber and BuildOps. So in a niche category the competitive set in AI answers is the same set of competing vendors you already face in the SERP, and their blogs are the sources being quoted about your category.

> "About 95% were direct vendors such as AMCS Group"

**Evidence:** Toro TMS ~95% direct vendors, Wrike 97% in-industry with Reddit at ~3%, ServiceTitan ~90% direct vendors.

**Tools:** Traqer

**Pitfall:** Treating competitor blogs as irrelevant to GEO misses that they are the documents describing your category to the model, including how they characterize you.

**Apply at Pabau:** David should audit what competing practice management vendors say about Pabau on their own comparison pages, since those pages are among the sources models read when recommending software to clinics.

**Apply anywhere:** Audit what competing vendors write about your category and about you on their own blogs, since in niche verticals those pages are the main documents the models read.

### 2. Expect content marketing to produce AI visibility as a byproduct  `87.18`
*useful · general insights · source 87*

Grow and Convert's client example is Toro TMS, a relatively young brand that had done little content marketing before they started. Once the agency began producing product-centric content targeting relevant Google keywords, ChatGPT visibility followed, tracked in Traqer both overall and for specific queries like bulk hauling software and trucking management software. Their framing is that the AI visibility came as a byproduct of high-quality content marketing, not from any AI-specific tactic. The content they describe is thorough and detailed, about the product and the problems it solves, aimed at real Google keywords where the product is a genuine answer. That last condition matters: they do not claim content wins citations for queries the product does not honestly answer.

> "The AI visibility came as a byproduct"

**Evidence:** Toro TMS, a young brand with no prior content marketing, showed rising Traqer ChatGPT visibility for bulk hauling software and trucking management software after publishing product-centric content.

**Tools:** Traqer

**Pitfall:** Expecting the byproduct without the input. Publishing shallow pages for keywords the product does not genuinely answer produces neither ranking nor citation.

**Apply at Pabau:** Pabau should measure AI visibility on category queries like practice management software for clinics with a tracker, then read it as a lagging indicator of the content programme rather than a separate workstream.

**Apply anywhere:** Track AI visibility on your category queries as a lagging indicator of your content programme, not as a separate workstream with its own tactics.

### 3. Expect different users to trigger different retrieval paths for one query  `76.17`
*useful · content insights · source 76*

In its query understanding step the paper notes that transformer-based embeddings produce multiple vector representations of a query, capturing intent, entity references and task type, and that the platform often also incorporates contextual user signals such as prior behavior, device state or search history. The implication the authors call out explicitly is that the same query submitted by different users may trigger different retrieval paths. This compounds later in the paper's measurement section, where personalization is said to make a universal brand ranking obsolete: a brand first for one user may not appear at all for another. Practically it means a single manual check of an AI answer tells you about one retrieval path, and disagreements between colleagues checking the same prompt are the system working as designed rather than a tooling bug.

> "the same query submitted by different users may trigger different retrieval paths"

**Evidence:** The paper attributes this to contextual user signals such as prior behavior, device state and search history feeding query understanding, and links it to the obsolescence of universal brand ranking.

**Pitfall:** Debugging a discrepancy between two people's manual checks of the same prompt. Contextual signals mean they were never running the same retrieval, so the difference explains nothing about your content.

**Apply at Pabau:** When Pabau spot-checks an AI answer, do it in a logged-out session, record the engine and date, and treat any single result as anecdote rather than evidence of a change.

**Apply anywhere:** When spot-checking an AI answer, do it logged out, record the engine and date, and treat any single result as anecdote rather than evidence of a change.

### 4. Expect funnel stage to shift general-site share by only a few points  `84.15`
*useful · content insights · source 84*

A widely held assumption is that top-of-funnel prompts pull in Reddit and Wikipedia while bottom-of-funnel prompts pull in vendors. Grow & Convert tested it and found the effect small. General sources showed up slightly more often in top-of-funnel prompts at about 18%, against about 11% mid-funnel and about 14% bottom-of-funnel, and they describe the differences as minor. Their reading is that even at the top of the funnel, LLMs still lean heavily on industry sources in a niche vertical. This contradicts the intuition that top-of-funnel content is where community and mainstream sources take over. In a niche category, the industry ecosystem is the only ecosystem, so it supplies the sources at every stage of the funnel.

> "General sources show up slightly more often in TOF prompts"

**Evidence:** General-site share by stage across 120 prompts: ~18% top-of-funnel, ~11% mid-funnel, ~14% bottom-of-funnel.

**Tools:** Traqer

**Pitfall:** Assuming top-of-funnel prompts need a Reddit or mainstream strategy leads to off-site spend that changes nothing, because industry sources still supply four in five citations there.

**Apply at Pabau:** Pabau's educational articles for clinic owners compete against other industry sites for citations, not against Reddit threads, so the quality bar is set by rival vendors and trade press.

**Apply anywhere:** Do not assume top-of-funnel prompts need a community or mainstream media strategy. In a niche vertical industry sources still supply roughly four in five citations at every funnel stage.

### 5. Expect prompt-level overlap to swing from 0% to 100%  `87.7`
*useful · content insights · source 87*

The headline 40% figure hides an enormous spread. Grow and Convert found 20 of their 100 prompts had zero cited sources anywhere in the fan-out SERPs, despite ChatGPT choosing to search the web for them. Only one prompt out of 100 showed 100% overlap. They grouped prompts by business type to see whether the spread came from category, and found less variation across B2B, B2C SaaS, physical products and services than expected. Physical products were lowest, which they attribute to Google Shopping data not covered in the study, and B2C SaaS was weak because those products are pulled from app stores. Their conclusion is that the variability comes from how heavily a given run weighs search results against training data, not from what the buyer is shopping for.

> "20 of the prompts had zero cited sources"

**Evidence:** 20 of 100 prompts at 0% overlap, 1 of 100 at 100%; less category variation than expected.

**Pitfall:** Reading a single prompt's citation result as a verdict on your visibility. One prompt tells you almost nothing given this spread.

**Apply at Pabau:** Any Pabau citation tracking has to be a basket of prompts per topic. A single check on best practice management software will read as noise.

**Apply anywhere:** Track citations as a basket of prompts per topic. Single-prompt checks are noise given how widely overlap swings run to run.

### 6. Expect schema and llms.txt to miss unique scenarios entirely  `83.10`
*useful · content insights · source 83*

Grow and Convert use invisible prompts to justify de-emphasizing tier three, the on-site content tweaks. Adding schema or an llms.txt file will not help you cover the unique scenarios personalization creates, because those files carry no situational content. An FAQ might help at the margins, they say, but what is far more effective is actual detailed content. The mechanism is the same one running through the whole piece: the effective prompt is a long personalized description of a buyer's circumstances, and a markup file has nothing in it for the model to match against that description. This is a direct ranking of effort, not a claim that the tactics are harmful. Ship them cheaply if you want, then put the real budget into pages.

> "Adding a schema or an LLMs.txt file won't help you cover"

**Evidence:** Grow and Convert rank on-site tactics as tier three of their GEO pyramid and say an FAQ helps only at the margins compared with detailed content.

**Pitfall:** On-site technical tweaks are easy to complete and easy to report, so they absorb GEO budget while the content coverage that actually moves recommendations stays untouched.

**Apply at Pabau:** Pabau can ship llms.txt and schema in an afternoon, but should not count them as the GEO programme. The budget belongs in use-case pages and case studies for specific practice types.

**Apply anywhere:** Ship llms.txt and schema quickly if you want them, but do not count them as your GEO programme. The budget belongs in detailed pages covering specific customer situations.

### 7. Expect the personalization gap to widen as memory and agents spread  `83.13`
*useful · general insights · source 83*

Grow and Convert argue invisible prompts are growing, not stabilizing, and name the four drivers. More people are logging in and staying logged in, and they point out almost nobody uses ChatGPT or Claude regularly in incognito. People are using agents and granting them access to email and calendar. Context windows are getting larger, so more information is factored into each answer. And the tools have memory features that carry facts across chats. The result is that a model knows far more about a user who has been chatting for a year than one who signed up yesterday, and that history changes what it recommends. The gap between the literal prompt and the effective prompt is widening, so any strategy that depends on predicting typed phrasings decays over time.

> "the gap between the literal prompt and the effective prompt is only getting wider"

**Evidence:** Grow and Convert cite four compounding drivers: persistent logged-in use, agents with email and calendar access, growing context windows, and cross-chat memory features.

**Tools:** ChatGPT, Claude, Gemini

**Pitfall:** A prompt-tracking process that looks adequate today gets less representative every quarter, and nothing in the dashboard signals the decay.

**Apply at Pabau:** Pabau should treat prompt-level tracking as a depreciating asset and shift reporting to topic coverage now, before the gap widens further. Budget for situation-specific pages should rise each year, not the tracking tool subscription.

**Apply anywhere:** Treat prompt-level tracking as a depreciating asset and move reporting to topic coverage now. Personalization is deepening every quarter, so budget should shift toward situation-specific content rather than more tracked prompts.

### 8. GEO is the only legitimate new SEO acronym  `07.1`
*useful · general insights · source 07*

The creator argues that of all the new terms circulating (GEO, AEO, AI SEO, LLM SEO), only GEO — generative engine optimization — is legitimate, because it is the only one grounded in peer-reviewed research. Generative engines (ChatGPT, Google AI Overviews, Perplexity) differ from traditional search engines by synthesizing a direct answer instead of returning ranked blue links, so GEO is specifically the discipline of getting a business's information into those generated answers. This reframing matters because it tells David not to chase every new buzzword as a distinct discipline requiring new tactics — there is one real additional layer (GEO) sitting on top of standard SEO. Treat GEO as an extension of existing SEO work, not a parallel field requiring a separate team or toolset.

> "engines give you the answer directly from the question you asked"

**Evidence:** Creator states GEO is 'the only one that's actually been published in peer-reviewed papers,' distinguishing it from AEO/AI SEO/LLM SEO, which he treats as unsubstantiated marketing terms.

**Apply at Pabau:** David can safely ignore vendor pitches built around AEO/LLM SEO branding and instead frame Pabau's AI-visibility work internally as GEO — an extension of existing content/technical SEO, not a separate discipline needing new headcount or tooling.

**Apply anywhere:** You can safely ignore vendor pitches built around AEO/LLM SEO branding and instead frame your AI-visibility work internally as GEO — an extension of existing content/technical SEO, not a separate discipline needing new headcount or tooling.

### 9. Google is shifting search into a summarized, interactive answer engine  `35.3`
*useful · content insights · source 35*

Charles cites a Wall Street Journal interview with Google's Nick Fox, in which Fox reportedly said the entire concept of search is changing: rather than people searching, seeing a list of pages, and clicking through, the future is a summarization of sources into a single interactable answer. Charles interprets this as Google's AI mode being deliberately designed to keep users inside Google's own ecosystem rather than sending them out to websites, which is a different goal from simply 'better answering a query.'

> "concept of search is going to completely change"

**Evidence:** Secondhand citation of a Nick Fox (Google) Wall Street Journal interview, watched by Charles a few days before this conversation, describing search becoming 'a summarization of sources, a summarized answer, an interactable answer.'

**Apply at Pabau:** Plan for Pabau content to be consumed and acted on inside an AI answer surface rather than always via a click-through, which means the win condition for some queries shifts from ranking a page to being the cited/summarized source — track brand citation share in AI answers as a parallel KPI to GSC clicks.

**Apply anywhere:** Plan for your content to be consumed and acted on inside an AI answer surface rather than always via a click-through, which means the win condition for some queries shifts from ranking a page to being the cited/summarized source — track brand citation share in AI answers as a parallel KPI to GSC clicks.

### 10. Grounding is why traditional ranking is the cheapest route into LLM answers  `82.12`
*useful · content insights · source 82*

Grow and Convert state the premise behind Prioritized GEO plainly: LLMs almost always search the web to help formulate responses when users ask for product recommendations, a process called grounding, because their training data alone is not always current or sufficient for those prompts. That makes traditional search the most efficient lever. If a user asks ChatGPT for voice of customer platforms, it runs a search, and an article of yours appearing in those results substantially raises the chance your brand is named. The strategic conclusion is not that GEO is fake, but that the retrieval step is ordinary search, so ranking work and GEO work are the same spend until the retrieval step changes. Product-recommendation prompts are the specific class where this holds most strongly.

> "LLMs almost always search the web to help formulate responses"

**Evidence:** Grow and Convert's stated basis for Prioritized GEO, with the voice of customer platforms example.

**Tools:** ChatGPT

**Pitfall:** The premise is narrower than it sounds. It holds for product-recommendation prompts that trigger grounding; on definitional or general-knowledge prompts the model may answer from training data and skip search entirely.

**Apply at Pabau:** Pabau should keep GEO budget inside the existing ranking programme for commercial prompts about practice management software, and only treat off-site mention building as a separate track once the target pages already rank.

**Apply anywhere:** Because product-recommendation prompts trigger a web search, keep GEO budget inside your existing ranking work until the target pages rank, then add off-site mentions.

### 11. Keep Organization schema despite no proof AI agents read it  `69.9`
*useful · general insights · source 69*

Smarty is explicit that there is no confident proof or confirmation on whether AI agents pay any attention to website schema usage. Her recommendation to use Organization schema anyway rests on a different justification: it is officially recommended by Google, so it stays a consistent SEO recommendation regardless of what AI systems do with it. This is a useful calibration against GEO advice that sells schema as an AI-visibility lever. It aligns with the wider finding in this base that on-site technical tweaks such as schema and llms.txt move AI visibility very little compared with owned content and off-site mentions. Do the markup because it is cheap and Google asks for it, not because it will win citations.

> "no confident proof or confirmation on whether AI agents"

**Evidence:** Smarty states there is no confident proof AI agents use schema, and justifies it only on Google's official recommendation.

**How to do it**

1. Implement Organization schema because Google documents it, and budget it as maintenance rather than GEO work.
2. Do not build a GEO business case or forecast on schema changes alone.
3. Spend the GEO budget on owned content, credibility signals and off-site mention consistency first.
4. If you test schema changes, isolate the variable and measure citation counts before and after across a fixed prompt basket.
5. Keep the markup facts synchronized with the visible copy so the two never disagree.
6. Revisit if a platform publishes documentation confirming it consumes structured data.

**Tools:** Schema.org

**Pitfall:** Selling a schema project internally as the fix for weak AI visibility. When citations do not move, the whole GEO program loses credibility for a change that was never expected to move them.

**Apply at Pabau:** Pabau should keep Organization and Person schema as standard hygiene, but any AI-visibility roadmap should put budget into the About page facts, use cases and off-site listing consistency ahead of markup work.

**Apply anywhere:** Implement Organization schema as hygiene because Google recommends it, but do not fund it as an AI-visibility tactic; there is no confirmation AI systems read it.

### 12. LLMs now reward consensus and volume, like 2010-era SEO  `26.1`
*useful · content insights · source 26*

Dooley argues that ChatGPT, Claude, and Gemini currently weight the 'volume and consensus' of mentions about a brand similarly to how Google's algorithm rewarded raw backlink volume and keyword density around 2010, before quality-focused updates. In practice this means the same claim (a case study, review, or proof point) repeated across many independent guest posts, press releases, and social platforms builds a citation/consensus signal that LLMs pick up on, rather than relying on a single authoritative page. This reframes 'AI visibility' work as a distribution and repetition problem as much as a content-quality problem.

> "a lot of it now is to do with volume and consensus"

**Evidence:** Dooley's direct comparison: "a lot of it now is to do with volume and consensus, and that used to be what it used to be in 2010... Volume of backlinks used to win, it used to be just a volume game of keyword stuffing... I feel like LLMs now are pretty similar to that."

**Apply at Pabau:** For Pabau, don't assume one well-optimized article is enough for AI visibility on a topic — plan to also generate multiple independent, repeated mentions of key proof points (customer results, review scores, comparisons) across guest content, PR, and social so LLMs see consensus, not just a single source.

**Apply anywhere:** For your site, don't assume one well-optimized article is enough for AI visibility on a topic — plan to also generate multiple independent, repeated mentions of key proof points (customer results, review scores, comparisons) across guest content, PR, and social so LLMs see consensus, not just a single source.

### 13. Multimodal search input (uploaded files/tabs) will personalize AI token output  `35.7`
*useful · content insights · source 35*

Charles points to Google's search bar becoming multimodal — accepting uploaded tabs, images, and files as additional context, not just typed text — and argues this personalization will substantially change the AI's token output per user. He speculates that incidental details in that added context, such as a copyrighted company name appearing in an uploaded document, or visible software/theme choices on a webpage (his example: a Shopify theme), could end up shifting which sources or brands the AI surfaces, even though these feel like small technical details.

> "personalization changes the token output of the AI substantially"

**Evidence:** Direct claim: 'personalization changes the token output of the AI substantially... you have a copyrighted company name in a document you've uploaded, or you're using software on a web page, or using a Shopify theme on a web page — all sorts of things that end up changing the actual context.'

**Apply at Pabau:** As Google's AI Mode search bar becomes multimodal, Pabau should consider how visible technical signals on its own site (structured data, visible tech-stack markers) and any content designed to be uploaded/screenshotted by prospects (comparison sheets, UI screenshots) might factor into which vendor an AI surfaces, not just classic on-page text.

**Apply anywhere:** As Google's AI Mode search bar becomes multimodal, you should consider how visible technical signals on its own site (structured data, visible tech-stack markers) and any content designed to be uploaded/screenshotted by prospects (comparison sheets, UI screenshots) might factor into which vendor an AI surfaces, not just classic on-page text.

### 14. Old black-hat tactics work again on unpoliced AI platforms  `20.13`
*useful · content insights · source 20*

Several tactics long considered black-hat and penalized in traditional search — building microsites, cloaking, and white-on-white (invisible) text — are reportedly working again on AI search platforms, because those platforms currently have no equivalent policy/enforcement framework and their retrieval systems focus on extracting content rather than evaluating how it was presented to human visitors. The speaker frames this as an observation about the current lack of guardrails rather than a recommendation, noting it alongside a separate example of someone offering 'millions of AI-generated mentions' as blatant spam-for-hire. This is presented as a temporary gap likely to close as AI platforms mature their anti-spam enforcement.

> "there's a lot of old tactics coming back"

**Evidence:** 'there's a lot of old tactics coming back — a lot of people building microsites, a lot of people doing what would be considered cloaking, although that's not black hat here, because there are no rules on these AI search platforms... White-on-white text is working again.'

**Apply at Pabau:** David should treat this as a warning sign, not a playbook — these tactics are currently unpoliced, not durably safe, and Pabau's content strategy should keep avoiding manipulative tactics like cloaking or hidden text, since AI platforms are highly likely to eventually build enforcement against exactly this, mirroring Google's own history.

**Apply anywhere:** You should treat this as a warning sign, not a playbook — these tactics are currently unpoliced, not durably safe, and your content strategy should keep avoiding manipulative tactics like cloaking or hidden text, since AI platforms are highly likely to eventually build enforcement against exactly this, mirroring Google's own history.

### 15. Prefer owned content over Reddit because single-site strategies get switched off  `79.8`
*useful · best practices · source 79*

Grow & Convert's algorithm-risk argument for putting owned content at the bottom of the pyramid: a GEO strategy built on showing up on one site carries the risk that OpenAI, Anthropic, Google or Perplexity tunes its systems to rely on that site less, killing the strategy overnight. They say that literally happened with Reddit in ChatGPT. In September, multiple people reported the number of prompts citing Reddit as a source dropped dramatically, meaning money spent on Reddit marketing before that was likely wasted or made much less effective. Their counter-case is that the chance of the models de-prioritizing all sites across the web is very low. Your own site is one of billions that make up the bulk of the internet's content and has powered search results for decades, so it is not easily updated away.

> "the number of prompts with Reddit as a source dropped dramatically"

**Evidence:** September reports of a dramatic drop in ChatGPT prompts citing Reddit as a source, cited as retroactively devaluing prior Reddit marketing spend.

**How to do it**

1. Score every GEO tactic by what fraction of your visibility depends on a single third-party domain.
2. Cap the share of your AI-visibility plan that any one external site can carry.
3. Keep owned, ranking content as the base layer that survives a single-platform demotion.
4. Track the citation mix for your prompt basket monthly so a platform shift shows up as a distribution change, not a mystery drop.
5. When one domain's share of your citations falls sharply, redirect that budget to owned content rather than doubling down.

**Pitfall:** The failure is invisible until it is total. A Reddit-dependent program looks healthy right up to the month the model reweights, and there is no warning in your own analytics.

**Apply at Pabau:** This is an argument for Pabau keeping its GEO investment on pabau.com articles and healthcare trade coverage rather than any single community platform. David should track what share of Pabau's AI citations comes from one domain and treat above roughly a third as concentration risk.

**Apply anywhere:** Keep the bulk of your GEO investment in owned, ranking content and diversify earned mentions across several trade sites. Treat any single domain carrying more than about a third of your citations as concentration risk.

### 16. Prefer owned pages over Reddit because a mention cannot carry context  `83.9`
*useful · content insights · source 83*

Grow and Convert explain why owned content sits as tier one in their prioritized GEO pyramid, above off-site mentions in tier two and on-site tactics in tier three. Creating your own content gives you the room to discuss all the nuance and detail of where and when you shine, what pain points you solve and for whom. Their argument against chasing Reddit is mechanical, not moral. On Reddit, what are you going to do, drop your name in one sentence? That is not enough context for an LLM to connect you to a specific user's needs. The invisible prompt is a personalized essay, so a one-line brand drop has almost no surface for the model to match against. Owned pages can carry hundreds of words of situational detail per scenario.

> "That's not enough context for an LLM to connect you"

**Evidence:** Grow and Convert place owned content at tier one of their GEO priorities pyramid, off-site mentions at tier two and on-site tactics at tier three.

**Tools:** Reddit

**Pitfall:** Teams read that Reddit is heavily cited and shift budget there, then find mentions do not convert into recommendations because each mention carries a single sentence of context.

**Apply at Pabau:** Pabau should keep the majority of GEO effort on pabau.com pages that describe specific practice situations in depth, and treat Reddit or forum mentions as a supporting tier rather than the main play.

**Apply anywhere:** Keep most GEO effort on your own pages, where you can describe specific customer situations in depth. Treat forum and community mentions as a supporting tier, since a one-sentence name drop gives a model very little to match against.

### 17. Publish SEO-style content even before it ranks, because citation does not wait  `87.20`
*useful · content insights · source 87*

Grow and Convert set out the question directly: if you produce a traditional SEO post like a listicle but do not yet rank for your target keyword or related keywords, do you still have a shot at being cited by ChatGPT for similar prompts? Their data says yes. Among the 60% of cited sources that appeared in neither Google nor Bing's fan-out SERPs, about 74% were still listicles, product pages, homepages and pricing pages. So the format earns citation independent of current position. They tie this to their theories of caching and training-data retrieval: the content was found by a web search at some earlier point, or memorized, and the citation persists without a current ranking. This removes the usual argument for delaying publication until a page can rank.

> "but don't rank yet for your target keyword"

**Evidence:** ~74% of cited sources absent from both engines' fan-out SERPs were still typical SEO-style marketing content.

**Pitfall:** Holding content back until you think it can rank. Citation does not require a current position, so the delay costs you both routes.

**Apply at Pabau:** Pabau does not need to wait for a template or listicle page to rank before it can contribute to AI answers. Publish, then work the position.

**Apply anywhere:** Do not hold content back until you think it can rank. Cited sources frequently do not rank at all, so publish first and work the position after.

### 18. Publish on your own site to get into the crawl for training data  `87.12`
*useful · best practices · source 87*

Grow and Convert point out that OpenAI admits to using web crawlers both for live search and for training data, which means content on your own site has a route into the model itself, not only into retrieval. They pair this with their finding that ~74% of citations that did not appear in any SERP were still ordinary marketing content, listicles and landing pages, consistent with the model having seen that content when it was last trained. The action is unglamorous: keep publishing substantive product content on a crawlable site. They explicitly say this is not about easy-to-read content with digestible chunks, which is the tactic they keep rejecting.

> "OpenAI admits to using web crawlers"

**Evidence:** ~74% of citations absent from both SERPs were still typical SEO-style marketing content.

**How to do it**

1. Confirm your robots.txt does not block OpenAI's crawlers if you want training-data inclusion.
2. Publish detailed product, use-case and feature content on your own domain rather than only on third-party sites.
3. Keep URLs stable over years, since memorized URLs are cited under old titles.
4. Avoid gating substantive product information behind forms or JavaScript that crawlers will not render.
5. Do not substitute llms.txt, FAQ blocks or summary bullets for actual published depth.
6. Re-audit crawlability annually, since training snapshots are infrequent.

**Pitfall:** Blocking AI crawlers to protect content, then wondering why the brand never appears in answers that do not trigger a live search.

**Apply at Pabau:** Check that pabau.com does not block OpenAI's crawlers, and keep template and blog URLs stable so memorized addresses keep resolving.

**Apply anywhere:** Check you are not blocking AI crawlers, publish product depth on your own domain, and keep URLs stable for years so memorized addresses still resolve.

### 19. Rank owned content above off-site mentions because you control the wording  `86.10`
*useful · general insights · source 86*

Grow & Convert explain why owned content sits below off-site mentions in their pyramid even though both work by the same mechanism. Both expose your brand to the LLM when it searches the web to ground an answer. The difference is control. With owned content you decide what is published, how the product is positioned and how much detail you give. With off-site mentions you depend on another site to describe you accurately and favorably, and it may not. Owned content is also where you have the space to tell the whole story: who you are for, what problems you solve, how you differ, and proof you deliver. Off-site mentions amplify that story through additional sources rather than replacing it. The practical reading is that off-site work is a multiplier on a message you have already fixed on your own site, so fixing the message comes first.

> "The key distinction between Tier 1 and Tier 2 is control"

**Evidence:** Grow & Convert's stated reason for ordering the pyramid: both tiers work through grounding, but owned content carries full editorial control and unlimited space to state positioning.

**Pitfall:** Running PR before the owned positioning is settled means third-party writers invent their own description of you, and inconsistent descriptions across sources weaken what the model repeats.

**Apply at Pabau:** Pabau should settle the positioning paragraph on its own comparison and category pages before commissioning outreach, so any aesthetic-industry site that covers Pabau repeats the same description.

**Apply anywhere:** Settle the positioning on your own comparison and category pages before commissioning outreach, so any site that covers you repeats the same description.

### 20. Ranking #1 for the head term wins long, specific buying-intent prompts  `79.13`
*useful · content insights · source 79*

Grow & Convert's Perplexity example ties the whole framework together. The prompt is a long jobs-to-be-done question with heavy buying intent: 'I have a business in the healthcare space that I'm looking to sell. Can you help me think through what I need to do to sell it?' Their article for Axial, a company that helps owners find a broker, appears as the first source. The point they make is that the same article ranks #1 on Google for 'how to sell my healthcare business'. So the traditional head-term ranking is what caused the citation on a conversational prompt that shares no keyword phrasing with it. This is the concrete case for their claim that ranking in Google is the mechanism behind AI visibility, and that you cannot target conversational prompts directly.

> "ranks #1 on Google for"

**Evidence:** Axial's article is the first Perplexity source for a long JTBD healthcare-business-sale prompt, and ranks #1 on Google for 'how to sell my healthcare business'.

**Tools:** Perplexity

**Prompt / template:**

```text
I have a business in the healthcare space that I'm looking to sell. Can you help me think through what I need to do to sell it?
```

**Pitfall:** Trying to write pages that match long conversational prompts word for word produces unrankable pages that then win nothing, because the retrieval step still runs on ordinary search queries.

**Apply at Pabau:** Pabau should keep optimizing for ordinary head terms rather than trying to author pages against chat-shaped prompts. The check is whether the page holds position one for its head term, since that is what surfaces it in the long conversational queries clinic owners actually ask.

**Apply anywhere:** Keep optimizing for ordinary head terms rather than authoring pages against chat-shaped prompts. Position one on the head term is what surfaces you in long conversational queries.

### 21. Read outdated cited titles as evidence of training-data citations  `87.9`
*useful · content insights · source 87*

Grow and Convert found several cases where ChatGPT cited a real live URL but attached a title that no longer matches the page. In one case it cited the same Zapier URL twice in one source list, once as The best video conferencing software in 2026 and once as the 2025 version, while Google's SERP showed the actual current title, The best video conferencing software for teams in 2026. They rule out caching as the explanation, since OpenAI's documentation puts cache lifetimes at 5-10 minutes and sometimes up to an hour, not the months or years separating those titles. Their reading is that the URL came from training data. NeurIPS research showing models reproduce training text verbatim supports the idea that exact URLs can be memorized too. A stale title in a citation is therefore a diagnostic: that citation did not come from a live search.

> "cited a real, live URL but gave it an outdated title"

**Evidence:** OpenAI documents cache lifetimes of 5-10 minutes, up to an hour; the observed title gaps span years.

**Tools:** ChatGPT

**Pitfall:** Chasing a live-search explanation for a citation that came from memory. You will change the page and see no effect.

**Apply at Pabau:** If ChatGPT cites a Pabau page under an old title, that citation is coming from training data. Keep the URL stable so the memorized address still resolves, and do not expect an on-page edit to fix the title.

**Apply anywhere:** When an AI cites your URL under an outdated title, that citation came from training data, not live search. Keep the URL stable and do not expect on-page edits to change it.

### 22. Read the Google and AI overlap as parallel scraping, not one reading the other  `89.8`
*useful · content insights · source 89*

Grow and Convert checked what is publicly known about training data. OpenAI says only that models are trained on publicly available data plus licensed private data, and is deliberately vague to protect its competitive position. The GPT-2 paper describes a purpose-built crawler that prioritized pages humans linked to, sourced from Reddit. On that basis they conclude it is unlikely a model was trained by literally Googling things, so 'ChatGPT reads Google' does not explain the overlap they measured. The better explanation is that both systems scrape the same web and each decides in its own way what is most relevant or most commonly said. The overlap is a shared input, not a dependency. The strategic consequence is that one activity, being written about widely, serves both.

> "unlikely that GPT-4 was trained by literally Googling things"

**Evidence:** OpenAI's published statement covers only 'publicly available data and private data from licensed third-party providers'; the GPT-2 paper describes a Reddit-sourced crawl filtered by human links.

**Tools:** ChatGPT

**Pitfall:** Explaining an AI mention gain by pointing at a ranking gain in the same period. Both can rise from the same underlying coverage without one causing the other.

**Apply at Pabau:** Pabau should brief content and PR as one programme with a single goal of being written about in aesthetic-practice contexts, rather than running separate SEO and GEO tracks that duplicate work.

**Apply anywhere:** Brief content and PR as one programme aimed at being written about in your category, rather than running separate SEO and GEO tracks that duplicate work.
