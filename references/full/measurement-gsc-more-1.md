# Measurement & GSC — supporting (part 1 of 4)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Add landing page as a secondary dimension in the default conversions report  `149.7`
*useful · concrete actions · source 149*

GA4 ships a report called Conversion Events by Name under Reports, Life cycle, Engagement, Conversions. Grow and Convert use it as a high-level view only, but they get more from it with two moves. Clicking into an individual event breaks it down by Default channel group, which answers which channels drive the most conversions. Changing that dropdown to Source, Medium or Campaign narrows it further. Then the plus sign at the top right of the left column adds a secondary dimension, and setting that to Landing page and query string gives page plus channel pairs, which they call the second question most marketers want answered. The caveat stays: this report uses whatever the property attribution default is, normally data-driven.

> "see which page + channel pairs are driving"

**Evidence:** Grow and Convert describe the report as a decent high-level view of conversion volume and channel performance, with the accuracy caveat attached.

**How to do it**

1. Open Reports, then Life cycle > Engagement > Conversions.
2. Click into the individual conversion event name you care about, not the summary.
3. Read the Default channel group breakdown first to answer which channels convert.
4. Change the top-left dropdown to Source / medium for a more granular channel view.
5. Click the plus sign at the top right of the left column to add a secondary dimension.
6. Select Landing page + query string to get page plus channel pairs.
7. Set the date range explicitly, and note that the numbers use the property default attribution model.
8. Treat the output as a directional overview and confirm anything decision-grade in a rules-based report.

**Tools:** Google Analytics 4

**Pitfall:** This report inherits the property default attribution model, so a content page that assisted but did not close gets no credit here and looks worthless.

**Apply at Pabau:** For Pabau this is the fastest check of which /blog/ and /templates/ URLs pair with organic to produce demos, but it should never be the report a content decision rests on.

**Apply anywhere:** Use the default GA4 conversions report with a landing-page secondary dimension as a fast directional check, never as the decision report.

### 2. Add multi-touch attribution or your BOFU entry pages get credited to brand  `105.7`
*useful · concrete actions · source 105*

Grow and Convert name a specific measurement failure that makes bottom-of-funnel content look worse than it is. Most blog readers do not convert on the first visit. Someone finds a comparison article through Google, leaves, returns a week later through a branded search, and then books a demo. Under last-click attribution the whole conversion is credited to branded search, and the comparison article that started the sequence records nothing. Teams then cut the content that actually opened the pipeline. Their fix is multi-touch attribution reporting in GA4 so first and assisting touches are visible alongside the closing one. This matters most for exactly the content type they recommend, since comparison and alternatives pages are typically the entry point rather than the closing touch.

> "you'll credit that conversion to branded search and never know"

**Evidence:** Grow and Convert describe the pattern of a reader finding a comparison article via Google, returning a week later via branded search, and converting, with last-click assigning the credit to brand.

**How to do it**

1. Open GA4 Advertising then Attribution and check which model your conversion reports currently use.
2. Switch reporting to a data-driven or position-based model rather than last click for content evaluation.
3. Open the Conversion paths report and filter to your primary lead event.
4. Look for paths that begin with organic search and close with direct or branded organic.
5. Note which landing pages appear as the first touch on those multi-step paths.
6. Credit those pages in the content report even when their last-click conversion count is zero.
7. Keep last-click as a secondary view so paid and brand teams still have their usual number.
8. Re-check quarterly, since path length grows as the content library grows.

**Tools:** Google Analytics 4

**Pitfall:** Running content decisions off last-click attribution systematically defunds first-touch comparison and JTBD pages. The signal is a page with high engaged sessions, strong rankings on a buying-intent term and a recorded conversion count of zero.

**Apply at Pabau:** Pabau's comparison and alternatives articles are likely first-touch rather than closing-touch. David should read them in GA4's conversion paths report, not the last-click table, before deciding any of them are underperforming.

**Apply anywhere:** Switch content evaluation off last-click attribution and read GA4's conversion paths report instead. Comparison and jobs-to-be-done pages are usually the first touch, so last-click hands their credit to branded search and makes them look like failures.

### 3. Agree at kickoff whether the campaign is judged on leads or traffic  `140.13`
*useful · best practices · source 140*

Lewis names this as a client-management decision made before the work started. Different clients have different goals, and this one was not concerned with traffic growth at least in the beginning, only with whether the content brought highly qualified leads. That agreement is what let her choose keywords that drive converting visitors over keywords that drive the most traffic, and she says the leads came much sooner than a volume-led plan would have produced. The reporting consequence is real: her traffic took months to pass a thousand, and she explains that in the write-up by pointing out the niche is narrow and the articles were not the story-driven pieces that spread on social. If the success metric had been traffic, the same campaign would have read as a failure at month three.

> "he was more concerned with how well this new content could bring"

**Evidence:** ADA Compliance Pros traffic took a few months to pass a thousand visits, while blog leads went from zero to 5-15 a month over four months at over $1,000 average order value.

**How to do it**

1. Ask at kickoff whether the client is judging the work on traffic, leads or revenue, and get one answer.
2. If the answer is leads, define the conversion event precisely, such as a submitted email plus website for a free audit.
3. Set up conversion tracking for that event before the first article is published.
4. Warn the client in writing that traffic will look flat for several months on a niche bottom-of-funnel set.
5. Build the monthly report around leads per article, with traffic as a secondary line.
6. Add average order value to the report so a two-lead month is legible as revenue.
7. Revisit the metric only at an agreed checkpoint, not in reaction to a slow traffic month.

**Tools:** Google Analytics

**Pitfall:** An unstated metric defaults to traffic, and a bottom-of-funnel programme then looks like it is failing for its first three months while it is actually working. The signal is a client asking why sessions are flat when leads are arriving.

**Apply at Pabau:** David should report Pabau's bottom-of-funnel comparison and template pages on demo requests, with sessions as a secondary line. A comparison page with low traffic and steady demo requests should not be judged against a high-traffic blog post.

