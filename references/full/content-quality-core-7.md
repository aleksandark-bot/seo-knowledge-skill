# Content Quality — core (part 7 of 9)

23 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Retarget old non-ranking posts before writing anything new  `139.3`
*core · concrete actions · source 139*

Brandon's first move on Keeper Tax was not new content. He audited existing posts that were not ranking for anything useful and repointed them at better keywords. His reasoning: old posts skip the discovery, crawl and initial ranking wait, and they usually already carry some backlinks. His worked example was a post on receipts and taxes that ranked only for 'paper receipts' and 'are paper receipts required by irs', terms with no commercial value to a tax write-off app. He researched a nearby keyword with more volume, aligned intent and relatively low difficulty, and settled on 'receipts for taxes' because a person searching it is at least thinking about saving receipts, which is one step from the product. He then updated the URL, headers, title tag and body copy to the new target.

> "you don't need to wait for Google to discover, crawl, and rank them"

**Evidence:** Keeper Tax: a receipts post moved off 'paper receipts' onto 'receipts for taxes' as part of a program that took the site from ~10,000 monthly visitors to 400% growth in 3.5 months.

**How to do it**

1. Export every existing blog URL and pull its current ranking queries from Ahrefs or Search Console.
2. Flag every post whose ranking queries have no commercial connection to the product.
3. For each flagged post, identify the pain point it genuinely covers, in the customer's words.
4. Find a nearby keyword with higher volume, matching intent and relatively low keyword difficulty.
5. Confirm the searcher of that keyword is one step from needing your product before committing.
6. Rewrite the URL, H1, title tag, headers and body copy around the new target keyword.
7. Add the missing subtopics the new query demands rather than only swapping the phrase.
8. Recheck rankings after two to four weeks and only then move to the next post.

**Tools:** Ahrefs, Clearscope, Wayback Machine

**Pitfall:** Changing only the title and headers while leaving 800 words written for the old query gets you a mismatch Google ignores. The body has to answer the new question.

**Apply at Pabau:** Pabau should run this pass over older /blog/ posts that rank only for irrelevant fragments, repointing each at the nearest keyword an aesthetic practice owner would search when evaluating software.

**Apply anywhere:** Audit old posts that rank for nothing useful, repoint each at a nearby keyword with real commercial intent, and rewrite the body to answer that query before publishing anything new.

### 2. Rewrite a meandering passage as bullets to find the real value proposition  `124.6`
*core · concrete actions · source 124*

Grow and Convert use bullet conversion as a diagnostic, not a formatting preference. Their example is a rambling intro about schools for sensory processing disorder that jumps between environment, sensory breaks, class size and scheduling. Rewritten as four labeled bullets, two things happened. Each bullet gained detail, because a bullet with a bolded label demands a supporting explanation. More importantly, they could see that the first bullet, catering the school environment to the child, was the actual value proposition and the other bullets were supporting evidence for it. The final intro was then rebuilt around that single claim with five bullets beneath it. Their stated conclusion is that organizing into bullets is what let them identify the core argument, which the prose version had hidden.

> "allowed us to clearly identify the core argument"

**Evidence:** Grow and Convert's education client piece on schools for sensory processing disorder went through several edits from a rambling five-sentence intro to a lead claim plus five detailed bullets.

**How to do it**

1. Take the meandering passage and split every distinct claim onto its own numbered line.
2. Give each line a bolded label of three to six words naming the claim.
3. Write two or three sentences under each label explaining the mechanism and why it matters to the reader.
4. Read the labels only and decide which one is the value proposition and which are supporting evidence.
5. Promote the value proposition into the lead sentence above the list.
6. Rewrite the remaining bullets as support for that lead claim, dropping any that do not support it.
7. Add any bullet the exercise revealed as missing, such as a scheduling or timing angle.
8. Keep the bullet form if it reads better, or convert back to prose now that the argument is settled.

**Pitfall:** Treating bulleting as a readability tweak and keeping the same vague claims in list form. The signal you did it wrong is that no bullet stands out as the main point and all of them read as equally important.

**Apply at Pabau:** When a Pabau draft section wanders, David should have the writer bullet it with bolded labels rather than reword it. On aesthetic-practice comparison pieces this usually reveals which single benefit is the argument and which are supporting details.

**Apply anywhere:** When a passage wanders, rewrite it as labeled bullets with two or three sentences of support each, then identify which bullet is the actual value proposition. Promote that one to the lead sentence and make the rest support it.

### 3. Rewrite ad copy from the primary benefit customers name themselves  `161.4`
*core · concrete actions · source 161*

Question four asks what primary benefit the customer received. Khanal's point is that the benefit you built the product for and the benefit people actually get are often different things. The instruction is to look for commonalities across respondents rather than pick the most articulate single answer, then test the recurring benefit in messaging and ad copy. This is a testing loop, not a rewrite: you take the phrasing that repeats, put it in a headline or an ad, and measure whether it beats the current line. He frames it as the second most important question in the survey, behind only asking how you could improve.

> "You should look for commonalities amongst respondents' answers"

**Evidence:** Khanal reports that at ThinkApps this class of question surfaced trust, visibility and communication as the real benefits, which then drove business model, content, ad copy, landing pages and sales approach.

**How to do it**

1. Ask 'What is the primary benefit that you have received from X?' as a free-text question.
2. Paste all answers into one column and tag each with the benefit it names.
3. Count the tags and keep any benefit named by three or more people.
4. Check whether your current homepage headline names the top benefit; usually it does not.
5. Write two or three headline variants using the customers' own words, not your internal category language.
6. Run those variants as ad copy first, where you get a read in days rather than months.
7. Roll the winning phrasing into the homepage, the landing pages and the sales deck.
8. Re-ask the question six months later, since the dominant benefit shifts as the product changes.

**Tools:** Survey Monkey

**Prompt / template:**

