# Keyword Research — supporting (part 3 of 4)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Place the target keyword in five specific on-page spots  `52.2`
*useful · concrete actions · source 52*

The concrete on-page checklist given for making a page relevant to its target keyword is to place that keyword in five specific spots: the page title, the H1, the URL slug, the meta description (explicitly flagged as optional to use at all), and the beginning of the first sentence of body copy. This is framed as a baseline relevance signal that should be paired with actually picking keywords likely to drive conversions, customers, users, or warm leads, rather than just traffic, since relevance without a converting keyword target doesn't achieve the underlying business goal.

> "the page title, the H1, the URL slug, the meta description"

**How to do it**

1. Identify the single primary target keyword for the page you're optimizing, chosen because it plausibly drives conversions, not just traffic.
2. Place that exact keyword, or a close natural variant, in the page title tag.
3. Place the same keyword in the page's H1 heading.
4. Include the keyword in the URL slug.
5. If you choose to use a meta description at all, include the keyword there too, since the source treats meta descriptions as optional.
6. Open the page's first sentence of body content and place the keyword at or near its beginning.
7. After publishing, verify in Google Search Console that the page is being indexed for that keyword and check its position over the following weeks (inferred verification step).

**Tools:** Google Search Console

### 2. Qualify a traffic keyword by naming who in your market searches it  `115.3`
*useful · best practices · source 115*

Grow and Convert do not dismiss high-volume top-funnel keywords, but they apply a test before accepting one. For 'electrician salary' at 33,100 searches a month they name the specific person and reason: the owner or manager of an electrician business searching to decide what to pay their electricians. That is what makes some portion of the traffic plausibly their client's audience rather than job seekers. The test is to write the sentence out. If you cannot name a role in your buying market and a concrete reason that role types the query, the volume belongs to someone else, most often students, employees or hobbyists. They are explicit that even passing this test does not make the keyword a lead driver, only a defensible traffic play, and they still expect it to produce few leads.

> "some portion of these searchers would fall into our client's target audience"

**Evidence:** Grow and Convert accept 'electrician salary' at 33,100 searches a month on the basis that electrical business owners search it to set pay rates.

**How to do it**

1. For each high-volume candidate, write one sentence naming the job title that searches it and why.
2. Reject the keyword if the most likely searcher is a job seeker, student or employee rather than a buyer.
3. Check the SERP for confirmation: salary and career pages ranking mean the audience is employees, not owners.
4. Estimate what fraction of the volume is your audience, and multiply the volume by that fraction before comparing keywords.
5. Cap top-funnel terms as a minority of the calendar even when they pass, since they are a traffic play and not a lead play.
6. Tag every accepted top-funnel article in analytics so its lead contribution can be checked separately from bottom-funnel pages.
7. Drop the term from future cycles if the tagged pages show no conversions after six months.

**Pitfall:** Accepting a keyword because the audience overlaps 'in theory'. If nobody can name the role and the reason in one sentence, the traffic will arrive and bounce, and the page will look successful on pageviews for years.

**Apply at Pabau:** David should apply this to Pabau's top-funnel aesthetics topics. 'Botox training courses' is searched by aspiring injectors, not practice owners, so it fails. 'How much do medical spas make' is searched by owners, so it passes as a traffic play with tagged conversion tracking.

**Apply anywhere:** Before accepting a high-volume informational keyword, write one sentence naming which role in your buying market searches it and why. If the likely searcher is a student, employee or hobbyist, the volume is not yours. Passing the test makes it a defensible traffic play, not a lead source.

### 3. Rank category keywords by backlink counts in the top ten, not by difficulty score  `120.4`
*useful · concrete actions · source 120*

Inside their prioritization order, Grow and Convert give one concrete screen for picking which competitive category terms to attack first: look for SERPs where the top-ranking results have fewer backlinks. They treat that as the practical read on keyword difficulty, and say those terms give quicker ranking opportunities. The reasoning is that a difficulty score is a summary of the same underlying data, but the score compresses away the case you actually want, which is a competitive-looking term whose current top ten happens to be weakly linked. Checking the actual referring domain counts on the ranking URLs surfaces those. They apply the same screen when ordering competitor and pain point keywords, not only category ones.

> "Look for SERPs where the top results have fewer backlinks"

**Evidence:** Grow and Convert name low backlink counts in the top results as the marker of keywords with lower difficulty and quicker ranking opportunities.

**How to do it**

1. Take the shortlist of buying-intent category keywords you already believe are worth a page.
2. Search each one and export the top ten URLs.
3. Run those URLs through Ahrefs Batch Analysis or Site Explorer and record referring domains per URL, not per domain.
4. Flag any SERP where most of the top ten sit under the referring domain count your own comparable pages already carry.
5. Move those flagged terms to the front of the queue regardless of their difficulty score.
6. Push terms whose top ten are all heavily linked into the long-term bucket that gets link budget.
7. Repeat the screen for the competitor comparison and pain point lists before scheduling them.
8. Re-run the check every six months, since weakly linked SERPs get discovered by rivals too.

**Tools:** Ahrefs, Moz, Semrush

**Pitfall:** Reading referring domains at the domain level instead of the page level. A weak page on a strong site still looks unbeatable in domain metrics, and you skip a term you could have taken.

**Apply at Pabau:** When Pabau selects which comparison or category page to build next, the deciding number should be referring domains on the ranking URLs, not Ahrefs keyword difficulty. Aesthetic-software SERPs often have weakly linked directory pages in the top ten.

**Apply anywhere:** When choosing which competitive term to attack next, decide on referring domains counted per ranking URL rather than on a keyword difficulty score. Weakly linked top tens are the openings a difficulty score averages away.

### 4. Rank for the single feature buyers reduce your platform to  `109.5`
*useful · concrete actions · source 109*

The mirror image of overestimation is underestimation. Grow and Convert's client StrataPT sells a complete platform for physical therapy practices, but its dominant function is billing, because insurance reimbursement is the hardest part of running a PT clinic. Calling StrataPT 'billing software' is technically inaccurate, since the product does much more. The author targets it anyway, on two grounds. First, people searching that term are strong prospects because billing and collection rate is the main benefit they will buy on. Second, standalone billing software without the surrounding platform does not deliver the same collection results anyway, so the argument for the full product is honest and easy to make on the page. The keyword is wrong about the product and right about the buyer.

