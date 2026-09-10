# Measurement & GSC — core (part 4 of 5)

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Read blog conversion from the Landing Pages report, not pageviews  `154.3`
*core · concrete actions · source 154*

Once the thank you page goal exists, Grow and Convert send you straight to the Landing Pages report, which shows traffic and conversions for the first page a visitor hit on the domain. Their own read of it found that their article about going viral on Medium converted far better than anything else on the site, which then became a template to study and copy on other high-traffic posts. They also point out you can use the report's search filter to look separately at main site pages such as home, features, pricing and case studies, so you can compare how the marketing site and the blog each pull in traffic that converts. Note this contradicts source 150, which argues the Landing Pages report should not be used to credit blog conversions because it hides assisted paths.

> "our article on going viral on Medium converts way higher"

**Evidence:** Grow and Convert's Medium virality article converted at a far higher rate than the rest of the site, which they used to guide edits elsewhere.

**How to do it**

1. Open Behavior then Site Content then Landing Pages in Google Analytics, with the thank you page goal already live.
2. Set the date range to at least 90 days so low-traffic posts accumulate enough completions to read.
3. Add the goal conversion rate column and sort by goal completions, not by sessions.
4. Filter the page path to /blog/ to isolate content, then filter to the money pages separately for comparison.
5. Ignore any row with fewer than about 10 completions; the rate is noise at that volume.
6. Take the top converting posts and note what they share: topic, offer placement, funnel stage, format.
7. Apply those shared traits to your highest-traffic posts that currently convert poorly.
8. Treat the numbers as last-touch, so cross-check any surprising winner against a first-click or assisted-conversion view before reallocating budget.

**Tools:** Google Analytics

**Pitfall:** The report only credits the entry page, so an article that introduces someone to the brand and gets revisited later scores zero. Source 150 makes exactly this argument against relying on it.

**Apply at Pabau:** David should run this report on pabau.com filtered to /blog/ and /templates/ separately. Template pages likely convert at several times the rate of general blog posts, which changes which pages deserve refresh effort.

**Apply anywhere:** Run this report filtered to your blog and to your gated or template pages separately. Bottom-funnel resource pages usually convert at several times the rate of general blog posts, which should change which pages you spend refresh effort on.

### 2. Read heavy homepage conversions as a tracking artifact, not performance  `151.11`
*core · content insights · source 151*

Devesh names three separate mechanisms that all push credit onto the homepage. A reader finds a post on their phone, gets to work, then converts on desktop; the cookie cannot connect the two sessions, so the conversion is attributed to whatever they landed on, which is the homepage. A reader who converts more than 90 days after first reading is outside the lookback window, and again lands on the homepage to sign up. And word of mouth is invisible entirely. His conclusion is the diagnostic: if you do enough content marketing, you will see a ton of conversions from the homepage. So a homepage that dominates your conversion table is not evidence the homepage is your best asset. It is evidence your content is being undercounted.

> "you'll see a ton of conversions from the homepage"

**Evidence:** Grow and Convert attribute homepage-heavy conversion tables to three causes: cross-device sessions, conversions beyond the 90 day lookback, and word of mouth.

**How to do it**

1. Pull the landing page attribution table and note the homepage's share of total conversions.
2. Compare that share against the homepage's share of total sessions; a much higher conversion share signals reassignment.
3. Check the cross-device rate in your analytics device report to size how often readers switch devices.
4. Check what share of your sales cycle sits beyond the 90 day lookback window.
5. Do not credit the homepage in content reporting until those two effects are accounted for.
6. Add a self-reported source field at signup and count how many homepage conversions name an article.
7. Report content performance as a floor and state the homepage reassignment as the reason.

**Tools:** Google Analytics

**Pitfall:** Concluding from the attribution table that the homepage converts best leads teams to cut content budget, when the homepage is simply collecting credit for work the blog already did.

**Apply at Pabau:** Pabau's homepage will look like the top demo driver in GA4 for exactly these reasons, so David should discount that row before using the table to decide article budget.

**Apply anywhere:** Treat a homepage that dominates your conversion table as a symptom of cross-device and out-of-window tracking loss, not as proof the homepage is your best converting page.

### 3. Read last, first and linear as three separate whole numbers  `151.3`
*core · content insights · source 151*

Devesh walks through one blog post's row in the model comparison tool. Last Interaction showed 5, meaning five users converted in the exact same session they landed on that post. First Interaction showed 13, meaning that within a 90 day window there were 13 conversions where this post was the first page the converting user ever landed on. Linear showed a decimal, because when a converting user touched the site four times and the post was one of them, the post gets 0.25 of a conversion. He is explicit that these numbers are not additive. You do not add first click to last click. Each is a different lens producing its own count of the same conversions. The reading is 'if I counted only last click, what would the number be?' and then the same question for first click.

> "The conversion numbers are not additive."

**Evidence:** Grow and Convert's worked example: one post showed 5 last-interaction conversions, 13 first-interaction conversions over 90 days, and a decimal linear value.

**How to do it**

1. Read the Last Interaction column as conversions that happened in the same session as the landing.
2. Read the First Interaction column as conversions where this page was the visitor's first landing inside the lookback window.
3. Read Linear as fractional credit, so a post that was one of four touchpoints earns 0.25 per conversion.
4. Never sum the columns; report each model as its own count of the same conversion set.
5. Phrase every report line as 'counting only first click, this post produced N conversions'.
6. Compare first minus last per post to see how many conversions came back in a later session.

