# AI Visibility / GEO — supporting (part 1 of 3)

22 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. A chunk of apparent AI Mode queries are bots, not users  `02.5`
*useful · content insights · source 02*

When reviewing the Claude-classified list of likely AI Mode queries, a noticeable share turn out to be clearly automated queries run by tracking tools rather than genuine human searchers, mixed in among ambiguous, hard-to-interpret real queries such as 'how long does it take?' or a bare 'Yes' that only make sense with their cited landing page as context. This means any AI Mode query analysis needs a manual noise-filtering pass to separate real user behavior from SEO/AI-visibility monitoring tool traffic before drawing conclusions.

> "including some that are clearly automated via some tracking tools"

**Evidence:** 'Brace yourself, you will find some wild prompts in the data, including some that are clearly automated via some tracking tools,' alongside examples of genuinely ambiguous real queries like 'how long does it take?' and 'why is this happening?' that are only interpretable via their cited landing page.

**Apply at Pabau:** Before reporting AI Mode query volume or patterns for Pabau to stakeholders, manually review a sample of the classified output to strip out likely bot/tracking-tool queries, since automated monitoring traffic can otherwise inflate the apparent scale of genuine AI Mode usage.

**Apply anywhere:** Before reporting AI Mode query volume or patterns to stakeholders, manually review a sample of the classified output to strip out likely bot/tracking-tool queries, since automated monitoring traffic can otherwise inflate the apparent scale of genuine AI Mode usage.

### 2. AI Mode queries read as conversational follow-ups, not search terms  `02.7`
*useful · content insights · source 02*

The queries identified as likely AI Mode usage are recognizably different in form from traditional search queries: they extend a conversation, answer a chatbot's question, or are elaborate, longer prompts that would never be typed into a traditional search box, in contrast to short keyword-style queries. Reviewing this data firsthand shows people using AI Mode to dig deep into a topic and have an extended back-and-forth conversation with Google, a qualitatively different interaction pattern than a single-query traditional search session.

> "how some people are using AI Mode to dig deep"

**Evidence:** Direct observation: 'It's fascinating to see how some people are using AI Mode to dig deep, have conversations with Google via AI Mode, etc.,' following examples of elaborate prompts paired with the landing pages that ranked inside those AI Mode conversations.

**Apply at Pabau:** When writing Pabau content intended to be cited inside AI Mode conversations, anticipate follow-up-style questions on the same topic (not just the initial head-term query) and ensure the page or surrounding content can answer likely follow-ups, since AI Mode usage is shown here to be multi-turn rather than single-query.

**Apply anywhere:** When writing your content intended to be cited inside AI Mode conversations, anticipate follow-up-style questions on the same topic (not just the initial head-term query) and ensure the page or surrounding content can answer likely follow-ups, since AI Mode usage is shown here to be multi-turn rather than single-query.

### 3. AI Overviews deep-link to the exact section that answers the query  `79.12`
*useful · content insights · source 79*

Grow & Convert show a Google AI Overview naming their client Insider as one of the best customer data platforms, citing and linking the article they published on Insider's site. The detail they highlight is what the link does: clicking it does not just open the page, it scrolls down and highlights the specific section discussing the five best enterprise CDPs, where Insider is named first and the platform is discussed in detail. That is Google's scroll-to-text behaviour applied to AI Overview citations. The practical reading is that the unit being cited is a section, not a page, so the section that answers the query needs to stand alone: name the entity, state the specifics, and make it readable without the paragraphs above it.

> "it scrolls down and highlights the section"

**Evidence:** Google AI Overview named Insider among the best CDPs and deep-linked with scroll-and-highlight into the five-best-enterprise-CDPs section of the article.

**Pitfall:** A section written to depend on context set earlier in the article reads as a fragment when a user lands directly on it, which wastes the one visit the citation earns.

**Apply at Pabau:** Every section of a Pabau listicle or comparison page should work as a cold landing point: name the product, restate what it does, and carry the pricing and specifics locally rather than referring back to an earlier section.

**Apply anywhere:** Write every section of a listicle or comparison page to work as a cold landing point, restating the product and carrying its specifics locally rather than referring back.

### 4. AI search agents run multiple queries per question  `27.1`
*useful · content insights · source 27*

