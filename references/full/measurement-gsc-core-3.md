# Measurement & GSC — core (part 3 of 5)

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Kill the unmeasurable thought leadership argument with a first-click cohort report  `110.2`
*core · concrete actions · source 110*

Grow and Convert take on the standard defense of top-of-funnel content: it is thought leadership and you cannot measure it. Their answer is that you can measure it and most agencies simply do not. They use Google Analytics first-click attribution, which counts anyone who landed on a post and came back to convert within 90 days, against last-click, which only counts same-session conversions. Running both for a client, the high-traffic mid-funnel post had 14 first-click conversions to their bottom-funnel post's 11, but the conversion rates were 0.07 percent versus 0.57 percent. Their point is that the measurement is imperfect and gives a lower-limit estimate, which is enough to show which topics drive the majority of conversions. So nobody gets to hand-wave.

> "It's generating business, I swear; you just can't see it"

**Evidence:** Client three-month report: high-traffic post 14 first-click conversions at 0.07 percent, Grow and Convert's bottom-funnel post 11 first-click conversions at 0.57 percent; on last click 0.52 percent versus a 0.08 percent blog average.

**How to do it**

1. Tag every blog URL with a funnel label: top-of-funnel, pain-point or product-intent.
2. Pull the Google Analytics landing pages report for a three-month window with sessions and goal conversions.
3. Record last-click conversions and conversion rate per URL.
4. Run the model comparison tool for first-click over the same window to catch people who converted within 90 days of first landing.
5. Join both to the funnel labels and average conversion rate by cohort, not by post.
6. Present the two cohorts side by side and state explicitly that this is a lower-limit estimate, not full attribution.
7. Ask the thought leadership advocate what number would change their mind, before showing the chart.
8. Re-run quarterly so the comparison survives seasonality.

**Tools:** Google Analytics

**Pitfall:** Comparing single posts instead of cohorts. Grow and Convert's own data shows a top-funnel post can beat a bottom-funnel post on absolute conversions while losing eight-fold on rate, so a one-post comparison lets the advocate pick the winner.

**Apply at Pabau:** David should label every pabau.com /blog/ URL by funnel stage and run last-click and first-click cohort reports before the next content plan. Template pages and code-reference pages need their own cohorts because their intent differs sharply from general blog explainers.

**Apply anywhere:** Do not accept that top-funnel content's value is unmeasurable. Label every blog URL by funnel stage, pull last-click and first-click conversion data for a three-month window, and compare cohort averages rather than individual posts.

### 2. Know what first click and last click actually count before reporting them  `149.17`
*core · content insights · source 149*

Grow and Convert give working definitions rather than model names. A last-click conversion means the blog post was the landing page of the session in which the visitor converted, so the page was the entry point of their last session before converting. A first-click conversion means the post was the first page viewed in the user's very first session, the page that brought them to the site at all, and that user converted at some point in the following 90 days. They argue this concreteness is the advantage of rules-based models over data-driven attribution: you can state exactly what a row means to a business, whereas with the algorithm you cannot. The 90-day window is the number to state out loud when reporting first click.

> "converted at some point later within the next 90 days"

**Evidence:** Grow and Convert define first click as the entry page of the user's first session with a conversion within the next 90 days, and last click as landing page of the converting session.

**How to do it**

1. Write the two definitions into the report so nobody has to guess what the column counts.
2. Report last click as: user landed on this page and converted in that same session.
3. Report first click as: this page brought the user to the site and they converted within 90 days.
4. State the 90-day window explicitly whenever you quote a first-click figure.
5. Expect first click to credit top-of-funnel and discovery content and last click to credit closing pages.
6. Show both columns for the same period rather than choosing the flattering one.
7. Use rules-based figures, not data-driven ones, when you need to explain to a stakeholder exactly what a number means.

**Tools:** Google Analytics 4

**Pitfall:** Quoting a first-click number without the 90-day window invites the reasonable objection that the conversion happened for other reasons months later.

**Apply at Pabau:** Pabau's content reporting should carry both definitions in writing next to the numbers, because a demo booked 60 days after reading a template page is a real content win that a last-click read would erase.

**Apply anywhere:** Write the first-click and last-click definitions, including the 90-day window, next to the numbers in every content report.

### 3. Make 'how did you hear about us' a required signup field  `65.1`
*core · concrete actions · source 65*

Cody's simplest measurement tactic, which he says he has used for years: put a required 'how did you hear about us' field in the signup form. What makes it worth doing is the discrepancy - he says it is always shocking to compare that self-reported data against what the analytics data shows. The specific finding he has drawn from it over the last eighteen months is a shift in what people say: they increasingly name social media as the source of discovery, which is a dramatic contrast with three years ago. He notes he works in B2B so there's always a lag behind what happens in direct-to-consumer first. The reason this matters is that organic social is extremely hard to put an ROI number on - whether that's founder marketing or sponsoring creators - so the self-reported field is one of the only direct reads you get.

> "required field within your sign up form"

**How to do it**

1. Add a 'how did you hear about us' field to the signup form and make it required.
2. Keep the options broad enough to be answerable - social, search, referral, podcast, event - with a free-text option.
3. Report it monthly alongside your analytics attribution, deliberately comparing the two.
4. Treat the divergence between them as the finding, not as an error in one of them.
5. Watch the trend over quarters rather than reading single months.
6. Use it specifically to sanity-check channels analytics can't attribute, like organic social and podcasts.