```text
What is the primary benefit that you have received from (Product or Company Name)?
```

**Pitfall:** Picking the most eloquent single response instead of the repeated one. One customer's polished quote is a testimonial; three customers using the same plain phrase is a positioning finding.

**Apply at Pabau:** Pabau should ask practices what they actually got from the software, and if the repeated answer is something like fewer no-shows rather than the feature set, that phrase belongs in the hero of the book-demo page.

**Apply anywhere:** Ask customers what benefit they actually got, keep only the phrasing that repeats across several people, and test it as ad copy before rewriting the site.

### 4. Run first-hand product tests with a disclosed method  `66.13`
*core · concrete actions · source 66*

Content that tests one product or service under specified conditions and reports what was observed or measured. Its role is to answer 'How did this specific option perform?' with a transparent method, evidence, expert judgement and limitations — not to infer market trends or prove a customer's before-and-after outcome, which the framework assigns to original research and case studies respectively. It covers hands-on tests, benchmarks, teardowns, trials, demonstrations and measured reviews, documenting the method, sample, conditions, results, pros, cons and limitations. It scores High on click resilience, citation potential, business value and proprietary advantage, at High effort — the type where cost and return are both at their maximum. The scored boundary matters: one product, specified conditions, reported observations. A 'review' assembled from other people's reviews scores as a rehashed explainer instead, on every dimension.

> "tests one product or service under specified conditions and reports what was observed or measured"

**How to do it**

1. Choose one product or service and one question about it that a buyer actually asks — not a general impression.
2. Define the test conditions before testing: the sample, the environment, the settings, the duration, and what counts as a pass.
3. Run the test and record raw observations and measurements as you go, including the runs that went wrong.
4. Capture evidence a reader can inspect: photographs, screenshots, exported data, timings, or the test file itself.
5. Report the method, sample, conditions and results explicitly, in that order, so another practitioner could repeat it.
6. Add expert judgement as a separate, labelled layer — what the numbers mean for a specific use case — so the measurements stay separable from the opinion.
7. State the limitations plainly: what the test did not cover, what the sample cannot support, and where the result might not hold.
8. List pros and cons against the named use case rather than in the abstract.
9. Publish the underlying data where you can, since that is what converts a test into a citable primary source.
10. Re-test when the product changes materially, and date the result so an AI system citing it knows which version it describes.

**Pitfall:** Drifting from testing one option into ranking the market. The moment the page starts inferring which product is best overall, it stops being a first-hand test and becomes the framework's deprioritized 'biased best-of' type — losing the citation potential that the measurement earned.

**Apply at Pabau:** High effort, so pick the tests that only Pabau can run: measuring what happens inside real practices using the product. Keep them as single-product tests with a disclosed method — the moment a test turns into 'Pabau vs competitor, and Pabau wins', it lands in the deprioritized biased-comparison bucket.

**Apply anywhere:** High effort, so pick the tests only you can run: measuring what happens when real customers use the product. Keep them as single-product tests with a disclosed method — the moment a test turns into 'us vs competitor, and we win', it lands in the deprioritized biased-comparison bucket.

### 5. Run the Jony Ive test on your opening sentence  `127.2`
*core · best practices · source 127*

Grow and Convert give a one-line test for whether an opening states the obvious. Imagine walking up to Jony Ive and saying 'Design is an important part of building products consumers love.' He designed the iPod, iPhone and iPad. You do not need to tell him that, and saying it makes you look like a fool. The article maps this straight onto B2B blog intros: telling a 20-year sales manager that most growing businesses will need a CRM at some point does the same damage. The mechanism they name is trust, not style. A high-school-paper opener gives away that the author does not know the reader, which implies they do not care about the reader, which is a reason not to trust them, not to keep reading, and not to opt in, request a demo or contact sales. The test is cheap because it takes one substitution.

> "You don't need to tell him that!"

**Evidence:** Grow and Convert's paired example: an intro telling a 41-year-old sales manager that 'Most growing businesses will need a CRM system at some point in their lives.'

**How to do it**

1. Name the single most experienced person in your target audience, ideally a real named expert in that field.
2. Read your first two sentences aloud as if you were saying them to that person's face.
3. Flag any sentence that would make them think you assume they are a beginner.
4. Flag any sentence that defines the product category or argues that the category matters.
5. Flag any statistic used only to prove the problem exists rather than to say something specific about it.
6. Replace each flagged sentence with the most specific claim in your article.
7. Re-run the test after the rewrite, because the second draft often reintroduces one hedge sentence.
8. Apply the test to email subject lines and landing-page headers too, not only blog intros.

**Pitfall:** Writers defend obvious openers as warm-up or as a courtesy to less experienced readers. The cost lands on the buyer, who is usually the most experienced reader on the page and the one who decides whether to request a demo.

**Apply at Pabau:** For Pabau, the named expert is a practice owner or clinic manager who has run a business for a decade. No blog intro should explain what patient management is, why retention matters, or why no-shows cost money. Open on the specific version of the problem instead.

**Apply anywhere:** Pick the most experienced person in your target audience and read your opening two sentences as if you were saying them to their face. Delete anything that defines the category or argues it matters. The most experienced reader is usually the buyer.

### 6. Run the three-step update pass: score, SERP intent, then details  `119.5`
*core · concrete actions · source 119*

Grow and Convert give an ordered procedure for actually updating a page once monitoring has flagged it. First, check the content's SEO score in Clearscope and adjust keyword coverage until it reaches an A. Second, and they call this the most critical step and explicitly separate from the score, search the target keyword yourself and compare your page against what Google is ranking, on format and on topics. Third, polish details: stats, examples and quotes up to date, no broken links, SEO title and meta description refreshed including the year if the title carries one. The order matters because the score step is mechanical while the intent step can tell you the whole piece needs restructuring, which makes detail polishing premature until it is done.