**Apply anywhere:** Settle at kickoff whether the work is judged on traffic, leads or revenue. If it is leads, define the conversion event, instrument it before publishing, and warn stakeholders in writing that traffic will stay flat for months. Report leads per article with order value attached, and traffic underneath.

### 4. Ask 'how did you hear about us' to measure AI  `12.10`
*useful · concrete actions · source 12*

Given that AI search breaks the traditional click-through attribution model, since users often re-Google a brand name after getting an AI recommendation and that shows up as Google Organic, Devesh's recommendation is not to chase a technical attribution fix but to add a direct, simple 'how did you hear about us' question to lead forms, sales conversations, and customer surveys, then watch whether mentions of ChatGPT, Claude, or other AI tools trend upward over time. He frames this self-reported signal explicitly as a workaround rather than a solution, since he considers the underlying attribution problem very difficult to solve and not worth chasing directly with technical fixes. He pairs this with a baseline reminder to at least do the fundamentals well: track traffic-source graphs properly and have some form of conversion attribution in place, since most companies aren't even doing those basics yet.

> "ask in your lead forms, sales conversations, surveys"

**How to do it**

1. Add a 'How did you hear about us?' open-text or multiple-choice field to every lead capture form, checkout flow, and onboarding survey.
2. Add the same question as a standard opening question in sales discovery calls, and have reps log the answer in the CRM.
3. Include a dedicated 'AI tool (ChatGPT, Claude, Gemini, etc.)' option or free-text capture in the answer choices so it's explicitly trackable, not buried in 'other.'
4. Track the percentage of respondents citing an AI tool over time, monthly or quarterly, as a directional proxy metric for GEO impact rather than trying to build precise click-based attribution.
5. In parallel, confirm your analytics setup is correctly capturing traffic-source graphs, such as ChatGPT/AI referral sessions versus Google Organic, as a baseline, since most companies aren't tracking even this yet.
6. Set up whatever conversion-attribution model your team already uses, even a simple one, to connect these traffic sources to actual leads and customers rather than leaving this unmeasured entirely.

**Tools:** Google Analytics (GA4)

**Pitfall:** Don't spend significant effort trying to build a precise, click-based attribution model for AI search traffic - Devesh calls this very difficult to solve and says most companies haven't even nailed the basics yet, so a simple self-reported 'how did you hear about us' trend is a better use of time than chasing an unsolvable measurement problem.

### 5. Assume most companies cannot report content leads at all  `154.7`
*useful · general insights · source 154*

Grow and Convert state that over 90% of the companies they talk to are not at the level of sophisticated attribution, and that most cannot tell them how many leads content generated last quarter. They frame this as an observation rather than a criticism, and it sets the baseline for how they pitch and scope measurement work. The practical consequence is that the first deliverable in most content engagements is not a strategy or a keyword list, it is a working conversion number. Without it, cost per acquired customer cannot be calculated, which they call the most important metric in marketing, since you cannot compute cost per customer when you do not know how many customers were acquired. Treat a missing lead number as the default state of a new client or a new employer, not an edge case.

> "90%+ of companies we talk to are not at this level"

**Evidence:** Grow and Convert report that over 90% of companies they speak to cannot say how many leads content produced last quarter.

**Pitfall:** Assuming a company already tracks content leads because it uses Google Analytics. Analytics being installed says nothing about whether goals exist.

**Apply at Pabau:** If Pabau cannot answer how many demo requests came from blog content last quarter, that number is the first thing to build, ahead of any new article commissioning.

**Apply anywhere:** If you cannot answer how many leads came from blog content last quarter, that number is the first thing to build, ahead of commissioning any new articles.

### 6. Assume your highest-traffic posts are not your highest-converting posts  `90.13`
*useful · content insights · source 90*

Grow and Convert open with a distribution claim worth checking on any blog: most of the traffic comes from two to five posts, and those are usually not the posts producing conversions. The example they show has three highlighted posts generating ten to twenty-five times more signups than the rest, with the very last post in the screenshot producing the most conversions on a tenth of the traffic of the top two. A second client example has the sixteenth highest-traffic article at 1,612 pageviews and 39 product signups. The mechanism is straightforward: head terms have volume because they sit at the top of the funnel, and volume and buying intent trade off against each other. There are keywords with both, and Grow and Convert say they are ideal when you find them, but there are rarely many. The practical consequence is that a traffic report and a conversion report rank the same blog in almost opposite orders.

> "the posts with the highest volume of traffic don't have the highest volume of conversions"

**Evidence:** Grow and Convert's client screenshots: three highlighted posts at 10x to 25x the conversions of the rest, the highest converting post on a tenth of the top posts' traffic, and a sixteenth-ranked article at 1,612 pageviews producing 39 signups.

**How to do it**

1. Build two reports over the same period: organic landing pages by sessions, and the same pages by product conversions.
2. Put them side by side and note how far the top converting page sits down the traffic list.
3. Flag any post in the top five by traffic that is outside the top twenty by conversions.
4. Check what query each flagged post ranks for and whether that query implies buying intent.
5. Look for the inverse case: low-traffic pages high in the conversion list, and generate more keywords in the same shape.
6. Report both lists to stakeholders together so a traffic decline on a non-converting page is not treated as a crisis.
7. Rebuild the pair of reports quarterly so the comparison stays current.

**Tools:** Google Analytics

**Pitfall:** Reporting blog performance on sessions alone makes the top-of-funnel posts look like the site's best assets and hides the low-traffic pages actually producing revenue. The signal is a blog report where the best page has never generated a signup.

**Apply at Pabau:** Pabau's blog reporting should always pair sessions with demo requests per landing page. Expect the pages that drive demos to sit well down the traffic list, and protect them accordingly in any content pruning.

**Apply anywhere:** Build a traffic report and a conversion report over the same period and read them side by side; expect your best converting page to sit well down the traffic list and protect it in any content pruning.

### 7. Attribute conversions per article so traffic is never the only success metric  `133.10`
*useful · best practices · source 133*

