# Measurement & GSC — core (part 1 of 5)

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. A falling total crawl count after a migration can be a good sign  `03.4`
*core · concrete actions · source 03*

After the CMS migration described in the same case study, total crawl hits per day actually decreased, which the author calls a positive signal rather than a problem, because the decrease came entirely from a non-essential other-file-types segment while crawl requests for the HTML section increased, along with smartphone crawl requests and the ratio of indexable, self-canonicalized HTML URLs supported by internal links. Increasing crawl requests per URL is normally something to pursue because it consistently improves rankings, indexing speed, and crawl delay, and increases the number of query terms a site covers — so the lesson is to read a crawl-stats drop by its composition, not its headline number.

> "total crawl hits per day decreased after the migration"

**How to do it**

1. After any site migration or major technical change, open Google Search Console's Crawl Stats report and compare total daily crawl requests before vs. after.
2. Do not treat an overall decrease in crawl requests as automatically bad; check the breakdown by file type or purpose before drawing a conclusion.
3. Segment the crawl-request change by resource type (HTML pages vs. images/CSS/JS/other file types) using the Crawl Stats breakdown.
4. If the decrease is concentrated in non-essential file types while HTML crawl requests hold steady or increase, treat this as a positive reallocation signal.
5. Check the smartphone (mobile) crawl request trend specifically; an increase here alongside the HTML increase reinforces a healthy reallocation.
6. Cross-check the ratio of indexable HTML URLs that are self-canonicalized, included in the sitemap, and supported by internal links; an increase here is a further positive confirmation.
7. If instead the drop is concentrated in HTML crawl requests, or image/video crawl requests and rankings fall together, treat that as a real problem requiring a redirect/mapping audit. (inferred)

**Tools:** Google Search Console

**Pitfall:** Assuming a drop in total daily crawl requests after a migration is automatically bad — it can be a healthy reallocation away from low-value asset types toward HTML, so the file-type breakdown must be checked before concluding there's a problem.

### 2. AI-driven leads get miscounted as Google Organic traffic  `12.1`
*core · content insights · source 12*

Devesh argues that AI-driven traffic is severely undercounted by standard analytics because most users don't click the citation link inside a ChatGPT response - they see a brand name mentioned, open a new tab, Google that brand name directly, and land on the homepage, which analytics then logs as plain Google Organic traffic. He illustrates this with a real anonymized client: their visible ChatGPT-plus-other-AI sessions were only in the hundreds per month versus 11,000-16,000 monthly sessions from traditional Google Organic, which makes AI search look almost irrelevant by comparison. But he argues the true number hiding inside that Google Organic figure is much larger - if even 1 in 20 people who have this kind of AI conversation subsequently Google the brand and click through, a channel showing 500 visible sessions is really driving roughly 10,000 hidden sessions, and if the click-through ratio is closer to 1 in 50, the number is even higher.

> "They'll open a new tab, Google your brand name, see your homepage"

**Evidence:** Real anonymized client data (early 2025-2026): visible ChatGPT-plus-other-AI sessions in GA4 were only in the hundreds per month versus 11,000-16,000 monthly sessions from traditional Google Organic; Devesh's own math shows a 1-in-20 or 1-in-50 click/re-search ratio implies roughly 10,000 or more hidden AI-driven sessions behind a channel showing only 500 visible sessions.

**Apply:** Don't judge AI search's importance purely from what analytics shows as 'ChatGPT/AI referral traffic' - that number is a severe undercount; treat any noticeable share of new customers mentioning ChatGPT/Claude in sales calls or lead forms as a signal that true AI-influenced traffic is a multiple of what GA4 reports.

### 3. Add an any-click GA segment so influenced conversions are counted  `141.1`
*core · concrete actions · source 141*

Grow and Convert report three attribution views for content, not one. First click and last click come from Google Analytics' model comparison tool. The third came from a reader, Ryan Walters: build a GA segment on the user-interaction condition, set the dropdown from 'first user interaction' to 'any', and filter on users who viewed a blog post. That returns every conversion where a blog post appeared anywhere in the journey, which they call 'any click conversions' internally. The point of running all three is that they answer different questions. First click says content was the first touch. Last click says the conversion followed the post directly. Any click says the blog influenced the deal. Grow and Convert explicitly refuse to ask which model is right, saying the models do not fight each other. Report all three side by side so a client sees the floor, the direct credit and the influence.

> "We've been calling this "any click conversions" internally"

**Evidence:** Grow and Convert use all three models across client engagements and say the combination gives them and clients a holistic picture of blog-driven conversions.

**How to do it**

1. Set a Google Analytics goal on the real conversion action: free trial signup or demo request for SaaS, consultation form for services.
2. Open the model comparison tool and pull first-click and last-click conversions, broken out by landing URL so you see which posts earn them.
3. Build a new GA segment with a blog-post page condition, e.g. page path contains /blog/.
4. In that segment's condition, change the 'first user interaction' dropdown to 'any user interaction'.
5. Apply the segment to the conversion report to get any-click conversions, meaning the user touched a blog post at any point before converting.
6. Report the three numbers together each month and label them first click, last click and any click.
7. Do not average or reconcile them; treat first click as the floor and any click as the influence ceiling.
8. Use the per-URL breakdown to decide which posts get more link building and which formats to repeat.

**Tools:** Google Analytics

**Pitfall:** Reporting only last click, which most default GA reports do, undercounts content badly because posts that started the relationship weeks earlier get no credit at all.