> "The first thing we do is check the content's SEO score"

**Evidence:** Grow and Convert's stated three-step process for updating client SEO content, with the SERP intent step named as arguably the most critical.

**How to do it**

1. Open the flagged page in Clearscope and read its current grade and missing terms.
2. Work the keywords into the copy until the page reaches an A grade, without stuffing.
3. Search the target keyword in a clean browser session and open the top ten results.
4. Record the dominant format across those results: blog post, landing page, list, narrative.
5. List the topics and subtopics most of the top-ranking pieces cover, and mark which your page lacks.
6. Decide whether the page needs a topic addition or a full restructure into the dominant format.
7. Rewrite to that decision before touching any surface details.
8. Refresh every stat, example and quote, and replace anything more than a year or two old.
9. Run a link checker over the page and fix or remove every broken link.
10. Rewrite the SEO title and meta description for accuracy, updating the year if the title includes one.

**Tools:** Clearscope

**Pitfall:** Stopping at the Clearscope A. Grow and Convert stress the score is separate from intent, so a page can grade well and still be the wrong format for the current SERP.

**Apply at Pabau:** Pabau's refresh work should not be an editorial polish pass. David should require a SERP format check on every flagged article before any copy is edited, because a Pabau feature page competing against listicles needs restructuring, not tightening.

**Apply anywhere:** Update in order: fix on-page coverage, then check your format and topics against the live top ten, then polish stats, links and the title tag. Never polish before the intent check.

### 7. Run your own survey to make a top-funnel post convert  `111.7`
*core · concrete actions · source 111*

Grow and Convert show how they made a genuinely top-funnel query pay for Circuit, a delivery route planning tool. The keyword was 'what makes a great delivery experience', which carries no purchase intent. Instead of writing opinion, they surveyed 275 people who regularly receive packages and asked what makes a great delivery experience. They reported the results, with 40.8% of respondents choosing 'deliveries being on time' as the most important factor, and bridged that finding into an explanation of how Circuit's product enables on-time delivery. The survey does two jobs at once. It is the originality that earns the ranking and the links on a crowded top-funnel term, and it produces a statistic that leads directly to the product's core benefit. The bridge only works if the question is designed so the winning answer is something your product delivers.

> "we surveyed 275 people who regularly receive packages"

**Evidence:** Circuit's 'what makes a great delivery experience' post: 275 respondents surveyed, 40.8% chose deliveries being on time, bridged into Circuit's route optimization.

**How to do it**

1. Pick a top-funnel keyword where an opinion post would have nothing original to say.
2. Write the survey question so the plausible top answer is the outcome your product produces.
3. Recruit at least 250 respondents from the group the article is about, not from your customer list.
4. Run it through a panel service or a paid social audience so the sample is not your own audience.
5. Report the headline percentage with the sample size and the recruitment method in the article.
6. Publish the full result table, since that is what other sites cite and link to.
7. Bridge from the winning answer into one section on how your product delivers that outcome.
8. Pitch the statistic to trade publications to convert the survey into links as well as rankings.

**Pitfall:** Surveying your own customers or too small a sample. The result reads as marketing, nobody cites it, and the page has no advantage over the opinion posts it was meant to beat.

**Apply at Pabau:** Pabau can run the same play on top-funnel aesthetic queries, surveying patients on what makes a clinic visit good and bridging the winning answer into booking, reminders or consultation notes. One survey a quarter would give /blog/ its originality nuggets and its link assets at once.

**Apply anywhere:** When a top-funnel keyword has no original angle available, run your own survey of 250-plus people in the audience the article is about, design the question so the likely top answer is the outcome your product produces, and bridge from the result to the product.

### 8. Same content ranked better on a commercial site than an affiliate site  `03.11`
*core · content insights · source 03*

Across a two-and-a-half-year case study, a semantic content network with exactly the same content and context failed to rank while hosted on an affiliate website, then began ranking better once moved to a commercial website. This is attributed to Google's post-Helpful-Content-System updates favoring functional websites that provide concrete, unique services and benefits over pure content or affiliate sites, generalized into a standing principle: informational outer-section pages should be written to be as commercially related as possible — even checklist or ideas content should be merged with direct product tie-ins and conversion elements near the top of the page — because ranking signals generated on outer/informational pages transfer through internal links to the commercial core of the topical map.

> "began ranking better when we moved it to a commercial website"

**Evidence:** A 2.5-year case study where identical content/context ranked poorly on an affiliate site but ranked better after being moved to a commercial website; further illustrated by an ecommerce example where informational festival-checklist and festival-outfit-ideas pages are deliberately kept commercial by merging that content with direct product placements rather than leaving it purely informational.

**Apply at Pabau:** Pabau should keep even its most informational blog content (guides, checklists, how-to-choose articles) structurally tied to the product, with concrete calls to action or feature tie-ins near the top of the page, rather than writing pure informational content in isolation from the commercial product, since the same words can rank measurably worse divorced from a functional commercial site than integrated with one.

**Apply anywhere:** You should keep even its most informational blog content (guides, checklists, how-to-choose articles) structurally tied to the product, with concrete calls to action or feature tie-ins near the top of the page, rather than writing pure informational content in isolation from the commercial product, since the same words can rank measurably worse divorced from a functional commercial site than integrated with one.

### 9. Say the AI tells are not the real problem, then strip them anyway  `72.15`
*core · concrete actions · source 72*

Khanal makes an argument he wants in the article itself: the difference between good copy and AI slop is not em dashes or the 'not X, it's Y' construction. It is whether the copy talks about the right subjects in the right order, which features to lead with, which benefits to pair with them, how to frame yourself against alternatives. He still removes the surface tells. He deliberately avoids an em dash where he would normally use one, because it makes copy read as AI. He catches his own tool writing 'comprehensive' and cuts it, noting the stuff still creeps in. And he flags AI's habit of adding an extra clause after the point is made, comparing it to the guy who does not stop texting. Both passes are needed: surface tells and substance.

