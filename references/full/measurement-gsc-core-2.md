# Measurement & GSC — core (part 2 of 5)

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Diagnose a low-converting post by framework, not by audience relevance  `90.10`
*core · content insights · source 90*

Grow and Convert show two blog posts from the same client with almost identical organic traffic where the second produces far fewer conversions. Their diagnosis is precise and worth copying. Post two does rank for a keyword the target audience would search for, in this case a sales-related term, so it passes the usual relevance test that most teams apply. What it fails is the framework test: it is not a category page, not a comparison page and not a jobs-to-be-done page, so it is a classic low-converting top-of-funnel post. The lesson is that audience relevance and buying intent are different filters, and the first one passes almost everything. When a page has traffic and no conversions, the question is not whether the right people are reading it but whether the query implies anyone is close to buying.

> "they get almost the identical level of traffic, but #2 gets far lower conversions"

**Evidence:** In Grow and Convert's client report, two posts with near-identical organic traffic differed sharply in last-click conversions, with the weaker one ranking for an audience-relevant but framework-less keyword.

**How to do it**

1. Pull the organic landing pages report with sessions and product conversions side by side.
2. Pair up posts with similar traffic and very different conversion counts.
3. For each low-converting post, write down the primary query it ranks for.
4. Classify that query into one of the three frameworks; if it fits none, label it top of funnel.
5. Do not accept 'our audience searches this' as evidence of intent, since that test passes almost any topic.
6. For posts that fit a framework but still fail, check the CTA is contextual to the post before rewriting the content.
7. For posts that fit no framework, decide between adding a genuine product angle, merging them into a stronger page, or leaving them as traffic pages with no expectation of conversions.
8. Record the classification against each post so future planning does not repeat the mistake.

**Tools:** Google Analytics

**Pitfall:** Trying to fix a top-of-funnel post's conversion rate with a better CTA or more copy. Grow and Convert's point is that the query itself carries no buying intent, so no on-page change recovers it.

**Apply at Pabau:** When a Pabau article has traffic but no demo requests, David should classify its main query first. If it is neither a category, comparison nor clinic-task query, the fix is repositioning the topic, not rewriting the CTA.

**Apply anywhere:** When a post has traffic and no conversions, classify its main query before rewriting anything: audience relevance passes almost every topic, so check for buying intent instead.

### 2. Diagnose a top-3 post with falling conversions as a lost-tail problem  `116.12`
*core · content insights · source 116*

The most useful bucket in Grow and Convert's audit is the counter-intuitive one: posts still ranking in the top three for their target keyword whose conversions dropped anyway. Because the target position is unchanged, the usual explanations, algorithm hit or a worse page, do not fit. What actually happened is that the SERPs for the post's secondary keywords changed and the page fell out of the top spots for those, which is where much of the traffic and therefore the conversions came from. They say it was in the process of assigning a fix to each post that they discovered secondary keywords in the first place. So the diagnostic rule is: unchanged primary position plus falling conversions equals go and diff the secondary keywords.

> "still ranking in the top 3 for their target keyword yet saw a significant dip"

**Evidence:** Grow and Convert discovered secondary keywords while working through exactly this bucket for a SaaS client whose conversions had plateaued and dipped.

**How to do it**

1. Filter the audit for posts whose target keyword position is unchanged and in the top three.
2. Cross-check those against the conversion waterfall and keep the ones whose conversions fell.
3. For each, pull the ranked-keyword list for the pre-decline month and for today.
4. Identify the secondary keywords that dropped out of the top 10 or disappeared entirely.
5. Rank the losses by the traffic they carried and by buying intent.
6. Choose re-optimization or a new article per keyword using the SERP comparison test.
7. Do not touch the target keyword optimization, since it is still working.

**Tools:** Ahrefs, GA4

**Pitfall:** Reoptimizing the target keyword on a page that already ranks top three for it. You risk the ranking that still works while leaving the actual cause, the lost tail, untouched.

**Apply at Pabau:** When a Pabau page holds its position but demo requests fall, David should diff its secondary keywords rather than rewrite the page. The target term is not the problem and editing around it risks the ranking that still works.

**Apply anywhere:** When a page holds its position but conversions fall, diff its secondary keywords rather than rewriting. The target term is not the problem and editing around it risks what still works.

### 3. Discount AI tools' prompt volume figures as opt-in panel extrapolation  `83.4`
*core · best practices · source 83*

Devesh is specific about why prompt volume numbers are shaky, including from tools claiming data from millions of real chats. He names Profound directly. The data comes from people who volunteered, knowingly or not, to have their browsing tracked. The vendor summarizes patterns in that panel and reports that certain prompts have certain search volumes. His objection is that this is still the old SEO way of thinking, keywords with volumes, and that nothing in the panel reveals the personalization sitting underneath each prompt. That personalization is what decides whether you get recommended. He argues the honest planning assumption is that the search volume of most people's prompts is one. Use volume figures for rough topic sizing only.

> "even ones like Profound that claim to have data"

**Evidence:** Grow and Convert say panel data is collected from users who volunteered to have browsing tracked, and that the vendors summarize patterns and attach volumes to them.

**How to do it**