**Apply at Pabau:** David should build the same three views for pabau.com. Set the GA goal on the book-demo request, then segment on /blog/, /templates/, /diagnostic-codes/ and /procedure-codes/ separately with the any-interaction condition, so template and code pages get credit for demos they influenced but did not close.

**Apply anywhere:** Build three attribution views instead of one. Set the analytics goal on your real conversion action, pull first-click and last-click from the model comparison tool broken out by URL, then add a segment using the any-user-interaction condition on your blog path to capture influenced conversions. Report all three together rather than picking a winner.

### 4. Answer the ROI question with four numbers, never a percentage  `150.1`
*core · best practices · source 150*

Grow and Convert say every article that ranks for 'content marketing ROI' hands back the same formula, return minus investment over investment times 100. In five years of running content for over 30 companies, no CMO or CEO has ever asked them for that percentage. What executives actually want is four practical answers: how much business the channel can generate, how long until breakeven, how long until it makes money, and how much total spend it takes to get there. They reframe the first question as an inventory question, how many keywords in the space carry business value, because SEO content keeps producing leads once it ranks in the top half of page one without further spend. The other three are answered by the breakeven math and the conversions chart.

> "has ever asked us for a percentage ROI calculation"

**Evidence:** Grow and Convert ran content for over 30 companies across five years and say not a single executive ever asked for a percentage ROI figure.

**How to do it**

1. Drop the (return - investment) / investment x 100 formula from your reporting deck entirely.
2. Open the report with the count of business-value keywords in the space, so upside has a ceiling attached.
3. State the monthly cost of the content program as one number, including tools and management time.
4. Give the breakeven leads or sales per month, derived from that cost.
5. Give the month you expect to hit breakeven and the cumulative spend to that point.
6. Show a chart of monthly conversions against the breakeven line so progress is visible without commentary.
7. Repeat the same four answers every month so the trough is expected rather than argued about.

**Tools:** Google Analytics

**Pitfall:** Reporting a percentage ROI figure invites arguments about the inputs and answers none of the four questions the person asking actually has. The signal you have hit this is a stakeholder who nods at the number and then asks again next month.

**Apply at Pabau:** Pabau's content reporting should carry four figures: the number of commercial keywords left in aesthetics and healthcare practice management, the monthly content cost, the demos per month needed to break even, and the month breakeven is expected. David should build that as a standing sheet rather than a traffic dashboard.

**Apply anywhere:** Stop reporting percentage ROI for content. Report the size of the commercially useful keyword inventory, the monthly cost, the leads per month needed to break even, and the expected breakeven month, then chart actual conversions against that line.

### 5. Ask a prospective agency for a live client ROI graph over two years  `182.10`
*core · concrete actions · source 182*

Grow and Convert describe the artifact they build for every client: a graph plotting monthly leads from their articles against a horizontal line showing the number of leads that client needs per month to break even on the retainer. They show one from a B2B SaaS client they have worked with for over two years, and say they report progress against the break-even number so the client can see when ROI turns positive. The buyer-side action is to ask for that artifact rather than a case study. A two-year live graph is hard to fake and it forces the agency to state the break-even number, which in turn forces both sides to agree what a lead is and how it is attributed before the engagement starts.

> "the number of leads this client needs per month to break even"

**Evidence:** Grow and Convert show a live graph from a B2B SaaS client of more than two years, plotting monthly MQLs from their articles against the break-even threshold.

**How to do it**

1. Ask each shortlisted agency for a client graph of monthly leads from their content, spanning at least a year, with a break-even line on it.
2. If they cannot produce one, ask what the top metric on their monthly report is instead and treat the answer as the real KPI.
3. Agree the definition of a lead in writing before signing: demo request, trial start or qualified form fill, not newsletter signups.
4. Agree the attribution method, so a lead counts only if the visit touched one of their articles.
5. Compute your own break-even line from the retainer plus your average deal value and close rate.
6. Plot it monthly from month one so the first negative months are expected rather than a surprise.

**Tools:** Google Analytics, HubSpot

**Pitfall:** Without an agreed lead definition the graph inflates itself with low-quality form fills. The signal is a rising lead line while sales report no change in pipeline.

**Apply at Pabau:** David should keep a single chart of monthly demo requests attributed to pabau.com content against the cost of producing it, so the content function is argued on payback rather than sessions.

**Apply anywhere:** Ask any content supplier for a multi-year client graph of monthly leads against a break-even line, and build the same chart for your own content spend.

### 6. Assume analytics undercounts top-funnel conversions through three named gaps  `132.6`
*core · content insights · source 132*

Grow and Convert are careful to state that the same Google Analytics data producing the 25x gap systematically undercounts top-funnel content more than bottom-funnel. They name three limitations. Cross-device: a reader finds the post on a phone, later types the brand URL on a desktop, and the conversion is credited to the homepage. Time gaps over 90 days: Google Analytics uses a 90-day lookback window, so a visitor who converts later has the conversion attributed to an incorrect origin source. Word of mouth: a reader recommends the product to a colleague, or a CMO reads the post and tells an employee to start a trial, and nothing links that back. All three hit top-funnel harder because those pages draw more traffic and their visitors are more likely to convert at a later date. So the measured gap is an upper bound on top-funnel's underperformance, not an exact figure.

> "There are 3 key limitations to measuring how many conversions are brought in from your content"

**Evidence:** Grow and Convert note the 90-day Google Analytics lookback window, and cite their own leads saying 'Oh I've been following you guys for years' with no way to recover their first landing page.