> "Not just removing m dashes"

**Evidence:** Khanal cut 'comprehensive' from his own tool's output on air, noting it still creeps in despite the tool being built to avoid AI phrasing.

**How to do it**

1. Do the substance pass first: check the copy names the right features, in the right order, against the right alternatives.
2. Then run the surface pass for tells: em dashes, 'not X, it's Y', 'comprehensive', 'seamless', and similar filler adjectives.
3. Delete trailing qualifier clauses that extend a heading or sentence after the point is made, such as 'beyond templates and pricing'.
4. Check for the repeat-the-ask pattern where a sentence restates its own request in different words.
5. Re-read for confident but unsupported judgments, which are the substance-level version of the same problem.
6. Re-run the surface pass after your own edits, since the phrasing creeps back in during rewriting.

**Pitfall:** Treating em-dash removal as the edit. Khanal says a piece with every tell stripped still reads as AI if it makes no concrete argument, and the reader's nagging sense comes from the missing substance.

**Apply at Pabau:** Pabau's AI-tell list should sit second in the editorial pass, after a check that the article makes concrete, Pabau-specific arguments. Stripping tells from an article with no substance leaves an article with no substance.

**Apply anywhere:** Run the substance check first, confirming the copy makes concrete arguments, then strip surface AI tells such as em dashes and filler adjectives, and re-run that strip after your own rewrites.

### 10. Scaled, unedited AI content creates a boom-then-crash traffic "mountain"  `19.7`
*core · content insights · source 19*

Referencing a point made by Mike King in a separate episode, Kaleigh and the host describe a repeating pattern they call the "mountain." A site scales up AI-generated content, company-blog-attributed, no named author, telltale em dashes, self-promotional listicles, and traffic climbs and appears to work well for a while. Then, not very long after, the organic traffic graph takes the shape of a mountain: it rises sharply and falls right back down. The stated cause isn't an algorithm penalty targeting AI content specifically, but bad user engagement signals — because the content itself isn't made well and doesn't match what searchers actually want, the site is effectively mass-producing negative user signals at scale, described as one of the more damaging things a site can do to itself.

> "organic traffic graph looks like a mountain and comes right back down"

**Evidence:** Mike King's observation, relayed secondhand by Kaleigh from his appearance on the same podcast, that scaled AI content programs commonly show this rise-then-crash "mountain" shaped traffic graph, attributed to bad user signals rather than a direct AI-content penalty.

**Apply at Pabau:** Before scaling up AI-assisted content production for Pabau's blog, treat genuine content quality and real user engagement, not just publishing volume, as the actual gating factor; mass-producing unedited, self-promotional, no-byline AI content risks a visible boom-and-crash traffic pattern driven by bad engagement signals, not a one-time penalty that could otherwise be planned around.

**Apply anywhere:** Before scaling up AI-assisted content production for your blog, treat genuine content quality and real user engagement, not just publishing volume, as the actual gating factor; mass-producing unedited, self-promotional, no-byline AI content risks a visible boom-and-crash traffic pattern driven by bad engagement signals, not a one-time penalty that could otherwise be planned around.

### 11. Score every draft against two criteria: positioning and original instruction  `126.13`
*core · content insights · source 126*

Grow and Convert give a two-item definition of a good piece and then use it as the yardstick for every method they criticize. A good piece positions the product in the industry the way the founder or executive would, and it has original or instructive ideas that teach the customer something or answer their question. They then ask how a freelance writer is supposed to hit both unaided at the level of a founder, executive or long-standing employee, since the writer cannot know the nuances of how the product is positioned against competitors and has no original solutions to the customer's product-related pain points. They apply the same two criteria to the Google research paper method and conclude it has little chance of success measured that way. The value of the pair is that it makes review objective: a draft can be well written and fail both.

> "Positions the product in the industry the way the founder"

**Evidence:** Grow and Convert apply the two criteria to page-one competitors for 'enterprise reporting tool' and show all of them failing.

**How to do it**

1. Add two yes-or-no fields to your draft review: does it position the product as an executive would, and does it teach something original.
2. Have the internal expert, not the editor, answer the positioning question.
3. Require the writer to point to the specific passage that satisfies each criterion.
4. Reject drafts that pass on prose quality but fail both criteria, rather than editing them.
5. Record which criterion fails most often and fix that input in the brief.
6. Keep one passing draft per criterion as the internal benchmark.

**Pitfall:** Reviewing on readability. Grow and Convert note the Google research paper may be well written, fun to read, with neat images and all the right SEO stuff, and still fail both criteria.

**Apply at Pabau:** Pabau's editorial pass should carry these two checks explicitly alongside the sentence gate: does the piece position Pabau the way a Pabau executive would, and does it teach an aesthetic practice owner something they could not get from the other page-one results.

**Apply anywhere:** Score drafts on two questions: does it position the product the way your founder would, and does it teach the customer something original. Well-written drafts routinely fail both, so ask the questions separately from the prose review.

### 12. Segment implementation and troubleshooting guides by the variable that changes the answer  `66.17`
*core · concrete actions · source 66*

Content that helps an existing user configure, implement or fix a specific product when the correct steps depend on the version, device, environment, error, location or constraint. Its role is 'Help me make it work here' — not proving a past outcome or choosing between products. It covers troubleshooting trees, configuration guides, advanced implementation instructions and support content segmented by version, device, symptom, customer stage or operating environment. It scores High on click resilience, business value and proprietary advantage at Medium effort, with Medium citation and brand mention potential. The segmentation is what makes the type defensible rather than a keyword-variant farm: a separate page per version or environment is justified precisely when the correct answer differs, and unjustified when only the wording differs — which is the boundary against the framework's deprioritized fragmented-FAQ type. Click resilience is High because an AI answer trained on the general case cannot know the user's version, device or error state.

