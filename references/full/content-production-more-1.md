# Content Production — supporting (part 1 of 7)

22 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. "Query fan-out" is just Google's rebrand of the older "query augmentation"  `25.6`
*useful · content insights · source 25*

Koray asserts that Google's publicly-branded term 'query fan-out' (popularized at Google I/O for AI Mode/AI Overviews) is the same underlying mechanism as 'query augmentation,' the term actually used in Google's patents — the AI-era branding is new marketing language for an existing patented process, not a new mechanism. Every time Google changes how it augments/expands a query (adding related terms, contexts, sub-intents), it changes how your document should be structured to match, which is why document structure must be treated as dynamic rather than fixed. From this he derives 'query deserves a page': after augmenting a query, you must decide whether the augmented sub-topic deserves its own dedicated page, just a heading within an existing page, or merely a sentence, and that decision needs revisiting since augmentation patterns shift with core updates. He references a case study covering 14 real websites published in Search Engine Land as the source of this framework.

> "query fan-out is just a fancy term they made up"

**Evidence:** Koray's Search Engine Land case study covering 14 websites (12 named) introducing the 'query deserves a page' framework; ties the term 'query fan-out' directly to the pre-existing patent term 'query augmentation.'

**Apply at Pabau:** When restructuring Pabau content, don't assume a sub-topic automatically needs a standalone page — check current SERPs/AI Overviews for whether that augmented query cluster is being answered by dedicated pages, headings, or single sentences elsewhere, and match that granularity, re-checking after major core updates.

**Apply anywhere:** When restructuring your content, don't assume a sub-topic automatically needs a standalone page — check current SERPs/AI Overviews for whether that augmented query cluster is being answered by dedicated pages, headings, or single sentences elsewhere, and match that granularity, re-checking after major core updates.

### 2. Add AI-citation building as a third prong to content promotion  `180.4`
*useful · concrete actions · source 180*

Grow and Convert run three promotion prongs on every article rather than two. First, paid ads for short-term traffic, using both cold interest and demographic targeting and lookalike audiences built from the client's customer list or site visitors, tested across Facebook, Twitter, LinkedIn and Google Ads depending on where the audience is. Second, manual link building, but only once a piece starts ranking for its keyword, to push it onto page 1 or the top of page 1. Third, and newer, building citations from AI-referenced sources: they track which sources ChatGPT, Perplexity and Claude cite when answering queries in the client's industry, then work to get the client published on or mentioned by those same sources. They fund all of this from their own budget with no extra client spend.

> "Building Citations from AI-Referenced Sources"

**Evidence:** Grow and Convert say the combination gives a short-term traffic boost followed by long-term sustainable organic traffic that compounds across articles.

**How to do it**

1. Publish the article and start cold and lookalike paid campaigns to it on the one or two channels where the audience actually sits.
2. Build lookalikes from the customer list rather than from all site visitors, so the seed matches buyers.
3. Leave link building alone until the page is ranking somewhere for its target keyword.
4. Once it ranks, point manual links at that specific page to move it up page 1.
5. In parallel, run your key industry queries through ChatGPT, Perplexity and Claude and log every domain cited.
6. Count citations per domain and rank them to get an outreach list.
7. Pitch those domains for a mention, a listing or a contributed piece that references the client.
8. Re-run the query set monthly to see whether the client now appears and which domains carried the mention.

**Tools:** ChatGPT, Perplexity, Claude, Google Ads, LinkedIn, Facebook

**Pitfall:** Building links before the page ranks at all. Grow and Convert deliberately wait for a ranking signal, because links to a page Google has not placed yet buy little movement.

**Apply at Pabau:** Pabau blog posts get published and left alone. Add a promotion step after publication: a small paid test on LinkedIn to aesthetic practice owners, then links only once the post ranks, then outreach to the industry sites that ChatGPT cites for aesthetic software queries.

**Apply anywhere:** Promote each new article three ways: paid ads to cold and lookalike audiences for immediate traffic, manual links once the page starts ranking, and outreach to the specific domains AI engines cite for your industry queries.

### 3. Add video only when the SERP already shows a video pack  `105.4`
*useful · concrete actions · source 105*

Grow and Convert push back on the standard advice that video is needed for organic leads. Their rule is that video earns its cost only when the SERP demands it, and they name the two signals: the results page contains a video section, or every top-ranking result embeds video. Their example of a yes is 'how to set up GA4', where Google surfaces a video block, meaning a meaningful share of searchers want to watch. Their example of a no is 'CRM for small business' or 'best legal assistant software', where nothing in the top results carries video. They say nine times out of ten the SERP has no video, especially on buying-intent terms. Where the SERP is ambiguous, they substitute annotated screenshots and diagrams, which they use in their own GA4 guide.

> "If the SERP includes a section for videos or all of the top ranking"

**Evidence:** Grow and Convert report the SERP lacks video nine times out of ten, citing 'best legal assistant software' and 'CRM for small businesses' as examples with no video results, against 'how to set up GA4' which has a video section.

**How to do it**

1. Search the target keyword before scoping the article and look for a video carousel or video block in the results.
2. Open the top five ranking pages and check whether each embeds a video in the body.
3. Commission video only if the SERP shows a video block or if all five top pages embed one.
4. If neither condition holds, budget the same time into annotated screenshots, diagrams and step visuals instead.
5. If you already own a relevant video, embed it rather than commissioning a new one.
6. Place any embedded video where it does not block the answer: never above a list the reader came for.
7. On comparison and listicle pages, offer the video as an optional alternative below the visual walkthrough.
8. Re-check the SERP at the next refresh, since a video block appearing later is the trigger to add one.