**Tools:** Google Analytics

**Pitfall:** Two failure modes sit either side of this. One is treating the measured number as complete and zeroing the top-funnel budget. The other, which Grow and Convert call out, is using the same limitation as an open-ended excuse for a blog that shows almost no attributable leads at all.

**Apply at Pabau:** Pabau's blog reporting should carry a stated caveat that top-funnel numbers are a floor, and the demo request form should ask how the prospect first heard about Pabau. That free-text answer is the only practical way to recover the cross-device, over-90-day and word-of-mouth conversions the analytics misses.

**Apply anywhere:** Treat measured top-funnel conversions as a floor rather than a full count, because cross-device journeys, the 90-day analytics lookback window and word-of-mouth referrals all clip them. Add a how-did-you-hear-about-us question to your signup or enquiry form to recover some of what attribution drops.

### 7. Benchmark SEO upside against your current total monthly lead count  `129.12`
*core · concrete actions · source 129*

For an established business, Grow and Convert offer a benchmark that needs no keyword tool: compare total monthly leads with the share currently coming from organic rankings. If you get 100 leads a month and barely any come from organic, or you get leads from a couple of high-intent keywords while dozens more sit unranked, they say it is reasonable to estimate another 100-plus leads a month from SEO. The second case is the mature one: if your homepage and product landing pages already rank for the main high-intent terms in your space, but long-tail buying-intent keywords and a decent set of mid- and top-funnel keywords remain, estimate something like a 50% increase in total SEO leads by going after those with the blog. Both are explicitly ballparks, but they anchor the upside in numbers the business already generates rather than in tool estimates.

> "it's pretty reasonable to estimate you could get another 100+ leads per month from SEO"

**Evidence:** Grow and Convert's benchmarks: a business at 100 total leads a month with almost none from organic can reasonably project 100-plus more from SEO; a business whose money pages already rank can project roughly a 50% lift from long-tail and mid-funnel blog content.

**How to do it**

1. Pull total leads per month from your CRM for the last three months and take an average.
2. Segment out how many of those came from organic search, using your attribution setup rather than a guess.
3. Check in Search Console which of your money pages already rank for the main high-intent terms in the category.
4. If organic contributes almost nothing and dozens of high-intent keywords sit unranked, benchmark the upside at roughly your current total lead count again.
5. If your homepage and product pages already own the main terms, benchmark a roughly 50% lift from long-tail and mid-funnel keywords built on the blog.
6. Cross-check that figure against the four-line keyword math; a wide gap means one of the two inputs is wrong.
7. Take the lower of the two figures into the go/no-go decision.

**Tools:** Google Search Console, Google Analytics

**Pitfall:** Assuming near-zero organic leads means near-zero opportunity. It usually means the opposite, but it can also mean your attribution is not crediting organic-sourced leads at all — check the tracking before reading the number as demand.

**Apply at Pabau:** Pabau's money pages already rank for core practice-management terms, which puts it in the mature case. Benchmark the blog, template and code-reference libraries at roughly a 50% lift in organic demo requests rather than a doubling, and hold new page families to that.

**Apply anywhere:** Benchmark SEO upside from your own lead numbers. If organic contributes almost none of your current monthly leads and dozens of high-intent keywords sit unranked, project roughly your current total again. If your money pages already own the main terms, project about a 50% lift from long-tail and mid-funnel content instead.

### 8. Benchmark each post's leads as a percent of homepage leads  `137.4`
*core · best practices · source 137*

Grow and Convert judge a blog post by comparing its leads to the leads the homepage produced in the same period, which gives a scale-free benchmark that works on any site. Their 'what does a concussion headache feel like' post brought 32 leads in its first year, equal to 4% of homepage leads over the same span, for a service costing $9,000 per week of treatment. Their 'multiple concussions' post produced 91 conversions, or 11% of homepage leads. They note many companies' entire blogs do not generate that share of attributable leads, so a single post at 4% is a strong result. The benchmark is useful because it normalizes for site size and seasonality, unlike raw conversion counts.

> "that's equal to 4% of the leads they got from their homepage"

**Evidence:** Cognitive FX: one post produced 32 leads in a year (4% of homepage leads) and another 91 conversions (11% of homepage leads) on a $9,000 service.

**How to do it**

1. Define one conversion event that maps to revenue, such as a consultation request form fill, not a newsletter signup.
2. In your analytics tool, pull first-click conversions for the homepage over a fixed 12-month window.
3. Pull first-click conversions for each blog post over the same window.
4. Divide each post's conversions by the homepage total to get its homepage-percent score.
5. Treat anything at or above 4% of homepage leads as a strong single post and 10%-plus as exceptional.
6. Rank the whole blog by this score and look at what the top posts have in common on intent, not on traffic.
7. Commission the next quarter of topics from that pattern and re-run the report at the next 12-month mark.

**Tools:** Google Analytics

**Pitfall:** Comparing posts on raw conversion counts favors older posts and larger sites, so nobody can tell whether a number is good. Also, first-click attribution undercounts, so a post scoring 3% may be genuinely stronger than it looks.

**Apply at Pabau:** Pabau should report every blog post's demo requests as a percentage of the homepage's demo requests over the same 12 months, and use a 4% threshold to decide which /blog/ topics get sequels and which get retired.

**Apply anywhere:** Score each article's conversions as a percentage of what your homepage produced in the same window. It normalizes for site size, and 4% from one post is already a strong result.