Grow and Convert close the Circuit case with attribution as an explicit lesson: measure direct conversions attributed to your content so you are not left with traffic as the only metric of success. They report at the article level using first-click conversions, which is how the /routific-competitors-alternatives page could be defended at 6 conversions from 80 pageviews despite target keywords showing near-zero volume. Without per-article conversion data, that page looks like a failure on every traffic metric and gets cut. They also flag a reporting caveat worth copying: they build these reports in Data Studio using regex on URLs, and the regex sometimes pulls in other pages on the site that match the same pattern, which is why their published numbers ran within 100 sessions of an earlier tweet.

> "Measure direct conversions attributed to your content"

**Evidence:** Grow and Convert report per-article first-click conversions for Circuit, including 6 for the /routific-competitors-alternatives page from 80 pageviews, and note their Data Studio regex sometimes pulled in other matching URLs.

**How to do it**

1. Define the conversion event that matters commercially, such as a trial signup or demo request, not a newsletter subscribe.
2. Set up first-click attribution so a blog post gets credit for a visitor who converts on a later session.
3. Build a report that lists conversions by landing page URL rather than by channel.
4. Match URL patterns with regex, and audit the regex for pages that match by accident before trusting the numbers.
5. Report pageviews, organic pageviews and conversions side by side for each article.
6. Compute conversion rate per article and rank the library by it, not by traffic.
7. Protect high-converting low-traffic pages from any content pruning exercise driven by session counts.
8. Feed the top converters back into the keyword plan as the pattern to produce more of.

**Tools:** Google Analytics, Looker Studio

**Pitfall:** URL regex in the reporting tool silently matching unrelated pages, which inflates the numbers. Grow and Convert saw their own figures shift by up to 100 sessions per month from exactly this.

**Apply at Pabau:** Pabau's content reporting should show demo requests per article URL with first-click attribution, so a low-traffic competitor comparison page that produces demos is visible and protected. Audit the URL regex used for /blog/, /templates/ and code-reference groupings before trusting any grouped total.

**Apply anywhere:** Report conversions per article URL with first-click attribution, not just sessions. Audit the URL regex behind any grouped report, since a loose pattern quietly pulls in unrelated pages and inflates the group.

### 8. Benchmark a B2B content site at 0.4% visitor-to-lead conversion  `173.10`
*useful · general insights · source 173*

Grow and Convert publish KlientBoost's numbers as a usable benchmark. Two years in, the site drew about 50,000 monthly unique visitors and produced 30 to 40 inbound leads a week, around 150 a month, which is a 0.4% conversion rate from visitor to lead. They describe this as good and very achievable for many B2B companies. The second half of the number is the important part: most of those leads are unqualified, and KlientBoost passes only 3 to 4 a week through to an audit. So the funnel is roughly 50,000 visitors to 150 leads to about 15 qualified opportunities a month, and the company held 80 clients on that flow. Planning content volume against a 0.4% lead rate, then a further 10% qualification rate, gives a realistic traffic target for a revenue goal.

> "a 0.4% conversion rate, a good, yet very achievable"

**Evidence:** KlientBoost, two years in: 50,000 monthly uniques, 150 leads a month, 3-4 qualified per week, 80 clients, $300,000 monthly recurring revenue.

**How to do it**

1. Pull last month's unique visitors and inbound leads and compute your own visitor-to-lead rate.
2. Compare it to 0.4% and treat anything far below as a CTA or intent-match problem rather than a traffic problem.
3. Separately compute what share of leads pass qualification, and expect something near 10% for a broad-reach content site.
4. Multiply the two rates to get visitors needed per qualified opportunity.
5. Work backwards from your revenue target and close rate to the monthly traffic that target actually requires.
6. Decide from that number whether to add traffic or to raise conversion, and pick only one to work on this quarter.
7. Re-baseline quarterly, because rising traffic from broader keywords lowers the qualification rate.

**Pitfall:** Optimizing on raw lead count hides a falling qualification rate. If lead volume rises while qualified opportunities stay flat, the new traffic is the wrong traffic.

**Apply at Pabau:** David should track pabau.com's visitor-to-demo rate against 0.4% and, separately, the share of demo requests that clear the practice-size threshold. If blog traffic grows while qualified demos do not, the keyword mix has drifted top-funnel and the fix is more bottom-funnel pages, not more posts.

**Apply anywhere:** Hold your content site to roughly 0.4% visitor-to-lead as a B2B benchmark, then track qualification rate as a separate number. Traffic goals should be derived from both rates and your revenue target, not set independently.

### 9. Bring the channels report to budget meetings as your argument  `154.4`
*useful · concrete actions · source 154*

Grow and Convert make a specific political case for the Acquisition channels report. When someone in a management meeting says the company needs to invest more in social, and you want to argue for SEO content instead, one simple channel table with goal conversion rate per channel changes the outcome of that conversation. Their own report showed organic converting best and social converting worst, with email excluded because most of that traffic was already on the list. They add that the report's credibility comes partly from living inside the company's own Google Analytics rather than in a Tableau dashboard or a custom spreadsheet, which executives discount as marketer-built. The exclusion of email is the part most people skip and it matters, because retargeting an existing list flatters any channel comparison.

> "you're in a management meeting where someone is telling you"

**Evidence:** Grow and Convert's own channels report showed organic converting best and social worst.

**How to do it**

1. Open Acquisition then All Traffic then Channels in Google Analytics.
2. Set the goal selector to your thank you page goal and add goal conversion rate and goal completions as columns.
3. Exclude the email channel from the comparison, or footnote it, because that traffic is already a captured audience.
4. Also exclude direct traffic where it is dominated by returning customers logging in.
5. Use at least a 12-month range so seasonality does not decide the winner.
6. Screenshot the native Google Analytics view rather than rebuilding it in a slide chart, so it reads as the company's own data.
7. Bring the same view to every quarterly planning meeting so the comparison becomes a tracked habit rather than a one-off argument.