> "calling their product 'billing software' is technically inaccurate"

**Evidence:** StrataPT, a full physical therapy platform, ranked and converted on billing software terms because reimbursement is the buyer's dominant pain.

**How to do it**

1. Ask sales which single feature closes the most deals, regardless of how you position the platform.
2. Search that feature as a standalone software category and pull volume and variants.
3. Confirm the searcher's outcome, such as collection rate, is one your product improves more than the point tool does.
4. Build a page targeting the narrow feature term with your product named as the answer.
5. Devote a section to why the standalone point tool underperforms on the same outcome.
6. Use a real number, such as a collection-rate or reimbursement improvement, rather than a feature list.
7. Link from that page to the full platform page so the searcher can widen their view.
8. Track conversions from the narrow page separately, because it will convert differently from category pages.

**Pitfall:** Positioning teams block this because they fear being pigeonholed as a point tool. The page must lead with the narrow term and widen inside the body, not the reverse, or it stops matching intent.

**Apply at Pabau:** Pabau is a full practice management platform, but many aesthetic clinics buy on one thing, often online booking or client records. Pabau should publish pages targeting those narrow software terms and argue inside them that a standalone booking tool leaves the rest of the workflow broken.

**Apply anywhere:** Identify the single feature buyers reduce your platform to, and rank for it as a standalone software category. Inside the page, show why buying that feature alone underperforms on the outcome the searcher actually wants.

### 5. Read a workaround query for the audience it does not name  `109.10`
*useful · content insights · source 109*

Grow and Convert's Circuit case shows a second reason workaround keywords convert. They targeted 'how to plan the shortest route for multiple destinations in google maps' for a delivery route-planning product. The plan was to walk the reader through the Google Maps process so they would feel how painful it is, including the ten-stop maximum. The unexpected value was audience composition. A significant number of people searching that query are making deliveries. They never say so in the search term, but delivery is one of the main reasons anyone needs a shortest route across a list of stops. That is Circuit's core audience, arriving through a query that names neither the product nor the industry. The post has generated thousands of free trial signups.

> "a significant number of people searching for this are doing so"

**Evidence:** Circuit's Google Maps multi-stop routing post has generated thousands of free trial signups, driven partly by delivery drivers who never mention delivery in the query.

**Tools:** Google Maps

**Pitfall:** The inference can be wrong. If the hidden audience you assume is not actually there, you get traffic with no signups, so check the assumption against who converts on the page in the first two months.

**Apply at Pabau:** Before dismissing a generic query, David should ask who realistically needs that task done. Searches about managing appointment reminders or client no-shows are often run by clinic owners even when no clinic word appears in the query.

**Apply anywhere:** Ask who realistically performs the task behind a generic query, not just what the words say. A workaround search that names no industry can still be dominated by one occupation, and that occupation may be your core buyer.

### 6. Read the ranking page types for intent signatures before committing a keyword  `113.6`
*useful · best practices · source 113*

Grow and Convert give a page-type signature test that runs after volume validation. Look at what is actually ranking in the top 10. Product pages, comparison posts and buying guides confirm high intent. Encyclopedia entries, scholarly articles and tips-and-trends educational posts mean the keyword lacks buying intent, even if the volume looks good. Their worked pair: mental health journaling returns educational articles and research papers, while mental health journaling app returns app lists and product comparisons. Same topic, completely different intent. This adds a named list of negative signatures to the general advice about checking what ranks: Wikipedia-style entries, academic papers and trends pieces are the specific things that disqualify a term.

> "encyclopedia entries, scholarly articles"

**Evidence:** Grow and Convert's pair: mental health journaling returns educational articles and research papers; mental health journaling app returns app lists and product comparisons.

**How to do it**

1. Search the candidate keyword in an incognito window and list the page type of each of the top 10 results.
2. Count results that are product pages, comparison posts or buying guides as intent-positive.
3. Count encyclopedia entries, scholarly or research articles, and tips-and-trends educational posts as intent-negative.
4. Drop the keyword if the intent-negative types dominate, regardless of what the volume or the tool's intent label says.
5. Where a topic fails, test the same topic with a product-shaped modifier appended, such as app, software, tool or service, and re-run the check.
6. Record the page-type mix in the brief so the writer matches the format that is already ranking.

**Tools:** Ahrefs, Semrush

**Pitfall:** Trusting the intent label from Ahrefs or Semrush instead of the SERP. The tools label by phrasing, so a high-volume educational term can carry a commercial tag and waste a full article.

**Apply at Pabau:** Before David briefs any Pabau article, the SERP page types go in the brief. A term like skin analysis returning research papers gets rejected; skin analysis software returning product roundups gets built.

**Apply anywhere:** Before committing a keyword, list the page type of each top 10 result. Product pages, comparisons and buying guides confirm intent. Encyclopedia entries, research papers and trends posts disqualify it.

### 7. Read tool volume as stale sampled data, for four named reasons  `95.10`
*useful · content insights · source 95*

Matt Goolding gives four reasons why a page ranking for a mini-volume keyword almost always gets more monthly pageviews than the reported search volume. First, the data in SEO tools is rarely current, and search trends move fast: Covid-19 searches exploded in spring 2020 but tools did not reflect it for months. Second, volumes differ between tools and shift as databases update, so no single figure is authoritative, which is why he says start from pain points and check volume afterwards. Third, keyword variations add up: a 20-volume target with 10 variations each worth 5 to 10 searches produces a much healthier total, plus long-tail phrasings absent from any tool's database. Fourth, mini-volume is not permanent in a growing niche. He notes tool vendors say the same thing themselves.

> "The data we get from SEO tools is rarely up-to-date"

**Evidence:** Covid-19 search volumes exploded in spring and summer 2020 but did not appear in SEO tool databases for several months afterwards.

**Tools:** Ahrefs, Moz

**Pitfall:** Treating a zero or a 10 as evidence of no demand. It is an absence of data, and for newly emerging or highly specific phrasings the absence is expected.