### 9. Bucket your own blog posts by intent and compare conversion rates  `113.2`
*core · concrete actions · source 113*

Rather than argue about funnel stage, Grow and Convert measure it on the client's own site. For Geekbot they analyzed 60-plus posts, split them into posts targeting high buying intent keywords and posts targeting higher-volume lower-intent keywords, and compared conversion rate per bucket. The high-intent bucket converted 2400% better. They ran the same comparison in a smaller analytics screenshot for their Pain Point SEO article, where three boxed posts following the approach produced new user signups hundreds of percent above the rest. Their point is that the conversion-rate gap more than made up for the traffic difference between the buckets, so the comparison has to be run on signups per post, not sessions per post.

> "an analysis of 60+ posts for our client Geekbot"

**Evidence:** Geekbot: 60-plus posts analyzed, high buying intent posts converted 2400% better than higher-volume lower-intent posts.

**How to do it**

1. Export every blog URL with organic sessions and its conversion count for the last 12 months from GA4 or your analytics tool.
2. Label each URL high buying intent or low buying intent based on the keyword it ranks for, using the category, comparison and jobs-to-be-done buckets as the test.
3. Calculate conversion rate per URL, then the average per bucket, so a single outlier post does not carry the result.
4. Also total absolute conversions per bucket, to show whether the high-intent bucket wins despite lower traffic.
5. Present the two bucket averages side by side to stakeholders as the case for reallocating the content budget.
6. Repeat the analysis every two quarters, adding newly published posts, to confirm the gap holds on your site rather than only on the case study.

**Tools:** Google Analytics, Google Search Console

**Pitfall:** Running the comparison on sessions instead of conversions inverts the answer, because the low-intent bucket almost always wins on traffic. Grow and Convert had to show the conversion-rate gap outweighed the traffic gap.

**Apply at Pabau:** David should run this on pabau.com before commissioning the next batch. Split existing posts into buckets, pull demo-request conversions per URL, and put the two averages in the content plan as the justification for weighting toward comparison and alternatives pages.

**Apply anywhere:** Run this analysis on your own site before commissioning more content. Split existing posts by keyword intent, pull conversions per URL, and use the two bucket averages to justify where the next budget goes.

### 10. Build a monthly content CAC model from three cost buckets  `152.1`
*core · concrete actions · source 152*

Grow and Convert's model computes content marketing CAC as total monthly content costs divided by customers acquired that month. They split costs into exactly three buckets: per-article costs (freelance writers, custom graphics, promotion spend per post), salary costs (full-time employees, developer time, or an outside agency retainer), and technology costs (email software, opt-in tools, landing page tools). Everything is expressed monthly because companies budget monthly, software bills monthly, and their other models output traffic per month. Partial attribution is allowed in the salary and software buckets, so a marketing manager who spends half their time on content contributes half their loaded salary. Building it monthly also makes the model comparable to paid-channel CAC, which is already reported that way.

> "I've divided up the cost into three categories"

**Evidence:** Grow and Convert's published spreadsheet model, with worked examples for a self-serve B2C SaaS and a B2B sales business.

**How to do it**

1. Open a spreadsheet with one column per month and rows grouped into per-article, salary and technology costs.
2. Enter per-article costs: freelance writing fee times articles published that month, plus graphics and any promotion spend per article.
3. Enter salary costs: each person's base salary multiplied by 1.3 for benefits and taxes, then multiplied by the percentage of their time spent on content, divided by 12.
4. Add an agency retainer line and a developer-time line as placeholders even if they are zero today.
5. Enter technology costs: email service, opt-in tool, landing page tool, SEO tool, attributing the percentage used for content only.
6. Sum the three buckets into one total monthly content cost cell.
7. Divide that total by customers acquired from content that month to get CAC.
8. Rerun the sheet every month so you have a trend rather than a single snapshot.

**Tools:** Google Sheets, Google Analytics

**Pitfall:** Leaving salary out because it is 'already paid for' understates CAC by an order of magnitude. Grow and Convert found salary is the bulk of content cost, so a model showing a $10 CAC almost always has a missing headcount line.

**Apply at Pabau:** David should build this sheet for the Pabau blog once, with the content headcount, freelance rate and per-article visual cost filled in. Then Pabau can answer 'what does a demo from the blog cost' with a number rather than a traffic chart.

**Apply anywhere:** Build the three-bucket monthly sheet once for your own blog, filling in real headcount, freelance and tooling costs. Then you can answer what a lead from content costs instead of showing a traffic chart.

### 11. Build an any-touchpoint exploration from a two-step sequence segment  `149.12`
*core · concrete actions · source 149*

Grow and Convert's answer to the model comparison tool's blind spot, which is that it credits nothing when a post was viewed mid-journey rather than in the first or last session. In Explore they open a blank report, name it, and add a User segment. They delete the Include users when module, then Add sequence to include, Add new condition, and select Landing page and query string. Add filter, choose matches regex, and paste a regex covering the set of URLs to measure, which for them is every post written for that client. Then Add step for a second step, Add new condition, and pick the conversion event from the Events dropdown. Name and save. The segment is now every user who landed on one of your pages and later converted.

> "Select Add sequence to include"

**Evidence:** Grow and Convert built this specifically because the model comparison report does not credit a post viewed in a session between the first and the last.

**How to do it**

