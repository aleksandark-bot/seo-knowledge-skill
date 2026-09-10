# Measurement & GSC — core (part 5 of 5)

18 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Start with last-click attribution and call the result an upper limit  `152.4`
*core · best practices · source 152*

The standard objection to measuring content CAC is that content assists conversions over months or years and last click undercounts it. Grow and Convert's answer is to use last click anyway, count anyone who signs up from a blog post as a lead, and be explicit that the resulting CAC is an upper limit. They concede the two gaps openly: it gives no credit for someone who first found you through a post and converted later elsewhere, and none for credibility built by posts emailed over time. Their argument is that a defensible upper limit beats the zero insight most companies have. They also give the meeting line to use: CAC is even lower than this, because I am not counting the other ways content generates sales. The one exception they name is content used purely as brand advertising, like a Pepsi stadium board, where this model does not apply.

> "you are computing an upper limit to content marketing's CAC"

**Evidence:** Grow and Convert frame the last-click figure as an upper limit and supply the meeting argument for it.

**How to do it**

1. Set last-click attribution as the model for the first version of the CAC calculation.
2. Count only leads whose landing page was a blog URL, ignoring assisted paths for now.
3. Label the output clearly in the sheet as an upper-limit CAC.
4. Write the one-line caveat into the reporting deck: assisted and brand-driven conversions are excluded.
5. Bring the upper-limit framing to the budget meeting rather than defending the model's gaps.
6. Once the upper limit is accepted, add a multi-touch or time-lag report as a second view to close the gap.
7. Exclude content that is genuinely pure brand advertising from the model instead of forcing a number on it.

**Tools:** Google Analytics

**Pitfall:** Refusing to publish any number until attribution is perfect. The team then reports open rates and follower counts, and the CEO reasonably concludes content is unmeasured.

**Apply at Pabau:** David should publish Pabau's content CAC as an upper limit rather than waiting for full multi-touch attribution. Labeling it that way makes the number safe to defend in a budget conversation.

**Apply anywhere:** Publish a last-click content CAC labeled as an upper limit rather than waiting for perfect attribution, and say plainly that assisted conversions are excluded.

### 2. Stop counting email subscribers as leads in your reporting  `147.6`
*core · best practices · source 147*

Grow and Convert draw a hard definitional line. An email subscriber has expressed interest in your content; a lead has expressed interest in your product or service, which means a trial start, a demo request, or a conversation with a sales rep. They say the difference is big and that most reporting blurs it. The blur has a specific measurement consequence they call out: most companies do not know whether a given person became a lead first or a subscriber first, so they cannot tell whether the nurture emails converted anyone or simply mailed people who had already converted. Until the CRM and analytics record the order of those two events, any claimed email-to-lead rate is unverifiable, and the whole nurture-versus-direct comparison rests on a number nobody actually has.

> "they've expressed interest in your content, but not in your product"

**Evidence:** Grow and Convert note most companies cannot tell whether the prospect became a lead first or a subscriber first.

**How to do it**

1. Define lead in your analytics as a product action only: trial start, demo request, or booked sales call.
2. Move email subscription to a separate engagement event so it never counts in the lead total.
3. Record a timestamp on both events per person in the CRM.
4. Build a report that segments email-sourced leads by whether the subscription timestamp precedes the lead timestamp.
5. Exclude anyone who was already a lead when they subscribed from the email-to-lead rate.
6. Re-report historic email-attributed leads with that exclusion applied before anyone defends the nurture budget.
7. Set the primary content goal on the product action, and report subscriber growth separately as a secondary metric.

**Pitfall:** Reporting a healthy email-to-lead rate that is mostly existing customers and existing leads who happened to subscribe. The signal is a nurture rate that looks strong while sales cannot name a customer sourced from the list.

**Apply at Pabau:** In Pabau's reporting, the blog goal should be demo requests, with newsletter signups tracked as a separate event. David should also check the order of the two timestamps before crediting any demo to the newsletter.

**Apply anywhere:** Set your content goal on the product action, track list signups as a separate event, and check the order of the two timestamps before crediting any lead to your newsletter.

### 3. Stop forecasting traffic by multiplying volume by a CTR curve  `129.4`
*core · best practices · source 129*