1. Ask any AI visibility vendor how their prompt volume is sourced, and whether it is an opt-in browsing panel.
2. Ask what percentage of the panel is logged in with memory enabled, since logged-out sessions cannot show personalization.
3. Stop reporting individual prompt volumes to stakeholders as if they were keyword volumes.
4. Roll the vendor's prompts up into topic baskets and report basket-level presence instead.
5. Sanity-check any prompt the tool calls high-volume against your own shared customer chats.
6. Assume a prompt volume of one when deciding whether to build a page for a specific phrasing.
7. Keep vendor data for trend direction over time, not for absolute planning numbers.

**Tools:** Profound, Peec, Traqer

**Pitfall:** Building a content plan off a ranked prompt volume list reproduces keyword-era thinking on data that is far thinner than a keyword tool's. The signal you have hit it is a plan whose top targets all came from one vendor's export.

**Apply at Pabau:** Pabau should not let a Profound-style prompt volume export drive the blog calendar. Use it to spot topic gaps, then decide priority from real practice questions collected by sales and support.

**Apply anywhere:** Do not let a vendor's prompt volume export drive your content calendar. Use it to spot topic gaps, then set priority from the real questions your sales and support teams hear.

### 4. Divide rankings by posts published to isolate time from volume  `153.2`
*core · best practices · source 153*

Grow and Convert make a measurement point most content reports miss. Their first chart showed total first-page rankings climbing with tenure, but they note the obvious objection: a client with 50 published pieces will naturally outrank a client with five. So they re-cut the same data by dividing first-page rankings by number of pieces published per client. That normalized curve is what shows time itself carrying the effect. The lesson generalizes to any content dashboard. Raw ranking counts and raw traffic conflate publishing volume with content effectiveness, so they cannot tell you whether your process is improving or whether you simply published more. Only the per-post ratio separates the two.

> "isolate the effect of time on rankings by controlling for the number of pieces published"

**Evidence:** Grow and Convert re-cut their 40+ client dataset by dividing first-page rankings by pieces published, which is what surfaced the month-15 crossover.

**How to do it**

1. Pull total first-page (top 10) ranking count for the site each month.
2. Pull the cumulative count of unique posts published as of that same month.
3. Divide rankings by posts to get a rankings-per-post figure for every month.
4. Plot both the raw count and the normalized ratio side by side on the same dashboard.
5. Treat a rising raw count with a flat ratio as evidence that volume, not quality, is driving results.
6. Segment the ratio by content type or author to see which production route actually performs.
7. Re-run the split whenever you change your writing process, so you can attribute the change.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Reporting raw ranking or traffic counts only. They always go up while you keep publishing, which hides a process that is not actually working.

**Apply at Pabau:** Pabau's content reporting should carry a rankings-per-post line alongside total sessions. Split it by route so /templates/ pages and /blog/ articles are judged separately, since the two convert and rank on different timelines.

**Apply anywhere:** Report first-page rankings per published post alongside your raw totals, and split it by content type. Raw counts rise with publishing volume alone, so only the ratio tells you whether the process is getting better.

### 5. Do not fix last-click by switching to first-click attribution  `177.7`
*core · best practices · source 177*

The author makes a point that cuts against a common reflex. Most companies measure success on last-click and therefore have no real understanding of why someone bought, but he says the solution is not as simple as switching to first-click. His worked example is a referral lead that took the rep months to close, during which the decision makers signed up for a drip sequence, saw retargeting ads, and read a blog post that convinced them to work with the company. No single-touch model captures that. His conclusion is not that measurement is impossible but that budget allocation follows measurability. It is easy to credit the rep for closing and hard to credit the influencing touches, so marketing loses the budget argument unless senior leadership already believes in it. This contradicts the frequent advice to simply flip the model.

> "Most companies still measure success on last-click attribution"

**Evidence:** The author's example deal: a client referral closed over months, during which the buyers went through a drip sequence, retargeting ads and a blog post, none of which either single-touch model captures.

**How to do it**

1. Report last-click and first-click side by side, and label neither as the truth.
2. Add a self-reported attribution question on the demo or contact form asking how the buyer first heard of you.
3. Record the assisting touches per closed deal: drip sequence, retargeting, specific articles read.
4. Pull that list from your CRM per closed-won deal rather than from analytics alone.
5. Present influenced pipeline as a separate line from sourced pipeline in every report.
6. Agree the definition of an influencing touch with sales before you present it, not after.
7. Re-argue the budget on influenced pipeline, and expect to need leadership belief to close the gap.

**Tools:** Google Analytics, HubSpot

**Pitfall:** Switching to first-click to win the credit argument just moves the distortion. Long sales cycles with referral origins will now credit marketing for deals it did not influence, which sales will notice and use against you.

**Apply at Pabau:** Pabau's demo requests are high-consideration and multi-touch, so David should not settle the credit question with one attribution model. Adding a how did you hear about us field to the demo form is the cheapest fix.

**Apply anywhere:** Report first-click and last-click together and treat neither as the answer. Add a self-reported how-did-you-hear-about-us field and record the assisting touches per closed deal, then argue budget on influenced pipeline.

### 6. Do not trust data-driven attribution as your only conversion number  `149.5`
*core · best practices · source 149*

GA4 defaults to data-driven attribution, which uses machine learning on your own account data to split credit across click interactions. Grow and Convert give two specific reasons not to rely on it alone. First, the algorithm is opaque; Google's own documentation of it is esoteric and you end up trusting the numbers blindly, which is not the case with a rules-based model. Second, above a volume of events in a month, and GA4 counts all its automatic scroll, click and page_view events toward that volume, the reporting runs on a sample rather than raw data, which can skew the conversion figures. Their conclusion is that data-driven attribution alone is risky and insufficient, so they run rules-based reports alongside it.

