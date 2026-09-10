# Measurement & GSC — supporting (part 2 of 4)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Expect a mixed first-last pattern for self-serve free trials  `151.10`
*useful · content insights · source 151*

Grow and Convert's SaaS client data shows a middle case. There are plenty of last-click free trial signups, but there are also several posts where the first-click model shows a lot more, sometimes double, the signups. Devesh explains this by decision weight: starting a self-serve free trial is not as flippant as joining an email list, but it is nowhere near as involved as contacting an agency about a project. So the attribution shape sits between the two extremes, and neither pure immediate-CTA thinking nor pure long-nurture thinking is right. The practical use is as a benchmark: if your self-serve product's blog shows near-identical first and last figures, your CTAs are probably capturing only the impulse segment.

> "sometimes double) the signups when you use a first click model"

**Evidence:** For a Grow and Convert SaaS client, several posts showed roughly double the signups under first click compared with last click, alongside many same-session signups.

**How to do it**

1. Run first versus last click for your trial signup goal across all blog landing pages.
2. Expect a mix rather than a single dominant pattern for a self-serve product.
3. Identify the posts where first click is roughly double last click and treat them as discovery assets.
4. Identify the posts where the two are close and treat them as closing assets with working CTAs.
5. Give the discovery posts an email capture step, and the closing posts a direct trial CTA.
6. Compare your ratio against the email-opt-in and high-ticket-service extremes to sanity-check your funnel design.

**Tools:** Google Analytics

**Pitfall:** Applying one CTA pattern across the whole blog wastes the discovery posts, whose readers are not ready to start a trial in that session.

**Apply at Pabau:** Pabau's demo request sits closer to the high-consideration end than a self-serve trial, so David should expect first click to exceed last click on most articles and plan CTAs accordingly.

**Apply anywhere:** For a self-serve product, expect a mixed pattern and split your CTAs: email capture on discovery posts, direct signup on closing posts.

### 2. Expect a two-week window before a consolidation fix shows  `49.6`
*useful · concrete actions · source 49*

After executing a cannibalization consolidation, follow a specific verification timeline rather than judging results too early: in week one, check only that the 301 redirects are functioning and that there are no 404 errors; from week two onward, expect ranking position volatility as Google re-processes which page is authoritative; only after that should the winning page start stabilizing at a better position, with total clicks for the target keyword trending up.

> "expect some position volatility while Google sorts things out"

**How to do it**

1. In the first week after consolidating, crawl or spot-check every 301 redirect to confirm it returns a 200 status on the destination page and that no losing-page URL now 404s.
2. Do not judge ranking impact during week one — treat it purely as a technical-verification period.
3. From week two onward, monitor the winning page's position for the target keyword in Google Search Console, expecting continued volatility rather than an immediate jump.
4. Track total clicks for the target keyword summed across what used to be multiple competing pages, rather than judging the winner page in isolation.
5. Confirm the fix worked once the winning page's position stabilizes at a better rank than any of the original competing pages achieved, with total clicks trending upward.

**Tools:** Google Search Console

**Pitfall:** Judging a consolidation as a failure during the first one to two weeks is premature — position volatility during this window is expected as part of Google re-processing the change, not evidence the fix didn't work.

### 3. Expect over 40% of conversions from positions 1 to 3  `135.12`
*useful · general insights · source 135*

Grow and Convert break their conversions down by ranking position, which is useful when deciding whether to push an existing post up or publish a new one. Posts in positions 1 to 3 produced 43.6% of all conversions and converted at 1.7% on average. Posts in positions 1 to 10 produced 57.4% of conversions at 1.27% average. So the top three positions delivered most of the value at roughly a third higher conversion rate than the wider page-one set, and everything below page one produced the remainder. Across the engagement the average position for all blog posts was 9. The practical reading is that moving a post from position 8 to position 3 is worth more than the raw click difference implies, because the conversion rate rises with the position too.

> "43.6% of conversions were from posts in positions #1-3"

**Evidence:** Grow and Convert: positions 1 to 3 produced 43.6% of conversions at 1.7% average conversion rate; positions 1 to 10 produced 57.4% at 1.27%; average position across all posts was 9.

**Tools:** Google Search Console

**Pitfall:** Judging a program by average position across all posts. Their average was 9, which looks mediocre while the top three positions were quietly producing 43.6% of conversions.

**Apply at Pabau:** Pabau's reporting should split conversions by position band, not just count them. Pages sitting at positions 4 to 10 on bottom-funnel terms are the refresh queue, because the move into the top three lifts both clicks and conversion rate.

**Apply anywhere:** Report conversions by position band. Posts in the top three positions convert around a third better than the rest of page one, so promoting a position 4 to 10 page is worth more than the click delta alone suggests.

### 4. Expect the exploration table to list every landing page, not just yours  `149.15`
*useful · content insights · source 149*

The most common misreading of the any-touchpoint report, which Grow and Convert spell out. The table under the totals is not a list of the URLs in your segment. It is a list of every landing page across every session belonging to the users who met the segment condition, with the users and conversion events for each. Because most users have more than one session, adding the users in each row nearly always gives a number larger than the Total users figure above. Their working method is to scan the table for their own URLs and read those rows as same-session or last-click conversions for that page. The row they walk through shows 10 of the 42 users landing on a post from google/organic, with conversions in those sessions.

> "it'll almost always add up to be larger"

**Evidence:** Grow and Convert's first table row shows 10 users landing on a post from google/organic and triggering 34 conversion events in those sessions, out of a 42-user segment.

**How to do it**