When an LLM-based agent (e.g., ChatGPT) answers a question, it doesn't run one search — it performs a "query fan-out," firing anywhere from one to three, sometimes as many as eight or more, separate search queries depending on the mode, and it can go far wider and deeper than a person because it doesn't get tired of searching. Custom agents built on top of the base model can further control this: how many times it fans out, how deep it searches, and even give it explicit scraping instructions like "ignore this kind of content." The speaker predicts this filtering capability will increasingly let people, and eventually platforms, instruct search agents to exclude gray-hat or black-hat content from what gets surfaced and cited, changing which sites qualify as usable sources for AI answers.

> "one to three, sometimes as many as eight searches"

**Evidence:** Andrew Melnichuk Osine, who builds SEO agent tooling, states query fan-out ranges "one to three, sometimes as many as eight" searches per question depending on mode, and describes custom agents that can be given explicit content-filtering instructions during the scraping step.

**Apply at Pabau:** Since AI answer engines effectively multiply a single user question into several underlying searches, David should audit Pabau's content against the broader cluster of related queries a topic could fan out into, not just the primary target keyword, and assume sites carrying spam/manipulation signals may get programmatically filtered out of agent-driven research going forward.

**Apply anywhere:** Since AI answer engines effectively multiply a single user question into several underlying searches, you should audit your content against the broader cluster of related queries a topic could fan out into, not just the primary target keyword, and assume sites carrying spam/manipulation signals may get programmatically filtered out of agent-driven research going forward.

### 5. AI search compresses the evaluation journey your website used to run  `86.15`
*useful · content insights · source 86*

Grow & Convert draw a clean before-and-after. In traditional search you rank for a keyword, the user clicks through, and your page does the selling: they read the content, browse the site, look at pricing, check a case study, then decide. In AI search that whole sequence gets compressed. The model reads your content and your competitors', synthesizes it, and hands the user a recommendation in its own wording. The screenshots they cite show ChatGPT writing its own bullets selling ClickUp and Asana. The consequence is that the evaluation work your site used to perform now happens inside the model, using only what your content said. Anything you communicate through site navigation, pricing pages the model did not read, or a sales conversation later, is not part of the pitch it delivers.

> "Your content has become your sales pitch, delivered by AI"

**Evidence:** Grow & Convert's observation of ChatGPT writing its own selling bullets for ClickUp and Asana in response to a project management software prompt.

**Tools:** ChatGPT

**Pitfall:** Teams keep the differentiators spread across separate pages, assuming a visitor will assemble them by browsing. The model does not browse; it summarizes the page it retrieved.

**Apply at Pabau:** Any Pabau page that can rank for a commercial query must carry the whole pitch on the page itself: who it is for, the problem, the differentiator and proof. Pabau cannot rely on a reader clicking through to the pricing or features pages.

**Apply anywhere:** Any page that can rank for a commercial query must carry the whole pitch on the page itself: who it is for, the problem, the differentiator and proof. Don't rely on the reader clicking through to your pricing or features pages.

### 6. AI use is K-shaped: a small minority drives most usage  `43.12`
*useful · content insights · source 43*

Rand describes AI usage as following a 'K-shaped' distribution, borrowing the term from post-COVID US economic analysis. Citing data from Datos, he states roughly 20% of people use AI tools heavily while the remaining 80% of devices in the panel show only one or two visits per month, sometimes fewer, and critically, many of even those rare visits aren't the person actually prompting the AI themselves but someone else's shared AI response being viewed — he states roughly half of all observed ChatGPT visits are exactly this. He extends this to predict businesses will likely keep adopting/investing in AI even if consumer trust and usage stays flat or declines (per Morning Consult data placing AI among the least-trusted, most negatively perceived categories they measure), because the heavy-usage minority alone can sustain the business case.

> "Half the ChatGPT visits we see are someone sharing a response"

**Evidence:** Datos data cited: roughly 20% of users are heavy AI users while about 80% of devices show only one or two AI visits per month; roughly half of observed ChatGPT visits are someone viewing a shared response rather than prompting it themselves; Morning Consult data placing AI among the least-trusted, most negatively perceived categories they track.

**Apply at Pabau:** David should not assume broad, even AI adoption across Pabau's entire buyer base when planning GEO/AI-visibility strategy — a heavy-using minority likely drives most AI-assisted research, and a meaningful share of AI-answer exposure happens via someone else's shared response rather than the buyer's own prompt, which affects how attribution should be modeled.

**Apply anywhere:** You should not assume broad, even AI adoption across your entire buyer base when planning GEO/AI-visibility strategy — a heavy-using minority likely drives most AI-assisted research, and a meaningful share of AI-answer exposure happens via someone else's shared response rather than the buyer's own prompt, which affects how attribution should be modeled.