**Pitfall:** Producing video by default on buying-intent pages burns budget and can push the answer below the fold. If the reader wants a quick list of options and has to scroll past a player, you have added friction to your highest-converting page.

**Apply at Pabau:** Pabau should not add video to comparison or software-category articles by default. David should check the SERP for a video block first, and otherwise invest that time in the original chart or diagram every article already needs.

**Apply anywhere:** Check the SERP for a video block and check whether the top five results embed video. Commission video only when one of those is true; otherwise put the budget into annotated screenshots and diagrams, and never place a player above the answer the reader came for.

### 4. Answer five customer questions before deciding value-prop order  `92.12`
*useful · concrete actions · source 92*

Grow and Convert explain that ranking automation and accuracy as criteria one and two was not a judgment call, it followed from answering a fixed set of questions about the customer. Who are they. Why are they translating their website. How were they doing it before. What is annoying or a pain about it. In their case the answers were concrete: a common customer type is ecommerce brands selling in multiple countries, they are constantly adding new products, every new product needs its copy translated into typically most European languages, and this was managed by humans. That is why they do not want to go into a tool and click translate over and over. Automation ranked first because the before-state was manual and repetitive. Accuracy ranked second because automatic translation means computer translation, which everyone knows sounds unnatural, so brands want a human able to check and edit. Third was translated SEO meta information so each language version is optimized. Without talking to customers you would have no idea this was the critical pain point.

> "How were they doing it before?"

**Evidence:** Grow and Convert derived the automation, accuracy, translated SEO meta ordering from extensive interviews with their client, and note there were many more pain points in the five-things section.

**How to do it**

1. Before ranking value props, answer in writing: who is the customer, why are they buying now, how were they doing it before, what is painful about that, and what happens if they do nothing.
2. Write the before-state as a concrete workflow with the frequency attached, such as translating copy every time a product is added.
3. Rank pain points by how often the painful step repeats and how manual it is; the most repeated manual step becomes criterion one.
4. For each top pain point, name the objection that comes with the obvious fix, such as machine translation sounding unnatural.
5. Make the answer to that objection the next criterion down the list, as accuracy follows automation.
6. Check for downstream pains the buyer only meets later, such as needing translated meta tags for SEO.
7. Carry that ranking straight into the article's section order.

**Pitfall:** Ranking value props by how impressive they sound rather than by the frequency of the painful step. The tell is a criteria list where the first item is a capability rather than a repeated chore.

**Apply at Pabau:** For Pabau, the before-state questions surface the repeated manual chores in an aesthetic practice: rekeying consent forms, chasing no-shows, reconciling stock. Rank article criteria by how often each chore repeats in a week, not by feature impressiveness.

**Apply anywhere:** Use the before-state questions to surface the repeated manual chores in your customer's week, then rank your article's criteria by how often each chore repeats, not by how impressive the feature is.

### 5. Ask any AI-content vendor for one good example before signing  `174.9`
*useful · concrete actions · source 174*

Khanal closes with a challenge that doubles as a procurement test: he has yet to see anyone show him an example of a good piece of content produced with AI, and invites anyone with one to share the link. Turn that into a buying step. Vendors and tools pitching AI content marketing describe throughput, not outcomes, so ask instead for a specific published URL, on a real client site, that the vendor considers genuinely good, and then apply the second-read test to it. The demand is hard to fake because it requires a live page rather than a sample. It also surfaces the vendor's own quality bar quickly. A vendor who sends a competently written but generic overview has told you what they think good means.

> "I have yet to see anyone show me an example"

**Evidence:** Khanal's open challenge at the end of the piece: nobody had yet shown him an example of a good piece of content produced with AI, and he invited readers to post a link.

**How to do it**

1. Ask every AI-content vendor or tool for one live published URL they consider a genuinely good piece.
2. Reject sample documents and demo outputs; require a real page on a real client domain.
3. Read the page once for flow, then list the claims it makes and check them against the top five ranking pages.
4. Ask the vendor which specific claim in the piece came from a human source and where that source came from.
5. Check the page's search performance and whether it earned any links or citations since publishing.
6. Walk away if the best example the vendor can produce is a competent but non-differentiating overview.

**Pitfall:** Accepting a polished sample document rather than a live URL. Samples are cherry-picked and hand-edited, so they tell you nothing about what the vendor ships at volume.

**Apply at Pabau:** If David evaluates an AI writing tool or agency for pabau.com, require a live client URL and run the same claim-comparison check used in the editorial pass. Also ask which claim came from a human source, since that is the step most AI content pipelines skip.

**Apply anywhere:** Before buying an AI-content service or tool, ask for one live published URL the vendor considers genuinely good. Refuse sample documents. Run the claim-comparison check on it, ask which claim came from a human source, and check whether the page earned links or citations. A competent but generic overview as their best example is your answer.

### 6. Ask four questions to find out if an agency scales content with AI  `180.6`
*useful · concrete actions · source 180*