**Tools:** Google Analytics

**Pitfall:** Adding first-click and last-click counts together doubles the same conversions and produces a number no finance team will accept once they check it against actual signups.

**Apply at Pabau:** Any attribution reporting David builds for Pabau should show the first and last columns side by side per article with a note that they are alternative counts, not components of a total.

**Apply anywhere:** Show first-click and last-click as parallel counts of the same conversions in every content report, and never add them together.

### 4. Read the exploration totals row as the real answer, not the table  `149.14`
*core · content insights · source 149*

Grow and Convert say the most important number in the any-touchpoint report is the Total users figure at the top of that column, because it is the count of people who met the whole segment condition: landed on one of your specified pages and then converted, inside the date range. In their client example that number is 42. The Conversions total beside it, 228, is the number of conversion events those 42 people triggered, including events unrelated to the one in the segment. They separate the totals from the table below with a box in their own screenshot for exactly this reason. If you take one number from this report to a stakeholder, it is Total users, and it should be described as people who converted after landing on your content.

> "42 users met this segment criteria"

**Evidence:** In the walked-through client report, 42 users met the segment criteria and those users triggered 228 conversion events in the same period.

**How to do it**

1. Read the Total users figure at the top of the column first, before any row.
2. Describe it as the number of people who converted after landing on the specified pages in the date range.
3. Read the Conversions total as event volume from those same people, not as a second count of conversions.
4. Expect Conversions to exceed Total users, often by a lot, if multiple events are flagged as conversions.
5. Report Total users as the headline content-contribution number.
6. Only quote the Conversions total when a single event is toggled on in conversion settings.
7. Keep the date range identical when comparing periods, since the segment is evaluated inside it.

**Tools:** Google Analytics 4

**Pitfall:** Quoting the Conversions total as the number of leads inflates the result several-fold; in Grow and Convert's example that would have turned 42 people into 228 conversions.

**Apply at Pabau:** Pabau's monthly content report should quote users who converted after landing on a blog or template page, not raw conversion events, or the demo number will read several times higher than reality.

**Apply anywhere:** Quote the total-users figure from the segment as the content contribution number, not the raw conversion-event count, which is inflated by every other flagged event.

### 5. Refuse assisted conversions and brand awareness as the answer on leads  `179.15`
*core · best practices · source 179*

Grow and Convert say many agencies do not report on conversions at all. The monthly report shows keyword rankings, traffic growth and domain authority improvements, with nothing connecting any of it to business results. The specific test is to ask how many leads the SEO work generated last month. They describe two responses that both mean no: the agency cannot answer, or it deflects to assisted conversions and brand awareness, which they characterize as metrics that are difficult to verify and easy to hide behind. Their own reporting keeps conversions as the primary KPI tracked in Google Analytics, with keyword rankings and organic traffic reported alongside rather than instead. They frame this level of accountability as what the standard should be, and an unwillingness to show it as a sign the agency is not confident it can deliver.

> "metrics that are difficult to verify and easy to hide behind"

**Evidence:** Grow and Convert report conversions as the key performance indicator tracked in Google Analytics, alongside keyword rankings and organic traffic, and say many agencies never report conversions at all.

**How to do it**

1. Ask, in plain numbers, how many leads or signups the SEO work produced last month, and wait for a figure.
2. Treat assisted conversions or brand awareness as a non-answer, and re-ask for the direct number.
3. Require the monthly report to carry conversions as the headline metric, with rankings and traffic below it.
4. Set up conversion tracking in Google Analytics before the engagement starts so the number exists from month one.
5. Ask to see an example monthly report from a current client, redacted, before signing.
6. Attribute conversions to specific URLs so you can see which pages produce leads and which only produce sessions.
7. Review the report each month against the break-even lead number rather than against last month's traffic.

**Tools:** Google Analytics

**Prompt / template:**

```text
How many leads did your SEO work generate for us last month? Can you show me an example of how you report results for a current client?
```

**Pitfall:** Letting domain authority into the monthly report. It moves reliably, has no revenue meaning, and fills the space where the conversion number should be.

**Apply at Pabau:** Pabau's own SEO reporting should lead with demo requests attributed to specific pabau.com URLs, with rankings and sessions as supporting lines. Any vendor report that opens with a traffic chart should be sent back.

**Apply anywhere:** Ask an agency how many leads its work produced last month and insist on a number. Assisted conversions and brand awareness are deflections, not answers. Require conversions as the headline metric in every monthly report, with rankings and traffic underneath, attributed to specific URLs. Set the tracking up before the work starts so the number exists from month one.

### 6. Report content leads as a floor and name the three leaks  `151.12`
*core · best practices · source 151*

Grow and Convert tell clients directly that these limitations mean you will never really know how many leads content generates, but you can get a lower limit. They rank the options: last click is the worst lower limit, and if you run content for a company and report only last-click conversions, you are doing yourself a huge disservice and will not get the credit you deserve. First click is a lot better and catches far more conversions, but it is still a lower limit. The three leaks they name are cross-device sessions, conversions beyond the 90 day lookback window, and word of mouth including a colleague or friend signing up instead of the reader. Naming the leaks in the report is what makes the floor framing credible rather than defensive.

> "Last click attribution is the worst lower limit."