1. Do not treat the table as a filtered list of your segment URLs; it is not one.
2. Read each row as: users of the segment who at some point entered a session on that URL.
3. Never sum the row-level user counts to reconcile against the totals row.
4. Scan the table for your own URLs and read those rows as same-session conversions for that page.
5. Note the First user source and Session source on those rows to tell how the visit was acquired.
6. Limit conversion settings to one event before drawing conclusions from row-level conversion counts.
7. Ignore rows for pages outside your program, except as context on where those users also go.

**Tools:** Google Analytics 4

**Pitfall:** Analysts try to reconcile the row totals with the header total, conclude the report is broken, and abandon it; the discrepancy is expected because users have multiple sessions.

**Apply at Pabau:** Whoever reads this report at Pabau needs the multi-session caveat written into the report itself, or the first person to add up the rows will report the wrong demo number.

**Apply anywhere:** Document the multi-session caveat next to the exploration table, since row-level user counts sum to more than the segment total by design.

### 5. Filter the model comparison report to your own article URLs  `149.9`
*useful · concrete actions · source 149*

Grow and Convert restrict the model comparison table to the pages they are responsible for, so a client report shows only the conversions their work contributed. They add a filter with the plus button, choose the dimension Landing page and query string, then individually select the URLs of the blog posts they created under Dimension values. The gotcha they name is that a URL only appears in that value list once GA4 has registered it, and as far as they can tell that usually happens after a conversion has taken place on it. So a new post that has not converted yet will not be selectable at all, and its absence from the picker is not evidence it is failing. They also use the same filter mechanism for page, device and traffic-source cuts.

> "URLs will appear in this value section once GA4 has indexed"

**Evidence:** Grow and Convert report that URLs appear in the Dimension values list once GA4 has registered them, which in their experience is usually after a conversion has occurred.

**How to do it**

1. Click Add filter + in the model comparison report.
2. Set the Dimension to Landing page + query string.
3. Under Dimension values, select the URLs of the posts you want the report limited to.
4. Accept that a URL missing from the picker usually means no conversion has occurred on it yet, not that the filter is broken.
5. Keep a master list of the URLs in the program outside GA4, so you can tell missing-from-picker apart from forgotten.
6. Build parallel filters for platform, device and traffic source when you need those cuts.
7. Re-check the picker each month and add newly appearing URLs to the filter.

**Tools:** Google Analytics 4

**Pitfall:** Manually selected URL lists go stale the moment you publish, and because unconverted URLs are unselectable you cannot tell a new page from an omitted one without an external list.

**Apply at Pabau:** Pabau should keep a maintained list of the /blog/ and /templates/ URLs in the SEO program so the GA4 filter can be rebuilt without relying on what the picker happens to offer.

**Apply anywhere:** Keep an external master list of the URLs in your content program, because GA4's dimension-value picker only offers URLs that have already converted.

### 6. Find your converting topic type by analyzing why posts differ, not averaging  `110.16`
*useful · concrete actions · source 110*

Grow and Convert describe how they arrived at pain point SEO in the first place, working with Leadfeeder. At the start they believed, like everyone else, that top-funnel stories and topics drove growth. What changed their mind was looking at what was actually converting and trying to analyze why certain posts converted at a much higher percentage than others. The finding was that the topic of the blog post is what affects conversion rate most, and bottom-funnel posts converted far higher than the rest. Once they shifted the whole strategy to pain point SEO and stopped producing top-funnel stories, both traffic and conversions scaled quickly, reaching over 200 signups a month. The transferable part is the diagnostic method: analyze the outliers and ask why, rather than reporting blog averages.

> "trying to analyze why certain posts converted"

**Evidence:** Leadfeeder: Grow and Convert analyzed why individual posts converted at different rates, found topic was the driver, shifted entirely to pain point SEO and scaled signups to over 200 a month.

**How to do it**

1. Pull per-post conversion rates for the last twelve months rather than a blog-wide average.
2. Isolate the top five and bottom five posts by conversion rate, ignoring traffic.
3. For each of the ten, write down the topic type, the searcher's situation and the product connection.
4. Look for the variable the top five share and the bottom five lack.
5. State that variable as a rule, then commission the next three pieces against it.
6. Recheck after those pieces have three months of data before scaling further.
7. Stop producing the topic type shared by the bottom five, even if it drives traffic.

**Tools:** Google Analytics

**Pitfall:** Reporting a blog-wide conversion rate hides the pattern completely. The outliers carry the signal, and averaging them into a single number is why most teams never find their converting topic type.

**Apply at Pabau:** David should run this outlier analysis on pabau.com before the next planning cycle, comparing the five best and five worst articles by demo-request rate rather than reading a blog average.

**Apply anywhere:** Find your converting topic type by analyzing outliers, not averages. Compare the five highest and five lowest converting posts, name the variable the winners share, and commission against that rule before scaling.

### 7. Fire signup and payment events to the data layer via Google Tag Manager  `68.25`
*useful · concrete actions · source 68*

Cody's advice to his younger self about setting up a paid funnel properly. Use Google Tag Manager to create conversion actions for two events: the signup and the payment. You push each event to the data layer, then use GTM as a listener to send that information back to Facebook Ads and Google Ads, so you can see what a dollar in becomes in revenue out. The reason he treats this as foundational is cash flow rather than optimization. He gives real numbers from software he owned: $89 to acquire a customer, $39 average revenue per customer, roughly $600 customer lifetime value, so a 6x return, but two months before the money replenished in the bank. That gap between acquisition cost and payback period is the specific thing that kills bootstrapped software companies, and you cannot see it without the events wired up. His own rule was to reinvest 10% of revenue into marketing.

> "create a conversion action using Google Tag Manager"

**Evidence:** Cody's own figures: $89 acquisition cost, $39 average revenue per customer, about $600 lifetime value, roughly two months to payback.