**Tools:** Google Analytics

**Pitfall:** Leaving email in the comparison makes email look like the best channel and buries the acquisition channels you are actually deciding between, because most email clicks come from people already converted.

**Apply at Pabau:** David should keep a standing channel conversion view for pabau.com and bring it whenever spend is debated between paid, social and content. Screenshot it from Analytics directly rather than rebuilding it in a deck.

**Apply anywhere:** Keep a standing channel conversion view and bring it whenever spend is debated between paid, social and content. Screenshot it from the analytics tool directly rather than rebuilding it in a deck, since native views carry more credibility with executives.

### 10. Build a custom analytics dashboard for content sign-ups and demos  `131.8`
*useful · concrete actions · source 131*

Grow and Convert say they do this for every client: build a custom dashboard in Google Analytics that tracks conversion metrics from their content specifically. For Smartlook the tracked conversions were free account sign-ups and demo requests, reported as trials, demos and the combined figure. This is what let them report that conversions to their content passed 600 per month within 16 months, and organic traffic to their posts alone passed 18,000 a month, separate from the site's overall numbers. The discipline is scoping the report to the pages the content program produced, so the program is judged on its own output rather than on sitewide totals that include brand traffic and product pages.

> "we created a custom dashboard in Google Analytics"

**Evidence:** The scoped dashboard let Grow and Convert report 600+ monthly conversions in 16 months and 18,000+ monthly organic sessions to their posts alone.

**How to do it**

1. Define the conversion actions that count, such as free account sign-up and demo request, and confirm each fires a distinct event.
2. List the URLs the content program has produced and keep that list updated as new pieces publish.
3. Build a dashboard segment restricted to that URL list as the landing page.
4. Report trials, demos and the combined total as three separate lines so mix shifts are visible.
5. Add organic sessions to the same URL set as a second chart, so traffic and conversions can be read together.
6. Report per-piece conversions monthly and rank the pieces by conversion volume, not by traffic.
7. Use that ranking to decide which keyword types get more budget next quarter.

**Tools:** Google Analytics

**Pitfall:** Reporting sitewide conversions makes the content program unfalsifiable. Brand traffic and product-page sign-ups drown the signal, and you cannot tell which keyword type earns.

**Apply at Pabau:** Pabau should keep a dashboard scoped to the URLs the content program publishes, splitting demo bookings from other conversions, so /blog/ and /templates/ output is judged separately from branded and paid traffic.

**Apply anywhere:** Build a dashboard scoped to the exact URLs your content program has published, tracking each conversion action separately, so the program is judged on its own pages rather than on sitewide totals.

### 11. Build the GA conversion goal as a destination or event goal  `150.5`
*useful · concrete actions · source 150*

Grow and Convert give two goal types they use with clients. A destination goal needs a unique thank-you page that only people who signed up or submitted the form reach, set as the goal URL. An event goal covers cases where you cannot create a unique page: attach a Google Analytics event to a user action such as clicking a form's submit button or completing a trial signup. Creating the event usually needs a developer, because the event snippet goes into the button or form code, so send them the developer-facing event documentation. Events need a category and an action label, named however makes sense; they typically leave label and value blank. In goal setup, choose Custom, name it, choose Event, and type the category and action exactly as the developer implemented them, because the match is case sensitive. Set the event value to equal the goal value, which records a 1 per fire when the event value is blank.

> "type in the category and action exactly as the developer did"

**Evidence:** Grow and Convert set up goals this way for all agency clients.

**How to do it**

1. Decide whether the conversion has a unique confirmation URL; if it does, build a destination goal on that URL.
2. If there is no unique URL, brief a developer to add the analytics event snippet to the submit button or signup completion.
3. Agree the exact category and action strings with the developer in writing before the code ships.
4. Leave the event label and value fields blank unless you have a reason to use them.
5. In analytics goal setup choose Custom, give it a description, and select Event as the goal type.
6. Type the category and action exactly as implemented, matching case character for character.
7. Set 'use the event value as the goal value' to YES so a blank event value records a 1 per conversion.
8. Fire the action yourself once and confirm the goal registers before reporting anything from it.

**Tools:** Google Analytics

**Pitfall:** Category and action strings are case sensitive, so a goal typed as 'Submit' against an event fired as 'submit' silently records zero conversions and the whole ROI report reads as a failure.

**Apply at Pabau:** Pabau's demo booking flow should have a single unique confirmation URL so a destination goal works without developer time, and any in-page booking widget needs an agreed event category and action documented alongside the code reference pages.

**Apply anywhere:** Set your conversion goal as a destination goal on a unique thank-you URL where possible. Where there is no unique URL, have a developer fire an analytics event on the submit action, agree the category and action strings in writing, and match them exactly and case-sensitively in goal setup.

### 12. Build the SEO ROI sheet with inputs, cumulative outputs and three charts  `129.14`
*useful · concrete actions · source 129*

Grow and Convert ship a downloadable spreadsheet with a specific structure, and the structure is the useful part. Inputs are three columns you fill in: value of a lead, estimated monthly spend, and estimated leads generated each month as the program progresses. Outputs are calculated: spend to date, value generated from SEO, net ROI, value generated to date, and net ROI to date. Charts are generated from those columns: ROI per month over time, net ROI to date over time, and spend versus value generated to date. They also include a separate calculator showing how much traffic you would need at different conversion rates to hit a desired number of leads. The numbers in their version are hypothetical placeholders. The point of the build is that the cumulative columns are what show the deficit period closing, which the monthly columns alone never make visible.

> "Columns to input your value of a lead, estimated monthly spend"

**Evidence:** Grow and Convert's published spreadsheet uses three input columns, five output columns including two cumulative ones, three charts and a separate traffic-needed-at-conversion-rate calculator.

**How to do it**

