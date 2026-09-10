# Content Quality — supporting (part 1 of 7)

23 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. A 'satisfied searcher' either stays or searches a different query  `42.5`
*useful · content insights · source 42*

The operational definition of a page that satisfies search intent is a page where a visitor arriving from a search engine is satisfied enough that they don't go back to the search results at all. If they do go back, it should be to search for something different, because they already got their answer or completed what they came to do on your page. This distinguishes true intent satisfaction from simple bounce-rate or time-on-page metrics. Someone who pogo-sticks back to refine or re-search the same query is a signal of dissatisfaction, while someone who returns to search an unrelated follow-up query is not, even though both can look identical in a basic "did they leave" metric.

> "they're not going back to the search results"

**Apply at Pabau:** For Pabau's content, don't just track whether a visitor bounces; consider whether return searches, where trackable, such as a subsequent branded search or a related but different query, represent task completion rather than dissatisfaction, and design pages so a reader who came with a specific question or task can fully resolve it on-page before deciding whether to explore further.

**Apply anywhere:** For your content, don't just track whether a visitor bounces; consider whether return searches, where trackable, such as a subsequent branded search or a related but different query, represent task completion rather than dissatisfaction, and design pages so a reader who came with a specific question or task can fully resolve it on-page before deciding whether to explore further.

### 2. AI writes to the average, so force it into the top 10% with three inputs  `68.15`
*useful · best practices · source 68*

Cody's rebuttal to the claim that AI content does not rank is that it is user error and cope. His mechanism is specific: the model is trained to the average, so a bare instruction to write a blog post about a keyword returns an average blog post by construction. To pull output into the top 10 percent he supplies three inputs. First, he scrapes what currently ranks on page one for the target phrase and puts it in context. Second, he records a transcript of himself talking about the industry, his example being how AI is changing data analytics. Third, he specifies tone of voice. He then instructs the model to combine the source content with his own insights, and runs it on Claude or Gemini 2.5 Flash. His success criterion is behavioural, not stylistic: the reader gets value and does not bounce, which is what Google actually measures. This adds the model recommendation and the trained-to-the-average framing to what the base already records about scraping page one.

> "is trained to the average"

**Evidence:** Cody claims this produces content 99% of readers find valuable, and ties ranking to them not bouncing from the page.

**How to do it**

1. Scrape the full text of every page ranking on page one for the target phrase and paste it into context.
2. Record yourself talking through the topic from your own experience and transcribe it.
3. Write out the tone of voice explicitly rather than assuming the model infers it.
4. Instruct the model to combine the ranking-page source material with your transcript insights, in your stated tone.
5. Run it on a long-context model such as Claude or Gemini 2.5 Flash.
6. Check the output answers the query's question directly rather than circling it.
7. Judge the result on whether a reader would bounce, since that is the signal that decides ranking.

**Tools:** Claude, Gemini

**Prompt / template:**

```text
Here is the source content to work from: [page-one scrapes]. Here is the tone of voice to work from, with my own insights: [interview transcript]. Combine these into an output.
```

**Pitfall:** Prompting for a blog post on a keyword with no supplied context returns average content by design, which is exactly the output people then point at as proof AI cannot write.

**Apply at Pabau:** Pabau's AI-assisted drafting should never run without all three inputs attached, and the recorded practitioner interview is the input most often skipped and the one that makes the article defensible.

**Apply anywhere:** Never prompt a model for an article with only a keyword. Supply the page-one scrapes for coverage, a recorded transcript of your own expertise for originality, and an explicit tone spec, then run it on a long-context model.

### 3. Add a smidge of uniqueness, not a claim of having no competitors  `159.8`
*useful · best practices · source 159*

Grow and Convert's third positioning criterion is competitive advantage, and their qualifier is deliberate: add just a smidge of uniqueness. They say you do not need a lot, and that being so unique you have no competitors is usually a dangerous sign because it suggests no market. Their observation from client work is the opposite problem. Companies routinely have genuine competitive advantages that never appear anywhere in their positioning, and only surface in conversation. Benji's line is that the agency is not surfacing what makes it unique, it is generalizing because it has not gone through the process of determining what it is best at. The fix they recommend is not inventing a differentiator but pulling one out of the targeting and pain point work already done in criteria one and two.

> "add just a smidge of uniqueness"

**Evidence:** Grow and Convert say they repeatedly meet companies with real competitive advantages that appear nowhere in the positioning, discovered only in person.

**How to do it**

1. Ask the founders and delivery team, in conversation, what work the company is genuinely best at.
2. Write down every specific answer, including ones that feel too small to be a differentiator.
3. Cross-check each against the target customer and pain point you already chose, and keep the ones that reinforce them.
4. Reject any claim you cannot support with delivered work.
5. Put the surviving claim into the headline or subhead in concrete terms, naming the segment or the capability.
6. Do not chase a differentiator so unusual that no competitor exists, since that usually signals no demand.
7. Re-ask the team every six months, since new capabilities appear faster than the site copy is updated.

**Pitfall:** Generic claims because nobody ran the exercise. The signal is a homepage whose claims would still be true if a competitor's logo were dropped on it.

**Apply at Pabau:** Pabau should name specific advantages on product pages, such as depth of aesthetics-specific charting or the iOS app, rather than general claims about saving time that any practice management vendor could make.