> "based only on a sample of your data"

**Evidence:** Grow and Convert list opacity and sampling as the two drawbacks and state that relying on data-driven attribution alone is risky and insufficient for understanding true conversion numbers.

**How to do it**

1. Treat the default Conversions report as a high-level volume view, not a decision report.
2. Check your monthly event volume, remembering automatic events count toward it, to gauge sampling risk.
3. Reduce that volume by turning off unnecessary automatic events as conversions.
4. Build at least one rules-based report, first click or last click, alongside the default.
5. Compare the same date range across models and note where the numbers diverge most.
6. Report the range across models to stakeholders rather than one number presented as truth.
7. Never change a content strategy on a data-driven number that a rules-based model contradicts without investigating why.

**Tools:** Google Analytics 4

**Pitfall:** On a busy site the data-driven number is a sampled estimate, so month-to-month movement can be sampling noise rather than performance, and there is no warning in the interface.

**Apply at Pabau:** Pabau should read demo attribution across at least two models and treat any single GA4 number as one view; the /blog/ contribution in particular will look different under last click than under data-driven.

**Apply anywhere:** Read conversion attribution across at least two models and treat any single GA4 number as one view rather than the answer.

### 7. Expect bottom-funnel blog traffic to plateau around 3,500 pageviews a month  `141.5`
*core · content insights · source 141*

Grow and Convert publish the shape of the curve their strategy produces so clients stop reading a plateau as failure. On the VC-backed subscription client, combined Facebook advertising, community promotion and SEO drove thousands of visitors to the blog within the first two months, then traffic leveled off around 3,500 pageviews a month. They say that is the designed outcome, not a stall: conversion-intent bottom-funnel content is not highly shareable and not traffic driving, and even their keyword-led posts were prioritized on the conversion intent of the query rather than its search volume. The contrast case in the same article is the B2C concussion treatment center, which reached over 8,000 visitors a month on a handful of articles. Their conclusion is that you cannot predict traffic before starting, B2C generally out-traffics B2B, and the strategy matters more than the traffic target.

> "traffic then starts leveling off around 3,500 pageviews a month"

**Evidence:** Subscription client: thousands of visitors within 2 months, leveling off near 3,500 pageviews a month. B2C concussion center: over 8,000 visitors a month on a handful of articles.

**How to do it**

1. Before the engagement starts, tell the stakeholder that a bottom-funnel program plateaus on traffic and rises on conversions.
2. Set the monthly report's headline metric to conversions, with pageviews as a supporting line.
3. Track pageviews to your published articles only, starting from zero, rather than to the whole blog, so the numbers are attributable.
4. When traffic flattens, check whether conversions are still climbing before treating the flatness as a problem.
5. Do not set an absolute traffic goal at kickoff; commit instead to beating the previous month on traffic and conversions.
6. If traffic genuinely matters to the business, add a separate shareable or paid-social content line rather than diluting the bottom-funnel keyword list.

**Tools:** Google Analytics

**Pitfall:** A stakeholder who was promised traffic growth reads the plateau as the program failing and pushes for high-volume head terms, which reverses the conversion gains.

**Apply at Pabau:** Pabau's practice-management blog is closer to the B2B case, so David should expect a modest traffic ceiling from bottom-funnel articles and report demo requests as the headline. Do not let a flat pageview line trigger a swing back to high-volume aesthetics topics that never book demos.

**Apply anywhere:** Expect a bottom-funnel content program to plateau on traffic by design, since conversion-intent content is not shareable. Report conversions as the headline metric, track pageviews only to the articles you published, and never commit to an absolute traffic number at kickoff.

### 8. Export GSC queries via API, let Claude tag AI Mode ones  `02.1`
*core · ai workflows · source 02*

Because AI Mode and AI Overview queries are not broken out anywhere in standard Google Search Console reporting, Glenn Gabe's workaround is to export every query-plus-landing-page combination from the Search Analytics API in one bulk pull using Analytics Edge, which writes directly into Excel or Google Sheets, then hand that full spreadsheet to Claude, using Claude Cowork specifically, with a new project and the exported file added as a working-directory document, prompting it to identify which queries look like they came from someone using Google's AI Mode, provide reasoning per query, and output a new worksheet listing its findings plus the URL cited in each case. In his test run, Claude processed over 50,000 exported queries in just a few minutes.

> "export all of that query data via the Search Analytics API"

**How to do it**