> "helps an existing user configure, implement or fix a specific product"

**How to do it**

1. Pull the actual failure and configuration questions from support tickets, chat logs and community posts rather than from keyword tools.
2. For each, identify the variable that changes the correct answer: version, device, operating environment, error code, location, or plan.
3. Create one page per genuinely different answer, and a single page covering all cases where the answer is the same. Let the answer decide the URL structure, not the phrasing.
4. Open each page by stating the exact conditions it applies to, so a user or an AI system can confirm they are in the right place before following it.
5. Write the steps against a real environment you have reproduced, including the exact interface labels and the expected result of each step.
6. For troubleshooting, structure as a decision tree: the symptom, the checks in order, and where each branch leads.
7. Include the error text verbatim, since that is what users and AI systems search on.
8. Say what to do when the guide does not resolve it, with a route to support that carries the diagnostic information already gathered.
9. Version the pages against product releases and retire guides for versions no longer supported, redirecting to the current equivalent.
10. Feed resolution data back: any guide that support still has to explain by hand is not finished.

**Tools:** Google Search Console

**Pitfall:** Splitting by wording rather than by answer. If two pages give the same steps for the same conditions, they are the deprioritized fragmented-FAQ type wearing a troubleshooting label, and they compete with each other for the same intent.

**Apply at Pabau:** Pabau's support content earns its place when it is segmented by what actually changes the answer — the module, the device, whether it is Pabau GO on iOS or the web app, the market's regulatory requirements. Same steps for two different phrasings means one page, not two.

**Apply anywhere:** Support content earns its place when it is segmented by what actually changes the answer — the module, the device, the platform version, the market's regulatory requirements. Same steps for two different phrasings means one page, not two.

### 13. Sell in content by demonstration, not by repeating landing-page copy  `108.8`
*core · best practices · source 108*

Grow and Convert push back on the content marketing convention that blogs should not be salesy, but they qualify how the selling happens. On bottom-funnel keywords the searcher literally wants to know what the product does, how it solves their problem and how it differs from alternatives, so discussing the product is part of meeting search intent. The distinction they draw is that selling through content looks different from selling on a landing page. In content you sell by demonstration and education: showing how the product solves specific problems, walking through features inside real use cases, and explaining why the approach differs from the alternatives. Done that way it does not read as salesy, because it is the information the reader came for. Their example is 'help desk software for small business', where you name what makes the product suited to small businesses, whether that is pricing structure, setup ease, integrations or ticket handling, instead of listing features every product has.

> "you're selling through demonstration and education"

**Evidence:** Grow and Convert's 'help desk software for small business' example: name pricing structure, ease of setup, specific integrations or ticket-management approach rather than generic help desk features.

**How to do it**

1. Confirm the keyword is bottom-funnel before adding product depth; the tactic does not transfer to informational terms.
2. Write the product section as a walkthrough of one real use case, not a feature list.
3. Name the specific attribute that fits the searcher's qualifier: pricing model, setup time, a named integration, a workflow.
4. Cut any feature claim that every competitor could also make.
5. Show the manual or rival approach first, then where it breaks, then what the product does instead.
6. Use screenshots or steps rather than adjectives.
7. Close with the differentiator stated plainly rather than a generic call to action.
8. Have someone who talks to customers read the section and flag anything a competitor could copy verbatim.

**Pitfall:** Pasting landing-page positioning into an article. It reads as an ad in the middle of a guide, and it fails the qualifier the searcher typed, so the page converts no better than a generic post.

**Apply at Pabau:** Pabau's bottom-funnel articles should demonstrate one workflow end to end, such as running a consultation from booking through consent form to before-and-after photos, rather than restating feature-page copy.

**Apply anywhere:** On bottom-funnel keywords, sell by demonstration. Walk the product through one real use case, name the specific attribute that matches the searcher's qualifier, and cut any claim a competitor could make word for word.

### 14. Sell the product hard inside JTBD posts, despite the usual advice  `93.12`
*core · best practices · source 93*

Goolding contradicts the standard content-marketing rule that blog posts should not talk about the product much. He says Grow and Convert do sell their clients' products in JTBD blog posts, often heavily, and that this is the point: JTBD keywords were selected because they still carry buying intent. He draws a clean line between the two decisions. When choosing the keyword you look for terms indicating the user has a goal your product helps achieve, without requiring the term to mention your product. When writing the article you definitely need to sell how your product helps achieve that goal, in detail. Treating the keyword's product-free phrasing as a licence to write a product-free article is the mistake, because the article then ranks and converts nobody.

> "we do sell our clients' products in JTBD blog posts, often heavily"

**How to do it**

1. Separate the two decisions in the brief: keyword selection is product-free, article writing is not.
2. Require every JTBD brief to name which product feature does the job being searched.
3. Write a dedicated section explaining, in detail, how the product completes the job, not a one-line mention.
4. Include the concrete mechanism, such as an integration or an automation, rather than a benefit statement.
5. Place the product section after the reader can already do the job manually.
6. State plainly that it is your product, without pretending to be neutral.
7. Add a CTA tied to the specific job the post covers.
8. Review published JTBD posts and add the product section where writers left it out.

**Pitfall:** Writers apply the generic 'do not be salesy' rule to a keyword that was chosen for its buying intent, and the post reads as a neutral guide that sends the reader back to Google to find a tool.

**Apply at Pabau:** Pabau's how-to articles must include a substantive Pabau section, which the content guides already require ahead of the Conclusion. Treat it as a detailed explanation of how the feature does the job, not a two-sentence mention.

**Apply anywhere:** Sell your product in detail inside jobs-to-be-done posts, because the keyword was chosen for buying intent and a neutral guide sends the reader elsewhere to pick a tool.

### 15. Selling the product in a bottom-funnel post is intent matching, not salesiness  `113.7`
*core · best practices · source 113*