**Apply at Pabau:** Pabau should order keyword work by the pain points practices actually raise, then look up volume as a tiebreaker rather than a gate. Aesthetics terms move with treatment trends faster than Ahrefs updates.

**Apply anywhere:** Start keyword selection from customer pain points and check volume afterwards as a tiebreaker. Tool volume is stale, sampled and inconsistent between vendors, so a zero reading means no data rather than no demand.

### 8. Replicate the keyword expansion across every product line, not just one  `112.17`
*useful · concrete actions · source 112*

Grow and Convert make the scaling step explicit, because it is where the volume comes from. Working through Truwild's hydration product alone, product-attribute terms plus competitor terms gave them 10 or more bottom-of-funnel opportunities. They then say they would replicate the same strategy, both product and competitor keywords, for each of the other three lines: pre-workout, superfood and immune support. Doing that puts the brand in reach of 50 to 100 or more revenue-generating keywords it would otherwise have left completely untapped, and the pain-point and use-case loops add roughly the same again. This is the answer to the earlier arithmetic problem: a low order value needs many conversions, and the way to get there is to run one repeatable expansion process over every product rather than a deep effort on the flagship.

> "rank for 50-100+ revenue generating keywords"

**Evidence:** Grow and Convert count 10+ opportunities from one Truwild product and project 50-100+ across four lines, plus another 50-100+ from pain points and use cases.

**How to do it**

1. List every product line you sell, not just the best seller.
2. For each, run the product-page attribute expansion and record the terms.
3. For each, run the competitor-alternative expansion against its own rival set, which differs per line.
4. For each, run the pain-point inversion and the use-case autocomplete loop.
5. Collect everything into one sheet with columns for line, keyword type, volume and current ranking.
6. Sort by keyword type first and volume second, so bottom-of-funnel terms stay ahead of use cases.
7. Track coverage per product line so no line is left with zero dedicated pages.
8. Re-run the whole expansion whenever a new product line launches.

**Tools:** Clearscope, Ahrefs

**Pitfall:** Doing the deep expansion only on the flagship product leaves the rest of the catalog dependent on category head terms it will never win, and the total keyword count stays too small to reach breakeven.

**Apply at Pabau:** Pabau's equivalent lines are the feature families and the audience verticals. David should run the same four expansions per family rather than concentrating on the main product term, and keep a coverage sheet so no feature family sits with no dedicated page.

**Apply anywhere:** Run the same expansion process, product attributes, competitor alternatives, pain points and use cases, over every product line rather than only the flagship. One brand with four lines can reach 50 to 100 purchase-intent keywords that way, which is what a low order value needs.

### 9. Reserve exactly 20% of your keyword list for zero-volume bets  `11.5`
*useful · concrete actions · source 11*

Gotch applies an explicit 80/20 split to keyword selection: 80% of the topics in any given cluster or sprint should have some form of proven demand from the four signal types (volume, GSC impressions, Reddit/Quora engagement, or first-party data), while the remaining 20% are deliberately allocated to experimental topics with zero measurable volume, treated as calculated gambles that might not pay off but are worth the risk allocation. This gives a concrete, numeric governance rule for how much risk to take in a keyword set rather than either avoiding all zero-volume topics or chasing too many speculative ones.

> "you can deploy the 80/20 rule when it comes to this"

**How to do it**

1. Once your candidate keyword list for a cluster is filtered down, tag each keyword as either 'proven demand' (has volume, GSC impressions, Reddit/Quora activity, or first-party evidence) or 'experimental' (none of the above).
2. Calculate what percentage of the current list is tagged experimental (inferred: use a COUNTIF formula in the tracking sheet).
3. If experimental keywords exceed 20% of the list, cut the weakest-rationale experimental entries until the list is back to an 80/20 split.
4. If experimental keywords are under 20%, deliberately add a small number of no-volume but strategically interesting topics to use the full risk allowance.
5. Track performance of the experimental 20% separately after publishing (inferred: tag these URLs in GSC/Analytics) to learn which types of zero-volume bets pay off for your niche over time.

**Tools:** Google Search Console

### 10. Reverse-engineer competitor paid keywords into your own organic topics  `114.6`
*useful · concrete actions · source 114*

Grow and Convert use iSpionage to enter a competitor's domain and see both the paid keywords they bid on and the organic keywords they rank for. The logic is that a competitor spending money on a term has proof it converts, so you can back into their converting keywords without any of your own data. The author worked the example of Gong, a sales pipeline tracking product. If he sold a competing pipeline or sales reporting tool, he would read Gong's bid list and pull out only the terms that tie to a feature his own product has. Two he names are 'pipeline report template' and 'sales report example', because pipeline reporting and sales reporting would be features in the competing tool. The article for each then shows how much easier the report is to build inside your product. The filter is explicit: only take the keyword if it makes sense for what you actually sell.

> "see what paid keywords they're bidding on"

**Evidence:** Worked example on Gong: 'pipeline report template' and 'sales report example' picked out as feature-tied bid terms a competing product could write against.

**How to do it**

1. Enter each direct competitor's domain into iSpionage and export both the paid and organic keyword lists.
2. Drop every brand term and every term with no product tie-in.
3. List your own product's features from the homepage and pricing page.
4. Keep only competitor bid terms that map to one of your features.
5. Favor bottom-of-funnel formats in that list: templates, examples, calculators, comparisons.
6. Check the SERP for each survivor to confirm the ranking pages are commercial rather than editorial.
7. Write one page per term that walks through the task and shows it done inside your product.
8. Repeat across three competitors and prioritize any term two or more of them bid on.

**Tools:** iSpionage

**Pitfall:** Copying a competitor's whole bid list imports terms tied to features you do not have, so the article cannot honestly show your product doing the job. The signal is a post that ranks and then has no natural product mention anywhere in it.

**Apply at Pabau:** Pabau should run competitor domains through a paid-keyword tool and keep only terms tied to real Pabau capabilities: consent form templates, treatment record examples, appointment reminder setup. Each becomes a template page showing the task done in Pabau.

**Apply anywhere:** Pull a competitor's paid keyword list, keep only the terms that map to a feature you actually ship, and prefer template and example formats. Write each page as a walkthrough of that task inside your product.

