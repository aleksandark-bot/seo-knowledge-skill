# Content Production — core (part 4 of 8)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Make the brief name the ICP and the pain point driving the search  `71.21`
*core · ai workflows · source 71*

Devesh's brief identifies which of the business's target customers is searching for the keyword and what pain point is driving the search, because the tool has already read a corpus about the business and produced a brand summary. For 'AI content brief generator' it named marketing managers, content marketers, freelance writers, solo marketers and agency account managers, and it named the pain point as briefs being shallow rather than briefs being slow. He corrects it in passing, judging directors too senior and agency owners less likely than the writers inside agencies. He argues a brief without this is broken: without a real persona the outline and article will not speak to your ICP, and in SEO you are writing for the searcher, so the writer needs to know who that is.

> "Does it identify which of your customers is searching"

**Evidence:** The brief for 'AI content brief generator' named five customer profiles and identified shallowness, not speed, as the dominant pain point, which Devesh accepted after cutting directors from the list.

**How to do it**

1. Feed the writing tool a corpus about your business so it can produce a brand summary before any brief is generated.
2. For each keyword, have the brief name which of your defined customer profiles is doing that specific search.
3. Have it state the pain point driving the search, phrased as a problem rather than a topic.
4. Review and correct the list yourself, cutting profiles that are too senior or too peripheral to actually run the query.
5. Where two pain points are proposed, pick the dominant one and say so, since it sets the article's angle.
6. Reject any brief that arrives without a named searcher and a named pain point.

**Tools:** Wave Writer

**Pitfall:** Generated persona lists skew senior and generic. Devesh cut directors as too high and reframed agency owners as the account managers and writers who actually do the work, so the list needs a human correction pass every time.

**Apply at Pabau:** Pabau briefs should name whether the searcher is a clinic owner, a practice manager or a front-desk coordinator, and which of their problems drives the query, since those three read the same article very differently.

**Apply anywhere:** Require every brief to name which customer profile runs that specific search and the pain point behind it, then correct the generated list yourself. Persona lists skew too senior by default.

### 2. Match every content format to a promotion channel that can carry it  `136.9`
*core · best practices · source 136*

Grow and Convert name the failure they hit as a content-promotion mismatch. Their promotion engine was community sharing, which works for magazine-style stories people read while browsing Facebook or Reddit, and fails completely for lists of tools and product comparisons. Those posts are meant for Google, to appear when the right person asks for that exact information. When they switched formats without switching channels, traffic dropped. The fix was to pair each format with a channel that suits it: pain point posts get early traffic from paid Facebook and long-term traffic from organic search, stories get communities. The early traffic matters beyond the visits, because it puts the post in front of people who link to it, which speeds up how fast Google ranks it.

> "has fixed our content-promotion mismatch"

**Evidence:** Grow and Convert saw blog traffic dip after switching to pain point SEO precisely because those posts do not spread in communities, and recovered once paid Facebook plus link building replaced community promotion.

**How to do it**

1. List every content format you publish in one column and the promotion channel that will carry it in the next.
2. Mark any format whose only channel is community sharing or organic search as a mismatch risk.
3. For commercial, utilitarian posts, plan a paid traffic push at publication instead of a community push.
4. For story and research posts, plan the community and outreach push and skip the paid spend.
5. Never change format mix without changing the promotion plan in the same decision.
6. Measure whether the early traffic push is producing referring domains, not just sessions.
7. Drop any channel that stops producing after two quarters of testing, as community promotion did for them in late 2018.

**Tools:** Facebook

**Pitfall:** Changing what you publish while keeping the old promotion motion. The new posts get no early traffic, no early links, and rank slower than they should, which reads as the content being wrong.

**Apply at Pabau:** Pabau's comparison and template pages should not rely on the same distribution as its story articles. Plan a paid push or a targeted outreach list for each commercial page at publication, and reserve social and community sharing for the story pieces.

**Apply anywhere:** Pair each content format with a promotion channel that suits it. Utilitarian bottom-funnel posts need paid traffic or outreach at publication; stories need communities. Never change your format mix without changing the promotion plan alongside it.

### 3. Match sentence subject to the query's subject entity (microsemantics)  `03.6`
*core · concrete actions · source 03*

Microsemantics is demonstrated with two sentences stating the identical fact but differing in which entity is the grammatical subject: financial independence is achieved by families with the help of financial advisors, versus financial advisors help families achieve financial independence. Despite equivalent meaning, these phrasings score differently for relevance depending on the query network targeted, because Google's query augmentation (query fan-out) matches the subject-predicate-object structure of a sentence against the structure of the target query. The rule: if an entity is the subject of the target query, the sentence should have that same entity as its grammatical subject; because this is a per-sentence micro-effect, it compounds — on a query template with 3,000 variations, getting subject-alignment right on every sentence turns a small individual improvement into a major aggregate ranking factor.

> "Micro differences in word order and in the dependency tree create relevance"

**How to do it**

1. For each target query variation, identify which entity functions as the grammatical subject in how users phrase that query.
2. Rewrite the on-page sentence covering that fact so the same entity occupies the subject position, restructuring the sentence as a subject-predicate-object triple mirroring the query.
3. Do this consistently for every distinct query variation/entity targeted on the page, rather than writing one generic sentence and assuming meaning alone carries relevance.
4. Where a single page targets many query variations, audit a sample of sentences against their corresponding query subjects to confirm subject alignment throughout, since the effect compounds at scale. (inferred)
5. Treat this as a rewriting/editing pass distinct from keyword insertion — the words used can stay identical between two sentence versions; only the grammatical subject position changes.

**Pitfall:** Assuming that stating the same fact is enough because the meaning is identical — relevance scoring is sensitive to which entity sits in the subject position of a sentence relative to the query's own subject, so semantically-equivalent sentences can score very differently.

### 4. Match the page type the SERP already ranks before choosing article format  `108.6`
*core · best practices · source 108*