Grow and Convert single out the standard bottom-up forecast as the reason teams underestimate SEO. The pattern they name is: 1,000 searches a month, rank one, take 30% of clicks, forecast 300 pageviews. They say this severely underestimates traffic, and give their own data. Devesh Khanal reported ranking seventh for 'seo content writing', which Ahrefs showed at 90 searches a month. At position seven a 4% click share implies 3.6 clicks a month. The page actually got around 100 organic pageviews in February, roughly five times the bottom-up estimate. Their replacement rule of thumb is order-of-magnitude: rank highly for keywords with hundreds of monthly searches and expect hundreds of monthly pageviews from each; rank for thousands and expect thousands. The mechanism is that a ranking page collects long-tail and related queries the tool never attributed to the head term.

> "don't do this typical granular calculation"

**Evidence:** Devesh Khanal: ranking #7 for 'seo content writing' at an Ahrefs volume of 90/month implied 3.6 clicks a month at a 4% CTR, but the page drew around 100 organic pageviews in February 2023 — about five times the estimate.

**How to do it**

1. Drop CTR-curve multiplication from any SEO forecast you present.
2. Sum the reported monthly volume of the keywords you intend to rank for.
3. Forecast pageviews at roughly the same order of magnitude as that volume, not a fraction of it.
4. Sanity-check the rule against your own site: pick three pages ranking in the top ten and compare actual pageviews with the head term's reported volume.
5. Record the ratio you observe and use your own multiple in future forecasts.
6. Keep the forecast as a range, and label it a go/no-go input rather than a revenue projection.
7. Re-verify after your first five to ten ranked pages and replace the rule of thumb with measured data.

**Tools:** Ahrefs, Google Search Console, Google Analytics

**Pitfall:** The forecast becomes so small that SEO fails its own business case, and the channel gets rejected on arithmetic rather than evidence. The signal you have hit it is a model where every page is worth a few clicks a month.

**Apply at Pabau:** When Pabau builds the business case for a page family, forecast pageviews at the order of magnitude of summed keyword volume, and verify it against existing Pabau pages in Search Console. Template and code-reference pages in particular pick up long-tail variants that no tool attributes to the head term.

**Apply anywhere:** Do not multiply search volume by a click-through curve to forecast traffic. That method understated one measured case by about five times. Forecast pageviews at roughly the same order of magnitude as the summed volume of your target keywords, then calibrate with the actual ratio on three of your own top-ten pages.

### 4. Stop using the Landing Pages report to credit blog conversions  `150.4`
*core · concrete actions · source 150*

Grow and Convert say the instinct most marketers have, and the way most blogs explain it, is to read content conversions from Behavior > Site Content > Landing Pages in Google Analytics. That report is insufficient because it only counts conversions where the user landed on the blog post at the start of a session and converted inside that same session. If your post ranks for 'best X software', someone reads it, then returns days or weeks later and converts, the post gets no credit. For most products a fraction of customers need multiple touches and sessions before converting, and getting credit across sessions is exactly what content is supposed to do. Their fix is Google's Model Comparison Tool, which attributes the conversion back to the first session's landing page.

> "it only measures conversions where a user lands on a blog post"

**Evidence:** Grow and Convert use the Model Comparison Tool for every agency client rather than the Landing Pages report.

**How to do it**

1. Open Behavior > Site Content > Landing Pages and note the conversion figure it gives for blog URLs.
2. Treat that number as a floor, not the result, because it excludes every multi-session path.
3. Switch to the Model Comparison Tool for the same goal and date range.
4. Compare first interaction against last interaction attribution for the same blog URLs.
5. Report both numbers, since first click shows what content introduced and last click shows what closed.
6. Expect the gap to widen with longer sales cycles and higher price points.
7. Use the first-click figure when defending content budget, since same-session conversion undercounts it.

**Tools:** Google Analytics

**Pitfall:** Same-session-only reporting makes content look worse the longer your sales cycle is, so the highest-value B2B programs are the ones most likely to be defunded on bad data.

**Apply at Pabau:** Pabau's buying cycle for practice management software runs across weeks, so same-session attribution will badly understate what /blog/ and /templates/ pages contribute. David should report first-click and last-click demo conversions side by side for blog URLs.

**Apply anywhere:** Do not judge blog conversions from the Landing Pages report, which only counts same-session conversions. Use an attribution model comparison and report first-click alongside last-click for blog URLs.

### 5. Switch off GA4's default events as conversions before reading counts  `149.4`
*core · concrete actions · source 149*