Grow and Convert give a short interrogation for the production side of an agency engagement. Ask what their process is for writing and conveying your value props, benefits, messaging and differentiators in a way that feels native to your brand. Ask whether they even have one. Ask how it works. Ask whether they use AI to scale content production or run a human-driven research and writing process. Then push on frequency: is it a one-off interview at the start of the engagement, a few one-hour calls, or do they interview experts at your company piece by piece? They say the piece-by-piece version is both extremely rare among outside agencies and the most effective, because bottom-of-funnel topics are product-centric and demand knowledge of your features, the nuanced pain points they solve, and how you differ from competitors.

> "Do they even have one?"

**Evidence:** Grow and Convert say per-piece expert interviews are extremely rare in outside agencies but the most effective approach they have found for expressing product and domain expertise.

**How to do it**

1. Ask the agency to describe, step by step, how your value props and differentiators get into an article.
2. Ask whether that process is written down anywhere, and ask to see it.
3. Ask directly whether AI is used to scale production, and at which step.
4. Ask how often they interview your internal experts: once at kickoff, a few calls, or per article.
5. Ask who at your company they expect to interview and for how long each time.
6. Ask for one recent article and the interview it came from, so you can see the mapping.
7. Check the sample for detail only an insider could supply: why a feature was built that way, what it replaces.
8. Reject any answer where the writer is expected to research the topic themselves and become the expert.

**Pitfall:** Accepting a kickoff-only interview. It covers the first few articles and then the writer is back to self-research, which is when the output flattens into generic coverage.

**Apply at Pabau:** Any freelancer or agency writing for pabau.com should be committed to a recorded interview with a Pabau product or clinical specialist per article, not a single onboarding session. David should make that a contract term, not a hope.

**Apply anywhere:** Interrogate a content agency on four points: how your differentiators reach the page, whether the process is documented, whether AI scales production, and how often they interview your experts. Insist on per-article interviews, not a kickoff call.

### 7. Assign named owners to topic, creation, promotion and measurement  `102.10`
*useful · best practices · source 102*

Grow and Convert close their execution section with a staffing point that most strategy documents skip. Whether you use an agency, freelancers, in-house staff, or a combination, you have to decide who is responsible for each step: topic selection, content creation, content promotion and distribution, and measuring content performance. They note that these steps require different skill sets, so effective execution usually needs multiple people. The failure mode is implicit but clear: teams hire a writer, assume the writer covers the whole chain, and end up with articles that are produced but never promoted and never measured. Naming an owner for each of the four steps at the point of choosing the resourcing model is what prevents the gap.

> "these steps often require different skill sets"

**Evidence:** Grow and Convert list the four steps and say multiple people are usually needed because the skill sets differ.

**How to do it**

1. Write the four steps as rows: topic selection, content creation, promotion and distribution, and performance measurement.
2. Put a named person against each row, including the steps you are outsourcing.
3. Where one person owns two rows, confirm they have both skill sets rather than assuming it.
4. If a row has no owner, do not commission articles until it does.
5. Set the cadence for each row: calendar per quarter, drafts per week, promotion at publish, measurement monthly.
6. Review the table when the resourcing model changes, since agencies and freelancers usually cover creation only.

**Pitfall:** Assuming a writer or agency owns promotion and measurement. The signal is a growing library of published pieces with no promotion log and no conversion reporting.

**Apply at Pabau:** Pabau should name an owner for each of the four steps in its content process, particularly promotion and measurement, which tend to fall between the writer and the SEO workflow.

**Apply anywhere:** Name an owner for each of topic selection, creation, promotion and measurement before commissioning content. Agencies and freelancers usually cover creation only, and the other three quietly go unowned.

### 8. Assume marketers are one level removed from the customer  `122.12`
*useful · best practices · source 122*

Grow and Convert state plainly that marketers typically do not have direct contact with customers, and apologize for it while insisting it is true. This is the mechanism behind their whole process design. If the person choosing topics has never spoken to a buyer, their topic list is built on second-hand summaries and best guesses, and no amount of writing skill repairs that. It also explains why the research session is stacked with sales and support rather than marketers. The standing rule that follows is that a content team should have some structural route to first-hand customer contact, whether that is sitting in on sales calls, reading support chats or joining onboarding sessions, rather than relying on internally circulated persona documents.

> "Marketers typically don't have direct contact with customers."

**Evidence:** Grow and Convert say they consistently find marketers lack direct customer contact, which is why they refuse filtered or best-guess information in the research session.

**How to do it**

1. Give every content writer read access to the support inbox or chat transcripts.
2. Require each writer to sit in on two sales calls per month and take notes.
3. Record and transcribe sales calls so quotes can be searched by pain point.
4. Replace the persona document as the primary brief input with quotes from real calls.
5. In the research session, let sales and support answer customer questions first and marketing last.
6. Audit topic lists quarterly for items that trace to no customer statement at all.

**Pitfall:** Persona documents written by marketing and then cited by marketing create a closed loop. Everyone agrees on a customer nobody has spoken to, and the mismatch is invisible from inside.

**Apply at Pabau:** Pabau's writers should read clinic support tickets before drafting operations content. Ticket wording is the closest thing available to how a practice owner actually describes the problem.

**Apply anywhere:** Assume your content team is one step removed from the customer and fix it structurally: support-inbox access, sales-call attendance, and call transcripts as brief inputs.

### 9. Book a fresh expert interview for every unique topic, not just at kickoff  `134.15`
*useful · best practices · source 134*