Grow and Convert attack the standard advice not to be too salesy by reframing it as a ranking argument rather than a taste argument. If someone searches best project management software, their intent is to learn the details of various options: what is better about one than another, how they compare, which is better for whom. Discussing those product details is not being salesy for that query, it is fulfilling search intent, which they treat as a ranking factor deciding whether the page ranks at all. So targeting high buying intent keywords necessitates discussing your product. They note most content marketers barely mention the product, glancingly link a product page, and rely on pop-ups, opt-in forms and CTA graphics to take care of conversions, which they tie back to the top-of-funnel culture of whitepapers, infographics and ultimate guides.

> "it's just fulfilling search intent"

**Evidence:** Grow and Convert sell their clients' products in every piece they produce, on the grounds that their focus on high buying intent keywords requires it.

**How to do it**

1. For each bottom-funnel post, write down what a searcher on that query needs to decide, in one sentence.
2. Check the draft answers that decision with specifics: features, how they solve the pain, who each option suits.
3. Replace any single glancing product-page link with a full section that explains how your product handles the job.
4. Weave in testimonials and case studies as evidence for the claims rather than as separate trust blocks.
5. Name at least one differentiator against a specific competitor rather than describing your product in isolation.
6. Delete the assumption that pop-ups and CTA graphics will carry conversion, and remove any that interrupt the comparison the reader came to make.
7. Reread the draft against the query: if a reader still cannot say why they would pick you, the post has failed intent, not just conversion.

**Pitfall:** Writers trained on top-of-funnel rules self-censor product detail on commercial queries, then the page under-serves the intent and rankings suffer as well as conversions.

**Apply at Pabau:** Pabau's comparison and best-of articles should discuss Pabau features in depth, not mention it once. That is intent matching for those queries, and it is compatible with the house rule of introducing Pabau on first mention as practice management software like Pabau.

**Apply anywhere:** On commercial queries, in-depth product discussion is what the searcher asked for. Replace glancing product links with a full section on how your product handles the job, backed by testimonials and named differentiators.

### 16. Set the beginner or advanced level at the topic, not in the writing  `99.5`
*core · best practices · source 99*

Khanal corrects a belief he used to hold. He assumed that spelling out obvious details in a post risked making it read as beginner level, which is what Grow and Convert call Mirage Content. He now says the advanced versus beginner distinction happens at the topic level, not in the writing. Topic selection should still be as advanced as the target customer, which is why he rejects posts like '9 Tips for IT professionals in 2019' or a free guide aimed at CTOs, because wanting nine tips about your own job is not a pain point. But once the topic is chosen, detail should never be held back for fear of sounding basic. His mechanism is that details behind a claim show the author knows what they are talking about, and details behind a pain point show the author knows what the reader is going through. So details are the sign of advanced knowledge, not the opposite. He ties this to the Specificity Strategy: specificity and detail are the same thing, guiding both topic and writing.

> "details are the sign of advanced knowledge"

**Evidence:** Khanal's reversal of his own prior position, tied to Grow and Convert's Customer-Content Fit and Mirage Content frameworks and their Specificity Strategy post.

**How to do it**

1. Set the level of the piece when you pick the topic, using customer research rather than keyword volume.
2. Reject topic formats that a veteran in the role would never search, such as generic tips roundups about their own job.
3. Once the topic is locked, stop rationing detail in the draft.
4. Add the why and how behind each step even when the step looks obvious to you.
5. Judge a passage as beginner level only if the topic is beginner level, not because the explanation is thorough.
6. Use the same specificity standard for the headline topic and for every supporting section.

**Pitfall:** Teams strip explanatory detail from advanced pieces to keep them sounding senior, which removes the exact material that proves seniority. The signal is a short article full of assertions aimed at experts.

**Apply at Pabau:** Pabau articles aimed at practice owners should not cut the step-level explanation to sound senior. Pick a topic a practice owner would actually search, then explain the workflow fully, including the settings and the failure cases.

**Apply anywhere:** Pick a topic your experienced reader would actually search, then explain the workflow fully. Do not cut step-level explanation to make the piece sound senior.

### 17. Show the draft to real target customers and ask if it is valuable  `122.9`
*core · concrete actions · source 122*

The strongest validation move in the FundersClub workshop cost nothing. Grow and Convert had VC partners and portfolio company founders in the room, so they asked the already-funded founders directly whether the Series A checklist piece would be valuable to them. They all said no. That single question settled an argument that could have run for months in an editorial meeting, and it changed the direction of FundersClub's content strategy. The technique generalizes: rather than debating whether a piece serves the target reader, put it in front of three or four people who match the best-customer profile and ask them. Their answer replaces internal opinion, and it can be gathered by email in a day.

> "if this piece would be valuable to them, they all said no"

**Evidence:** Every already-funded founder in the FundersClub workshop said the Series A checklist would not be valuable to them, and the firm changed strategy as a result.

**How to do it**

1. Pick three to five contacts who match the best-customer profile, ideally existing customers.
2. Send them the live URL or the outline of a planned piece, with no framing about who wrote it.
3. Ask one question: would this be valuable to you, yes or no, and why.
4. Treat a majority no as disqualifying regardless of traffic potential.
5. Ask the same people what they would have wanted to read instead, and log those answers as topic candidates.
6. Repeat the check on the first piece produced under the new direction to confirm the fix landed.

**Pitfall:** Asking people who are not in the profile, including your own team or general industry contacts. They will say the piece is useful, because it is useful to them, and that is the mismatch you are trying to detect.

**Apply at Pabau:** Pabau has clinic customers who will answer this by email. Before publishing the next template or blog piece aimed at practice owners, David should send the outline to four owner-operators and ask the yes or no question.

**Apply anywhere:** Put the piece, or its outline, in front of a handful of people who match your best-customer profile and ask whether it is valuable to them. Their no outranks the editorial team's yes.