**Evidence:** Grow and Convert tell clients repeatedly that attributed content leads are a lower limit and that last-click attribution is the worst such limit.

**How to do it**

1. Report first-click conversions per article as the headline content number, not last click.
2. Label that number explicitly as a lower limit inside the report, not in a footnote.
3. List the three leaks underneath it: cross-device, beyond the lookback window, and word of mouth.
4. Add the last-click number alongside so the size of the delayed-conversion effect is visible.
5. Add a self-reported source question at signup or on the first sales call to catch untracked leads.
6. Track the total conversions from generic pages including the homepage as a supporting trend line.
7. When a stakeholder challenges the numbers, show the gap between models rather than defending one figure.

**Tools:** Google Analytics

**Pitfall:** Reporting only last click leaves content marketers looking like they produce almost no leads, which is how content budgets get cut on a measurement artifact.

**Apply at Pabau:** David should present Pabau's content-attributed demos as a floor with the three leaks named, so the number survives scrutiny without overclaiming.

**Apply anywhere:** Present content-attributed leads as an explicit floor, name cross-device, out-of-window and word-of-mouth losses as the reasons, and show first and last click together.

### 7. Report conversions per article or concede the strategy is traffic-first  `115.6`
*core · best practices · source 115*

Grow and Convert close their process with the point they call the most notable of their three metrics. Most content teams, in house and agency alike, do not hold themselves accountable to leads generated from content, and most do not even report on it. Their argument is that this is not a neutral omission: without conversion data you are conceding that the strategy is traffic-focused, because traffic is the only thing everybody tracks. So the reporting choice retroactively decides the strategy. A team that says it wants leads but reports pageviews will drift back to high-volume keywords within a cycle or two, because those are the only ones the report rewards. The fix is to put conversions at the top of the monthly report, per article, before traffic appears anywhere on the page.

> "you are essentially conceding that your content strategy is traffic focused"

**Evidence:** Grow and Convert report that most in-house and agency content teams do not report leads generated from content at all.

**How to do it**

1. Define one conversion event that counts as a lead: demo request, trial signup, or qualified form fill.
2. Set it up as a goal or conversion in your analytics before publishing the next article.
3. Attribute conversions to the landing article, not to the site as a whole, so per-article numbers exist.
4. Put conversions per article at the top of the monthly report and push traffic below it.
5. Report zero honestly for articles that produced none, rather than substituting assisted sessions.
6. Review the bottom quartile each quarter and either rewrite them for buying intent or stop maintaining them.
7. Feed the per-article conversion numbers back into keyword selection for the next cycle.
8. If a writer or agency will not report this number, treat that as the answer about what they are optimizing.

**Tools:** Google Analytics

**Pitfall:** Reporting site-level conversions instead of per-article. The total looks healthy because branded and paid traffic converts, and nobody notices that the blog contributed almost none of it.

**Apply at Pabau:** David should make demo requests per article the first line of Pabau's content reporting, ahead of sessions. Any /blog/ or /templates/ page with zero demo requests over two quarters goes into a rewrite queue aimed at buying-intent keywords.

**Apply anywhere:** Track and report conversions per article, not just site-wide. Teams that report only traffic drift back to high-volume keywords regardless of what the strategy document says, because traffic is the only number being rewarded. Put per-article conversions above traffic in the monthly report.

### 8. Report conversions per article or concede the strategy is traffic-focused  `108.17`
*core · concrete actions · source 108*

Grow and Convert name their reporting stack and make an accountability argument out of it. Conversions are tracked and reported using the Model Comparison Tool in Google Analytics. Keyword rankings are monitored per article against its single target keyword using the Ahrefs rank tracker, with Semrush or Search Console as alternatives. Overall pageviews and organic traffic run through Looker Studio dashboards. They call conversion tracking the most notable of the three, and say most SEO teams, in-house or agency, do not hold themselves accountable to leads generated from content and most do not even report on it. Their line is that without conversion data you are conceding your SEO strategy is traffic focused, because traffic is what everybody already tracks. The reporting choice is therefore a strategy choice: what you report is what the program optimizes for.

> "the Model Comparison Tool in Google Analytics"

**Evidence:** Grow and Convert's stack: Model Comparison Tool for conversions, Ahrefs rank tracker per article target keyword, Looker Studio for pageviews and organic traffic.

**How to do it**

1. Define the conversion that matters: demo request, trial signup or booked call, not newsletter subscribes.
2. Set up conversion tracking that attributes each conversion to the entry article.
3. Use the Model Comparison Tool in Google Analytics to see how attribution changes the picture for content-assisted conversions.
4. Add every published article's single target keyword to the Ahrefs rank tracker.
5. Build one Looker Studio dashboard for pageviews and organic traffic so traffic stays visible but secondary.
6. Report all three together, with conversions per article as the first table in the report.
7. Review each article at three and six months on conversions, not on sessions.
8. Feed the converting articles into the link-building queue and rewrite or retire the non-converters.

**Tools:** Google Analytics, Ahrefs, Looker Studio, Google Search Console, Semrush

**Pitfall:** Reporting traffic because it is easy and conversions because a client asked once. If conversions are not the lead metric, keyword selection quietly drifts back to high-volume top-of-funnel terms.

**Apply at Pabau:** Pabau's content reporting should lead with demo bookings attributed to the entry article, then per-article target-keyword position, then traffic. Template pages and blog articles should be judged on bookings, not sessions.