1. Create one row per month for at least 24 months.
2. Add three input columns: value of a lead, monthly spend, and expected leads that month.
3. Ramp the expected-leads column from near zero, with first rankings around months five to ten.
4. Calculate monthly value as leads times lead value, and monthly net ROI as value minus spend.
5. Add cumulative columns for spend to date, value to date and net ROI to date.
6. Chart three views: monthly ROI, cumulative net ROI, and cumulative spend against cumulative value.
7. Add a second tab that solves for the traffic needed to hit a target lead count at 0.5%, 1% and 2% conversion.
8. Replace the projected leads column with actuals each month and let the charts re-draw.

**Tools:** Spreadsheet (Sheets/Excel), Google Sheets

**Pitfall:** Building only the monthly columns. Monthly net ROI turns positive well before the program has repaid its earlier deficit, and reporting that month as success sets an expectation the cumulative line will contradict.

**Apply at Pabau:** Pabau should keep one sheet like this per page family, with the leads column fed from actual demo requests attributed to those URLs. The cumulative net ROI column is the number to bring to a decision about whether to keep commissioning that family.

**Apply anywhere:** Build the ROI sheet with a row per month for 24 months. Three inputs: lead value, monthly spend, expected monthly leads. Outputs including spend to date, value to date and net ROI to date. Chart monthly ROI, cumulative net ROI, and cumulative spend versus value, and add a tab that solves for traffic needed at 0.5%, 1% and 2%.

### 13. Calculate SEO conversion rate per post against three published benchmarks  `142.7`
*useful · best practices · source 142*

Grow and Convert define SEO conversion rate as the share of organic traffic that completes a specific action, such as filling out a contact form or starting a free trial or subscription. The calculation they give is organic conversions divided by organic traffic. They then publish three reference points from their own client work: blog posts targeting high-volume keywords typically convert at 1% or less, the average homepage converts around 3%, and posts ranking for high buying-intent keywords often return 5% or higher. Note the counts in this study are product-related conversions only, meaning free trial starts, demo requests and sales form fills, not newsletter signups or content downloads. That definition matters, because counting content conversions makes a top-of-funnel post look competitive with a bottom-funnel one when it is not.

> "dividing total organic conversions by total organic website traffic"

**Evidence:** Grow and Convert's stated benchmarks: 1% or less for high-volume keyword posts, about 3% for the average homepage, 5% or higher for high buying-intent keywords.

**How to do it**

1. Define one product-related conversion event per site: demo request, trial start or sales form fill.
2. Exclude newsletter signups and content downloads from that event, and track them separately.
3. In GA4, build a report of landing page by organic session and by that single conversion event.
4. Divide conversions by organic sessions for each page to get its SEO conversion rate.
5. Compare each page against the three benchmarks: under 1% is high-volume informational, around 3% is homepage-level, above 5% is buying intent.
6. Flag any bottom-funnel page sitting under 1% for a rewrite or a keyword change.
7. Rerun the report quarterly and track the rate per page over time, not just the site average.

**Tools:** Google Analytics

**Pitfall:** Counting soft conversions such as ebook downloads inflates informational posts and hides the gap. Grow and Convert count only trial starts, demo requests and sales form fills.

**Apply at Pabau:** Pabau's blog reporting should use demo requests only as the conversion event and show a rate per article. Any bottom-funnel article below 1% should go on the rewrite list.

**Apply anywhere:** Report a per-article conversion rate using only your primary sales action as the event, and put any bottom-funnel article below 1% on the rewrite list.

### 14. Cap the team scorecard at five KPIs — and include team satisfaction  `46.e6`
*useful · best practices · source 46 · universal-edition only*

Running an agency-side organization, Tallent measured leadership success on a deliberately short list: revenue, retention, growth, client satisfaction and team satisfaction. Both satisfaction numbers came from quarterly surveys scored one to 10, with eight-plus as the standing target, hit in some quarters and missed in others. His stated principle is that too many KPIs dilute performance and success, so the discipline is refusing to add more rather than building a richer dashboard.

> "I'm a big fan of not overcomplicating KPIs — I think when you have too many KPIs, it really dilutes performance and success."

**How to do it**

1. Write down the smallest set of numbers that would tell you the team is healthy — aim for about five.
2. Include at least one internal measure (team satisfaction), not only client or revenue outcomes.
3. Run the satisfaction measures as a fixed quarterly survey on a one-to-10 scale.
4. Set an explicit target band (eight-plus) and report against it honestly, including the quarters you miss.
5. Refuse additions to the list by default; adding a KPI should require removing one.

**Tools:** Survey tool, Spreadsheet (Sheets/Excel)

**Pitfall:** Letting the KPI list grow because each individual metric seems useful — the stated failure mode is dilution, where nothing on the list actually drives behavior.

### 15. Carry the article count and traffic multiple with the conversion rate split  `121.5`
*useful · content insights · source 121*

Grow and Convert's Geekbot-style analysis of 60-plus articles for one SaaS client is usually quoted as 4.78% conversion on bottom-of-funnel against 0.19% on top-of-funnel, a 2,400% difference. This piece adds the two numbers that make the argument survive pushback. The client had nearly twice as many top-of-funnel articles as bottom-of-funnel ones, and those top-of-funnel articles generated ten times the traffic. Despite both advantages, the bottom-of-funnel articles still brought in three times more conversions. That is the version to use in a meeting, because the standard objection to a conversion-rate comparison is that the high-converting bucket is small. Here the high-converting bucket was smaller on both counts and still won on absolute conversions.

> "nearly twice as many top-of-funnel articles that generated 10x the traffic"

**Evidence:** One SaaS client, 60+ articles analyzed: bottom-funnel 4.78% versus top-funnel 0.19%, with the top-funnel bucket holding roughly twice the articles and 10x the traffic yet producing a third of the conversions.

**Tools:** Google Analytics

**Pitfall:** Presenting only the rate split invites the reply that the bottom-funnel sample is tiny. Without the article counts and the absolute conversion totals the comparison is easy to dismiss.

**Apply at Pabau:** When David defends low-volume Pabau topics internally, pull the same four numbers from GA4 for pabau.com: article count, sessions and conversions per bucket, then the rate. The rate alone will not carry the meeting.