**How to do it**

1. Define the two events that matter: account signup and first payment.
2. Push each event to the data layer when it fires in the application.
3. Create a Google Tag Manager listener for each data layer event.
4. Configure GTM to send the conversion back to both Google Ads and Facebook Ads.
5. Verify the events fire in GTM preview mode before spending on ads.
6. Compute cost per acquisition, average revenue per customer and lifetime value from real data, not estimates.
7. Compute the payback period in months and hold marketing spend within what your cash position supports.
8. Set a fixed share of revenue, such as 10%, to reinvest in marketing.

**Tools:** Google Tag Manager, Google Ads, Facebook Ads

**Pitfall:** A 6x lifetime return can still bankrupt you if payback takes two months and you spend faster than the cash returns. Cody names this gap as the specific problem with bootstrapping software.

**Apply at Pabau:** Pabau's demo-request and subscription events should both be wired as distinct conversions, so content-assisted signups can be separated from paid ones and payback measured per channel rather than blended.

**Apply anywhere:** Wire signup and payment as separate data-layer events through Google Tag Manager into both ad platforms, then compute payback period, not just return on ad spend. The payback gap is what sinks bootstrapped software.

### 8. Follow the channels report with source/medium before deciding anything  `154.5`
*useful · concrete actions · source 154*

Grow and Convert rate the Source/Medium report as equal in usefulness to the Landing Pages report, and they use it as the second step after the high-level channel view. Channels tell you that social converts badly; source/medium tells you which specific social platform or referring site the traffic came from and how each one actually converts. In their case it revealed where the bulk of referral and social traffic really originated, and how well each source converted, which is the level at which you can actually cut or double a spend. The sequence matters: the channel report frames the argument, the source/medium report tells you what to do about it. Acting on the channel report alone kills a channel when only one bad source inside it was dragging the average down.

> "on par with the Landing Pages report in terms of utility"

**How to do it**

1. Open Acquisition then All Traffic then Source/Medium with the thank you goal selected.
2. Sort by goal completions to see which named sources actually produce leads.
3. Then sort by goal conversion rate, filtered to sources with a meaningful session count, to find efficient sources hidden behind low volume.
4. Compare each source against the channel-level average to see which sources are dragging a channel down.
5. For any social or referral source producing leads at a good rate, look at what content those visitors landed on using landing page as a secondary dimension.
6. Cut or reduce only the specific sources that underperform, not the whole channel.

**Tools:** Google Analytics

**Pitfall:** Judging a whole channel from the channel report can retire a channel where one referrer or one platform was the only problem. The signal is a channel-level conversion rate far below the median of its own sources.

**Apply at Pabau:** For Pabau this matters most on referral traffic, where a handful of aesthetics industry sites and directories may convert far better than the referral average. Those are the sites worth pursuing more listings and content on.

**Apply anywhere:** This matters most on referral traffic, where a handful of niche industry sites may convert far better than the referral average. Those are the sites worth pursuing more listings and partnerships with.

### 9. Frame the SEO decision as pass or fail, never as a precise ROI figure  `129.19`
*useful · best practices · source 129*

Grow and Convert are direct that precise SEO ROI estimation is basically impossible before the fact, and they name why. You do not know where you will rank, how long it will take, how much traffic that ranking will actually generate — which they say is almost always far more than tools estimate — or the conversion rate you will get, which depends heavily on how well the product is sold in the article. Every one of those is a multiplicative unknown, so a model built from four uncertain inputs cannot produce a defensible number. Their instruction is to approach the whole exercise as a go/no-go or pass/fail decision and to resist getting overly precise. This is a process rule about how to present the analysis, not just about the arithmetic: a single ROI percentage handed to a stakeholder becomes a commitment, while a pass/fail verdict stays a decision.

> "Approach this part as a go/no-go or pass/fail decision"

**Evidence:** Grow and Convert list four unknowns — rank, time to rank, traffic from that rank, and post-ranking conversion rate — as the reason exact SEO ROI cannot be estimated.

**How to do it**

1. Write the output of the SEO business case as a single word: go or no-go.
2. List the four unknowns explicitly next to it — final position, time to rank, actual traffic per ranking, and post-ranking conversion rate.
3. Show the arithmetic as a range, with the conservative end using 1% conversion and volume-order traffic.
4. Refuse to publish a single ROI percentage as the headline number for stakeholders.
5. State that the estimate is a screening tool and that real numbers come from a five-to-ten article test.
6. Set the date when the estimate will be replaced by measured data.
7. After that date, report actuals and retire the estimate rather than comparing against it.

**Tools:** Spreadsheet (Sheets/Excel)

**Pitfall:** Handing a stakeholder a specific ROI percentage. It becomes the target the program is judged against, and since the underlying inputs were guesses, the program fails against a number nobody could have known.

**Apply at Pabau:** Pabau's internal case for a new page family should end in go or no-go with the assumptions listed, not in a projected lead number that later gets treated as a commitment in a marketing review.

**Apply anywhere:** Present the SEO business case as pass or fail, not as a percentage. List the four unknowns — where you will rank, when, how much traffic that rank brings, and the conversion rate after ranking — show the math as a conservative range, and set the date when measured data replaces the estimate.

### 10. GSC data lags 24-72+ hours and is only a sample  `21.6`
*useful · content insights · source 21*

David explains that Google stores search-performance data at a scale far beyond what Search Console exposes - what you see is described as 'a tiny, tiny subset' of all the click-through-rate testing Google actually runs. Search Console isn't connected to a fully live system, which is why data is normally about 24 hours out of date, and during any Google update (algorithmic or simply a software update) combined with the need to replicate across globally distributed search data centers, the lag can stretch to three, four, or even five days. He stresses this delay is normal and not a glitch, even though it regularly triggers 'is something broken?' questions from SEOs.

