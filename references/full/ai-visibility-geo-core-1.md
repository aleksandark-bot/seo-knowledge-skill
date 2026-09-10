# AI Visibility / GEO — core (part 1 of 6)

24 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. 'Mount AI': mass AI content spikes traffic, then crashes it  `13.12`
*core · content insights · source 13*

Edward describes a named pattern he calls Mount AI: a site begins mass-publishing AI-written articles, hundreds a day by his description, traffic climbs as the new pages get indexed, but because the content does not properly satisfy search intent it generates negative user signals at scale, specifically worse click-through rates and pogo-sticking, where users land and immediately return to the search results. Eventually Google's systems detect the pattern of dissatisfied searchers across the site and traffic falls back down, tracing a mountain-shaped curve on a traffic graph. The distinction both speakers draw is not AI versus no AI but volume and intent-satisfaction: using AI strategically as an assistant on a normal publishing cadence does not trigger this pattern, only mass, low-quality, intent-mismatched production does.

> "You publish these AI pages, start publishing a lot of them"

**Evidence:** Edward names and describes the shape explicitly, tying the rise-then-fall traffic curve to worsening click-through rates and repeated pogo-sticking across what he says is 'a lot of brands.'

**Apply at Pabau:** If Pabau scales AI-assisted content production, track click-through rate and pogo-sticking (short dwell time plus return-to-SERP) as leading indicators before a traffic crash appears in GSC; a rising publish-volume curve paired with flat or falling engagement quality is the early warning sign, not the eventual drop itself.

**Apply anywhere:** If your site scales AI-assisted content production, track click-through rate and pogo-sticking (short dwell time plus return-to-SERP) as leading indicators before a traffic crash appears in GSC; a rising publish-volume curve paired with flat or falling engagement quality is the early warning sign, not the eventual drop itself.

### 2. 'Source SEO': website as reservoir feeding AI's water treatment plant  `46.8`
*core · general insights · source 46*

Travis's mental model for AI search strategy: your own website is the 'reservoir' of original information, where technical SEO and structured content like the Five Ws live so crawlers can access it. Third-party platforms — YouTube, TikTok, Reddit — are the 'rivers and streams' feeding outward from that reservoir. AI search itself, meaning AI Overviews, Google AI Mode, and ChatGPT, is the 'water treatment plant,' deciding based on searcher intent whether to surface Reddit reviews, your source content, or a blend of both, while the user simply 'turns on the faucet.' His conclusion: table stakes have expanded from website SEO alone to website SEO plus YouTube SEO plus digital PR plus Reddit presence all being required simultaneously, whereas ten years ago most SEOs only worked the website layer.

> "your website is the reservoir of initial water"

**Evidence:** Travis's own coined analogy ('source SEO'): website equals reservoir, third-party platforms equal rivers/streams, AI search equals the water-treatment plant that blends or selects sources, user equals the faucet; supported by his claim that website SEO, YouTube SEO, and digital PR are now all 'table stakes' simultaneously.

**Apply at Pabau:** Pabau's AI-visibility strategy can't be website-content-only — deliberately invest in a YouTube presence, Reddit presence and mentions, and digital PR coverage as parallel 'streams' feeding the same reservoir, since AI answer engines are shown to blend third-party platform content with source-website content when deciding what to surface.

**Apply anywhere:** Your AI-visibility strategy can't be website-content-only — deliberately invest in a YouTube presence, Reddit presence and mentions, and digital PR coverage as parallel 'streams' feeding the same reservoir, since AI answer engines are shown to blend third-party platform content with source-website content when deciding what to surface.

### 3. 'The great decoupling': AI Overviews raise impressions, crash clicks  `28.1`
*core · content insights · source 28*

Endre names the phenomenon he lived through 'the great decoupling' — Google Search Console showed rankings and impressions holding roughly steady while clicks collapsed, because AI Overviews extracted and displayed his sign-language videos directly in the results without sending users to his site. The magnitude was severe and fast: roughly 50% of total organic clicks disappeared, and app-download-driving high-intent keyword traffic was hit even harder, dropping from tens of thousands of clicks to almost nothing over about three days once AI Overviews began surfacing the videos directly. For a period of three to four months afterward, the team had no clear answer and simply watched impressions rise while clicks fell, unsure whether any fix was working.

> "impressions would go up and clicks would go down"

**Evidence:** Endre's own numbers: 'several tens of thousands of clicks down to almost nothing' over roughly three days, plus his description of impressions going up while clicks went down for three to four months before a fix took hold, and the named term 'the great decoupling' both speakers use.

**Apply:** When auditing a Pabau page for an AI Overview hit, check GSC for the specific decoupling signature (impressions flat or rising, clicks falling) rather than assuming a ranking drop caused the traffic loss — the fix in that case is not to chase rankings but to change what the page offers so it can't be fully answered by a snippet alone.

### 4. AI Overview and AI Mode summarize search results directly  `12.6`
*core · content insights · source 12*