### 11. Route competitor and jobs-to-be-done keywords to blog pages deliberately  `145.3`
*useful · concrete actions · source 145*

Beyond category and product-variant terms, Grow and Convert name two more high-intent keyword frameworks that drive conversions: competitor and alternatives keywords, and jobs-to-be-done keywords. Their operational point is about hosting. Neither framework can be served by a homepage or a product page, because a competitor comparison needs its own page per competitor and a job query needs copy about the job rather than about the product. So both belong on the blog. They treat this as a reason the blog is a selling asset rather than an awareness channel, and they say most companies never build these pages at all despite the conversion value.

> "two other high intent keyword frameworks"

**Evidence:** Grow and Convert say both frameworks drive significant conversions but are not reachable with home and product or service pages.

**How to do it**

1. List your direct competitors and generate the alternatives, versus and comparison keywords for each.
2. List the jobs your buyers hire the product to finish, phrased the way they would search them, not the way your product markets them.
3. Check each keyword's SERP and confirm it ranks article-type pages rather than only vendor homepages.
4. Assign one dedicated page per competitor keyword and one per job keyword; never bundle several competitors onto one page.
5. Publish them on the blog if the product-page template cannot carry comparison tables or long job explanations.
6. Name and sell the product inside each page, since that is what the query is asking for.
7. Add contextual links from each job page into the relevant product or category page.
8. Report conversions per page and cut only the pages that fail after they have ranked, not before.

**Pitfall:** Teams fold all competitors into one comparison post to save effort. That page tends to rank for none of the individual competitor terms, which are the ones with the intent.

**Apply at Pabau:** Pabau needs a dedicated page per named competitor and per practice job, such as recall messaging, consent forms or no-show reduction. David should check the existing template and blog inventory for one-page-per-competitor coverage.

**Apply anywhere:** Competitor and jobs-to-be-done keywords each need their own page, and neither fits a homepage or product page. Build one page per competitor and one per job, on the blog if the templates cannot carry them.

### 12. Run a category keyword inventory because most brands have never done one  `142.9`
*useful · concrete actions · source 142*

Grow and Convert say many of the brands they talk to, whose analytics they have seen, have never systematically identified and targeted their category keywords, and they call that a waste of marketing potential. Their prescription is a two-part brainstorm: first the obvious category keywords and every variation people might Google to find products or services exactly like yours, then the layers of specificity that could be added to those terms and that align with your product's strengths. The supporting data from their client work is that when you cover the variations you should expect most of them to convert at 3% or higher to free trial starts. For one video marketing client they ranked on page one across the app, software and service variations of a sub-category term, converting at 5.73%, 3.31% and 3.00%. They caution that if you only sell an app or only a service, some variations will not fit your offering and will convert worse.

> "you should expect most variations to convert well"

**Evidence:** Video marketing client: app, software and service variations of one sub-category term converted at 5.73%, 3.31% and 3.00% respectively.

**How to do it**

1. Write down what you sell in the plainest words a buyer would use, without internal jargon.
2. Expand each into the product-noun variants: software, tool, platform, app, system, service.
3. Add every synonym for the category that competitors and review sites use.
4. Add the specificity layers that match a real product strength: vertical, size, cost, feature.
5. Check each candidate has a SERP dominated by list posts before committing.
6. Drop variants that describe a delivery model you do not offer, such as service if you only sell software.
7. Put the full inventory in one sheet and mark which already have a dedicated page.
8. Commission a dedicated post for each uncovered term and hold it to a 3% conversion floor.

**Pitfall:** Reading the video client's numbers as proof that app keywords beat software keywords. Grow and Convert say explicitly that is not the takeaway; it is one post that happened to convert best.

**Apply at Pabau:** Pabau should keep one master sheet of every category term for practice management, clinic software, salon and medspa software and their noun variants, with a column for the page covering each. Gaps become the next briefs.

**Apply anywhere:** Keep one master sheet of every category term and noun variant in your space, with a column naming the page that covers each. The gaps become your next briefs.

### 13. Run five extra ideation channels once the three categories are mapped  `120.12`
*useful · concrete actions · source 120*

After the category, comparison and pain point lists are built, Grow and Convert name five further sources for keyword and content ideas. Interview the departments with the deepest customer knowledge: sales, customer success and the executive team. Use tools such as email auto-responders to ask customers directly about their biggest challenges. Join or create online communities where customers ask questions and discuss problems. Examine the Google Ads account for keywords already converting on paid, since those can be pursued organically. And plug existing keywords into Google to harvest Suggested Search, People Also Ask and People Also Search For. The point of listing all five is coverage: each channel surfaces phrasing the others miss, and the paid account in particular supplies terms with proven conversion rather than estimated intent.

> "Examine your Google Ads account for high-converting keywords"

**Evidence:** Grow and Convert list five ideation channels alongside their keyword process, including Google Ads high-converting keywords as an organic source.

**How to do it**

1. Book 30 minutes each with sales, customer success and a founder, and ask what customers say their problem is.
2. Add a single question to the welcome email auto-responder asking the subscriber's biggest challenge.
3. Join the two or three communities where your customers already discuss the problem and log recurring questions.
4. Open the Google Ads search terms report, filter to converting queries, and export them.
5. Cross out paid queries you already rank for and keep the rest as organic targets.
6. Paste your best terms into Google and copy the Suggested Search, People Also Ask and People Also Search For entries.
7. Merge all five sources into the master list and tag each row with its origin.
8. Score every new row for buying intent before it enters the build queue.

**Tools:** Google Ads, Google

**Pitfall:** Treating these as replacements for the three buying-intent categories. They generate volume of ideas, and without an intent filter the list fills with informational questions that convert poorly.

**Apply at Pabau:** Pabau should mine the Google Ads search terms report for converting queries and add a biggest-challenge question to the newsletter welcome email, then feed both into the blog queue.

**Apply anywhere:** Once the category, comparison and pain point lists exist, add ideas from staff interviews, a biggest-challenge email question, customer communities, converting Google Ads queries, and Google's Suggested Search, People Also Ask and People Also Search For. Tag each idea's source and score it for buying intent.