1. Select Explore in the left menu and create a new Blank report.
2. Give it a name under Exploration Name that states the URL set and the conversion event.
3. Add a User segment, not an event or session segment.
4. Delete the 'Include users when' module that appears by default.
5. Click Add sequence to include, then Add new condition.
6. Select Landing page + query string, click Add filter, and choose 'matches regex'.
7. Paste a regex matching the URL set you want to measure and click Apply.
8. Click Add step to add a second sequence step.
9. Click Add new condition and pick your conversion event from the Events dropdown.
10. Name the segment and click Save and apply.
11. Sanity-check the regex against a handful of your URLs before trusting the segment size.

**Tools:** Google Analytics 4

**Pitfall:** A User segment is required; a session-scoped segment collapses the whole point, because the landing and the conversion are usually in different sessions.

**Apply at Pabau:** This is the report that would show whether Pabau's /blog/ and /templates/ pages appear anywhere on the path to a demo, which matters because aesthetic practice buying cycles run over weeks with several people involved.

**Apply anywhere:** Build a user-scoped sequence segment, landed on these URLs then fired this conversion event, to credit content that appears mid-journey rather than only first or last.

### 12. Build the GA4 Model Comparison report for first and last click  `149.8`
*core · concrete actions · source 149*

Grow and Convert's rules-based report, rebuilt from the Universal Analytics workflow they used for years. Advertising in the left menu, then Model Comparison under Attribution. Select the conversion events you want, remembering that all of them are selected by default so you have to uncheck the ones you do not want. Then change the left column from Default Channel Group to Source / medium, and add Landing page and query string with the plus sign. In the third column, headed Attribution model (non-direct), open the dropdown and select First click. Set the date range and apply. The value is definitional clarity: a last-click row means a user landed on that page and converted in that same session, and a first-click row means that page brought the user to the site and they converted within 90 days.

> "Under Attribution, select Model Comparison"

**Evidence:** Grow and Convert say this report gave them a more holistic view of how SEO content contributes to client conversion goals than the Universal Analytics landing pages report most marketers used.

**How to do it**

1. Select Advertising in the left-hand menu.
2. Under Attribution, select Model Comparison.
3. In the conversion event selector, uncheck every event except the ones you want, since all are checked by default.
4. Click Default Channel Group at the top left of the table and set it to Source / medium.
5. Click the plus sign next to Source / medium and add Landing page + query string.
6. Open the dropdown in the third column, Attribution model (non-direct), and select First click.
7. Set the date range you want and click Apply.
8. Read first-click rows as pages that brought the user in and led to a conversion within 90 days.
9. Read last-click rows as pages the user landed on and converted from in that same session.
10. Repeat the read with Last click selected so you hold both views for the same period.

**Tools:** Google Analytics 4

**Pitfall:** Leaving every conversion event checked, which is the default state, mixes scroll and page-view conversions into the table and makes the page-level numbers meaningless.

**Apply at Pabau:** Pabau should run this monthly, filtered to demo-request only, to see which articles bring first-touch visitors who convert within 90 days rather than only crediting the final demo page.

**Apply anywhere:** Run a monthly model comparison report filtered to a single conversion event, so first-touch content credit is visible next to last-click credit.

### 13. Check impression volume before trusting an average-position-one stat  `53.6`
*core · concrete actions · source 53*

A specific Google Search Console trap David Quaid flags: a page can show an average position of 1 while only being credited with a low impression count, his example is 60 impressions, which reads as a clean win, but the real underlying picture can be very different — there may actually be around 6,000 total impressions, with the page briefly spiking to position 1 and then dropping so far down the results that Google stops counting those lower-ranked appearances as impressions at all. In other words, the average-position-1 figure only reflects the narrow window when the page was performing best, silently hiding the much larger volume of impressions earned at worse positions. He connects this to Google separately comparing your click-through rate against other pages' CTR at that position to help decide whether to keep boosting you or throw you back in to lower rankings.

> "an average position of one for, say, 60 impressions"

**How to do it**

1. In Google Search Console, open Performance > Search Results for the page or query in question.
2. Note both the Average Position figure and the total Impressions figure together, never reading average position alone.
3. If average position looks excellent, e.g., near 1, but impressions are low relative to what you'd expect for that query's real search volume, treat that as a red flag rather than a clean win.
4. Break the date range into shorter windows, e.g., day-by-day where available, to check whether position is spiking briefly to 1 and then falling out of counted range, rather than holding steady.
5. Cross-reference with a keyword research tool's actual search-volume estimate for that query to sanity-check whether the impression count you're seeing in GSC seems artificially low.
6. Use the fuller picture, true impression volume plus position volatility, rather than the headline average-position number when deciding whether a page needs more internal-link support.

**Tools:** Google Search Console

**Pitfall:** Reading "average position 1" at face value can hide the fact that the page is actually oscillating wildly, dropping so far down the results at other times that those appearances stop being counted as impressions, so the true, larger impression volume never shows up next to that flattering average.

### 14. Choose the simplest attribution setup an organization will actually use  `154.6`
*core · best practices · source 154*

Grow and Convert's closing argument is that simplicity beats detail when the goal is changing how an organization makes decisions. They give two mechanisms. First, a complicated measurement process reduces the chance the person responsible actually performs it, so the data never gets collected. Second, complication reduces the chance executives understand and believe the numbers, so even collected data does not change decisions. That is why they recommend a last-touch thank you page goal, which they openly admit is a crude model, over multi-touch attribution which is more accurate but rarely maintained. The rule they draw from it: pick the measurement setup that will survive contact with the actual team, and only upgrade once the habit exists. Accuracy that nobody looks at scores zero.

