# Measurement & GSC — supporting (part 4 of 4)

23 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Separate aspirational topics from tracked ones so ambition is not punished  `85.5`
*useful · best practices · source 85*

Grow and Convert identify the incentive failure that a single visibility percentage creates. Adding prompts for topics you want to win but are not yet visible for mathematically lowers the number. So a team that is being more ambitious reports a worse result, and the rational response is to stop tracking new topics. They call this the exact opposite of good marketing. The fix is structural, not cultural: split the reporting into a current portfolio and an aspirational portfolio, so the aspirational set has its own baseline near zero and its own trajectory, and the team is measured on movement inside it rather than on its effect on the blended average.

> "It encourages marketing teams to be less ambitious"

**Evidence:** Grow and Convert observe teams are incentivized to avoid tracking new prompts because doing so makes their visibility percentage look worse.

**How to do it**

1. Split your tracked topics into two lists, current topics you already compete in and aspirational topics you want to enter.
2. Report each list with its own visibility figure and never blend them.
3. Set the aspirational list's success criterion as movement off zero, for example any topic crossing 10%, not a share of the total.
4. Review the aspirational list quarterly and promote a topic into the current list once it holds a medium band for two consecutive months.
5. Tell leadership up front, in writing, that new aspirational topics start at or near zero by design.
6. Make adding an aspirational topic a routine planning act, not a decision that needs defending.

**Tools:** Peec, Profound, Traqer

**Pitfall:** If the two lists still roll up into one headline percentage anywhere in the report, the disincentive survives. The signal you have it wrong is a team quietly declining to track a topic they say matters.

**Apply at Pabau:** When Pabau expands into a new category page or a new specialty, add its prompts to a separate aspirational tracker from day one so the main GEO number does not drop the month the expansion starts.

**Apply anywhere:** When you expand into a new category, add its prompts to a separate aspirational tracker from day one so your main visibility number does not drop the month the expansion starts.

### 2. Set a 3-6 month ranking expectation and track leads from month one  `181.7`
*useful · concrete actions · source 181*

Grow and Convert give a specific timing frame for SaaS content. For rankings, they tell clients to expect 3 to 6 months before articles reach first-page positions, with faster results on less competitive keywords. For conversions they separate the two clocks: qualified leads can arrive within the first month, either because a low-competition article ranked quickly or because the article was promoted to an existing audience rather than waiting on search. The operational rule that follows is that conversion tracking is set up from day one, so you can see which articles drive results while they are still gaining traction, instead of having no data at the point where the program is first questioned. Promotion to an owned list is the mechanism that produces evidence before rankings exist.

> "expect 3-6 months to see articles reaching first-page positions"

**Evidence:** Grow and Convert quote 3-6 months to first-page positions, with qualified leads possible within the first month via promotion.

**How to do it**

1. Set the ranking expectation with stakeholders at 3-6 months to first page, and note which target keywords are low-competition enough to move faster.
2. Install conversion tracking on the first article, before publication, rather than after the first review cycle.
3. Promote each new article to your email list, social and paid channels in the first month so it can generate leads before it ranks.
4. Report first-month results as promotion-driven conversions, and keep them separate from organic in the reporting.
5. From month three, start reading organic position per article and compare it against the 3-6 month expectation.
6. Do not judge a page's rank in its first two weeks live, since new pages are still being tested.
7. At month six, split articles into ranking-and-converting, ranking-not-converting and not-ranking, and act differently on each group.

**Tools:** Google Search Console, Google Analytics

**Pitfall:** Adding conversion tracking retroactively means the first six months of data are lost, exactly when the program most needs evidence to survive a budget review.

**Apply at Pabau:** David should set the 3-6 month expectation internally for new Pabau blog and template pages, and pair every publish with a promotion push so there is lead data before rankings arrive.

**Apply anywhere:** Tell stakeholders to expect 3-6 months to first page, set up conversion tracking before the first article publishes, and promote each new article so it produces lead data while it is still ranking up.

### 3. Set a breakeven leads-per-month target before publishing content  `111.14`
*useful · concrete actions · source 111*

Grow and Convert summarize their four-step process for measuring content marketing ROI. Define a KPI that aligns with an actual business goal rather than a vanity metric such as organic traffic or overall website traffic. Set up analytics to record that KPI. Calculate the number of leads per month needed to break even on your content spend. Then track progress against that number. The third step is the one most teams skip, and it is what turns content into a budget decision instead of an opinion. They also note that attribution modelling matters separately, because content performance in Google Analytics reads differently depending on the model applied. Their stated diagnosis of B2B content marketing is that companies rarely see measurable ROI and tend not to know how to measure it in the first place.

> "our 4-step process for measuring ROI from content"

**Evidence:** Grow and Convert's four-step ROI process, which they say fixes the common problem of B2B companies not knowing how to measure content ROI.

**How to do it**

1. Choose one KPI tied to revenue: demo requests, trials started or qualified leads. Not sessions.
2. Instrument that KPI in Google Analytics as a conversion, with the landing page recorded.
3. Add your total monthly content spend, including writers, tools and management time.
4. Divide that spend by your lead-to-customer rate and average contract value to get the leads per month needed to break even.
5. Write that breakeven number at the top of the content dashboard before the first article ships.
6. Report conversions by landing page monthly and compare the total against the breakeven number.
7. Compare first-touch and last-touch attribution models, since the two tell different stories about content.
8. Review the breakeven target whenever spend or contract value moves.

**Tools:** Google Analytics