**Apply anywhere:** Interview your own delivery team for what you are genuinely best at, then put the most specific defensible claim into the headline. Generic claims survive only because nobody ran the exercise.

### 4. Address clinical, financial and operational buyers in one B2B health post  `117.16`
*useful · concrete actions · source 117*

For B2B healthcare, Grow and Convert say the difficulty is not vulnerability but multiplicity. You are speaking to several stakeholders with different priorities at once: physicians focused on clinical outcomes and administrators focused on costs, across a longer sales cycle where several options are being evaluated. The content still has to sell, but it has to build credibility with both groups at different touchpoints, addressing clinical, financial and operational concerns. The practical consequence for keyword work is that you must understand what each persona would search when evaluating solutions, since they use different language for the same purchase. A single post that only speaks clinically will not survive the administrator's review, and one that only speaks to cost will not get past the clinician.

> "physicians focused on clinical outcomes and administrators focused on costs"

**Evidence:** Grow and Convert report this pattern across their B2B healthcare clients over ten years of agency work.

**How to do it**

1. List the stakeholders who touch the purchase: clinician, administrator, operations lead, owner.
2. Write the primary concern of each in one line: outcomes, cost, workflow disruption, risk.
3. For each persona, note the search phrasing they would use when evaluating solutions, and check those terms separately.
4. In each bottom-funnel post, give clinical outcomes, cost and operational impact their own section.
5. Put the persona-specific proof next to each: outcome data for clinicians, pricing and ROI for administrators.
6. Map the personas to touchpoints so early posts educate and later posts answer the evaluation questions.

**Pitfall:** Writing to one persona means the post is forwarded internally and dies at the second reader, who finds nothing addressing their objection.

**Apply at Pabau:** Pabau sells to clinic owners, practitioners and front-desk managers at once. Bottom-funnel articles should carry a section each on clinical workflow, cost and day-to-day operations rather than one blended argument.

**Apply anywhere:** In B2B healthcare, write each bottom-funnel post for every stakeholder in the decision. Give clinical outcomes, cost and operational impact their own sections with proof matched to each.

### 5. Aim for the top three, because lower page-one spots barely convert  `94.5`
*useful · best practices · source 94*

Grow and Convert add an aside that governs how much effort a target keyword deserves. The vast majority of conversions they generate for clients come when a post ranks in the top three spots for its target keyword. Their point is that bolting a target keyword onto an existing page can get you onto the top two pages of Google, or the bottom half of page one, but in their experience it will not get you into the top three, so you still miss most of the available conversions. This is the argument against the cheap option of optimizing what you already have. It also sets the bar for judging a page after publication: position seven is not a partial win, it is a page that needs the dedicated treatment it never got.

> "come when posts rank in the top 3 spots"

**Evidence:** Grow and Convert say the vast majority of client conversions come from top-three rankings, and that keyword-bolted existing pages in their experience do not reach the top three.

**How to do it**

1. Set top three, not page one, as the success threshold for every bottom-of-funnel keyword you track.
2. Review each tracked page at 90 days and split them into top three, positions 4-10, and beyond.
3. For anything stuck in positions 4-10, check first whether the page was purpose-built for that keyword or had it bolted on.
4. Rebuild bolted-on pages as dedicated pages rather than tweaking the existing copy.
5. Compare conversions from your own top-three pages against your positions 4-10 pages to confirm the gap on your data.
6. Drop keywords where the top three are all incumbents with tailored pages and thousands of links, and spend the effort on a qualified variant instead.

**Tools:** Google Search Console, Ahrefs

**Pitfall:** A page sitting at position six looks like progress in a rank tracker and produces almost nothing. Reporting on average position instead of conversions per page hides this for months.

**Apply at Pabau:** Pabau should judge blog performance by how many bottom-of-funnel keywords sit in the top three, not by page-one counts, and rebuild anything stuck mid-page-one as a purpose-written article.

**Apply anywhere:** Treat top three as the success threshold for buying-intent keywords. Review tracked pages at 90 days, and rebuild anything stuck in positions 4-10 as a page written for that one keyword.

### 6. Answer 'free' keywords with a hidden-costs piece, not a fake free claim  `109.6`
*useful · concrete actions · source 109*

Grow and Convert give a specific rule for the 'free' modifier when your product is not free. If you offer a genuine free plan, the keyword is not deviant at all and you should target it directly. If you only offer a temporary free trial, do not frame the product as free, because it annoys readers who arrive expecting free and find a paywall. The recommended play is to target the free keyword with a piece on the pros and cons of free software in your category, weighted toward the cons. Their worked example title is The Hidden Costs of Free CRM Software. The page still matches the query, since the searcher wants to know whether free will work, and it converts because the honest answer for most buyers is that it will not.

> "we'd target the 'free' keyword by writing a piece that highlights"

**Evidence:** Grow and Convert's stated approach for clients with trial-only pricing, exemplified by The Hidden Costs of Free CRM Software.

**How to do it**

