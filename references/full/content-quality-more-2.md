# Content Quality — supporting (part 2 of 7)

23 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Build a keyword map of every page before deciding new versus rewrite  `139.10`
*useful · concrete actions · source 139*

After uncovering pain points, Brandon faced a per-keyword choice: convert an older post with similar intent, or write a new one. He resolved it systematically by building a keyword map of every page on the site and matching each page to a keyword under the new content strategy. Where a keyword had no existing page with matching intent, it went into the content backlog for new writing. Where a page existed, he updated and optimized it instead. This is what let him sequence the work: he changed and optimized the highest-converting pages first, prioritizing terms where the searcher was already looking to save money or handle their taxes over higher-volume general advice terms like 'tax advice'. The map is what makes that prioritization possible rather than ad hoc.

> "I created a keyword map of all the pages on the site"

**Evidence:** Brandon used the keyword map to decide every rewrite-versus-new decision across the Keeper Tax site during a 3.5 month engagement.

**How to do it**

1. Export every URL on the site into a sheet with columns for current ranking query and current conversions.
2. Add a column for the keyword each page should target under the new strategy.
3. For every keyword on the strategy list, search the sheet for a page with matching intent.
4. Mark matched keywords as rewrite jobs and unmatched keywords as backlog jobs for new content.
5. Sort the rewrite jobs by conversion intent, not by volume, and start at the top.
6. Flag any two pages mapped to the same keyword and merge or repoint one of them.
7. Update the map every time a page is published or retargeted so it stays the single source of truth.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Without the map you write new posts for keywords an old page already half-covers, and end up with two pages splitting the same query. The signal is two of your URLs alternating in the same SERP.

**Apply at Pabau:** Pabau should maintain one sheet mapping every /blog/, /templates/ and code-reference URL to its intended keyword, and check it before commissioning any new article.

**Apply anywhere:** Map every existing page to its intended keyword before commissioning content, rewrite where intent already matches, and send only the unmatched keywords to the backlog.

### 2. Build comprehensive guides instead of chasing fan-out drift  `20.7`
*useful · best practices · source 20*