**Tools:** Google Analytics 4

**Pitfall:** Self-reported attribution is unreliable in absolute terms - people name the last thing they remember. Its value is the trend and the divergence from analytics, not the percentages.

**Apply at Pabau:** A required 'how did you hear about us' field on Pabau signups and demo requests would be the only direct read on whether the podcast, LinkedIn and creator work is producing anything - analytics cannot attribute those.

**Apply anywhere:** A required 'how did you hear about us' field on signups and demo requests is the only direct read on whether the podcast, social and creator work is producing anything - analytics cannot attribute those.

### 4. Make leads, not traffic, the reported ROI number for content  `132.11`
*core · best practices · source 132*

Grow and Convert name lead tracking as the paired half of their bottom-funnel-first strategy, not an afterthought to it. They track leads rather than just traffic to measure ROI from content marketing, and that measurement choice is what makes the funnel-stage prioritization visible at all. The two decisions reinforce each other: if you report traffic, top-funnel content always looks like the winner because it drew 204,303 sessions against 28,190. If you report leads, the same comparison flips to 1,348 against 397. Grow and Convert stress that their client results across multiple posts show the same conversion-rate ordering. The rule to adopt is that no content report goes out with sessions as its headline metric, because the metric selection silently makes the strategy decision.

> "we track leads (rather than just traffic) to measure ROI from content marketing"

**Evidence:** Grow and Convert's Geekbot reporting: 1,745 leads across 232,493 sessions, with the lead split reversing the ranking that the traffic split implies.

**How to do it**

1. Define the single conversion event that counts as a content lead, such as a trial start or a demo request.
2. Set that event up in analytics so it can be reported by landing page.
3. Rebuild the monthly content report so leads by landing page is the first table and sessions is secondary.
4. Add a per-post lead count to the content calendar so each commissioned piece is judged on the same number afterwards.
5. Report leads per stage alongside sessions per stage, so the ratio between the two is always on the page.
6. When comparing two keyword candidates, present expected leads for each and leave sessions out of the recommendation.
7. Review any post with high sessions and zero leads over six months, and either rework it toward the pain point or stop linking budget to it.

**Tools:** Google Analytics

**Pitfall:** A traffic-led report makes the wrong keyword look right every month, and nobody notices because the chart goes up. The signal is a blog whose sessions have doubled while signups are flat.

**Apply at Pabau:** Pabau's content reporting should lead with demo requests by landing page, with sessions as a secondary column. That single change makes the case for building more competitor-comparison and specialty pages rather than more industry guides, without anyone having to argue it.

**Apply anywhere:** Put leads by landing page at the top of every content report and demote sessions to a secondary column. The metric you headline quietly makes your keyword strategy, and a traffic-led report will always favor informational content over the pages that actually convert.

### 5. Max the lookback window at 90 days every single time  `151.2`
*core · best practices · source 151*

Grow and Convert set the lookback window to its maximum and say they see no reason not to. The window controls how far back Google Analytics searches for a user's first touchpoint when crediting a conversion that landed inside your reporting date range. A 30 day setting means a conversion today only looks 30 days back, so a reader who found you six weeks ago through a post gets credited to whatever page they landed on today, usually the homepage. Because the maximum in Google Analytics is 90 days, that is also the hard ceiling on what any first-click report can ever see. Devesh treats 90 as the default and then separately warns that anything beyond it is structurally invisible.

> "We see no reason not to max this out at 90 days."

**Evidence:** Grow and Convert use 90 days on their own high-value B2B service reporting and say some prospects come back over a month after first reading a post.

**How to do it**

1. Open the lookback window setting in the attribution report before reading any numbers.
2. Set it to 90 days, the maximum Google Analytics allows, on every report you run.
3. Note the setting on the report itself so nobody compares a 30 day run against a 90 day run.
4. Check your typical sales cycle length against 90 days and record how much of it falls outside the window.
5. For cycles longer than 90 days, add a self-reported source field at signup to catch what the window misses.
6. Re-run the same report monthly at the same window so the series is comparable.

**Tools:** Google Analytics

**Pitfall:** A short lookback window silently reassigns long-consideration conversions to the homepage, which then looks like your best converting page while the posts that actually did the work look dead.

**Apply at Pabau:** Aesthetic practice software has a long evaluation cycle, so David should assume a large share of Pabau's demo bookings begin outside any 90 day window and never treat the attribution table as the full picture.

**Apply anywhere:** Always run attribution at the maximum lookback window your analytics allows, and assume conversions from long buying cycles fall outside it entirely.

### 6. Measure AI search in three linked buckets  `20.8`
*core · best practices · source 20*

The recommended GEO/AI-search measurement framework splits into three buckets that must all be tracked together: (1) performance measurement — traditional referral traffic and on-site outcomes; (2) brand/channel visibility measurement — citation rate and citation accuracy across AI answer engines; and (3) input metrics — the underlying levers you can act on, including bot activity, rankings for synthetic/fan-out queries, passage relevance scores, and entity salience. The explicit warning is that measuring only one bucket (most commonly just 'visibility') misses the bigger picture, and that this measurement work spans multiple disciplines/teams, not something an SEO team alone should own.