1. Check first whether you have a permanent free tier; if so, target the free keyword directly and skip this play.
2. If you only have a trial, do not use the word free to describe the product anywhere on the page.
3. Build the page as an honest assessment of free tools in your category, listing pros before cons.
4. Name the actual free products by name, since the searcher will check whether you have covered them.
5. Make the cons concrete: record limits, seat caps, missing integrations, data export restrictions, support tiers.
6. Quantify one cost of the free route in money or hours so the trade-off is measurable.
7. Introduce your paid product late, framed as what the reader needs once the free limit bites.
8. Title it around hidden costs rather than around your product, following the pattern of The Hidden Costs of Free CRM Software.

**Pitfall:** Framing a trial-only product as free to capture the query produces angry visitors and no conversions. The signal is high traffic with near-zero signup rate on the page.

**Apply at Pabau:** Pabau has structured onboarding rather than a free trial, so free-software queries in the aesthetic practice space should be answered with a hidden-costs article that names the actual free booking and records tools and shows where they break for a growing clinic.

**Apply anywhere:** If your product is not genuinely free, do not chase free keywords by implying it is. Write an honest hidden-costs piece that names the real free tools and quantifies where they fail, then position your paid product as the next step.

### 7. Answer the beginner question anyway when the beginner is your buyer  `111.12`
*useful · content insights · source 111*

The base already carries the rule that bottom-funnel audiences should not be served beginner content. Grow and Convert qualify it here. They targeted 'daily standup questions' for Geekbot and describe the searcher as looking for beginner-level information, such as what questions typically get asked during a daily standup. They answered it, and also found natural ways to tie in the product, which they say increased the conversion rate. The distinction is which audience the beginner query belongs to. A beginner query inside your product's exact job is a person setting up the workflow your tool runs, so answering it plainly is right. The mistake they warn against elsewhere in the article is different: writing beginner-level content for advanced B2B audiences on topics only loosely related to the product, such as industry trends and ultimate guides.

> "The searcher is looking for beginner-level information"

**Evidence:** Geekbot's 'daily standup questions' post answered a beginner query and still tied in the product to raise conversion rate.

**Pitfall:** Using this as licence to publish beginner explainers generally. It only holds when the beginner query is about setting up the exact workflow your product runs.

**Apply at Pabau:** Pabau can publish beginner pieces like 'what to ask in an aesthetic consultation' because the searcher is configuring a workflow Pabau runs. Beginner pieces about general clinic business topics stay off /blog/.

**Apply anywhere:** Beginner-level queries are fine when they sit inside the workflow your product runs, because the searcher is configuring that workflow. They are not fine when the topic is only loosely related to what you sell.

### 8. Answer the beginner question fully, then tie the product in naturally  `132.12`
*useful · concrete actions · source 132*

Grow and Convert describe their handling of a beginner-level top-funnel keyword for Geekbot: 'daily standup questions', where the searcher wants to know what questions typically get asked in a daily standup. Their approach was to answer that question, then find natural ways to tie in the product, which they say increases the conversion rate. The wording matters. The answer comes first and it is complete, because the page has to satisfy a search that had no product intent behind it. The product appears where the answer itself opens the door, for example where the reader now needs somewhere to collect those answers day after day. This is the same pattern as the frustration keyword 'standup meetings waste of time', where they validate the frustration and then present Geekbot as a potential solution to that problem.

> "we also find natural ways to tie in the product, thus increasing the conversion rate"

**Evidence:** Geekbot's 'daily standup questions' and 'standup meetings waste of time' pages, part of the top-funnel set that produced 397 conversions from 204,303 sessions.

**How to do it**

1. Answer the beginner question directly and completely near the top of the page, in the searcher's own framing.
2. List the practical detail a newcomer needs next: how often, who is involved, how long, what usually goes wrong.
3. Identify the point in that answer where following the advice manually becomes tedious or error-prone.
4. Insert the product there as the way to do what you just described repeatedly, not as a separate pitch block.
5. Show it concretely with a screenshot or a short walkthrough rather than a feature claim.
6. For frustration keywords, validate the complaint first with the specific reason the current method fails, then present the product as one option among the alternatives.
7. Keep the product section short enough that the page still reads as an answer, and close with a low-commitment next step.

**Pitfall:** A product mention bolted onto the end of an informational post reads as an ad and converts nothing. The tie-in has to sit at the point where the reader's own next problem appears, which means you need to know what that problem is.

**Apply at Pabau:** Pabau's guide-style articles should answer the operational question in full, then introduce Pabau at the point where doing it by hand every day becomes the problem. A closing paragraph mentioning Pabau with no link to the question just answered will keep those pages near the 0.19 percent floor.

**Apply anywhere:** On beginner-question keywords, answer the question completely first, then place the product exactly where following your own advice manually becomes tedious. On frustration keywords, validate the complaint with a specific reason the current method fails before offering your product as one of the alternatives.

### 9. Apply show-don't-tell selectively because data and steps should be told  `99.12`
*useful · content insights · source 99*

Khanal distinguishes his detail principle from the writing-advice cliche 'show don't tell', which he notes is applied almost exclusively to fiction. He checked: a Google search for 'show don't tell writing' returns ten results that only give fiction examples, the most famous being Chekhov's line about the glint of light on broken glass rather than the shining moon. For non-fiction marketing content he says many details can or should be told outright. Data should be told: 'when we applied this method, our traffic doubled to 25,000 pageviews.' Steps in a how-to should usually be told: do not show what it feels like to set up a Google Analytics report, just tell the reader how to set it up. The second difference is that show-don't-tell asks you to eliminate claims, whereas his principle keeps the claim and adds backup, because the backup does not make sense without the claim stated first.