GA4 arrives with automatically collected events such as page_view, scroll and click, and any of them left flagged as conversions get counted in the Conversions column of every report. Grow and Convert show what this does: in their client exploration, 42 users produced 228 conversion events, and 10 users in a single table row produced 34, because the client had a large number of events marked as conversions. The column then tells you nothing about the action you care about. Their fix is to go to Admin, then Events under the Property column, and turn the conversion toggle off for everything except the events you actually want counted. Do this before you build reports, not after.

> "this conversion number will inflate to include those"

**Evidence:** In Grow and Convert's client exploration, 42 segment users showed 228 conversion events, and one table row showed 10 users against 34 conversions, purely because many events were flagged as conversions.

**How to do it**

1. Go to Admin, then Events under the Property column.
2. List every event currently showing the Mark as conversion toggle switched on.
3. Toggle off page_view, scroll, click, file_download and any other automatically collected event.
4. Leave on only the events that represent a real commercial action.
5. If you need one report focused on a single action, leave only that event toggled on while you read it.
6. Re-open your exploration and confirm the Conversions total now sits in the same order of magnitude as Total users.
7. Document which events are toggled on and the date, since anyone can flip a toggle and silently change every historical-looking report.

**Tools:** Google Analytics 4

**Pitfall:** A Conversions figure many times larger than Total users is the signal you have hit this; teams then report scroll events to clients as conversions without realizing.

**Apply at Pabau:** Before Pabau reports demo numbers from any blog or template page, audit the Events screen and leave only demo-request and template-download toggled as conversions.

**Apply anywhere:** Audit the GA4 Events screen and leave only genuine commercial actions toggled as conversions, or every report inflates with scrolls and page views.

### 6. Target 1-5% per bottom-funnel page and 0.5-2% blog-wide  `143.5`
*core · content insights · source 143*

Grow and Convert give explicit conversion benchmarks so teams stop judging organic against the wrong yardstick. For an individual page ranking for bottom-of-funnel keywords, a good conversion rate is 1% to 5%, and anything above that is great. For a whole blog or content operation that is largely bottom-funnel, 0.5% to 2% from visitor to lead, trial start or ecommerce sale is good. They report getting 2%+ average conversion rates on client blog posts across both a mid-market demo-based SaaS company and a B2SMB self-service SaaS company. These are visitor-to-conversion numbers, not sessions-to-MQL, and they apply only when the pages genuinely target buying intent.

> "between 1%–5%. Anything above that is great"

**Evidence:** Grow and Convert report 2%+ average blog post conversion rates across two client types, a mid-market/enterprise demo-based SaaS and a B2SMB self-service SaaS.

**Tools:** Google Analytics 4

**Pitfall:** Applying the 1-5% band to a top-funnel post sets an unreachable target and gets good informational content killed. The band only holds for pages ranking on buying-intent terms.

**Apply at Pabau:** David should set the target for Pabau's comparison and alternatives pages at 1-5% demo requests per visitor, and hold the blog as a whole to 0.5-2%. Anything reported below that on a buying-intent page is a page problem, not a market problem.

**Apply anywhere:** Set 1-5% as the conversion target for an individual bottom-funnel page and 0.5-2% for the blog as a whole, visitor to lead or trial. Judge pages against the band that matches their intent.

### 7. Track AI visibility by topic with prompt baskets  `12.11`
*core · ai workflows · source 12*

Devesh's recommended AI-visibility measurement process is to stop trying to predict and track one exact prompt per topic, which is unreliable due to invisible prompts and personalization, and instead define topics first, such as 'SEO agency,' 'content agency,' and 'GEO/AI search agency' as three separate topics for Grow & Convert. For each topic, generate 3 to 10 different phrasings a real person might use to ask about it, run each phrasing across target LLMs, and calculate the average mention rate across that whole basket of prompts per topic. Track that average over time rather than any single prompt's result, which turns an unpredictable, noisy single-prompt signal into a directionally reliable topic-level trend line. This lets you spot exactly which topics are weak, his example being strong visibility for 'content agency for SaaS' but far less for the more competitive 'SEO agency' topic, so you know where to direct new content.

> "come up with three, five, even ten different prompts"

**How to do it**