> "simplicity is more important than detail in changing organizational culture"

**Evidence:** Grow and Convert's observation from building content strategies for many companies, backed by their claim that over 90% of the companies they speak to cannot report content-generated leads.

**How to do it**

1. Before building any measurement system, name the specific person who will run it every month and the meeting where the output gets used.
2. Choose the crudest model that answers the actual question, which for content is usually last-touch goal completions by landing page.
3. Time yourself producing the report end to end; if it takes more than 15 minutes a month it will not get produced.
4. Show a draft to one executive and ask them to explain the chart back to you; rewrite it if they cannot.
5. Run the simple version unchanged for a few months so the numbers get quoted in meetings.
6. Only add multi-touch, data-driven or modelled attribution once that habit exists and someone asks a question the simple report cannot answer.
7. Document the model's known blind spot, such as last-touch under-crediting top-funnel content, so nobody mistakes it for truth.

**Tools:** Google Analytics

**Pitfall:** Building a sophisticated attribution model first paralyzes the project: it never gets maintained and executives distrust output they cannot follow, so the company keeps deciding on opinion.

**Apply at Pabau:** David should resist building a full multi-touch model for Pabau before a simple demo-request goal is being read in monthly meetings. Get the one-page channel and landing-page view quoted first, then add complexity.

**Apply anywhere:** Resist building a full multi-touch model before a simple conversion goal is being read in monthly meetings. Get the one-page channel and landing-page view quoted by decision makers first, then add complexity.

### 15. Close the loop: refresh the same articles from Search Console data  `63.4`
*core · ai workflows · source 63*

The refresh half of the workflow, run from the same terminal session. He asks the agent to find the other versus articles on the blog, use the Google Search Console connection to pull the top five versus pages, find the keywords related to those pages, and give him insights on how to optimise them - looking at both the content and the Search Console data together. Alongside that he builds the tracking: select Google Search Console as the data source and prompt for a chart, then add a scorecard for impressions filtered to blog URLs containing 'versus', then add clicks on a secondary axis because the values differ by an order of magnitude. His broader point is that the complaint that this content doesn't work usually reflects people not refreshing it or improving it at all - the publishing step is only half of the loop.

> "improve the content based off of the data"

**How to do it**

1. Connect Search Console as a data source your agent can query.
2. Identify the content campaign you want to track by a URL pattern rather than individually.
3. Ask the agent to pull the top pages in that pattern along with the keywords each ranks for.
4. Ask for optimisation recommendations that consider the page content and the query data together, not either alone.
5. Build a chart of impressions for the URL pattern, then add clicks on a secondary axis since the scales differ hugely.
6. Set a cadence for re-running the same analysis so the loop actually closes.
7. Apply the recommendations as edits and date-stamp them so you can attribute movement.

**Tools:** Claude Code, Google Search Console, Looker Studio

**Prompt / template:**

```text
Use the Search Console data connection and pull the top five versus pages. Find the keywords related to those top five pages and give me insights on how I can optimise those pages so they'll perform better. Look at both the content and the data from Google Search Console.
```

**Pitfall:** Charting impressions and clicks on the same axis makes clicks invisible - he explicitly moves clicks to a secondary axis, which is a small thing that makes the report actually readable.

**Apply:** Pabau's refresh work should be driven by exactly this pairing - the page's own content next to its query data - and reported by URL pattern so a whole content campaign can be judged rather than individual posts.

### 16. Compare funnel cohorts on conversions per article, not on traffic  `95.9`
*core · best practices · source 95*

Matt Goolding cites his colleague Daniel Levi's Geekbot case study, where bottom-of-funnel posts converted 25 times better than top-of-funnel ones. More striking than the rate is the absolute count: bottom-of-funnel content drove 1,348 conversions from 28,000 organic sessions, while top-of-funnel content generated only 397 conversions from 200,000 organic sessions. So the pages with roughly 7 times less traffic produced more than three times the conversions. This is the number Goolding uses to answer the client objection that low volume means low value. The point for reporting is that a traffic-first dashboard makes the top-of-funnel cohort look like the winner and hides the fact that the small pages carry the pipeline.

> "BoF posts converted 25X more than ToF posts"

**Evidence:** Geekbot: 1,348 conversions from 28,000 organic sessions on bottom-of-funnel content versus 397 from 200,000 on top-of-funnel.

**How to do it**

1. Tag every published article in your CMS or sheet as bottom-of-funnel or top-of-funnel at the moment you assign the keyword.
2. Set up landing-page-level conversion tracking so signups, demos and inquiries attach to the entry article.
3. Report each cohort's total sessions, total conversions and conversion rate side by side each month.
4. Report absolute conversions first in the deck, with traffic as a secondary line.
5. Break the bottom-of-funnel cohort down further by reported keyword volume so the sub-20 group is visible.
6. Multiply conversions by trial-to-paid rate and deal value to state each cohort in revenue.
7. Use the cohort table, not tool estimates, to defend the next quarter's low-volume keyword picks.
8. Rebalance the calendar toward whichever cohort produces conversions, not sessions.

**Tools:** Google Analytics

**Pitfall:** Last-click attribution can starve top-of-funnel pages of credit entirely. Report both cohorts and note that the comparison measures directly attributed conversions, not total influence.