### 7. Assume ChatGPT runs server-side searches you cannot observe  `87.15`
*useful · general insights · source 87*

Grow and Convert offer three theories for the 60% of citations that trace to no visible fan-out SERP. The first is that the fan-out queries visible in the browser are only part of the picture: OpenAI likely distributes additional searches across servers, using different engines and query variations, because doing all of it sequentially in the browser would make responses painfully slow. They credit QueryBurst's documentation of this. The second is response caching, since OpenAI offers developers discounts for cached responses, though they note documented cache lifetimes of 5-10 minutes undercut caching as an explanation for years-old titles. The third is training-data memorization. The practical consequence is that the fan-out queries you can scrape are an incomplete and possibly unrepresentative sample of what the model actually searched.

> "running different query variations"

**Evidence:** OpenAI documents cache lifetimes of 5-10 minutes, sometimes up to an hour, which cannot explain multi-year-old cited titles.

**Pitfall:** Treating the visible fan-out list as the complete retrieval set and optimizing exclusively against it.

**Apply at Pabau:** Any Pabau tool that scrapes visible fan-out queries should be labeled as a partial sample in reporting, not as the query set ChatGPT used.

**Apply anywhere:** Label scraped fan-out queries as a partial sample. The engine runs additional searches server-side that you never see.

### 8. Assume roughly 17% of buying prompts never trigger a web search  `87.8`
*useful · content insights · source 87*

Grow and Convert report that of the 100 buying-intent prompts they tested, 83 triggered a web search. That leaves 17% answered purely from the model's parameters, with no live retrieval at all. They frame the 80%-plus figure as supporting the case that search still matters for product prompts, but the inverse matters just as much for planning. For roughly one prompt in six, nothing you do to your live pages can influence the answer in that session. The only routes into those answers are training data and whatever the model already holds about your brand. This is part of why they argue against per-prompt content targeting, and part of why they push being present on the open web ahead of any on-page tweak.

> "83 triggered a web search"

**Evidence:** 83 of 100 buying-intent prompts triggered a web search in the ChatGPT browser UI.

**Tools:** ChatGPT

**Pitfall:** Promising a client that a page fix will change an answer. If that prompt is in the no-search 17%, the answer will not move regardless.

**Apply at Pabau:** When Pabau's team checks whether an article changed an AI answer, first confirm the prompt triggered a search. If it did not, the article was never in play.

**Apply anywhere:** Before testing whether a page change moved an AI answer, confirm the prompt triggered a web search at all. Roughly one in six buying prompts does not.

### 9. Audit tracked prompts for business value before funding a topic  `85.9`
*useful · concrete actions · source 85*

Among the outcomes Grow and Convert attribute to brand-level visibility reporting is a focus on ranking for prompts that have little to no business value, and resources wasted on activities with no real impact on lead generation or revenue. A blended percentage rewards any prompt that is easy to appear for, so a basket quietly fills with low-value phrasings that lift the average. Topic-level reporting exposes this because each topic has to be named, and a named topic with no commercial story is obvious in a review. The practical step is a periodic prune of the prompt set against commercial intent, done before the next quarter's content budget is allocated to whichever topics look weakest.

> "A focus on "ranking" for prompts that have little to no business value"

**Evidence:** Grow and Convert list wasted resources and no-business-value prompts as direct outcomes of brand-level visibility reporting.

**How to do it**

1. List every tracked topic and write one sentence on which deal or signup it plausibly precedes.
2. Cut any topic where that sentence is not writable, and log why so it is not re-added next quarter.
3. For the survivors, check the prompts inside each basket still match the topic and are phrased the way a buyer would ask.
4. Flag baskets that are easy wins with no commercial edge, for example pure definition prompts, and stop counting them toward the headline.
5. Allocate the quarter's content budget only to surviving topics in the low and medium bands.
6. Re-run this prune every quarter, immediately before budgeting, not after.

**Pitfall:** Cutting a topic because it currently converts nothing, when it is early-funnel and the tracking is the only evidence you would ever get. Keep those but score them in a separate list rather than deleting them.

**Apply at Pabau:** Pabau should prune its tracked prompt set each quarter, keeping topics that precede a demo request, such as clinic scheduling software comparisons, and demoting pure definitional prompts to a separate low-priority list.