> "The data we get in Search Console is a tiny fraction"

**Evidence:** David's operational explanation: GSC reporting typically runs about 24 hours behind because it pulls from a non-live table, and during Google updates plus data-center replication, lag can extend to three to five days - normal behavior, not a bug.

**Apply:** Build reporting cadences and panic-thresholds that assume normal 24-hour (and occasionally multi-day, during updates) GSC data lag, and remember that any single day's numbers represent a small sample of Google's actual testing - so don't treat short-term dips or lag as evidence of a technical problem.

### 11. GSC hides data on 1M+ click sites until you filter twice  `49.9`
*useful · content insights · source 49*

On very high-volume sites (1 million+ clicks), Google Search Console's data behaves unreliably in a way relevant to cannibalization diagnosis: viewing the default, unfiltered chart for a selected page or query can show zero clicks and zero impressions, but applying a second filter on top makes the "missing" data reappear. This is attributed to GSC's data-withholding or privacy thresholds, and it compounds diagnostic difficulty because cannibalizing pages on these sites typically only rotate ranking position every few days, meaning a full diagnosis or remediation impact study can take about a week to complete reliably.

> "with 1 million+ clicks, data from Google Search Console becomes really weird"

**Evidence:** "We found that when the graph is at a default position for either a selected page or query, no data is shown. No clicks, no impressions. When data is filtered with a second filter, data magically appears... pages only rotate every few days, which means it can take a week to make a full diagnosis."

**Apply at Pabau:** When diagnosing suspected cannibalization on Pabau's higher-traffic pages in GSC, don't trust a page/query view that shows zero data at face value — apply a second filter (e.g., a date range or device filter on top of the query+page filter) before concluding there's no data, and budget roughly a week of observation for a reliable diagnosis rather than reacting to a single day's snapshot.

**Apply anywhere:** When diagnosing suspected cannibalization on your higher-traffic pages in GSC, don't trust a page/query view that shows zero data at face value — apply a second filter (e.g., a date range or device filter on top of the query+page filter) before concluding there's no data, and budget roughly a week of observation for a reliable diagnosis rather than reacting to a single day's snapshot.

### 12. Google's new Generative AI report in GSC has no click data  `02.3`
*useful · content insights · source 02*

Google's newer Generative AI performance report inside GSC is a step toward surfacing AI-specific data, but it ships without any click metric, so it can show that AI-surface impressions or citations exist without ever showing whether those appearances led to any click-throughs. This leaves site owners with two incomplete data sources that must be combined or cross-referenced: the standard performance report (which has click data but no AI-surface breakdown) and the new Generative AI report (which has AI-surface breakdown but no click data).

> "there is no click data there"

**Evidence:** Direct statement: 'there is no click data there' regarding the new Generative AI reporting, contrasted with 'You have click data in the performance reporting, AIO and AI Mode data is there, but it's not broken out by surface.'

**Apply at Pabau:** Treat the Generative AI report as a citation/visibility signal only, not a performance metric, and continue to rely on the workaround of exporting full query data and classifying it (e.g., via Claude) whenever click-level performance on AI-surfaced queries needs to be assessed for Pabau.

**Apply anywhere:** Treat the Generative AI report as a citation/visibility signal only, not a performance metric, and continue to rely on the workaround of exporting full query data and classifying it (e.g., via Claude) whenever click-level performance on AI-surfaced queries needs to be assessed for your own site.

### 13. Group keywords by topic in GSC to gauge topical authority  `53.7`
*useful · concrete actions · source 53*

To assess topical authority rather than judging any single keyword in isolation, David Quaid recommends building sub-reports that group your ranking keywords by topic in Google Search Console. A spread-out distribution, his example is three keywords at position one, three at position five, three at position fifteen, indicates topical authority is still developing, whereas a topic where you hold roughly 20 keywords all within the first two positions means you're effectively the topic authority for the internet on that subject. He pairs this with a warning against reading click-through rate in aggregate at all: a site-wide or page-level top-line CTR figure makes no sense, since CTR is only meaningful when read at the individual keyword-per-page level, where you can see whether performance is trending up, down, or oscillating like a sine wave over a period such as three months.

> "you're pretty much the topic authority for the internet"

**How to do it**

1. In Google Search Console, filter the Queries list to a single topic or subject area your site covers.
2. Record each keyword in that topic along with its current average position, building a simple grouped sub-report, e.g., in a spreadsheet export from GSC.
3. Assess the spread: if positions are scattered across many ranks, e.g., some at 1, some at 5, some at 15, treat topical authority for that subject as still developing.
4. If a large share of keywords in that topic, the source's benchmark is around 20 keywords, sit within the first two positions, treat that topic as one where you already hold strong topical authority.
5. Never evaluate click-through rate at a site-wide or page-level aggregate; instead pull CTR at the individual keyword-per-page level.
6. Plot that keyword-per-page CTR or position over a period such as 3 months and check whether it's trending steadily, or oscillating up and down, to judge whether the topic is still being fought for.

**Tools:** Google Search Console

**Pitfall:** Reading click-through rate as a single top-level number is explicitly called out as making no sense — the only meaningful read is at the keyword-per-page level, since aggregating hides exactly the topic-by-topic or keyword-by-keyword rotation that signals whether authority is still developing.

### 14. Judge JTBD posts by trial signups over months, not by traffic  `93.18`
*useful · best practices · source 93*