> "we're not asking you to **eliminate** claims"

**Evidence:** Khanal's check of the top ten Google results for 'show don't tell writing', all of which drew examples from fiction only.

**Tools:** Google Analytics

**Pitfall:** Writers trained on fiction advice bury results in narrative scene-setting, which makes a data point harder to extract and harder for a search engine or model to quote.

**Apply at Pabau:** Pabau articles should state results and steps plainly rather than dramatizing them, then add the detail underneath. This also keeps the capsule-answer format that AI answers extract cleanly.

**Apply anywhere:** State results and steps plainly rather than dramatizing them, then add detail underneath. Plain statements also extract more cleanly into AI answers.

### 10. Apply three quality levers once the topic is right: specificity, intro, funnel stage  `122.14`
*useful · best practices · source 122*

Grow and Convert separate fit from execution and name three ways a correctly aimed piece still fails. First, specificity: do not blow it by making a single article's topic too broad. Second, introductions: do not blow it by having a terrible introduction. Third, funnel mapping: strategically create content to attract buyers at different buying stages rather than treating every piece the same. The ordering matters. These levers only pay off after content-customer fit exists, because a tightly written, well-introduced, correctly funnel-mapped article for the wrong reader still produces nothing. Used together with fit, they are what turns the right topic into a piece that converts.

> "Don't blow it by making a single article's topic too broad"

**Evidence:** Grow and Convert list specificity, blog introductions and funnel mapping as their three published execution levers, positioned after the customer research work.

**How to do it**

1. Check each planned piece covers one pain point, and split it if the outline needs more than one.
2. Write the introduction to name the reader's specific situation in the first two sentences, not the category.
3. Tag every piece with its funnel stage and match the CTA to that stage.
4. Keep a deliberate mix across stages rather than publishing only top-funnel explainers.
5. Reject any outline whose title could apply to three different audiences.
6. Review the intro separately from the body in editing, since it is the most common failure point.

**Pitfall:** Applying these levers before fixing fit. Sharper writing on a piece aimed at the wrong buyer just makes the mismatch more polished.

**Apply at Pabau:** Pabau template pages should each serve one clinic job, with an intro that names the situation, and a CTA matched to stage. A comparison page gets a demo CTA; an early explainer does not.

**Apply anywhere:** Once the topic fits the buyer, tighten execution with three levers: one pain point per article, an introduction that names the reader's situation, and a CTA matched to the funnel stage.

### 11. Assume your B2B customer knows more than any writer you hire  `126.14`
*useful · content insights · source 126*

Grow and Convert explain why self-research fails in B2B specifically. For many B2B companies the customer often knows more about the topic than the writer does, because the customer is usually an executive or someone who has been in the industry for years, has done deep research on all the alternatives to your product, and lives and breathes these problems every day in their job. A writer who Googled the topic for a couple of hours is writing above their own knowledge and below the reader's. Grow and Convert turn this into a direct comparison: if someone is Googling enterprise reporting tools, who can better answer their questions, April who does this every day for her job, or a writer who Googled the topic for a couple of hours. The consequence is that anything discoverable in two hours of Googling is already known to the reader.

> "your customer often knows more about the topic"

**Evidence:** Grow and Convert contrast April, a customer success manager working with enterprise clients daily, against a writer with two hours of Googling.

**How to do it**

1. Write a one-line profile of the reader's seniority and years in the field for each target keyword.
2. Assume everything findable in two hours of search is already known to that reader.
3. Cut any passage that only restates category basics.
4. Set the article's floor at what the reader could not have found themselves.
5. Source that floor from the internal expert who talks to those readers daily.
6. Have the internal expert read the draft and flag anything they would consider obvious.

**Pitfall:** Writing for a beginner when the searcher is a buyer. The signal is a page that ranks and gets impressions but converts nothing, because the reader learned nothing.

**Apply at Pabau:** Pabau's readers are practice owners and managers who have already used one or two systems. Articles that explain what practice management software is are below their level. Aim the floor at what a Pabau CS manager knows and a competitor's blog does not.

**Apply anywhere:** In B2B, assume the searcher has more industry experience than your writer. Anything discoverable in two hours of search is already known to them, so set the article's floor at what only your internal expert could supply.

### 12. Attach a specific story to every item in a list post  `100.17`
*useful · concrete actions · source 100*

The Patreon business models post is a simple list, yet Grow and Convert single out that each idea has a specific story attached to it. They got those stories by interviewing someone inside Patreon and pulling examples from named creators on the platform, and they note the team inside Patreon thinks about business models constantly because helping creators succeed is one of their biggest goals, which makes it equivalent to interviewing an expert. Without deliberate SEO optimization for any specific keyword, the post ranks top five for 'best patreon models' (300 searches a month), 'patreon models' (300) and 'patreon ideas' (200), and gets 6,000 to 7,000 pageviews a month primarily from search. They acknowledge publishing on patreon.com helps it rank for branded terms, but insist the story-per-item quality is what makes it work.

> "Each idea has a specific story attached to it"

**Evidence:** The Patreon business models post ranks top five for 'best patreon models' (300/mo), 'patreon models' (300) and 'patreon ideas' (200) and draws 6,000 to 7,000 pageviews a month, mostly from search, with no deliberate keyword optimization.