Devesh explains that Google's AI Overview and AI Mode function as 'pure search summarizers' that never answer without linking to sources, and their own documentation confirms they summarize the underlying search results for literally every query asked, unlike ChatGPT, which frequently answers from memory without searching or citing anything. Grow & Convert's own AI-visibility tool, Traqer, plotted across 19 of their clients, found AI Overview and AI Mode had the highest brand-visibility numbers of any AI surface specifically because the agency already ranks its clients well in traditional Google organic results that those tools summarize. The same data showed Perplexity and Gemini scoring markedly higher than ChatGPT, which he attributes to Perplexity being built entirely around search and citations, and Gemini searching the web more often than ChatGPT does.

> "are pure search summarizers. They never answer a question"

**Evidence:** Grow & Convert's Traqer tool, plotted across 19 clients: AI Overview and AI Mode showed the highest brand-visibility numbers of any AI surface, attributed to the agency already ranking its clients for relevant SEO terms in traditional Google; Perplexity and Gemini scored markedly higher than ChatGPT.

**Apply:** Don't treat ranking well in Google organic and winning AI Overview citations as separate workstreams - since AI Overview and AI Mode are documented summarizers of the underlying organic results, traditional on-page and technical SEO that wins Google rankings directly drives citations in Google's own AI surfaces; prioritize AIO/AI Mode and Perplexity/Gemini visibility over chasing ChatGPT specifically, since the data shows ChatGPT is currently the laggard of the four for citation-based visibility.

### 5. AI Overviews name unknown brands but link known entities  `26.7`
*core · content insights · source 26*

Dooley's testing indicates that being cited by name inside an AI Overview or AI Mode answer doesn't guarantee a clickable link — when an answer names multiple companies, the ones with strong Knowledge Graph/entity recognition are disproportionately more likely to actually receive the outbound link, while lesser-known brands get mentioned without one. This means brand/entity strength acts as a gating factor for whether AI visibility converts into referral traffic at all, separate from whether your content is good enough to be mentioned in the first place.

> "might cite five companies, but if two of them are known entities"

**Evidence:** "They might cite five companies, but if two of them are known entities, those two might get the links, and the other three might not."

**Apply at Pabau:** Pabau should treat entity-strength building (Knowledge Panel, consistent branded citations, Wikidata) as a parallel track to content optimization — ranking well enough to be cited in an AI Overview may not deliver traffic unless Pabau is also recognized as a strong entity, since the link itself appears biased toward already-known brands.

**Apply anywhere:** You should treat entity-strength building (Knowledge Panel, consistent branded citations, Wikidata) as a parallel track to content optimization — ranking well enough to be cited in an AI Overview may not deliver traffic unless your site is also recognized as a strong entity, since the link itself appears biased toward already-known brands.

### 6. AI answer engines are aggregating page one and two, and the vendors know it  `61.4`
*core · content insights · source 61*

Cody had spoken to James, co-founder of Profound, immediately before this recording, and reports the data: about 95% of the searches happening on AI answer engines are doing web scraping, and when you look at where that scraping goes, ChatGPT is scraping Google and returning an aggregate of page one and page two results. Google's AI Overview is the same thing; Perplexity is the same thing. His reasoning for why it will stay that way for a while: Google has 25 years of signal about what content is best for a specific query, so it's the most valuable resource that exists - and OpenAI isn't going to index the entire web when it can lean on Google. They might in the long term, but not now. He also explains what the AI visibility tools are actually doing: creating synthetic data - a corpus of questions and topic variations, because people use these tools with questions rather than keywords - prompting the engine with them, scoring your surface area in your category, and showing the gaps. The gaps are real and useful; the mechanism underneath is still page one and two of Google.

> "95% of the searches that are happening"

**How to do it**

1. Treat AI visibility as downstream of conventional rankings for the queries the engines run.
2. Use the visibility tools for gap analysis - which question categories you're absent from - rather than as a ranking system.
3. Build content for the gaps they surface, then verify by asking the engines the question directly.
4. Frame your target keywords as questions rather than keywords, since that's how these tools are used.
5. Keep ranking on pages one and two as the primary lever, since that's what's being aggregated.

**Tools:** Profound, ChatGPT, Perplexity

**Pitfall:** The gap reports are generated against a synthetic question set, so absence from a gap report means absence from that tool's invented questions - not necessarily from real user queries.

**Apply at Pabau:** The reassuring conclusion for Pabau is that AI visibility isn't a separate discipline: ranking on pages one and two for the questions clinic owners ask is the mechanism, and the visibility tools are useful only for spotting which question categories Pabau is missing.

**Apply anywhere:** The reassuring conclusion is that AI visibility isn't a separate discipline: ranking on pages one and two for the questions your buyers ask is the mechanism, and the visibility tools are useful only for spotting which question categories you're missing.

### 7. AI answer visibility now runs on a separate, brand-level signal set  `11.8`
*core · content insights · source 11*

Gotch argues competitive analysis must add an entirely new layer beyond traditional domain- and page-level link metrics: brand-level signals that determine whether an AI system recommends you, independent of how well you rank traditionally. He has observed brands that don't rank exceptionally well organically for a keyword still get repeatedly recommended in AI answers, driven by reviews and consensus and other signals distinct from backlinks and site authority, which he says are what drives traditional search results instead. His practical takeaway is that competitor research now has three tiers to assess — domain-level link authority, page-level link authority, and brand-level AI-trust signals — where the third tier runs on a different rule set than the first two.