Grow and Convert put page-type matching ahead of subtopic coverage in their SERP analysis. Before looking at what the top results say, look at what they are: list posts, step-by-step guides, comparison articles, landing pages or something else. Their worked example is 'project management software for agencies'. If the top results are all listicles comparing tools, searchers want options to evaluate, not a landing page pitching one product. Build the landing page anyway and you will not reach page one, because you are not matching what searchers and therefore Google expect. This is the format decision that governs everything downstream, and it is the reason SaaS product pages lose category terms. Once the format is fixed, click into the top three to five results and list the subtopics they share, since a missing subtopic that every top result carries signals incompleteness to Google.

> "If you create a landing page when Google is ranking listicles"

**Evidence:** Grow and Convert's example of 'project management software for agencies', where an all-listicle SERP means a product landing page cannot reach page one.

**How to do it**

1. Search the target keyword and classify each of the top ten results by page type.
2. Take the majority page type as the format your page must adopt.
3. Where a listicle wins, build a listicle even if the keyword names your own category.
4. Where guides win, do not publish a product page, whatever the sales team prefers.
5. Click into the top three to five results and write down every section each one includes.
6. Mark any subtopic that appears in all of them as mandatory in your outline.
7. Include pricing and comparison tables when every top result carries them.
8. Differentiate on angle, data and examples, not by changing the format.
9. Recheck the format mix if the page stalls outside the top 20 after three months.

**Pitfall:** Choosing format from what the business wants to publish rather than from the SERP. The signal is a landing page that never breaks page two for a term whose SERP is entirely listicles.

**Apply at Pabau:** Before Pabau writes anything for a software-category term, classify the top ten by page type. Most aesthetics-software SERPs are listicles, so those keywords belong to /blog/ roundups, not to a feature page.

**Apply anywhere:** Classify the top ten by page type before deciding your article format. Adopt the majority format, cover every subtopic all top results share, and differentiate on substance rather than by picking a different page type.

### 5. Mine an existing draft's subsections for nine standalone post ideas  `98.4`
*core · concrete actions · source 98*

Hyam's refactoring move, done on a live draft. Working with Sara Binde of Carob Cherub, they used the suggested search hack to find 'Why Am I Fat' as a high-volume question and she wrote the post. Reading her draft, he realized each subsection could be a post of its own, and pulled out nine: how to deal with bullies when you're overweight, diets don't fix unhealthy eating habits, the problem with 'stop eating', skinny kid fat adult, how the media is to blame for self confidence issues, why you shouldn't go to your doctor for nutrition advice, why you shouldn't listen to your mother, why food labels lie, and why science is best for nutrition advice. He kept the original post, which he expected to rank on the long tail because it was better than the alternatives. The subsections became the pipeline.

> "each of her subsections could've been entire posts of their own"

**Evidence:** One post, 'Why Am I So Fat?', yielded nine specific post ideas from its subsections.

**How to do it**

1. Open a recently published long post and list every H2 and H3 it contains.
2. For each subheading, ask whether a reader could search for that alone as a question.
3. Keep the ones that pass and discard the ones that only make sense inside the parent piece.
4. Rewrite each survivor as a standalone headline that names the specific situation or claim.
5. Check each headline for a real query using Google suggested search or a keyword tool before committing.
6. Write each as a deep post that goes further than the two or three paragraphs the parent gave it.
7. Internally link every new post back to the parent, and link the parent's subsection down to its dedicated post.
8. Repeat the pass on your next-best-performing long post rather than starting from a blank ideation session.

**Tools:** Google

**Pitfall:** Splitting a section out and then leaving the parent's version untouched creates two pages saying the same thing. Cut the parent's coverage back to a summary plus a link when you publish the child.

**Apply at Pabau:** Pabau's longest existing blog posts are an ideation backlog. Take a 3,000-word guide, list its H2s, and check which ones are questions practice owners search on their own. Those become the next quarter's briefs, each linked back to the parent.

**Apply anywhere:** Treat your own long-form posts as an idea backlog. Each subsection that reads as a standalone question is a post you can write in far more depth, with the parent piece providing the internal link.

### 6. Mine daily executors in the weeds for tactic-level thought leadership  `125.5`
*core · concrete actions · source 125*

Grow and Convert make the point that thought leadership does not have to come from the CEO and does not have to be groundbreaking. The unique ideas often come from the weeds, the details the daily executors are mired in: designers in a product company, strategists and account managers in a service company. Product managers will describe very specific nuances of how their product works differently from other solutions. Their example is a client selling paid ad services whose account manager had a specific Facebook ad strategy of layered ads for the same company, progressing from loose brand awareness to specific conversion-focused buy-now ads, applied to ecommerce companies. They call it very specific and say it worked well as thought leadership. Narrowness is the asset here, not a problem to be broadened away.

> "the details that the daily executors in the company are mired in"

**Evidence:** Grow and Convert's client in paid ad services: an account manager's layered Facebook ad strategy progressing from brand awareness to buy-now conversion ads, scoped to ecommerce companies, worked as thought leadership.

**How to do it**

1. List the people who execute daily rather than manage: product managers, strategists, account managers, designers, support leads.
2. Book 30 minutes with each and ask what they do differently from how they were taught or from how competitors do it.
3. Ask specifically which nuance of the product they end up explaining to every customer.
4. Capture the segment the tactic applies to, since narrow application is what makes it credible.
5. Write it up at full specificity, including the sequence and the thresholds, not as a general principle.
6. Keep the executor's name on the piece as the source of the method.
7. Do not broaden the tactic to sound more widely useful; the narrowness is the differentiation.

**Pitfall:** Editors sand the specificity off to widen the audience, and the piece becomes another general best practices post. The signal is that the final draft no longer names a segment or a sequence.

**Apply at Pabau:** Pabau's account managers and onboarding specialists hold setup sequences that no competitor documents. David should interview them for one specific configuration workflow per article rather than restating generic practice management advice.

**Apply anywhere:** Interview the people who execute daily, not just leadership. Write up one specific tactic at full detail, including its sequence and the segment it applies to, and resist the urge to generalize it.

### 7. Move top-of-funnel content to Reddit and social, not your blog  `26.3`
*core · content insights · source 26*