**How to do it**

1. Interview someone with a front-row view of the topic, ideally inside the company that owns the ecosystem.
2. Ask for one concrete example per list item, with a named subject and what happened.
3. Reject list items you cannot attach a real story to, and cut them rather than padding.
4. Write the story before the explanation, so the reader sees evidence first.
5. Name the source of each story in the copy so the piece carries verifiable detail.
6. Keep the list format that search intent demands; the stories are the nugget inside it.
7. Watch which items get quoted or linked, and expand those into their own posts.

**Pitfall:** Filling a list to a round number with items that have no story behind them dilutes the piece. The signal is that half the entries are two generic sentences.

**Apply at Pabau:** Pabau's listicles of clinic marketing ideas or retention tactics should carry a named practice's story per item, sourced from customer success. Cut items that have no real example rather than padding to a round count.

**Apply anywhere:** Give every item in a list post a specific, named story sourced from an interview. Cut items you cannot evidence rather than padding the count.

### 13. Attack the part of your market that runs on guesswork  `170.12`
*useful · content insights · source 170*

The whole business started from one observed contradiction. Companies told Campbell they poured time and effort into their product, but for pricing, in their own words, 'we just throw shit out there and see how it does.' He found that illogical and asked whether a smarter system was possible. The general pattern is a useful topic and product filter: find the decision in your market where sophisticated operators invest heavily on one side and improvise on the other. That asymmetry is where a rigorous method has obvious value, where no incumbent content exists, and where the audience already knows privately that they are guessing.

> "when it comes time to ascribe the value"

**Evidence:** Campbell's econometrics background plus the repeated observation that clients guessed at pricing became Price Intelligently, now over $6 million a year.

**Pitfall:** Choosing a topic where the audience already feels competent. If people believe they have the decision handled, a rigorous method reads as overkill rather than relief.

**Apply at Pabau:** Aesthetic practices invest heavily in equipment and training but often improvise on treatment pricing, retention and no-show policy. Those improvised decisions are where David should aim Pabau's most rigorous articles and calculators.

**Apply anywhere:** Find the decision your market invests heavily in on one side and improvises on the other. Build your most rigorous content and tools around the improvised half, because that is where a method has obvious value and no incumbent.

### 14. Audit a case study for what failed and for link building, not just the percentage  `180.10`
*useful · concrete actions · source 180*

Grow and Convert give a checklist for reading an agency case study that goes past the usual traffic percentage. For any claimed increase, work out how many articles it took, whether one article produced most of it or it was spread out, which keywords ranked, how and why those keywords were chosen, how long ranking took, what the client's domain authority was at the start and at the end, whether link building was involved, whether traffic increases turned into trials, demos or revenue, and what did not work. The last two are the ones agencies leave out. Testimonial quotes and lines like 'we grew X company's organic traffic by 200%' are not proof, and traffic growth alone does not show the agency can deliver the qualified leads and product signups a software company actually needs.

> "What didn't work?"

**Evidence:** Grow and Convert say the more transparent an agency is about both the results and how they got them, the more you can trust them to replicate it.

**How to do it**

1. For each claimed result, ask how many articles produced it and over what period.
2. Ask whether one article carried the growth, and check the client's top pages to verify.
3. Get the keyword list and ask why those keywords were selected over alternatives.
4. Ask how long each page took to reach its position, from publication.
5. Ask for the client's domain authority at the start and at the end of the engagement.
6. Ask directly whether links were built during the period, and how many.
7. Ask whether the traffic converted into trials, demos or revenue, and how that was attributed.
8. Ask what did not work in the engagement; an agency with no answer has not analyzed its own results.

**Pitfall:** Being satisfied by a percentage lift. A 200% traffic increase can be one lucky post on an unrelated term, and it says nothing about whether the strategy produces signups.

**Apply at Pabau:** Pabau's own published results and case-study style pages should carry the same details: how many articles, which keywords, how long to rank, and what did not work. That level of disclosure is what makes a page credible to a practice owner comparing vendors.

**Apply anywhere:** Read an agency case study for the mechanics: article count, whether one page carried it, the keyword list and why, time to rank, starting and ending authority, whether links were built, whether it converted, and what failed.

### 15. Audit every live intro with the high-school-teacher question  `127.11`
*useful · concrete actions · source 127*

Grow and Convert give the audit prompt in bold: take a long hard look at your blog introductions and ask yourself if they are written for your target audience or written for a high school teacher reading a student's paper on this topic. They anchor the pattern with a concrete memory, the school essay on dogs that opens 'For centuries, dogs have been a great companion animal to humans.' That is the shape to hunt for. They add a caveat with teeth: if you are trying to add high school students to your email list then so be it, but if you are selling a B2B product to industry veterans you should be more careful. So the severity of the problem scales with the sophistication of your buyer, which makes this a higher-priority audit for B2B and specialist markets than for broad consumer content.

> "written for a high school teacher reading a student's"

**Evidence:** Grow and Convert's 'for centuries, dogs have been a great companion animal to humans' example, given as the exact shape of the pattern to look for.

**How to do it**