> "we also have to examine the brand level"

**Evidence:** Gotch's direct observation that 'there are brands that aren't necessarily doing exceptionally well for a keyword in traditional search, but in the AI answers, the AI is recommending them over and over... because they have a lot of other signals that influence the AI systems,' naming reviews and consensus as the AI-specific signal set versus backlinks and authority for traditional search.

**Apply at Pabau:** When Pabau audits competitors for a target keyword, check AI answers (ChatGPT, Perplexity, Google AI Overview) for brand mentions separately from traditional SERP position, and treat review volume, sentiment, and cross-site consensus about Pabau as a distinct GEO lever to invest in, not an afterthought of traditional link building.

**Apply anywhere:** When you audit competitors for a target keyword, check AI answers (ChatGPT, Perplexity, Google AI Overview) for brand mentions separately from traditional SERP position, and treat review volume, sentiment, and cross-site consensus about your site as a distinct GEO lever to invest in, not an afterthought of traditional link building.

### 8. AI answers are token-sampled probability, not a stable position to hold  `25.11`
*core · content insights · source 25*

Charles explains that AI-mode outputs (ChatGPT, Google AI Mode, AI Overviews) are fundamentally probabilistic rather than deterministic, because they're generated via token sampling: each output token carries a percentage likelihood (he gives an illustrative '98.79%' example) of following the prior tokens, recalculated fresh based on full context each time. This means the same query can produce a different answer/citation set on every call unless caching is active, in sharp contrast to traditional Google search results, which have historically had a roughly 24-hour cache window (a refresh within an hour returns near-identical results; 24-25 hours later it may shift slightly, changing meaningfully only with an overnight index update or new SERP feature). The practical consequence: there is no stable 'position one' to target and defend in AI answers the way there was in blue-link SEO — visibility becomes a probability distribution you influence, not a rank you hold.

> "the AI model understands relationships and associations of a probabilistic nature"

**Evidence:** Illustrative token-probability example ('98.79%, 1.33% recurring chance of association with the next token'); contrast with Google's traditional roughly 24-hour SERP cache period, cited as the baseline stability that AI Mode/LLM outputs do not share.