When launching new sites, Dooley's team now deliberately publishes less top-of-funnel informational content directly on the client's own domain, because AI Overviews increasingly intercept and satisfy those broad informational queries before the user ever clicks through. Instead of writing that content as on-site blog posts, they place top-of-funnel material on Reddit and social media and link it back to the site, treating those platforms as the new top-of-funnel real estate. New site launches focus the roughly 50 initial pages on core service/commercial pages plus only the informational content judged necessary, rather than broad blog coverage.

> "AI Overviews are taking a lot of the clicks away"

**Evidence:** "A lot of the time though we're doing a lot less top-of-funnel, just because AI Overviews are taking a lot of the clicks away. So we might put the top of the funnel on, let's say, Reddit and social media and link it back through to the website."

**Apply at Pabau:** Pabau should reassess how much budget goes into broad, awareness-stage blog content likely to be fully answered by an AI Overview, and consider testing Reddit/community engagement or social posts for those same topics (linking back to the site) rather than defaulting every topic to an owned blog post.

**Apply anywhere:** You should reassess how much budget goes into broad, awareness-stage blog content likely to be fully answered by an AI Overview, and consider testing Reddit/community engagement or social posts for those same topics (linking back to the site) rather than defaulting every topic to an owned blog post.

### 8. Name one primary pain, never a list of ten features  `91.4`
*core · best practices · source 91*

Grow and Convert warn that most companies want to talk about the many problems their product solves and the numerous benefits it delivers. That belongs on the website, not in a disruption story. Their line is that nobody stops scrolling social for an article whose angle is 'Here's our product and its 10 core features'. They frame the difference as a Product Hunt listing versus a story, and say the piece has to lean into the why behind the product. The three questions they use to get there: why was it created, what problems were so severe that you set out to build your own solution, and what are you disrupting and why. This is the discipline that makes the narrative land, because a single severe pain is something a reader recognizes in themselves, while a benefit list is something they skim.

> "You're not creating a Product Hunt listing, you're writing a story"

**Evidence:** Grow and Convert's experience writing dozens of these; they cite the '10 core features' angle as the one that fails on social.

**How to do it**

1. List every problem your product solves, then force-rank them by how much the target reader complains about them.
2. Keep only the top one as the story's spine and move the rest to the product pages.
3. Answer, in writing, why the product was created and what problem was severe enough to justify building it.
4. Answer what you are disrupting and why the current way is flawed.
5. Rewrite the narrative sentence so it contains one pain and one solution, no conjunctions stacking extra benefits.
6. Delete any paragraph in the draft that introduces a second unrelated pain.
7. Keep secondary features in the body only where they visibly serve the one named pain.

**Pitfall:** Stakeholder review pulls the extra benefits back in, one per reviewer, and the story degrades into a feature roundup. Watch for the draft growing a section per department.

**Apply at Pabau:** Pabau's product breadth is the temptation here. A Pabau disruption story should pick one pain, most likely the admin load of running an aesthetic practice on disconnected tools, and leave the full feature set to the product pages.

**Apply anywhere:** Pick the single most severe pain your product was built to fix and build the whole story on it. A list of ten benefits belongs on your website; it will not stop anyone scrolling social.

### 9. Open a subscription-business engagement with four specific post types  `141.6`
*core · concrete actions · source 141*

For the VC-backed subscription client at a $500 a month price point, Grow and Convert name the exact opening slate. First, a comparison post against competitors, chosen because there was search volume around comparing the company to competitors and no page on their site objectively explaining the difference. Second, a post targeting category search terms, which they class as middle to bottom of funnel. Third, a couple of posts going after product use cases, which they call mid-funnel. Fourth, a founder story explaining the vision for why he started the company and the problem he was solving, included because those pieces do well from a promotion standpoint rather than a search one. Note the ordering logic: the gap they spotted first was an objective comparison the company had never written, and they treated that missing page as the highest-priority build.

> "there was search volume around comparing this company to competitors"

**Evidence:** Grow and Convert used exactly this slate for a VC-backed subscription business selling to startups and small businesses at $500 a month; the comparison post produced the client's first organic conversion in month 2.

**How to do it**

1. Search your brand name plus 'vs' and each named competitor and check whether any page on your own site answers it objectively.
2. If none exists, write the comparison post first; it is the most bottom-funnel piece available.
3. Add one post targeting the category search terms, the phrase a buyer uses when they know the product type but not the vendors.
4. Add two posts on specific product use cases, framed around the job the buyer is doing rather than the feature.
5. Write one founder story covering why the company was started and which problem it solves, and budget it as a promotion asset, not a ranking asset.
6. Skip top-of-funnel entirely if the category already has demand and you are not creating a new product category.
7. Track conversions per post from month one and let the first organic converter tell you which format to repeat.

**Pitfall:** Teams skip the comparison post because writing objectively about competitors feels risky, leaving the highest-intent query in the category to a review site or the competitor's own page.

**Apply at Pabau:** Pabau should confirm a published, objective comparison page exists for every practice-management competitor buyers actually shortlist, plus one category page for terms like aesthetic clinic software, and treat those as higher priority than another top-funnel treatment guide.

**Apply anywhere:** Open a new content program with four pieces: an objective comparison against your named competitors, one category-term post, two use-case posts, and a founder story built for promotion rather than search. Write the comparison first if no page on your site answers it.

### 10. Open an expert interview by stating what you already understand  `134.4`
*core · concrete actions · source 134*

Grow and Convert's first advanced interviewing tactic. They note most subject matter experts are not trained communicators, so with no idea of your baseline they oversimplify and use language they would never use with peers. Repeat that back in an article and you write below the audience's knowledge level, or get it wrong. The fix is to embed your current understanding in the question. Their Rainforest example, paraphrased from an early call: what I understand about software testing is that most tools don't test exactly what the user sees and instead test the code itself, and that's a problem because you can miss visual bugs, but what I don't understand is whether those tools are still considered to be testing the user interface even though the test doesn't happen on the user interface. That question is long on purpose. The contrast case is asking 'so what differentiates your product?' and getting cliches already on the website.

> "Most SMEs aren't experts in communicating about their expertise."