**Pitfall:** Reporting organic traffic because the conversion numbers look small early on. Without the breakeven figure set in advance, there is no way to say whether the program is working or how long to give it.

**Apply at Pabau:** David should compute Pabau's breakeven demo requests per month from the content budget and put that figure on the reporting sheet, then report /blog/ and /templates/ conversions against it instead of sessions.

**Apply anywhere:** Calculate the leads per month your content must produce to break even on its cost, put that number on the dashboard before you publish, and report conversions against it rather than traffic.

### 4. Set the exploration to landing page against total users and conversions  `149.13`
*useful · concrete actions · source 149*

The variables Grow and Convert load into the any-touchpoint exploration. Under Dimensions they search for and import Landing page and query string, First user source and medium, and Session source and medium. Under Metrics they select Total users and Conversions. Then in Tab Settings they double-click or drag the three dimensions into Rows and the two metrics into Values. The pairing of First user source with Session source is the useful part: it lets a single row say both how the user first reached the site and how they arrived in the session where that landing page was the entry point, which is what separates a page that acquired the visitor from a page they returned to.

> "all of which you can find"

**Evidence:** Grow and Convert use exactly these three dimensions and two metrics in the client report they walk through.

**How to do it**

1. In the Variables panel, use the Dimensions search bar to find Landing page + query string.
2. Add First user source / medium and Session source / medium as well, then click Import.
3. Open Metrics and select Total users and Conversions.
4. In Tab Settings, double-click each of the three dimensions to move them to Rows.
5. Double-click Total users and Conversions to move them to Values.
6. Set the date range for the period you are reporting on.
7. Read First user source against Session source per row to tell acquisition from return visits.
8. Exit back to the Exploration reports page; the report saves automatically.

**Tools:** Google Analytics 4

**Pitfall:** Dropping the two source dimensions leaves a landing-page-and-conversions table that cannot distinguish a page that brought a stranger in from one an existing visitor happened to re-enter on.

**Apply at Pabau:** For Pabau this row structure shows whether a template page acquired the practice owner or was just a return entry point after a branded search, which changes how that page is valued.

**Apply anywhere:** Include both first user source and session source in the row set, so acquisition entries are distinguishable from return entries on the same landing page.

### 5. Start with thank-you-page goals before touching attribution models  `151.15`
*useful · best practices · source 151*

Devesh is clear that the advanced attribution work sits on top of a simple foundation most companies never build. The basic method is to create unique thank you pages that are only reachable by signing up, then set Google Analytics goals on visits to those pages, and read the built-in reports to understand conversion rates from different angles. He says he still thinks 75% of businesses doing content marketing could use that simple setup alone to calculate their content marketing ROI and benefit from it. Everything in the model comparison tool depends on those goals existing first. So the sequence is goals, then last-click landing page reporting, then the model comparison tool, and skipping to the last step gives you an empty report.

> "75% of businesses doing content marketing could use it"

**Evidence:** Grow and Convert say most businesses are not measuring conversion rates at all, and that the simple thank-you-page goal setup alone would serve roughly 75% of content marketing teams.

**How to do it**

1. Create a unique thank you page for every conversion type that is only reachable after the action completes.
2. Block those pages from search indexing so they cannot be landed on directly.
3. Create a Google Analytics goal or GA4 conversion event on a pageview of each thank you page.
4. Verify each goal fires by completing the action yourself and checking realtime reporting.
5. Read the landing page report first to get last-click conversion rates per post.
6. Only then open the model comparison tool, which needs those goals to exist to show anything.
7. Keep one goal per conversion type rather than one blended goal, since the attribution report asks you to pick one.

**Tools:** Google Analytics

**Pitfall:** If the thank you page is reachable without converting, direct visits and search traffic inflate the goal and every attribution number built on it is wrong.

**Apply at Pabau:** Pabau should have a distinct, noindexed confirmation page for demo bookings and template downloads, each with its own conversion event, before any per-article reporting is built.

**Apply anywhere:** Set unique noindexed thank you pages with one conversion event each before building any attribution reporting; the models are worthless without clean goals underneath.

### 6. Subtract last from first to size the delayed-conversion gap  `151.4`
*useful · concrete actions · source 151*

Grow and Convert use the gap between the two models as the actual finding. In their worked example the post showed 5 last-click conversions and 13 first-click conversions, which they describe as 8 extra conversions in the first click model, meaning more than double the number who signed up immediately came back and signed up in a later session. That single subtraction answers the question they say the tool exists to answer: are people signing up immediately, or are they coming back multiple times and signing up later? Because the report is per landing page, you get the answer post by post rather than for the blog as a whole, which is what lets you decide what type of content to focus on next.

> "there are 8 extra conversions in the first click model"

**Evidence:** Grow and Convert's example post: 5 same-session conversions against 13 first-click conversions over 90 days, a gap of 8.

**How to do it**

1. Export the model comparison table with first-click and last-click columns per landing page.
2. Add a column for first minus last, the count of conversions that happened in a later session.
3. Add a second column for that difference divided by last click, to size the delay effect proportionally.
4. Sort the table by the difference to find posts whose value is invisible in last-click reporting.
5. Group the high-difference posts by content type and funnel stage.
6. Use the immediate converters and the delayed converters as two separate content briefs, not one blended plan.

**Tools:** Google Analytics

**Pitfall:** Judging a post by last click alone hides posts whose readers all convert in a later session, and those posts then get killed in a content audit for producing nothing.