### 14. Run three content frameworks in parallel: competitors, use cases, pain points  `139.15`
*useful · concrete actions · source 139*

Brandon organized the whole Keeper Tax strategy into three named buckets held in one spreadsheet: competitor keywords, use case keywords, and pain-related training keywords. Competitor terms were 'alternatives to QuickBooks self-employed', 'expensify alternatives' and 'QuickBooks self-employed alternative', shipped as a 15-item Expensify alternatives roundup, a best QuickBooks self-employed alternatives page and a one-to-one Keeper Tax versus QuickBooks comparison. Use case terms described what the product does in the searcher's words: 'app to track receipts for taxes', 'best app to track receipts', 'Keeper Tax review'. Pain terms came from the interviews: 'how much should I set aside for 1099 taxes', 'what can I write off on my taxes 1099', 'deductions for independent contractors', 'tax write offs for self-employed'. His argument for competitor terms is that most companies never systematically target them, so ranking is easier than the general category term.

> "The content strategy that I developed for them consisted of 3 main content frameworks"

**Evidence:** Keeper Tax published a top-15 Expensify alternatives page, a best QuickBooks Self-Employed alternatives page and a one-to-one comparison as part of a program reaching top 10 for 996 keywords.

**How to do it**

1. Create one spreadsheet with a tab or column group per framework: competitors, use cases, pain points.
2. Fill competitors with '[rival] alternatives', '[rival] alternative' and 'us vs [rival]' for every named competitor.
3. Ship three page types per competitor set: a multi-item alternatives roundup, a best-of page, and a one-to-one comparison.
4. Fill use cases with the plain-language description of what the product does, plus your own brand review term.
5. Fill pain points with the questions customers asked in interviews, verbatim.
6. Check volume and difficulty on each row, then order by conversion intent within each framework.
7. Publish across all three frameworks rather than finishing one before starting the next.
8. Track signups per framework after 90 days and reweight the backlog toward the best performer.

**Tools:** Ahrefs, Clearscope

**Pitfall:** Competitor terms look small and get skipped for the category head term, which every rival already fights over. The comparison pages are the easiest ranks on the list precisely because nobody systematically builds them.

**Apply at Pabau:** Pabau should hold one sheet with the same three buckets: alternatives and versus pages for every named practice-management rival, use-case pages phrased as practices describe the job, and pain-point articles taken from support conversations.

**Apply anywhere:** Run one spreadsheet with three keyword frameworks in parallel - competitor alternatives, plain-language use cases, and interview-sourced pain points - and publish across all three rather than sequentially.

### 15. Scan the top ten titles to decide one post or two for similar keywords  `107.6`
*useful · concrete actions · source 107*

Grow and Convert give a cheap test for the common problem of two keywords that look nearly identical. The answer depends on how closely related the two SERPs are, and they stress you only need to scan the titles of the top ten results, not read the articles. If the results are nearly identical for both keywords, one post can target both. If the SERPs are considerably different, you need separate posts. If there is partial overlap, which they quantify as three to five of the first-page results shared, you make your best guess and test it. This is a lighter procedure than a formal cannibalization audit and is meant to be run at the planning stage, before a brief is written, rather than after two competing posts already exist.

> "you can simply scan the titles of the top ten results"

**Evidence:** Grow and Convert put the ambiguous band at three to five shared first-page results.

**How to do it**

1. Search both keywords in an incognito window and copy the top ten titles for each into a sheet.
2. Count how many URLs appear in both top tens.
3. If nearly all overlap, write one post and target both keywords in it.
4. If three to five overlap, pick the higher-intent keyword, write one post, and check after eight weeks whether the second keyword also ranks.
5. If the overlap is low or the page types differ, commission two separate posts.
6. Record the decision and the overlap count so a later refresh does not relitigate it.

**Pitfall:** Deciding on keyword similarity by wording rather than by SERP produces two posts competing for the same results, or one post trying to serve two genuinely different intents and serving neither.

**Apply at Pabau:** Pabau has many near-duplicate query pairs, such as a treatment name plus software versus the same treatment plus booking system. David should run the top-ten title scan before commissioning either, and log the overlap count in the brief.

**Apply anywhere:** Before writing, scan the top ten titles for both similar keywords and count the shared URLs. Near-total overlap means one post, low overlap means two, and three to five shared results means pick one and test.

### 16. Score keywords with a weighted formula across 8 automated inputs  `11.16`
*useful · ai workflows · source 11*

Gotch's keyword-prioritization engine computes a single point score per keyword by weighting eight inputs together: search volume, keyword difficulty, CPC, current ranking position, intent (commercial vs. informational), a manually-assigned relevance score for how relevant the keyword is to what you sell, required word count to competitively rank, and the lowest domain score among ranking competitors pulled from a third-party tool such as Rankability, Semrush, or Ahrefs, plus a count of competing SERP features. Two keywords with similar raw volume can score radically differently — his worked example has one keyword score 39 as a strong target while a similar one is excluded entirely once position, domain-score gap, word-count requirement, and SERP-feature count are all factored in. He notes you don't need his exact formula and can build a simpler manual version, or have ChatGPT/Claude generate the regex or spreadsheet formulas that auto-populate each component score.

> "you can only pull this from a tool like Rankability"

**How to do it**