**Evidence:** Grow and Convert used this framing in early Rainforest QA interviews and credit it for writing at the knowledge level of QA specialists and developers.

**How to do it**

1. Write each question in two halves: what I understand is X, what I don't understand is Y.
2. Put the specific technical detail you found in research into the first half, so the expert can correct it.
3. Restrict the second half to something you genuinely could not answer online.
4. Delete any question whose answer already appears on the client's website.
5. When the expert oversimplifies anyway, say the peer-level version back and ask if that is right.
6. Keep the corrected version in your notes as the phrasing to use in the draft.

**Prompt / template:**

```text
What I understand about [topic] is that [specific mechanism you found in research], and this is a problem because [consequence], but what I don't understand is, [precise question you could not answer online]?
```

**Pitfall:** Broad opening questions such as 'what makes you different' return the elevator pitch, and the writer leaves with material already published on the product page. The tell is an interview transcript you could have written before the call.

**Apply at Pabau:** When David interviews a Pabau product owner for an article, the question should carry the specific mechanism already found in the docs, so the expert corrects a detail rather than explaining practice management from scratch.

**Apply anywhere:** Frame every expert question as 'here is what I understand, here is the exact thing I could not resolve'. It calibrates the expert to your level and stops them handing you the elevator pitch.

### 11. Open bottom-funnel posts by teaching the reader how to judge the category  `72.3`
*core · concrete actions · source 72*

Khanal's intro framework for bottom-of-funnel listicles is to teach the reader how to think about the product space rather than to introduce the topic. He frames it as honestly stating your view of the world: here are the categories, here is what actually matters, here is what most comparisons get wrong. He argues this is what separates a self-promotional listicle that ranks stably from one that gets penalized, and says his agency has run these for ten years without a client being dinged. His concrete version opens by naming the reader's real question, 'does it do anything I can't already do?', states his agency's ten-plus years of experience, and then lists the three factors to evaluate on. The reader self-selects: agree with the framing and keep reading, disagree and leave.

> "teach the user and set up this idea of teaching them"

**Evidence:** Khanal says Grow and Convert has published self-promotional listicles for ten years with stable rankings and no client penalized for them.

**How to do it**

1. Write down the one skeptical question the buyer actually has about the category, in their words.
2. Open the intro with that question rather than with a definition of the category.
3. State your own credential in one concrete clause, such as how many years you have done this work.
4. List three factors the reader should evaluate on, framed as questions they can ask any vendor.
5. Make each factor something you genuinely believe matters, not a feature list dressed as advice.
6. Say plainly that this is your view of the space so the reader can self-select.
7. Cut any sentence that only restates that the market is crowded and confusing.

**Pitfall:** Writing the generic version instead: 'these days AI writing is important because it helps you scale'. Khanal says nobody who gets penalized for self-promotional listicles is writing an intro at this level of nuance.

**Apply at Pabau:** Pabau's 'best practice management software' and similar comparison pages should open with the objection a clinic owner actually has, plus three evaluation questions drawn from what Pabau genuinely does well, instead of a generic paragraph about the crowded software market.

**Apply anywhere:** Open your comparison pages with the buyer's real objection, then give three evaluation questions you genuinely believe in, so readers can self-select rather than wade through a generic market intro.

### 12. Open the intro on the reader's exact pains, not a generic struggle  `91.6`
*core · best practices · source 91*

Grow and Convert say the number one goal of a disruption story intro is getting the problem right, so the target reader thinks 'Yes! That's exactly it. They get me.' Their example is Vocal Video's opening line: creating video testimonials is time consuming, difficult to coordinate, and expensive, no matter what service you use, and even if you do it yourself. They point out what makes it work. It does not say companies struggle to create video testimonials. It names the three specific things that make it painful, then pre-empts the workaround most companies reach for, doing it themselves. They give a structural formula for the intro too: some combination of here's what everyone else is doing or how it is typically done, here's why we think that is flawed or what led us to believe it was a problem, and a preview of the solution you provide. How you weight those depends on how well the audience already understands the problem and how complicated your solution is.

> "They didn't just say 'Companies struggle to create video testimonials"

**Evidence:** Vocal Video's live opening line, cited by Grow and Convert as the model; they also note SEO listicle readers skim intros while disruption-story readers do not.

**How to do it**

1. List three to five concrete attributes of the pain, in the words the reader would use, for example time consuming, hard to coordinate, expensive.
2. Write the first sentence using those attributes rather than the abstract noun 'struggle' or 'challenge'.
3. Add the workaround the reader has probably already tried and name it explicitly.
4. Follow with a sentence on how the problem is typically handled across the industry.
5. Follow with why you think that standard approach is flawed, or what made you see it as a problem.
6. Close the intro with a one-line preview of your solution, not the full explanation.
7. Judge the weighting by audience knowledge: explain the problem more when readers only feel the symptoms.
8. Read the intro aloud and cut it if a target reader would not think 'that's exactly it' by sentence two.

**Pitfall:** Abstract pain statements read as true and land as nothing. If the opening sentence could be pasted into a competitor's article unchanged, it is too generic to earn the read.

**Apply at Pabau:** Rewrite the intros on Pabau's positioning and template pages the same way. Instead of 'practices struggle with admin', name it: double-entered patient data, no-shows chased by hand, consent forms on paper, card payments reconciled separately.

**Apply anywhere:** Open on the specific attributes of the pain in the reader's own words, then name the workaround they have already tried, then say why the standard approach is flawed, then preview your solution in one line.

### 13. Pair cold and lookalike paid ads with link building once pages rank  `178.8`
*core · concrete actions · source 178*

Grow and Convert run a two-pronged promotion process, split by time horizon. Short term, paid ads carry traffic while pages are still climbing, with two targeting methods: cold audiences built on interest and demographic targeting, and lookalike audiences built from the client's existing customer list or website visitors. They test Facebook, Twitter, LinkedIn and Google Ads and pick per client based on where that audience actually is. Long term, they wait for the trigger. Once a piece starts ranking for its keyword, they deploy manual link building to push it onto page one or to the top of page one. The sequencing matters: links go to pages that have already proved they can rank, not to every new publication. They fund both from their own budget with no extra client spend, which they present as the difference between a full-service agency and a writing supplier.