1. List every distinct topic or category you want your brand associated with, such as 'practice management software,' 'clinic scheduling software,' 'med spa CRM,' and 'patient booking software' for Pabau.
2. For each topic, write out 3 to 10 different natural-language phrasings a real prospect might use to ask an LLM about that topic, covering different angles such as feature-focused, budget-focused, and industry-focused.
3. Run every phrasing in the set against each target LLM or AI surface, including ChatGPT, Claude, Gemini, Perplexity, and Google AI Overview/AI Mode, and record whether your brand is mentioned for each, manually or via an AI-visibility tool (inferred).
4. Calculate the percentage of prompts within each topic's basket that mention your brand, and treat that percentage, not any single prompt's result, as the topic's visibility score.
5. Re-run the same basket of prompts on a recurring cadence such as monthly, and track each topic's average mention rate over time to identify trend direction.
6. Rank topics by average visibility score to identify weak topics, such as a highly competitive category where you're rarely mentioned, and prioritize new bottom-of-funnel content production specifically to strengthen those weak topics.

**Tools:** Traqer, Peec, Profound, Scrunch

**Pitfall:** Don't try to predict or chase the single exact prompt wording a real user will type - Devesh shows this is fundamentally unpredictable due to personalization, so build topic-level prompt baskets instead of obsessing over any one prompt's tracked result.

### 8. Track AI visibility per topic, not per individual prompt  `78.4`
*core · concrete actions · source 78*

Grow and Convert measure GEO success at the topic level because prompts are not repeatable. They name three sources of uncertainty: you cannot know the prompts users type, personalization and chat history mean your tool never sees the answer a real user sees, and the same user asking the same prompt twice gets different responses and citations. Given that, a per-prompt score is noise. They note that Peec, Profound and Scrunch default to per-prompt measurement and that they built their own tool, Traqer.ai, to report which topics the brand is visible in and whether that is growing. This is a disclosed vendor position, so treat the tool claim accordingly, but the topic-level principle stands on the repeatability argument alone.

> "We track your AI visibility at the topic level"

**Evidence:** Grow and Convert cite three uncertainty sources: unknown prompts, personalized context from chat history, and non-repeatable responses to the same prompt from the same user.

**How to do it**

1. Group your tracked prompts into topic baskets matching the branches of your topic map.
2. Put at least 10 to 20 prompt variants in each basket so one prompt's variance cannot move the score.
3. Run each basket across ChatGPT, Perplexity and Google AI Overviews on a fixed cadence.
4. Score each basket as the share of prompts in it where the brand appears, not a pass or fail per prompt.
5. Report the basket score over time and ignore week-to-week movement on any single prompt.
6. Correlate basket score changes with the content you published for that branch.
7. Re-run baskets from clean sessions so account history does not bias the result.

**Tools:** Traqer.ai, Peec, Profound, Scrunch

**Pitfall:** Reporting single-prompt checks to stakeholders. Because responses vary run to run, you will report a win one week and a loss the next with no underlying change, and lose credibility for the whole program.

**Apply at Pabau:** David should define Pabau prompt baskets by topic (clinic scheduling software, med spa EMR, aesthetic practice management) and report the basket share of voice monthly, not screenshots of individual ChatGPT answers.

**Apply anywhere:** Group your tracked prompts into topic baskets of 10 to 20 variants, score each basket as share of prompts where you appear, and report basket trends. Never report a single prompt check as a result.

### 9. Track conversions per post in a waterfall so decline is visible per URL  `116.10`
*core · concrete actions · source 116*

Grow and Convert run their whole audit off a conversion-by-post waterfall chart that shows how many conversions each article produced each month, with GA4 attributing conversion events to specific pages. In the client example, one post converted 61 times in June 2022, then declined to 15 in December and 24 in January 2023. That per-post monthly series is what makes the rest of the process possible: it names the best-converting month to pull historical rankings for, and it distinguishes a post that is slipping from one that never worked. A site-level conversion chart would have shown only the plateau and the dip, with no way to know which of 71 posts caused it.

> "the highlighted post had converted 61 times"

**Evidence:** Grow and Convert's client waterfall showed one post at 61 conversions in June 2022 falling to 15 in December and 24 in January 2023.

**How to do it**

1. Set up conversion events in GA4 so demo requests and signups are attributed to the landing page that produced them.
2. Build a monthly table with one row per published post and one column per month, holding conversions.
3. Render it as a waterfall or heatmap so declines stand out visually across the row.
4. Each month, flag any post whose conversions fell more than roughly half from its own peak.
5. For each flagged post, record its peak month; that date is the input to the lost-keyword diff.
6. Keep the series running for the life of the site so peaks stay recoverable years later.
7. Review the chart before commissioning any new article, so refresh work competes fairly with new publishing.

**Tools:** GA4, Google Sheets