### 18. Sit in on sales calls and reconcile the two sets of talking points  `177.5`
*core · concrete actions · source 177*

The author's third fix is to have marketers sit in on sales conversations so they learn the talking points and the shape of a real call. He reports a specific finding from doing this repeatedly: sales and marketing were not on the same page, because marketing had one set of talking points and sales had another. His claim about the consequence is direct. When that misalignment happens, prospects get confused and buy from someone else. The remedy he names is to work out how to sell through the buyer's journey as a team, which he says has the best impact on the bottom line. For content, this is a check on whether the value proposition in an article survives contact with the conversation that follows the click.

> "Have marketers sit in on sales conversations"

**Evidence:** The author reports finding talking-point misalignment repeatedly when marketers sat in on calls.

**How to do it**

1. Have each marketer listen to at least two live or recorded sales calls a month.
2. Write down the exact phrases the rep uses for the value proposition and the differentiators.
3. Put those phrases beside the ones used on your landing pages and in your articles, in one document.
4. Mark every place the two disagree, including differences in ordering and emphasis.
5. Settle each conflict with sales rather than unilaterally editing the page, and record the decision.
6. Map the agreed talking points to each stage of the buyer's journey.
7. Update the affected pages and brief sales on what changed, so the handoff stays consistent.

**Tools:** Gong

**Pitfall:** The failure mode is silent: pages and calls each read fine on their own, but the prospect hears a different pitch after clicking and goes elsewhere. You only see it if you put the two sets of wording side by side.

**Apply at Pabau:** David should compare the wording on Pabau's product and comparison pages against how the sales team describes the same features on demo calls. Where they differ, the page is setting up a conversation the rep then has to correct.

**Apply anywhere:** Have marketers listen to sales calls monthly and transcribe the exact value-proposition wording reps use. Put it beside your page copy, mark every disagreement, and settle each one with sales.

### 19. Sort a declining blog into four buckets before choosing any fix  `116.2`
*core · concrete actions · source 116*

When conversions plateaued for a SaaS client after roughly 71 posts over two years, Grow and Convert ran a high-level audit that sorted every article by two axes: how it ranks for its target keyword, and how it converts. That gives four buckets. Posts that used to convert well but fell out of the top three. Posts still in the top three that converted less anyway. Posts always in the top three that never converted much. Posts that never ranked and never converted. They excluded the most recent three months of publishing from the tally, since new posts have not had time to rank. Of the 60 posts that qualified, 31 were still converting at least once a month, which told them the problem was concentrated, not systemic.

> "We grouped these posts into 4 different categories"

**Evidence:** Grow and Convert audited ~71 posts for a SaaS client; after excluding three months of new posts, 31 of 60 were still converting at least monthly.

**How to do it**

1. List every published post with its target keyword, current position, and conversions per month.
2. Exclude anything published in the last three months from the audit tally.
3. Mark each post as converting consistently if it produced at least one conversion a month.
4. Bucket 1: was high-converting, now out of the top three for its target keyword.
5. Bucket 2: still in the top three but conversions have dropped significantly.
6. Bucket 3: always in the top three but never converted much.
7. Bucket 4: never consistently ranked and never converted.
8. Count how many posts still convert so you know whether the decline is site-wide or limited to a handful of pages.

**Tools:** GA4, Ahrefs

**Pitfall:** Including recently published posts drags the ranking-and-converting ratio down and makes a healthy blog look broken. Grow and Convert cut three months of publishing out of the count for exactly this reason.

**Apply at Pabau:** Pabau's blog audit should be a table of post, target keyword, current position and demo requests per month, with the last three months of publishing excluded. Sorting into these four buckets tells David which articles to refresh first instead of refreshing by publish date.

**Apply anywhere:** Build an audit table of post, target keyword, current position and conversions per month, excluding the last three months of publishing, then sort into those four buckets before choosing any fix.

### 20. Spend thought leadership ideas inside boring SEO posts, not only white papers  `125.12`
*core · best practices · source 125*

Grow and Convert push back on the assumption that thought leadership content means the white paper or the standalone provocative opinion piece. They argue it is also expressed in smaller ways throughout otherwise unsexy or utilitarian content. The same unique idea that would carry an opinion piece can serve as a supporting argument or originality nugget inside an SEO piece targeting a boring keyword like best accounting tools. The same goes for small in-the-weeds details from daily executors. They call this what makes everyday content stand out. The strategic payoff is that most companies do not have enough unique ideas to fill whole articles, but every idea they do have can be spread across the utilitarian content they were publishing anyway, which pushes ordinary posts toward being perceived as leadership.

> "originality nuggets inside an SEO piece targeting a boring keyword"

**Evidence:** Grow and Convert's stated strategy of inserting originality nuggets into SEO pieces on utilitarian keywords such as best accounting tools, on the grounds that most companies' ideas do not warrant whole articles.

**How to do it**

1. Keep a running list of every unique idea the company holds, sourced from founders and executors.
2. Before drafting any SEO article, check that list for an idea relevant to the keyword.
3. Assign at least one idea to each article as a supporting argument, not as the article's topic.
4. Place the idea where it does work, usually as the reason behind a recommendation the competing pages state without reason.
5. Reuse the same idea across several articles rather than reserving it for one flagship piece.
6. Retire a piece from the plan if no idea on the list can attach to it.
7. Reserve standalone opinion pieces and white papers for the two or three ideas strong enough to carry a whole argument.

**Pitfall:** Companies save their few real ideas for a flagship white paper nobody reads, and publish undifferentiated posts everywhere else. The signal is a blog where only one page says anything a competitor could not have written.

**Apply at Pabau:** Pabau's ideas about aesthetic practice operations should appear inside the template pages and best-tool listicles, not only in a dedicated opinion post. David should require one named idea per brief even on code-reference and template pages.