Every result Goolding reports for a JTBD post is a signup count over a stated window, never a traffic number: 20 free trial signups in the first 6 months for Timetastic's Outlook post, more than 40 across 9 months for the two spreadsheet-template posts, thousands since 2020 for Circuit's Google Maps post. That is deliberate, because JTBD keywords sit mid-funnel and their traffic looks unimpressive next to top-of-funnel terms while converting far better. The measurement rule that follows is to attribute signups per post and give each post several months before judging it, since a post published in 2020 was still compounding years later. Reading a JTBD post on sessions alone leads teams to cut the pages that actually produce customers.

> "This post generated 20 free trial signups in the first 6 months"

**Evidence:** Timetastic Outlook post: 20 signups in 6 months. Two spreadsheet-template posts: 40+ signups in 9 months. Circuit Google Maps post: thousands of signups since 2020.

**How to do it**

1. Tag every JTBD post in analytics so signups can be attributed to the landing page.
2. Report signups per post, with the publication date and the window, rather than sessions.
3. Set the first review at 6 months, not at 30 or 90 days.
4. Compare signups per post across the category, comparison and JTBD cohorts to see the real conversion gap.
5. Keep posts that convert at low traffic and refresh them rather than consolidating them away.
6. Cut posts that draw traffic but produce no signups after two review windows.
7. Recheck long-lived posts annually, since the Circuit post kept compounding for years.
8. Feed the signup data back into keyword selection so the next batch mirrors what converted.

**Tools:** Google Analytics

**Pitfall:** A traffic-based content report ranks JTBD posts near the bottom, so they get pruned in the next content audit even though they produce the signups.

**Apply at Pabau:** Pabau should attribute demo requests per blog URL and review how-to articles on a 6-month window, so low-traffic clinic-task posts that produce demos are kept and expanded.

**Apply anywhere:** Attribute signups per post and review jobs-to-be-done content on a six-month window, because judging it on sessions will delete the pages that convert.

### 15. Leave recent page-2 pages alone; they need time or links, not a rewrite  `130.10`
*useful · best practices · source 130*

Grow and Convert report that 16% of their client's pages sat on page 2 and 5% on page 3, and they attribute that specifically to recency. The pages ranking on page 2 and further are mostly recently published pieces that just need time, or links, to reach page 1. Their diagnostic is therefore chronological before it is editorial: check publish date before deciding a page-2 page underperforms. This matters for a program running at roughly 40 pieces a year, because a steady state will always show a tail of recent pages on page 2, and that tail is a sign of publishing pace, not of quality problems.

> "mostly recently published pieces that just need time (or links)"

**Evidence:** Grow and Convert: 16% of pages on page 2 and 5% on page 3, described as mostly recent pieces awaiting time or links.

**How to do it**

1. Pull every target keyword with its ranking position and the page's publish date into one sheet.
2. Segment page-2 and page-3 pages by age: under six months versus over six months.
3. Leave the under-six-month group alone and let it settle.
4. For the over-six-month group on page 2, check whether the gap to page 1 is content depth or referring domains.
5. Where competitors on page 1 have more referring domains, treat it as a link problem and point internal links at the page from pages that already rank.
6. Where the content misses part of the query intent, re-optimize rather than build links.
7. Recheck the sheet quarterly and expect a permanent tail of recent pages on page 2.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Rewriting a six-week-old page because it sits on page 2 wastes the effort and resets whatever ranking momentum it had. The tell is that the page is still climbing week over week when you intervene.

**Apply at Pabau:** Pabau's ranking reports should show publish date next to position so recent pages are not queued for a refresh. Only pages over six months old and stuck on page 2 should enter the /SEO refresh queue.

**Apply anywhere:** Put publish date next to position in your ranking report. Page-2 pages under six months old need time or links, not a rewrite. Only escalate the ones stuck there past six months, and split those into link problems and intent problems before acting.

### 16. Leave the GA4 default model alone and build custom reports instead  `149.6`
*useful · best practices · source 149*

You can change the account-wide attribution model in GA4 under Admin then Attribution Settings, and that changes what every default report shows. Grow and Convert deliberately do not do this. They leave the property default on data-driven attribution and build custom reports that use other models on top. The reasoning is practical: changing the default silently rewrites what every stakeholder sees in the standard reports, including historical-looking comparisons, and you lose the data-driven view as a cross-check. Building separate reports keeps both views available and makes the model an explicit choice per report rather than a hidden global setting somebody forgets was changed.

> "we have left our default setting as data-driven"

**Evidence:** Grow and Convert state they left the default on data-driven attribution and use custom reports with other models to get the most accurate picture they can.

**How to do it**

1. Leave Admin > Attribution Settings on the data-driven default.
2. Build the model comparison and any-touchpoint reports separately for rules-based views.
3. Label every custom report with the attribution model it uses, in the report name.
4. If someone does change the property default, record the date, because report comparisons across it are not like for like.
5. Present the default report and the rules-based reports side by side rather than replacing one with the other.
6. Re-check Attribution Settings during any analytics handover, since it is a single dropdown with account-wide effect.

**Tools:** Google Analytics 4

**Pitfall:** Flipping the account default is a one-click change with account-wide effect and no visible marker in reports, so numbers appear to shift for no reason months later.

**Apply at Pabau:** Pabau should not change the property-level attribution setting to make blog numbers look better; add named custom reports instead so the default stays a stable baseline.

**Apply anywhere:** Keep the property-level attribution default untouched and express model choices in named custom reports instead.

### 17. Low-volume keyword rankings are fragile and can silently reverse  `22.4`
*useful · content insights · source 22*