**Apply at Pabau:** Pabau articles that introduce a category, such as practice management basics, will show almost no last-click demos, so David should judge them on the first minus last gap before pruning them.

**Apply anywhere:** Rank posts by the difference between their first-click and last-click conversions before pruning anything, so delayed converters are not mistaken for dead pages.

### 7. Tag every published post with its funnel stage before measuring anything  `132.9`
*useful · concrete actions · source 132*

The Geekbot analysis only works because every one of the 64 articles was classified as bottom-funnel or top-funnel, and the definitions were fixed in advance. Grow and Convert define bottom-funnel as keywords where there is product-buying intent, where the act of searching means the person is looking for a product right now and no nurturing or product education is needed. Top-funnel is defined as keywords where the act of searching does not necessarily mean the searcher wants to buy. That binary, applied consistently across a two-year archive, is what let them compute 4.78 percent against 0.19 percent. Without the tag, the blog reports one blended conversion rate and the 25x gap is invisible. Build the classification as a permanent field on every brief, not as a one-off audit spreadsheet.

> "we define bottom of funnel as keywords where there's product-buying intent"

**Evidence:** Grow and Convert classified all 64 Geekbot articles as 22 bottom-funnel and 42 top-funnel, which is what produced the 4.78% against 0.19% comparison.

**How to do it**

1. Write the two definitions down: buying intent means the search itself shows the person wants a product now, with no education needed; everything else is top funnel.
2. Add a required funnel-stage field to the content brief template so classification happens at commissioning, not later.
3. Back-classify the existing archive in one pass, one row per URL, using the search intent rather than the page's own tone.
4. Export landing-page sessions and conversions per URL from analytics for a period long enough to include slow pages, ideally 12 months or more.
5. Join the two tables on URL and sum sessions and conversions by funnel stage.
6. Compute conversion rate per stage and the ratio between them, and record the ratio as your own benchmark instead of borrowing 25x.
7. Recompute quarterly and watch whether the bottom-funnel rate is holding as you publish deeper into the long tail.
8. Flag any page whose measured conversion rate contradicts its funnel tag, and re-read the SERP for that keyword to check the classification.

**Tools:** Google Analytics

**Pitfall:** Classifying by how the article is written rather than by what the search means produces a corrupted dataset. A buying-intent keyword written as a general guide is still a bottom-funnel keyword, and tagging it top-funnel hides a fixable content problem.

**Apply at Pabau:** Pabau should add a funnel-stage field to every content brief and back-classify the existing pabau.com archive by URL. Then join it to demo-request data so the blog reports two conversion rates rather than one blended number that hides how the comparison and specialty pages actually perform.

**Apply anywhere:** Tag every article with its funnel stage at commissioning, using the search intent rather than the writing style, then join that tag to landing-page conversion data. Compute your own ratio between the stages instead of borrowing someone else's, and recompute it each quarter.

### 8. Track AI visibility by topic basket, not by a single prompt check  `84.10`
*useful · best practices · source 84*

Grow & Convert describe their tool Traqer as topic-based, meaning it tracks a brand's AI visibility across a topic area rather than a single prompt. For each topic it runs a set of prompts approaching that topic from different angles, for example the topic 'California job training programs' for Climb Hire carrying its own prompt set. Their whole dataset is organized this way: five clients, a set of topics each, 120 prompts underneath, and citation counts rolled up per topic. This matters because a single prompt returns a resampled answer each call, so one check tells you almost nothing. Rolling to topic level is also what let them say clients appeared in 88% of topics, a statement that would be meaningless at prompt level.

> "Traqer.ai is topic-based, meaning it tracks a brand's AI visibility across a topic area"

**Evidence:** Grow & Convert's study is structured as topics per client with prompt sets underneath, producing the 88% of topics figure across five brands.

**How to do it**

1. Define topics that map to buying decisions, not to individual keywords.
2. Write 5 to 10 prompt variations under each topic, approaching it from different angles.
3. Run the full basket against ChatGPT, Perplexity and Google AI Overview on the same schedule.
4. Record brand presence and cited domains at prompt level, then roll up to a topic score.
5. Report visibility as percentage of topics where the brand appears, not as a per-prompt hit rate.
6. Keep the prompt wording fixed between runs so movement reflects the engines, not your edits.
7. Investigate a topic only when its score moves across two consecutive runs.

**Tools:** Traqer, ChatGPT, Perplexity

**Pitfall:** Reporting a single prompt result to stakeholders creates false alarms, because the same prompt returns different citation sets on different calls.

**Apply at Pabau:** Pabau should define topic baskets such as 'clinic booking software' and 'medspa EMR' with several prompt phrasings each, and report the share of topics where Pabau appears.

**Apply anywhere:** Define topic baskets with several prompt phrasings each, run them on a fixed schedule, and report the share of topics where your brand appears rather than single-prompt results.

### 9. Track AI visibility weekly as a metric separate from rankings and leads  `107.14`
*useful · concrete actions · source 107*

Grow and Convert's seventh implementation step is tracking, and they split it into three layers. Leads are tracked in GA4, HubSpot or a tool such as WhatConverts. Rankings are tracked in Ahrefs or Semrush. They then argue those two no longer capture the picture, because AI platforms now handle a meaningful share of buyer research and most analytics tools do not show whether your brand is being recommended in those answers. For clients they track AI visibility separately with Traqer.ai, monitoring brand mentions across the major LLM platforms weekly and showing which topics and queries the brand is cited for. Their point is that without a dedicated measurement, you cannot tell whether your content is doing the AI-visibility work that matters at the buying-decision stage, and no ranking or conversion report will tell you.