1. Export the URL and first 200 characters of every published article, using a crawl or your CMS.
2. Read each opening and mark it if it could plausibly begin a school essay on the topic.
3. Look specifically for the 'for centuries' and 'in today's world' shape: a timeless statement about the category.
4. Sort the marked pages by traffic and by commercial intent, highest first.
5. Rewrite the top pages by promoting the most specific sentence already in the first three paragraphs.
6. Weight the effort toward pages aimed at experienced buyers, since the damage is largest there.
7. Add the question to your editorial checklist so new drafts do not reintroduce the pattern.
8. Re-run the audit quarterly, or after any batch of outsourced writing lands.

**Tools:** Screaming Frog

**Pitfall:** Running this audit alphabetically or by publish date wastes the effort. The pages where a school-essay opener costs real money are the high-intent ones read by experienced buyers, and those are a small subset.

**Apply at Pabau:** David can crawl pabau.com, pull the first 200 characters of every blog and template page, and flag openers that state the obvious about aesthetics or practice management. Template pages aimed at practice owners get fixed first.

**Apply anywhere:** Crawl your site, pull the first 200 characters of every article, and flag any opener that could begin a school essay on the topic. Fix the highest-intent pages first, since experienced buyers are where a beginner-level opener costs the most.

### 16. Audit the introduction for copy written below the reader's level  `144.8`
*useful · concrete actions · source 144*

Grow and Convert treat the introduction as a conversion problem, not a style problem, and give a diagnostic for it. Their example is an article aimed at sales managers that sells a CRM, opening by explaining that CRMs are important for tracking sales data. To an experienced sales manager that is an immediate turn off, because the article is written below the knowledge level of its target audience and the introduction is what gives that away. The consequences they name are concrete: you show the reader you are not on their level, you fail to entice them to keep reading, and you lose a chunk of them, cutting the conversion rate right at the gate. They say this matters most in B2B, where visitors are often advanced in the topic area, and point to their founder Devesh's separate piece on writing better introductions.

> "written below the knowledge level of the target audience"

**Evidence:** Grow and Convert's worked counter-example: a CRM article for sales managers that opens by explaining CRMs help track sales data, which they describe as an immediate turn off for that reader.

**How to do it**

1. Take the first two paragraphs of a post and read them as the most experienced person in your target audience.
2. Flag any sentence that defines the category or explains why the category matters, since that audience already knows.
3. Flag any statistic used to establish that the problem exists rather than to say something specific about it.
4. Rewrite the opening so it starts at the specific difficulty the reader is having right now, in the words they would use.
5. Include one detail early that only someone who has done the job would know, as proof you are on their level.
6. Check the rest of the article for the same failure, since an intro written down usually signals a body written down too.
7. Compare bounce rate and scroll depth before and after on the rewritten posts.

**Pitfall:** Rewriting the intro but leaving beginner-level body sections in place. The reader clears the opening, hits a section defining terms they use daily, and leaves anyway.

**Apply at Pabau:** Pabau writes for practice owners and managers who run clinics daily. David should reject any Pabau intro that opens by explaining why scheduling or client records matter, and replace it with the specific operational problem the article solves.

**Apply anywhere:** If you write for practitioners who do the job daily, reject any intro that opens by explaining why the category matters. Replace it with the specific operational problem the article solves.

### 17. Back every claim with detail, and admit when you lack the expertise  `128.11`
*useful · best practices · source 128*

The Detail Principle is the third of Grow and Convert's three content strategies, and they describe it as what backs up the other two. In practice it means writing pieces with as much detail as possible to support the claims they make, rather than asserting them. Their honest admission is the operationally useful part: they say this is not possible without interviewing subject-matter experts for pieces where they themselves lack the expertise, and that the majority of their pieces fall into that category. So the detail principle is not a writing instruction, it is a sourcing constraint. If nobody on the team can supply the specifics behind a claim, the claim either gets an interview behind it or it comes out of the article. That is a more usable rule than "add depth", because it names what to do when the depth is not available internally.

> "writing pieces with as much detail to back up the claims"

**Evidence:** Grow and Convert say the Detail Principle is impossible without subject-matter expert interviews and that the majority of their pieces need one.

**How to do it**

1. List every load-bearing claim in the outline before drafting.
2. For each claim, name the source of the specifics: internal expertise, an interview, or published data.
3. Mark any claim where nobody internally can supply the detail and treat that as an interview requirement, not a writing problem.
4. Assume most pieces fall into that category rather than the exception.
5. Replace assertions with the mechanism, the numbers and the case that support them.
6. Cut any claim you cannot back after the interview instead of hedging it.
7. Review the draft for sentences that state a position with no supporting specifics and either source them or delete them.

**Pitfall:** Treating detail as a length target. Padding raises word count without backing a single claim, and the piece still reads as assertion, which is exactly what the ranking articles already do.

**Apply at Pabau:** Pabau's fact-check pass should list the load-bearing claims in each article and flag any that no internal expert can back, sending those for a practitioner interview or removing them.

**Apply anywhere:** Treat detail as a sourcing constraint rather than a writing instruction. List the load-bearing claims before drafting, name who can supply the specifics behind each, and either book an interview for the ones nobody internally can back or cut them.

### 18. Back-button hijacking and unchecked AI pages both get penalized  `52.4`
*useful · content insights · source 52*