> "and lookalike audiences (based on the client's existing customer list"

**Evidence:** Grow and Convert fund both the paid promotion and the link building from their own budget with no extra spend for clients.

**How to do it**

1. Build two paid audiences per client: an interest and demographic cold audience, and a lookalike from the customer list or site visitors.
2. Test across Facebook, LinkedIn, Twitter and Google Ads, then keep only the channel where that audience concentrates.
3. Run paid traffic to new articles from publication, treating it as the bridge until organic arrives.
4. Track each article's position weekly and wait for it to enter the ranking range before spending on links.
5. Once a piece ranks for its keyword, start manual link building aimed at moving it to page one or higher on page one.
6. Do not build links to pages that have shown no ranking movement; spend the budget on the ones that have.
7. Report the two traffic curves separately so the paid bridge is not mistaken for organic growth.

**Tools:** Facebook Ads, LinkedIn Ads, Google Ads

**Pitfall:** Spending link budget on every new article. Links to a page that has not begun to rank waste the budget that would move a page already sitting at the bottom of page one.

**Apply at Pabau:** Pabau should hold link outreach until a new article shows movement in Search Console, then concentrate outreach on the two or three pages sitting just off page one.

**Apply anywhere:** Promote new articles with cold and lookalike paid ads while they climb, then start manual link building only on pages that have already begun to rank for their keyword.

### 14. Pay $200 for a writer test project and never run it unpaid  `167.8`
*core · best practices · source 167*

Grow and Convert are explicit that the test project must be paid, because if it is not, most good writers will pass on working with you. At the time of writing they pay $200 per test project. That figure is worth reading against their production rates: they say do not pay a writer less than $200 to produce a top blog post, and they pay $500 for every article. The test is a shortened version of a real brief, pain points plus introduction plus outline rather than a full piece, so $200 is roughly a full article rate for a fraction of the work. That premium is the price of getting strong applicants to take the test seriously. It also removes the awkwardness of asking for spec work, which is the reason many good freelancers decline hiring processes.

> "Right now, we pay $200 per test project."

**Evidence:** Grow and Convert pay $200 per test project and $500 per published article.

**How to do it**

1. Set a flat test-project fee and state it in the job posting, not after the applicant asks.
2. Benchmark the fee near your normal article rate; Grow and Convert pay $200 for a partial test against $500 for a full article.
3. Keep the test short, pain points, introduction and outline, so the fee buys a real effort without a full piece.
4. Pay on submission, not on whether the applicant is hired.
5. Never publish the test work, so nobody can claim it was unpaid production.
6. Budget the total: your fee multiplied by the number of applicants who clear the application filter.
7. Use the fee as a filter in itself, since applicants who ignore a paid, well-specified test are unlikely to hit deadlines.

**Pitfall:** Unpaid test articles. Grow and Convert say most good writers will simply decline, so an unpaid test silently selects for the weakest half of your applicant pool.

**Apply at Pabau:** David should budget a fixed paid test fee into any Pabau writer search, around a third to a half of the per-article rate, rather than asking for a free sample article.

**Apply anywhere:** Always pay for test projects. Set the fee near your article rate, keep the test partial, and pay on submission regardless of the hiring outcome.

### 15. Pay $200 for the writer test project and never run it unpaid  `164.5`
*core · concrete actions · source 164*

Grow and Convert are direct that the test project must be paid, because if it is not, most good writers will pass on working with you. Their current rate is $200 per test project, which buys a list of pain points, a full introduction and an outline for a shortened replica of a real client article. That figure sits alongside their other pay rules: never pay under $200 for a top blog post, and pay $500 per article for real work. The $200 test fee is therefore roughly the floor rate for a real post, spent on output you will never publish. They treat that as the cost of the filter rather than as wasted money, because the alternative is discovering the mismatch on a live client article that has a deadline attached.

> "The test project should be paid."

**Evidence:** Grow and Convert pay $200 per test project and pay $500 per published article.

**How to do it**

1. Budget $200 per test project and say the rate in the job posting.
2. Scope the test to pain points, introduction and outline so $200 is fair for the work.
3. Pay on submission, not on whether you hire the person, and pay even for weak submissions.
4. Only send test projects to applicants who cleared both portfolio and mini sample, to control spend.
5. Track the cost per hire: number of tests paid divided by writers who lasted, and use it to tighten the earlier filters.
6. Compare that cost against the price of one failed live article with a deadline.

**Pitfall:** Running the test unpaid to save money. The applicants who walk are the ones with other options, so an unpaid test systematically selects for the weakest half of your applicant pool.

**Apply at Pabau:** Pabau should budget roughly $200 per writer test and only spend it on applicants who cleared the portfolio and mini-sample filters, so a handful of tests covers a hiring round.

**Apply anywhere:** Pay for the writer test project, around $200 for a scoped pain-points-intro-outline task. Unpaid tests filter out the writers with options, which is the opposite of what you want.

### 16. Pay per article, not hourly, and treat $1,000 rates as no guarantee  `167.9`
*core · best practices · source 167*

Grow and Convert set out three pay rules from six years of trying different models. Do not pay by the hour, because it can incentivize the writer to string the project out so you pay more. Do not pay very high rates on the assumption that expensive writers are better: they expected that and found it untrue, having paid as much as $1,000 for a piece they could not publish. And do not pay less than $200 for a top blog post, because you will not get what you need. Their own rate is $500 per article, for a writer who is given the keyword, an expert interview, a kick-off call and ongoing coaching. They note the corollary: if you also expect content strategy, keyword research, subject-matter research and interviews from the same person, you should pay significantly more.

> "we thought writers charging high rates would be really good"

**Evidence:** Six years of pay experiments at Grow and Convert: $500 per article as standard, a $200 floor, and a $1,000 piece that never ran.

**How to do it**