> "you have no way of knowing whether your content"

**How to do it**

1. Set up lead tracking in GA4 or HubSpot, or a call and form tracker such as WhatConverts, and confirm blog attribution works.
2. Set up rank tracking in Ahrefs or Semrush for the scored high-intent keyword list.
3. Write a fixed basket of 20 to 40 buying prompts covering your category, competitor comparisons and use cases.
4. Run that basket weekly across ChatGPT, Perplexity and Google AI Overviews, manually or with a monitor such as Traqer.ai.
5. Record whether your brand appears, in what position, and which of your URLs or which third-party source is cited.
6. Report the three layers side by side each month so a rankings gain with no mention gain is visible.
7. Feed the topics where you are never cited back into the content and mention-building plan.

**Tools:** GA4, HubSpot, WhatConverts, Ahrefs, Semrush, Traqer.ai

**Pitfall:** Checking a single prompt occasionally gives a random answer, because outputs vary run to run. A fixed basket run on a fixed weekly schedule is the only way to see a trend.

**Apply at Pabau:** Pabau should keep a standing prompt basket about practice management, clinic booking and named competitor comparisons, run it weekly, and report citation share next to rankings and demo requests.

**Apply anywhere:** Track three layers separately: leads, rankings, and AI mentions from a fixed weekly prompt basket. A rankings gain with no change in citations is a signal you can only see if you measure both.

### 10. Track a fixed keyword set and report the number-one count  `137.15`
*useful · best practices · source 137*

Grow and Convert report Cognitive FX results as a tracked keyword set rather than as total organic keywords. They actively track 204 keywords, most of which they targeted with an individual blog post, and report 66 number-one rankings and 180 first-page rankings out of that set. Alongside it they show the uncontrolled figures for context: Ahrefs indexed keywords rose from 1,700 in February 2019 to 48,500 in February 2023, domain rank doubled, and 1,400 keywords sit in the top three. Reporting a tracked set works because each keyword maps to a deliberate piece of work, so the hit rate is a measure of the strategy rather than of long-tail drift. They are explicit that far more long-tail keywords exist that they do not track.

> "We're actively tracking 204 keywords"

**Evidence:** Cognitive FX: 204 tracked keywords, 66 number-one rankings, 180 first-page rankings; indexed keywords rose from 1,700 to 48,500 and domain rank doubled over four years.

**How to do it**

1. Add every keyword you deliberately target with a page to a rank tracker at the moment you commission the page.
2. Keep the tracked set closed; do not add long-tail terms you never targeted.
3. Report three numbers monthly: tracked keywords, number-one rankings and first-page rankings.
4. Report total indexed keywords and domain rank separately as context, not as the headline.
5. Note in the report when the business adds a new service line, since target keywords shift with it.
6. Review any tracked keyword still off page one after twelve months and decide to refresh, merge or drop it.

**Tools:** Ahrefs

**Pitfall:** Reporting total indexed keywords as the headline hides whether the deliberate work is landing, because long-tail drift inflates the number regardless of strategy.

**Apply at Pabau:** David should keep a closed tracker of the keywords Pabau deliberately targets per article and report number-one and page-one counts from it, with total indexed keywords shown only as background.

**Apply anywhere:** Track only the keywords you deliberately targeted with a page, and headline your reporting with the number-one and first-page counts from that closed set. Show total indexed keywords as context.

### 11. Track every keyword you deliberately target  `22.5`
*useful · best practices · source 22*

The diagnostic behind this whole tactic only works if you're tracking your target keywords over time — the source notes many people starting in SEO don't track their keywords at all. The specific pattern to watch for: a keyword not targeted by any competitor in their URL slugs or page titles, that does appear in yours, isn't especially high-volume, and where your page still isn't indexed — that combination is the signal to try republishing under a new URL.

> "If you are doing SEO where you are deliberately targeting keywords"

**How to do it**

1. Build or maintain a rank-tracking list covering every keyword you deliberately target with a specific page, not just your highest-volume terms.
2. Include easy, low-competition, low-volume keywords in this tracking, since these are the pages most likely to silently fail to index or rank briefly then vanish.
3. Periodically review the tracked list for two patterns: a page never getting indexed despite targeting an easy keyword no competitor targets in slugs/titles, or a page that ranked briefly then dropped out.
4. When you find a page matching either pattern, check its Search Console coverage status ("Crawled/Discovered – currently not indexed" vs. fell out of the index) to confirm it's a candidate for the republish-under-new-URL fix.
5. Treat consistent keyword tracking as the precondition for this diagnostic — without it, these silently-failed pages simply go unnoticed.

**Tools:** Google Search Console

**Pitfall:** Only tracking high-volume or primary keywords and never noticing that easy, low-competition, low-volume keyword pages have silently failed to index or fallen back out — a failure mode beginners especially miss because they "don't even track their keywords."

### 12. Track organic share of total blog traffic as the maturity signal  `141.10`
*useful · best practices · source 141*

Grow and Convert use the ratio of organic sessions to total pageviews to show a content program maturing from promotion-driven to search-driven. On the B2B SaaS client, March 2018 showed 1,652 organic sessions against 7,378 total pageviews, a 22% share. By July 2019 it was 13,845 organic sessions against 20,829 total pageviews, a 66% share. They describe the same shift on the subscription client at the conversion level: in the very beginning most signups come from paid or social, and the longer the engagement runs the more the sources move toward almost entirely organic. The ratio is useful because it separates two things a raw traffic line mixes together. Total traffic can hold flat while the expensive paid share drains out and the compounding organic share replaces it, which is the outcome you actually want.