**Apply anywhere:** Report conversions per article first, then per-article target-keyword position, then traffic. A report without conversion data is an admission that the strategy is aiming at traffic.

### 9. Report highest position reached per keyword, not aggregate CTR  `21.13`
*core · concrete actions · source 21*

Responding directly to the Reddit post that sparked the episode (443 clicks, 7,740 impressions, 5.7% CTR, average position 6.4), David says the poster should instead report, for each keyword they're actually targeting, the highest position ever reached for that specific phrase. If the highest position is already near the top but CTR is very low (his example: 0.4%), that signals a content/relevance issue, likely pogo-sticking. If the highest position reached is far down the results (his example: around 64), that signals an authority issue - the domain isn't strong enough to break into that competitive index regardless of content quality, and competing against entrenched high-authority sites (SEMrush, Moz) may mean the realistic move is to target a smaller keyword first, guided by a personalized keyword-difficulty score.

> "the highest position I got to was three, or one"

**How to do it**

1. List the specific keywords/phrases you are actually trying to rank for, not just aggregate site metrics.
2. For each target keyword, pull the highest position ever reached for that specific query in GSC's Performance report (filter by query, check the full available date range), not just the average position.
3. If the highest position is already near the top (1-3) but CTR is very low, diagnose it as a content/relevance issue such as pogo-sticking.
4. If the highest position reached is far down the results (e.g., around 60+), diagnose it as an authority issue rather than a content problem.
5. Before assuming fault, check which domains occupy that index - competing against entrenched high-authority sites may mean the keyword itself is currently unwinnable.
6. Use a keyword-difficulty score, ideally personalized to your own domain's authority, to identify realistically winnable keywords rather than guessing from a SERP screenshot.
7. Report or request feedback using this format - target keyword, highest position ever reached, and CTR at that position - instead of raw aggregate clicks/impressions/CTR/average position.

**Tools:** Google Search Console, SEMrush (keyword difficulty score)

**Pitfall:** Posting or evaluating aggregate site-wide clicks, impressions, average CTR, and average position is meaningless without knowing which specific keywords you're targeting and the highest position reached for each - the same aggregate numbers could reflect a content problem, an authority problem, or a perfectly healthy small campaign, and there's no way to tell which without drilling into query-level data.

### 10. Report leads and sales per article, not email signups  `102.13`
*core · concrete actions · source 102*

Grow and Convert report content performance on three things, and they lead with conversions. They track and report leads and sales for clients using the Model Comparison Tool in Google Analytics, and they say measuring actual leads and sales is very uncommon among agencies. Most agencies and content marketers measure softer conversions such as email signups, which sit further from the purchase stage. The reason to push measurement to the money event is that it changes what the strategy optimizes for: if signups are the metric, top-funnel content wins the report, and the program drifts back toward the traffic goal they warn against. Attribution modelling is what makes this possible, since content usually assists rather than closes, and a last-click view will show content contributing almost nothing.

> "using the Model Comparison Tool in Google Analytics"

**Evidence:** Grow and Convert say measuring leads and sales for clients is very uncommon among agencies, and use attribution model comparison to do it.

**How to do it**

1. Define the conversion that the business actually cares about: a demo request, trial, quote or purchase.
2. Configure that as a goal or conversion event in analytics, alongside any softer signup event.
3. Use the Model Comparison Tool to compare last-click against position-based or data-driven attribution for content pages.
4. Report both views, so assisted content contribution is visible rather than hidden by last-click.
5. Break the report down by article and by keyword category, not just by channel.
6. Review monthly and shift the calendar toward the article categories producing conversions.

**Tools:** Google Analytics

**Pitfall:** Reporting only email signups. It flatters top-funnel content and quietly rebuilds the traffic-first strategy under a conversion label.

**Apply at Pabau:** Pabau should report demo requests per article using a multi-touch attribution view, so long comparison and workflow articles are credited for assisted demos rather than looking unproductive under last-click.

**Apply anywhere:** Report the real revenue event per article, not email signups, and compare attribution models so assisted content is credited. Last-click reporting makes content look worthless and pushes the calendar back toward traffic.

### 11. Require conversion reporting, not just traffic and rankings  `101.5`
*core · concrete actions · source 101*

Step five: confirm the candidate can report on metrics that match the goal you set in step one. Grow and Convert note that most companies and agencies report traffic, keyword rankings and email signups, and far fewer report conversions from content, even though conversions are what buyers actually want. Their own stack is specific: conversions tracked with the Model Comparison Tool in Google Analytics, per-article target keyword rankings tracked in the Ahrefs rank tracker, and pageviews plus organic traffic dashboards built in Looker Studio. The reason they track rankings and conversions together is operational, not cosmetic: with both, they can see which topics produce results and commission more of that kind.

> "using the Model Comparison Tool in Google Analytics"

**Evidence:** Grow and Convert report conversions, per-article keyword rankings and Looker Studio traffic dashboards for every client.

**How to do it**

1. Ask the candidate to show a live client report, not a template.
2. Check the report contains conversions attributed to individual articles.
3. Set up conversion tracking with the Google Analytics Model Comparison Tool so assisted paths are visible.
4. Track each article's single target keyword in the Ahrefs rank tracker.
5. Build a Looker Studio dashboard for pageviews and organic traffic by article.
6. Review monthly and commission more topics of the type that converted best.