Edward cites Google's own recent public statement penalizing "back button hijacking" — sites that used code to trap visitors so that clicking the browser's back button kept them on the same site instead of returning to search results — as a concrete, real example of the if-it-seems-clearly-spammy-avoid-it principle, noting the enforcement is "better late than never" since the tactic was obviously manipulative long before Google acted on it. He pairs this with a second named pattern, "Mount AI": companies that publish large volumes of AI-generated pages without checking them typically see a short traffic spike, followed by getting hit. Both examples are offered as evidence that tactics which look obviously manipulative to a human observer tend to eventually draw explicit enforcement, even when there's a lag between the tactic emerging and Google acting on it.

> "penalizing back button hijacking. Now, this is better late than never"

**Evidence:** A specific named enforcement action, Google penalizing back-button hijacking, described as "better late than never," and a named pattern, "Mount AI," describing unchecked mass AI-content publishers getting a short spike up, and then they get hit.

**Apply at Pabau:** When auditing Pabau's site or any third-party tools/plugins under consideration, explicitly check for any UX pattern resembling back-button trapping, such as history manipulation, forced interstitials, or JS redirects on back-navigation, and treat any unreviewed bulk AI-content publishing plan as sitting in the same enforcement-risk category as "Mount AI," regardless of any short-term traffic gain it shows.

**Apply anywhere:** When auditing your site or any third-party tools/plugins under consideration, explicitly check for any UX pattern resembling back-button trapping, such as history manipulation, forced interstitials, or JS redirects on back-navigation, and treat any unreviewed bulk AI-content publishing plan as sitting in the same enforcement-risk category as "Mount AI," regardless of any short-term traffic gain it shows.

### 19. Big impressive numbers are usually the least important value prop  `92.7`
*useful · content insights · source 92*

Grow and Convert single out language counts as the classic example of a wrong value prop that looks right. Both the number-one ranking article and their own client article mention how many languages a plugin supports, and one led with it as the very first thing said about the product. But most companies only translate their site into a handful of languages, and everyone assumes any translation plugin covers the ones they need. Their evidence is behavioral: look at the language switcher on any site you visit and it lists three to five options, the usual suspects, English, Spanish, French, German, Chinese. Even the United Nations homepage lists only six. So the hundred-language figure is a value prop but never the opening one. They explain why writers keep reaching for it: the number is easy to find, bigger seems better, and to someone new to the space it looks like it matters. Their own article demotes it correctly, mentioning over 100 languages as a side note inside a bullet about automation.

> "Even the United Nations website only has 6 languages listed."

**Evidence:** Grow and Convert's own #2 ranking article mentions over 100 languages only as a side note inside an automation bullet, while the #1 article opened a product description with the language count.

**How to do it**

1. List every numeric claim in the draft: counts of integrations, languages, templates, users, features.
2. For each, ask how many the typical buyer actually uses, and find a real-world check like a public site's language switcher.
3. Demote any number the buyer does not consume in full out of the opening sentence.
4. Keep the number, but attach it as a sub-clause to the value prop that does matter.
5. Replace the opening sentence with the feature that removes the buyer's biggest pain.
6. Ask a customer-facing colleague whether any buyer has ever chosen on that number; if not, it never leads.

**Pitfall:** Vendor marketing pages lead with these numbers, so a writer working from the website inherits the wrong emphasis directly. The signal you have hit it is that your first sentence about a product is a figure rather than a problem.

**Apply at Pabau:** Pabau articles should not open a product description with integration counts or feature totals. Lead with the workflow the practice stops doing manually, and keep the number as a supporting clause.

**Apply anywhere:** Do not open a product description with integration counts or feature totals. Lead with the workflow the buyer stops doing manually and keep the number as a supporting clause.

### 20. Blame topic breadth, not competition, when content stops working  `98.9`
*useful · content insights · source 98*

Hyam's framing of the whole problem, and it contradicts the common complaint. He reports hearing people say content marketing has become too hard and that it is impossible to compete with the other blogs writing about the same thing. His counter is that content marketing has not become harder, readers have just become smarter, having been tricked by clickbait headlines for five years. The challenge, as he defines it, is not what content to create but how to make it stand out from the other blogs covering the same topic. He explicitly positions this against the two dominant answers of the era: Rand Fishkin's 10x content and Neil Patel's long-form content. Grow and Convert's answer is neither length nor a quality multiplier but specificity of topic selection.

> "Content marketing hasn't become harder. Readers have just become smarter."

**Evidence:** Positioned explicitly against Rand Fishkin's 10x content and Neil Patel's long-form advice as competing answers to the same problem.

**Apply at Pabau:** When a Pabau article underperforms, check topic breadth before adding word count or upgrading design. A narrower topic beats a longer version of the same broad one.

**Apply anywhere:** When content stops working, the usual fixes of more length or more polish treat the symptom. Check whether the topic was too broad to be distinctive in the first place.

### 21. Bridge an adjacent-audience keyword through a complementary feature  `111.9`
*useful · concrete actions · source 111*

Grow and Convert describe the loosest keyword they accepted for Leadfeeder, a tool showing which companies visit your website. The term was 'how to find decision makers in a company', which is not about visitor identification at all. They accepted it because it indicates an audience very likely to be in B2B sales, which is the right audience. Their handling was to give a thorough, genuinely useful explanation of finding decision makers using LinkedIn Sales Navigator, then find ways to incorporate how Leadfeeder shows which companies are visiting your site, framed as a complementary feature to the job they were Googling. The rule that emerges: when the keyword does not match the product, it must at least match the buyer, and the product enters as the next step in the same workflow rather than as the answer to the query.