> "that's 22%. But in the last month on these graphs"

**Evidence:** B2B SaaS client: 1,652 organic on 7,378 total pageviews in March 2018 (22%), rising to 13,845 organic on 20,829 total in July 2019 (66%).

**How to do it**

1. Pull monthly organic sessions and monthly total pageviews for the blog only, not the whole site.
2. Compute organic as a percentage of total for each month and chart the ratio as its own line.
3. Add a second chart doing the same for conversions: organic conversions as a share of all content conversions.
4. Set the expectation at kickoff that the ratio starts low, because paid and community carry the early months.
5. Read a rising ratio at flat total traffic as progress, since the paid share is being replaced by compounding organic.
6. Read a falling ratio as either promotion spend rising or organic stalling, and check which before acting.
7. Review the ratio quarterly rather than monthly, since single months are noisy.

**Tools:** Google Analytics

**Pitfall:** Watching only total traffic hides the composition change, so a program that has successfully swapped paid traffic for organic looks like it did nothing.

**Apply at Pabau:** Add an organic-share line to Pabau's content reporting, split by section, so the /templates/ and /diagnostic-codes/ pages can be shown converting to search-driven traffic over time rather than judged on raw sessions.

**Apply anywhere:** Chart organic sessions as a percentage of total blog traffic each month, and do the same for conversions. A rising share at flat total traffic means compounding organic is replacing paid, which is the outcome you want but the raw traffic line will not show.

### 13. Track overall and homepage conversions as the uplift trend line  `151.13`
*useful · concrete actions · source 151*

Devesh closes with the compensating measurement for everything attribution cannot see. Because cross-device, out-of-window and word-of-mouth conversions all land on generic pages, you should monitor overall conversions including generic pages like the homepage and check that trend is heading upwards as well. If content is working, that untrackable pool grows alongside the attributed pool. He is explicit that if you have been performing well with content for yourself, a client or an employer, you should take some credit for that rise. This gives you a second, cruder KPI that moves with content effort and cannot be dismissed as a modelling choice, since it is a raw count.

> "monitor overall conversions including generic pages"

**Evidence:** Grow and Convert say in every sales call they open by asking how the prospect heard about them, and many answer that they have been following the company since the beginning or joined the email list a year ago.

**How to do it**

1. Chart total site conversions per month for the goal you care about, with no attribution model applied.
2. Chart homepage and other generic-page conversions as a separate series on the same timeline.
3. Overlay content publishing volume or blog sessions on the same chart.
4. Look for the generic-page series rising in the months after content output rises.
5. Report the attributed figure and this untracked trend side by side, with the lag between them noted.
6. Repeat the sales-call question 'how did you hear about us' and tally answers that name content but were not attributed to it.

**Tools:** Google Analytics

**Pitfall:** A rising homepage conversion count also rises with paid brand campaigns and PR, so present it as supporting evidence alongside the attributed number rather than as a content metric on its own.

**Apply at Pabau:** Pabau should log the 'how did you hear about us' answer from every demo call in the CRM and count how many name an article that attribution never credited.

**Apply anywhere:** Chart total and generic-page conversions alongside your attributed figure, and log self-reported sources at signup to capture what no model can see.

### 14. Track rank per article's single target keyword plus a traffic dashboard  `102.14`
*useful · concrete actions · source 102*

Alongside conversions, Grow and Convert measure two more things. They use the Ahrefs rank tracker to monitor rankings progress for each article's target keyword, noting Semrush or Google Search Console would also work. And they build traffic dashboards in Google Data Studio measuring overall pageviews and organic traffic to their articles, with Google Analytics reports as the alternative. The structure matters: rank is tracked per article against the one keyword that article was built for, which only works because they build one page per keyword. That pairing turns rank tracking into a direct check on whether the production process worked for a given brief, rather than a vanity chart of hundreds of unassigned keywords moving around.

> "We use Ahrefs rank tracker to monitor rankings progress"

**Evidence:** Grow and Convert use Ahrefs rank tracker per article target keyword and Data Studio dashboards as their standard reporting stack.

**How to do it**

1. Record the single target keyword on every brief, and add it to the rank tracker on the day the article publishes.
2. Tag each tracked keyword with its article URL so rank can be read per piece, not per site.
3. Build a dashboard in Looker Studio showing pageviews and organic sessions per article over time.
4. Review rank and traffic together monthly, and flag any article that has not moved into the top 20 after three months.
5. Send flagged articles back through SERP analysis to find the coverage gap, rather than publishing something new.
6. Keep the three reports, conversions, rank and traffic, on one review so no metric is read alone.

**Tools:** Ahrefs, Semrush, Google Search Console, Looker Studio, Google Analytics

**Pitfall:** Tracking a large unassigned keyword list. Without a keyword-to-article mapping, rank movement cannot be traced back to a specific brief, so nothing gets fixed.

**Apply at Pabau:** Pabau should map one tracked keyword to each article URL and review rank, traffic and demo requests together each month, flagging any piece still outside the top 20 after three months for a SERP-driven rewrite.

**Apply anywhere:** Track one target keyword per article, tagged to its URL, and pair it with a per-article traffic dashboard. Flag any article outside the top 20 after three months and rework it against the SERP instead of publishing something new.

### 15. Treat a blog-to-signup rate under 0.1 percent as an intent problem  `106.15`
*useful · best practices · source 106*