1. In your keyword tracking sheet, add a component-score column for each of: Volume, Keyword Difficulty, CPC, Position, Intent, Relevance (a manual 1-5 or 1-10 rating of fit to what you sell), Target Word Count, and Lowest Competitor Domain Score.
2. Pull Lowest Domain Score for the top-ranking competitor pages from a third-party SEO tool such as Rankability, Semrush, or Ahrefs.
3. Estimate Target Word Count needed to competitively rank by reviewing the word count of current top-ranking pages for that query (inferred: use an SEO tool's content report or manually check the top 3-5 results).
4. Assign weights to each component reflecting your own priorities, since Gotch is explicit his weighting is his own opinion, not a fixed industry standard.
5. Ask ChatGPT or Claude to generate the spreadsheet formula or regex that auto-calculates each component score from the raw inputs, if you don't want to build the formulas manually.
6. Sum the weighted component scores into one Total Score column per keyword, and sort the sheet by Total Score descending to surface the top 25-30 keywords in the cluster worth deep-diving.
7. Re-run the score whenever a component input changes, such as after checking current position or adding domain-score data, to confirm keywords are still correctly prioritized.

**Tools:** Rankability, Semrush, Ahrefs, ChatGPT, Claude, Google Sheets

**Pitfall:** Scoring keywords on volume alone without layering in position, domain-score gap, word-count cost, and SERP-feature count — Gotch's own example shows two similar-volume keywords scoring 39 versus an exclusion once the full weighted formula is applied.

### 17. Scrape Reddit with Perplexity to source ad angles and audience language  `68.26`
*useful · ai workflows · source 68*

Cody says all of his ad research is literally scraping Reddit using Perplexity, and that the volume of information you can pull out about a target audience this way is incredible. The point he attaches is about problem discovery: founders build things nobody wants because they do not know the problems people face, and AI has made that ignorance avoidable. This is the desk-research counterpart to his podcast method. The podcast gets you a customer's own phrasing in a live conversation; the Reddit scrape gets you the same phrasing at scale, unprompted, from people who were not talking to a vendor. Both feed the same downstream assets: ad hooks, landing page headlines, and article angles that match how the audience actually describes the problem rather than how the industry names it.

> "you can go and scrape Reddit using Perplexity"

**Evidence:** Cody states that all of his ad research is Reddit scraped through Perplexity.

**How to do it**

1. List the subreddits where your target customer discusses their work, not the ones about your product category.
2. Ask Perplexity to summarize the recurring complaints and problems raised in those subreddits over a recent window.
3. Ask specifically for the exact phrasing people use, not a paraphrase of the themes.
4. Sort the extracted problems by how often they recur across separate threads.
5. Turn the top recurring problems into ad hooks and landing page headlines using the community's own words.
6. Cross-check the resulting phrases for search volume, since the community wording often differs from industry jargon.
7. Repeat quarterly, since the complaints shift with product and market changes.

**Tools:** Perplexity, Reddit

**Prompt / template:**

```text
Scrape and summarize the recurring problems and complaints discussed in [subreddits] over the last six months. Quote the exact phrasing people use to describe each problem.
```

**Pitfall:** Taking themes rather than exact wording loses the whole value. The point is the customer's language, and a summarized theme reads like every other vendor's copy.

**Apply at Pabau:** For Pabau this is a cheap source of the words practice owners use for admin overload, no-shows and staff scheduling, which should feed both ad copy and the H2 wording on blog articles rather than industry vocabulary.

**Apply anywhere:** Run your audience's subreddits through Perplexity and extract the exact phrasing people use to describe their problems. Use those words in ad hooks and headings instead of industry terminology.

### 18. Screen every community question by who is actually asking it  `114.10`
*useful · best practices · source 114*

Grow and Convert add a filter that stops community mining from producing content for the wrong audience. After finding a question in a Facebook group, a subreddit or a Quora thread, they ask who is asking this. Their worked example is an ecommerce thread on Reddit. The author had heard on a call that around fifty percent of ecommerce sites are custom built, which suggested a controversial piece on why building a custom ecommerce site is a bad idea. But the people asking on Reddit appeared to be founders starting ecommerce companies. If your target is large brands doing fifty million dollars or more, they moved past that question years ago and the piece would draw the wrong reader. The filter is applied to every sourced question, not just the doubtful ones, and it is the difference between a community ideas list and a community ideas list that converts.

> "who is asking this question?"

**Evidence:** Grow and Convert reject a custom-ecommerce-site topic sourced from Reddit on the grounds that the askers are startups, not the 50 million dollar brands a given product might target.

**How to do it**

1. For every question you pull from a community, write one line naming the likely company size, role and stage of the person asking.
2. Read the poster's profile and post history where the platform allows it, rather than guessing from the question alone.
3. Compare that profile against your written ideal customer profile.
4. Discard questions your buyer solved years ago, however much engagement they carry.
5. Discard questions from people who will never have budget, even if they are numerous.
6. Keep questions where the asker matches the buyer, and note the phrasing they used for the title.
7. When a question is right but the asker is wrong, look for the same problem restated at your buyer's scale and target that version.
8. Re-check the filter at brief stage, since a broad brief can drift back to the beginner reader.

**Pitfall:** Communities skew toward beginners because beginners ask the most questions. Mining them without the who-is-asking filter fills the calendar with starter-level content and the blog converts nothing.

**Apply at Pabau:** Aesthetic Facebook groups are dominated by solo injectors just opening up, while Pabau's better fit is multi-location and established practices. David should filter group-sourced ideas against that, and restate beginner questions at clinic-group scale before commissioning.

**Apply anywhere:** Communities over-represent beginners. For every sourced question, name the asker's company size, role and stage, compare it to your ideal customer, and either discard the question or restate the same problem at your buyer's scale.

### 19. Screen out keywords poisoned by an overlapping consumer market  `93.9`
*useful · content insights · source 93*

Goolding warns about a competitor type that is not a competitor at all: completely different companies using the same terminology. One of his clients integrates technology into offices and commercial buildings for energy control, access and air quality, a specialized high-ticket purchase. A large share of their keyword opportunities are poisoned by overlapping B2C terms such as air quality sensors, smart heating system and automatic door closer, where the SERP is filled with consumer product pages and reviews. Volume on those terms looks strong in a keyword tool, but the intent behind almost all of it is a homeowner buying a gadget. The check is to read the actual SERP rather than the volume figure, and to drop or requalify any term where the ranking pages serve a different buyer than yours.

> "'poisoned' by overlapping B2C terms"

**Evidence:** Goolding's commercial building technology client, where a bulk of keyword opportunities overlapped with consumer terms like air quality sensors and smart heating system.

**Pitfall:** Keyword tools give no signal that a term is split between two markets, so the poisoned terms usually have the highest volume on the sheet and get prioritized first.

**Apply at Pabau:** Pabau should check SERPs for terms like 'appointment book', 'client records' and 'consent form', which overlap with consumer and general-business intent, and add a clinical or practice qualifier where the SERP belongs to another market.

**Apply anywhere:** Read the SERP before trusting volume on any term your industry shares with a consumer market, and add a qualifier or drop the term when the ranking pages serve a different buyer.

### 20. Search Reddit, Discord and Quora by keyword and sort by top threads  `114.11`
*useful · concrete actions · source 114*

Alongside Facebook groups, Grow and Convert name Reddit, Discord and Quora as ideation sources, and they give a specific method rather than general browsing. Run a keyword search on the platform, sort the results by top threads, and read down looking for questions or challenges that stand out. Sorting by top rather than by recent is the operative instruction: it surfaces the threads the community itself upvoted, which is a demand signal you get for free without any keyword tool. The author demonstrates with a Reddit search for 'ecommerce'. He pairs what he finds with something heard on a sales call, that around half of ecommerce sites are custom built, and turns the combination into a controversial angle on why building a custom ecommerce site is a bad idea. The pattern is worth copying: a community thread supplies the question, a first-hand data point supplies the angle.

> "run a keyword search, sort by top threads"

**Evidence:** A Reddit search for 'ecommerce' plus a sales call data point that around 50 percent of ecommerce sites are custom built produced a contrarian topic on custom builds.

**How to do it**

1. List the two or three subreddits, Discord servers and Quora topics your buyers actually use.
2. Search each one for your core category keyword rather than scrolling the feed.
3. Sort results by top threads, not by newest, so upvotes act as the demand filter.
4. Read the top twenty threads and copy out every post phrased as a problem or a decision.
5. Note the vote and comment counts next to each, as your ranking signal.
6. Pair each recurring question with a data point you own, from a sales call, your product data or a customer conversation.
7. Turn the pairing into an angle rather than publishing a plain answer to the question.
8. Run the who-is-asking filter on each thread before it enters the calendar.

**Tools:** Reddit, Quora, Discord

**Pitfall:** Sorting by new gives you noise and a skewed picture of what the community cares about. The signal is an ideas list full of one-reply threads that nobody else asked.

**Apply at Pabau:** David should search the aesthetics and med spa subreddits and Quora topics for terms like patient records, no-shows and consent forms, sorted by top. Pair the recurring threads with Pabau's own product data to give each article an angle a competitor cannot copy.

**Apply anywhere:** Search each community by your category keyword and sort by top threads so upvotes do the filtering. Pair the recurring question with a first-hand data point you own, and write the angle rather than a plain answer.

### 21. Search for keywords that carry your differentiator as a phrase  `102.5`
*useful · concrete actions · source 102*

Grow and Convert argue your product's differentiators should be treated as keyword modifiers, not just sales copy. Their example: if you sell a plant-based pre-workout mix and being natural or plant-based is a competitive advantage, search for and target keywords containing those exact phrases. The payoff is double. The traffic matches the ideal buyer persona more closely, because the searcher has already self-selected for the attribute you win on. And the article gets a natural opening to argue why your version is better than the rest of the category, since the query itself is about that attribute. This is a cheap way to raise conversion rate on a page without changing anything about the writing, because the qualifier does the filtering before the click.

> "if you sell a plant-based pre-workout mix"

**Evidence:** Grow and Convert give the plant-based pre-workout example and say the approach reaches people who closely match the ideal buyer persona.

**How to do it**

1. Write down the two or three attributes on which your product genuinely beats the alternatives.
2. Put each attribute in a keyword tool as a modifier on your main category term and pull the suggestions.
3. Keep the variants where the modifier is the searcher's main filter, not an incidental word.
4. Build a page per kept variant and put the modifier in the title, URL, H1 and first sentence.
5. Inside the page, compare against alternatives specifically on that attribute, using evidence rather than assertion.
6. Compare conversion rate on modifier pages against your plain category pages to confirm the qualifier is working.

**Pitfall:** Choosing a differentiator nobody searches for, or one your competitors also claim. The signal is a modifier page with no volume and a SERP full of competitors using the same word.

**Apply at Pabau:** Pabau should target modifiers it actually wins on, such as all-inclusive pricing, and build pages for queries pairing those attributes with practice management software rather than only the bare category term.

**Apply anywhere:** Treat your genuine differentiators as keyword modifiers. Build one page per modifier variant, put the modifier in the title and first sentence, and use the page to argue the attribute head-on.

### 22. Segment the audience by what they search, not by who they are  `105.3`
*useful · best practices · source 105*

Grow and Convert reject the standard persona exercise as an input to SEO. Knowing your buyer is a 35 to 45 year old VP of Engineering at a mid-size SaaS company tells you nothing about whether that person is in the market today. Their replacement is to segment on the search itself: what the person is looking for beats who the person is, because organic lead generation starts from a query. They keep the persona work only insofar as it produces pain points, and they source those pain points from sales and customer success rather than from a demographic template. The practical effect is that the planning document changes shape. Instead of a persona deck, the team maintains a list of pain-point queries mapped to pages.

> "Who cares if they have a certain job title"

**Evidence:** Grow and Convert call this Pain Point SEO and say pain points and buying intent matter more than whether a searcher fits a persona, based on writing thousands of bottom-funnel pieces for clients.

**How to do it**

1. Stop the persona deck at demographics and do not use it to choose topics.
2. Book a 45-minute call with sales and a second with customer success.
3. Ask which problems come up repeatedly on sales calls, which parts of the product prospects get excited about, and which specific capability closed the last ten deals.
4. Write each answer as a problem statement in the customer's own words, not in your product vocabulary.
5. Convert each problem statement into the query that person would type when ready to fix it.
6. Check each query in Ahrefs or Semrush for real phrasing and variants, keeping candidates even at low volume.
7. Map one page to each surviving query and drop any query where the searcher is not choosing a solution.
8. Revisit the list quarterly with the same two teams as the product and objections change.

**Tools:** Ahrefs, Semrush

**Pitfall:** Teams keep the persona doc and bolt pain points onto it, then still choose topics by what the persona would find interesting. The signal is a content calendar full of industry trend pieces that the persona would enjoy but never search for.

**Apply at Pabau:** Pabau's briefs should be driven by what practice owners type when a problem bites, not by a clinic-manager persona. David should run the three questions past Pabau's sales and CS teams and keep the output as a live pain-point-to-page map.

**Apply anywhere:** Drop the persona deck as a topic-selection input. Interview sales and customer success for the problems that come up on calls and the capability that closes deals, turn each into the query someone types when ready to fix it, and map one page per query.

### 23. Split keyword duties: autocomplete tool for terms, Ahrefs for volume  `139.9`
*useful · best practices · source 139*

Brandon ran two tools in sequence rather than one. After the customer interviews surfaced the pain points, he used Clearscope to see what relevant keywords people actually search, since Clearscope surfaces terms drawn from Google autocomplete behaviour, and then used Ahrefs to find which of those matched the intent and carried real search volume. His stated split is that Ahrefs gives a much broader view of keywords to target while Clearscope shows the language people use around a topic. The order matters: the pain point comes first from interviews, the phrasing comes second from the autocomplete-driven tool, and the volume and difficulty filter comes last from Ahrefs. Volume never opened the process.

> "Ahrefs can give you a much broader view of keywords to target"

**Evidence:** Brandon used this sequence to build the Keeper Tax keyword list across competitor, use case and pain-point groups.

**How to do it**

1. Write each interview pain point as the sentence the customer actually said.
2. Run that phrasing through Clearscope to see the related terms and autocomplete-style language around it.
3. Copy the candidate phrasings into Ahrefs Keywords Explorer in a batch.
4. Filter to terms whose searcher intent matches the pain point, discarding same-word different-intent matches.
5. Sort the survivors by volume and keyword difficulty and note which are realistic for your domain.
6. Rank the final list by conversion intent first and volume second.
7. Assign each surviving term to either an existing page to retarget or the content backlog.

**Tools:** Clearscope, Ahrefs

**Pitfall:** Starting in Ahrefs and sorting by volume produces terms whose searchers share your words but not your problem, which is exactly how Keeper Tax first landed on 'business expense tracker'.

**Apply at Pabau:** Pabau's keyword work should start from what practice owners said in support tickets and sales calls, get phrasing from a SERP term tool, and only then check volume and difficulty in Ahrefs.

**Apply anywhere:** Start from the customer's own wording, get phrasing variants from an autocomplete-driven term tool, then check volume and difficulty in Ahrefs last.

### 24. Start month one with three keywords: one category, one comparison, one platform  `140.8`
*useful · concrete actions · source 140*

Lewis narrowed a longer research list to three topics for the first month, and the mix is instructive rather than arbitrary. She took manual vs automated accessibility testing, manual accessibility audit, and WordPress ADA compliance. One is a comparison of approaches, one names the service exactly as sold, and one attaches the problem to a platform the buyer already uses. Her selection rule was that each topic either directly described what the client offered or showed the searcher comparing options, which puts them near the end of the buying cycle. She sourced the category-style terms by reading the client's own website for the specific words describing the service offering, rather than starting in a keyword tool. Three per month is a deliberately small batch that lets you learn from conversions before committing to more.

> "decided to narrow it down to three for the first month"

**Evidence:** ADA Compliance Pros started with manual vs automated accessibility testing, manual accessibility audit and WordPress ADA compliance in month one, and had eight first-page articles by month four.

**How to do it**

1. Read the client's own service pages and list the exact words used to describe what is sold.
2. Turn those words into category terms such as best X, X services and X tools.
3. Add comparison terms pitting the two main approaches or products against each other.
4. Add platform-qualified terms combining the problem with the software the buyer already runs.
5. Cut the list to three for month one: one category, one comparison, one platform-qualified.
6. Check each survivor answers yes to whether it describes the offering or shows the searcher comparing options.
7. Publish those three, run paid distribution to them, and read conversions before choosing month two.

**Tools:** Ahrefs

**Pitfall:** Publishing fifteen bottom-of-funnel pieces before any of them has converted means you learn nothing from month one and have to fix fifteen articles instead of three.

**Apply at Pabau:** David should batch pabau.com's bottom-of-funnel work in threes: one category page such as practice management software for medical spas, one comparison against a named rival, and one platform-qualified page tied to a system clinics already run. Read demo requests before commissioning the next three.

**Apply anywhere:** For month one, pick three keywords: a category term taken from your own service page wording, a comparison of the two main approaches or products, and a term qualifying the problem by the platform your buyer already uses. Publish only those three, distribute them, and let conversions choose the next batch.

### 25. Start the competitive head category pages early despite the wait  `106.18`
*useful · best practices · source 106*

Grow and Convert single out the obvious category keywords, terms like 'CRM software' or 'marketing analytics tools', as the ones with the clearest buying-intent and the heaviest competition. Their handling is a timing decision rather than a skip. Start these early so they have time to rank, and in parallel build the expanded variant list that fewer competitors are targeting so something delivers in the meantime. This pairs with their fourth mistake, where waiting until you feel ready to compete simply hands the term to the incumbent for another year. The practical implication is that the head category page should be commissioned in the first batch and then reviewed on a nine-to-twelve month horizon, while the long-tail variants are reviewed at three.

> "get started on these early on to give them time to rank"

**Evidence:** Grow and Convert note the obvious category keywords are often highly competitive, which is why they start them early and build variants alongside.

**How to do it**

1. Identify the three or four head category terms that describe your product most directly.
2. Commission a dedicated page for each in the first publishing batch.
3. Do not judge these pages on three-month rankings; set the review at nine to twelve months.
4. Publish the expanded low-competition variants in parallel so the batch produces early conversions.
5. Internally link the variant pages up to the head category page as they start ranking.
6. Point any link building or digital PR at the head category page rather than at the variants.
7. Refresh the head page every six months with current competitor and pricing detail while it climbs.

**Pitfall:** Deferring the head category page until the site is 'ready'. It is the slowest page to rank, so deferring it just moves the payoff back by however long you waited.

**Apply at Pabau:** Pabau's head term pages, practice management software and clinic management software, should be live and refreshed continuously, with the vertical variant pages linking up into them.

**Apply anywhere:** Commission your head category pages in the first batch even though they are the hardest, review them on a nine-to-twelve month horizon, and run the low-competition variants alongside so the batch still delivers early.