In the source's own tracked case, a page targeting a low-competition keyword reached position one "out of nowhere" about a year and a half after publishing, but because the keyword's search volume was so low, the page received too few clicks for Google to gather meaningful signal about it — reasoned as "Google doesn't have enough information to discern the value of the page" — and it subsequently fell back out of the index, still being judged by the topical authority the site had at its original publish date. This shows a low-volume-keyword ranking is a fragile, easily-reversed state distinct from an authority-based ranking failure, since click-signal starvation becomes a second failure mode that can undo even a temporary win.

> "Google doesn't have enough information to discern the value"

**Evidence:** The source's own tracked page, first published March 2023, briefly ranked #1 roughly 18 months later before dropping back out of the index.

**Apply at Pabau:** For Pabau pages targeting low-volume, easy long-tail keywords, don't treat a brief #1 ranking as a stable win — keep tracking the keyword afterward, and be ready to apply the republish-under-new-URL fix if the page drops back out of the index.

**Apply anywhere:** For your pages targeting low-volume, easy long-tail keywords, don't treat a brief #1 ranking as a stable win — keep tracking the keyword afterward, and be ready to apply the republish-under-new-URL fix if the page drops back out of the index.

### 18. Measure a keyword theme by its share of total blog conversions  `109.12`
*useful · concrete actions · source 109*

Grow and Convert report Cognitive FX's deviant-keyword bet with a metric most content teams never produce. The articles targeting PCS-related terms accounted for 23% of all blog conversions in the month before the article was written, and according to Olivia Seitz those articles consistently drive 20 to 25% of blog conversions every month. That is the number that justifies overriding the clinical team's objection to the terminology. Pageviews would not have done it, and per-article conversion counts would have looked small spread across dozens of posts. Grouping the pages into a named keyword theme and reporting the theme's share of total conversions is what makes an unusual keyword bet defensible and repeatable.

> "23% of all blog conversions in the month prior to us writing"

**Evidence:** Cognitive FX: PCS-term articles drove 23% of all blog conversions in one month and 20-25% consistently month to month.

**How to do it**

1. Tag every published post with the keyword theme it targets, not just its URL.
2. Set up conversion tracking on the blog for the action that matters: trial signup, inquiry, call.
3. Report conversions grouped by keyword theme monthly, as a share of total blog conversions.
4. Compare each theme's conversion share to its traffic share to find themes that punch above their volume.
5. Hold the report for at least three consecutive months before drawing a conclusion, since a single month is noisy.
6. Use the theme's conversion share, not pageviews, when arguing for more content in that theme.
7. Kill themes whose conversion share stays near zero regardless of traffic.
8. Publish the number internally so subject-matter experts see what the disputed terminology earned.

**Pitfall:** Reporting per-article conversions makes any theme spread across dozens of posts look trivial, and the theme gets cut. Aggregate before you judge.

**Apply at Pabau:** Pabau should tag blog posts by keyword theme and report conversion share per theme monthly. That is the evidence needed to decide whether to keep investing in a given content cluster on pabau.com.

**Apply anywhere:** Tag posts by keyword theme and report conversions per theme as a share of the blog's total, monthly, over at least three months. Themes spread across many posts look worthless per article and obvious in aggregate.

### 19. Measure content ROI per page, never the blog as a single unit  `145.8`
*useful · best practices · source 145*

Grow and Convert's answer to the two questions teams cannot answer, what is our ROI from content and what should we expect it to be, starts with a measurement rule: do not measure all content as a whole, measure the ROI of individual pieces. The reason follows from their own data. Conversion rates differ by an order of magnitude between buying-intent and low-intent posts, so a blend hides both the winners worth scaling and the losers worth cutting. A blog-level average also moves whenever the traffic mix moves, which makes it useless for deciding what to publish next. They pair this with published benchmarks: 1% to 5% for a page ranking on bottom-funnel keywords, and 0.5% to 2% blog-wide.

> "measure all content as a whole"

**Evidence:** Grow and Convert's benchmarks: 1% to 5% per bottom-funnel page, 0.5% to 2% for a blog largely made of bottom-funnel pieces.

**How to do it**

1. Build a per-URL report of organic sessions and conversions rather than a single blog total.
2. Attach each URL's target keyword and its intent classification to the row.
3. Calculate conversion rate per URL and compare against the 1% to 5% bottom-funnel benchmark.
4. Compute the blog-wide rate separately and compare it against the 0.5% to 2% range, as a portfolio check only.
5. Rank URLs by conversions, then by conversion rate, and treat the two lists as different questions.
6. Scale the format and keyword type of the top converters into new briefs.
7. Refresh or repoint the low converters instead of averaging them away.
8. Recalculate quarterly so the traffic mix cannot flatter the blend.

**Tools:** Google Analytics 4, Google Search Console

**Pitfall:** A blog-wide conversion average that looks acceptable while most pages convert near zero and two pages carry everything. The signal you have hit it is that no one can name which posts produce leads.

**Apply at Pabau:** David should keep a per-URL conversion table for Pabau's /blog/ and /templates/ pages, judge each against the 1% to 5% band, and commission new pieces that copy the keyword type of the top converters.

**Apply anywhere:** Report content ROI per URL, not as one blog figure. Judge bottom-funnel pages against 1% to 5% and the whole blog against 0.5% to 2%, and treat those as two separate questions.

### 20. Measure content conversion separately from homepage and landing pages  `147.11`
*useful · best practices · source 147*

Grow and Convert stop three times to insist on the scope of the number they are benchmarking. They are not talking about conversion rates from a landing page, not from the homepage, but from content, meaning blog posts. The reason it matters is that landing pages and homepages carry far higher intent and produce rates several times larger, so a blended site-wide figure makes a blog look fine when it is converting near zero. They pair this with a second scoping rule: as traffic increases, expect conversion rates to decrease, which they state for both the email rate and the direct rate. Both rules point the same way. Any benchmark you compare against has to match the page type and the traffic band, or the comparison is meaningless.