**Apply anywhere:** When you argue for bottom-funnel content, report four numbers per bucket: article count, traffic, absolute conversions and conversion rate. The rate on its own is too easy to dismiss as a small sample.

### 16. Chart branded impressions over time as a standing KPI  `65.4`
*useful · concrete actions · source 65*

The reporting mechanic, which he demonstrates in about a minute. Select Google Search Console as the data source, then prompt for a chart of total impressions over time for queries containing the brand name in quotation marks. That's it - the chart is the KPI, and the job from there is increasing those branded searches through whatever levers you have. The reason he shows the build rather than just asserting the metric is that most teams don't have this chart, and its absence is why unattributable channels don't get credit. He notes it works for any brand: substitute the brand name in the query filter.

> "how to actually track this"

**How to do it**

1. Connect Google Search Console as the data source in your reporting tool.
2. Build a chart of total impressions over time filtered to queries containing your brand name.
3. Put the brand name in quotation marks so it matches as a phrase rather than as loose terms.
4. Include common misspellings and the brand-plus-modifier variants in the filter.
5. Put the chart in the standing internal report rather than pulling it ad hoc.
6. Annotate it with campaign and PR dates so spikes are explicable.

**Tools:** Google Search Console, Looker Studio

**Prompt / template:**

```text
Build a chart showing total impressions over time for queries containing "[brand name]".
```

**Pitfall:** Filtering on the brand name alone misses misspellings and brand-plus-word queries, which for a distinctive brand name can be a substantial share of the total.

**Apply at Pabau:** This chart should exist in Pabau's standing report with misspellings included, annotated with campaign dates - without it, every channel that doesn't produce a click gets no credit at all.

**Apply anywhere:** This chart should exist in your standing report with misspellings included, annotated with campaign dates - without it, every channel that doesn't produce a click gets no credit at all.

### 17. Check AI rankings weekly on a fixed keyword set, not ad hoc  `80.8`
*useful · concrete actions · source 80*

Grow and Convert built Traqer.ai because ad hoc checking does not produce a trend. It is an AI search tracking tool that automatically checks rankings each week across ChatGPT, Perplexity and Gemini, and they use it to keep momentum on the coverage they already have. The point that generalizes is the cadence and the fixed set: the same keywords, the same engines, every week, so a drop is visible as a change rather than as a one-off bad answer. This is consistent with the base's rule that citations are sampled probability, so a single check tells you almost nothing.

> "an AI search tracking tool that automatically checks rankings"

**Evidence:** Grow and Convert built Traqer.ai to check rankings automatically each week across ChatGPT, Perplexity and Gemini.

**How to do it**

1. Fix a list of bottom-funnel keywords and prompts you want to be recommended for, and freeze the wording.
2. Run that list weekly against ChatGPT, Perplexity and Gemini rather than checking whenever someone remembers.
3. Record whether you were mentioned, in what position in the list, and what the model said about you.
4. Store the results with dates so you can read a trend rather than a single sample.
5. Set a review trigger, such as dropping out of a prompt for two consecutive weeks, before you act on any change.
6. When a drop persists, look first at what changed in the third-party sources and listicles the model draws on.
7. Report the coverage percentage alongside Google rank for the same keywords.

**Tools:** Traqer.ai, ChatGPT, Perplexity, Gemini

**Pitfall:** Reacting to one bad answer. Model outputs vary between runs, so a single miss is noise, and a team that chases it rewrites pages that were never the problem.

**Apply at Pabau:** Pabau should keep a frozen prompt list for practice management software queries and check it weekly across the three engines, reporting the percentage alongside Google positions for the same terms.

**Apply anywhere:** Freeze a keyword and prompt list, check it weekly across the major AI engines, log mention and wording each time, and only act when a drop persists over two checks.

### 18. Check indexation with a site: query plus a distinctive phrase from the page  `74.19`
*useful · concrete actions · source 74*

David Quaid gives the fastest indexation check in the walkthrough. Go to Google, type site: followed by your domain, and it returns the pages Google holds from your site. To check one specific page, take a snippet or search phrase from that page and add it to the site: query. Google returns the matching pages ordered by relevance to that phrase. He raises this at the point where the starter guide asks whether Google has found your content, and treats it as the check to run before assuming anything more complicated is wrong. It is deliberately low-tech, and it works without waiting for Search Console's reporting lag or reading a coverage report.

> "you would type in site like primaryposition.com"

**Evidence:** David demonstrates the site: parameter search live during the walkthrough as the way to confirm Google has found a specific page.

**How to do it**

1. Run site:yourdomain.com in Google to confirm the site is indexed at all and see roughly what is held.
2. Copy a distinctive sentence fragment from the specific page, ideally one that appears nowhere else.
3. Search site:yourdomain.com "that exact phrase" in quotes.
4. If the page returns, it is indexed; if not, treat it as an indexing problem and check internal links to it first.
5. Note which URL Google returns for the phrase, since a different URL returning means a cannibalization or canonical issue.
6. Confirm anything ambiguous in GSC URL Inspection, but run the site: check first because it is instant.

**Tools:** Google Search Console

**Pitfall:** Reading site: result counts as an accurate index size. The count is an estimate; use the query to answer yes-or-no on a specific page, not to measure totals.

**Apply at Pabau:** When a new pabau.com article does not appear in GSC, David should run the site: plus exact-phrase check before escalating. If a different Pabau URL returns for the phrase, that is a slug or title collision to fix, not an indexing failure.

**Apply anywhere:** Check a specific page's indexation with site:yourdomain.com plus an exact phrase from the page in quotes, and treat a different URL returning as a cannibalization signal.

### 19. Check lead quality from broad or automated campaigns, not just lead count  `157.15`
*useful · best practices · source 157*