**Tools:** Google Analytics, Ahrefs, Looker Studio

**Pitfall:** Reporting only traffic and rankings hides which topics produce revenue, so the next quarter's topic list is picked on pageviews and the mix drifts top-of-funnel.

**Apply at Pabau:** Pabau's content reporting should show demo requests per article, not just sessions, so the template pages and code-reference pages that actually produce trials can be identified and expanded.

**Apply anywhere:** Insist on per-article conversion reporting alongside rankings and traffic, using analytics attribution modelling plus a rank tracker and a traffic dashboard. Tracking both lets you double down on the topics that produce customers.

### 12. Route every lead form to one unique thank you page first  `154.1`
*core · concrete actions · source 154*

Grow and Convert's whole measurement method rests on one build step that comes before any analytics work. Every lead form on the site, wherever it sits, must redirect to a single dedicated thank you page after submission. Unique means traffic reaches that URL only by completing the form, never by navigation, never from search, never from a link. They deliberately did not link to their own /thank-you page in the article and showed a screenshot instead, so the URL would stay clean. If the form instead reloads the same page or swaps in a JavaScript success message, the method fails outright and you need event tracking rather than a destination goal. Do this before touching Google Analytics, because the goal you set later is only as trustworthy as the uniqueness of that page.

> "just reloads the homepage or creates a dynamic"

**Evidence:** Grow and Convert use www.growandconvert.com/thank-you as their own example and note the page is unreachable except by opting in.

**How to do it**

1. List every lead form on the site: homepage, blog inline forms, pop-ups, footer, demo request, template downloads.
2. Point all of them at one destination URL such as /thank-you, using a server-side redirect on submit rather than an in-page success message.
3. Remove every internal link to that URL from navigation, footers, sitemaps and blog body copy.
4. Add noindex to the thank you page so it cannot be landed on from search.
5. Load the URL directly in an incognito window and confirm nothing else drives traffic there.
6. For any form that cannot redirect, such as a chat widget or an AJAX form, plan an event-based conversion instead and note it as a separate measurement path.
7. Watch the page's pageviews for a week and compare them against your CRM lead count; a gap means the page is not unique.

**Tools:** Google Analytics

**Pitfall:** Dynamic JavaScript thank you messages and same-page reloads produce no unique URL, so the destination goal never fires and content looks like it converts nobody. The signal is a goal with zero completions while the CRM shows leads arriving.

**Apply at Pabau:** David should audit every Pabau conversion path — demo request, template download, pricing enquiry — and confirm each ends on its own dedicated thank you URL rather than an inline confirmation. Template pages in particular tend to use in-page download confirmations, which silently break attribution for the highest-intent pages on the site.

**Apply anywhere:** Audit every conversion path on your site and confirm each ends on its own dedicated thank you URL rather than an inline confirmation message. Gated download pages in particular tend to confirm in-page, which silently breaks attribution for your highest-intent pages.

### 13. Run a one-variable sensitivity sweep on your CAC model  `152.6`
*core · concrete actions · source 152*

Rather than arguing about assumptions, Grow and Convert vary one input at a time across a wide range and chart CAC against it. Their results, using the B2C self-serve scenario as the baseline: promotion spend per article from $0 to $500 moved CAC only from $93 to $130. Articles per month from 1 to 8, taking freelance writing spend from $300 to $2,400 a month, moved CAC from $78 to $113. Monthly full-time salary spend from $0 to $10,000 moved CAC from $20 to $180. Traffic and both conversion rates produced the steepest curves, dropping CAC sharply at the low end and asymptoting toward zero at the high end. The point of the sweep is to rank levers by how much they actually move the output, so effort goes where the curve is steep.

> "We'll start by checking off the least important levers"

**Evidence:** Promotion spend $0-$500 moved CAC $93 to $130; articles 1-8/month moved CAC $78 to $113; salary $0-$10k/month moved CAC $20 to $180.

**How to do it**

1. Duplicate the CAC sheet into a sensitivities tab with the baseline scenario locked.
2. Pick one input, for example promotion spend per article, and build a column of values from zero to a plausible ceiling.
3. Use a data table or a formula column to recompute CAC at each value, holding everything else fixed.
4. Chart CAC against that input in Google Sheets and note the range of CAC produced.
5. Repeat for writing cost per article, articles per month, monthly salary, traffic, lead rate and lead-to-customer rate.
6. Rank the inputs by the size of the CAC swing they produce.
7. Direct next quarter's budget and headcount at the top two levers only.
8. Repeat the sweep after any pricing or headcount change, because the baseline moves.

**Tools:** Google Sheets

**Pitfall:** Reading a one-variable sweep as a forecast. Grow and Convert warn that in real life conversion rates dip as traffic grows and headcount rises to sustain the growth, so the isolated curves are optimistic.

**Apply at Pabau:** David should run this sweep on Pabau's content model before the next budget cycle. It will show whether an extra writer or a conversion-rate project buys more demos per dollar.

**Apply anywhere:** Run a one-variable-at-a-time sweep on your own CAC sheet, chart each curve, and rank the levers by the size of the swing before setting next quarter's budget.

### 14. Run one report per conversion event by isolating it in settings  `149.16`
*core · best practices · source 149*