**Apply at Pabau:** Pabau's content reporting should split blog performance into bottom-of-funnel pages such as alternatives, pricing and template pages versus general aesthetics guides, and lead with demo requests per cohort. Traffic-led reporting will keep pushing budget toward the pages that convert worst.

**Apply anywhere:** Tag every article by funnel stage and report conversions per cohort alongside traffic. Low-traffic bottom-of-funnel pages routinely out-convert high-traffic guides in absolute numbers, and traffic-led dashboards hide that.

### 17. Compare total conversions, not conversion rate, when defending BOFU content  `105.1`
*core · concrete actions · source 105*

Grow and Convert anticipate the standard objection that top-of-funnel content wins on sheer volume even at a worse conversion rate, and they answer it with the Geekbot data. Across 60+ posts, top-of-funnel pieces pulled nearly 200,000 pageviews while bottom-of-funnel pieces pulled under 50,000, roughly a four-to-one traffic advantage. Despite that, the bottom-of-funnel set produced over three times as many total conversions. The point is that the 4.78% versus 0.19% rate gap is around 25x, which swamps a 4x traffic gap. They argue most teams never run this comparison on their own site, so they keep publishing top-of-funnel because the traffic chart looks better in the monthly report. The fix is to report the two cohorts side by side on absolute conversions.

> "the BOTF content we produced brought in over 3x"

**Evidence:** Geekbot, 60+ posts analyzed by Grow and Convert: TOF near 200k pageviews versus BOTF under 50k, yet BOTF delivered over 3x the conversions; conversion rates 4.78% BOTF versus 0.19% TOF.

**How to do it**

1. Tag every published article in a sheet as bottom-of-funnel or top-of-funnel based on the intent of its target keyword.
2. Pull pageviews per URL for both cohorts over the same date window in GA4.
3. Pull conversion counts per URL for the same window using your primary lead event, not a soft engagement event.
4. Sum pageviews and sum conversions for each cohort separately.
5. Report three numbers per cohort: traffic, conversion rate, and absolute conversions.
6. Check whether the rate gap is larger than the traffic gap; if it is, the low-traffic cohort is your lead engine.
7. Reallocate the next quarter's publishing budget toward the cohort that wins on absolute conversions.
8. Re-run the comparison every quarter so the split stays evidence-led rather than assumed.

**Tools:** Google Analytics 4

**Pitfall:** Teams compare only conversion rates, which executives dismiss as a small-sample artifact on low-traffic pages. Reporting absolute conversions is what ends the argument. The signal you have this wrong is a content calendar dominated by high-volume explainers while the demo pipeline stays flat.

**Apply at Pabau:** David should build one sheet tagging every pabau.com /blog/ and /templates/ URL as bottom- or top-funnel, then report pageviews, conversion rate and absolute demo requests per cohort. If the template and comparison pages beat the general aesthetics explainers on absolute demos, the publishing calendar should shift toward them.

**Apply anywhere:** Tag every published URL as bottom- or top-of-funnel, then report traffic, conversion rate and absolute conversions per cohort side by side. Comparing absolute conversions, not rates, is what settles whether low-traffic buying-intent pages are outperforming your high-traffic explainers.

### 18. Count blog leads with a unique success page and a GA landing page report  `152.3`
*core · concrete actions · source 152*

Grow and Convert's answer to 'how do I know how many leads my blog generates' is deliberately low-tech. Every lead action, whether a sales form, an email signup or a trial start, must send the user to its own unique success, thank-you or onboarding URL. Set that URL as a goal or conversion event in Google Analytics. Then read the Landing Pages report, which attributes each thank-you page hit back to the page the session landed on, and sum the hits whose landing page was a blog URL. They note their own process changed with GA4 and point to their GA4 conversion-tracking tutorial, but the principle is identical: a distinct destination URL per conversion is what makes the attribution readable at all.

> "have a very clear "success" page when a user becomes a lead"

**Evidence:** Grow and Convert show their own GA landing pages report counting thank-you-page hits originating from the blog.

**How to do it**

1. List every lead action on the site: demo request, newsletter signup, trial start, download.
2. Give each one its own unique thank-you URL rather than a shared confirmation modal or one generic /thanks page.
3. Create a GA4 conversion event keyed to a page_view of each of those URLs.
4. Open the Landing Pages report and add the conversion event as a metric column.
5. Filter landing pages to the blog path to isolate conversions that started on content.
6. Sum those conversions to get monthly leads from content.
7. Feed that number into the customers-acquired half of the CAC model.
8. Validate with an incognito test conversion before trusting the first month's data.

**Tools:** Google Analytics, GA4

**Pitfall:** Using one shared thank-you page for every form, or a JavaScript modal with no URL change. The landing page report then cannot separate a demo request from a newsletter signup and the lead count is unusable.

**Apply at Pabau:** Pabau should give the demo request, the template download and any newsletter signup separate thank-you URLs. Without that split, template pages and blog posts cannot be compared on leads generated.

**Apply anywhere:** Give each conversion action its own thank-you URL, set each as a GA4 conversion, and read the landing pages report filtered to your blog path.

### 19. Count product conversions, not content conversions  `103.9`
*core · best practices · source 103*

Grow and Convert open by separating two things most teams report together. A content conversion is an email signup, ebook download, white paper download or webinar registration. A product conversion is a trial start, demo request or account creation. Most SaaS content strategies optimize for the first and assume a meaningful share of those people eventually want the product. Grow and Convert say that assumption very often fails, or holds for only a tiny percentage. They apply this to in-house teams, agencies and freelancers alike. The practical consequence is that a content program reporting healthy lead numbers can be producing almost no revenue, and nobody notices because the reported metric was never the business metric.