> "which is a complementary feature to what they're Googling"

**Evidence:** Leadfeeder's 'how to find decision makers in a company' post explained LinkedIn Sales Navigator in full and positioned Leadfeeder as complementary.

**How to do it**

1. Check that the keyword's searcher is your buyer persona even though the topic is not your product.
2. Reject the keyword if the audience is wrong, regardless of volume; audience fit is the only thing carrying this page.
3. Answer the query properly first, naming the specific third-party tools the reader would actually use.
4. Identify the step that comes immediately before or after this task in the reader's real workflow.
5. Introduce your product at that step, described as complementary rather than as the answer.
6. Keep the product section short and clearly subordinate to the main answer.
7. Measure conversion separately from bottom-funnel pages, since the expected rate is much lower.

**Tools:** LinkedIn Sales Navigator

**Pitfall:** Forcing the product in as the answer to a query it does not answer. Readers see the switch, bounce, and the page loses the ranking that gave it any value.

**Apply at Pabau:** Pabau can accept adjacent aesthetic-practice keywords like hiring or insurance topics only when the reader is a practice owner, and must answer them properly before introducing Pabau as the adjacent step in the same workflow.

**Apply anywhere:** An off-topic keyword is acceptable when the audience is exactly your buyer. Answer it fully with the tools they would really use, then introduce your product as the complementary next step in the workflow, not as the answer.

### 22. Budget for top-funnel to supply roughly a fifth of blog conversions  `132.8`
*useful · content insights · source 132*

Grow and Convert push back on a misreading of their own advice. Readers took their bottom-funnel-first posts to mean they never produce top-funnel content and that it generates no conversions. The Geekbot numbers say otherwise: top-funnel content produced 397 of the 1,745 total conversions, which is 22.76 percent. They call that number nothing to sneeze at and frame the whole thing as a prioritization argument rather than an exclusion. Missing 397 conversions is a big deal, just less of one than missing 1,348. The planning implication is a rough expectation to hold once both tiers exist: something close to three quarters of blog conversions from buying-intent pages and something close to a fifth to a quarter from the top-funnel tier. A blog wildly outside that split at maturity is likely mis-weighted.

> "the number of TOF conversions is nothing to sneeze at"

**Evidence:** Geekbot: 1,348 bottom-funnel conversions (77.24%) and 397 top-funnel conversions (22.76%) out of 1,745 total across 64 articles.

**Tools:** Google Analytics

**Pitfall:** The split only holds once the bottom-funnel tier is complete. Reading it as a target to hit from day one leads teams to commission top-funnel content early, which is the exact sequencing error the case study argues against.

**Apply at Pabau:** Pabau should not treat top-funnel guides as zero-value, but should expect them to supply roughly a fifth of blog-attributed demo requests once the bottom-funnel set is complete. If guides are supplying most of the demos today, that means the bottom-funnel pages are underbuilt rather than that guides are working well.

**Apply anywhere:** Once both tiers exist, expect roughly three quarters of blog conversions from buying-intent pages and around a fifth to a quarter from informational ones. If informational content is supplying most of your conversions, your buying-intent pages are underbuilt rather than your guides overperforming.

### 23. Budget four months to see a re-optimization program move conversions  `116.14`
*useful · general insights · source 116*

Grow and Convert give the timeframe and the hit rate for this program, which is useful for setting expectations before committing a quarter to refreshes rather than new publishing. They began re-optimizing in February 2023. Comparing the four months before against the four months after, average monthly conversions from their content went from 171 to 258. The client hit an all-time high in free trial signups, and the important framing is that conversions afterwards bottomed out at what had previously been the peak. On volume: they re-optimized 22 posts targeting 30 lost secondary keywords, and 20 of those 30 keywords improved significantly in position. So roughly two thirds of attempted recoveries worked, over about a four-month window.

> "our content has averaged 258 conversions a month"

**Evidence:** Grow and Convert: 171 average monthly conversions in the four months before re-optimization, 258 in the four months after; 22 posts re-optimized, 20 of 30 targeted secondary keywords improved significantly.

**How to do it**

1. Commit a four-month window before judging a re-optimization program.
2. Fix the baseline as average monthly conversions over the four months before you start.
3. Re-optimize in batches rather than all at once, so you can attribute movement.
4. Track each targeted secondary keyword's position weekly in a rank tracker.
5. Expect roughly two in three targeted keywords to improve; plan the workload accordingly.
6. Compare the four-month post-period average against the baseline, not month against month.
7. Judge success by the new floor rather than the new peak.

**Tools:** Ahrefs, GA4

**Pitfall:** Reading month-on-month noise as failure. Grow and Convert saw ebbs and flows after the change; the signal was that the low months matched the old all-time high, which only shows up over a four-month average.

**Apply at Pabau:** If David proposes pausing new Pabau articles to refresh existing ones, the case should be a four-month comparison of average monthly demo requests, with an expectation that about two thirds of targeted keywords move.

**Apply anywhere:** If you propose pausing new publishing to refresh existing pages, build the case as a four-month comparison of average monthly conversions, expecting about two thirds of targeted keywords to move.