Grow and Convert are explicit that their two-stage onboarding has a limit. The pre-kickoff research plus the two kickoff hours give you enough industry understanding to build the strategy and decide which topics to write first. They do not give you the details needed to write every article. For that you need a subject matter expert interview for every unique topic you write about, which is why the interviewing skills matter more than domain expertise. This sets the operating cost of the model honestly: an engagement producing 34 articles in a year, as Rainforest did, implies roughly 34 interviews on top of the kickoff. The trade is that the writer never needs to become a domain expert, because the expertise arrives per article and is verified on the call.

> "you're going to need an SME interview for every unique topic you write about"

**Evidence:** Grow and Convert produced 34 articles for Rainforest QA in the first year under this model.

**How to do it**

1. Treat kickoff research as strategy input only, and do not let writers draft from it.
2. Schedule one expert interview per commissioned article, booked before the outline is approved.
3. Send the SERP-gap analysis and the question list to the expert in advance.
4. Run the interview with the baseline framing, the claim challenges and the aha-moment push.
5. Record and keep each interview as reusable source material for later articles on adjacent topics.
6. Budget interview time in the content calendar as a line item, not as overhead.

**Pitfall:** Reusing the kickoff notes for the fifth and tenth article. The drafts get progressively more generic because the specific details that made article one convert were exhausted at the start.

**Apply at Pabau:** Pabau should treat an expert interview as a required input on every new /blog/ or /templates/ article, with the recording stored so later articles on the same feature can reuse it rather than reinterviewing.

**Apply anywhere:** Run one expert interview per article, not one per engagement. Kickoff research is strategy input; it runs out of specifics after the first few drafts.

### 10. Break long-form content into short chunks, bullets, and 3-minute videos  `43.13`
*useful · best practices · source 43*

Rand argues the primary barrier to content being read and valued isn't writing quality but format: shrinking attention spans, which he attributes to TikTok's broader cultural effect, now apply to written content the same way they apply to video. His prescribed response is to actively break long-form assets, multi-paragraph reports, and big PDFs into short chunks: a few paragraphs, a clear bullet-point list, a couple of graph visuals, or several three-minute videos, rather than one long report or article. He states he believes in long-form content less than he ever has, favoring this chunked, multi-format breakdown as the way to convey information going forward.

> "less of a believer in them than I've ever been"

**How to do it**

1. Audit existing long-form Pabau assets (whitepapers, big guides, long blog posts) and identify ones that could be split into shorter standalone pieces (inferred).
2. For each long asset, extract three to five core standalone points that could each stand alone as a short chunk.
3. Turn each core point into a short paragraph block, a bullet-point list, or a simple graph/visual, rather than leaving it embedded in continuous prose.
4. Convert at least one core point per asset into a short-form video of roughly three minutes rather than only text.
5. Distribute the resulting short chunks/videos across the channels your audience uses, rather than only publishing the one long original piece.
6. Track engagement on the short chunks/videos versus the original long-form piece to confirm the chunked format performs better for your audience (inferred verification step).

**Pitfall:** Continuing to invest primary effort in long-form, multi-paragraph reports on the assumption that thorough written detail is inherently more valuable — Rand argues shrinking attention spans make this the wrong default format regardless of the content's underlying quality.

### 11. Budget two full days to build the nurture course, not two hours  `155.12`
*useful · best practices · source 155*

Grow and Convert are explicit that the email course is where the work goes. Erika started from a series she had already been using for over a year and still put in two solid days, about 15 additional hours, to turn it into the eight-email version. She kept lengthening the sequence over time, moving from five emails up to eight. The article's argument is that this step should take time, because it is the step where value actually reaches the subscriber. If you intend to make an ask later, what you gave first has to be good enough to earn it. The ads and the landing page took a fraction of that effort: a dollar in Canva and 30 minutes in LeadPages.

> "2 solid days, or 15 additional"

**Evidence:** Erika: 15 additional hours on top of a year-old series, growing the sequence from five emails to eight.

**How to do it**

1. Draft the course outline as one lesson per email before writing any copy.
2. Start from material you have already published or already send, rather than a blank page.
3. Budget about 15 hours of writing on top of that starting material.
4. Write each email so it can be acted on the day it arrives, with a concrete routine or checklist.
5. Keep the format plain text and conversational rather than designed.
6. Ship at five emails, then extend toward eight as you see which lessons hold attention.
7. Spend far less time on the ad and landing page; a template and a Canva image are enough.
8. Review open and click rates per email and rewrite the weakest lesson before adding a ninth.

**Tools:** Mailchimp, Canva, LeadPages

**Pitfall:** Teams invert this and spend the budget on creative and page design while the sequence is thin. The pitch in email 6 then lands on someone who received nothing worth paying for.

**Apply at Pabau:** If Pabau gates a template behind an email, the follow-up sequence deserves more writing time than the landing page. Budget two days of a writer's time per sequence and reuse existing blog material as the base.

**Apply anywhere:** Spend roughly 15 hours building the nurture sequence, starting from material you already have, and keep the ad and landing page cheap by comparison.

### 12. Build a paired swipe file of bad and good intros for the same keyword  `127.13`
*useful · concrete actions · source 127*