> "which, notably, is not the same as a product conversion"

**Evidence:** Grow and Convert state the assumption that content subscribers become product signups very often fails or holds for only a very small percentage.

**How to do it**

1. List every conversion event currently reported on content, and label each one content or product.
2. Pick a single product conversion as the headline metric for the content program.
3. Keep content conversions in the report but move them below the product metric and label them as such.
4. Pull the historical rate at which email subscribers became product signups; if it is under a few percent, stop treating list growth as the goal.
5. Re-score existing articles on the product metric and note which top performers drop out.
6. Rewrite briefs so each piece has a named path to a trial, demo or account, not to a download.
7. Set the breakeven number of product conversions per month for the content spend and report against it.

**Tools:** Google Analytics

**Pitfall:** A content program can hit every lead target and produce no revenue. The signal is a large subscriber list with a conversion-to-product rate nobody has measured.

**Apply at Pabau:** Pabau's content reporting should lead with demo requests per article, with any gated download counted separately. Template pages in particular need the download tracked as a step, not as the outcome.

**Apply anywhere:** Separate content conversions from product conversions in reporting, make a product conversion the headline metric, and measure what share of subscribers ever become customers.

### 20. Create a GA4 conversion event off the thank-you page URL  `149.1`
*core · concrete actions · source 149*

Grow and Convert's exact click path for a GA4 conversion event, written for a form-based lead business. Go to Admin in the bottom left, pick Events in the Property column, then Create event and Create. In the configuration form name the custom event, choose the parameter page_location, pick an operator, and paste the thank-you page URL as the value. Leave the box for copying parameters from the source event checked, save, then toggle Mark as conversion on. They then repeat the registration under Conversions with New conversion event, typing the event name exactly as spelled in the configuration form. Every event they measure is a landing on a post-submission page, which is why page_location does all the work.

> "Fill out the Configuration form"

**Evidence:** Grow and Convert use the event Agency_Lead firing on their own 'Work With Us' thank-you page.

**How to do it**

1. Open GA4, click Admin in the bottom left corner.
2. In the Property column select Events, then Create event, then Create.
3. Name the custom event in the format Agency_Lead or Demo_Signup, underscores between words.
4. Set the Parameter to page_location.
5. Set the Operator, then paste the thank-you page URL into Value.
6. Leave 'Copy parameters from the source event' checked and click Save.
7. Toggle 'Mark as conversion' on in the right-hand column of the new event.
8. Go to Conversions under Events, click New conversion event, and type the event name exactly as created.
9. Toggle 'Mark as conversion' on for that conversion event too.
10. Submit the form yourself and confirm the event fires in GA4 realtime before trusting any report.

**Tools:** Google Analytics 4

**Pitfall:** The name typed under New conversion event must match the custom event name character for character; a mismatch leaves an event that fires but never registers as a conversion, and the report simply shows zero.

**Apply at Pabau:** Pabau should have one GA4 conversion event per real commercial action, fired off the /book-demo/ thank-you URL, before any judgment is made about whether blog or template pages produce demos.

**Apply anywhere:** Set one GA4 conversion event per real commercial action, fired off the post-submission thank-you URL, before judging whether any content type produces leads.

### 21. Define your AI visibility prompt set from your own keyword strategy  `86.12`
*core · concrete actions · source 86*

Grow & Convert's specific complaint about most AI visibility tools is that the tool generates its own prompt list and then reports which prompts you rank for. Those prompts are often random and invented by the tool. You do not know whether anyone types them into ChatGPT, or whether they are even relevant to your business, which means the tool is leading the strategy rather than the other way round. Their stated right order is to decide which topics and keywords matter to the business first, then track visibility for prompts related to those topics. This is why they built Traqer.ai: they start each client by identifying the bottom-of-funnel topics that matter, then track visibility across multiple prompts per topic in ChatGPT, Perplexity and Google AI Overviews, week over week, so they can see what is working and adjust.

> "these prompts are often random and made up by the tool"

**Evidence:** Grow & Convert built Traqer.ai after finding existing tools had too many issues, and run every client on a prompt set derived from that client's bottom-of-funnel topics, measured weekly across three engines.

**How to do it**

1. Start from the bottom-of-funnel keyword list, not from any tool's suggested prompt library.
2. Group the keywords into a handful of topics that map to how you make money.
3. For each topic, write several prompts in the natural phrasing a buyer would type, including the alternatives and comparison forms.
4. Load that prompt set into your tracking tool and turn off or ignore its auto-generated prompts.
5. Run the set weekly in ChatGPT, Perplexity and Google AI Overviews and record presence per prompt.
6. Report movement per topic over time rather than per single prompt, since any one answer is a sample.
7. Add prompts only when the keyword strategy adds a topic, not because the tool suggests them.

**Tools:** Traqer, ChatGPT, Perplexity

**Pitfall:** Auto-generated prompt sets produce a visibility score that moves for reasons unconnected to your business, and teams then chase gaps in queries no buyer asks.

**Apply at Pabau:** Pabau's AI tracking should run on prompts built from the aesthetic and medspa buying questions the sales team hears, tracked weekly, not on whatever prompt list a vendor dashboard generates.

**Apply anywhere:** Run AI tracking on prompts built from the buying questions your sales team actually hears, tracked weekly, not on whatever prompt list a vendor dashboard generates.