Grow and Convert add a second-order check that most accounts skip. Even when a broad match campaign does appear to produce leads, they say that if you go one step deeper and look at the quality of those leads, there is a high likelihood based on their experience that the leads are not a good fit. This matters because a lead-count dashboard makes loose targeting look successful, and the cost only shows up later in the sales team's time and close rate. The related instruction from the end of the article is to optimize for the metrics that truly matter: total leads and cost per lead. Their framing is that because you pay for every click, you need full control over where spend goes and a metric that reflects revenue rather than activity.

> "if you go one step deeper and look at the quality of these leads"

**Evidence:** Grow and Convert report a high likelihood, from their client experience, that broad match leads are not a good fit even when volume looks healthy.

**How to do it**

1. Tag every paid lead in the CRM with its campaign, ad group and search term.
2. Ask sales to mark each lead qualified or not qualified within a fixed window such as 14 days.
3. Build a report of qualified leads and cost per qualified lead by campaign and ad group.
4. Compare broad match and automated campaigns against phrase and exact campaigns on that qualified rate, not on raw lead count.
5. Pause any campaign whose qualified rate is materially below the account average even if its lead volume is high.
6. Report cost per lead and total leads as the headline paid metrics, with clicks and CPC as diagnostics only.
7. Re-run the quality review monthly so drift is caught early.

**Tools:** Google Ads

**Pitfall:** Reporting on leads without a qualified flag. Loose campaigns then look like the best performers, and the true cost surfaces only as falling close rate months later.

**Apply at Pabau:** Pabau should pass campaign, ad group and search term into the CRM on every demo request, so paid spend can be judged on qualified aesthetic and healthcare practices rather than total form fills.

**Apply anywhere:** Pass campaign, ad group and search term into your CRM on every lead, have sales flag qualification, and judge paid spend on cost per qualified lead rather than lead count.

### 20. Crawling and index-refreshing are separate; use "request indexing" deliberately  `45.8`
*useful · content insights · source 45*

David explains Google runs two distinct crawl modes relevant to migration planning: 'discovery' crawling, which is Google encountering and indexing a URL for the first time, and 'refresh' crawling, which is Google revisiting an already-indexed URL to judge whether it has changed enough, and still carries enough authority, to stay in the index versus being dropped. Critically, a page can be crawled repeatedly (his example: crawled 10 times in 12 months) without ever meeting the bar for an index-refresh, meaning frequent crawling is not the same as the indexed version actually being updated. This is precisely why the manual 'request indexing' button in Google Search Console exists, and David states it should really only be used for exactly this situation: a page you know has meaningfully changed but isn't gaining a natural refresh because it lacks enough authority to trigger one on its own.

> "There are two crawl modes: discovery and refresh."

**Evidence:** David's specific example: a page 'crawled 10 times in the last 12 months but never passed an index-refresh requirement,' used to illustrate that crawl frequency and index-refresh are two separate things Google evaluates independently.

**Apply at Pabau:** David should stop assuming Search Console showing a page as recently crawled means its indexed content has been updated — for lower-authority Pabau pages with meaningful content changes, use the GSC 'request indexing' button deliberately rather than assuming a passive refresh will pick up the change.

**Apply anywhere:** You should stop assuming Search Console showing a page as recently crawled means its indexed content has been updated — for lower-authority your pages with meaningful content changes, use the GSC 'request indexing' button deliberately rather than assuming a passive refresh will pick up the change.

### 21. Cross the how-did-you-find-us answer with CRM deal size  `161.11`
*useful · concrete actions · source 161*

Question one asks how the customer discovered the product. The obvious use is finding which channels acquire users. Khanal adds the step most teams skip: take the channel answers a step further by pulling CRM data to see which channels drove the best customers, measured by deal size and time to close. That turns a volume report into a quality report. A channel can dominate signups and still be the wrong place to spend, because it brings small, slow-closing accounts. Self-reported attribution also catches what analytics misses, since it records the touch the buyer remembers rather than the last click the tracking saw.

> "use data from your CRM to determine which channels"

**Evidence:** Khanal describes using CRM data to determine which channels drove the best customers in terms of deal size and time to close.

**How to do it**

1. Ask 'How did you discover X?' as an open text field, not a dropdown, so people name the podcast or person.
2. Normalize the free-text answers into channels in a sheet, keeping the raw wording in a second column.
3. Match each respondent back to their CRM record by email.
4. Add deal size, time to close and current status to each row.
5. Calculate average deal size and average days to close per channel.
6. Compare that ranking against your analytics channel report and note where they disagree.
7. Shift budget toward the channels with the best deal size and close speed, not the highest signup count.
8. Keep the raw wording column and mine it for named publications, communities and people worth pitching.

**Tools:** Survey Monkey

**Prompt / template:**

```text
How did you discover (Product or Company Name)?
```

**Pitfall:** Ranking channels by response count alone. The cheapest channel usually wins on volume and loses badly on deal size, and you only see that once CRM values are joined on.

**Apply at Pabau:** Pabau should add a free-text 'how did you hear about us' field to demo bookings and join the answers to deal value in the CRM, so content and paid budget follow the channels that bring multi-location practices rather than single rooms.

**Apply anywhere:** Ask how customers found you in free text, join the answers to CRM deal size and close time, and rank channels by quality rather than signup volume.

### 22. Discount about 10% of AI citations as broken before reporting  `87.10`
*useful · best practices · source 87*

Grow and Convert found roughly 10% of citations in their dataset led to error pages. They note recent academic work puts the number higher, with a February 2026 study reporting hallucination rates above 14% for cited sources and an earlier 2023 Nature paper documenting similar patterns. These are plausible URLs with plausible titles pointing at pages that do not exist. Any citation-share report that counts raw citations without resolving them is inflated by this margin, and the inflation is not evenly spread. Checking status codes on every cited URL is cheap and turns a soft number into a defensible one.

> "roughly 10% of citations led to error pages"

**Evidence:** ~10% error-page rate in Grow and Convert's data; >14% hallucination rate in a February 2026 study.

**How to do it**