1. Price per article, not per hour, so the incentive is quality of output rather than time spent.
2. Set a floor of $200 for a serious blog post and treat anything below that as unusable.
3. Set your standard rate around $500 per article where you supply keyword, interview and coaching.
4. Do not read a $1,000 quote as a quality signal; run the same test project on that writer as on everyone else.
5. Raise the rate significantly, not slightly, if the writer must also do keyword research, subject-matter research and expert interviews.
6. Agree the rate for an ongoing relationship rather than negotiating each piece.
7. Track cost per publishable article, not cost per commissioned article, since unpublishable drafts are the real expense.

**Pitfall:** Assuming price signals quality. Grow and Convert paid $1,000 for a piece they could not publish, which means the cost of a bad expensive hire is the fee plus the editor time plus the empty slot in the calendar.

**Apply at Pabau:** For Pabau, budget per article at a rate that assumes David supplies the keyword and the expert input, and re-test any premium writer rather than paying for a reputation.

**Apply anywhere:** Pay per article with a floor around $200 and a standard near $500 when you supply the keyword and expert interview. Premium rates predict nothing; test expensive writers like everyone else.

### 17. Pay writers per article, never by the hour or by word count  `164.11`
*core · best practices · source 164*

Grow and Convert set out three pay rules from six years of trying different models. Do not pay by the hour or by word count, because both incentivize the writer to string the project out or pad the prose, so you pay more for worse work. Do not chase expensive writers: they assumed high rates signalled quality and it did not hold, and they name paying $1,000 for a piece they could not publish. Do not go under $200 for a top blog post, because you will not get what you need, and pay significantly more if you also expect keyword research, subject-matter research and interviews. Their own standing rate is $500 per article, for writers who are handed the keyword and an expert interview and are not asked to do strategy.

> "it may incentivize the writer to string out the project"

**Evidence:** Grow and Convert pay $500 per article and $200 per test project, after six years of testing pay models and one $1,000 unpublishable piece.

**How to do it**

1. Move every writer agreement to a flat per-article fee and remove hourly and per-word terms.
2. Set the floor at $200 per article and treat anything below as unusable output.
3. Set the standard rate around $500 per article for a writer who receives the keyword and an interview.
4. Raise the rate materially, not marginally, if the writer must also do keyword research, research and interviews.
5. Do not equate a high quoted rate with quality; run the same paid test on expensive applicants.
6. Cap your exposure by only ever paying a premium rate after a writer has passed the test project.
7. Fix the word count in the brief so a flat fee does not become an argument about length.

**Pitfall:** Assuming price signals quality. Grow and Convert paid $1,000 for a single piece they were never able to publish, which is the failure mode of buying on rate instead of on a test project.

**Apply at Pabau:** Pabau should benchmark outside writers at roughly $500 per article with the keyword and an expert interview supplied, and never commission on an hourly or per-word basis.

**Apply anywhere:** Pay writers a flat per-article fee. Floor at about $200, standard around $500 when you supply the keyword and an interview, and more if the writer also does research and strategy. Hourly and per-word terms pay for padding.

### 18. Pick the intro pattern from the keyword type, not from which reads better  `71.4`
*core · best practices · source 71*

Devesh's tool generated two intro options and he rejected one immediately. The rejected option was a 'factors to consider' intro, which opens by saying there are many players and then frames how to choose between them. He says that pattern is right for SaaS keywords of the form 'best X software', where you genuinely want to teach a buying framework. It was wrong here because the article's actual argument is that all the other products suck. The chosen intro instead defined a content brief, described what free generators give you, and then attacked that output as a template rather than a brief. His rule is that the intro pattern follows from the position the article is taking, so you decide the argument first and then pick the opening that sets it up.

> "saying all of these other products suck"

**Evidence:** Devesh rejected the factors-to-consider intro for 'AI content brief generator' on the grounds that it suits 'best blah software' keywords, and took the definition-then-problem teardown intro instead.

**How to do it**

1. Write down in one sentence the argument the article is making, for example 'the free tools in this space produce shallow output'.
2. Generate two or three intro options rather than accepting the first.
3. Match each option to a pattern: factors-to-consider, teardown, definition-then-problem, or story.
4. Use factors-to-consider only when the keyword is a 'best X software' style comparison and you are teaching a buying framework.
5. Use the teardown pattern when your argument is that the incumbent options are bad.
6. Reject any intro whose pattern contradicts your stated argument, even if the prose is good.
7. Keep the chosen intro as a raw draft and plan to edit it heavily rather than shipping it as generated.

**Tools:** Wave Writer

**Pitfall:** Choosing the intro on prose quality alone lands you with an opening that frames a fair comparison when the body of the piece is an attack, and the reader feels the mismatch by the third heading.

**Apply at Pabau:** Pabau comparison articles and template pages should decide the argument before generating the intro. A factors-to-consider opening fits 'best practice management software' pages, while a teardown opening fits pages arguing a specific workflow is broken.

**Apply anywhere:** Decide the article's argument before you pick its opening. A factors-to-consider intro suits genuine buying-guide comparisons; a teardown intro suits pieces arguing the existing options are bad. Never pick on prose quality alone.

### 19. Pick the intro that sets up your product's features, not the cleverest one  `72.7`
*core · best practices · source 72*

Khanal faces a genuine choice between two intros he wrote himself and one the AI produced. He likes his own more, calls it clever, direct and unique on that SERP, and still rejects it. The reason: his intro ends by telling the reader to think about two things, whether the copy sounds better and what the tool automates, and he does not want the article to be about automation. The AI intro's three-category framing gives him more excuses to talk about the features he actually wants to sell. He states the test out loud: this does not set me up to talk about all of the best features the way I want to. Originality was not the tiebreak; whether the intro opens the doors the body needs was.

> "I don't think this sets me up to talk about all of the best features"

**Evidence:** Khanal discarded an intro he had written himself and preferred on craft, because it steered the article toward automation rather than the features he wanted to cover.

**How to do it**

1. Write or collect two or three candidate intros for the page rather than committing to the first.
2. For each, list the body sections it logically obliges you to write next.
3. Check whether those sections let you discuss the product strengths you want the page to sell.
4. Reject any intro that commits you to a theme you do not want to argue, even if it is the most original.
5. Confirm the chosen intro's factors map one to one to the body headings.
6. Keep the rejected intro's best single framing device and graft it into the winner if it fits.
7. Re-read the whole page to check the intro's promise is actually delivered by the body.