Grow and Convert's precision rule for the any-touchpoint report. The Conversions column shows every event flagged as a conversion, not the one you named in the segment, so the only way to be certain the column corresponds to the action in your segment is to make that action the sole event toggled on in conversion settings while you read the report. They say it plainly: if you want to be precise about defining a conversion as a single event, such as a trial or demo signup, that must be the only event toggled on. This turns a vague conversions figure into a countable number of signups per landing page, which is the number the report exists to produce.

> "the only event toggled on in your conversion settings"

**Evidence:** Grow and Convert say this is the key detail that makes the table useful, and that without it they could only say a row had 43 conversions without knowing what they were.

**How to do it**

1. Decide the single conversion event the report is about, for example a demo signup.
2. Go to Admin > Events and toggle Mark as conversion off for every other event.
3. Leave the toggle on only for that one event.
4. Open the exploration and read the Conversions column, which now counts only that action.
5. Record the date range and note in the report which single event was toggled on.
6. Restore the other toggles afterwards if other teams depend on them, and note that this changes their reports too.
7. Where several teams need different events, agree a fixed minimal set rather than toggling back and forth.

**Tools:** Google Analytics 4

**Pitfall:** Toggling events on and off changes what every other report in the property shows at the same time, so an uncoordinated toggle breaks somebody else's number without any notification.

**Apply at Pabau:** Pabau should fix a minimal set of conversion events, demo request and template download, and keep it stable, rather than toggling events per report and breaking other people's dashboards.

**Apply anywhere:** Fix a minimal, stable set of conversion events rather than toggling events per report, since toggles change every report in the property at once.

### 15. Run time-series and location-series tests to measure zero-click marketing  `43.10`
*core · concrete actions · source 43*

To measure marketing impact that leaves no clickable analytics trail (offsite mentions, podcast appearances, brand awareness), Rand runs time-series experiments: pick a single, isolated marketing action (e.g., clipping a podcast segment and posting it across all social channels on one day), hold other marketing constant that day, then compare sign-ups/conversions on that day and the following three days against a trailing baseline (the average of the prior two weeks) — the difference is attributed as the value of that action. He pairs this with location-series experiments: run a comparable action (a localized launch, a conference talk) in one geography, repeat it in a second geography later, and compare results between the two locations to isolate whether the channel/tactic actually works, tying this to the same basic before/after testing logic advertising agencies used for offline campaigns as far back as 1965.

> "take the average number of sign-ups we've gotten over the last two"

**How to do it**

1. Identify one discrete, schedulable marketing action to test (posting a podcast clip across all social channels, a conference appearance, a localized launch).
2. Calculate your baseline metric (e.g., daily sign-ups) as the average of the prior two full weeks before the test action, pulled from your product's admin/analytics dashboard.
3. Pause or hold constant all other marketing activity on the test day to avoid confounding variables, as much as is practical.
4. Execute the single test action on the chosen day (e.g., publish the clip across every channel at once).
5. Record the actual metric (sign-ups, trial starts) for the test day and the following three days.
6. Subtract the baseline average from the observed post-action numbers to calculate the attributed lift from that specific action.
7. For a location-series test, repeat a comparable action in a second, different market at a later date.
8. Compare the lift/result between the two locations to judge whether the channel/tactic itself is generally effective versus a one-off fluke (inferred).
9. Use the resulting lift figure as evidence when requesting more budget for that channel from stakeholders who otherwise only trust last-click analytics (inferred).

**Pitfall:** Trying to attribute offsite/brand marketing value using only last-click analytics — Rand states this doesn't work for dark-social/offsite influence and you have to build your own before/after experiments instead, and getting stakeholder buy-in to pause other marketing for a clean test is itself a common blocker.

### 16. Score each post by first-interaction conversions over a 90-day window  `103.8`
*core · concrete actions · source 103*

Grow and Convert measure content with Google Analytics' model comparison tool, reading the first-interaction column per landing page. That column counts users whose first ever session on the site started on that blog post and who then converted within the next 90 days. The conversion goal in the example is 'create an account', on a client with a free tier and paid upgrades. Each row is one post they produced. One top-of-funnel post accounted for roughly 137 signups, making it among the highest converting pieces they had produced for that client. The dataset ran January 2021 to January 2022. One practical wrinkle: a post appeared as two rows because its URL was changed after publication, so rows have to be summed by article, not by URL.

> "converted them sometime within the next 90 days"

**Evidence:** Grow and Convert client data, January 2021 to January 2022: one top-funnel post generated around 137 account signups on first-interaction attribution, split across two rows because of a URL change.

**How to do it**

1. Define one product conversion goal in analytics, such as account creation or demo request, not an email signup.
2. Open the model comparison report and set the lookback window to 90 days.
3. Break the report down by landing page and filter to the blog directory.
4. Read the first-interaction conversion column, which credits the post that brought the user to the site.
5. Merge rows for the same article where the URL changed after publication, or the post will look half as effective.
6. Compare first-interaction against last-interaction per post to see which pieces acquire and which pieces close.
7. Rank posts by first-interaction conversions and use that ranking to decide what to write more of.
8. Rerun quarterly, since pieces published in the last 90 days cannot have completed the window.

**Tools:** Google Analytics

**Pitfall:** Judging a post inside its first 90 days. The window has not closed, so a new piece always looks worse than an old one and gets killed early.

**Apply at Pabau:** Pabau should score blog articles on demo requests attributed to first interaction over 90 days, not on sessions. That report tells David which article types to commission next and which to stop repeating.