Rather than chasing every minor variation in query fan-outs (which shift slightly between runtimes but don't introduce dramatically new angles), the recommended response is to make content comprehensive in the traditional sense — building genuinely thorough 'ultimate guide'-style resources covering the topic's full breadth. Audience research should drive keyword/topic research, since these AI systems are described as reactive to real audience query patterns rather than generating queries in a vacuum. This reframes fan-out anxiety: comprehensive, audience-informed coverage largely future-proofs content against fan-out drift, rather than needing a new article per fan-out variant.

> "make sure your content is comprehensive"

**How to do it**

1. When planning content, treat query fan-out variability as a signal to go broader/deeper on the topic, not as a cue to fragment it into many near-duplicate articles.
2. Build 'ultimate guide' style comprehensive resources addressing the full breadth of sub-questions around a topic in one place, rather than one thin page per fan-out variant.
3. Ground topic/keyword selection in real audience research (support tickets, sales calls, community questions) rather than purely tool-generated keyword lists.
4. Periodically re-check a live prompt's fan-out (using the DevTools inspection method) to confirm existing comprehensive content still covers the current sub-query set.
5. Add any newly-appearing sub-topics into the existing comprehensive page rather than spinning up a new page for every fan-out shift. (inferred consolidation step)

**Pitfall:** Reacting to every fan-out change by producing new, narrowly-targeted content — fan-outs shift only 'a little bit between runtimes' and aren't introducing 'a dramatically new idea,' so fragmenting content this way is unnecessary churn versus simply being comprehensive.

### 3. Build one page per query instead of sprinkling keywords into existing pages  `106.14`
*useful · content insights · source 106*

Grow and Convert close on the on-page habit they see most: taking a keyword list and working the terms into pages that already exist on the site. They say the method rarely helps you rank for the specific keyword, because Google's algorithm distinguishes between content that loosely relates to a topic and content that specifically addresses the search term. Their conclusion is blunt: you have a very slim chance, if any, of ranking unless the entire page matches the intent of the query. This is the reason their process ends with creating a new blog post or landing page, or substantially updating an existing one, rather than editing keywords into place. It also explains why underdog sites can beat large brands whose pages are broad by necessity.

> "unless the entire page matches the intent of the search query"

**Evidence:** Grow and Convert state the sprinkling method 'rarely helps you rank for specific keywords' across their client work.

**Pitfall:** A page tuned for two or three keywords at once matches none of their intents fully, and typically ranks on page two for all of them.

**Apply at Pabau:** Pabau should stop adding target keywords into existing blog posts as an optimization. If a keyword deserves ranking, it gets its own page or a full rewrite of an existing one to that single intent.

**Apply anywhere:** Do not add a target keyword to an existing page and call it optimization. Google separates loosely related content from content built for the query, so give the keyword its own page or rewrite the page entirely to that intent.

### 4. Build originality-led ideas from five named company-owned story types  `107.20`
*useful · concrete actions · source 107*

Grow and Convert acknowledge that finding originality-led ideas is harder than finding keywords, because you need something unique and shareable. Their advice is still to start from the potential customer's pain points and brainstorm around those, and they give five specific idea types to work through: your company's disruption story, meaning why you decided to create the company; unique data you can pull together and analyze; case studies showing how you solve a specific problem; details about projects you have worked on or are working on now; and your company's opinions on aspects of your field. All five share a property: they draw on something only your company has, which is what makes them defensible against both competitors and AI summarization. For originality-led pieces they also stress casting a wider research net, beyond Google, to the platform you plan to promote on.

> "Write your company's disruption story"

**How to do it**

1. Take the pain-point list from the sales and CS interviews as the starting point.
2. For each pain point, ask which of the five types you can produce: disruption story, original data, case study, project write-up, or a stated opinion.
3. Check what data your product already collects that nobody else has, and scope one analysis from it.
4. Write one case study per major customer type, naming the situation, the fix and the outcome.
5. Before writing any originality piece, name the promotion platform and research what performs there.
6. Kill the idea if none of the five types applies, rather than writing a generic thought-leadership post.

**Pitfall:** Originality-led ideas generated without a company-owned angle turn into opinion posts anyone could have written, which get neither shares nor rankings.

**Apply at Pabau:** Pabau has aggregate data from practices and a real founding story, so original data analysis and case studies are the two viable originality types. Those also make strong candidates for the original visual every Pabau article requires.

**Apply anywhere:** Generate original ideas from five company-owned types: your founding story, proprietary data analysis, specific case studies, project write-ups, and stated opinions. If none applies to a topic, do not write the piece.

### 5. Buy differentiated content because it sells, not because it ranks  `174.10`
*useful · content insights · source 174*

Khanal justifies original, opinionated content on commercial grounds rather than ranking grounds. High-quality content of this kind helps convince customers about your product over competitors and helps your brand and ideas stand out. Most companies do not want to say the same thing as everyone else. They want to share unique, original or provocative opinions, explain why their competitors' approach to industry problems is wrong and why theirs is better, and be known for their thinking. He adds a caveat that this is easier said than done. The argument matters when defending budget, because the case for original content does not depend on any algorithm holding steady. It depends on a reader deciding you understand their problem better than the alternative, which stays true whether traffic arrives from search or from an AI answer.

> "They want to explain why the approach their competitors are taking"

**Evidence:** Khanal's argument that this kind of content is effective because it convinces customers to pick your product over competitors and makes the brand's ideas stand out, while noting thought leadership is easier said than done.

**How to do it**

1. Write down the two or three ways your approach to the customer's problem differs from your main competitors'.
2. For each difference, state why the competing approach fails and what it costs the customer.
3. Turn each into an article premise rather than a topic, so the piece argues rather than describes.
4. Have a customer-facing person check the premise against objections they actually hear on calls.
5. Measure these pieces on assisted pipeline and sales-team usage, not on sessions alone.
6. Keep a running list of premises you have published so the same argument is not rewritten under a new title.

**Pitfall:** Confusing a provocative headline with a differentiated argument. If the body reverts to balanced coverage, you get the reputational risk of a strong title with none of the persuasive value.

**Apply at Pabau:** Pabau's strongest articles should argue why a particular way of running an aesthetic or healthcare practice fails and what to do instead, then show how the software supports the better approach. David should measure these on whether sales uses them, not on sessions alone.

**Apply anywhere:** Justify original content commercially, not algorithmically. Write down how your approach to the customer's problem differs from competitors', say why theirs costs the customer something, and turn each difference into an article premise that argues rather than describes. Have a customer-facing colleague sanity-check it against real objections, and measure by sales usage as well as traffic.

### 6. Cannibalization halves your own ranking chances, it doesn't just dilute  `49.1`
*useful · content insights · source 49*

Keyword cannibalization occurs when two or more of your own pages target the same keyword, leaving Google unable to decide which one to rank, so it splits the available ranking authority between them rather than letting either compete at full strength. The practical effect is that neither page ranks as well as a single consolidated page would, meaning the site is effectively halving its own chances for that keyword rather than simply having one underperforming page.

> "can't decide which one to rank, and so it splits the authority"

**Evidence:** "You have two or more pages targeting the same keyword, Google can't decide which one to rank, and so it splits the authority between them. Neither page ranks well."

**Apply at Pabau:** When multiple Pabau articles target the same core keyword, treat it as a self-inflicted ranking cap on both pages rather than a content-quality problem to fix by improving either page individually — the fix is structural (consolidate or clearly differentiate), not more editing of either page alone.

**Apply anywhere:** When multiple your articles target the same core keyword, treat it as a self-inflicted ranking cap on both pages rather than a content-quality problem to fix by improving either page individually — the fix is structural (consolidate or clearly differentiate), not more editing of either page alone.

### 7. Check a top-funnel outline against your buyer's actual expertise level  `110.10`
*useful · content insights · source 110*

Grow and Convert argue most SaaS products sell to advanced customers, people who have worked in their industry for years and are not starting from zero knowledge. Top-of-funnel content usually covers introductory 'why this is important' or 'ultimate guide to this niche' material, which sits below that knowledge level. Their test is to read the table of contents of a top-ranking top-funnel piece against the person who decides the purchase. Pipedrive ranks #1 for 'sales presentation', and the decision maker on which CRM to use is an experienced sales executive. One of that article's bullets is 'what to bring to your sales presentation'. Inside the sections it notes that most sales presentations include a sales deck. Calling that thought leadership to an experienced sales team does not survive the test.

> "most SaaS businesses sell to advanced customers"

**Evidence:** Pipedrive's #1-ranking 'sales presentation' article includes 'what to bring to your sales presentation' and states that most sales presentations include a sales deck, aimed at a market where experienced sales executives choose the CRM.

**How to do it**

1. Name the person who signs off on buying your product and how many years they have worked in the field.
2. Open the table of contents of your best-performing top-funnel article.
3. Read each heading aloud and mark any that person already knows the answer to.
4. If more than half are marked, the article cannot be thought leadership for your buyer.
5. Check the body of one section for statements of the obvious, the tell Grow and Convert use.
6. Either rewrite the piece at your buyer's level or move the topic out of the blog queue.

**Pitfall:** Assuming reader and buyer are the same person. A beginner-level article can pull real traffic from people who will never buy, which makes the traffic chart look like validation.

**Apply at Pabau:** Pabau's buyers are practice owners and managers who have run clinics for years. Any pabau.com article explaining what a patient record is, or why appointment reminders matter, sits below their level and should be rewritten at practitioner depth or dropped.

**Apply anywhere:** Test a top-funnel outline against your actual buyer's experience level. Read every heading and mark what they already know; if most headings are marked, the piece is not thought leadership for the people who make the purchase.

### 8. Chewy's category-page keyword stuffing works only due to domain authority  `13.15`
*useful · content insights · source 13*

Edward cites a real, still-published example, referencing a Search Engine Land article on cosine similarity in ecommerce SEO, of Chewy running dense, repetitive keyword-stuffed paragraphs beneath its category-page product listings, a pattern Search Engine Land documents as common ecommerce practice of three to five paragraphs of search-optimized text placed beneath product listings. Both speakers argue this specific execution is bad SEO practice that only works because Chewy's domain authority and backlink profile are strong enough to absorb the risk; Edward says he has personally and repeatedly seen the reverse effect on other sites, where removing the exact-match keyword from multiple on-page instances, keeping it only in the title tag, URL slug, H1, first sentence, and sometimes meta description or alt text, then using natural variations everywhere else, causes the page to rank better for that same keyword, not worse.

> "I've literally removed the keyword from multiple instances on the page"

**Evidence:** Edward's direct account of repeatedly removing a keyword from multiple page instances and seeing rankings improve, contrasted with the Chewy example of dense repeated-keyword paragraphs that he says Google can easily detect.

**Apply at Pabau:** When optimizing Pabau pages, resist repeating the exact-match keyword throughout the body; place it only in the title, URL, H1, and first sentence, then use natural variations elsewhere, and do not benchmark against high-DR competitors like Chewy who can get away with outdated keyword-density tactics that would hurt a lower-authority site.

**Apply anywhere:** When optimizing your pages, resist repeating the exact-match keyword throughout the body; place it only in the title, URL, H1, and first sentence, then use natural variations elsewhere, and do not benchmark against high-DR competitors like Chewy who can get away with outdated keyword-density tactics that would hurt a lower-authority site.

### 9. Choose a list-style post when the query wants options compared  `112.12`
*useful · concrete actions · source 112*

Grow and Convert give a format rule for bottom-of-funnel product queries. For terms a general product page cannot win, they say it is often necessary to create either a page optimized for that specific query or a list-style post presenting multiple options. They note the list is often what actually holds the top rankings for these queries, and give the reason: people searching want to explore options before making a purchase decision, so lists are the best content type for satisfying that intent. The decision is therefore made from the SERP rather than from preference. This matters for a brand publishing on its own domain, because it means writing a roundup that includes competitors is sometimes the only format that can rank for a term describing your own product.

> "lists are the best content type for satisfying search intent"

**Evidence:** Grow and Convert observe that list-style posts are what typically hold top rankings for bottom-of-funnel product variation queries.

**How to do it**

1. Search the target query and classify the top 10 by format: single-product page, brand landing page, or list.
2. If more than half are lists, write a list; if dedicated single-topic pages dominate, write one of those.
3. When writing the list, include real competing options rather than only your own product lines.
4. Order it so your product leads on the specific attribute in the query, and say why in the entry.
5. Give every entry the same fields, so the page reads as a comparison rather than a pitch.
6. Recheck the SERP format mix at every refresh, since the dominant format shifts over time.

**Pitfall:** Publishing a single-product page into a SERP full of roundups leaves you unable to satisfy the compare-options intent, and the page stalls outside the top 10 no matter how good the copy is.

**Apply at Pabau:** Pabau's listicles already carry a Pricing heading and table per provider, which is the comparison structure this calls for. David should let the SERP decide between a listicle and a single-topic page before commissioning, rather than defaulting to whichever format the calendar prefers.

**Apply anywhere:** Classify the top 10 by format before you commission. If roundups dominate, write a roundup that genuinely compares options including competitors, because searchers at that stage want to explore before deciding.

### 10. Choose article format for answer-seekers, landing page for buyers  `36.11`
*useful · best practices · source 36*

The final decision rule for matching format to intent: if the searcher is looking for an answer rather than a solution or a way to contact someone, serve them an article; if the searcher is looking to use, buy, or contact something or someone, serve them a conversion-based SEO landing page instead of an article. Conflating these two formats, such as writing an article for a buy-intent keyword or writing a stiff conversion landing page for an informational keyword, is called a huge, costly mistake in SEO, with a dedicated earlier episode referenced as further reading on exactly this failure mode.

> "if somebody is looking for an answer rather than a solution"

**How to do it**

1. For every target keyword or page, classify searcher intent as either answer-seeking (informational) or action-seeking (wants to use, buy, or contact something).
2. For answer-seeking keywords, build the page as a genuine article or guide format optimized for explaining and informing.
3. For action-seeking keywords, build the page as a conversion-focused SEO landing page rather than an article, applying the fast-answer, above-fold-media, single-CTA formula.
4. Audit existing pages for the mismatch, such as an article-style page targeting a clear buy-intent keyword or a hard-sell landing page targeting a clearly informational keyword, and rebuild the format to match intent. (inferred)
5. Treat this format decision as happening before writing begins, not as an afterthought during editing, since the two formats are framed as fundamentally different jobs. (inferred)

**Pitfall:** Writing a keyword-targeted article for a page where searchers actually want to buy or contact someone, or vice versa — described as a mistake that loses people a lot of money, since the wrong format actively undermines conversion regardless of ranking.

### 11. Classify a mixed page by its primary user job  `66.4`
*useful · best practices · source 66*

Real pages rarely match one content type: a pricing page carries a definition, a comparison page carries a case study, a template page carries a how-to. The worksheet sets a single rule for this — the unit being classified is the page format or content pattern, and if one page includes more than one type, classify it by its primary user job. That keeps the audit decidable, and it also decides the fix: a page whose primary job is completing an action gets judged and improved as a transaction page even though it contains explanatory copy, and the explanatory copy inside it is not separately deprioritized. It also prevents the opposite error of splitting a working page into its component types just because the audit has a row for each.

> "includes more than one type, classify it by its primary user job"

**How to do it**

1. For each page in the audit, write down what the user is trying to finish on it — not what the page contains.
2. Where two jobs compete, pick the one the page is measured on and the one its main call to action serves.
3. Assign the page to exactly one content type row, and score it on that row's dimensions only.
4. Treat the secondary content inside the page as supporting material for the primary job, not as its own audit row — a definition inside a pricing page is context, not a commodity definition page.
5. Resist splitting a page into separate URLs to match the audit's rows; the framework's fragmentation warning applies to the audit itself as much as to the site.

**Tools:** Screaming Frog, Google Sheets

**Pitfall:** Letting the page's word count decide its type. The longest section is usually the explanatory copy, so classifying by volume turns transaction and documentation pages into 'guides' and marks them for deprioritization.

### 12. Convert a run of three parallel claims into a bullet list  `71.23`
*useful · concrete actions · source 71*

While editing the intro, Devesh hit three consecutive sentences that all had the same shape, each naming something the free brief tools fail to do. His instruction was to make this bullets. The three became a list: they do not tell you who is actually searching, they do not read what is already ranking on Google, and they say nothing about your product. He judged the passage great after the change. The mechanism is that a lead-in sentence stating the general failure followed by three parallel specifics reads as padding in prose, because the parallelism is invisible, and reads as evidence as a list, because the reader can see three distinct items rather than one repeated point.

> "You can make this bullets"

**Evidence:** Devesh converted three parallel claims about what free brief tools fail to do into bullets during the intro edit and judged the section fixed afterwards.

**How to do it**

1. Scan each section for runs of three or more consecutive sentences that share the same grammatical shape.
2. Confirm each sentence in the run carries a genuinely different specific, not the same point rephrased.
3. Write one lead-in sentence stating the general claim the run supports.
4. Convert the parallel sentences into bullets, keeping each to a single clause.
5. Delete any bullet that duplicates another, since the list format makes duplication obvious.
6. Leave prose runs alone where the sentences build on each other rather than sitting in parallel.

**Pitfall:** Bulleting a run whose items repeat each other exposes the repetition rather than hiding it, so check the items are distinct before converting. And converting sequential reasoning into bullets breaks the argument.

**Apply at Pabau:** Pabau articles that list what a manual process fails to do should use bullets, provided each item is a distinct failure. This matters most in the intro and in the section preceding a Pabau feature.

**Apply anywhere:** Convert runs of three or more parallel sentences into a bullet list under one lead-in sentence, but only when each item is genuinely distinct.

### 13. Correct the terminology inside the page, not in the title  `109.16`
*useful · best practices · source 109*

Grow and Convert close the geothermal story with a rule that keeps a deviant keyword honest. Be present for the searches people actually run, then use the post or page itself to explain the nuances of what they really need, if that distinction matters. The title, URL and opening sentence carry the searcher's wording so the page matches the query and does not pogo-stick. The correction goes in the body, after the reader has confirmed they are in the right place. This resolves the objection subject-matter experts raise, that publishing the wrong term spreads a misconception. It does the opposite: the page becomes the place the misconception gets corrected, by the company with the most expertise, for the audience holding it.

> "explain the nuances of what they *really* need"

**Evidence:** The renewable heating client ranked on erroneous geothermal terms while using the pages to explain what UK residential buyers really needed.

**How to do it**

1. Put the searcher's wording in the title, URL slug and first sentence without qualification.
2. Answer the query itself in the first two sentences before any correction.
3. Place the terminology correction in its own short section, one to three paragraphs in.
4. State the correct term, what it actually means, and why the two get confused.
5. Say plainly which of the two the reader most likely needs, given the query they ran.
6. Avoid tone that implies the reader was stupid to use the wrong word.
7. Route the reader to the accurate product or service page after the correction.
8. Have the subject-matter expert review the correction section, which is what they actually care about.

**Pitfall:** Putting the correction in the title breaks the intent match and the page never ranks for the term you targeted. Keep the correction below the fold of the answer.

**Apply at Pabau:** Pabau's articles targeting terms aesthetic practitioners consider wrong should keep the search term in the H1 and URL, answer the query first, then correct the terminology in a dedicated section. That is also what satisfies clinical and product reviewers.

**Apply anywhere:** Use the searcher's wording in the title, URL and opening sentence, answer the query first, then correct the terminology in its own section further down. The page ranks for the term people search and becomes the authoritative correction.

### 14. De-indexing low-value pages can coincide with rising traffic  `37.3`
*useful · content insights · source 37*

Jotform's blog is simultaneously losing individual pages from Google's index while its overall blog traffic keeps climbing. Edward attributes the de-indexing to Jotform pruning low-value pages that weren't ranking anyway or that sat outside the blog's topical authority (or Google doing that pruning itself), while the surviving content keeps compounding in clicks - a useful counterexample to the instinctive panic newer SEOs feel whenever a page shows as not indexed.

> "Their blog is actually seeing pages get de-indexed"

**Evidence:** Jotform's blog shows individual pages being de-indexed at the same time its total monthly blog clicks are increasing, which the video attributes to pruning of low-value or off-topic pages rather than a penalty.

**Apply:** Don't treat every de-indexed page as an emergency - check whether the page was actually driving value (rankings, clicks, topical relevance) before reacting, since pruning genuinely low-value or off-topic content can coincide with, and possibly contribute to, rising overall traffic for the remaining content.

### 15. Delete the second sentence when it restates the first  `99.11`
*useful · best practices · source 99*

Khanal isolates a specific and very common failure he says he sees all the time. A writer states a claim, then writes a second sentence that restates the same claim in different, more cutesy words. His example: 'Measuring conversions from content marketing is important. If you're serious about content marketing, you have to get serious about measuring conversions.' The second sentence adds nothing new. His rule is that you would be better off keeping only the first sentence if you have nothing different to say in the second. He applies the same rule to pain points, where the restatement often arrives as clever phrasing or a rhetorical question, such as 'If only digital marketing were easy!' He calls those useless filler sentences. The value is that this is a mechanical check an editor can run without domain knowledge.

> "That second sentence adds nothing new"

**Evidence:** Khanal's paired example of the conversions claim and its rephrased follow-up, drawn from repeated observation in freelance test drafts.

**How to do it**

1. Read the draft in sentence pairs rather than paragraphs.
2. For each pair, ask whether the second sentence adds a fact, a mechanism, a number or an example.
3. Delete the second sentence if it only restates the first with different wording.
4. Treat rhetorical questions immediately after a claim or pain point as restatements by default.
5. Treat 'if you're serious about X, you have to get serious about Y' constructions as restatements.
6. Where the restatement is deleted, decide whether to leave the claim bare or write real backup in its place.
7. Run the pass again on the intro and on the first sentence under each H2.

**Pitfall:** Restatements survive review because they read as emphasis and keep the word count up. The tell is that deleting the sentence loses no information.

**Apply at Pabau:** Add sentence-pair restatement checking to the Pabau editorial pass, alongside the AI-tell and 25-word checks. Rhetorical questions after a claim are the most frequent offender in blog intros.

**Apply anywhere:** Add sentence-pair restatement checking to your editorial pass. Rhetorical questions placed right after a claim are the most frequent offender in intros.

### 16. Diagnose a non-converting page by asking which of the two steps failed  `113.15`
*useful · concrete actions · source 113*

Grow and Convert's framework doubles as a diagnostic because the failure modes are separable. If you get Step 1 wrong and target keywords without buying intent, no Step 3 tactic, well-crafted headlines, banner CTAs or CRO hacks, will make the content convert. If you nail Step 1 but fail Step 2 by writing generic content that does not sell your specific product, you might generate traffic but not conversions. So the observable pattern tells you where to look: traffic present and conversions absent points at the writing, while traffic present from the wrong searchers points at the keyword. The value of the split is that it stops teams from applying CRO fixes to a keyword problem, which is the failure Grow and Convert say they see most often in clients arriving with good design.

> "you might generate traffic but not conversions"

**Evidence:** Grow and Convert report clients arriving with good headlines, clean blog design and good user experience whose content still barely converted.

**How to do it**

1. Pull the page's queries from Google Search Console and check whether they are category, comparison or jobs-to-be-done queries.
2. If the queries carry no buying intent, stop: this is a Step 1 failure and the page needs re-targeting or retiring, not editing.
3. If the queries do carry buying intent but conversions are near zero, read the body copy for the product section.
4. Score the product section: is the product named, are features tied to a pain point, is a named competitor differentiated against, is there proof.
5. Rewrite the failing part of that section rather than the headline or the CTA.
6. Recheck conversions after four to six weeks and only then consider layout or CTA changes.
7. Log which step failed for each audited page, so you learn whether the systemic problem is keyword selection or writing.

**Tools:** Google Search Console

**Pitfall:** Editing headlines and CTAs on a page whose queries carry no buying intent. The metrics never move and the team loses confidence in content rather than in the keyword list.

**Apply at Pabau:** David should add this two-question diagnostic to the Pabau content audit: pull the GSC queries first, then read the Pabau section. Only pages that pass both go to the editorial or CTA queue.

**Apply anywhere:** Diagnose a non-converting page in two questions. Pull its GSC queries: no buying intent means re-target the page. Buying intent but no conversions means rewrite the product section, not the headline.

### 17. Diagnose generic content as two separate flaws, not one  `174.4`
*useful · content insights · source 174*

Khanal separates the causes of mirage content into two distinct failures, and they need different fixes. The first is the Google Research Paper approach: a freelancer with no expertise researches by Googling the topic, reading the top 10 results, and rehashing what those articles said, which reads like a high school research paper. The second is that the article is not specific enough, covering broad concepts at a high level and never reaching the details people actually care about. He notes the second flaw is itself a function of the first, since a writer without expertise has no specifics to reach for. Separating them matters for diagnosis: a piece can be written by a genuine expert and still fail on specificity, and an outline can be specific but still filled from the SERP.

> "The second flaw was that most articles weren't specific enough"

**Evidence:** Khanal's 2016 Mirage Content article identified these as the two flaws in the content production process, and he argues AI reproduces exactly the same approach faster.

**How to do it**

1. Audit a weak article for flaw one: check whether its sources are the pages currently ranking for its keyword and nothing else.
2. Audit for flaw two separately: count how many concrete numbers, named tools, screenshots or worked examples appear per 1,000 words.
3. Fix flaw one by adding a source outside the SERP, an internal expert interview or first-party data.
4. Fix flaw two by replacing each broad concept section with the specific decision a reader faces at that step.
5. Set a floor in the brief, such as at least one concrete example or figure per H2, and hold drafts to it.
6. Track which flaw each rejected draft failed on, so you can tell whether the problem is sourcing or briefing.

**Pitfall:** Assuming an expert byline fixes both flaws. Experts write vague high-level copy all the time when the brief asks for broad coverage; the specificity flaw needs a brief-level fix even when the sourcing is solid.

**Apply at Pabau:** When auditing an underperforming pabau.com article, David should record which of the two flaws caused it. Sourcing-only failures get an expert input pass. Specificity failures get a brief rewrite that names the actual decision a clinic manager faces at each step, such as which fields to require at booking.

**Apply anywhere:** When a page underperforms, diagnose which of two flaws caused it. Flaw one is sourcing everything from the pages already ranking. Flaw two is covering broad concepts without ever reaching the specifics readers care about. Sourcing failures need input from outside the SERP; specificity failures need the brief rewritten around the reader's actual decisions.

### 18. Diagnose meandering writing by reading the draft aloud  `124.7`
*useful · best practices · source 124*

Grow and Convert give a specific test for structureless writing. Read it aloud, and if it sounds like listening to a kid tell you about their day at school, it is meandering. They name two costs. The reader gets confused about the main point, and the writer loses the ability to check whether everything that needed covering was covered. They add a third and sharper cost: rambling hides gaps in the argument, so without clarity you cannot tell whether you are actually making the point you intended. That reframes the problem from readability to correctness. Their fix is the bullet-point rewrite, but the read-aloud test is what tells you a passage needs it in the first place.

> "like listening to a kid tell you about their day at school"

**Evidence:** Grow and Convert report writers regularly submitting work that jumps from point to point without clear structure, and use the read-aloud test as the first diagnostic.

**How to do it**

1. Read every draft section aloud before submitting, at normal speaking pace.
2. Flag any passage that sounds like an unstructured recount rather than an argument.
3. For each flagged passage, try to state its single main point in one sentence out loud.
4. If you cannot, treat the passage as hiding a gap in the argument, not just a style problem.
5. List what the section was supposed to cover and check each item is actually present.
6. Rewrite the passage as labeled bullets to expose the missing support.
7. Reread aloud after the rewrite to confirm the main point now lands first.
8. Repeat on the introduction last, since it is the section most likely to ramble.

**Pitfall:** Assuming rambling is only a style issue. It usually means the argument has a hole, and polishing the sentences leaves the hole in place.

**Apply at Pabau:** Pabau's editorial pass should include a read-aloud check on every section, not just the intro. Where a section fails, treat it as a missing-evidence problem and go back to the interview notes rather than rewording.

**Apply anywhere:** Read each draft section aloud and flag anything that sounds like an unstructured recount. Then try to state the section's point in one sentence; if you cannot, the argument has a gap, not a style problem.

### 19. Distrust pillar pages that chase dozens of keywords at once  `179.9`
*useful · content insights · source 179*

Grow and Convert name over-reliance on pillar page strategies as a related failure to keyword sprinkling. The theory is appealing: build one large page covering a broad topic, then link out to smaller related pages. In practice they see those pillar pages trying to rank for dozens of keywords simultaneously and ranking well for none of them. Their explanation is intent, not length. Each keyword carries its own search intent, and a single page can rarely satisfy several intents at once. This connects to their broader argument about user experience: when someone searches a specific query, they want content that addresses that query directly, and a page clearly written for them holds attention, answers more thoroughly and converts better. Pages that match intent outperform pages that only relate to the topic, which is why both sprinkling and sprawling pillars underperform.

> "end up ranking well for none of them"

**Evidence:** Grow and Convert say pillar pages built to cover a broad topic commonly rank well for none of the dozens of keywords they target, because each keyword has its own intent.

**Pitfall:** Judging a pillar page by its total keyword count in a rank tracker. A page ranking on page four for forty terms looks productive in a report and earns almost nothing.

**Apply at Pabau:** If Pabau builds a hub page for a broad area such as clinic management, it should be scoped to one intent and used to route to dedicated pages, not to absorb every related keyword itself.

**Apply anywhere:** A pillar page that targets dozens of keywords usually ranks well for none of them, because each keyword carries its own intent and one page rarely satisfies several at once. Scope a hub page to a single intent and let it route to dedicated pages that each own one query.

### 20. Do not force 10X content on low-competition, high-intent terms  `100.12`
*useful · content insights · source 100*

Grow and Convert name their disagreement with Rand Fishkin's 10X content directly. Rand's central thesis in his 2015 video is that good unique content is not enough. They answer 'kind of', and split it two ways. First, their definition of an originality nugget is much stricter than Rand's phrase 'good unique content', which they read as describing basic me-too content, noting he says it should be good enough not to vomit. A nugget has to make the reader think 'oh, that's interesting'. Second, their work suggests you do not always need 10X to rank, particularly for less competitive terms. They accept that ranking #1 for a head term like 'SEO' needs 10X, but argue that terms like 'yourbrand vs. yourcompetitor vs. anothercompetitor' do not, and that their Pain Point SEO framework shows leads driven from very low volume keywords.

> "you don't always need 10X content to rank"

**Evidence:** Grow and Convert cite their Pain Point SEO framework driving leads via rankings on very low volume keywords, and contrast it with Moz's guide ranking #1 for 'SEO'.

**Pitfall:** Applying a head-term quality bar to a long-tail comparison keyword wastes months for the same ranking a strong short piece would win. The signal is a 15,000-word draft aimed at a keyword with three-figure volume.

**Apply at Pabau:** Pabau's vs-competitor and alternatives pages do not need to be exhaustive studies. David should ship them fast with a genuine angle and reserve the heavy effort for head terms in aesthetic practice management.

**Apply anywhere:** Match the quality bar to the term. Head terms genuinely need a 10X effort; low-volume, high-intent comparison and alternatives pages need only a real angle done quickly.

### 21. Do the original work first and treat writing as the last step  `100.19`
*useful · best practices · source 100*

Describing the heavy originality tier, the author says these posts often take a bunch of work that needs to be done beforehand, and the actual writing of the post is just the last step, like a scientist writing a research paper after two years of lab work. The mobile checkout study is the illustration: months of auditing 40 sites, a giant spreadsheet, then charts, then AB test results, then writing. This reorders how a heavy piece is planned and staffed. The deliverable schedule is a data-collection schedule, not a drafting schedule, and the writer is assigned at the end rather than the start. It also means the piece cannot be commissioned from a freelancer as a writing job, because the value sits in the work that precedes the words.

> "the actual "writing" of the post itself is just the last step"

**Evidence:** The Growth Rock mobile checkout study took months of page-by-page analysis across 40 sites before any writing, and ranks #1 for two terms.

**How to do it**

1. Scope the underlying work first: the audit, the test, the tool or the interviews.
2. Schedule the data collection with its own deadline, separate from the publication date.
3. Assign the collection to whoever can actually do it, not to the writer.
4. Store raw findings in one shared spreadsheet so charts can be regenerated later.
5. Only brief the writer once the findings exist, and give them the raw data, not a summary.
6. Budget the writing at a fraction of the total project time.
7. Plan a refresh cadence for the data, since a study dates faster than an opinion piece.

**Pitfall:** Commissioning a heavy piece as a writing assignment produces a long article dressed as a study with nothing new underneath. The signal is a draft whose data all comes from other people's published research.

**Apply at Pabau:** For a Pabau study, David should schedule the audit or data pull as its own project with its own owner and deadline, then brief the writer afterwards with the raw spreadsheet.

**Apply anywhere:** Plan a heavy piece as a research project with the writing as its final step. Schedule and staff the data collection separately, and brief the writer only once findings exist.

### 22. Don't build tools an AI interface can already run  `66.29`
*useful · best practices · source 66*

Calculators, quizzes and generators that apply a basic formula or produce a shallow answer from inputs an AI interface can handle directly. The framework's keep-condition is specific: keep it only when live or proprietary data, meaningful personalization, repeat use or a clear product action makes the output actually useful. It covers generic quizzes, calculators and generators with no live data, personalization depth, recurring use, distinctive output or credible product journey. It scores Low on all five value dimensions at Medium effort. The type is worth flagging because the build is cheap enough to feel like a low-risk experiment and it produces a page that looks like a prioritized tool, so it consumes engineering capacity while landing in the deprioritized list. The four keep-conditions are the specification for the prioritized version of the same idea — and the fastest way to test any tool concept is to put the same inputs into an AI interface before building it.

> "applies a basic formula or produces a shallow answer from inputs an AI interface can handle directly"

**How to do it**

1. Before building any tool, put its inputs and question to an AI interface and see what comes back. A usable answer means the tool is this type.
2. Test the concept against the four keep-conditions: does it need live or proprietary data, does it personalize meaningfully, will the same user return to it, and does it lead to a clear product action?
3. If none holds, do not build it. If one can be made to hold, redesign the concept around that condition rather than building the generic version first.
4. For tools already live, run the same test and score each against the four conditions.
5. For the failures, decide by usage: retire the unused ones, and for the used ones add the missing condition — wire in live or proprietary data, deepen the personalization, or attach a real product next step.
6. Where a generic calculator draws genuine traffic, keep the page but replace the generic formula with one driven by your own benchmarks, which converts it into the prioritized type.
7. Consolidate multiple near-identical generators into one, since they are also the fragmented-variant type.
8. Add the AI-interface test to the tool intake process, so the check happens before engineering time is committed.

**Tools:** ChatGPT

**Pitfall:** Judging the tool by its build cost. Medium effort sounds cheap enough to try, but it buys a page that scores Low on all five value dimensions and occupies the slot a proprietary-data tool would have filled.

**Apply at Pabau:** Test any Pabau calculator or quiz idea in ChatGPT first. If it answers usefully, build something else — or rebuild the concept on Pabau's own benchmarks and the practice's own numbers, which is what moves it into the prioritized tools type.

**Apply anywhere:** Test any calculator or quiz idea in an AI interface first. If it answers usefully, build something else — or rebuild the concept on your own benchmarks and the customer's own numbers, which is what moves it into the prioritized tools type.

### 23. Drop the rule that content must not sell  `182.11`
*useful · content insights · source 182*

Grow and Convert name a cultural belief they blame for top-of-funnel drift: that the role of content is not to sell, only to build brand awareness, capture people at the top of the funnel and nurture them over months or years through email automations and remarketing ads until they eventually buy. They call that culture completely misguided. Their argument is not that awareness has no value but that it is chosen as the default while people are actively searching to buy right now, and that a strategy which does not show up in those buying discussions leaves extremely qualified leads on the table. The practical consequence is permission: an article aimed at a buying query is allowed to argue for the product, compare it to alternatives and ask for the demo.

> "the role of content isn't to sell"

**Evidence:** Grow and Convert attribute the top-of-funnel default in B2B content marketing directly to this belief and reject it explicitly.

**How to do it**

1. Write the product recommendation into bottom-funnel articles rather than saving it for a nurture sequence.
2. Place the call to action where the reader reaches a decision, not only at the end.
3. Say plainly what your product replaces and who it is not for, since a comparison that never picks a side does not convert.
4. Keep the nurture track for genuinely early-stage readers instead of routing buyers into it.
5. Judge these pieces on demo requests, and accept lower pageviews as the trade.

**Pitfall:** Overcorrecting turns an informational article into a pitch and loses the ranking, because the page no longer satisfies the query. Selling belongs in articles whose query is already commercial.

**Apply at Pabau:** Pabau's comparison, alternatives and best-software pages should argue for Pabau openly, with the demo link where the reader decides. Blog explainers keep the softer introduction on first mention.

**Apply anywhere:** Let articles that target buying queries actually sell: recommend, compare, say who the product is not for, and ask for the next step in the body of the page.