**Apply anywhere:** Spread your few genuine ideas across the utilitarian SEO posts you were publishing anyway, as supporting arguments. Reserve standalone opinion pieces for the two or three ideas strong enough to carry an argument alone.

### 21. Spin off dedicated pages when a converting page ranks p2-3 for variants  `102.15`
*core · concrete actions · source 102*

Grow and Convert give a specific expansion trigger from their measurement loop. If Google Search Console shows a piece of content that is converting well and also ranking on page 2 or 3 for a number of different keyword variations, that is the signal to create dedicated pages targeting those terms. Two conditions have to hold together: the page already converts, which proves the topic produces customers, and it ranks in positions 11 to 30 for variants, which proves the variants have demand and are within reach. They pair it with a second trigger from the conversion report: if one category of keywords is driving a high share of overall conversions, prioritize more keywords from that category. Both turn measurement into the next content calendar rather than a status report.

> "ranking on page 2 or 3 for a bunch of different keyword variations"

**Evidence:** Grow and Convert name page 2 or 3 rankings on a converting page as their trigger for creating dedicated pages.

**How to do it**

1. Filter GSC by page for your converting articles and list every query where the page sits in positions 11 to 30.
2. Keep queries with meaningful impressions and a distinct intent from the page's own target keyword.
3. Check each kept query's SERP; if the ranking pages are dedicated to it, build a dedicated page.
4. Write the new page for that one query and link it to and from the parent article.
5. Separately, group conversions by keyword category and rank the categories by share of total conversions.
6. Weight the next quarter's calendar toward the top converting categories and drop the categories producing none.

**Tools:** Google Search Console

**Pitfall:** Spinning off a variant that shares a SERP with the parent, which cannibalizes the page that was already converting. Check the SERP overlap before building.

**Apply at Pabau:** Pabau should run this GSC check monthly on its converting template and comparison pages, and build dedicated articles for the position 11 to 30 variants instead of adding more sections to pages that already work.

**Apply anywhere:** Each month, list the position 11 to 30 queries on your pages that already convert, and build a dedicated page for each variant with a distinct SERP. Also weight the next calendar toward the keyword categories driving the most conversions.

### 22. Split near-identical keywords because top 3-5 clicks dwarf lower spots  `115.4`
*core · content insights · source 115*

Grow and Convert add a click-distribution argument to the usual case for one page per keyword. They concede a single article can often rank on page one for two near-identical variants. What it struggles to do is reach the top three to five positions for both, and clicks in those top spots heavily outweigh clicks from the bottom half of page one. So a bundled page that ranks fifth and ninth loses far more than half the traffic of two dedicated pages ranking first and second. Their worked examples: Geekbot ranking first for both 'daily standup meeting' and 'daily catch up meeting' with two separate articles, and Circuit ranking first for 'delivery driver tracking app' and second for 'gps app for delivery drivers' with two more. The point is that page-one presence is the wrong success bar when deciding whether to split.

> "it's hard to get into the top 3 to 5 positions"

**Evidence:** Geekbot ranked #1 for both 'daily standup meeting' and 'daily catch up meeting' with separate articles; Circuit ranked #1 for 'delivery driver tracking app' and #2 for 'gps app for delivery drivers' with separate articles.

**Pitfall:** Judging a bundled page as a success because it ranks on page one for both variants. Positions six to ten pass a fraction of the clicks of positions one to three, so the loss never appears in a rankings report that only checks page-one presence.

**Apply at Pabau:** When David reviews a Pabau article ranking sixth and eleventh for two variants, the fix is to split it rather than to keep optimizing one page. Set the internal bar at top three for the single target keyword, not page one for several.

**Apply anywhere:** When deciding whether to split near-identical keywords, judge by top-three potential rather than page-one presence. One page can usually reach page one for two variants but rarely the top three to five for both, and click volume is concentrated in those spots.

### 23. Split near-identical keywords into separate pages because you get one title  `108.22`
*core · best practices · source 108*

Grow and Convert call this a differentiator of their agency's strategy: build a dedicated page for each high-intent keyword even when two keywords are nearly identical and mean almost the same thing. Their mechanism, credited to a conversation with Bernard Huang of Clearscope, is that you only get one SEO title, one H1 and one meta description per page, and those are key ranking factors for top positions. Cover two target keywords with one article and it usually ranks for only one of them, or misses the intent of both and ranks for neither. They stress this matters most on high buying-intent terms, where competition is fierce and competitors are already building dedicated pages, so a bundled page starts at a disadvantage. The trade is more pages and more production cost, accepted deliberately because the terms convert.

> "even when keywords are nearly identical and have similar meanings"

**Evidence:** Grow and Convert credit the reasoning to Bernard Huang of Clearscope: one SEO title, one H1 and one meta description per page, all key ranking factors.

**How to do it**

1. Take the bottom-funnel keyword list and stop grouping variants into clusters by default.
2. For each pair of similar terms, search both and compare the top ten results.
3. Treat the pair as one page only if the results are essentially the same URLs in the same order.
4. Where the results differ at all, commission two pages.
5. Give each page its own title, H1, meta description and URL built around its single keyword.
6. Write each page to that keyword's specific intent rather than covering both angles.
7. Cross-link the pair so they support each other rather than compete.
8. Check after three months whether either page ranks for the other's term, and split further if one is absorbing both.

**Pitfall:** Bundling variants to save production budget. The page ranks for one term, the other stays unranked, and the loss is invisible because the page looks like a success.

**Apply at Pabau:** Pabau should split near-duplicate aesthetics terms into separate pages rather than merging them into one long guide, especially where the SERPs differ, and cross-link the pair instead of consolidating.

**Apply anywhere:** Build one page per buying-intent keyword, even for near-identical terms, because a page has only one title, H1 and meta description. Compare the two SERPs first and merge only when the ranking URLs are effectively the same.