**Apply anywhere:** Score each post on first-interaction conversions to a real product goal over a 90-day window, merging rows where a URL changed, and use that ranking to decide what to publish next.

### 17. Set GA4 conversion events, then read them through several attribution models  `145.4`
*core · concrete actions · source 145*

Grow and Convert reduce SEO conversion tracking in GA4 to three steps. First, create the events you care about and mark the relevant ones as conversion events, because without that flag you cannot build or access the reports. Second, decide which attribution models the reports will use, since no single model gives a complete picture; they recommend running more than one. Third, go beyond the default conversion report and build custom reports; the two they use are the model comparison tool and an any-touchpoint report. The point of the third step is that a blog post rarely sits last in the path, so a last-click default report will systematically undercount content.

> "attribution models you"

**Evidence:** Grow and Convert published a step-by-step GA4 tutorial and a long-form video walkthrough of this exact setup.

**How to do it**

1. In GA4 Admin, create the events for the actions that matter: demo request, trial signup, contact form submit.
2. Mark each of those events as a conversion event so it becomes available to reports.
3. Verify each event fires by triggering it yourself and checking GA4 realtime.
4. Open the default conversion report only as a high-level overview, not as the decision report.
5. Build a model comparison report so the same conversions are shown under more than one attribution model.
6. Build an any-touchpoint report so a page that appeared anywhere in the path gets credited.
7. Segment organic search traffic and split blog URLs from product and landing-page URLs before reading rates.
8. Read the models side by side and treat any single-model number as one view, not the answer.

**Tools:** Google Analytics 4

**Pitfall:** Relying on GA4's default conversion report alone means last-click credit, which hides most content-assisted conversions and makes good bottom-funnel posts look like they do nothing.

**Apply at Pabau:** Pabau's GA4 needs demo-request and contact events flagged as conversions, plus a model-comparison and any-touchpoint report that splits /blog/ and /templates/ from the marketing site, so David can judge which article types actually generate demos.

**Apply anywhere:** Create and flag your conversion events in GA4, then build a model comparison report and an any-touchpoint report alongside the default. Judge content on the multi-model view, not on last click.

### 18. Set page-level conversion events in GA4 before judging any content strategy  `105.6`
*core · concrete actions · source 105*

Grow and Convert say the whole buying-intent argument is untestable without page-level conversion data, and that most of the dozens of companies they work with are not measuring it. Those teams track traffic and maybe a site-wide conversion total, but cannot say which blog post produced a demo request or which keyword drove a qualified lead. The consequence is structural: with no page-level data, the only visible metric is traffic, so teams default to publishing more top-of-funnel because those charts look better. That locks the strategy onto the wrong metric. Their minimum bar is conversion events in GA4 for form submissions and demo requests, plus reports attributing those conversions back to specific landing pages and traffic sources.

> "you need conversion events set up in GA4 that track form submissions"

**Evidence:** Grow and Convert report that across dozens of client companies most could not name which blog post generated a demo request or which keyword drove a qualified lead.

**How to do it**

1. Define your single primary lead action: demo request, form submission or trial signup. Pick one.
2. Create a GA4 conversion event for that action and confirm it fires on the thank-you state, not on button click alone.
3. Build a GA4 exploration with landing page as the dimension and your conversion event as the metric.
4. Add session source and medium as a secondary dimension so organic is separable from paid and referral.
5. Verify the event with GA4 DebugView on a real submission before trusting any report.
6. Let it collect at least one full month before drawing conclusions on low-traffic pages.
7. Sort the landing-page report by conversions and check which intent type dominates the top rows.
8. Put that report in the monthly content review so traffic is never the only number on the page.

**Tools:** Google Analytics 4

**Pitfall:** Tracking only a site-wide conversion total makes every page look equally responsible. Teams then keep optimizing for traffic because it is the only per-page number they have, which entrenches top-of-funnel publishing.

**Apply at Pabau:** Before David judges which pabau.com articles are working, GA4 needs a demo-request conversion event with a landing-page report behind it. Otherwise the /blog/ traffic chart keeps deciding the calendar and the template pages get undercounted.

**Apply anywhere:** Create a GA4 conversion event for your single primary lead action, then build a landing-page report attributing those conversions to specific pages and sources. Without per-page conversion data, traffic becomes the default metric and the strategy optimizes for the wrong thing.

### 19. Set traffic goals against your own baseline, never against other companies  `165.8`
*core · best practices · source 165*

Asked what good traffic growth is, Hyam refuses the benchmark framing. He says the answer is subjective, that your business is unique, and that how much traffic you can drive depends on your industry. His replacement is competing against yourself with concrete step targets: if you previously had 5,000 blog visitors, can the new hire add 1,000 or 2,000 within the first couple of months, and reach 5,000 more within three months. The structure matters more than the numbers. It gives the hire a target derived from your own baseline, it sets checkpoints at two and three months rather than one annual review, and it removes the argument about whether a competitor's numbers are comparable. It also protects the hire from being judged against a case study written in a different industry.

> "Instead what you should do is compete against yourself"

**Evidence:** Hyam's worked example: from a 5,000-visitor baseline, target 1,000-2,000 added in the first couple of months and 5,000 within three.

**How to do it**