Grow and Convert give a specific diagnostic number for the volume-first mistake. When a company chases high-volume, low-intent industry topics, the failure shows up in analytics as a minuscule blog-to-signup conversion rate, which they put at under 0.1 percent. That figure matches the 0.19 percent they measured on Geekbot's top-of-funnel articles. The value of the number is that it converts a strategy argument into a measurement. Traffic charts will look healthy while the rate sits there, and no amount of email nurture fixes it, because most of those readers were never in the market. Their framing is that dripping content to an audience cannot create a need for a product where none existed, so the fix is upstream in keyword selection, not in the funnel.

> "a miniscule blog to signup conversion rate in your analytics"

**Evidence:** Grow and Convert cite <0.1% as the analytics signature of low-intent keywords; Geekbot's TOTF cohort measured 0.19% against 4.78% for BOTF.

**How to do it**

1. Set up conversion tracking from blog sessions to signup or demo request, segmented by landing page.
2. Calculate the rate per article, not sitewide, over at least 90 days.
3. Flag every article converting under 0.1 percent as a keyword-selection failure rather than a copy failure.
4. Check each flagged article's target keyword against the top-ten SERP intent scan.
5. Stop commissioning further articles on the topics the flagged pages cover.
6. Redirect the budget to category, comparison and JTBD keywords instead of rewriting the flagged pages first.
7. Recheck the cohort rate a quarter after the new pages publish, expecting the bottom-funnel cohort well above 1 percent.

**Tools:** Google Analytics

**Pitfall:** Reading a low blog conversion rate as a CTA or copy problem and A/B testing the page. If the searcher was never buying, no CTA fixes it.

**Apply at Pabau:** Pabau should measure demo requests per blog article rather than sitewide. Any Pabau article under 0.1 percent is evidence its keyword failed the intent test and should not seed more articles like it.

**Apply anywhere:** Measure signup or enquiry rate per article, not sitewide. Anything under 0.1 percent is a keyword-selection failure, not a CTA problem, and the fix is upstream in which keywords you target.

### 16. Treat attributed content leads as a lower limit, never a total  `137.16`
*useful · best practices · source 137*

Grow and Convert warn that the Cognitive FX numbers, where content drives roughly 50% of all site leads, are a lower limit rather than a total. Anyone who arrives through a blog post and later returns via the homepage on another device, in a different browser, or where a different family member signs up, will not be tracked back to the content. They flag the same issue when showing that a single post produced 4% of homepage-equivalent leads. The practical consequence is that content should not be judged against paid channels on last-click or even first-click attribution alone, because the undercount is structural and larger for high-consideration purchases where the research and the purchase happen weeks apart on different devices.

> "on a different browser, a different family member signs up"

**Evidence:** Grow and Convert report Cognitive FX content at roughly 50% of all site leads and state this is a lower-limit estimate because cross-device and cross-family-member returns go untracked.

**How to do it**

1. Label every content attribution chart as a lower limit in the report itself.
2. Run a first-click model rather than last-click, and state that it still undercounts.
3. Add a 'how did you hear about us' free-text field to the main conversion form.
4. Tag the answers monthly and count how many name an article or the blog without analytics recording it.
5. Use that gap as a rough uplift factor when comparing content to paid channels in budget discussions.
6. Expect the gap to widen the longer and more expensive the buying cycle.

**Tools:** Google Analytics

**Pitfall:** Comparing content to paid on the same attribution model makes content look worse by design, because paid clicks convert in one session and content research spans devices and weeks.

**Apply at Pabau:** Pabau's demo request form should carry a 'how did you hear about us' field, and the monthly content report should show attributed demo requests as a floor plus the count of self-reported article mentions.

**Apply anywhere:** Label content attribution as a lower limit, add a 'how did you hear about us' field to your main form, and use the self-reported answers to size the undercount before comparing content with paid.

### 17. Treat publishing on time as the vanity metric it is  `151.16`
*useful · general insights · source 151*

Benji Hyam's argument, relayed by Devesh, is that most businesses do not measure content conversion rates because of misaligned incentives between content marketers and the company. Getting leads from content is hard, and harder than getting traffic. So it is not in the content marketer's interest to set up conversion tracking or report on it. They would rather report vanity metrics such as whether they published on time, which from the company's perspective is a nonsensical metric. The practical consequence is that the absence of conversion reporting is usually a choice, not a technical gap, and fixing it means changing what the team is judged on before changing the analytics setup.

> "whether they're publishing "on time," which of course"

**Evidence:** Benji Hyam's argument that misaligned incentives, not tooling, explain why most content teams never report conversion rates.

**How to do it**

1. Audit what your content reporting currently leads with: pageviews, publish cadence, or conversions.
2. Replace publish-cadence and traffic headlines with conversions per article as the top line.
3. Set the team's targets on attributed conversions rather than articles shipped per month.
4. Give the team the first-click number so the target is achievable rather than punitive.
5. State publicly that the attributed figure is a floor, so nobody is penalised for untracked leads.
6. Review the metric definition quarterly so it does not drift back to output counting.

**Pitfall:** Switching the team's target to conversions while still reporting only last click sets an unfair bar and pushes people back to defending traffic numbers.

**Apply at Pabau:** David should judge Pabau's content programme on demos attributed per article rather than articles published per month, while reporting first click so the target is fair.

**Apply anywhere:** Judge your content team on conversions per article rather than publishing cadence, and report first-click numbers so the target is fair.

### 18. Treat thank you page goals as last touch and say so out loud  `154.9`
*useful · content insights · source 154*