**Apply:** Stop reporting AI-visibility performance as a fixed rank or position (e.g., 'we're #1 in AI Overviews for X') and instead track presence/citation frequency across repeated queries over time as a probability/share-of-voice metric, since any single check of an AI answer is just one sample from a distribution that changes on every call.

### 9. AI answers echo podcast phrasing without ever citing the podcast  `43.8`
*core · content insights · source 43*

Rand raises a specific concern about AI citation analysis as a discipline: he's confident, from repeatedly observing SparkToro's brand appearances in AI Overviews, ChatGPT, and Claude answers, that the exact words and phrasing used to describe his brand match language he has used specifically on podcast appearances, yet podcasts are never listed as the citation source for those answers. He concludes there's a real mismatch between what an AI answer actually draws its phrasing from and what it displays as its formal citation, meaning citation-tracking tools may be measuring the wrong thing or missing an entire influence channel that isn't being credited, and he explicitly asks someone in the research space to investigate this gap.

> "things I've used to describe the brand on podcasts"

**Evidence:** Rand's own repeated observation: SparkToro's phrasing in AI Overview/ChatGPT/Claude answers matches language he has specifically used on podcasts, but podcasts never appear as the listed citation source; contradictory industry data cited in the same conversation (an Adweek article claiming YouTube is the most-cited AI source vs. other studies claiming it's cited less than reported).

**Apply at Pabau:** David shouldn't fully trust AI-citation-tracking tools/reports as a complete picture of what's shaping AI answers about Pabau — podcast and video appearances may be influencing AI phrasing about Pabau even when they never show up as a tracked citation, so podcast/video PR may be undervalued by citation-only measurement.

**Apply anywhere:** You shouldn't fully trust AI-citation-tracking tools/reports as a complete picture of what's shaping AI answers about your site — podcast and video appearances may be influencing AI phrasing about your site even when they never show up as a tracked citation, so podcast/video PR may be undervalued by citation-only measurement.

### 10. AI answers finish explanation jobs, not proof, personalization or action jobs  `66.3`
*core · content insights · source 66*

The framework's underlying mechanism for why some content survives AI answers and some does not is a claim about user need, not content quality. AI answers are much more likely to fully satisfy the user's need when they only want a quick explanation, and much less likely when they still need proof, current or personalized data, a meaningful comparison, context-specific guidance, or somewhere to complete the next action. That gives a testable dividing line: the split is not between good and bad content but between content whose job an AI answer can finish and content whose job still requires the site itself. A well-written explainer and a badly-written explainer are equally exposed, because the exposure comes from the job, not the execution — which is why lengthening or retitling an explainer does not change its outlook.

> "AI answers are much more likely to fully satisfy the user's need when they only want a quick explanation"

**Evidence:** The framework is built on the distinction that AI answers 'are much more likely to fully satisfy the user's need when they only want a quick explanation, and less likely when they still need proof, current or personalized data, a meaningful comparison, context specific guidance, or somewhere to complete the next action' — and the twenty-one scored content types sort cleanly along exactly that line, with every High click-resilience type requiring proof, live data, personalization or an action.

**Apply:** For each Pabau page, name the user job in one word — explain, prove, personalize, or act. Explain-only pages are the exposed set and need original evidence or a tool added to survive; prove, personalize and act pages are already defensible and deserve the investment.

### 11. AI judges realness and community activity, not DA or traffic  `30.3`
*core · content insights · source 30*

Ellen argues that AI systems answering local queries can't access domain authority, website traffic, or other 'hard' SEO metrics at all, so they instead infer legitimacy from proxies: is this a real business in a real place, is it actively connected to other local businesses and organizations, is it sponsoring things, is it posting on social media. This reframes what a 'good' signal is for AI visibility specifically — a local business sponsoring a local nonprofit reads as a completely natural, unforced signal precisely because it's a real-world action AI can detect evidence of, rather than an engineered SEO signal.

> "AI doesn't see domain authority, doesn't see website traffic"

**Evidence:** "AI doesn't see domain authority, doesn't see website traffic, doesn't see those hard metrics, it just doesn't have access to them... So instead, it looks for: is this a real business in a real place, really active in the community?"

**Apply at Pabau:** For Pabau, AI-answer visibility may hinge less on classic authority metrics and more on detectable signals of being a real, active, connected organization — trade-association memberships, conference sponsorships, real named case studies, and social/community activity — which suggests these should be treated as AI-visibility investments, not just brand-marketing nice-to-haves.

**Apply anywhere:** For your site, AI-answer visibility may hinge less on classic authority metrics and more on detectable signals of being a real, active, connected organization — trade-association memberships, conference sponsorships, real named case studies, and social/community activity — which suggests these should be treated as AI-visibility investments, not just brand-marketing nice-to-haves.

### 12. AI now shapes six-figure B2B software buying decisions, unverified  `19.13`
*core · content insights · source 19*

Drawing on a recent G2 report about how people make software-purchasing decisions, Kaleigh's newsletter research found that AI has changed buyer behavior so much that many buyers now make purchasing choices based on what an AI recommends without fact-checking that recommendation themselves. At the same time, the evaluation phase, not awareness or consideration, is now described as the longest part of the B2B buyer journey, because a CFO typically has to get involved, a stronger budget case has to be built, and the purchase has to be justified on ROI with attribution, all of which is described as genuinely hard to track. The context given is buyers deciding what software to spend around $100,000 on, meaning real enterprise-level SaaS purchase decisions, not small self-serve buys.

> "so many people make choices based on what the AI recommends"

**Evidence:** Reference to a specific G2 report, the subject of Kaleigh's most recent newsletter at time of recording, on how AI is changing software-purchasing decisions, and her framing of the research question as "how people decide what software to spend $100,000 on in 2026."

**Apply at Pabau:** Because buyers reportedly act on AI software recommendations without independently fact-checking them, and because the CFO-driven evaluation phase is now the longest, most ROI-scrutinized part of the buying journey, Pabau should treat being the AI's cited or recommended answer for relevant practice-management-software queries as directly tied to revenue, and should build content that pre-answers the CFO's ROI and attribution questions rather than only targeting earlier-funnel awareness queries.

**Apply anywhere:** Because buyers reportedly act on AI software recommendations without independently fact-checking them, and because the CFO-driven evaluation phase is now the longest, most ROI-scrutinized part of the buying journey, treat being the AI's cited or recommended answer for your category's queries as directly tied to revenue, and build content that pre-answers the CFO's ROI and attribution questions rather than only targeting earlier-funnel awareness queries.

### 13. AI passage-ranking rewards narrow, specific documents over broad ones  `29.6`
*core · content insights · source 29*

Hank's current highest-value content architecture change is more granular segmentation: instead of one large page covering a major topic, break it into multiple narrower, single-subtopic pages. The reasoning is mechanical - passage-ranking systems (used by AI Overviews and answer engines) no longer evaluate a whole document when constructing an answer; they slice every competing document into passages and reassemble pieces from many sources into one answer. That means the narrower and more concretely-worded a section of content is, the easier it is for the system to lift as a clean, unambiguous citation, whereas broad or abstract language dilutes a passage's usefulness.

> "the AI is no longer looking at your entire document"

**Evidence:** Hank's own tested observation across his consulting clients and personal site: segmenting one big topic page into multiple narrow subtopic pages 'works really well right now,' explained by how passage-ranking systems slice every competing document into pieces and reassemble them into an answer rather than reading one document in full.

**Apply at Pabau:** Restructure Pabau's long guide-style pages into a hub page plus a cluster of narrow, single-subtopic pages, and write each section in concrete, specific language rather than abstract topic sentences, so AI answer engines can lift a clean, self-contained passage as a citation.

**Apply anywhere:** Restructure your long guide-style pages into a hub page plus a cluster of narrow, single-subtopic pages, and write each section in concrete, specific language rather than abstract topic sentences, so AI answer engines can lift a clean, self-contained passage as a citation.

### 14. AI traffic converts at two to three times organic - because it arrives pre-sold  `60.1`
*core · content insights · source 60*

Joe Davies, founder of FATJOE, reports that click volume from AI surfaces is going exponentially higher month over month across his own site and client data, while still being tiny compared to Google - 'it's still really a tiny baby'. The number that matters is the conversion rate: two to three times traditional search. His explanation is that the visitor has already had a conversation with what amounts to a consultant before arriving, so they know you're the right option, they have context about your brand, and they purchase much faster. Cody's data agrees, with a qualification that sharpens it: the effect is strongest where the purchase decision has a long horizon and involves comparison research - software, exactly - and much weaker for transactional purchases like a pair of shoes. Joe's own worked example is buying a MacBook by asking ChatGPT questions back and forth, which he found better than Googling or reading blog posts because it was an assistant telling him what he needed.

> "click trends are already going exponentially"

**How to do it**

1. Segment AI referral traffic (ChatGPT, Perplexity, Copilot) separately in analytics rather than lumping it into referral or direct.
2. Compare its conversion rate against organic search rather than its volume - the volume comparison will make you dismiss it.
3. Judge the opportunity by your purchase cycle: long, research-heavy, comparison-driven decisions benefit most.
4. Expect the absolute numbers to stay small for now and plan on the trend rather than the current total.
5. For transactional or commodity purchases, don't over-invest yet - both hosts say the effect is much weaker there.

**Tools:** Google Analytics 4

**Pitfall:** Most of the AI visibility signal is not clicks at all - Joe notes much of it is visibility rather than traffic, so measuring only clicks understates the channel while measuring only visibility overstates it.

**Apply at Pabau:** Pabau's buying cycle is exactly the research-heavy comparison type Joe describes, so AI referral traffic should be segmented and judged on demo requests per session, not on session count - it will be small and disproportionately valuable.

**Apply anywhere:** If your buying cycle is the research-heavy comparison type, segment AI referral traffic and judge it on conversions per session rather than session count - it will be small and disproportionately valuable.

### 15. AI visibility is outbound link building against existing citations  `56.14`
*core · concrete actions · source 56*

Cody's position on generative engine optimisation is that the industry overcomplicates it and only one thing has mattered in what he has seen: showing up in the citations that ChatGPT or Claude are already pulling from. His method is blunt - look at the keywords you want to rank for, look at the citations the engines are using, email every one of those citation owners, and pay to get yourself added. 'Overnight you can make impact on AI SEO just by doing that.' He reframes the whole discipline: it isn't keyword research plus publishing, it's an outbound strategy, or more precisely very strategic citation link building. He says the founders he knows running competing AI-visibility companies all say the same thing: publishing on your own site does not move it if you aren't getting into the sources being cited. He also argues this is easier than traditional SEO, not harder.

> "you show up in the citations"

**How to do it**

1. List the prompts and keywords you actually want to be recommended for.
2. Run each one through the AI engines and record every URL cited in the answers.
3. Build a frequency table of citation URLs across all your prompts - the same few articles usually recur.
4. Contact the owners of the most-cited URLs and negotiate inclusion, paid if necessary.
5. Ensure the mention carries the context you want to be known for, not just the brand name.
6. Re-run the prompts after inclusion to confirm the citation is being pulled and your brand appears.
7. Treat this as an ongoing outbound programme with a pipeline, not a one-off project.

**Tools:** ChatGPT, Claude, Perplexity

**Pitfall:** He explicitly contrasts this with what he sees people do instead - elaborate private blog networks and volumes of on-site content - and calls it wasted effort if you aren't in the cited sources.

**Apply at Pabau:** For Pabau's AI visibility, the highest-leverage work is auditing which URLs the engines cite for practice-management and med-spa software queries and getting Pabau properly represented in those specific articles - not publishing more Pabau-hosted content about itself.

**Apply anywhere:** The highest-leverage AI visibility work is auditing which URLs the engines cite for your category's queries and getting properly represented in those specific articles - not publishing more of your own content about yourself.

### 16. AI-avatar fake review channels are gaming ChatGPT's citations undetected  `43.7`
*core · content insights · source 43*

Rand flags an active, working scam pattern: fully AI-generated review channels (AI avatar, AI voice, no real human) on YouTube that don't actually test or review the product — they target the keyword pattern 'brand name + review' and 'brand name + is it legit,' comment on the real product's landing page as if reviewing it, then pivot to recommend a competing product as the 'better alternative.' He states directly that ChatGPT cannot currently distinguish these fake AI-generated reviews from genuine ones and cites them as if they were real people's tested opinions, calling the pattern 'working' and noting he personally escalated it to a YouTube contact without seeing it resolved. He compares this to Google's historical 10-year lag (roughly 2008 to 2018) in fully solving earlier spam patterns, predicting AI platforms will eventually catch this too but not soon.

> "ChatGPT does not know these are fake reviews, that this is AI"

**Evidence:** Specific scam mechanic named: AI-avatar/AI-voice YouTube channels targeting '[brand] review' and '[brand] is it legit' keywords without reviewing the product, redirecting to a competing product; Rand's direct claim that ChatGPT cites these as genuine; his own escalation to a YouTube contact with no resolution; historical comparison to Google spam-fighting taking roughly 10 years (2008-2018) to mature.

**Apply at Pabau:** David should monitor for AI-avatar 'review' or 'is it legit' videos targeting the Pabau brand name on YouTube, since these can currently poison ChatGPT's perception of Pabau by citing fake negative reviews as genuine, and should have a monitoring plan (YouTube reports, an alerts tool) since AI platforms are not expected to reliably catch this pattern for years.

**Apply anywhere:** Monitor for AI-avatar 'review' or 'is it legit' videos targeting your brand name on YouTube, since these can currently poison ChatGPT's perception of your brand by citing fake negative reviews as genuine, and keep a monitoring plan in place (YouTube reports, an alerts tool) since AI platforms are not expected to reliably catch this pattern for years.

### 17. Accept that a brand-new product cannot be recommended by a language model  `89.6`
*core · general insights · source 89*

Grow and Convert reason from how the model is built. A language model learns which word sequences commonly appear together and then predicts the most probable continuation. Their illustration is asking it to complete 'A large ecommerce platform based in Canada is', which returns Shopify. The consequence they draw is blunt: if nothing has been written about your product in books or on the web, it is impossible for the model to mention you, because there is no association between your name and your category's words to reproduce. That makes new market entrants structurally invisible until third parties write about them. It also means the fix is not technical. It is getting text about you into circulation, specifically text that puts your name next to your category terms.

> "it's impossible for ChatGPT to mention you"

**Evidence:** Grow and Convert demonstrate the mechanism with the sentence completion 'A large ecommerce platform based in Canada is __' returning Shopify.

**Tools:** ChatGPT

**Pitfall:** Launching a new product and expecting schema, llms.txt or on-page tweaks to produce AI mentions. There is no corpus to tweak; the gap is coverage, and coverage takes months.

**Apply at Pabau:** When Pabau ships a new module or the Pabau GO app, assume zero AI visibility for it until third parties have written about it by name. Plan a mention-seeding push at launch rather than waiting to be discovered.

**Apply anywhere:** When you launch a new product or feature, assume zero AI visibility for it until third parties have written about it by name. Plan a mention-seeding push at launch rather than waiting to be discovered.

### 18. Add citations and mentions as new SEO KPIs  `07.2`
*core · general insights · source 07*

Beyond rankings and clicks, the creator says two new KPIs must be tracked for the AI-search era: 'getting cited' (an AI system uses your content to construct its answer) and 'getting mentioned' (an AI system names your brand even without pulling your exact text). These are presented as equally important as traditional ranking/click KPIs, not vanity metrics, because they represent visibility inside generative engines that never surface a clickable blue link. Practically, this means SEO reporting should add a citations/mentions column alongside clicks, impressions, and average position. Later in the video these become measurable via Bing Webmaster Tools' AI performance report and a brand tracker, so the KPI is trackable today, not just conceptual.

> "getting cited, which is when the AI uses your content"

**Evidence:** Creator names 'two new KPIs (key performance indicators)... getting cited... and getting mentioned' as necessary additions to the existing goal of ranking and clicks.

**Apply at Pabau:** David should add a citations/mentions tracking line to Pabau's regular SEO reporting (sourced from Bing Webmaster Tools and/or a brand-mention tool) rather than reporting on clicks and rankings alone, since a growing share of demand is now satisfied inside AI answers that never generate a click.

**Apply anywhere:** You should add a citations/mentions tracking line to your regular SEO reporting (sourced from Bing Webmaster Tools and/or a brand-mention tool) rather than reporting on clicks and rankings alone, since a growing share of demand is now satisfied inside AI answers that never generate a click.

### 19. Add relevant statistics to passages for up to 40% more visibility  `76.2`
*core · concrete actions · source 76*

The paper cites the Princeton-Georgia Tech GEO study, which tested nine optimization strategies across 10,000 queries. Adding relevant statistics improved visibility by up to 40 percent and was the single most effective intervention of the nine. Citing credible sources ranked second and including quotations from recognized authorities ranked third. Keyword stuffing, the canonical SEO tactic, showed negligible improvement. Separately the paper reports that fluency optimization alone improved passage visibility by 15 to 30 percent across query types. The authors tie this to the pairwise ranking architecture: in a head-to-head comparison the model reasons about which passage is more useful, and a passage carrying a verifiable data point, a named source or a concrete example offers something the competing passage lacks. A passage that restates widely available information in slightly different words offers no marginal value.

> "adding relevant statistics improved visibility by up to 40%"

**Evidence:** Princeton-Georgia Tech study: nine strategies tested across 10,000 queries; statistics up to +40% visibility, citations second, authority quotations third, keyword stuffing negligible. Princeton GEO study separately: fluency optimization +15-30%.

**How to do it**

1. List every claim in the draft that is currently stated without a number.
2. Attach a specific figure to each one, with the year and the source name in the same sentence.
3. Put the statistic inside the passage that needs it, not in a footnote or a stats roundup section further down.
4. Add one named-authority quotation per major section, since quotations were the third-strongest intervention.
5. Rewrite for fluency as a separate pass, worth 15-30% on its own.
6. Strip keyword repetition added for search: the study found it gave negligible improvement.
7. Re-check each passage against the competing page that currently gets cited and ask what your passage offers that theirs does not.

**Pitfall:** Collecting all the data into one 'statistics' section. Chunking then puts the numbers in a passage that answers no question, and the passages that do answer questions are left bare.

**Apply at Pabau:** Pabau's aesthetic-practice guides mostly argue qualitatively. Give each H2 one sourced figure with a year and a named source, and place it in that section rather than in a stats block.

**Apply anywhere:** Most guides argue qualitatively. Give each H2 one sourced figure with a year and a named source, and place it in that section rather than in a stats block.

### 20. Answer PAA-style fan-out questions in concise chunks  `18.10`
*core · concrete actions · source 18*

The claim is that AI Overviews and similar AI answers are built from 'little chunks of content synthesized from query fan-out' — meaning the AI expands a query into related sub-questions and pulls short, concise answers from across the web rather than reading one long article. The recommended workflow is to identify the People-Also-Ask-style sub-questions for a topic and write a concise, direct answer to each as its own addressable chunk, which the speaker says will 'consistently get pulled into AI Overviews' if done across the full set of fan-out questions. This is framed as more accessible than ever because it only requires ordinary keyword research skills (finding the fan-out questions) plus concise writing, not new tooling.

> "know the People-Also-Ask-style question, give a nice concise answer"

**How to do it**

1. Pull the People Also Ask questions and query fan-out variants for your target topic from the Google SERP or a keyword-research tool.
2. For each question, write a short, self-contained, direct answer positioned under a heading that matches the question wording. (inferred formatting mechanic)
3. State the direct answer in the first sentence after the heading, before any preamble, so it reads as an extractable standalone chunk. (inferred)
4. Cover the full set of fan-out questions/variants for the topic, not just the head question, since AI Overviews synthesize across multiple chunks.
5. Check the live SERP or an AI-Overview-tracking rank tool to see whether your pages start appearing inside AI Overviews for those queries. (inferred verification step)
6. If a chunk isn't getting picked up, tighten it further — shorter, more direct, and more closely matching the literal question phrasing.

**Pitfall:** Treating this as generic 'write good content' advice instead of first doing the specific research to find which People-Also-Ask-style fan-out questions are actually appearing for your topic.

### 21. Answer the Five Ws for every product/service page  `46.9`
*core · concrete actions · source 46*

Travis's single highest-conviction, immediately actionable AI-search tactic: make sure every product and service you sell clearly and explicitly answers the five Ws — who, what, when, where, why — somewhere in its on-page content. He argues this matters more now because AI search enables much longer, more specific, more personalized query strings than classic keyword search, so a page needs to directly answer compound multi-part questions rather than just target a short keyword. He says doing this thoroughly across a product/service catalog is enough to 'keep you and any AI agent you have busy for a decade' — a large but extremely high-leverage, never-finished content workstream.

> "the who, what, when, where, why"

**How to do it**

1. List every distinct product, module, and service sold, e.g. online booking, EPOS, marketing automation, forms, GO app.
2. For each one, draft explicit answers to who it is for, what it does, when someone would need it, where it fits in the client workflow, and why it matters.
3. Audit existing product/feature pages against this checklist and flag any page missing one or more of the five Ws explicitly in its copy, using a spreadsheet tracker with one row per page and one column per W (inferred).
4. Rewrite or add sections so each of the five Ws is answered in scannable, extractable prose that an AI system can lift as an answer, rather than only implied by marketing language.
5. Prioritize pages that already receive long, specific, multi-clause queries in Google Search Console's query report, since those are most exposed to AI-mode and AI-Overview personalized queries.
6. Treat this as a rolling, never-finished backlog and feed it to writers or an AI drafting agent once the five-W answers are mapped out per page.

**Tools:** Google Search Console

### 22. Ask every AI-sourced lead to share the chat that recommended you  `83.1`
*core · concrete actions · source 83*

Devesh at Grow and Convert says the only reason they know invisible prompts exist is that they asked customers to forward the conversations. Company after company tells them AI leads are arriving and they have no idea what was typed. Grow and Convert closed that gap by requesting the actual ChatGPT share link from leads who mention AI, then reading the literal prompt and inferring the effective prompt from how much the model already knew. One client's shared chat showed ChatGPT naming her industry, goals and constraints she never typed. That artifact is the only first-party data anyone has, because OpenAI has not released prompt data. Treat collected chats as a research corpus, not anecdotes, and mine them for the situations your content has to cover.

> "Because we've asked them to share their chats"

**Evidence:** Grow and Convert's client in the business loans and funding space shared the exact chat where ChatGPT named the agency first, which is what let them test the prompt in incognito.

**How to do it**

1. Add a required 'How did you find us?' field to the demo form with an explicit 'ChatGPT / Claude / Gemini / Perplexity' option.
2. When a lead picks an AI option, have the salesperson ask in the first reply for the ChatGPT share link to that conversation.
3. Save each shared chat to one folder with the date, the lead's industry and company size.
4. Record two columns per chat: the literal text the user typed, and every fact the model clearly knew that was never typed.
5. Tag each chat with the topic it belongs to, such as pricing, migration off a competitor, or a specific use case.
6. Review the corpus monthly and count which situations recur across chats.
7. Turn the top recurring situations into dedicated articles or case studies.
8. Re-check after publishing whether new shared chats cite your pages.

**Tools:** ChatGPT

**Pitfall:** Sales teams forget to ask, and the window closes fast because a lead will not dig out a chat two weeks after the fact. If your log has fewer than one shared chat per ten AI-sourced leads, the ask is not happening.

**Apply at Pabau:** Pabau should add an AI-source option to the demo request form and have sales ask for the share link on the first reply. Store the chats and mine them for the specific practice situations, such as a solo injector leaving paper records or a three-site clinic consolidating reporting, that should become articles.

**Apply anywhere:** Add an AI-source option to your demo or contact form and have sales ask those leads to forward the chat share link. Store the conversations, log what the model knew but the user never typed, and turn the recurring situations into content.

### 23. Audit the whole follow-up chain, not the first AI answer  `73.23`
*core · concrete actions · source 73*

Barnard calls this the AI resume, the successor to the brand SERP. On Google someone sees the knowledge panel, decides you are great, and stops - it is a single visual moment. AI changes the shape of that: ChatGPT and AI Mode actively encourage conversation, suggest follow-up questions and offer to tell the reader more about a specific topic. So the prospect goes down what he calls a due diligence rabbit hole, and you need that whole rabbit hole to represent you as you would want, all the way down, whatever anybody asks. Taking control of that is significantly harder than controlling a brand SERP. He connects it back to the panel: the knowledge panel demonstrates the AI understands you and is confident, which makes the answers it gives about you more accurate, more stable and more positive. He stresses stability specifically, warning that people see one answer and assume it is the answer everyone gets, when it may differ by person and circumstance.

> "you go down what I would call a due diligence rabbit hole"

**Evidence:** Barnard contrasts the single-glance Google knowledge panel with AI's conversational follow-ups, and argues the knowledge panel's real AI value is making those answers more stable.

**How to do it**

1. Ask an AI assistant the opening question a prospect would ask about your brand, and record the answer.
2. Click or ask every follow-up question the assistant suggests, and keep going three or four levels deep.
3. Log every claim it makes at each level and mark each as accurate, stale or wrong.
4. Trace each wrong claim to the source page or profile it likely came from, and correct that source.
5. Repeat the same chain in a fresh session and in a logged-out session, since answers vary by person and context.
6. Repeat across ChatGPT, Gemini and AI Mode rather than treating one engine's answer as the answer.
7. Re-run the chain quarterly and after any product or positioning change.

**Tools:** ChatGPT, Google AI Mode, Gemini

**Pitfall:** Checking one prompt, seeing a good answer and assuming everyone gets it. Barnard warns answers differ by person and circumstance, and the damage sits several follow-ups deep where nobody looks.

**Apply at Pabau:** Run this chain quarterly for Pabau: ask what Pabau is, then follow every suggested follow-up about pricing, competitors and suitability, and fix the source pages behind any wrong answer about gating or trials.

**Apply anywhere:** Audit the full conversation, not the first answer. Ask the opening brand question in each assistant, follow every suggested follow-up several levels deep, log wrong claims and correct the source page each one came from.

### 24. Beat high-authority competitors in AI search with scenario depth  `78.9`
*core · general insights · source 78*

Constitution Lending is a private lender competing with companies that have 80-plus domain authority, thousands of backlinks and decades of presence. Grow and Convert built their topic map by interviewing the lending experts who speak to borrowers daily, then produced content covering every specific lending scenario their ideal customers face: LLC mortgages, DSCR loans for specific property types, bridge loans for particular situations. The result was appearance in AI search results for 50-plus bottom-of-funnel prompts across ChatGPT, Perplexity and Google AI Overviews, often outranking decades-old lenders. Grow and Convert are explicit that this did not come from an llms.txt file or restructured headings. It came from detailed specific content that the models could match to user queries.

> "competing against companies with 80+ domain authority"

**Evidence:** Constitution Lending appears in AI search results for 50+ bottom-of-funnel prompts across ChatGPT, Perplexity and Google AI Overviews against 80+ DA incumbents.

**Tools:** ChatGPT, Perplexity, Traqer.ai

**Pitfall:** Concluding that authority no longer matters at all. The lever here is scenario-level specificity on queries the incumbents never wrote for, not parity on head terms.

**Apply at Pabau:** Pabau does not need to outrank large established software review sites on head terms to be recommended. Covering narrow practice scenarios competitors ignore is the faster route to AI mentions.

**Apply anywhere:** You can win AI recommendations against far stronger domains by covering narrow, specific customer scenarios they never wrote about. Authority helps, but scenario-level content is what the model matches on.