> "We're talking about conversion rates from content"

**Evidence:** Grow and Convert exclude landing pages and the homepage explicitly, and state twice that rates fall as traffic rises.

**How to do it**

1. Create a GA4 segment or explore report restricted to blog and article URL paths.
2. Create a second segment for the homepage and dedicated landing pages.
3. Report the two conversion rates separately and never publish a blended site figure as the content number.
4. Record monthly unique visitors alongside each rate so the traffic band is visible with the number.
5. Compare each period against the same traffic band, not against a period when the blog was much smaller.
6. When traffic grows and the rate falls, check absolute conversions before calling it a regression.

**Tools:** Google Analytics

**Pitfall:** Reporting one site-wide conversion rate. High-intent homepage and landing-page traffic props up the average and hides a blog converting near zero.

**Apply at Pabau:** David should split pabau.com reporting into blog and template pages versus the homepage and demo landing pages, and record monthly uniques next to each rate so a falling percentage on rising traffic is not read as a decline.

**Apply anywhere:** Split your reporting into content pages versus homepage and landing pages, and record monthly uniques next to each rate so a falling percentage on rising traffic is not misread as a decline.

### 21. Measure content on sales attributable to it, not pageviews  `112.18`
*useful · best practices · source 112*

Grow and Convert list the consequences of the standard B2C content approach in measurement terms: no measurable ROI because the content does not lead to sales, ineffective brand building because the lifestyle content does not generate positive awareness, and low SEO impact because competitors outrank them and the high-value keyword opportunities go untouched. Their prescription throughout is to define an actual business metric rather than a vanity metric like organic traffic or pageviews, calculate the leads per month needed to break even on spend, and track progress against that. They also note that content marketing attribution needs the right attribution model in analytics, because a single last-click view will not show which articles carried a purchase. The point is that the strategy and the measurement have to change together, since traffic reporting reverses the content sequence.

> "No measurable ROI: Their content doesn't lead to sales."

**Evidence:** Grow and Convert's ROI measurement process defines a business metric, sets up analytics, calculates leads needed for breakeven, and tracks progress, with a spreadsheet template.

**How to do it**

1. Pick one business metric, sales or qualified leads attributed to content, and delete pageviews from the primary report.
2. Calculate the monthly conversions needed to break even on your content spend and put that number at the top of the report.
3. Configure analytics with an attribution model that credits assisting content, not last click only.
4. Tag every article with its keyword type: product, pain point, use case, lifestyle.
5. Report conversions by keyword type each month so the sequence is defended by data.
6. Review any article with traffic and no conversions after six months, and decide whether to repoint or retire it.
7. Recheck the breakeven number whenever price or agency cost changes.

**Tools:** Google Analytics

**Pitfall:** Reporting organic traffic as the headline metric makes lifestyle posts look like the winners and quietly pushes purchase-intent pages down the calendar.

**Apply at Pabau:** Pabau's content reporting should lead with demos or trials attributed to content and the breakeven demo count, with sessions as a secondary line. David should tag each published article by keyword type so the monthly report can compare conversions by type rather than by page.

**Apply anywhere:** Report content on sales or qualified leads attributed to it, with the breakeven figure printed at the top, and keep pageviews as a secondary line. Tag every article by keyword type so you can compare conversions across purchase-intent and awareness content.

### 22. Measure the article change on the destination page's own traffic  `138.12`
*useful · concrete actions · source 138*

Nat Eliason's proof that the collection CTAs worked is not a blog metric. He shows traffic to the black tea collection page growing significantly after the change, and traffic arriving at a brand new 'best teas for weight loss' collection that had no other source. Reading the destination page rather than the source article is the cleaner measurement, because the collection had close to no traffic before and every visit is attributable to the article. It also survives the attribution gaps that make per-article revenue reporting unreliable. The new-collection case is the strongest form: a page created for one article, with no navigation link and no ad spend, so its entire session count is the article's contribution.

> "we can see that its traffic has grown significantly since implementing these changes"

**Evidence:** Cup & Leaf show the black tea collection's traffic rising after the CTA change, and a brand new 'best teas for weight loss' collection receiving traffic it had no other way to get.

**How to do it**

1. Record the destination collection or feature page's sessions for the 30 days before you add the article CTAs.
2. Add the CTAs, and note the exact date in an annotation.
3. Leave the destination page out of the main navigation where you can, so the article is its dominant traffic source.
4. Compare sessions for the 30 days after against the 30 days before on the destination page, not on the article.
5. Segment the destination page's traffic by referrer to confirm the article is the source.
6. For newly created destinations, treat the entire session count as the article's contribution.
7. Compare conversion rate on the destination page against your generic landing pages to check the qualified-traffic claim.
8. Repeat per article-destination pair rather than reporting one blended number.

**Tools:** Google Analytics, Shopify

**Pitfall:** Adding the new collection to the site navigation at the same time as the article CTAs. You then cannot separate article-driven traffic from browse traffic, and the measurement is lost.

**Apply at Pabau:** When Pabau adds an early CTA from an article to a feature page, baseline that feature page's sessions first and read the change there. It is a cleaner signal than trying to attribute demo requests back to the article.

**Apply anywhere:** Baseline the destination page's sessions before adding article CTAs and measure the change there rather than on the article. Keep newly built destinations out of the navigation so the article is their only traffic source.

### 23. Model expected conversions from position share before choosing a format  `146.13`
*useful · concrete actions · source 146*