Grow and Convert are careful to label the model rather than oversell it. The thank you page method assigns each lead to whichever landing page and source brought the visitor in on the converting session, which is last touch attribution. They say the tradeoff is deliberate: multi-touch is more accurate and not simple, so it does not get adopted. The practical rule is to state the model whenever you present the number, so nobody in the room reads a low-converting awareness article as a failure. Top-funnel content that introduces someone who converts three visits later scores zero under this model. That is a known distortion, not a finding, and naming it is what keeps the simple report from causing bad budget cuts.

> "this thank you page method effectively uses last touch attribution"

**Evidence:** Grow and Convert explicitly describe the method as last touch and say multi-touch attribution is not simple, deferring it to a later post.

**Tools:** Google Analytics

**Pitfall:** Presenting last-touch numbers without the caveat leads teams to cut awareness content that was feeding the pipeline, because it shows zero conversions in the report.

**Apply at Pabau:** When David reports which Pabau articles drive demo requests, add a line stating the number is last touch. Top-of-funnel aesthetics guides will show near zero and should not be judged on that alone.

**Apply anywhere:** When you report which articles drive conversions, add a line stating the number is last touch. Top-of-funnel guides will show near zero and should not be judged on that alone.

### 19. Use unique users and a three-step funnel to count content customers  `152.15`
*useful · best practices · source 152*

Grow and Convert specify the units precisely, which is where most homemade CAC models break. Traffic is unique visitors per month, called Users in Google Analytics, not sessions and not pageviews. The visitor-to-lead rate is the percentage of those unique visitors who take a lead action such as filling a sales form, requesting a demo or starting a trial. The third number is the percentage of those leads that convert to paid. Multiply the three and you have customers acquired from blog traffic that month. Using sessions instead of users inflates the denominator and understates the conversion rate; mixing a blog-only traffic figure with a site-wide lead count does the opposite and flatters content. Both errors move CAC by more than any of the levers the model tests.

> "Use unique visitors (in GA, this is now called "Users") per month for traffic"

**Evidence:** Grow and Convert specify unique visitors (GA Users) per month, percent of unique visitors converting to leads, and percent of leads converting to paid.

**How to do it**

1. Pull monthly unique Users for the blog path only, not sessions and not sitewide.
2. Pull the lead count for the same month, filtered to sessions whose landing page was in the blog path.
3. Divide leads by blog Users to get the visitor-to-lead rate.
4. Pull the share of those leads that became paying customers from the CRM, allowing for the sales cycle lag.
5. Multiply Users by both rates to get customers acquired from content.
6. Confirm the numerator and denominator cover the same date range and the same path filter.
7. Document the exact filters in the sheet so the next person reproduces the number.

**Tools:** Google Analytics, GA4

**Pitfall:** Pairing blog-only traffic with a sitewide lead count. It inflates the visitor-to-lead rate and produces a CAC that content cannot actually deliver.

**Apply at Pabau:** When David reports Pabau's content CAC, the traffic and lead figures must both be filtered to the same blog and template paths. A mismatched filter is the most likely reason two reports disagree.

**Apply anywhere:** Filter traffic and leads to the same paths and the same date range, and use unique users rather than sessions. A mismatched filter is the usual cause of two disagreeing CAC reports.

### 20. Validate attribution tracking with an incognito test conversion  `150.6`
*useful · concrete actions · source 150*

Grow and Convert insist on a live test once the Model Comparison Tool is configured, before any number from it is reported. The test is deliberately simple. Open an incognito window so no prior session or cookie interferes, paste the URL of a blog post directly into the address bar, then complete the conversion action on the site. Look at the Model Comparison Tool the next day, because the data is not immediate. If the setup works you will see a last interaction conversion attributed to the URL you used. Only when that appears is conversion tracking for the content program considered set, and only then do they start the breakeven and plotting work. The step exists because a silently broken goal produces a confident zero rather than an error.

> "Simply open up an incognito window"

**Evidence:** Grow and Convert run this incognito test for every client before treating the tracking as complete.

**How to do it**

1. Finish configuring the model comparison report against your conversion goal.
2. Open a fresh incognito or private window so no existing session or cookie is attached.
3. Paste the exact URL of one blog post into the address bar rather than arriving via search.
4. Complete the real conversion action on the site: submit the form, book the demo, start the trial.
5. Wait a full day, since attribution reports do not populate immediately.
6. Open the model comparison report and look for a last interaction conversion on that exact URL.
7. If nothing appears, check the event category and action strings and the goal type before rerunning the test.
8. Repeat the test after any change to the form, the thank-you page or the tracking code.

**Tools:** Google Analytics

**Pitfall:** A broken goal reports zero conversions, not an error, so months of content can look like it produced nothing when the tracking never fired. The signal is a program with rankings and traffic and a flat zero conversion line.

**Apply at Pabau:** Every time Pabau changes the demo booking form or its confirmation page, someone should run one incognito test conversion from a /blog/ URL and confirm it lands in the attribution report the next day.

**Apply anywhere:** After setting up attribution tracking, run one test conversion from an incognito window starting at a blog URL, then check the next day that it appears as a last-interaction conversion on that URL. Repeat after any form or tracking change.

### 21. Validate the framework's scores against your own data, then re-score  `66.6`
*useful · best practices · source 66*