**Pitfall:** Without per-post attribution you see only the site-level dip. Grow and Convert's client showed a plateau and a decline that could not be diagnosed until it was broken down by URL.

**Apply at Pabau:** Pabau should attribute demo requests in GA4 to the blog or template page that produced them and keep a monthly per-URL table. Without it, David cannot tell which article's decline is causing an overall drop in organic demos.

**Apply anywhere:** Attribute conversions in analytics to the page that produced them and keep a monthly per-URL table. Without it you cannot tell which article's decline caused an overall drop.

### 10. Track free AI-citation data via Bing Webmaster Tools  `07.15`
*core · concrete actions · source 07*

Bing Webmaster Tools (Bing's equivalent of Google Search Console) includes a dedicated 'AI performance' report that surfaces three free, otherwise-hard-to-get metrics: total citations, average pages cited, and the actual queries your site is being cited for inside AI search engines. This is presented as a genuinely reliable free alternative for teams without budget for a paid AI-visibility tool, since Bing 'actually does this really well.' Verification only requires having already authenticated the site in Google Search Console, since Bing Webmaster Tools supports authenticating from that existing verification rather than a separate manual process. The trend to watch is growth in both citation count and average cited pages over time, cross-referenced against your target keyword list to spot which topics are already earning AI citations.

> "total citations, average pages cited, and the queries you're being cited for"

**How to do it**

1. Confirm the site is already verified in Google Search Console (prerequisite).
2. Add the site to Bing Webmaster Tools and use the Search-Console-based authentication option rather than a separate manual verification.
3. Once verified, navigate to the 'AI performance' report inside Bing Webmaster Tools. (inferred: check the current Reports/Search Performance menu area, since exact placement may shift as Bing updates its UI)
4. Record the three headline figures: total citations, average pages cited, and the list of queries you're being cited for.
5. Track these figures monthly rather than expecting a single-point benchmark; rising citations and rising average cited pages are the target trend.
6. Cross-reference the 'queries cited for' list against your existing target keyword list to identify which topics already earn AI citations.
7. Use topics that are NOT yet appearing in this report to prioritize which articles need a content-capsule rewrite next. (inferred prioritization step)

**Tools:** Bing Webmaster Tools, Google Search Console

**Pitfall:** Assuming AI-citation tracking requires a paid tool — Bing Webmaster Tools provides total citations, average cited pages, and cited queries for free, and is described as reliable.

### 11. Triage a stalled page by its position band before changing anything  `120.5`
*core · concrete actions · source 120*

Grow and Convert track rankings in Ahrefs and conversions in Google Analytics, and give three named responses keyed to where a page has stalled. If a keyword sits on page two or three, they read it as a backlink shortage and raise link building for that page. If it is stalled at the bottom or middle of page one, they read it as a click-through problem and rewrite the SEO title to something more compelling. They report doing this repeatedly on their own agency site and moving from mid page one to the top. The third response is at the portfolio level: if one subset of keywords is both easier to rank and driving conversions, publish more of that subset. Worth noting the disagreement with source 112, which treats page two to four rankings as effectively zero and rebuilds with new dedicated pages instead of adding links.

> "keywords are stuck on page 2 or 3 in the SERPs"

**Evidence:** Grow and Convert report repeatedly moving their own agency pages from the bottom or middle of page one to the top by changing the SEO title alone.

**How to do it**

1. Pull current position per target keyword from Ahrefs and conversions per page from Google Analytics into one sheet.
2. Band every page: page two or three, bottom or middle of page one, top three.
3. For pages on page two or three, do not touch the copy; add the page to the link-building queue instead.
4. For pages at the bottom or middle of page one, rewrite the SEO title for click-through and leave the body alone.
5. Change only one variable per page so the next reading is interpretable.
6. Wait at least four weeks before rereading position, since fresh titles need re-crawl and testing.
7. Group the whole set by keyword category and find the subset with the best ratio of easy rankings to conversions.
8. Add more keywords from that subset to the next quarter's plan and cut from the worst-performing subset.

**Tools:** Ahrefs, Google Analytics

**Pitfall:** Rewriting the article for a page-two ranking. If the gap is authority, a rewrite consumes the budget and the position does not move, and you have lost the ability to tell which change mattered.

**Apply at Pabau:** Pabau should band every tracked page each month. Page-two pages go to the link and digital PR queue, mid-page-one pages get a title rewrite only, and no page gets two changes in the same month.

**Apply anywhere:** Band every tracked page by where it stalled. Page two or three means an authority gap, so add links and leave the copy alone. Bottom or middle of page one means a click-through gap, so rewrite the title only. One change per page per month.

### 12. Use 'striking distance' + information-gain reports to fast-track top-10 rankings  `50.7`
*core · concrete actions · source 50*

For any page already sitting in the top 20, specifically called out as the trigger threshold, the system automatically runs a "striking distance" analysis that looks for information gain and missing entities relative to competitors, and generates a report a human can act on quickly. Applying the report's recommended changes reportedly moves pages into the top 10 much faster than waiting for natural ranking movement, and the guest states search engines currently favor fresh content, so the ability to make quick, targeted updates, rather than a full rewrite, generates a steady stream of freshly-updated pages across a site. He says this pattern has held up across multiple projects, producing faster traffic gains than publishing net-new content alone.

> "it will rank much faster into the top 10"

**How to do it**

1. Set a monitoring rule that flags any page ranking in positions 11-20, the "striking distance" range, for automatic analysis rather than manual discovery.
2. For each flagged page, run an information-gain analysis comparing it to the current top-ranking competitors to find what unique information they have that your page lacks.
3. Separately run a missing-entity check against the same competitor set.
4. Generate a short, specific update brief from those two checks rather than a full content-strategy document.
5. Apply the recommended changes directly to the existing page, adding the missing information and entities and updating the modified date, instead of drafting a brand-new page.
6. Track the page's ranking position over the following one to two weeks to confirm the targeted update accelerated its move into the top 10 (inferred verification timeframe).
7. Repeat this scan across all striking-distance pages on a recurring schedule, since it's described as working consistently across multiple projects (inferred recurring cadence).

### 13. Use 3-month position stability to judge ongoing link needs  `53.5`
*core · concrete actions · source 53*

To decide whether a page that's receiving internal links still needs that support, David Quaid recommends checking its average position trend in Google Search Console over roughly a three-month window on a case-by-case basis. If the average position holds at a strong, stable number, his example is a perfect one, across that period, the page is probably safe and could be a candidate to have some of its incoming links reallocated elsewhere. If instead the position is oscillating, his example is an average of 3.3, meaning the page is bouncing between roughly position 1 and further down, effectively falling below the fold at times, that rotation is a signal the page still needs more authority, so you should leave its existing internal links in place or add further supporting pages rather than pulling links away.

> "average position is a perfect one for three months, you're"

**How to do it**

1. In Google Search Console, open Performance > Search Results and filter to the specific page you're evaluating.
2. Set the date range to a rolling 3-month window and review the Average Position trend line for that page.
3. If the average position holds steady near its target rank across that full window, classify the page as stable and a candidate to have some inbound internal links redirected elsewhere.
4. If the average position is oscillating, e.g., swinging around a value like 3.3, indicating it periodically drops below the fold, classify the page as still needing support.
5. For pages still needing support, leave existing internal links in place, or add more supporting pages/links to shore up its topical authority.
6. Re-check this same 3-month trend on a recurring basis, e.g., monthly, rather than treating any single check as final (inferred recurring-review step).

**Tools:** Google Search Console

**Pitfall:** Reallocating internal links away from a page just because it currently ranks well, without checking whether that ranking is stable or oscillating over a multi-month window, risks pulling support from a page that's actually still fighting to hold its position.

### 14. Use Starts with, not Equals, on the thank-you page value  `149.2`
*core · best practices · source 149*

A small configuration choice Grow and Convert flag as a trap. When you set the operator for the page_location parameter, Equals requires the visitor's URL to match your pasted value exactly. Any query string appended to the thank-you page breaks the match and the conversion is never counted. They name Calendly UTMs as the common culprit, but any campaign tagging, ad platform click ID or tracking parameter does the same thing. Their recommendation is to use Starts with so the base URL matches and anything appended is ignored. The failure is silent: the event exists, the toggle is on, and the report just reads lower than reality with nothing to indicate why.

> "it may be a safer choice"

**Evidence:** Grow and Convert cite Calendly UTMs attached to the landing page as the specific case that breaks an Equals match.

**How to do it**

1. In the event configuration form, set Parameter to page_location.
2. Choose 'starts with' as the Operator rather than 'equals'.
3. Paste only the stable part of the thank-you URL, with no query string, as the Value.
4. Include the protocol and host consistently so a www or https variant cannot fall outside the match.
5. Load your own thank-you page with a UTM appended and confirm the event still fires in realtime.
6. Repeat the check with a Calendly or ad-platform redirect, which is where the appended parameters usually come from.
7. If you inherited an Equals rule, compare its counts with a parallel Starts with rule for two weeks before switching.

**Tools:** Google Analytics 4, Calendly

**Pitfall:** With Equals, conversions from any traffic carrying UTMs or click IDs vanish, which disproportionately kills paid and email numbers and makes organic look better than it is.

**Apply at Pabau:** Pabau's demo-confirmation event should use starts-with on the thank-you path, otherwise every ad and email demo booking drops out and organic gets credited with the whole funnel.

**Apply anywhere:** Configure the thank-you page conversion with a starts-with operator so campaign parameters do not silently discard conversions from paid and email traffic.

### 15. Use indexation-then-first-rankings as the leading indicator, not traffic  `133.6`
*core · best practices · source 133*

Grow and Convert describe a 'magic moment' on every account, and they define it precisely: the point where their articles start getting indexed by Google and start ranking for the targeted keywords somewhere in the top few pages. That is the signal they use to know the process is working and that results will scale. It is deliberately upstream of traffic. On Circuit the sequence ran June for the structural fix, July and August for the first rankings, September for the traffic jump, and September for the conversion jump. Reading only the traffic line means waiting three months to learn whether a change worked. Reading indexation and first rankings means learning in weeks. They note the same lesson bluntly: content and SEO takes patience, and the gaps between the three signals are the reason.

> "it's when we see our articles start to get indexed"

**Evidence:** Circuit: subfolder move June 14 2020, first rankings visible July and August, organic traffic jump and trial-signup jump both in September 2020.

**How to do it**

1. Define three checkpoints per published article: indexed, first appearance in the top 100, first appearance in the top 30.
2. Confirm indexation within two weeks of publishing using the URL Inspection tool in Search Console.
3. Track average position across the whole targeted keyword set as one number and chart it weekly.
4. Report the average position chart to stakeholders in the months before traffic moves, so there is a visible line that is not flat.
5. Expect roughly a one to two month gap between first rankings and a visible traffic change.
6. Expect conversions to follow traffic within the same month, not later, if you are targeting bottom-of-funnel terms.
7. Escalate to a technical audit only when the indexed checkpoint fails, and to a content or authority review when pages index but never enter the top 100.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Reporting sessions as the only progress metric on a young domain. The chart stays flat for months while the process is working, which is what Grow and Convert call nerve-racking on a monthly client call and is where programs get cancelled.

**Apply at Pabau:** Pabau's monthly SEO reporting should lead with indexation status and average position across tracked keywords, with sessions and demo requests underneath. That way a new content area, such as a fresh template cluster, can be judged in weeks instead of a quarter.

**Apply anywhere:** Make indexation and first rankings your leading indicators, and report average position across the tracked keyword set every month. Traffic lags first rankings by one to two months, so a traffic-only report tells you nothing for a quarter.

### 16. Use one thank you page for all forms, not one per form  `154.2`
*core · concrete actions · source 154*

Grow and Convert are explicit that visitors go to the same unique thank you page regardless of which page they were on when they started the form. The point of the design is that the thank you page is the single conversion signal, and the page the visitor originally landed on is supplied by Google Analytics itself through the Landing Pages report. Splitting into many thank you pages adds goals to maintain, splits the numbers across reports, and gains nothing, because the segmentation you actually want comes from the landing page and source dimensions rather than from the destination. The one reason to break the rule is a genuinely different offer, such as a template download versus a sales demo, where the two count as separate conversion types with different values.

> "regardless of what page they were on"

**How to do it**

1. Standardize a single thank you URL for one conversion type, for example a demo request.
2. Configure every demo form on every page to redirect to that same URL.
3. Create a second thank you URL only where the offer itself is different, such as a content download versus a sales conversation.
4. Set one Google Analytics goal per conversion type, not per form location.
5. Read the split by originating page from the Landing Pages report rather than from separate destination pages.
6. Assign each goal a different monetary value if the two conversion types are worth different amounts to the business.

**Tools:** Google Analytics

**Pitfall:** Building a thank you page per blog post or per form fragments goal completions across dozens of goals, and Google Analytics caps how many goals a view can hold, so the account fills up before the site is covered.

**Apply at Pabau:** Pabau should keep one thank you URL for demo requests across the whole of pabau.com, and a second for template downloads, since those two are worth different amounts. That gives David a clean read on which blog articles feed demos versus which just feed the list.

**Apply anywhere:** Keep one thank you URL per offer type across the whole site rather than one per form, so you get a clean read on which articles feed sales conversations versus which just feed the email list.

### 17. Verify a ranking drop is real across 30- and 90-day windows  `21.9`
*core · concrete actions · source 21*

David's method for telling a genuine ranking loss from normal noise: tag every tracked keyword by business purpose when adding it (money/lead-gen/CPC vs. awareness/topical-authority/experiment) so exploratory terms can be excluded from panic checks. When a dip or 'lost ranking' alert appears, he re-views the same keyword's chart across both a 30-day and a 90-day window - if the flat or declining period shows up consistently in both, it's a real signal rather than a one-off sampling glitch from the third-party tracker's single daily crawl. He then pinpoints the exact date the decline began and confirms it has persisted for a meaningful stretch (his example: nearly a month since July 5th) before treating it as confirmed and drilling into that specific keyword in GSC for pogo-sticking or lost internal links.

> "Whether I look at this graph as 90 days or 30 days"

**How to do it**

1. Tag every keyword by business purpose when adding it to your rank tracker: money/lead-generator/CPC for revenue-critical terms vs. awareness/topical-authority/adjacency/experiment for exploratory terms.
2. When a concerning dip or 'lost' alert appears, first check the exact date and time the report ran, since daily third-party crawlers can misfire or catch a rotation/test window.
3. Re-view the same keyword's chart across both a 30-day and a 90-day date range.
4. Treat the dip as real only if the flat or declining period appears consistently in both windows.
5. Filter out keywords tagged as awareness/topical-authority/experimental from this check so exploratory-keyword noise doesn't obscure genuine revenue-keyword drops.
6. For remaining money/lead-gen keywords, check the estimated-traffic or average-position view, not just an overall visibility score.
7. Pinpoint the exact date the decline began and confirm it has held for a meaningful period before treating it as confirmed.
8. Once confirmed, drill into that keyword/page in GSC to check for pogo-sticking (declining CTR, position oscillation) or lost internal links as the likely cause.

**Tools:** SERP rank-tracking tool, Google Search Console

**Pitfall:** Reacting immediately to a scary 'lost rankings' alert from a daily rank-tracker without checking the date/time it ran, or without cross-checking both a 30-day and 90-day view, risks chasing noise from a single mistimed crawl or normal position-testing rotation instead of a real, sustained ranking loss.

### 18. Watch conversions first and dig back to rankings when they drop  `119.13`
*core · concrete actions · source 119*

Grow and Convert's client case ran the diagnosis backwards from how most teams do it. Conversions are their primary success metric, so the first thing they noticed was that a client generating 200-plus trial signups a month from content started dropping off around the end of 2022. Only then did they look at rankings and traffic to find the cause, which was lost positions on primary and valuable secondary keywords across several posts. They ran SERP analysis on each lost keyword, found the SERPs had changed, and re-angled the content. Some posts needed light additions such as new product features or competitor information. Others needed heavy remixes, for example turning a product-feature article into a list post covering several products. After the queue was cleared, content averaged 258 conversions a month against 171 before.

> "content was averaging 171 conversions per month"

**Evidence:** Grow and Convert client: 200-plus trial signups a month, dip from late 2022, then a recovery from 171 to 258 average monthly conversions after the update queue was completed.

**How to do it**

1. Put a monthly conversion count per content-sourced signup on the same dashboard as traffic, and review it before you review rankings.
2. When the conversion line dips for two months running, pull the list of pages that previously produced those conversions.
3. For each page, check which primary and secondary keywords lost position over the same window.
4. Run a SERP analysis on every lost keyword and write down how the results changed since you published.
5. Sort the affected posts into light fixes, such as adding new features or competitors, and heavy remixes, such as converting a product post into a list post.
6. Work the queue to completion before measuring, rather than judging one page at a time.
7. Compare the average monthly conversions for the six months before and after the queue, not week to week.

**Pitfall:** Running the program on traffic alone. Traffic can hold while the specific converting keywords slide, so the revenue-relevant decay is invisible until a quarter is already lost.

**Apply at Pabau:** Pabau should track demo requests per article, not just sessions, and treat a two-month decline in article-sourced demos as the trigger to pull the ranking data for those specific pages.

**Apply anywhere:** Track conversions per article, not just sessions, and treat a two-month decline in content-sourced conversions as the trigger to pull ranking data for those specific pages.