Grow and Convert structure the teaching half of the article as a deliberate exercise: let us discuss a few examples so you can sense patterns of good versus bad blog post introductions, and let us start with bad so you know what to avoid. They then run two intros for the same query, 'how to lose weight', one bad and one good, and annotate each. That pairing is the method worth copying. Comparing two openers written for the identical searcher isolates the variable, since topic, intent and competition are held constant and only the opening move differs. Their own bad-versus-good pair shows the difference reduces to a basic rhetorical question versus a contrarian evidence claim. A team file of these pairs, per keyword type, trains writers faster than a style rule does.

> "so you can sense patterns of good versus bad"

**Evidence:** Grow and Convert deliberately teach bad first, then good, using two intros from the same 'how to lose weight' SERP.

**How to do it**

1. Pick a keyword you target and open the top eight ranking results.
2. Screenshot the first two sentences of each, with the URL and its rank.
3. Sort them into a bad column and a good column and write one line saying why for each.
4. Repeat for two or three more keywords of different types, for example a how-to, a best-X listicle and a comparison.
5. Store the pairs in a single doc grouped by keyword type, since the right opening pattern differs by type.
6. Give new writers the doc as onboarding and have them classify five unlabeled examples before their first draft.
7. Add your own published intros to the file, in whichever column they honestly belong.
8. Refresh the file when the SERP turns over, so the examples stay current.

**Pitfall:** A swipe file of only good examples does not work; writers cannot see what they are doing wrong without the matched bad version from the same SERP. Mixing keyword types in one list also teaches the wrong pattern, since a listicle opener and a how-to opener should differ.

**Apply at Pabau:** David should keep a Pabau swipe file of paired intros pulled from the SERPs Pabau competes on, split by page type: blog, template and code-reference. It becomes the onboarding doc for any writer producing Pabau drafts.

**Apply anywhere:** Build a swipe file of paired introductions from the same SERP, bad and good side by side, grouped by keyword type. Holding the searcher constant isolates the opening move, and new writers learn the pattern faster from matched pairs than from a style rule.

### 13. Build a small portfolio of named stories, one concept each  `91.18`
*useful · concrete actions · source 91*

Grow and Convert say they have many articles that count as disruption stories, and they name four: Pain Point SEO, Mirage Content, Specificity Strategy and Content Brand. Each has brought high quality leads for the agency. That is a portfolio rather than a single flagship piece, and each entry is built on a different named concept attacking a different part of the industry's standard practice. The value of the portfolio structure is coverage: a reader who does not respond to one framing may respond to another, and each named concept gives you a separate reason to post on social and a separate phrase that can spread. It also spreads the risk that any one story fails to resonate, which they say happens often, since only some become link assets and only some strike a chord.

> "Pain Point SEO, Mirage Content, Specificity Strategy, Content Brand"

**Evidence:** Grow and Convert report that each of Pain Point SEO, Mirage Content, Specificity Strategy and Content Brand has brought high quality leads to the agency.

**How to do it**

1. List the standard industry practices your approach rejects, one per line.
2. Pick three or four that your product or service genuinely does differently.
3. Give each a short name and write one disruption story per name, not one story covering all of them.
4. Sequence them, publishing one at a time so each gets its own promotion window.
5. Promote each on paid and organic social with the name as the hook.
6. Track conversions per story and put more budget behind the ones that convert.
7. Retire or rewrite any story that gets traffic but no conversions, and keep the framing that worked.
8. Cross-link the stories so a reader who responds to one finds the others.

**Pitfall:** Bundling all your contrarian positions into one long manifesto means none of them gets a name people can repeat, and you get one shot at resonance instead of four.

**Apply at Pabau:** Pabau should aim for three or four named positions over time, each on a different thing aesthetic practices are told to do that Pabau thinks is wrong, published one at a time rather than as a single manifesto page.

**Apply anywhere:** Write one story per named concept rather than one manifesto covering everything. Three or four separate named positions give you separate promotion hooks, separate phrases that can spread, and several chances to find the framing that resonates.

### 14. Build a two-year conversion record per target keyword to win the pushback argument  `95.12`
*useful · concrete actions · source 95*

Matt Goolding wrote this analysis because Grow and Convert kept getting client pushback on proposed target keywords whenever SEO tools showed low volume. Clients accepted the higher conversion rate argument but objected that a high rate is useless if few people search. His answer was to stop arguing from principle and pull the number: a snapshot across 2 years and 17 clients showing that articles targeting sub-20 search volume generated more than 1,600 conversions directly attributed to their content. He then backed it with named examples, timescales and per-post conversion counts. The transferable procedure is to build the same record for your own site so the next low-volume recommendation is settled by data rather than by debate.

> "directly attributed to our content"

**Evidence:** Grow and Convert: 2 years, 17 clients, more than 1,600 conversions from articles targeting sub-20 search volume.

**How to do it**

1. Add a target keyword field and a reported-volume-at-selection field to every article record in your content sheet.
2. Freeze the volume figure at the moment of selection, since it changes later and destroys the comparison.
3. Attach conversion tracking at landing-page level so each article's signups, demos or inquiries are countable.
4. Every quarter, export conversions per article and join them to the frozen volume figure.
5. Bucket the articles as sub-20, 20 to 100, and above 100 reported volume.
6. Report total conversions and conversions per article per bucket, over a window of at least a year.
7. Add named examples with dates and counts, since aggregate numbers alone do not persuade stakeholders.
8. Bring that one-page summary to every keyword approval meeting instead of restating the theory.

**Tools:** Google Analytics, Ahrefs