The worksheet ships pre-filled scores for all twenty-one content types, and the framework warns against taking them as fixed. They are a directional starting point to be adapted to your audience, priority prompts, performance and business model, then validated against your actual search, AI visibility and conversion data, and revisited as interfaces and user behavior continue to evolve. The published scores encode assumptions about a generic site; a business whose buyers verify live availability, or whose category is barely covered by AI answers yet, will find its own click-resilience numbers diverge. The framework is therefore a scoring method with a default seed, not a lookup table — and treating it as a lookup table is how a team ends up deprioritizing a content type that is still working for them specifically.

> "validating the scores with your actual search, AI visibility and conversion data"

**How to do it**

1. Start from the worksheet's default score per content type rather than a blank sheet, so the first pass is fast.
2. For click resilience, check reality: compare clicks on your pages whose target queries now show an AI answer against pages whose queries do not, and adjust the score for that content type up or down accordingly.
3. For citation potential, run your priority prompts through the AI interfaces your audience actually uses and record which of your content types get cited or mentioned, rather than assuming.
4. For business value, pull conversions and assisted conversions by content type from analytics, and correct any score that assumed traffic equals value.
5. For proprietary advantage, test it adversarially: ask an AI interface to produce the page and see how close it gets. A close match means the score is too high.
6. Overwrite the default score with your measured one, and note the evidence beside it so the next reviewer can see why it moved.
7. Set a recurring re-score — quarterly is enough for most sites — and treat any large shift in AI-answer coverage of your category as a trigger to re-score early.

**Tools:** Google Search Console, Google Analytics, ChatGPT, Perplexity, Google AI Overviews

**Pitfall:** Adopting the published scores wholesale and calling it an audit. The scores describe a generic site; the whole point of the worksheet is that you replace them with numbers your own search, AI visibility and conversion data support.

**Apply at Pabau:** Seed Pabau's audit with the worksheet's defaults, then correct them with GSC and conversion data before acting — and check the priority prompts in ChatGPT and Google AI Mode to see which Pabau content types actually get cited, since the citation-potential defaults are the least likely to hold for a practice-management category.

**Apply anywhere:** Seed the audit with the worksheet's defaults, then correct them with Search Console and conversion data before acting — and check the priority prompts in the AI interfaces your audience uses to see which of your content types actually get cited, since the citation-potential defaults are the least likely to hold for a specific category.

### 22. Verify the actual cause before reacting to alarming signals  `54.7`
*useful · best practices · source 54*

Glenn's site-owner lessons stress that manual actions can take time to show up in Search Console even when a site is already being impacted in the actual search results, which creates a confusing lag - so the standing discipline is to not make any rash decisions until you actually know what a manual action is for, and are certain you have one at all. The companion habit is to make 'slicing and dicing' Search Console data (by property, then by page, then by query) a default reflex whenever something looks strange, rather than guessing at a cause - in this case that exact discipline is what surfaced the hijacked www homepage instead of the initially-feared AI-content explanation.

> "don't make any rash decisions until you know what"

**How to do it**

1. Adopt a standing rule: never take drastic action (panicking, rewriting content, disavowing links, etc.) based on an alarming signal until you've confirmed exactly what triggered it.
2. Internalize that manual actions can lag behind real-world search impact by many hours, so a sudden de-indexing with no visible manual action yet is 'not yet confirmed,' not 'safe.'
3. As a routine habit, not just during emergencies, periodically open every Google Search Console property for your domain and compare their trend lines against each other.
4. When any property shows a strange surge or drop, make filtering by page, then by query, then by date a default reflex rather than a last resort.
5. Document what you find at each slicing step so you build a clear evidence trail before communicating conclusions to stakeholders or filing anything with Google.
6. Only communicate a definitive diagnosis (to leadership, or to Google via a reconsideration request) once the GSC data has actually pinned down the specific page and cause.

**Tools:** Google Search Console

**Pitfall:** Reacting to an alarming signal before slicing the data down to the actual affected page and query risks fixing the wrong thing entirely - in this case the initial fear was AI-generated content, but systematically slicing GSC data by property, page, and query revealed the real cause was an unrelated hacked subdomain.

### 23. Query counting is named as a distinct SEO impact-tracking method  `06.2`
*context · general insights · source 06*

Among the five pillars listed, one is a named but unexplained technique the source calls query counting, described only as a way to track work and SEO impact, offered as a separate dedicated guide rather than explained inline. Its inclusion as a standalone pillar, alongside more familiar categories like technical compliance and link building, signals it is being treated as a distinct measurement discipline in its own right, separate from standard rank tracking or GSC click and impression reporting, though this source gives no detail on what counting queries actually means in practice or how it differs from existing measurement approaches.

> "How to use query counting to track work/SEO impact"

**Evidence:** The post lists query counting, how to use query counting to track work/SEO impact, as one of six linked guides, and separately restates how to use query counting to maximise SEO impact as one of five core outcome pillars, without defining the technique anywhere in the post itself.

**Apply at Pabau:** Since this is named as a distinct enough discipline to warrant its own dedicated guide from a UK agency claiming a number-one national ranking, it is worth a short independent investigation into what query counting means as a named SEO measurement technique, to check whether it captures something Pabau's current GSC or rank-tracking setup is missing, but nothing here should be treated as understood or actionable until the term is defined by a fuller source.

**Apply anywhere:** Since this is named as a distinct enough discipline to warrant its own dedicated guide from an UK agency claiming a number-one national ranking, it is worth a short independent investigation into what query counting means as a named SEO measurement technique, to check whether it captures something your current GSC or rank-tracking setup is missing, but nothing here should be treated as understood or actionable until the term is defined by a fuller source.