1. Open Analytics Edge, connected to Excel or Google Sheets, and connect it to the target GSC property.
2. Configure the report to include both the 'query' and 'page' dimensions together in the same export, so each row pairs a search query with the landing page that ranked for it.
3. Set a date range wide enough to capture a large sample (inferred: a recent 3-6 month window, since the case study covers over 50,000 exported query rows).
4. Run the export and use Analytics Edge's 'Write to worksheet' action to populate a worksheet with all query and landing page rows.
5. Save the resulting worksheet as a file Claude can read, such as an .xlsx file or a Google Sheet.
6. Open Claude (Claude Cowork was used here, though any Claude surface with file access works), create a new project, and add a working directory containing the exported spreadsheet.
7. Paste this exact prompt into Claude: 'Analyze the queries in the spreadsheet {sheet name here} and determine which ones could be prompts based on people using Google's AI Mode. These would be queries that extend conversations, answer questions from the chatbot, or are elaborate and longer prompts that would not fit a traditional search on Google. For example, "yes", "no", "tell me more", etc. Provide analysis and explain why each query was selected as an AI Mode candidate and then create a new worksheet with fields documenting your findings. Make sure to include the url that was cited as part of that conversation.'
8. Let Claude process the full query set and review the new worksheet it creates, which documents each AI Mode candidate query, its reasoning, and the cited URL.
9. Manually scan the output for two known noise sources: fully ambiguous queries with no clear context, and queries clearly generated by automated SEO or AI-visibility tracking tools rather than real users (inferred: cross-reference suspicious query patterns against known rank-tracking tool behavior).
10. Cross-check whether the cited, AI-Mode-flagged queries and landing pages are receiving any clicks in the standard performance report, since this case study found close to zero clicks on these despite citation.
11. Once the process works, save it as a reusable Claude skill so it can be re-run on other sites or clients without rebuilding the prompt from scratch (inferred: use Claude's skill-saving feature to persist this exact workflow).

**Tools:** Google Search Console, Analytics Edge, Claude, Claude Cowork, Excel, Google Sheets

**Prompt / template:**

```text
Analyze the queries in the spreadsheet {sheet name here} and determine which ones could be prompts based on people using Google's AI Mode. These would be queries that extend conversations, answer questions from the chatbot, or are elaborate and longer prompts that would not fit a traditional search on Google. For example, "yes", "no", "tell me more", etc. Provide analysis and explain why each query was selected as an AI Mode candidate and then create a new worksheet with fields documenting your findings. Make sure to include the url that was cited as part of that conversation.
```

**Pitfall:** Assuming every ambiguous, conversational-looking query is a genuine human AI Mode user — a portion of this traffic is clearly automated queries run by SEO and AI-visibility tracking companies, not real searchers, so treat the classified list as a starting point for further investigation, not a clean dataset.

### 9. Export GSC to BigQuery; compare crawl spend against click value  `03.9`
*core · concrete actions · source 03*

For any site large enough to run query-template or programmatic projects, using BigQuery via Search Console's bulk data export is described as mandatory, because the standard Search Console UI loses nearly 40% of query-level click and impression data to k-anonymization. With the full BigQuery data, a query can show each URL's first and last impression date and days elapsed since the last one, flagging pages as candidates for content revitalization once they've gone quiet. A second essential check compares crawl activity against click/impression activity per URL segment; in one example project, a huge share of Googlebot's crawl activity went to tech and asset URLs generating zero clicks, meaning crawl quota was wasted on sections that don't drive the click-satisfaction signals that actually influence rankings.

> "Google Search Console loses nearly 40% of the query-based click and impression"

**How to do it**

1. In Google Search Console, go to Settings and set up a bulk data export of Search Console data to a Google Cloud BigQuery project/dataset. (inferred exact menu path based on GSC's documented bulk-export feature)
2. Once data is flowing into BigQuery, write a query grouping impressions by URL that returns each URL's first and last impression date plus days elapsed since the last impression.
3. Flag URLs with a long gap since their last impression as candidates for content revitalization, rather than relying on the standard GSC UI, which undercounts low-volume queries via k-anonymization.
4. Separately, pull Googlebot crawl-activity data by URL/URL-segment via server log files or the Crawl Stats report.
5. Compare the crawl-activity data against click/impression data for the same URLs or segments to see where crawl budget and click value diverge.
6. Identify any segment receiving disproportionate crawl activity relative to the clicks/impressions it generates (the source's example: tech and asset URLs with heavy crawl activity and zero clicks).
7. Reallocate crawl budget away from those low-value segments, via robots.txt, noindex, URL pruning, or fixing internal-linking patterns that over-expose them, toward sections that drive click-satisfaction signals. (inferred specific levers)
8. Where relevant, also pull Semrush or an equivalent tool's ranking data alongside GSC, since it can surface Google Business Profile-driven visibility that Search Console's web-search-only data won't show. (inferred from the source's brief mention)

**Tools:** Google Search Console, BigQuery, Semrush

**Pitfall:** Relying only on the standard GSC UI/API for a large programmatic site, which silently discards roughly 40% of query-level click and impression rows via k-anonymization, and failing to check whether crawl budget is wasted on non-valuable URL segments instead of the sections that actually generate clicks.

### 10. Find your accidental best converters with GA's model comparison tool  `136.1`
*core · concrete actions · source 136*

Grow and Convert's whole pain point SEO strategy came out of one report. Challenged by Leadfeeder's CEO Pekka Koskinen in March 2018, Benji Hyam and Devesh Khanal opened the model comparison tool in Google Analytics, which attributes conversions under different models, and ranked blog posts by signups rather than pageviews. Two posts they had written almost as tests, a product comparison and a category tools list, were driving the most conversions while sitting outside the top 10 posts by traffic. Their conversion rates were roughly 10 times anything else on the blog. Traffic reporting had hidden both posts completely. The lesson they draw is that the strategy signal lives in the conversions-per-post view, and that you should read it before deciding what to publish next.

> "the model comparison tool in GA which measures"

**Evidence:** Two low-traffic posts at Leadfeeder converted around 10x better than the story posts that outranked them on traffic; that finding produced the pain point SEO strategy and 225+ signups a month.

**How to do it**

1. Open Google Analytics and run the model comparison report over the last 6-12 months against your signup or lead goal.
2. Break the report down by landing page and filter to blog URLs only.
3. Export conversions per post alongside sessions per post into one sheet.
4. Add a column for conversions divided by sessions and sort by it, not by sessions.
5. Flag every post whose conversion rate is 5x or more the blog median, however little traffic it has.
6. Label each flagged post by the keyword it ranks for and by content type: comparison, alternatives, category list, how-to.
7. Treat the content types that repeat among the flagged posts as your production frameworks for the next quarter.
8. Re-run the report monthly so new outliers surface before the editorial calendar is set.

**Tools:** Google Analytics

**Pitfall:** The highest-converting posts often sit outside the top 10 by traffic, so a pageview-ranked report buries them. Teams then conclude their best-performing format is whatever got shared most, and keep producing it.

**Apply at Pabau:** David should build a conversions-per-article view for pabau.com in GA4 or the CRM, keyed to demo bookings rather than sessions, and rank every blog and template page by it. Expect the winners to be comparison and alternatives pages with low traffic, and let that ranking pick the next quarter's briefs.

**Apply anywhere:** Rank your blog posts by conversions per session, not by pageviews, using the GA model comparison report. The pages converting 5-10x the median are usually low-traffic bottom-funnel posts, and the content types that repeat among them tell you what to publish next.

### 11. Fix the 4th/5th biggest revenue-loss page first, bottom-up  `29.12`
*core · concrete actions · source 29*

For an established site with limited SEO time (his benchmark is 10 hours a month), Hank starts by ranking pages by year-over-year revenue decline and immediately discarding unrecoverable categories - a discontinued product, or search demand fully absorbed by AI answers. Counterintuitively, he does not start with the single biggest revenue-loss page; he starts with the fourth or fifth biggest, because it's likelier to be genuinely fixable and lets him build a working method before tackling the toughest case. His process: document exactly what current best-performing comparable pages do differently, apply those specific changes to the chosen underperforming page as a controlled experiment, and note that you often don't need to recover 100% of a page's old traffic - rebuilding the revenue story around the right 40-50% of past traffic (the users who actually convert) is often enough. Each month's fix and lesson feeds into tackling the next-ranked item, working bottom-up toward the biggest problems over time.

> "start with maybe the fourth or fifth biggest revenue-loss item"

**How to do it**

1. Pull year-over-year organic traffic or revenue by page/segment and rank pages by size of decline.
2. For each declining page, diagnose the cause: discontinued product, search demand absorbed by AI answers, or a fixable on-page/ranking issue.
3. Discard the unrecoverable categories from your active fix list.
4. Do not start with the single biggest revenue-loss item; select the fourth or fifth biggest item on the ranked list instead.
5. Document specifically what your current best-performing comparable pages do differently in structure, targeting, depth, or CTA placement. (inferred)
6. Estimate what share of the page's historical traffic was genuinely valuable/converting traffic rather than assuming you need to recover 100% of past volume.
7. Implement the identified changes from the successful comparable pages onto the chosen underperforming page as a controlled experiment.
8. Measure the result, capture the learning, and apply it to the next-ranked revenue-loss item the following month.

**Pitfall:** Spending your limited monthly SEO time on the single biggest revenue-loss page first is tempting but often wasted effort if that loss is unrecoverable (discontinued product, AI-absorbed query) - diagnose the cause before picking where to start, and prioritize the fourth or fifth-ranked item where a fix is more likely to work.

### 12. Forecast a new page's ROI from your own ranking data first  `10.4`
*core · best practices · source 10*

Once a site has established topical authority (its pages reliably index and rank), build a per-query ROI model using your own historical data rather than trusting keyword-tool estimates at face value: for example, a query Ahrefs says gets 5,000 searches a month might actually get 8,000 in reality, and ranking number one for it might convert to 2,000 actual clicks a month — record that real estimate-vs-actual ratio per query. Before writing a new page, look up a similar already-ranking page's real click and revenue numbers and use its actual performance, not the tool's raw volume estimate, to forecast the new page's expected traffic and revenue, then decide whether the page is worth the production cost. This turns content planning into a page-by-page ROI queue rather than a volume-only keyword list, and it compounds in accuracy as more pages go live and add data points.

> "do the math on what you'll get for the next query"

**How to do it**

1. For every page you publish, log its target query's tool-estimated search volume (e.g., from Ahrefs) alongside its actual clicks-at-position from Google Search Console once it ranks.
2. Build a running reference table of tool-estimate versus real GSC performance per ranking position, broken out by query type or niche.
3. Before greenlighting a new page, find the closest comparable already-ranking page in your own data set.
4. Use that comparable page's real click and traffic numbers, not the raw keyword-tool estimate, to forecast the new page's expected clicks if it reaches a similar position.
5. Multiply forecast clicks by your known conversion rate and deal value to estimate revenue ROI for the page before committing writing or design resources (inferred link from clicks to revenue).
6. Rank your content backlog by this ROI forecast and prioritize the highest-ROI pages first.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Don't rely on a keyword tool's raw volume estimate alone — real GSC clicks at a given position can run well above or below the tool's number, so calibrate using your own historical actual-vs-estimated data.

### 13. Four GSC signals that flag keyword cannibalization  `49.2`
*core · concrete actions · source 49*

Four specific signals in Google Search Console flag likely cannibalization: the same query showing multiple different URLs from your own site; a page's ranking position bouncing wildly (e.g., between position 20 and 80) rather than trending steadily, which usually means Google is confused about which of your pages is the better answer; high impressions but low clicks spread across several of your own pages for the same query; and a `site:` search for the topic returning three or four results from your own domain.

> "the page is bouncing between positions 20 and 80"

**How to do it**

1. Open Google Search Console and go to the Performance/Search Results report.
2. Add both the Query and Page dimensions to the table so you can compare by query and page together.
3. Sort or filter to find any single query returning multiple different URLs from your own site — flag these as cannibalization candidates.
4. For each flagged query, check its page's position-over-time chart for volatility (e.g., swinging between position 20 and 80) rather than a stable trend.
5. Cross-reference impressions vs. clicks for the same query across the candidate pages — high impressions with low clicks spread across several of your own pages is a second flag.
6. Run a `site:yourdomain.com "exact query"` search in Google and note if three or four of your own pages appear for the same topic.
7. Compile the list of candidate query/page-group pairs from all four checks before moving to the SERP-overlap verification step.

**Tools:** Google Search Console

**Pitfall:** A page bouncing wildly between position 20 and 80 isn't random noise — it's usually Google alternating which of your own pages it considers the better answer, so treat volatility itself as a diagnostic signal rather than dismissing it.

### 14. Freeze the prompt set before reading any AI visibility trend  `85.1`
*core · best practices · source 85*

Grow and Convert show that a brand-level AI visibility percentage moves for reasons that have nothing to do with visibility. On January 13 a client's score in Peec was 26.7%. On January 14 they added two new prompts the brand had no visibility for, and the score fell to 20%. Nothing changed inside ChatGPT or any other engine. The denominator grew. Any tool that divides mentions by tracked prompts behaves this way, so a trend line is only readable across a period where the prompt set was constant. Their fix is to treat prompt-set changes as annotations on the chart, the same way you would annotate a Google core update in GSC, and to never compare a before and after that straddles one.

> "the visibility score in Peec for this brand was 26.7%"

**Evidence:** Grow and Convert's client score in Peec fell from 26.7% on January 13 to 20% on January 14 purely from adding two prompts with no existing visibility.

**How to do it**

1. Export the current tracked prompt list from Peec, Profound or whatever tool you use, with the date, and store it as the baseline set.
2. Compute the visibility percentage only across that frozen set when reporting week-on-week change.
3. When you add or remove prompts, record the date, the prompts and the reason in an annotation log next to the chart.
4. Recompute the historic series on the new set as well, so the before and after are measured on the same denominator.
5. Show both lines to stakeholders for the first report after a change: old set continuing, new set from day one.
6. Never report a percentage drop without first checking the prompt count on both dates.
7. Set a rule that the prompt set changes on a fixed cadence, for example the first Monday of the quarter, not ad hoc.

**Tools:** Peec, Profound, Traqer

**Pitfall:** Leadership reads the 26.7% to 20% drop as a performance failure and asks marketing to change tactics, when the only change was measuring more topics. The signature is a step change on a single day with no matching change in rankings or citations.

**Apply at Pabau:** When Pabau reports AI visibility, keep the tracked prompt list in a versioned file in the repo alongside the reporting script, and stamp every monthly report with the prompt count. A month where Pabau adds prompts for a new topic such as med spa payments must be reported as two numbers, not one falling number.

**Apply anywhere:** Keep your tracked prompt list under version control and stamp every AI visibility report with the prompt count. Any month where you add prompts should be reported as two numbers, the old frozen set and the new one, so a growing denominator is never mistaken for lost visibility.

### 15. GSC's performance report never separates AI Mode from normal search  `02.2`
*core · content insights · source 02*

Even though AI Mode and AI Overview data technically exists inside Google Search Console's performance reporting, it is blended into a single undifferentiated query stream alongside traditional 10-blue-link results, with no filter or dimension to isolate AI-surfaced queries from normal search queries. This means any site owner trying to understand AI Mode's specific impact on their site must reverse-engineer it from the mixed data rather than pull it directly, since John Mueller's own guidance (linking to Google's documentation) confirmed the data is technically present but did not resolve this lack of separation.

> "mixed in with all queries including 10-blue links"

**Evidence:** Direct statement that 'AIO and AI Mode data is not broken out' in the reporting and that it's 'mixed in with all queries including 10-blue links, AI Overviews, and AI Mode,' with no way to filter by AIOs or AI Mode directly in the GSC UI.

**Apply at Pabau:** Don't rely on GSC filters alone to measure Pabau's AI Mode/AI Overview visibility — plan to export the full query set and run a secondary classification pass (such as the Claude-based workflow in this article) any time AI-surface-specific reporting is needed.

**Apply anywhere:** Don't rely on GSC filters alone to measure your AI Mode/AI Overview visibility — plan to export the full query set and run a secondary classification pass (such as the Claude-based workflow in this article) any time AI-surface-specific reporting is needed.

### 16. Harvest page-2 and page-3 queries your best pages already rank for  `56.1`
*core · concrete actions · source 56*

Cody Schneider's core content-refresh loop starts from Search Console, not from a keyword tool. He looks at his top-performing articles and pulls the queries where those pages are already ranking on page two and page three - keywords the page was never written for and often doesn't even contain. His framing is that Google is telling you what it wants you to rank for: 'We want you to rank for this. We think you can rank for this.' Adding a section for those accidental keywords, or weaving them into the existing copy, typically produces a 10-20% lift 'overnight'. He says any site genuinely investing in SEO will find hundreds of these queries sitting on pages two and three.

> "go look at in page two, page three"

**How to do it**

1. In Search Console, open Performance and sort your pages by clicks to identify your top-performing articles.
2. For each of those pages, filter the query report by that page URL and set the position filter to roughly 11-30 so you only see page-two and page-three queries.
3. Export that query list and strip out queries that are simple variants of what the page already targets - you want the ones the page is ranking for accidentally.
4. Search the page's own HTML for each remaining query; the highest-value ones are the phrases that do not appear on the page at all.
5. Add a dedicated section (H2 or H3) answering the accidental query, or weave the phrase into existing copy where it reads naturally - do not bolt on a keyword list.
6. Republish and note the date, then watch clicks and average position for that specific query set rather than the page as a whole.
7. Re-run the same pull monthly; every lift creates a new set of page-two queries to harvest next time.

**Tools:** Google Search Console

**Pitfall:** This only works on pages that already have some ranking authority. Running it on pages with no impressions gives you nothing to harvest, and adding sections for keywords the page has never surfaced for is just padding.

**Apply at Pabau:** Pabau's biggest untapped SEO win is probably already in Search Console - run this page-two/page-three query pull against the top-performing Pabau articles before commissioning any new content, because a section added to an existing ranking page will move faster than a new URL.

**Apply anywhere:** Your biggest untapped SEO win is probably already in Search Console - run this page-two/page-three query pull against your top-performing articles before commissioning any new content, because a section added to an existing ranking page will move faster than a new URL.

### 17. Hold a content hire to four monthly numbers including which posts produce leads  `165.11`
*core · best practices · source 165*

Hyam's reporting set for a content marketing hire is four numbers, monthly: unique visitors to the blog, unique visitors from organic traffic specifically, leads or signups coming from the blog, and which blog posts are producing those leads or signups. The fourth is the one most teams skip and the one that changes behaviour. Total blog leads can be met by any traffic mix, but naming the posts that convert tells you which topics and funnel stages to commission more of, and exposes a blog where the leads all come from two old pages. Splitting organic out of total uniques separates promotion results from SEO compounding, which matters because Hyam expects promotion to carry the first months and SEO to build later.

> "Which blog posts are producing the leads/signups"

**Evidence:** Hyam's four-metric reporting set for content marketing hires.

**How to do it**

1. Build one monthly report with exactly four lines rather than a dashboard of everything.
2. Line one: unique visitors to the blog.
3. Line two: unique visitors from organic search, reported separately so promotion and SEO are distinguishable.
4. Line three: leads or signups attributed to the blog.
5. Line four: the specific posts producing those leads, ranked.
6. Set up conversion tracking and goals before the first report month, not after.
7. Use line four to decide the next quarter's topics, commissioning more of what converts.
8. Watch the organic line for the compounding curve; if it is flat after six months, the SEO half of the job is not happening.

**Tools:** Google Analytics

**Pitfall:** Reporting total blog traffic only. It hides the case where leads come from two legacy pages and every new article contributes nothing, which looks like growth until you check.

**Apply at Pabau:** Pabau's monthly content report should carry these four lines, with line four naming which articles produced demo requests. That list should then drive the next quarter's briefs.

**Apply anywhere:** Report four monthly numbers from a content hire: blog uniques, organic uniques, blog-attributed leads, and which specific posts produced those leads. Use the last line to pick the next quarter's topics.

### 18. Identify your top-traffic pages and freeze them into a rank tracker  `45.2`
*core · concrete actions · source 45*

David's second pre-migration step is to quantify exactly which pages carry your traffic, since he's observed the classic 80/20 split (80% of traffic through the top 20 pages) is often even more concentrated in practice — some sites get 90% of their traffic through only their top nine pages. The concrete action is to identify those top pages and the specific keywords each one ranks for, then deliberately change as little as possible about those specific pages during the migration, since they carry disproportionate risk. He also recommends loading those exact pages/keywords into a rank-tracking report before the migration so you have a clean before/after baseline to monitor as the migration proceeds.

> "figure out what the top pages are and what keywords they rank"

**How to do it**

1. Pull your analytics traffic-by-page report for the last 3-6 months.
2. Sort pages by organic sessions/clicks descending and calculate what percentage of total traffic the top 20 pages represent (inferred baseline check based on the 80/20 rule cited).
3. If the concentration is even higher (e.g., top 9 pages driving 90%), narrow your critical-page list accordingly.
4. For each identified top page, pull its top-ranking keywords from Google Search Console's Performance report or a rank tracker.
5. Load that exact list of URLs and keywords into a dedicated rank-tracking report/tool before the migration begins.
6. Flag these specific pages as 'minimal change' during migration planning — avoid altering their URL, title, H1, or core content unless the CMS switch absolutely requires it.
7. Monitor the rank-tracking report daily through and after the migration to catch any ranking drop on these specific pages early (inferred verification step).

**Tools:** Google Analytics, Google Search Console, a rank-tracking tool

### 19. Invert the model to find the direct rate that would beat nurture  `147.4`
*core · concrete actions · source 147*

When you have no reliable direct-to-lead number, Grow and Convert say to flip the calculation instead of abandoning it. Put in a guess and ask what your direct conversion rate would have to be in order to beat the email nurturing strategy. They run the same inversion in the other direction on Buffer's published numbers. Buffer reported 2.81% reader-to-email and 2.27% reader-to-app-signup. Feeding those into the model shows the email nurture would need to convert 81% of subscribers into app signups to beat going direct. They point out that getting 80% of a list simply to open an email is next to impossible, let alone sign up. The inversion turns an unmeasurable question into a plausibility check anyone can judge in seconds.

> "would need to convert 81% of email subscribers in to app signups"

**Evidence:** Buffer's published 2.81% reader-to-email versus 2.27% reader-to-signup implies an 81% email-to-signup requirement for nurture to win.

**How to do it**

1. Take the two numbers you can measure reliably, usually reader-to-email and reader-to-direct-signup.
2. Set the unknown email-to-lead rate as the variable in the spreadsheet.
3. Solve for the email-to-lead rate at which the nurture path exactly matches the direct path: direct rate divided by opt-in rate.
4. Compare that required rate against your actual email open rate as a sanity ceiling, since signups cannot exceed opens.
5. If the required rate exceeds a realistic open rate, stop building the list-first funnel and go direct.
6. Repeat the inversion whenever either measurable rate moves by more than a relative 20%.
7. Document the required threshold so stakeholders arguing for nurture have a specific number to beat.

**Tools:** Google Analytics

**Pitfall:** Treating a missing number as a reason to skip the analysis entirely. The inversion needs only the two rates you already have, and it usually produces a required threshold that is obviously unreachable.

**Apply at Pabau:** If Pabau cannot cleanly attribute newsletter-sourced demos, David should still solve for the required newsletter-to-demo rate and put that figure in front of anyone proposing list-first CTAs on pabau.com.

**Apply anywhere:** If you cannot cleanly attribute list-sourced leads, solve for the list-to-lead rate your nurture would need to win, and put that figure in front of anyone arguing for list-first CTAs.

### 20. Judge a non-search article on conversions, not traffic or rankings  `91.13`
*core · best practices · source 91*

Grow and Convert are explicit that the number one benefit of a disruption story is that it converts, meaning it brings visitors who match the target customer profile and resonate with the positioned pain points. Whether that is happening is measured in conversions, so conversion tracking has to be in place before the piece is promoted. They cannot show per-client conversion figures, so they present three proxy forms of evidence instead: their own lead numbers from their 'why we started' article, organic sharing and discussion of client stories on social, and long-term backlink accumulation. The practical point is that none of the usual content metrics apply. There is no keyword, so rank is meaningless, and social traffic volume says nothing about fit. Only conversions and the quality of the people converting tell you whether the pain point was right.

> "Whether you're doing that successfully or not can be measured in conversions"

**Evidence:** Grow and Convert say they have had disruption stories convert for dozens of clients, and show their own article's lead chart for early 2024 rather than traffic.

**How to do it**

1. Set up conversion tracking on the page before you spend a cent promoting it.
2. Define the conversion as a real lead action, a demo request or trial signup, not a scroll or newsletter opt-in.
3. Segment the report by landing page so this article's conversions are visible on their own.
4. Report conversions and lead quality, never sessions or rankings, for this piece.
5. Check whether converting visitors match the target customer profile, since fit is the actual test of the pain point.
6. If conversions are low but traffic is fine, rewrite the narrative and intro rather than the promotion.
7. Review it quarterly, since the asset is meant to run for years.

**Pitfall:** Reporting the piece on pageviews makes a well-shared but badly positioned story look successful. High traffic with near-zero conversions means the pain point is wrong, and no amount of extra promotion fixes it.

**Apply at Pabau:** Pabau's positioning articles should be reported on demo requests attributed to the page, not on sessions. That means the /blog/ conversion tracking has to distinguish landing pages before any paid social spend starts.

**Apply anywhere:** Measure a non-search article on conversions and lead quality only. Rankings do not apply and traffic volume hides a badly chosen pain point, so set up landing-page-level conversion tracking before promoting it.

### 21. Judge conversion pages on closed sales, not opt-in rate  `148.10`
*core · best practices · source 148*

Shour's warning is the most transferable part of the article. When looking at improving conversion, it is easy to look at the top-of-funnel conversion rate and call a winner. What you should do is dig deeper and find out whether those leads convert into sales. His catch-all page has the highest conversion rate of the three and the worst downstream sales rate. He applies the same discipline to his headline number: of the 884 leads the thank you pages generated, only about 18% were qualified, because SnackNation gets many leads from outside the US with North American phone numbers and only ships domestically. He notes a digital product or service would likely see a better lead-to-sale rate than his physical one.

> "the tradeoff has been lower quality leads"

**Evidence:** 884 total leads, about 18% qualified, over 20 closed sales; the highest-converting page produced the lowest sales conversion.

**How to do it**

1. Tag every lead in the CRM with the offer page that produced it.
2. Report three numbers per page: visitors, leads, and leads that reached qualified status.
3. Add a fourth column for closed sales once the sales cycle length has passed.
4. Define what qualified means before you start, for example a servable geography and a real company.
5. Check the geography and company fields for junk before counting a lead at all.
6. Rank pages by qualified leads per visitor, not by raw conversion rate.
7. Kill or rewrite any page whose leads qualify far below the site average.
8. Re-read the ranking each quarter, since sales-cycle lag hides early results.

**Pitfall:** Optimizing to the opt-in rate rewards vague, low-commitment offers that pull in unservable prospects. Shour's own number is 884 leads of which only about 18% were qualified.

**Apply at Pabau:** Pabau's demo requests from blog and template pages should be reported by source page and by qualified rate, filtering out prospects outside served markets, before anyone judges which content converts.

**Apply anywhere:** Report qualified leads and closed sales per offer page, not opt-in rate. The page with the best headline conversion is often the one bringing in prospects you cannot serve.