**Pitfall:** If you do not freeze the reported volume at selection time, terms that have since grown will be reclassified into the higher buckets and the analysis will understate the mini-volume case.

**Apply at Pabau:** Pabau should record the target keyword and its volume at the time each blog, template or code-reference page is commissioned, then report demo requests per volume bucket. That record is what settles internal arguments about whether a narrow page is worth writing.

**Apply anywhere:** Record each article's target keyword and its reported volume at selection, then report conversions per volume bucket every quarter. A year of that data ends the low-volume argument better than any reasoning does.

### 15. Build one content asset to serve rankings and citations together  `84.16`
*useful · best practices · source 84*

Grow & Convert's second reason for putting owned content first is a budgeting argument: content on your site kills two birds with one stone, driving traditional SEO results while simultaneously increasing visibility in LLM responses, because the same content that ranks on Google is what LLMs pull from when generating product recommendations. This is the practical case against running GEO as a separate workstream with its own briefs, its own writers and its own budget line. The implication for a content calendar is that a page only qualifies as a GEO asset if it is also a credible ranking candidate for a product-intent query. If a proposed page would not rank, it will not be discovered by the grounding step either, so it earns nothing on either channel.

> "kills two birds with one stone"

**Evidence:** Grow & Convert's stated Tier 1 rationale, supported by clients being cited in 88% of analyzed product topics off pages the agency wrote to rank.

**How to do it**

1. Kill any separate GEO content backlog and merge it into the SEO content calendar.
2. Score each planned page on whether it can realistically rank for a product-intent query.
3. Drop pages that fail that test, since they will not be discovered by the grounding step either.
4. Brief each surviving page for both jobs: rank on the query, and answer the buyer prompt in a quotable passage.
5. Measure each page on organic position and on citation appearance in your prompt basket.
6. Refresh the pages that rank but are not being cited before commissioning new ones.

**Pitfall:** Running a separate GEO content program produces pages optimized for a model that never finds them, because discovery still runs through search rankings.

**Apply at Pabau:** Pabau should not maintain a separate GEO content list. Every blog and template page brief should carry both targets, the ranking query and the buyer prompt it should be quoted for.

**Apply anywhere:** Merge your GEO content backlog into the SEO calendar and brief each page for both jobs. A page that cannot rank will not be found by the grounding step either.

### 16. Build one dedicated post per target keyword rather than combined guides  `131.5`
*useful · best practices · source 131*

Grow and Convert call it a proven tactic: create a separate blog post for each target keyword rather than folding several terms into one large guide. On Smartlook they applied it across category keywords, competitor 'vs' pieces and 'alternatives' pieces, producing head-to-head comparisons against a wide range of competitors including Amplitude and Mixpanel. The payoff shows in the ranking spread. Across 50 targeted keywords they took 11 number one rankings, 20 top three, 37 top 10, at an average position of 7. The three keyword types they used, category, competitors and alternatives, and jobs to be done, accounted for every piece in their top 15 converting content. The rule keeps each page's intent single and makes conversion attribution per keyword readable.

> "creating separate blog posts for each target keyword"

**Evidence:** 50 targeted keywords produced 11 no. 1 rankings, 20 top 3, 37 top 10 and an average position of 7.

**How to do it**

1. Take the keyword list and check for SERP overlap between any two terms before merging them.
2. Give any term whose SERP is materially different its own post, even when the topics look adjacent.
3. Title and slug each post around its single target keyword, front-loaded.
4. Write 'vs' pieces one competitor at a time instead of a single multi-competitor comparison, keeping the alternatives roundup separate.
5. Internally link the sibling posts to each other so the cluster shares authority.
6. Track rank and conversions per post, not per topic group, so you can see which keyword type earns.
7. Merge only when two posts start swapping positions for the same query, which is cannibalization rather than coverage.

**Pitfall:** The tactic breaks into cannibalization when two posts genuinely share a SERP. Check overlap first; if the top 10 for both terms is largely the same URLs, one post covers both.

**Apply at Pabau:** Pabau should keep 'Pabau vs X' pieces one competitor per article rather than rolling them into a single comparison page, and keep the alternatives roundup as its own article. Check SERP overlap before splitting near-identical terms.

**Apply anywhere:** Give each target keyword its own post rather than combining several into one guide, but check SERP overlap first so you are splitting distinct intents rather than creating cannibalization.

### 17. Build the mega guide by compiling published posts, not writing it first  `98.8`
*useful · best practices · source 98*

Grow and Convert's sequencing rule for pillar content, which is the reverse of the usual pillar-then-cluster order. They wrote three separate posts on hiring writers first: in-house vs agency vs freelancers, how to find and evaluate writers, and how much to pay and how to keep them motivated. Only once those three covered most of the process did they compile them, add content that filled the gaps between them, and turn the topic into a mega guide of 5,000+ words. Hyam's counterfactual is direct: if they had tried to cram all of that into one post from the start, it would have been too high level and probably not helpful. The order matters because each individual post gets to go deep on one question, and the guide inherits that depth rather than diluting it.

> "we compiled all three posts, added some more content that"

**Evidence:** Three Grow and Convert posts on hiring writers compiled into a 5,000+ word mega guide.

**How to do it**