1. Export every cited URL from your prompt basket run.
2. Request each URL and record the HTTP status code.
3. Drop anything returning 404 or 410 from the citation count.
4. Report both the raw count and the resolving count, with the discard rate stated.
5. Track the discard rate over time; a rising rate means the engine is leaning harder on memory.
6. Check whether any hallucinated URLs point at plausible paths on your own domain, and build those pages if the intent is real.

**Pitfall:** Reporting raw citation counts to stakeholders. Roughly one in ten is a dead link, and the number is higher in some published studies.

**Apply at Pabau:** If Pabau tracks AI citations, resolve every cited URL before counting it, and check whether hallucinated pabau.com URLs suggest pages worth building.

**Apply anywhere:** Resolve every cited URL before counting it. About one in ten AI citations points at a page that does not exist.

### 23. Exclude pure brand advertising content from the CAC model  `152.13`
*useful · best practices · source 152*

Grow and Convert draw a hard boundary on where the model applies. If content is used only as a brand-building endeavor, the model is not for you, and their example is Pepsi trying to attribute sales to advertising boards in soccer stadiums. They note it is not impossible to measure, but it needs much more complex experiments such as geographic holdouts, not a spreadsheet. Everything else, meaning content with an identifiable conversion action on or after the page, should be modeled with last click. The practical use of this boundary is defensive: it stops a team from being asked to produce a CAC for material that was never intended to convert, and it stops brand-only content from dragging down the measured CAC of content that does convert.

> "if content is only used as a "brand building" endeavor"

**Evidence:** Grow and Convert use the Pepsi stadium advertising board as the boundary case where CAC cannot be modeled simply.

**How to do it**

1. Tag every content page as conversion-oriented or brand-only before running the model.
2. Define brand-only strictly: no conversion action on the page and no funnel it feeds.
3. Exclude brand-only pages and their production costs from both sides of the CAC calculation.
4. Report brand-only content separately on reach and mention metrics, not on CAC.
5. If leadership demands attribution for brand content, propose a geographic or time-based holdout test instead of a spreadsheet.
6. Review the tagging quarterly, since brand pages often gain a CTA and move into the modeled set.

**Pitfall:** Leaving brand-only pages in the denominator's cost side while they contribute nothing to the numerator of leads. Measured CAC then rises for reasons that have nothing to do with the converting content.

**Apply at Pabau:** Pabau's thought-leadership and industry-commentary posts should be excluded from the content CAC sheet and reported on reach instead. Template pages and comparison pages carry the CAC number.

**Apply anywhere:** Exclude genuinely brand-only content from your CAC sheet and report it on reach instead. Let the pages with real conversion actions carry the acquisition-cost number.

### 24. Expect GSC to miss the queries actually driving a long-tail page  `95.15`
*useful · content insights · source 95*

Checking why Grow and Convert's 'landing page vs blog post' page earns over 100 organic sessions a month against a 10-search keyword, Matt Goolding found Google Search Console showed no queries delivering clicks to that page over three months. The queries GSC did list were terms like 'landing page' and 'blog vs landing page'. His explanation is that the traffic comes from extremely long-tail searches that are not in any SEO tool's database and are largely filtered out of GSC's reporting as well. This matters for diagnosis: a page with real analytics sessions and an empty GSC query list is not necessarily broken. It is usually a long-tail page whose demand is spread across hundreds of unique phrasings, each too rare to survive GSC's anonymization threshold.

> "aren't in the database of the SEO tool you're using"

**Evidence:** Grow and Convert's page took 138 organic sessions in May while GSC showed no queries producing clicks over the prior three months.

**Tools:** Google Search Console, Google Analytics

**Pitfall:** Concluding a page has a targeting problem because GSC shows few clicked queries. Check analytics sessions first; if the sessions are real, the page is working and GSC is simply hiding a wide, thin query spread.

**Apply at Pabau:** When auditing Pabau pages, cross-check GSC against analytics before declaring a page a failure. Narrow template and code-reference pages will often show almost nothing in GSC while still pulling steady sessions and demo requests.

**Apply anywhere:** A page can pull real organic sessions while Search Console shows almost no clicked queries. Check analytics before diagnosing a targeting problem, because long-tail demand is spread too thin for GSC to report.

### 25. Expect a cookie to fail whenever the reader changes device  `151.14`
*useful · content insights · source 151*

Devesh explains the mechanism behind first-click attribution so the failure mode is obvious. Google Analytics knows you visited two months ago because it placed a cookie in your browser; when you return, even after closing the browser and after weeks or months, the cookie identifies you as the same user. That is the entire basis on which the first-click report works. It breaks the moment two devices are involved: a user reads a post on their phone, likes the company, gets to work, opens the homepage on desktop and converts. The cookie on the phone and the session on the desktop are unconnected, so the conversion is credited to the homepage. The undercount is structural, not a configuration error, and it is worst where reading and buying happen in different places.

> "They used two separate devices!"

**Evidence:** Grow and Convert walk through the phone-read to desktop-convert path and show the conversion landing on the homepage instead of the post.

**How to do it**

1. Check your analytics device report for the split between mobile sessions and desktop conversions.
2. Assume any topic read predominantly on mobile but converted on desktop is being credited to the homepage.
3. Do not attempt to fix this with a longer lookback window; the window is not the constraint here.
4. Implement logged-in or user-ID based tracking if a real cross-device identity is available.
5. Otherwise add a self-reported source field and treat its answers as the cross-device correction.
6. State the cross-device loss in the report so the attributed figure is understood as a floor.

**Tools:** Google Analytics

**Pitfall:** Chasing a configuration fix for cross-device loss wastes time; without a logged-in user identity there is nothing in cookie-based analytics that can join the two sessions.

**Apply at Pabau:** Practice owners often read Pabau articles on a phone between appointments and book a demo later on a clinic desktop, so David should assume Pabau's mobile-read articles are structurally undercredited.

**Apply anywhere:** Assume articles read on mobile and converted on desktop are credited to your homepage, and correct for it with self-reported source data rather than analytics settings.