**Pitfall:** Choosing an intro on craft alone. A clever intro that commits you to arguing something off-strategy costs you the whole body of the page.

**Apply at Pabau:** When David reviews a generated Pabau outline, judge the intro by which body sections it forces, not by how well it reads. Reject intros that commit the article to a theme where Pabau has nothing distinctive to say.

**Apply anywhere:** Judge candidate intros by which body sections they commit you to writing, not by which reads best, and reject the ones that steer the page away from your strengths.

### 20. Pick the post type that already ranks, then differentiate on angle  `96.6`
*core · concrete actions · source 96*

Grow and Convert separate two decisions people usually blur. Post type should copy what already ranks, because that is what Google indicates searchers want. Differentiation should come from the angle, not from inventing a new format. For TapClicks they chose a 'how to create' blog post because one already ranked, and it gave them a natural structure to walk through creating a paid search dashboard in TapClicks. Then the angle came from the SERP weakness they had logged: none of the ranking pages explained what made their product different, so readers could not tell which one fit them. They made TapClicks' positioning the angle and put it in the title. They add that if you believe another type better meets intent, trying it is allowed, but it is the exception.

> "we chose to use a "how to create" blog post"

**Evidence:** TapClicks 'The Paid Search Dashboard That Scales Across Clients' sits at position 2 for 'paid search dashboard'.

**How to do it**

1. Take the page-type tally from the SERP analysis and pick the dominant type.
2. Prefer a type that also gives you a natural way to demonstrate the product.
3. Take the weakness you logged across page one and make fixing it your angle.
4. Write the angle into the title so it is visible in the SERP.
5. Repeat the angle in the introduction and again in the conclusion.
6. Deviate from the dominant post type only when you can state why it serves intent better.

**Pitfall:** Choosing a format nobody on page one uses because it feels more original. Grow and Convert treat that as the risky path; originality belongs in the angle, not the container.

**Apply at Pabau:** For Pabau, keep the format matching the SERP, listicle where listicles rank, template page where templates rank, and put the originality into the angle drawn from what competitors leave out.

**Apply anywhere:** Copy the post type that already ranks and put your originality into the angle, drawn from the weakness you found across page one.

### 21. Prepare a clinical interview from the SERP and the patient mindset  `117.1`
*core · concrete actions · source 117*

Grow and Convert's content strategist Olivia Seitz prepared her Cognitive FX interview in two passes before speaking to anyone. First she read the pages already ranking for 'post-concussion headaches' to list the subtopics the article had to cover to rank, and pulled the People Also Ask questions for the patient questions Google already surfaces. Second she did a thought exercise, sitting in the mindset of somebody with the condition and writing the questions they would have: what is causing this, how might I experience it, do my symptoms match, how is it treated, what are the options, how long is recovery. Those two lists became the interview guide. The point is that the SERP supplies ranking coverage and the mindset exercise supplies the human questions the SERP leaves out.

> "putting herself in the mindset of a person that has"

**Evidence:** The Cognitive FX article held position #1 for the target keyword for several years and ranks for 8.4K organic keywords, 165 of them in the top 3, per Ahrefs.

**How to do it**

1. Pick the exact target keyword before any interview prep, one keyword per article.
2. Read the top-ranking pages for that keyword and list every subtopic they cover.
3. Copy the People Also Ask questions for the keyword into the same list.
4. Separately write the questions a person with this problem would have: cause, variation, symptom match, treatment options, recovery time.
5. Merge both lists into a single interview guide ordered by what the reader wants first.
6. Take the guide into the interview with the in-house expert and use it to steer, not to script.
7. After the interview, map each answer back to a heading in the outline so nothing is lost.

**Tools:** Google, Ahrefs

**Pitfall:** Preparing only from the SERP produces a rewrite of the pages already ranking; preparing only from empathy produces an article missing the coverage it needs to rank at all.

**Apply at Pabau:** Before David briefs any clinical article, build the two-column prep sheet: SERP subtopics plus PAA on one side, the practice owner's or patient's live questions on the other. Use it as the interview guide with a Pabau clinician customer.

**Apply anywhere:** Prepare every expert interview twice over. Read the ranking pages and the People Also Ask box for the coverage you need, then write the questions your reader would actually ask, and interview against the merged list.

### 22. Promote launch posts into your audience's communities, not your feeds  `123.6`
*core · concrete actions · source 123*

Hyam's diagnosis of why most blog launches fail is that people publish a few posts, share them on Facebook, Twitter or LinkedIn, then wonder why only a couple dozen friends read the first article. For the Grow and Convert launch the promotion step was different: they promoted every post in the six-month challenge into the communities where they knew marketers, their target market, already gathered. That is a placement decision rather than a broadcast decision. Your own social channels at launch contain your friends and former colleagues, which is why the numbers stay in the dozens. A community contains strangers who match the buyer profile, so the same post reaches a qualified audience without any following of your own.

> "we promoted all of the posts that outlined our 6 month challenge"

**Evidence:** Community promotion of the challenge posts produced 1,878 unique visitors and 196 email subscribers in the first two weeks on a brand new domain.

**How to do it**

1. List the specific places your buyer already gathers: subreddits, Slack and Discord groups, Facebook groups, forums, niche newsletters.
2. Join them before launch and participate long enough that a post from you is not a first appearance.
3. Read each community's self-promotion rules and note which allow a link and which require a native writeup.
4. Post the launch piece with a short native framing of why it exists, not a bare link.
5. Repeat the placement for every follow-up post in the launch series, not just the first one.
6. Answer every comment in the thread, since the discussion is what holds the placement on the front page.
7. Track visits and email signups by community so you know which two or three deserve ongoing effort.

**Pitfall:** Treating your own social feeds as a distribution channel at launch. Hyam says this is exactly why launches produce a couple dozen visitors from friends, and you spot it when Analytics shows social traffic with no email conversion.