1. Publish the individual pain-point posts first, one per decision, in the order a reader hits them.
2. Wait until the set covers most of the process end to end before considering a guide.
3. Read the published set in sequence and note the gaps between posts where a reader would be lost.
4. Write only the connecting material needed to close those gaps.
5. Assemble the guide from the existing posts plus the connecting material, keeping the depth intact.
6. Link each guide section out to the fuller standalone post rather than deleting the originals.
7. Treat the guide as the hub for internal links and the individual posts as the long-tail entry points.

**Pitfall:** Writing the mega guide first forces every sub-topic down to a few paragraphs, and you then have a broad piece you cannot narrow without rewriting it. The compiled version keeps the depth because the depth already existed.

**Apply at Pabau:** Pabau should build its long template and guide pages from already-published narrow articles. Publish the three or four specific pieces first, then compile, rather than commissioning a 5,000-word guide up front that covers each point in two paragraphs.

**Apply anywhere:** Publish narrow posts first, then compile them into the pillar guide with connecting material. Writing the pillar first flattens every sub-topic and leaves you nothing to link to.

### 18. Build the outline from recurring SERP subtopics plus product demo sections  `96.7`
*useful · concrete actions · source 96*

Grow and Convert show the actual outline they built for TapClicks. The SERP analysis had told them the piece needed dashboard examples, template features, reporting features and trackable KPIs. They then wrote an H2 'How to Set Up a Paid Search Dashboard in TapClicks' with H3s for connecting data sources, selecting and customizing a template, and creating recurring reports with client access, plus H4s for creating a new widget and creating custom access permissions. A closing H2 covered the best paid search dashboards for scale agencies. Every required subtopic is covered, but each one is expressed as a step in using the product. They note headings do two jobs: they organize the post for readers, which improves readability and reduces bounce, and they carry relevant keywords, which Google weighs.

> "we structured the body of our piece like this"

**Evidence:** This outline produced the TapClicks post that ranks at position 2.

**How to do it**

1. Write out the required subtopics from the recurring-topic tally as a checklist.
2. Draft H2s that describe using your product to accomplish the reader's job.
3. Map each required subtopic onto an H3 under those H2s rather than a standalone section.
4. Use H4s for the sub-procedures a reader would actually get stuck on.
5. Close with an H2 that answers the comparison question for the buyer segment you target.
6. Check the finished outline against the subtopic checklist before writing a word.
7. Put the relevant keyword phrasing into the headings while keeping them readable.

**Pitfall:** Adding a heading per required subtopic in a flat list. That covers the topics but produces a directionless post that never demonstrates the product.

**Apply at Pabau:** Pabau outlines should express required subtopics as steps inside a workflow the reader runs in Pabau, rather than as detached 'benefits of' and 'features of' sections.

**Apply anywhere:** Turn required subtopics into steps of a workflow that uses your product, then check the outline against the subtopic checklist before drafting.

### 19. Buy Facebook traffic across cold, lookalike and retargeting audiences at publish  `136.10`
*useful · concrete actions · source 136*

After testing promotion channels at the end of 2018, Grow and Convert settled on paid Facebook promotion plus link building, and have used that combination for every client since. The specifics: they run three audience types against each article, cold audiences, lookalikes and retargeting of people who have already visited the client's site, and send that traffic to the article rather than to a landing page. The ad spend comes out of the agency's own budget, not the client's, which is unusual and worth noting when comparing their numbers to an in-house program. The stated purpose is not conversions from the ads. It is to replace the initial surge communities used to give, because that surge naturally builds some links to the piece and starts it ranking.

> "We test both cold audiences, lookalikes and retarget visitors"

**Evidence:** Grow and Convert adopted paid Facebook plus link building at the end of 2018 after community promotion lost effectiveness, and still use it for every client.

**How to do it**

1. At publication, set up three Facebook ad sets per article: cold interest targeting, a lookalike of converters, and retargeting of site visitors.
2. Point all three at the article URL, not at a demo or signup page.
3. Keep the budget small and treat cost per read as the buying metric, not cost per conversion.
4. Let the cold set find the audience, then shift budget to whichever of the three holds the lowest cost per engaged read.
5. Watch referring domains for the article over the following month; new links are the outcome you are buying.
6. Stop the spend once the post starts picking up organic impressions in Search Console.
7. Record which articles gained links from the push and reserve link building budget for those.
8. Decide explicitly who funds the spend, since agency-funded promotion changes what the reported cost per lead means.

**Tools:** Facebook, Google Search Console

**Pitfall:** Judging the push on conversions from the ads. It usually loses money on that basis; the return is the links and the earlier ranking, so a strict ROAS rule kills the tactic before it works.

**Apply at Pabau:** Pabau can run the same small push behind new comparison and template pages, targeting aesthetic and healthcare practice owners with cold interest sets plus a site-visitor retargeting set. Judge it on referring domains gained per page, not on demo bookings from the ad.

**Apply anywhere:** At publication, run a small paid social push at the article itself across cold, lookalike and retargeting audiences. You are buying the early traffic surge that produces natural links and faster ranking, so measure referring domains rather than ad conversions.

### 20. Buy any cheap tool that saves your content manager hours  `152.9`
*useful · best practices · source 152*

Grow and Convert could not make content marketing technology cost a meaningful line in the model. WordPress is free, email services are cheap, opt-in tools like OptinMonster or SumoMe are cheap, and landing page tools like Unbounce or LeadPages are cheap relative to salaries and usually serve paid ads too. They note you could add SEO software like Moz Pro or Ahrefs and it still would not matter. The only category that dents a content budget is an expensive inbound automation suite like HubSpot, and even that runs roughly $1,500 to $2,500 a month, still far less than the cost of humans. The decision rule that falls out: if a small tool saves your marketing manager hours a month, buy it, because an hour of salaried time costs more than the subscription.