**Apply anywhere:** Prune your tracked prompt set each quarter. Keep topics that plausibly precede a purchase and demote pure definitional prompts to a separate low-priority list.

### 10. Audit visibility across all three layers of the Algorithmic Trinity  `76.13`
*useful · best practices · source 76*

The paper adopts Jason Barnard's 'Algorithmic Trinity' as the frame for why single-channel AI visibility work fails. Three interdependent systems produce an answer. Large language models are the synthesis layer, and they do not independently verify claims; they reason over the passages assembled in their context window. Search engines are the retrieval layer, surfacing candidate documents and passages through retrieval calls without generating answers. Knowledge graphs are the validation layer, a structured database of entity nodes and relationships describing what entities exist, their attributes and their relations. The authors' conclusion is that a brand must be legible across all three: its content must be retrievable, its passages must be extractable, and the brand itself must exist as a recognizable entity whose claims can be validated against external signals. That yields two parallel imperatives, LLM readability and brand context, which cannot substitute for each other.

> "it must be legible across all three systems of the Algorithmic Trinity"

**Evidence:** Jason Barnard of Kalicube's framework as presented in the paper: LLMs synthesize, search engines retrieve, knowledge graphs validate.

**How to do it**

1. Split your AI-visibility backlog into three columns: retrievable, extractable, validatable.
2. Under retrievable, check crawlability, indexation and whether you rank at all for the sub-queries in scope.
3. Under extractable, check that passages are self-contained, dense and headed by the question they answer.
4. Under validatable, check the entity exists in the Knowledge Graph with a consistent description across third-party sources.
5. Find the weakest column and fix that first, since the paper's point is that strength in one does not compensate for absence in another.
6. Re-run the audit after any brand change, since the validation layer is where stale facts do the damage.

**Pitfall:** Teams that already do good SEO fix the retrieval column repeatedly and never touch validation, so well-ranked content is still passed over because the entity behind it is not recognized.

**Apply at Pabau:** Pabau likely scores well on retrieval and weakest on validation. Run the three-column audit and put the next quarter's effort into entity recognition rather than more content.

**Apply anywhere:** Most competent SEO teams score well on retrieval and weakest on validation. Run the three-column audit and spend the next quarter on entity recognition rather than more content.

### 11. Big brands are losing the AI-visibility race to small technical teams  `35.8`
*useful · general insights · source 35*

Charles claims that although 'AI SEO is now probably having more budget thrown at it than SEO is,' large brands investing heavily to gain scope/visibility inside AI models have largely failed to achieve it, because they don't understand the underlying algorithms the way power users do — people actually reading research papers and interacting with model engineers directly (e.g., on X). He attributes this gap to most agencies, CMOs, and campaign managers not understanding the underlying technology, which causes large amounts of AI-marketing budget to be spent on things that produce no measurable or lasting result, such as mass content-generation software applied with no regard for keyword cannibalization or brand tone.

> "big brands that have put a lot of investment"

**Evidence:** Direct claim: 'The big brands that have put a lot of investment into trying to achieve scope within the AI models haven't been able to achieve it, because they don't understand the algorithms the way the people who are interacting as power users with the AI models day to day do.' Supporting example: mass-produced blogging software criticized publicly (cited: 'Gagan' on X) for ignoring cannibalization and brand tone.

**Apply at Pabau:** Pabau's content team can compete for AI visibility against larger, better-funded competitors by building genuine technical understanding of how models retrieve and weight sources (co-occurrence, Reddit, structured trust signals) rather than assuming a bigger content budget or more agency headcount wins by default.

**Apply anywhere:** Your content team can compete for AI visibility against larger, better-funded competitors by building genuine technical understanding of how models retrieve and weight sources (co-occurrence, Reddit, structured trust signals) rather than assuming a bigger content budget or more agency headcount wins by default.

### 12. Build a branded exact-match reviews domain to win AI Overview citations  `08.9`
*useful · concrete actions · source 08*