**Apply at Pabau:** Pabau's launch and refresh promotion should go to aesthetics practitioner communities, clinic-owner Facebook groups and relevant subreddits, with a named owner and a per-community log, instead of only the Pabau company pages.

**Apply anywhere:** Promote launch content into the specific communities your buyers already use rather than your own social feeds, join those communities before you need them, post a native writeup rather than a bare link, and log signups per community so you know which two or three to keep working.

### 23. Prompt: generate image alt text from file names plus the full article  `50.10`
*core · ai workflows · source 50*

The host's own manual technique for writing alt text is to paste the full article into ChatGPT along with the images' exact file names, and ask it to write alt text for each image using both the file names and the article as context, which he reports "does a very good job." The guest confirms doing an equivalent, more automated version for Shopify e-commerce clients: using apps that run a template across every product image, automatically renaming files and writing descriptive tags, with everything stored in a shared media library per brand so images can later be matched to relevant articles or sales pages. Neither version requires manually looking at each image individually — the file name plus surrounding written context is enough for the model to produce accurate, descriptive alt text at scale.

> "write the alt text for these images using the file names"

**How to do it**

1. Assemble the target article's full text and the exact file names of every image that needs alt text.
2. Open ChatGPT or an equivalent LLM and paste in the article text.
3. State the image file names and ask for alt text for each one, using the prompt structure given in the source.
4. Review the generated alt text for accuracy against what the image actually shows, since the model is inferring content from file name and context rather than truly seeing the image (inferred quality check, since the technique relies on text context, not vision).
5. For e-commerce catalogs at scale, set up a templated app or workflow, such as a Shopify app, that runs the same file-renaming and tagging logic across every product image automatically rather than one image at a time.
6. Store all tagged images in a shared, brand-specific media library so they can be quickly matched to relevant future articles or sales pages.

**Tools:** ChatGPT, Shopify apps for bulk image tagging

**Prompt / template:**

```text
I have specific file names for images, write the alt text for these images using the file names and the article as context.
```

### 24. Prove positioning claims with long-form case studies, then how-tos and opinion  `159.11`
*core · concrete actions · source 159*

Grow and Convert close the article with the content job: content is one of the best ways to prove you can deliver on your unique positioning angles and value propositions. They rank three frameworks. Long-form case studies are the number one framework, and they explicitly reject the cheesy marketing-site format of problem, solution, result in favor of long-form stories. Second are how-tos, with the warning that most how-to posts are far too beginner and lack customer-content fit, so fixing that is itself proof you know the subject. Third are opinion pieces, which take a stand instead of teaching, and which they say most crappy blogs cannot produce. Benji's 'Why Marketing is the Hardest Position to Hire For' is their named example. They teach six frameworks in their course and single out these three for proof of delivery.

> "Content is one of the best ways to prove you can deliver"

**Evidence:** Grow and Convert name long-form case studies as the number one framework for proving a value proposition, ahead of how-tos and opinion pieces.

**How to do it**

1. Write out the positioning claim the content has to prove, in one sentence.
2. Commission one long-form case study that tells the whole story of delivering that claim for a named customer, not a problem-solution-result summary.
3. Include the messy parts: what was tried, what failed, the actual numbers and the timeline.
4. Add how-tos that assume the reader already knows the basics, aimed at the specific customer in your positioning rather than at beginners.
5. Check each how-to against the top-ranking posts and cut any section that repeats the beginner material they already cover.
6. Publish at least one opinion piece a quarter that takes a clear stand on a contested question in your field.
7. Map each published piece back to the positioning claim it proves, and commission for any claim with no supporting content.

**Pitfall:** Case studies written as short marketing-site testimonials. They prove nothing because every competitor has the same page, and they carry no detail a buyer could check.

**Apply at Pabau:** Pabau should publish long-form practice case studies with real numbers and timelines, and pitch its how-to articles above beginner level, since the beginner tier is what AI answers absorb first.

**Apply anywhere:** Publish long-form case studies with real numbers and timelines as the primary proof of your positioning claim, then how-tos pitched above beginner level, then opinion pieces that take a stand.

### 25. Prune the generated outline before drafting, section by section  `71.11`
*core · concrete actions · source 71*

Devesh treats the generated outline as a menu, not a plan. His tool deliberately over-produces sections on the principle that you can keep all of them if you want, because AI tends to write too much. Before clicking through to a draft he walked every proposed section and made a keep or cut call. He kept the longer teardown of why the existing tools are bad and the 'what to look for' setup. He cut 'how to get more out of any AI content brief generator' because the teardown had already covered it, cut 'never skip the SERP step' and 'treat the keyword as the first' as repetitive with material above, and cut the FAQ. He also debated a brief mention of competing tools and kept it, reasoning Google might value the only page that lists multiple generators.

> "AI does AI tends to like write too much"

**Evidence:** Devesh cut four proposed sections from the outline for 'AI content brief generator' before generating the draft, including an FAQ and a 'how to get more out of any AI content brief generator' section.

**How to do it**

1. Generate more outline sections than you intend to publish, so the cut decisions happen before drafting.
2. Walk the outline top to bottom and mark each section keep, cut or merge.
3. Cut any section whose argument the intro or an earlier section already makes.
4. Cut generic filler sections such as 'how to get more out of X' when the piece has already told the reader how.
5. Keep sections that add a new angle even if the SERP does not contain them, and note why.
6. Choose between competing intro options at this stage rather than after drafting.
7. Only then generate the draft, so the model writes to the pruned outline rather than the full menu.

**Tools:** Wave Writer

**Pitfall:** Generating the full draft first and cutting afterwards wastes the model's effort and makes you reluctant to delete prose you have already read and liked. Cut at outline stage where the sunk cost is zero.

**Apply at Pabau:** Pabau's /generate human outline approval step should be a keep-or-cut pass on an intentionally over-generated outline, so the writer never drafts sections that duplicate the Key takeaways or the intro.

**Apply anywhere:** Have the model over-produce the outline, then make a keep-or-cut call on every section before drafting. Cutting at outline stage costs nothing; cutting finished prose is much harder.