> "you need to stratify into three different buckets"

**How to do it**

1. Set up a performance-measurement layer tracking referral traffic from AI/search surfaces and what happens after it lands on your site (conversions, engagement).
2. Set up a brand/channel visibility layer tracking citation rate (how often you're cited for relevant prompts) and citation accuracy (whether the citation correctly represents you).
3. Set up an input-metrics layer tracking the underlying, actionable levers: bot crawl activity, rankings for synthetic/fan-out queries, passage relevance scores against target queries, and entity salience.
4. Use a measurement/monitoring tool (e.g., Profound) to cover as much of the citation-rate/accuracy and bot-activity tracking as it supports, supplementing with custom internal tooling for anything it doesn't cover.
5. Report all three buckets together in the same dashboard/review cadence rather than reporting visibility alone, explicitly connecting input-metric movement to visibility movement to performance movement.
6. Assign ownership across the relevant disciplines (SEO, content, PR, engineering/data) rather than routing all AI-search measurement through the SEO team by default. (inferred structural recommendation)

**Tools:** Profound

**Pitfall:** Measuring only visibility/citation rate and treating that as the whole picture — 'if you just measure one of those buckets, you're missing out on the bigger picture,' since input metrics and downstream performance need to be tracked and connected too.

### 7. Measure citation count per topic, not just whether you are mentioned  `82.4`
*core · concrete actions · source 82*

Grow and Convert go past the usual mentioned-or-not metric and count how often a specific URL is cited across a topic's whole prompt basket. For the Level AI article on call center real time reporting, across six tracked prompts, Google AI Overviews, Perplexity and ChatGPT cited that one article 15 times combined, almost twice as often as any other article on the topic. That gives a comparative number: your citation count against the next best source, on a fixed basket. It is a better health metric than brand mentions because it tells you whether you are the source the models build the answer from, which is what carries your value propositions into the response. On the call center quality assurance topic they concede they are not the top-cited article but are referenced consistently across prompts, which is the weaker but still acceptable state.

> "cite our article a combined 15 times, almost twice as often as any other article"

**Evidence:** Level AI's real time reporting article cited 15 times across six prompts by AIO, Perplexity and ChatGPT combined, roughly double the next article.

**How to do it**

1. Fix a basket of five or six prompt phrasings for one bottom-funnel topic.
2. Run the basket on ChatGPT, Perplexity and Google AI Overviews and record every cited URL, not just your own.
3. Sum citations per URL across the whole basket to get a topic-level citation count.
4. Rank the URLs and record your gap to the top-cited source as a multiple.
5. Track two numbers per topic each month: your citation count and your ratio to the leader.
6. Where you are cited but not leading, compare your page against the leader for depth on differentiators, use cases and pricing.
7. Where a competitor's page leads, add it to your citation outreach list as a page you could be included in.

**Tools:** Traqer, ChatGPT, Perplexity

**Pitfall:** Citation counts move with prompt phrasing, so a basket that changes between months produces a trend that is really noise. Freeze the basket and note the date of any addition.

**Apply at Pabau:** Pabau should record a citation count and a leader ratio per topic in its AI-visibility tracking, covering topics like clinic booking software and medspa QA. It shows whether Pabau's own pages are the source shaping the answer or just a name inside it.

**Apply anywhere:** For each topic, count how often your URL is cited across a fixed prompt basket and how that compares to the top-cited source. Track the ratio monthly rather than a binary mention flag.

### 8. Measure conversion rate by keyword type across your own archive  `118.4`
*core · concrete actions · source 118*

Grow and Convert did not argue the funnel case from theory; they audited their client Geekbot's archive. They took 64 published articles, tagged 22 as bottom-of-funnel and 42 as top-of-funnel, and measured pageviews and conversions per cohort over two years. Top-of-funnel produced 204,303 of the 232,493 organic pageviews, roughly ten times the bottom-of-funnel total of 28,190. But bottom-of-funnel produced 1,348 leads at a 4.78% conversion rate against top-of-funnel's 397 conversions at 0.19%, a 25x difference in rate and more than three times the absolute leads from a tenth of the traffic. The audit is repeatable on any archive with more than about fifty posts, and it settles the traffic-versus-conversion argument on your own data instead of someone else's case study.

> "we measured conversion rates by keyword type"

**Evidence:** Geekbot, 64 articles over two years: 42 top-of-funnel posts drove 204,303 pageviews, 397 conversions and 0.19%; 22 bottom-of-funnel posts drove 28,190 pageviews, 1,348 leads and 4.78%.

**How to do it**

1. List every published article with its target keyword and publish date, excluding anything under six months old.
2. Tag each row bottom-of-funnel or top-of-funnel using the category, comparison and JTBD definitions, and keep the tagging rule written down.
3. Pull organic-only pageviews per URL for a fixed window of at least a year, so seasonality cancels out.
4. Pull conversions per URL for the same window, using one clearly defined conversion such as demo request or contact form fill.
5. Sum pageviews and conversions per cohort and calculate conversion rate as conversions divided by pageviews for each.
6. Report both the rate gap and the absolute lead gap, since the rate alone will be argued away as small numbers.
7. Re-run the audit annually and check whether the gap holds as the archive grows.
8. Reallocate the next quarter's production budget in proportion to the lead counts, not the pageview counts.

**Tools:** Google Analytics, Google Search Console

**Pitfall:** Measuring last-click conversions only on pages that carry a form makes top-of-funnel look worse than it is, and measuring assisted conversions makes it look better. Pick one attribution rule, write it down, and use the same one for both cohorts.

**Apply at Pabau:** David should run this audit on pabau.com's blog and template archive, tagging each URL as category, alternatives, JTBD or general, so the next production quarter is sized by demo requests per cohort rather than by sessions.

**Apply anywhere:** Audit your own archive by tagging each post's keyword type, then compare pageviews and conversions per cohort over a year so budget follows leads rather than sessions.

### 9. Measure expected rank across users, not rank in one query  `76.10`
*core · concrete actions · source 76*

The paper's measurement argument is that personalization kills the idea of a universal brand ranking in LLM search. As models incorporate search history, stated preferences and behavioral signals, recommendations diverge across individuals: a brand that ranks first for one user may not appear at all for another. The authors' fix is to stop tracking absolute rank and estimate expected rank across the distribution of users, which they write formally as E[E[rank | user]], the average of personalized expected rankings across the user population. They concede this adds statistical complexity but argue it reflects true visibility in a personalized environment. They are also candid about why share of voice, the frequency and prominence with which a brand appears in LLM responses relative to competitors, remains imprecise: outputs are non-deterministic, responses vary across models, and there is no standardized methodology for sampling prompts, weighting results, or accounting for model updates that shift recommendations overnight.

> "the relevant metric becomes the average of the personalized expected rankings"

**Evidence:** The paper states the concept of a universal brand ranking within LLM search is effectively obsolete, and proposes E[E[rank | user]] as the replacement metric.

**How to do it**

1. Define a fixed basket of prompts per topic rather than one prompt per keyword.
2. Run each prompt repeatedly, since outputs are non-deterministic and one run is a single sample.
3. Run the basket across several models, since responses vary by platform.
4. Vary the simulated user context where the tool allows it, to sample the personalization distribution rather than one persona.
5. Record presence and prominence per run, then average into a share-of-voice figure with its variance stated.
6. Write down and freeze your sampling methodology, because no standard exists and comparability over time depends on yours staying fixed.
7. Re-baseline explicitly after any known model update rather than reading the shift as a performance change.

**Pitfall:** Reporting an AI rank from a single query. The paper's point is that this number is one draw from a distribution that also varies by user, so it moves for reasons unrelated to anything you did.

**Apply at Pabau:** If Pabau tracks AI visibility, define a frozen prompt basket for practice-management and aesthetics queries, run it repeatedly across ChatGPT, Gemini and Perplexity, and report an averaged share of voice with its variance.

**Apply anywhere:** Define a frozen prompt basket per topic, run it repeatedly across several engines, and report an averaged share of voice with its variance rather than a single-query rank.

### 10. Measure organic conversions site-wide, not article by article  `86.13`
*core · concrete actions · source 86*

Grow & Convert describe a measurement shift they made themselves. They used to focus heavily on tracking which specific articles drove conversions. That still has value, but it is no longer the whole picture, because AI visibility often sends users to the homepage or a product page rather than to the blog post that actually influenced the recommendation. Someone sees the brand named in ChatGPT, opens a tab, searches the company name, and lands on the homepage, so the conversion books as branded organic or direct. Their answer is to widen the unit of measurement: track organic traffic and conversions to homepage and product pages alongside blog pages, and judge the program on overall trajectory. If rankings are growing, AI visibility is growing and total organic conversions are growing, the strategy is working even when per-page attribution is messy.

> "tracking organic traffic and conversions to homepages and product pages"

**Evidence:** Grow & Convert changed their own reporting after finding AI visibility drives users to homepages and product pages rather than to the blog content that influenced the recommendation.

**How to do it**

1. Add homepage and product pages to the organic conversion report, not just blog URLs.
2. Track branded organic and direct conversion volume as a trend line beside non-branded organic.
3. Track AI visibility, meaning presence in your prompt set, as its own weekly series.
4. Set up referral reporting that identifies traffic from ChatGPT, Perplexity and other LLM platforms as a named group.
5. Review all four series together monthly and judge the program on whether the trajectories move together.
6. Stop asking which single article caused a given conversion; use it as directional evidence only.

**Tools:** Google Analytics

**Pitfall:** Per-article attribution now systematically undercounts AI-influenced conversions, so the pages doing the most work to earn recommendations look like the ones worth cutting.

**Apply at Pabau:** Pabau's content reporting should include homepage and pricing or product-page organic conversions in the same view as blog conversions, plus a named LLM referral segment, so blog posts that trigger a ChatGPT recommendation are not judged solely on their own page conversions.

**Apply anywhere:** Put homepage and product-page organic conversions in the same view as blog conversions, plus a named LLM referral segment, so posts that trigger an AI recommendation are not judged solely on their own page conversions.

### 11. Mine GSC for near-ranking keywords and push them with fast updates  `23.5`
*core · concrete actions · source 23*

Once a site starts ranking, Edward shifts keyword research toward mining Google Search Console for keywords the site already ranks for and pushing them further with a fast, targeted optimization pass (what he elsewhere calls a 'one-hour SEO update') applied to both existing and new pages, rather than searching for entirely new keywords. Internal linking's purpose also shifts: because the site now has a meaningful number of ranking pages, you deliberately link from those established, authority-carrying pages toward pages targeting more competitive keywords, actively directing the site's larger pool of authority toward its next tier of ranking opportunities.

> "targeting relevant keywords that you are already ranking for"

**How to do it**

1. Open Google Search Console's Performance report and filter for queries where your page ranks roughly positions 8-20 with meaningful impressions (inferred threshold).
2. Identify the specific page currently ranking for each of those near-miss queries.
3. Apply a fast, targeted on-page update to that page rather than a full rewrite.
4. Separately, list your current ranking pages by authority/traffic level and identify which more competitive keyword/page on the site would benefit from additional internal link equity.
5. Add contextual internal links from your established ranking pages to those higher-competition target pages.
6. Re-check GSC rankings for both the updated near-miss pages and the internally-linked competitive pages after several weeks to confirm improvement (inferred verification step).

**Tools:** Google Search Console

### 12. New or updated pages get roughly two weeks of position testing  `21.5`
*core · content insights · source 21*

Looking at his own GSC data for a page published on Monday, July 6th, David shows position swinging from 8, to 37, to 16, to 25, to 14 as Google tested it against different keywords and impression sources, before the volatility abruptly stopped around July 22-23 - roughly two weeks of active testing. During that window the page's blended CTR figure was meaningless on its own (5.6%) because it only makes sense once isolated to one specific query, where it can show 0% for the whole window despite position swings. He frames this explicitly as Google 'giving it a solid two weeks of testing' rather than instability or a problem with the page.

> "Google gave it a solid two weeks of testing"

**Evidence:** David's own GSC chart for a page published July 6th: position oscillated between roughly 8 and 37 for about two weeks before settling around July 22-23, with 0% click-through rate the entire time for the specific query 'EMD SEO' regardless of position.

**Apply:** When a newly published or recently updated page shows wild position swings in GSC during its first two to three weeks, treat it as expected algorithmic testing rather than an urgent problem, and hold off on making reactive changes until that settling window has passed.

### 13. Optimize at the search term level, not the keyword level  `158.10`
*core · concrete actions · source 158*

Grow and Convert's last finding was that the previous agency never doubled down on what worked, because it read performance at keyword level. Under the keyword 'magento development', two search terms behaved very differently. 'Magento web' took a few clicks and produced no quality conversions. 'Magento experts' produced one conversion from a single click and six impressions, because buying intent is high. The agency saw the parent keyword performing well and left it alone, so over $1,000 went to 'magento web' and only $44 to 'magento experts'. Their fix is to read the Search Terms report, find the terms that actually convert, and promote each into its own keyword so ad copy and landing page can be built specifically for it. Keyword-level reporting hides this entirely.

> "you need to dig into which search terms are doing well"

**Evidence:** Client spent over $1,000 on 'magento web' with no quality conversions and $44 on 'magento experts', which converted from one click.

**How to do it**

1. Open the Search Terms report in Google Ads for the last 90 days, not the Keywords report.
2. Add cost, clicks, impressions and conversions as columns and sort by cost descending.
3. Flag any term with meaningful spend and zero qualified conversions, and add it as a negative keyword.
4. Flag any term with a conversion, even on one or two clicks, however small the impression count.
5. Promote each converting term into its own keyword on exact match.
6. Move that keyword into an ad group whose copy uses the term verbatim.
7. Build or pick a landing page that answers that term specifically.
8. Shift budget from the flagged wasteful terms to the promoted ones and repeat the report monthly.

**Tools:** Google Ads

**Pitfall:** Reading the Keywords report instead of the Search Terms report makes a parent keyword look profitable while most of its spend goes to one bad variant inside it.

**Apply at Pabau:** Pabau's paid reporting should be built on the Search Terms report. Terms like 'best software for medspas' that convert once should be promoted to exact-match keywords with their own ad and landing page, and treatment-related terms negatived out.

**Apply anywhere:** Optimize from the Search Terms report, not the Keywords report. Negative out the expensive non-converting terms, promote any converting term into its own exact-match keyword, and give it matching copy and a matching page.

### 14. Pick one revenue KPI from three buckets and drop vanity metrics  `150.2`
*core · best practices · source 150*

Grow and Convert list the metrics content marketers reach for when they cannot show revenue: overall website traffic, blog pageviews, newsletter signups, webinar signups, organic traffic, brand awareness, social engagement, bounce rate and click-through rate. Their blunt explanation is that these are easier to move than leads or revenue. Some of them tell you direction, but none can be attributed to sales, so any ROI claim built on them is a guess. They say the business-value metric sits in one of three buckets for almost every company: qualified leads where there is a sales team, free trial signups or booked demos in SaaS, and purchases in ecommerce and direct to consumer. Pick one, track it, report it. Everything else is supporting detail.

> "in one of these 3 buckets"

**Evidence:** Grow and Convert's list of vanity metrics is drawn from what they saw across 30-plus client engagements.

**How to do it**

1. Write down which of the three buckets you are in: qualified leads, trial signups or booked demos, or purchases.
2. Choose exactly one metric inside that bucket as the reported KPI for content.
3. Move traffic, pageviews, bounce rate and social engagement into an appendix, not the headline.
4. Confirm the chosen KPI is something sales or finance already counts, so nobody disputes the definition.
5. Instrument that KPI as a conversion in analytics before publishing anything new.
6. Report the KPI monthly by landing page, so individual articles can be judged.
7. Refuse to substitute a proxy metric in months where the KPI number is small; report the small number.

**Tools:** Google Analytics

**Pitfall:** Newsletter and webinar signups feel like leads but are not attributable to revenue, so a program can look healthy for a year and still have produced no pipeline. The signal is a report where the headline metric is not one sales would recognize.

**Apply at Pabau:** Pabau's blog KPI should be booked demos, since that is the SaaS bucket, and every /templates/ and /blog/ report should lead with demos attributed to the page rather than sessions.

**Apply anywhere:** Decide which of three buckets your business is in, qualified leads, trial signups or demos, or purchases, then report exactly one metric from it for content and demote traffic metrics to an appendix.

### 15. Plot monthly content leads against a break-even line  `101.7`
*core · concrete actions · source 101*

Grow and Convert's accountability device is a single graph made for every client. They plot monthly leads from their articles, using two series for two signup metrics at different funnel depths, against horizontal lines that mark how many leads the client needs each month to break even on the retainer. Because the break-even threshold sits on the same chart as the actual result, both sides can see when the engagement crosses into positive ROI rather than arguing about attribution in the abstract. They describe one such live graph from a B2B SaaS client of over two years. They call this the number one differentiator of their agency, and say it is the thing they wanted as buyers and could never find.

> "the number of leads this client needs per month to break even"

**Evidence:** A live Grow and Convert graph tracks over two years of a B2B SaaS client's content leads against two break-even lines.

**How to do it**

1. Take the monthly content spend, including agency fees and internal time.
2. Divide it by the average value of one lead at each funnel stage to get the break-even lead count.
3. Draw that count as a horizontal line on a chart.
4. Plot actual monthly leads attributed to content as a series on the same chart.
5. Add a second, deeper-funnel conversion metric as a separate series.
6. Review the chart monthly with whoever produces the content and act when the line is not crossed within the agreed ramp.

**Pitfall:** Without the break-even line on the chart, rising lead counts look like success even while the program loses money every month.

**Apply at Pabau:** David should build one chart for Pabau content: monthly demo requests sourced from articles against the number needed to cover content spend, so a stream that never breaks even gets cut instead of extended.

**Apply anywhere:** Chart monthly content-sourced leads against the number of leads needed to break even on content spend. Putting both on one graph turns the ROI conversation into a visible crossing point rather than an argument.

### 16. Plot monthly content leads against a horizontal breakeven line  `178.9`
*core · concrete actions · source 178*

Grow and Convert build one ROI graph per client and show it live, including a B2B SaaS client running over two years. The construction is simple and specific. Horizontal lines mark the number of leads per month the client needs to break even on their monthly spend with the agency. Each month they plot the actual number of leads attributed to their articles. Reporting is then done in relation to that breakeven line rather than in absolute numbers, so the client can see the month positive ROI begins. They say this is the type of reporting they looked for as buyers and never found, and they call it the number one differentiator of their agency. The point of the horizontal line is that it converts an ambiguous growth chart into a pass or fail against a number agreed at the start.

> "The horizontal lines represent the number of leads this client needs"

**Evidence:** Grow and Convert maintain this graph for every client and show a live version from a B2B SaaS client of more than two years.

**How to do it**

1. Divide the monthly content spend by the value of one lead to get the breakeven lead count.
2. Draw that count as a horizontal line on a chart before the first article publishes.
3. Attribute leads to specific articles, and plot only leads that came from content.
4. Plot the actual monthly figure against the line every month, including the months it is far below.
5. Report the gap to breakeven, not the raw lead number.
6. State the pace: at the current slope, the line is crossed in month N.
7. Keep the same chart running for the life of the engagement so the crossing point is visible in context.

**Tools:** Google Analytics, Google Sheets

**Pitfall:** Reporting lead counts with no breakeven line. Growth looks good or bad depending on mood, and nobody can say whether the program is working, which is when budgets get cut just before the crossover.

**Apply at Pabau:** David should set a monthly booked-demo breakeven number for Pabau's content spend and chart actual content-sourced demos against it, so the pre-breakeven months are budgeted rather than defended.

**Apply anywhere:** Compute the monthly leads needed to break even on content spend, draw it as a horizontal line, and plot actual content-sourced leads against it every month from the start.

### 17. Plot monthly conversions against a flat breakeven line  `150.9`
*core · concrete actions · source 150*

The final step of Grow and Convert's process is a chart, not a table. In the ROI sheet they build for clients there is a section recording, per month, first click conversions, last click conversions, and the breakeven goal. Alongside it sits a line chart with two lines: actual conversions and the flat breakeven goal. They are explicit that their example graph is idealized and most content graphs will not look like that, citing Circuit for Teams as a real client case where it did. The reason for the chart is that five things become readable without commentary: where you are against breakeven, progress over time, the pace of approach, the month you cross the line, and total spend to date. Their experience is that once a business can see it is making money from the channel it is happy, and the real work is holding buy-in during the months before the crossing.

> "The pace at which you're approaching your break even goal."

**Evidence:** Grow and Convert publish a chart of trial signups for Circuit for Teams generated from their blog posts as a real example of this growth shape.

**How to do it**

1. Add a table to the ROI sheet with one row per month: month, first click conversions, last click conversions, breakeven goal.
2. Pull the first and last click figures from the attribution model comparison report each month.
3. Repeat the breakeven goal down every row so it plots as a flat line.
4. Insert a line chart with month on the x axis and both conversion series plus the goal line on the y axis.
5. Add a cumulative spend column so total investment to date is readable off the same sheet.
6. Draw the projected crossing point from the current slope and state it as a month, not a quarter.
7. Send the same chart every month without redesigning it, so the trend is the message.
8. When the line crosses the goal, keep publishing the chart, since the gap above the line is the ROI.

**Tools:** Google Analytics, Google Sheets

**Pitfall:** Redesigning the report each month hides the trend and reopens the argument. The hardest period is before the crossing, and a chart that changes shape gives stakeholders something to question other than the trajectory.

**Apply at Pabau:** Pabau should keep one unchanging chart of monthly booked demos attributed to content against a flat breakeven demo line, with cumulative content spend on the same sheet, and send it in the same format every month.

**Apply anywhere:** Record first and last click conversions per month next to a repeated breakeven figure, then chart both against the flat goal line. Send the same chart, unchanged, every month so the trajectory rather than the design is what gets discussed.

### 18. Prove the ranking-to-AI-visibility link using a topic you do not yet rank for  `81.6`
*core · concrete actions · source 81*

Grow and Convert build their case with a negative control rather than a correlation chart. Constitution Lending ranks number one for 'best LLC mortgage lenders' and shows up as a top recommendation in ChatGPT, Perplexity and Google AI Overviews for that topic. The company recently started a cash-for-houses line where several articles are not ranking yet, and for 'sell my house fast Connecticut' the brand rarely appears in AI answers at all. Same site, same brand, same tooling, different ranking status. They say the pattern held across different keywords and across their other clients. That test is worth running on your own site before spending on any GEO tactic, because it tells you whether your AI visibility problem is actually a rankings problem.

> "we see very little AI visibility for keywords we aren't yet ranking for"

**Evidence:** Constitution Lending appears top-three across three AI surfaces for 'LLC mortgage lenders' where it ranks #1, and rarely appears for 'sell my house fast Connecticut' where its new articles have not ranked yet.

**How to do it**

1. Pick one topic where you hold a top-three Google position and one topic where you rank outside the top 20.
2. Write eight to twelve natural-sounding prompts per topic, phrased the way a buyer would ask rather than as keywords.
3. Run both prompt sets through ChatGPT, Perplexity and Google AI Overviews on the same day.
4. Record for each prompt whether the brand is mentioned, cited as a source, or absent.
5. Compare the mention rate between the ranked topic and the unranked topic.
6. If the ranked topic scores far higher, treat rankings as the primary lever and stop buying on-site GEO tweaks.
7. Re-run the unranked topic's prompt set once those pages reach page one, and log the change.
8. Repeat the paired test quarterly so the relationship is measured, not assumed.

**Tools:** Traqer, ChatGPT, Perplexity, Ahrefs

**Pitfall:** Running a single prompt per topic. Nobody knows the exact phrasing users enter, especially inside long multi-turn ChatGPT conversations, so one prompt measures noise rather than visibility.

**Apply at Pabau:** Pabau should run this paired test using a topic where it already ranks well against a newer topic area, and use the gap to settle internally whether budget goes to rankings or to GEO tactics.

**Apply anywhere:** Compare AI mention rates for one topic where you rank top three against one where you rank outside the top 20, using the same prompt-set method on both. If the ranked topic wins clearly, your AI visibility work is really ranking work.

### 19. Prune pages stuck in GSC's not-indexed reports to regain traffic  `26.5`
*core · concrete actions · source 26*

Dooley treats Google Search Console's index-coverage statuses as the primary diagnostic for whether a site has scaled beyond its authority: 'Discovered – currently not indexed' means Google found the URL but hasn't even crawled it yet, regardless of content quality, signaling too many pages relative to crawl budget/authority. 'Crawled – currently not indexed' is a step worse — Google crawled it and actively chose not to index it, meaning the content itself (or excess thin/duplicate volume) isn't good enough. When his team acquires aged sites, the first action is always to clear out everything sitting in 'crawled, currently not indexed,' and he reports cases where deleting 50% of a site's pages led to a 5x increase in traffic because crawl budget and authority concentrated on the remaining stronger pages.

> "deleted 50% of pages yet the traffic has 5x'd"

**How to do it**

1. Open the property in Google Search Console.
2. Go to Indexing > Pages.
3. In the 'Why pages aren't indexed' table, click 'Discovered – currently not indexed' and export the full URL list.
4. Click 'Crawled – currently not indexed' and export that URL list separately.
5. Treat a large or growing 'Discovered – currently not indexed' count as a signal to stop publishing net-new thin pages until the backlog clears.
6. Manually review each 'Crawled – currently not indexed' URL for word count, uniqueness, and topical overlap with other pages on the site.
7. Delete or 301-redirect thin, duplicate, or low-value pages from that list into the strongest related page rather than leaving them live.
8. Resubmit the XML sitemap in GSC (Indexing > Sitemaps) after pruning.
9. Recheck the Pages report weekly to confirm the 'crawled, not indexed' count is falling.
10. Watch total clicks in the GSC Performance report over the following 1-3 months to confirm the prune helped rather than hurt traffic.

**Tools:** Google Search Console

**Pitfall:** Don't assume more published pages always means more traffic — pages published beyond what a site's authority/crawl budget supports get stuck in 'discovered, not indexed' limbo where Google never even evaluates their quality, and the fix is deletion/consolidation rather than adding more content on top.

### 20. Rank blog posts by sales attributed, not by traffic, before planning  `138.1`
*core · concrete actions · source 138*

Nat Eliason opened the Cup & Leaf project by joining conversion data to blog posts instead of reading the traffic report. The first thing he found was that the highest-traffic posts were not the ones driving sales. Their 'green tea side effects' post pulled over 60,000 visitors in three months and produced $0 in sales. Their 'best oolong tea' post had far less traffic and produced far more revenue. Everything that followed came out of that one sort. He treats the traffic leaderboard as actively misleading for a business with a product, because it hides both the zero-revenue giants and the small posts already paying. The audit is the prerequisite: you cannot pick better topics until you know which existing ones convert.

> "the posts getting the most traffic were not necessarily the ones driving the most sales"

**Evidence:** Cup & Leaf: 'green tea side effects' brought over 60,000 visitors in three months and $0 in sales, while the lower-traffic 'best oolong tea' post drove far higher conversions.

**How to do it**

1. Set up revenue or lead attribution per landing page in your analytics, so each blog URL carries a sales number, not just sessions.
2. Export every blog URL with three columns: organic sessions, clicks through to product or pricing pages, and attributed revenue over the last 90 days.
3. Sort by attributed revenue descending, not by sessions, and read the top 10 first.
4. Flag every post above roughly 5,000 sessions in the window that shows zero attributed revenue; these are your dead giants.
5. Flag every post in the bottom half by traffic that still shows revenue; these are your winning patterns.
6. Write down what the winning posts have in common as a keyword shape, for example 'best [product type]'.
7. Use that shape as the seed for the next quarter's topic list, and stop commissioning anything resembling the dead giants.
8. Re-run the same export every quarter so the list stays current.

**Tools:** Google Analytics, Shopify

**Pitfall:** Attribution has to exist before the audit. If your store has no per-landing-page revenue view, the sort defaults back to traffic and you keep commissioning the topics that already earn nothing.

**Apply at Pabau:** Pabau should join demo requests to landing page in the same way and re-sort the blog inventory by demos, not sessions. High-traffic definitional posts about aesthetics procedures may be Pabau's 'green tea side effects', and the /templates/ pages may be the oolong post.

**Apply anywhere:** Join revenue or lead data to every blog URL and sort by that, not by sessions. The posts you fund next should copy the shape of whatever already converts, and the high-traffic zero-revenue posts should stop setting the agenda.

### 21. Rank your blog posts by signups per post to find the intent pattern  `104.8`
*core · concrete actions · source 104*

Grow and Convert's evidence comes from a per-post analytics report for a client, where each row is a blog post and the columns carry sessions, conversion rate and new software trial signups. Three of the ten posts produced 30 to 50 trial signups each; the other seven produced between 0 and 8. All three winners were the posts with much higher buying intent. They repeated the analysis across 95 or more articles and thousands of conversions for several clients and found the same pattern for every keyword type, including jobs-to-be-done keywords where the buckets split cleanly: 'best tools for building a deck' converts, 'how to build a deck' does not. The point is that you can run this report on your own site and stop arguing about intent from first principles.

> "generated far more conversions (30–50 trial signups each)"

**Evidence:** One Grow and Convert client: three high-intent posts drove 30 to 50 signups each while the other seven drove 0 to 8. Confirmed across 95+ articles and thousands of conversions for multiple clients.

**How to do it**

1. Build a report in your analytics tool with one row per blog URL, over at least the last 12 months.
2. Add columns for sessions, conversions to your primary goal, and conversion rate.
3. Attach the target keyword to each row from your keyword sheet.
4. Tag each row high, medium or low buying intent based on that keyword, not on the article.
5. Sort by total conversions and read the top five and the bottom five.
6. Check whether the split follows buying intent rather than sessions; in the Grow and Convert client it did.
7. Reallocate the next quarter's calendar toward the intent tier that converted, and stop commissioning the tier that did not.
8. Repeat the report each quarter so the ratio is measured, not assumed.

**Tools:** Google Analytics

**Pitfall:** Reading the report by conversion rate alone on posts with tiny traffic. A single conversion from four sessions shows a 25 percent rate and proves nothing, so rank by total conversions and only then look at the rate.

**Apply at Pabau:** David should build a per-article demo-request report for pabau.com, tag every row with its target keyword's intent, and use the split to decide how much of the calendar goes to template pages versus clinical how-to posts.

**Apply anywhere:** Build a per-post report showing conversions, not just traffic, tag each post by the buying intent of its target keyword, and let the resulting split set your next quarter's content mix.