1. Pull the trailing three months of blog sessions and organic sessions to fix a baseline.
2. Set an increment target for month two, phrased as an addition to the baseline rather than a total.
3. Set a larger increment for month three, roughly matching your existing monthly baseline.
4. Agree the targets with the hire in writing at the start, not retroactively.
5. Review at the two-month and three-month checkpoints and adjust the slope, not the method.
6. Ban competitor traffic estimates from the review conversation unless the industry and site age genuinely match.

**Tools:** Google Analytics

**Pitfall:** Importing a growth target from a published case study sets a number your industry may not support, and the hire either burns out or games it with low-intent traffic.

**Apply at Pabau:** David should set pabau.com blog targets as increments over the trailing three-month baseline, reviewed at two and three months, rather than against competitor traffic estimates in aesthetics software.

**Apply anywhere:** Fix a baseline from your own trailing three months, then set increment targets for month two and month three. Do not benchmark against other companies, because industry and site age make the comparison meaningless.

### 20. Set up GA events to rank posts by conversions, not pageviews  `90.5`
*core · concrete actions · source 90*

Grow and Convert start the whole argument from a measurement step: set up events in Google Analytics that record product or service conversions coming directly from content, then read the blog report sorted by conversions rather than sessions. They define a conversion narrowly as a product-related signup or form fill, not an email or newsletter opt-in, because an opt-in can be earned by top-of-funnel traffic and hides the difference they are trying to see. Once the report is built the ranking usually reorders sharply. In one client report the sixteenth highest-traffic article brought only 1,612 pageviews but produced 39 product signups. In another, posts with almost identical traffic differed several times over in conversions. They also run GA's model comparison tool to see the picture with first-click conversions included, not only last-click.

> "you can set up events in Google Analytics"

**Evidence:** One client's sixteenth highest traffic article produced 1,612 pageviews and 39 product signups. Across the top ten converting posts on Grow and Convert's own site, only three were top of funnel and they accounted for 10% of conversions.

**How to do it**

1. Define the conversion event as a product signup, trial start or demo form fill; exclude newsletter and email opt-ins.
2. Create the event in Google Analytics and confirm it fires on the confirmation step, not the button click.
3. Build a report of organic landing page by sessions and by that conversion event side by side.
4. Sort by conversions descending and note which posts move up and which fall off entirely.
5. Calculate a conversion rate per post and flag every post that has produced zero conversions in the last several months.
6. Run GA's model comparison tool over the same period to see the list under first-click as well as last-click attribution.
7. Label each of the top converting posts with the framework it used: category, comparison, jobs-to-be-done, or top of funnel.
8. Use the labelled list to set the next quarter's publishing mix, and stop commissioning the framework that produces nothing.

**Tools:** Google Analytics

**Pitfall:** Counting newsletter signups as conversions makes top-of-funnel posts look successful and hides the effect the report exists to show. Many top-of-funnel posts will have produced no product conversions for months, which Grow and Convert say is extremely common.

**Apply at Pabau:** Pabau should track demo requests and trial starts as the blog conversion event, then rank blog posts by that event. Articles with high sessions and zero demo requests over six months are refresh or consolidation candidates, not successes.

**Apply anywhere:** Track a product signup or demo request as your blog conversion event, exclude newsletter opt-ins, then rank landing pages by conversions and check the same list under first-click attribution.

### 21. Set up the model comparison report in six specific clicks  `151.1`
*core · concrete actions · source 151*

Devesh Khanal of Grow and Convert gives the exact click path for reading content attribution in Google Analytics. Goals must exist first, tracking a thank-you page that is only reachable after a signup. The report itself lives under Conversions > Attribution. Pick one goal in the top-left selector, because leaving every goal highlighted rarely makes sense. Set the lookback window, which decides how far back GA looks for the first touchpoint of a conversion that happened inside your date range. Pick the attribution models to compare. Then change the primary dimension: click 'other' on the far right and search for 'Landing Page URL'. Finally type 'blog' into the search field to filter down to posts. He says that is largely it, and that navigating these reports is not hard.

> "The model comparison tool lives in Conversions > Attribution."

**Evidence:** Grow and Convert run this report for their own site and for agency clients, and also recorded a 45 minute webinar on setting up the goals it depends on.

**How to do it**

1. Create a conversion goal first that fires on a thank-you page reachable only after a signup or form fill.
2. Open the attribution report at Conversions > Attribution in Universal Analytics, or the equivalent model comparison view in GA4's advertising section.
3. Select a single goal in the top-left goal selector rather than leaving all goals highlighted.
4. Set the lookback window so GA knows how far back to search for the first touchpoint.
5. Add the attribution models you want side by side using the model selector.
6. Click 'other' on the far right of the primary dimension row and search for 'Landing Page URL'.
7. Type 'blog' into the table search field to filter the rows down to blog posts, or paste a single post URL.
8. Export the table so you have conversions per post rather than sessions per post.

**Tools:** Google Analytics

**Pitfall:** Leaving the primary dimension on the default source or channel means you never see which individual post drove the conversion, which is the only view that changes what you publish next.

**Apply at Pabau:** David should build this per-landing-page conversion view for pabau.com keyed to demo bookings, filtered to /blog/ and /templates/ URLs, so template pages and articles are ranked by demos rather than sessions.

**Apply anywhere:** Build a per-landing-page conversion report keyed to your real money event, filtered to your blog and resource URL patterns, so pages are ranked by conversions rather than sessions.