> "just doesn't cost a lot, tech-wise, to run a blog"

**Evidence:** Marketing automation suites at $1,500-$2,500 a month are still less than headcount; every other content tool is a rounding error in the model.

**How to do it**

1. Total your current monthly content tooling spend and put it next to the loaded monthly cost of your content headcount.
2. Convert the headcount figure into an hourly rate using the share of time spent on content.
3. For any candidate tool, estimate the hours per month it saves the content manager.
4. Buy the tool whenever hours saved times the hourly rate exceeds the subscription price.
5. Review only the one expensive line, the marketing automation suite, for genuine ROI, since it is the only tool large enough to matter.
6. Re-check the tooling total annually so it stays a rounding error against salary.
7. Do not cut cheap tools during a budget squeeze; cut them only if they save no time.

**Tools:** WordPress, OptinMonster, SumoMe, Unbounce, LeadPages, Moz Pro, Ahrefs, HubSpot

**Pitfall:** Auditing $19 subscriptions while the headcount line goes unexamined. It burns management attention on a term the model shows is negligible.

**Apply at Pabau:** Pabau's content team should approve small time-saving tools without a business case and reserve scrutiny for the automation suite. Hours the content manager gets back are worth more than the subscription.

**Apply anywhere:** Approve small time-saving tools for your content team without a business case, and reserve scrutiny for the one expensive automation suite.

### 21. Call out the industry's unnamed problem to strike a chord  `91.7`
*useful · concrete actions · source 91*

Grow and Convert describe a fourth title and angle pattern from previous client LAWCLERK: 'Why the Large Law Firm Business Model Is Dying and What We're Doing Instead'. The angle names a problem that people in the industry had either not yet put a name to but were feeling the effects of, or were avoiding altogether. They call it calling out the elephant in the room, and say it works because it immediately shows the reader you see and understand the problem and have a solution for it. This is a different starting point from the other formulas. Instead of restating a pain the audience already articulates, you supply the name for something they only feel. The angle is available only where a structural shift is genuinely underway in the market, which is why they present it as one option among several rather than the default.

> "we're calling out the elephant in the room"

**Evidence:** LAWCLERK's disruption story, cited as striking a chord with potential clients.

**How to do it**

1. List the structural shifts in your market that insiders discuss privately but rarely publish about.
2. Pick the one your product is positioned to answer and check nobody has already named it.
3. Give it a short, blunt name, for example 'the large law firm business model is dying'.
4. Write the title as that name plus 'and what we're doing instead'.
5. In the intro, prove you see the effects with specifics practitioners recognize, not projections.
6. Show why the incumbent model produces those effects, so the name feels earned rather than provocative for its own sake.
7. Only then introduce your product as the alternative model.
8. Skip this angle entirely if no real structural shift exists; a manufactured one reads as hype.

**Pitfall:** Naming a decline that your audience does not actually feel makes you look like you are talking down to the industry, and the piece gets dismissed rather than shared.

**Apply at Pabau:** Pabau has a credible version of this in the shift away from paper-and-spreadsheet practice management and single-purpose booking tools. A piece naming that shift would carry more weight than another comparison article.

**Apply anywhere:** Where a real structural shift is underway in your market, give it a name nobody has used yet, then say what you are doing instead. It signals you understand the problem before you have sold anything.

### 22. Cap the founder story to lived pain and how you solve it  `91.9`
*useful · best practices · source 91*

Grow and Convert warn that it is easy to go down a rabbit hole when sharing your personal story. The discipline they apply is a two-item filter for what stays in. A topic earns its place only if it shows you understand or have lived the reader's pains, or shows why and how your company solves those pains. Anything else, however interesting to the founders, comes out. This matters because the founder interview that produces the raw material tends to generate long personal narrative that feels significant internally and reads as self-indulgent externally. The filter also keeps the piece anchored to the overarching narrative agreed at the start, which is what makes the story convert rather than merely entertain.

> "it can be easy to go down a rabbit hole when sharing your personal story"

**Evidence:** Grow and Convert's stated rule from writing dozens of client disruption stories.

**How to do it**

1. Transcribe the founder interview and pull out every anecdote as a separate line.
2. Score each anecdote against two tests: does it prove lived experience of the reader's pain, or does it show how you solve that pain.
3. Delete every anecdote that scores zero, including funding history, team origin stories and industry commentary.
4. Keep at most one or two anecdotes per pain so the story does not stall.
5. Check the surviving anecdotes still ladder up to the agreed overarching narrative.
6. Have someone outside the founding team read the draft and flag anything that reads as inside baseball.
7. Move genuinely interesting off-narrative material to a separate about page or a different post.

**Pitfall:** Founders defend their favorite anecdotes because those moments mattered to them. Use the two-item filter as the stated rule up front so the cut is not a judgement call in review.

**Apply at Pabau:** If Pabau publishes a founder-led piece, hold every anecdote to those two tests. Stories about running or supporting a practice stay; company milestones and funding history do not.

**Apply anywhere:** Keep only the personal anecdotes that prove you have lived the reader's pain or show how you fix it. Everything else, however meaningful internally, belongs on an about page.