Registering an exact-match domain combining a brand name with 'reviews' (e.g., '[brand]reviews.com') and building it into a dedicated site aggregating the brand's genuine reviews is reported to get cited directly in AI Overviews and rank number one for '[brand name] reviews' queries. The approach can be extended with a second exact-match 'executive summary' domain, or separate micro-sites segmented by review source or customer profile, each linked from the parent site. The stated reason this works is that LLMs are sometimes out of date on third-party platforms' actual review counts (e.g., not reflecting a brand's true current Facebook review total), so an always-current, brand-owned aggregator can fill that gap and become the source the AI cites.

> "getting cited in the AI Overview and ranking number one"

**How to do it**

1. Register an exact-match domain combining your brand name with 'reviews' (e.g., '[brandname]reviews.com').
2. Build a dedicated site on that domain that aggregates your genuine reviews pulled from every relevant third-party platform.
3. Structure the site with a separate page or tab per review source (e.g., a Google reviews tab, a Facebook reviews tab) so both users and LLMs can quickly find the full current picture.
4. Keep the review counts and content on this site current, since third-party platforms' actual figures are sometimes outdated in what LLMs have indexed.
5. Optionally add a second exact-match 'executive summary' domain, or separate micro-sites segmented by customer profile, each linked back from the parent site.
6. Link to these review-domain assets from your main site's navigation or footer so both crawlers and users can discover them.
7. Periodically query brand-name-plus-reviews prompts in ChatGPT/AI Overviews to confirm the new domain is being surfaced and cited. (inferred verification step)

### 13. Build a one-page topic visibility view executives can read unaided  `85.6`
*useful · concrete actions · source 85*

Grow and Convert's reporting artifact is a single page listing every topic with its own visibility figure, shared directly with executives or clients. In the Mirascope case it takes one glance to see the brand performs well for prompt engineering tools and has work to do for context engineering platform, across 65 tracked prompts. Nobody has to dig through reports or click elsewhere. The design constraint is that the page has to answer two executive questions without a follow-up meeting: where are we strong and where should the next content budget go. Their claim is that a single blended percentage answers neither, and they call brand-level percentages a lazy way to assess GEO performance.

> "This page is what marketing teams can share directly with executives"

**Evidence:** Grow and Convert report Mirascope's topic visibility across 65 prompts on a single shareable Traqer page.

**How to do it**

1. List every topic as a row, with the topic name in the words the business already uses, not the prompt text.
2. Show each topic's visibility percentage and the number of prompts behind it, so a small basket is visibly small.
3. Sort rows by visibility descending so the gaps sit together at the bottom.
4. Add a delta column against the same frozen prompt basket last period.
5. Add one column naming the action currently funded for that topic, or leave it blank to show nothing is funded.
6. Keep the whole thing to one screen and link out to per-prompt detail rather than including it.
7. Send the same page every period so the format itself is not a variable.

**Tools:** Traqer

**Pitfall:** A topic row backed by two or three prompts swings wildly and reads as volatility. Show the prompt count on every row and treat baskets under roughly ten prompts as indicative only.

**Apply at Pabau:** Pabau's GEO report to leadership should be one page of topic rows covering the product's real categories, each with its prompt count and the content currently commissioned for it.

**Apply anywhere:** Make your GEO report to leadership one page of topic rows covering your real product categories, each with its prompt count and the content currently commissioned for it.

### 14. Build crawl paths into Common Crawl for AI training data  `20.12`
*useful · concrete actions · source 20*

To improve a brand's odds of being included in AI model training data, the recommended diagnostic is checking a domain's actual presence and crawl frequency within Common Crawl, described as one of the largest data sources used for AI training. Where a site's pages are under-represented, the tactic is to build more 'crawl paths' leading from pages already known to be in Common Crawl to your own pages — two named examples are link drops on Wikipedia and building links from other pages confirmed to already be in the Common Crawl dataset. The speaker is explicit this approach is still experimental and unproven, but flags it as likely to become a significant future battleground.

> "look at their presence in the Common Crawl"

**How to do it**

1. Check whether your target domain/pages appear in the Common Crawl dataset (via Common Crawl's public index) and note how frequently they're being crawled.
2. If coverage is thin, identify pages that are already confirmed to be well-represented in Common Crawl (larger, frequently-crawled sites/pages).
3. Build links from those confirmed-crawled pages to your target pages, creating a 'crawl path' Common Crawl's own crawler is more likely to follow.
4. Consider adding relevant, legitimate link drops on Wikipedia pages as one specific tactic, where genuinely appropriate to the article's content.
5. Re-check your Common Crawl presence periodically after implementing new crawl paths to see whether coverage/frequency improves.
6. Treat this as an experimental, unproven tactic rather than a guaranteed lever, and track it as a distinct workstream from live AI-citation optimization.

**Tools:** Common Crawl

### 15. Case study: gaming an AI Overview with an AI-built EMD  `10.13`
*useful · ai workflows · source 10*

As a live demonstration that Google's AI Overviews perform little to no fact-arbitration, Charles built seoawards.org, an exact-match domain site that was entirely AI-generated: he wrote one sentence describing invented judges and details, then had Claude Code build the entire site using his own pre-built skill files. He created a matching Wikipedia page formatted the way AI Overviews prefers, seeded a Reddit thread, and asked two people to publish posts on their own separate sites mentioning, but deliberately not linking to, the brand, purely to reinforce the entity through consensus and corroboration across independent domains. He built zero backlinks to the site at all, relying only on an indexing tool to get it indexed naturally; within three days the EMD ranked number one organically for the low-competition, roughly 300-volume query "SEO Awards," and Google's AI Overview stated it was the most prestigious awards show in SEO with real judges, before Google manually reversed the ranking days later.

> "Within three days, we were number one, organically, for"

**How to do it**

1. Register an exact-match domain for a low-competition query relevant to the topic you want AI Overviews to associate with your brand.
2. Write a single descriptive prompt covering the site's premise and invented specifics, and feed it to an AI coding agent such as Claude Code, using pre-built skill files, to generate the entire site.
3. Create a matching Wikipedia-style entity page structured in the format AI Overviews prefers for entities (inferred: this step carries real notability and sourcing risk on Wikipedia specifically, see pitfall).
4. Seed a public discussion thread, such as on Reddit, referencing the new entity.
5. Ask a small number of independent third parties to publish posts on their own separate sites that mention the brand or entity by name.
6. Explicitly instruct those third parties not to link to the new site, using mentions only, to avoid tripping artificial-link detection.
7. Submit the new site for indexing via an indexing tool rather than building any backlinks to it.
8. Monitor rankings and AI Overview citations daily to see how quickly the entity gets picked up and cited.
9. Expect and prepare for manual reversal by Google if the pattern is detected, treating any resulting ranking as temporary (inferred risk-management step).

**Tools:** Claude Code, an indexing tool, Reddit, Wikipedia

**Pitfall:** This got manually reversed by Google within days, and Charles deliberately avoided building any links because Google's engineers would likely flag them as artificial and could penalize the linking sites out of spite; this is a fabricated-entity manipulation tactic with real penalty and brand-safety risk, not a sustainable strategy for an established company.

### 16. Categorize prompts by funnel stage before you read a citation report  `84.5`
*useful · concrete actions · source 84*

Grow & Convert split their 120 prompts into three funnel stages before counting citations, and the definitions are worth copying because they are behavioral rather than intuitive. Bottom-of-funnel prompts explicitly ask for recommendations or a list of options, for example 'What are the top project management tools for marketers?'. Mid-funnel prompts are about products but invite evaluation or education rather than a direct recommendation, for example 'How can I improve efficiency in my bulk hauling operations using software?'. Top-of-funnel prompts do not reference products at all, for example 'Are there any online jobs for moms who want to work from home part-time?'. Their split was 72 bottom-of-funnel, 28 mid-funnel and 20 top-of-funnel, roughly 60/23/17. Without this split you cannot tell whether a general-site citation share is a category property or an artifact of which prompts you happened to test.

> "Prompts that don't reference products at all"

**Evidence:** Grow & Convert's 120 prompts split 72/28/20; general-site share was ~18% top-of-funnel, ~11% mid, ~14% bottom.

**How to do it**

1. Write your prompt set the way buyers phrase questions, not as keywords.
2. Tag any prompt that asks for a recommendation or a list of options as bottom-of-funnel.
3. Tag any prompt that discusses products but asks how to evaluate or improve as mid-funnel.
4. Tag any prompt that never mentions a product category as top-of-funnel.
5. Aim for a bottom-heavy mix, around 60% bottom, 23% mid, 17% top, so the set reflects commercial intent.
6. Run the citation count separately per stage.
7. Compare the general-site share across the three stages before concluding anything about your category.

**Tools:** Traqer

**Pitfall:** A prompt set skewed to top-of-funnel inflates the general-site share and makes Reddit and Wikipedia look more important to your category than they are.

**Apply at Pabau:** When Pabau builds its GEO prompt basket, keep it around 60% bottom-of-funnel questions like 'best clinic software for injectables' so the citation report reflects buying moments, not browsing ones.

**Apply anywhere:** Split your prompt set into recommendation, evaluation and no-product-mention tiers before counting citations, and keep it bottom-heavy so the report reflects buying intent.

### 17. Check whether an AI answer was grounded before drawing conclusions from it  `79.11`
*useful · concrete actions · source 79*

Grow & Convert give two clues for telling whether a ChatGPT response was grounded in a live web search rather than produced from training data. First, ChatGPT literally says 'Searching the web…' and often shows the query it is running. Second, if the response includes citations, it used web search. They note OpenAI's own search help page says ChatGPT searches whenever it believes an answer could benefit, not only when the user clicks Search, and that product-recommendation prompts usually trigger it. This matters because only grounded answers are influenceable through ranking. Google AI Overviews and Perplexity are described as pure web-search summarizers, so they are grounded by definition. An ungrounded ChatGPT answer that omits you tells you about training data, which the AI companies do not disclose and you cannot reliably influence.

> "ChatGPT will literally say"

**Evidence:** OpenAI's ChatGPT search help page states it searches whenever an answer could benefit; the authors observe product-recommendation prompts usually trigger a search.

**How to do it**

1. When testing a prompt in ChatGPT, watch for the 'Searching the web…' indicator and note the query it runs.
2. Check whether the answer carries citations; citations mean the answer was grounded.
3. Log each test result as grounded or ungrounded alongside the mention outcome.
4. Base your ranking and outreach work only on the grounded results.
5. Treat ungrounded misses as unactionable rather than as a content problem to fix.
6. Note the search queries ChatGPT ran, since those are the phrasings worth ranking for.
7. Cross-check the same prompt in Google AI Overview and Perplexity, which are always grounded.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Teams rewrite pages in response to an ungrounded answer that never touched the web. The signal is a miss with no citations and no search indicator.

**Apply at Pabau:** When David or the team spot-checks Pabau in ChatGPT, record whether the answer was grounded. Only grounded misses justify changing a page or adding an outreach target.

**Apply anywhere:** When you spot-check your brand in ChatGPT, record whether the answer was grounded. Only grounded misses justify changing a page or adding an outreach target.

### 18. Choose owned content because it is the channel you can actually execute  `79.9`
*useful · general insights · source 79*

Grow & Convert's execution argument, separate from their mechanism argument, is about organizational capability. Most companies, if pressed, could produce a blog post for each of their top three SEO keywords this month. They know who would write it, roughly what it costs and what the finished piece looks like. Ask the same company to get Reddit mentions or land a feature in a top industry publication and most have never done it, have no internal know-how and no vendor relationships. Hiring a PR agency does not solve it either, because the same team cannot vet the agency or judge whether the work is producing anything. They estimate it could take a year to figure out, a year you could have spent publishing and ranking for your key bottom-of-funnel terms while LLMs discover you. They are explicit that digital PR is not a bad strategy, only that it comes second.

> "It could take you a year to figure it out"

**Evidence:** Grow & Convert's observation across client organizations: content production capability exists in-house, PR capability usually does not.

**Pitfall:** Buying digital PR before you can evaluate it means paying for activity you cannot audit, and the lost year is the real cost, not the retainer.

**Apply at Pabau:** Pabau already has a working article pipeline, so the cheapest GEO gain is more good bottom-of-funnel articles rather than standing up a PR function. David should defer PR spend until the commercial page set is ranking.

**Apply anywhere:** If your team can already publish articles but has never landed press, spend first where you have capability. Defer PR spend until your commercial pages are ranking.

### 19. Citation potential rests on primary information, not on quality of writing  `66.7`
*useful · content insights · source 66*

Citation potential in this framework has a specific definition: how likely the page is to provide unique, verifiable, primary or well-documented information that an AI platform, publisher or another site may reference. All four qualifiers are about the provenance of the information rather than the craft of the page. A page can be the best-written article in its category and still score Low, because everything in it is available elsewhere and an AI system has no reason to reference this copy of it specifically. Conversely a plainly formatted specification table, benchmark result or dated status record scores High because it is the primary record. This is why the framework's High-citation types are documentation, first-hand tests, original research, live databases and first-party-data pages — and why comparison pages, despite high business value, score Low on citation.

> "Citation potential is how likely the page is to provide unique, verifiable, primary or well-documented information"

**Evidence:** The framework defines citation potential as unique, verifiable, primary or well-documented information 'that an AI platform, publisher, or another site may reference', and its scores follow provenance rather than craft: official documentation, first-hand product tests, original research, live first-party databases and first-party-data pages all score High, while evidence-led comparisons and selection guides — a genuinely useful, High business-value type — score Low.

**Apply at Pabau:** To make Pabau content citable, add something only Pabau holds — a measured figure, a dated policy record, a specification, an anonymized usage benchmark — rather than improving the prose. A well-written page with no primary information has no citation potential to improve.

**Apply anywhere:** To make content citable, add something only your organization holds — a measured figure, a dated policy record, a specification, an anonymized usage benchmark — rather than improving the prose. A well-written page with no primary information has no citation potential to improve.

### 20. Cover ideal and non-ideal customers so models can match specific needs  `79.14`
*useful · content insights · source 79*

Grow & Convert's first argument for owned content sitting at the base of the pyramid is control of narrative depth. On your own site you can go into detail on features, the pain points you solve, which customers are ideal versus non-ideal, and your differentiators against named competitors. This matters because ChatGPT users have conversations rather than typing short keywords, and the model looks for products that solve a specific problem rather than matching phrases or counting backlinks. To recommend you it needs to know who your product helps, how it helps them and why it works. They call this the long tail of GEO, where recommendations come through prompts so personalized to the user that no tracking or visibility tool can fully capture them. A short mention on Reddit carries none of that detail.

> "who your product helps, how it helps them, and why it works"

**Evidence:** Grow & Convert's positioning argument, supported by the Constitution Lending case where ChatGPT repeated the article's stated LTV, pre-approval and closing-speed specifics.

**Pitfall:** Pages that only describe the ideal customer give a model no basis to exclude you, so you get recommended into bad-fit conversations and filtered out of good ones by whoever was specific.

**Apply at Pabau:** Pabau's commercial pages should say plainly which practice types Pabau is built for and which it is not, alongside features and competitor differentiators. That non-ideal-customer paragraph is missing from most of the current set and is cheap to add.

**Apply anywhere:** Say plainly on your commercial pages which customers you are built for and which you are not, alongside features and competitor differentiators. The non-ideal paragraph is cheap to add and rarely present.

### 21. Expect AI visibility across several phrasings of the same category  `78.13`
*useful · general insights · source 78*

InnovationCast makes innovation management software for enterprises, and the category has several distinct use cases: crowdsourcing ideas from a large employee base, validating ideas, and scouting new technologies. Grow and Convert report that producing content across those topic areas built both an SEO presence generating qualified leads and AI visibility, and they show separate topic coverage for 'innovation portfolio management software' and for 'technology scouting software', which they describe as another slightly different way customers talk about software like theirs. The takeaway is that a category is not one topic. Customers name the same class of software several ways, and each naming is its own visibility target needing its own content.

> "another, slightly different way customers talk about software like theirs"

**Evidence:** InnovationCast show topic-level visibility for both 'innovation portfolio management software' and 'technology scouting software' after producing content across their use-case areas.

**Tools:** Traqer.ai

**Pitfall:** Assuming one category page covers the category. Alternate names for the same software class are separate topics in AI answers, and you can be visible in one and absent in the neighbouring one.

**Apply at Pabau:** Pabau should list every phrasing practices use for this software class, such as clinic management software, aesthetic EMR, med spa booking system, and treat each as a separate topic basket with its own page.

**Apply anywhere:** List every alternate name customers use for your software class and treat each as its own topic with its own content and its own tracking basket. Visibility in one phrasing does not carry to the next.

### 22. Expect app-store and Shopping categories to show low SERP overlap  `87.17`
*useful · content insights · source 87*

When Grow and Convert grouped their prompts by business type they found less variation than expected, but two categories stood out low. Physical products had the lowest overlap, which they attribute to ChatGPT tapping features like Google Shopping that their study did not cover. B2C SaaS was also weak, because those products are typically pulled from app stores rather than from the vendor's own website. The lesson is that a low fan-out overlap score does not always mean weak content. Sometimes the retrieval surface for that category simply sits outside the organic SERP you measured. Before acting on a low number, check whether your category is sourced from a marketplace, a store listing or a review platform instead.

> "Physical products had the lowest overlap"

**Evidence:** Physical products lowest overlap; B2C SaaS weak, both attributed to Shopping and app-store sourcing outside the study.

**Pitfall:** Concluding your content is failing when your category's citations actually come from an app store or Shopping feed you never measured.

**Apply at Pabau:** Pabau sells B2B software with an iOS app, so check whether App Store listings feed answers about mobile clinic apps before reading a low overlap score as a content problem.

**Apply anywhere:** Before acting on a low overlap score, check whether your category is sourced from app stores, marketplaces or review platforms rather than the organic SERP.