Grow and Convert make the traffic-versus-rate trade explicit with a number. On average, results in positions one to three receive roughly 60% of organic traffic. So even where a list post does convert at a lower rate than a product landing page, which their own data suggests is often not the case anyway, the extra traffic from a top-three position can still produce a higher volume of conversions. That turns the format decision into arithmetic rather than preference. Estimate the position each format can realistically reach, apply the click share, multiply by the conversion rate you have measured for that format on your own site, and compare the totals.

> "search results in position 1-3 receive ~60% of organic traffic"

**Evidence:** Grow and Convert cite roughly 60% of organic traffic going to positions one to three as the basis for preferring the format that can reach the top three.

**How to do it**

1. Pull the monthly search volume for the target keyword from your keyword tool.
2. Estimate the highest position each candidate format can realistically reach on that SERP, based on your authority and what currently ranks.
3. Apply a click-share model, using roughly 60% of organic traffic going to positions one to three, to convert position into expected sessions.
4. Use your own measured conversion rate for each format from the matched-keyword comparison, not a published benchmark.
5. Multiply sessions by rate for each format and compare expected monthly conversions.
6. Pick the format with the higher expected total, even if it has the lower rate.
7. Re-run the model once the page has ranked for three months with real position and conversion data.

**Tools:** Ahrefs

**Pitfall:** Running the model with a borrowed conversion rate. Published benchmarks come from other traffic mixes and will usually flatter the landing page option.

**Apply at Pabau:** David should build this as a small sheet for Pabau keyword decisions, holding volume, realistic position, click share and Pabau's own measured per-format conversion rates, and run it before commissioning any bottom-of-funnel page.

**Apply anywhere:** Build this as a small sheet holding volume, realistic position, click share and your own measured per-format conversion rates, and run it before commissioning any bottom-of-funnel page.

### 24. Move conversion tracking to a spreadsheet once GA starts sampling  `141.13`
*useful · concrete actions · source 141*

Grow and Convert note that for their highest-traffic client they had to measure conversions out of a spreadsheet rather than in Google Analytics, because the site had enough traffic that GA sampled the data. Sampling means the reported conversion figures are extrapolated from a subset, which is fine for trend shape and unreliable for the per-post attribution their strategy depends on. Their workaround was to maintain the conversion count manually and chart it over the whole engagement, which let them show a fairly linear increase crossing 150 signups a month. The general rule this implies: once a property is large enough to sample, stop trusting the interface for the numbers you report externally and build the record yourself from an unsampled source.

> "we have to measure conversions out of a spreadsheet"

**Evidence:** Grow and Convert's B2B SaaS client had enough traffic that GA sampled the data, so conversions were tracked in a spreadsheet, showing a linear rise past 150 signups a month.

**How to do it**

1. Check whether your GA reports carry a sampling notice on the date ranges you report from.
2. If they do, stop pulling headline conversion numbers straight from the interface.
3. Export conversions at the lowest granularity available, ideally per landing URL per month, and store them in a spreadsheet.
4. Where possible pull the same numbers from an unsampled source such as the CRM or the signup database and reconcile the two.
5. Maintain the spreadsheet monthly so the series is continuous rather than rebuilt each report.
6. Chart conversions per month for the full engagement so the trend line, not a single month, carries the argument.
7. Keep per-post conversion counts in the same sheet so link-building and refresh decisions still have unsampled data.

**Tools:** Google Analytics, Google Sheets

**Pitfall:** Reporting sampled GA conversion numbers on a high-traffic site produces figures that move when the date range moves, which destroys credibility the first time a client cross-checks against their own signup database.

**Apply at Pabau:** Pabau should reconcile content-attributed demo requests against the CRM record rather than relying on analytics alone, and keep a running monthly sheet per section so the trend survives any analytics migration.

**Apply anywhere:** When your analytics starts sampling, stop reporting conversions from the interface. Export at per-URL, per-month granularity into a spreadsheet, reconcile against the CRM or signup database, and maintain the series continuously so the trend line is unsampled.

### 25. Name conversion events in underscore case per business action  `149.3`
*useful · best practices · source 149*

Grow and Convert give a naming convention for GA4 custom events: words separated by underscores, describing the business action rather than the page. Their own is Agency_Lead. They suggest Demo_Signup for a SaaS business and Product_Purchase for ecommerce. The reason the convention matters beyond tidiness is that this string has to be retyped exactly when you register the conversion event in the Conversions section, and it is the string you will search for in every report, filter and segment afterwards. A name that describes the URL rather than the action ages badly, because the thank-you page can move while the action does not.

> "The standard format for this is to use an underscore"

**Evidence:** Grow and Convert use Agency_Lead in their own property and cite Demo_Signup and Product_Purchase as the SaaS and ecommerce equivalents.

**How to do it**

1. Write the list of commercial actions you want to count before touching GA4.
2. Name each one after the action, not the page: Demo_Signup, Trial_Start, Product_Purchase.
3. Use underscores between words and keep capitalization consistent across the whole account.
4. Record the exact strings in a shared document so the Conversions registration step can be copy-pasted.
5. Avoid encoding the URL or campaign in the name, since both change while the action does not.
6. Reuse the same names across properties if you run more than one site, so cross-property reporting works.

**Tools:** Google Analytics 4

**Pitfall:** Ad-hoc naming produces a Conversions list nobody can read six months later, and the exact-match retype step in the Conversions section starts failing on capitalization.

**Apply at Pabau:** Pabau should agree on strings like Demo_Request and Template_Download before adding events, so reports across the blog, templates and code-reference sections can be compared.

**Apply anywhere:** Agree on action-based, underscore-cased event names before adding GA4 events, so reports across site sections stay comparable.
