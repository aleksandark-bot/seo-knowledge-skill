# Conversion & Monetization — core (part 2 of 5)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Do not A/B test a post until its keyword has buying intent  `144.7`
*core · best practices · source 144*

Grow and Convert argue that general purpose CRO centers on A/B testing, but that content CRO has factors which precede testing and matter far more. They back it with a specific number from their Geekbot analysis of 60-plus posts, where bottom-of-funnel posts converted 2400 percent better than top-of-funnel posts, and they say plainly that no A/B or split test is going to get you a 2400 percent lift in average conversion rate. Their conclusion is that keyword buying intent is the number one factor by far in content conversion optimization, and that if you do nothing else, ranking for keywords where people are actively looking to buy what you sell will increase conversions. Testing is the last lever, not the first.

> "No AB or split testing is going to get you a 2400% lift"

**Evidence:** Geekbot analysis of 60-plus posts: bottom-of-funnel posts converted 2400 percent better than top-of-funnel posts, a gap Grow and Convert say no split test can match.

**How to do it**

1. Before approving any CRO test on a blog post, pull the queries actually driving traffic to that URL from Search Console.
2. Classify those queries as buying intent or not, using whether the searcher is actively looking to buy what you sell rather than merely interested in the topic.
3. If the driving queries are not buying intent, cancel the test and put the effort into a new post on a buying-intent keyword instead.
4. If the intent is right but the post ranks below the top half of page one, fix ranking before testing, since low traffic makes any test underpowered anyway.
5. If intent and ranking both hold, check the copy sells the product before testing button and layout variants.
6. Only then run the test, and size it against the conversion rate the post already achieves so you know what lift is detectable.
7. Report test results next to the intent-bucket conversion gap, so stakeholders see the relative size of the two levers.

**Tools:** Google Search Console

**Pitfall:** Running tests on low-traffic posts. Content pages rarely have the volume to reach significance, so teams read noise as a winner and roll out changes that do nothing.

**Apply at Pabau:** If David is offered CRO testing on Pabau blog pages, he should first check which pages already draw buying-intent queries such as software comparisons and alternatives. Testing on a definitional aesthetics article is effort spent on a page that cannot convert regardless of layout.

**Apply anywhere:** Before agreeing to CRO testing on blog pages, check which pages already draw buying-intent queries such as comparisons and alternatives. Testing on a definitional article is effort spent on a page that cannot convert regardless of layout.

### 2. Do not assume product landing pages outconvert blog posts organically  `146.1`
*core · content insights · source 146*

Grow and Convert compared organic conversion rates for one SaaS client's three industry product landing pages against their own blog posts targeting closely comparable bottom-of-funnel keywords. The landing pages averaged around 0.4%. The blog posts converted at 1.13%, and the single post targeting essentially the same keyword as the 'QuickBooks Integration' landing page converted at 1.27% while also outranking it and drawing more organic traffic. They call it a small, imperfect data set, but it is enough to kill the default assumption. Their explanation is that landing pages usually win only because most companies never write bottom-of-funnel blog posts that sell the product properly. A post that does sell converts as well or better, and it has more room to explain positioning and differentiation than a thin landing page.

> "hovers in the 0.4% range for the product landing pages"

**Evidence:** One SaaS client, three product landing pages averaging ~0.4% organic conversion vs Grow and Convert blog posts at 1.13%, with one matched-keyword post at 1.27%.

**Pitfall:** Reading the landing-page-wins assumption straight from paid-search benchmarks. If you compare an ad-fed landing page at 10% to an organic blog post, you are comparing traffic sources, not page formats.

**Apply at Pabau:** David should measure organic conversion rate per URL for Pabau's product and feature pages against comparable blog articles before assuming a new bottom-of-funnel term needs a product page. If a Pabau blog article on an equivalent term already converts higher, write the article.

**Apply anywhere:** Measure organic conversion rate per URL for your product pages against comparable blog articles before assuming a bottom-of-funnel term needs a product page. If the article already converts higher, write the article.

### 3. Doubling either conversion rate equals doubling blog traffic  `152.5`
*core · content insights · source 152*

Grow and Convert model customers acquired from content as three numbers multiplied together: monthly unique visitors to the blog, the percentage of those visitors who become leads, and the percentage of leads who become paying customers. Because it is a straight product, the output depends linearly and equally on all three. Improving either conversion rate by a factor of two is exactly equivalent to doubling traffic. Their worked example: 10,000 monthly uniques at a 1 percent overall conversion rate produces the same number of paying users as 5,000 monthly uniques at 2 percent. That matters because doubling traffic is usually far more expensive and slower than doubling a form's conversion rate, yet most content teams spend their effort on the traffic term alone.

> "improving the conversion rate at either step by a factor of two"

**Evidence:** 10,000 uniques at 1% equals 5,000 uniques at 2% in their model.

**How to do it**

1. Write the three-factor formula out explicitly: uniques times lead rate times lead-to-customer rate.
2. Measure each of the three terms separately for the last full quarter.
3. Estimate the cost of doubling each term: more articles and links versus CRO work on the existing pages.
4. Pick the cheapest term to double first, which on most blogs is the visitor-to-lead rate.
5. Run the CRO work on the highest-traffic converting posts before commissioning new articles.
6. Recompute CAC after the change to confirm the lever moved the number.
7. Only then spend on traffic growth for the remaining gap.

**Tools:** Google Analytics

**Pitfall:** Assuming traffic growth carries conversion rate with it. Grow and Convert warn conversion rates usually dip as traffic grows, because incremental traffic tends to be less qualified.

**Apply at Pabau:** Before commissioning more Pabau blog posts, David should test CTA placement and the demo form on the top converting posts. The same customer count can come from CRO at a fraction of the writing cost.

**Apply anywhere:** Before commissioning more posts, test CTAs and forms on your best-converting existing pages. The same customer count is usually cheaper to get from conversion rate than from traffic.

### 4. Drop broad match entirely and run phrase plus exact with negatives  `157.4`
*core · concrete actions · source 157*

Grow and Convert give a concrete example of why broad match fails. The keyword 'accounting software' on broad match can serve a query like 'bookkeeping companies that use quickbooks accounting software in Dallas, TX', which is useless if you sell accounting software. The same term on phrase match might show for 'what is the best affordable accounting software', which is better but still loose. Exact match returns only 'accounting software' or a very close variant such as 'accounting programs'. Their rule is that if you are using long-tail high-intent keywords, you should not be using broad match at all: run phrase and exact only. They also note broad match is what Google itself recommends inside the interface to lower costs, which is why so many agencies and brands turn it on. Phrase match requires a negative keyword list alongside it.

> "you shouldn't be using broad match at all"

**Evidence:** Grow and Convert's example: broad match on 'accounting software' serving 'bookkeeping companies that use quickbooks accounting software in Dallas, TX'.

**How to do it**

1. Export every keyword in the account with its match type.
2. Pause all broad match keywords rather than editing them.
3. Recreate the ones with genuine buying intent as phrase match and exact match versions.
4. Build a negative keyword list from the search terms report before phrase match runs, covering jobs, free, courses, definitions, and unrelated verticals.
5. Dismiss the Google Ads recommendation panel that suggests broad match with Smart Bidding, and check it has not re-enabled itself after each account change.
6. Review the search terms report weekly and add any off-intent query as a negative.
7. Compare cost per lead over the following month against the broad match baseline.

**Tools:** Google Ads

**Pitfall:** Applying Google's in-account recommendation to add broad match 'for more conversions at a similar or better ROI'. Accepting it silently re-widens the account and CPA climbs weeks later.

**Apply at Pabau:** Any Pabau paid search test should launch on phrase and exact only, with a negative list that excludes free, jobs, training and non-aesthetic verticals before the first click is bought.

**Apply anywhere:** Launch paid search on phrase and exact match only, with a negative keyword list built before the first click. Ignore the in-account recommendation to switch on broad match.

### 5. Enforce keyword to query to ad to landing page alignment in that order  `157.8`
*core · best practices · source 157*

Grow and Convert state the whole account structure principle as a chain: your high-intent keyword should match the query, the query should match the ad, and the ad should match the landing page. They call this three-tiered alignment and say it is what maximizes conversion, yet they rarely see it. The failure modes are separate at each link. A perfect keyword with an irrelevant ad produces very low click-through and almost no leads. A matching keyword and ad with a mismatched landing page produces the click but the visitor bounces: their example is appearing for 'marketing analytics software' and landing the visitor on a page about 'marketing operations software'. Both are wasted spend, but the second is worse because you paid for the click.

> "Your high-intent keyword should match the query"

**Evidence:** Grow and Convert cite the 'marketing analytics software' ad landing on a 'marketing operations software' page as the mismatch that causes bounce and lost leads.

**How to do it**

1. Build a spreadsheet with one row per ad group and columns for keyword, top actual search terms, ad headline, and landing page H1.
2. Pull the top three real search terms per ad group from the search terms report to fill the query column.
3. Flag any row where the ad headline does not contain the keyword or a near variant.
4. Flag any row where the landing page H1 uses different product language than the keyword.
5. Fix headline mismatches first, since they cost you click-through at no spend.
6. Fix landing page mismatches next, by pointing the ad group at a better existing page or building one.
7. Re-audit the sheet monthly, because new search terms drift the query column away from the keyword.

**Tools:** Google Ads

**Pitfall:** Fixing only the ad copy. A relevant ad pointed at a near-miss landing page raises click-through and therefore raises wasted spend, since bounce rate stays high.

**Apply at Pabau:** Every Pabau ad group needs its own destination. A keyword about online booking must not land on a general practice management page, which means some ad groups need a dedicated page built before the campaign launches.

**Apply anywhere:** Audit every ad group as a chain of keyword, real search term, ad headline and landing page H1. Fix headline mismatches first, then build dedicated destinations for the ad groups that have no matching page.

### 6. Expect 0.25-0.75% blog conversion on BOFU, 0.10% on TOFU  `150.12`
*core · content insights · source 150*

Grow and Convert publish the conversion-rate range they see across agency clients: most client blogs average between 0.25% and 0.75%, and that assumes high-quality content aimed at bottom-of-funnel purchase-intent keywords under their Pain Point SEO strategy. If instead you run a top-of-funnel strategy reaching people earlier in the journey with ultimate guides and infographics, they say conversion rates hover nearer 0.10%. Individual pages vary widely around those averages. The practical weight of the figures is in the ratio: a top-of-funnel program needs roughly three to seven times the traffic to produce the same number of leads, which usually means it cannot reach breakeven within any period the business will fund. The numbers are the argument for keyword selection, not just a benchmark.

> "average blog conversion rates in the range of 0.25%"

**Evidence:** Grow and Convert report most client blogs at 0.25-0.75% conversion with bottom-of-funnel content, versus around 0.10% for top-of-funnel strategies.

**How to do it**

1. Calculate your own blog conversion rate: conversions from blog landing pages divided by blog sessions, over six months.
2. Compare it against 0.25-0.75% for bottom-of-funnel programs and 0.10% for top-of-funnel ones.
3. If you sit near 0.10%, classify your published keywords by intent to confirm the cause is topic selection, not the page.
4. Rerun the breakeven traffic math at your actual rate rather than the benchmark.
5. Show stakeholders both plans: BOFU at 0.25% and TOFU at 0.10%, with the traffic each requires.
6. Shift the editorial calendar to purchase-intent keywords first and keep guides for later.
7. Recheck the blended rate quarterly as the intent mix of published pages changes.

**Tools:** Google Analytics

**Pitfall:** Planning at the 0.75% top of the range when your published mix is mostly guides will overstate expected leads by up to seven times, and the shortfall only becomes obvious a year in.

**Apply at Pabau:** Pabau should measure its own blog conversion rate and use it, not the benchmark, in planning. If it sits near 0.10%, the published mix is too top-of-funnel and the fix is more comparison, alternatives and pricing pages rather than more guides.

**Apply anywhere:** Benchmark your blog conversion rate against 0.25-0.75% for bottom-of-funnel content and 0.10% for top-of-funnel. If you are near the low end, the cause is usually topic selection, and a top-of-funnel plan needs several times the traffic to break even.

### 7. Expect 4.78% versus 0.19% conversion in the Geekbot 60-post analysis  `143.2`
*core · content insights · source 143*

Grow and Convert put a specific number on the bottom-funnel premium using their client Geekbot. Across an analysis of more than 60 posts, pages targeting high buying intent keywords converted at 4.78% while the higher-volume, lower-intent posts converted at 0.19%. They describe that as converting 2400% better, not a bit better. They add that in the case study the higher conversion rates more than made up for any difference in search volume or traffic between the two buckets, which is the argument that usually gets made against bottom-funnel work. This is a sharper figure than the 10x to 25x range Grow and Convert quote elsewhere in this base, and it comes from one named client with a stated post count, so it is usable as a benchmark rather than a range.

> "they converted 2400% better"

**Evidence:** Geekbot, 60+ posts analyzed: 4.78% conversion on bottom-of-funnel posts versus 0.19% on top-of-funnel posts.

**Tools:** Google Analytics 4

**Pitfall:** Quoting 2400% without the traffic context invites the objection that the bottom-funnel bucket is tiny. Have the absolute conversion counts for both buckets ready, not just the rates.

**Apply at Pabau:** When David needs to defend low-volume Pabau topics against high-volume ones, the Geekbot split is the cleanest single citation. Pair it with Pabau's own two-bucket conversion numbers from GA4 so the argument rests on internal data too.

**Apply anywhere:** When defending low-volume commercial topics internally, cite the Geekbot split: 4.78% conversion on bottom-funnel posts against 0.19% on top-funnel, across 60+ posts. Back it with your own two-bucket numbers.

### 8. Expect around 90% of blog conversions to come from framework posts  `90.12`
*core · content insights · source 90*

Grow and Convert publish the split from their own blog. Across the top ten converting posts in the period they measured, only three were what they consider top-of-funnel articles, and those three produced just 10% of the conversions. The other 90% came from posts built on the high-product-intent frameworks. They pair that with the per-post rates behind it: top-of-funnel posts converting between 0.03% and 0.19%, with many producing no conversions at all for months, against pain-point posts at 0.3%, 0.4% and in one case 4.3%. They describe both patterns as common rather than exceptional. The number to plan with is the share, not the rate: if your framework posts are not producing the large majority of conversions, either the frameworks are not being followed or the CTAs are not contextual. They also point to a wider analysis of 95 blog posts comparing conversion rates across the three keyword types.

> "90% of the conversions from these top 10 articles"

**Evidence:** Grow and Convert: three of ten top converting posts were top of funnel and made up 10% of conversions. Per-post rates were 0.03% to 0.19% top of funnel against 0.3%, 0.4% and 4.3% for pain-point posts.

**How to do it**

1. Pull your top ten converting blog posts for the last six to twelve months.
2. Label each as category, comparison, jobs-to-be-done, or top of funnel.
3. Calculate what share of total conversions the framework posts account for, and compare against Grow and Convert's 90%.
4. If the share is well below 90%, check whether the framework posts have contextual CTAs before blaming the topics.
5. Calculate a conversion rate per post and flag anything under 0.2%, which is Grow and Convert's top-of-funnel band.
6. List every post that has produced zero product conversions in the last several months.
7. Decide for each zero-conversion post whether to reposition it into a framework, merge it, or accept it as a traffic asset.
8. Set a target share for the next quarter and hold the calendar to it.

**Tools:** Google Analytics

**Pitfall:** Reading these as benchmarks for your own conversion rate rather than as a share. Rates vary hugely by product and price; the reliable pattern is the concentration of conversions in a small number of high-intent posts.

**Apply at Pabau:** David should produce this split for pabau.com once a quarter. If competitor comparison, category and clinic-task pages are not producing most of the demo requests, the blog is running on traffic topics regardless of what the calendar says.

**Apply anywhere:** Label your top ten converting posts by framework each quarter and check that high-intent posts produce the large majority of conversions; if they do not, the calendar has drifted back to traffic topics.

### 9. Expect comparison and alternative keywords to average 8.43% conversion  `121.4`
*core · content insights · source 121*

Grow and Convert put a specific figure on the top of their intent hierarchy: in their data, comparison and alternative keywords convert at the highest rate of any keyword type, averaging 8.43%. That sits well above the 4.78% they report for bottom-of-funnel content generally, so it separates the comparison bucket from the rest of the bottom funnel rather than lumping them together. Their explanation is that someone searching 'Salesforce alternatives' already knows what they want and is ready to switch if they find something better. The practical use of the number is prioritization: when the calendar has room for one page, the comparison or alternatives page beats the category page, and both beat a jobs-to-be-done post. They add that a brand too small to appear in these searches naturally can still target 'Competitor A vs Competitor B vs Your Brand' to enter the comparison.

> "comparison and alternative keywords convert at the highest rate"

**Evidence:** Grow and Convert's client data: comparison and alternative keywords averaged 8.43% conversion, the highest of any keyword type they track.

**Tools:** Google Analytics

**Pitfall:** Quoting 8.43% as a site-wide expectation. It is an average across one keyword type at one agency, and a comparison page that hides the honest verdict will not reach it.

**Apply at Pabau:** Pabau's competitor comparison and alternatives pages should be the first thing built and the first thing refreshed, and they justify a larger production budget per page than the how-to blog.

**Apply anywhere:** Treat comparison and alternatives keywords as your highest-converting type and build them first. One agency reports them averaging 8.43%, above the bottom-funnel average generally.

### 10. Expect content quality, not CTAs, to drive the conversion  `97.3`
*core · content insights · source 97*

Grow and Convert make an explicit claim about why blogs fail to produce leads: readers decide based on the quality of the content, not on the popup, ebook or CTA inviting them to learn more. Their illustration is a reader finishing a genuinely expert post and thinking they would buy the author's course or hire him without caring what it costs, purely because the post proved competence. The inverse is stated just as directly. If you sell SEO services and publish elementary SEO advice, there is no way a buyer does business with you, because you have demonstrated you are not the expert you claim to be. This reframes conversion work: before optimizing CTA placement, check that the post itself is evidence of expertise, because that is what is actually being evaluated.

> "they make a decision based on the quality of your content"

**Evidence:** Grow and Convert state readers do not decide because of a shiny popup, ebook or other CTA, but on content quality.

**How to do it**

1. For each money-driving post, ask whether it demonstrates you can do the job or only asserts that you can.
2. Add at least one artifact that proves competence: a real client situation, a real number, a screenshot of the work, or a walkthrough of a decision you made.
3. Stop A/B testing CTA copy on posts that fail that test, and fix the post first.
4. Match the depth of the post to the price of what you sell, since higher-priced offers need harder proof.
5. Track conversions per post rather than site-wide, so you can see which posts earn trust and which only earn traffic.
6. Retire or rewrite posts that get traffic but never convert, rather than adding more CTAs to them.

**Pitfall:** Adding more CTAs to a fluff post raises annoyance, not conversions. The signal is a post with strong traffic, decent time on page and near-zero demo requests no matter where you place the button.

**Apply at Pabau:** On Pabau template and blog pages, the demo CTA converts only if the surrounding content proves we understand clinic operations. David should prioritize adding real workflow detail over adding another CTA block.

**Apply anywhere:** Fix the proof of expertise inside the post before optimizing CTA placement, because readers judge whether to buy on content quality rather than on the offer box.

### 11. Expect most content conversions from organic bottom-funnel rankings, not promotion  `133.9`
*core · content insights · source 133*

Grow and Convert watched Circuit's conversion curve track the organic traffic curve almost exactly, both rising in September 2020, about three months after the subfolder move. They state the generalization directly: this correlation appears across many clients, and even though paid and other promotion tactics do yield conversions, the majority of content conversions come from ranking organically for bottom-of-funnel keywords. That is the argument for tolerating the flat months. Promotion buys conversions while it runs; rankings on high-intent terms produce them continuously afterwards. The 313% conversion increase, 59 to 244 trial signups over roughly six months to March 31 2021, sat alongside a 1484% organic traffic increase from 920 to 14,577 sessions, and the two moved together rather than independently.

> "the majority of content conversions comes from ranking organically"

**Evidence:** Circuit: conversions rose from 59 to 244 trial signups (313%) while organic traffic rose from 920 to 14,577 sessions (1484%) over roughly six months ending March 31 2021, with the conversion rise landing in the same month as the traffic rise.

**Tools:** Google Analytics

**Pitfall:** Concluding from early paid-promotion conversions that distribution is the growth engine and cutting the SEO track. The paid conversions stop with the budget; the ranked bottom-funnel pages do not.

**Apply at Pabau:** Pabau should judge blog and template pages on demo requests from organic bottom-funnel queries rather than on total content-sourced conversions, since paid and social promotion will inflate the latter without building anything durable.

**Apply anywhere:** Plot content conversions against organic sessions rather than total sessions. Promotion-driven conversions stop when the spend stops, while bottom-funnel rankings keep converting, and on most accounts the ranked pages produce the majority of the total.

### 12. Expect near-zero leads from an email list built off content readers  `147.5`
*core · content insights · source 147*

Grow and Convert report that the majority of companies in their beta Customers from Content program said leads converting from their email list were near zero, and most could not recall the last time they got a paying customer from the list. Their typical case is 900 email subscribers a month producing 1.8 leads a month on average. They name three causes: an undeveloped drip strategy, meaning literally no strategy at all; infrequent emailing, the once-a-month cadence; and the best prospects self-selecting into the lead form rather than the list. The underlying argument is a definitional one they make early: someone who joins your list has expressed interest in your content, not in your product, so calling them a lead is a category error that hides how weak the funnel is.

> "900 email subscribers a month but only 1.8 leads from the email list a month"

**Evidence:** Grow and Convert's beta program cohort reported near-zero email-sourced leads; their typical case is 900 subscribers a month yielding 1.8 leads.

**Pitfall:** Buying marketing automation software on the strength of subscriber growth. If line 7 is near zero, the volume of opt-ins is irrelevant and the spend produces nothing.

**Apply at Pabau:** David should check how many Pabau demo requests actually originate from newsletter subscribers before any further list investment. If the number resembles 1.8 a month, reallocate that effort to bottom-funnel articles and template pages that ask for a demo directly.

**Apply anywhere:** Check how many of your leads actually originate from newsletter subscribers before investing further in the list. If the number is near zero, move that effort to bottom-funnel content that asks for the sale directly.

### 13. Expect three conversion tiers: 2.7% BOFU, 1.06% mid-funnel, 0.5% TOF  `135.11`
*core · general insights · source 135*

Grow and Convert publish the per-tier conversion rates from this engagement, which give a benchmark for deciding what to write when bottom-funnel ideas run out. Specific bottom-of-funnel keywords converted at 2.7% on average, with 'video logging software' at 3.7% and 'online video editor' at 1.85%. Mid-funnel pain-point keywords averaged 1.06%, though the disruption story hit 9.8%. Top-of-funnel terms sit around 0.5%. Their conclusion is that when you exhaust bottom-funnel ideas you move up one step to mid-funnel pain points, not sideways into high-volume awareness content, because the volume on broad terms does not compensate for a five-fold conversion gap and those terms are harder to rank for. The comparison keyword post was the single best performer at 2.62%.

> "The specific BOTF keywords had, on average, a 2.7% conversion rate"

**Evidence:** Grow and Convert client data: BOFU 2.7% average, mid-funnel pain point 1.06%, TOF around 0.5%; 'video logging software' 3.7%, 'online video editor' 1.85%, alternatives post 2.62%, disruption story 9.8%.

**Pitfall:** Justifying a top-funnel program on volume alone. At 0.5% you need roughly five times the traffic of a bottom-funnel post to match it, on terms that are also harder to rank for.

**Apply at Pabau:** When Pabau's bottom-funnel list is exhausted, David should commission mid-funnel how-to articles about practice tasks rather than broad aesthetics-industry explainers, and hold each tier to these benchmarks in reporting.

**Apply anywhere:** Use 2.7% for specific bottom-funnel posts, around 1% for mid-funnel pain-point posts and around 0.5% for top-funnel as planning benchmarks, and move up the funnel one step rather than sideways into awareness content.

### 14. Fix drip strategy and cadence before blaming the list itself  `147.7`
*core · concrete actions · source 147*

Grow and Convert name three specific causes when nobody from the email list becomes a lead, and they are worth separating because two are fixable and one is structural. First, an undeveloped drip strategy, which they describe bluntly as having literally zero strategy. Second, infrequent emailing, the once-a-month cadence. Third, the best customers self-selecting to fill out a lead form instead of joining the list, which no email sequence can fix because those buyers were never on the list. They see this pattern in development agencies and enterprise software companies with high-touch B2B sales. Their recommendation is that if the third cause dominates, do not spend on marketing automation. Invest instead in user research and bottom-of-funnel content that converts readers directly.

> "An undeveloped drip email strategy (Having literally zero strategy.)"

**Evidence:** Grow and Convert see this in development agencies and enterprise software companies with high-touch B2B sales processes.

**How to do it**

1. Write down the current drip sequence email by email; if it does not exist, that is cause one and it is your first fix.
2. Check send frequency over the last 90 days; a once-a-month cadence is cause two.
3. Query the CRM for your last 20 closed customers and check how many were ever on the email list before converting.
4. If most closed customers never subscribed, accept that self-selection is the dominant cause and stop optimizing the sequence.
5. In that case, redirect the budget from marketing automation to user research interviews and bottom-of-funnel articles.
6. If the sequence and cadence are genuinely the problem, build a defined drip with a stated pitch point and raise frequency, then re-measure the email-to-lead rate after 90 days.
7. Re-run the nurture-versus-direct multiplication with the new rate before committing to either path permanently.

**Pitfall:** Rewriting the nurture sequence when the real cause is self-selection. If your strongest buyers skip the list entirely, better emails reach only the people who were never going to buy.

**Apply at Pabau:** Pabau's buyers are practice owners who tend to book a demo when ready. David should check whether any recent Pabau customers came through the newsletter first; if not, put the effort into bottom-funnel articles rather than sequence tuning.

**Apply anywhere:** Check whether your recent customers were ever on the list before converting. If they were not, the sequence is not the problem, and bottom-funnel content beats sequence tuning.

### 15. Fix keyword buying intent before running any CRO tweak  `143.1`
*core · concrete actions · source 143*

Grow and Convert, writing from conversion measurement across hundreds of blog posts and dozens of clients, argue the highest-impact conversion lever on a blog is not CRO at all. It is which keywords the posts rank for. They say popups with CTAs, lead magnets and long product-selling sections will not move much on a post whose visitors arrived from a low-intent query, because those readers are either too early in the journey or not in the market at all. Their example: a social media software company targeting 'how to stand out on Twitter' has no signal of purchase intent, while a searcher of 'best social media management software' does. Their conclusion is blunt: even with content that is not especially high quality, ranking for terms where people are actively looking to buy will beat any CRO program on a low-intent page.

> "trying to solve that by making CRO tweaks to your site"

**Evidence:** Grow and Convert measured conversion rates for hundreds of blog posts across dozens of clients; in their Pain Point SEO analytics screenshot, the three posts targeting high buying intent keywords produced signups hundreds of percent higher than the rest.

**How to do it**

1. List every blog URL with its primary ranking query from Search Console.
2. Label each query as buying intent (best X, X software, X alternatives, X pricing) or not.
3. Pull conversions per URL and compare the two labels before touching any page element.
4. If low-intent posts dominate the archive, stop the CRO backlog and reassign the budget to new buying-intent posts.
5. For each product or service you sell, list the terms a ready buyer would type and check which you rank for.
6. Publish or rebuild pages against those terms first, accepting lower search volume.
7. Only after a page ranks for a buying-intent term, test CTA placement, popups and social proof on it.
8. Re-measure conversions per URL by intent label each quarter to confirm the gap persists.

**Tools:** Google Search Console, Google Analytics 4

**Pitfall:** Teams read a flat conversion rate as a CRO failure and spend months on heatmaps and A/B tests. The signal you have hit this is a post with healthy traffic, a strong CTA and near-zero signups: the query, not the page, is the problem.

**Apply at Pabau:** David should label every Pabau blog URL by query intent before scheduling any CTA work. Posts ranking for definitional aesthetics terms will not convert however the book-demo block is styled, and the effort belongs on comparison, alternatives and software-category pages.

**Apply anywhere:** Label every blog URL by the buying intent of the query that drives it before you spend anything on conversion optimization. Low-intent pages will not convert whatever you do to the CTA, so move the budget to pages targeting terms a ready buyer types.

### 16. Gate an asset only when the asset itself carries buying intent  `105.5`
*core · best practices · source 105*

Grow and Convert draw a single line through the gating debate. Gating is right when the downloadable resource is itself the answer to a high-intent search, and wrong when it exists to salvage value from traffic that will not convert. Their positive example is a 'project budget template' page: the searcher has an immediate practical need, the download is what they came for, so the email exchange is low friction and natural. Their negative example is an ebook gate placed in front of a reader searching 'best CRM for small businesses', who wants to compare options and decide now. Adding a form there inserts friction into the moment of highest intent. Their diagnostic is blunt: if you are gating because blog traffic is not converting, the problem is the keywords, not the lead magnet.

> "The difference comes down to whether you're gating content because readers actually want"

**Evidence:** Grow and Convert regularly build gated template pages for clients targeting JTBD queries like 'project budget template', while removing gates from comparison content such as 'best CRM for small businesses'.

**How to do it**

1. For each gated asset, name the keyword the page targets and check whether the asset is the literal thing that searcher is looking for.
2. Keep the gate on template, tool, checklist and calculator pages where the download is the answer to the query.
3. Remove the gate from any page targeting a comparison, category or alternatives keyword.
4. On those ungated pages, do the selling in the body: options, trade-offs and where your product wins.
5. Audit existing gates by pulling each gated page's conversion-to-customer rate, not its form-fill rate.
6. Kill any gate whose downloads never progress to a demo or a sale.
7. When a gate is failing, rewrite the keyword target rather than redesigning the lead magnet.
8. Keep one ungated path to the primary CTA on every high-intent page.

**Pitfall:** Reporting form fills as leads hides the failure. Grow and Convert describe companies posting impressive lead counts to executives from low-intent gated downloads, then wondering why none become revenue. The tell is a large list with near-zero nurture open rates.

**Apply at Pabau:** Pabau's /templates/ pages are the correct place for a download box, because the template is what the searcher wants. David should not add gated downloads to comparison or 'best software' articles, where the download box would sit between a ready buyer and the demo CTA.

**Apply anywhere:** Keep gates only on template, tool and checklist pages where the download is the literal answer to the query. Remove them from comparison, category and alternatives pages, and judge every gate on downloads that become customers rather than on form fills.

### 17. Give away the free product as a wedge into $1,000-a-month offers  `170.6`
*core · concrete actions · source 170*

Because ProfitWell could not be sold as a subscription, Campbell made it free. 'ProfitWell essentially was going to be our wedge,' he says. The free analytics product generates leads for two higher-priced products, Retain and Recognized, plus the Price Intelligently service. He is explicit that this is freemium with an unusual gap: instead of a paid tier at $49 or $99, the paid versions start at $1,000 a month. The free tier is not a discounted version of the paid one, it is a diagnostic that tells both sides when the paid product is needed. ProfitWell crossed $1 million in annual revenue and also feeds the $6 million service business.

> "ProfitWell essentially was going to be our wedge"

**Evidence:** ProfitWell crossed $1 million in annual revenue as a free product feeding paid tiers, while Price Intelligently grew past $6 million.

**How to do it**

1. Identify the free asset that requires the customer to connect real data or answer real questions, not just read a page.
2. Make it genuinely free and complete for its own job, with no crippled features that force an upgrade.
3. Choose paid products that solve a problem the free asset can detect, not a bigger version of the free asset.
4. Set the paid price by value to the customer, not as a multiple of the free tier; Campbell's starts at $1,000 a month.
5. Instrument the free product so you can see the condition that signals the paid product is relevant.
6. Trigger the offer on that condition rather than on a calendar-based drip.
7. Accept a long payback window and fund it from another revenue line while lead generation builds.

**Tools:** Stripe

**Pitfall:** The wedge delays cash badly. Campbell says it took months for ProfitWell's lead generation to get traction, which only worked because the service business was funding it.

**Apply at Pabau:** Pabau's free tools and template pages are the wedge. David should make each one genuinely useful standalone, then instrument it so the demo offer fires on a signal the tool detects, rather than putting a generic book-a-demo banner on every page.

**Apply anywhere:** If your core product cannot carry a subscription, make it free and use it as the diagnostic that qualifies buyers for a much higher-priced offer. Instrument the free tier to detect the condition your paid product fixes.

### 18. Give every post an in-article CTA written for that post's topic  `90.4`
*core · concrete actions · source 90*

Grow and Convert credit part of their conversion advantage to in-article CTAs that are contextual to the post rather than a generic site-wide banner. The example they give for a post about best CRM tools is a CTA reading along the lines of 'Looking for a CRM tool for your small business? Try a free trial of X tool for 30 days, free.' The CTA restates the reader's situation in the words of the article's topic, then names the specific next step. This matters most on jobs-to-be-done posts, where the reader arrived with a task rather than a product in mind and needs the connection between the task and the product made explicit. A generic 'book a demo' box placed on every article ignores that the reader of a migration how-to and the reader of a comparison page are at different points and need different offers.

> "we use in-article CTAs that are contextual to the post"

**Evidence:** Grow and Convert name contextual in-article CTAs as one of the reasons their bottom-of-funnel posts convert at 0.3% to 4.3% against 0.03% to 0.19% for top-of-funnel posts.

**How to do it**

1. List every blog post that currently carries the same site-wide CTA block.
2. For each post, write the reader's situation as a question in the article's own vocabulary, e.g. 'Looking for a CRM tool for your small business?'
3. Follow it with one specific next step naming the product and what the reader gets, e.g. a trial length or a named feature.
4. Place the CTA inside the body of the article near where the reader is most likely to feel the problem, not only at the very bottom.
5. Keep one CTA per topic; do not stack a contextual CTA and a generic one on the same page.
6. Track conversions per landing page so you can compare the contextual CTA against the previous generic block.
7. Rewrite the CTA whenever the article is refreshed and its angle changes.

**Pitfall:** Swapping in a contextual CTA but keeping the generic footer banner splits attention and makes the comparison meaningless. If conversion per page does not move after the swap, check whether the old CTA is still on the page.

**Apply at Pabau:** Pabau's blog CTA should not be the same book-a-demo block on every article. An article about no-show rates should offer the reminders feature by name; a competitor comparison should offer a migration conversation.

**Apply anywhere:** Replace the site-wide CTA block with a per-article CTA that restates the reader's situation in the article's own words and names one specific next step.

### 19. Give the full audit and the secret sauce away before quoting  `173.7`
*core · best practices · source 173*

KlientBoost's step four is a free audit: they brainstorm ideas for improving the prospect's PPC campaigns and send a proposal describing everything the client could and should do. On the follow-up call they answer every question honestly and, in Grow and Convert's wording, do not hold back any insider info or secret sauce. Dane is unbothered by prospects stealing the advice, and the reason is structural rather than optimistic. The qualification filter has already established the company spends heavily on ads, so it has both the budget and the reason to hire out rather than execute in-house. The generosity is the same instinct as the cold emails that started the company: give ideas away, then let the buyer decide they would rather you ran them.

> "they'll brainstorm ideas for how to improve a client's PPC campaigns, for free"

**Evidence:** KlientBoost holds 80+ clients and 16 account managers on this process, with Dane personally running the sales stage.

**How to do it**

1. Only offer the free audit to leads that have already cleared your size and spend checks.
2. Cap the audit at a fixed number of hours so the unpaid work stays bounded.
3. Write the proposal as a list of things the prospect could and should do, in their order of impact.
4. Include the method, not just the finding, so the document is genuinely usable without you.
5. Book a call to walk through it rather than emailing it and waiting.
6. Answer every implementation question fully, including how you would do it.
7. Only after that walkthrough, ask the upside question and quote a fee.
8. Track how many audited prospects implement alone and never buy; if it is more than a fifth, tighten qualification rather than withholding advice.

**Pitfall:** Giving free audits to unqualified leads is where this becomes expensive. Dane can afford it because only 3 to 4 of 30 to 40 weekly leads reach the audit stage at all.

**Apply at Pabau:** Pabau can run the same play as a free workflow audit for a practice: map their current booking, consent and follow-up process and hand back the fixes, including the ones that do not need Pabau. Gate it behind the size and paid-acquisition checks so it stays affordable.

**Apply anywhere:** Once a lead is properly qualified, give away the full audit and your actual method rather than teasing it. Prospects with real budget and real spend hire the work out; withholding detail only makes you look like every other vendor.

### 20. Homepage SEO copy taxes your highest-traffic, non-SEO page  `41.3`
*core · best practices · source 41*

Edward's central argument against homepage keyword-stuffing is a traffic-mix insight: the homepage is typically the single page on a website that receives the most visits from non-SEO marketing channels combined, meaning direct traffic, public relations coverage, social media, and referral traffic. When you optimize that specific page's copy for SEO keyword relevance instead of for conversion, you are degrading the conversion experience for the largest pool of already-arriving, non-organic visitors purely to chase organic rankings that a dedicated page could capture just as well without that tradeoff. He calls this a 'huge L,' meaning a significant unforced loss, because the cost of lost conversions from your highest-traffic page is being paid across all channels to fund a benefit, keyword relevance, that only helps the smaller organic-search slice of that traffic.

> "optimizing it for SEO copywriting and not for conversions"

**How to do it**

1. Pull your homepage's traffic-source breakdown in your analytics tool, such as GA4, and confirm what share comes from direct, PR/referral, social, and organic search versus other pages on your site.
2. If the homepage is indeed your highest-traffic page across non-SEO channels, treat its copy as a conversion-rate-optimization priority first, not an SEO-copywriting priority.
3. Remove or relocate any secondary or tertiary keyword-stuffed H2 sections from the homepage that exist purely for SEO relevance rather than to help a visitor understand and act on your offer.
4. Rewrite the homepage's hero section and H1 around your core value proposition and benefits, rather than around a keyword phrase.
5. Redirect the keyword-targeting work that used to live on the homepage to dedicated landing pages instead, so no ranking potential is lost, only relocated.
6. Compare homepage conversion rate before and after removing keyword-driven copy and substituting conversion-focused copy, to confirm the expected lift (inferred).

**Pitfall:** Optimizing your homepage's copy for SEO keyword relevance directly taxes conversion rate on the page that collects the most non-SEO traffic, direct, PR, social, referral - treating this as an acceptable tradeoff for organic-keyword gains is, in Edward's words, 'a huge L,' since a dedicated page can capture the same keyword relevance without costing you conversions on your highest-traffic page.

### 21. Interview both buyers and non-buyers after every launch  `183.4`
*core · concrete actions · source 183*

After both the phone course and the failed online launch, Grow and Convert ran structured exit interviews. The buyer interviews revealed that access, not content, drove the purchase. The non-buyer feedback revealed the persona mismatch and surfaced a demand they had not planned for: business owners repeatedly asking whether they offered a done-for-you content marketing service. They also learned from exit interviews after the phone course that companies struggled to measure content ROI and wanted help scaling writing teams, and they turned both into new modules. The pattern is that the post-mortem, not the launch, produced the next business. Interviewing only buyers would have missed the agency demand entirely.

> "get feedback from the customers who purchased and the prospects who didn't purchase"

**Evidence:** Non-buyer interviews after the course launch surfaced repeated requests for a done-for-you service, which became the agency that replaced the course business.

**How to do it**

1. Within two weeks of a launch closing, list both cohorts: everyone who bought and everyone who visited the landing page or replied but did not buy.
2. Ask buyers one question first: what was the main reason you bought, in your own words.
3. Ask non-buyers what they expected the offer to be and what they would have bought instead.
4. Log every unprompted request that arrives through the landing page form or reply emails, even off-topic ones.
5. Tally repeated requests across the non-buyer set; a question asked by multiple prospects is a product signal, not noise.
6. Turn the recurring pain points buyers name into new modules or sections of the offer (they added ROI measurement and scaling writing teams this way).
7. Compare the words buyers use to describe the value against the words on your landing page and rewrite where they diverge.
8. Decide the next offer from the non-buyer tally, not from the buyer praise.

**Pitfall:** Interviewing only happy buyers. They confirm the product you built and cannot tell you about the larger group that wanted something adjacent, which is where the next revenue line usually is.

**Apply at Pabau:** After any Pabau launch, campaign or gated asset, David should collect the questions that came in and did not match the offer. Practices asking for something Pabau does not sell yet is the highest-value output of a launch, and it should be logged in one place rather than answered ad hoc in inboxes.

**Apply anywhere:** Run exit interviews with both cohorts after every launch. Buyers tell you why the thing sold; non-buyers tell you what you should have sold. Log every repeated off-offer request, because that tally usually names your next product.

### 22. Interview non-buyers by survey and phone to find the positioning miss  `159.2`
*core · concrete actions · source 159*

After the failed course launch, Grow and Convert emailed a survey to their list and got on the phone with a handful of people they knew, asking why they did not buy. The answer that repeated was: 'I don't really care about taking a course so I can help my company. I want to take a course to help myself.' That single theme reframed the whole product. Buyers wanted to become great content marketers who could work anywhere, not to drive leads for their current employer. One person said the company-focused opening line made him start skimming instead of reading. The method matters as much as the finding: they mixed a broad survey for volume with a few calls for depth, and they asked non-buyers rather than customers.

> "we emailed a survey out to folks as well as got on the phone"

**Evidence:** More than one respondent independently said they wanted the course for themselves, not for their company, which drove the rewrite that lifted conversion roughly 6x.

**How to do it**

1. List everyone who saw the offer and did not convert, using email opens or page visits rather than customers.
2. Send them a short survey asking one question: why did you not buy?
3. Pick five to ten people you have some relationship with and book phone calls instead of relying on written answers.
4. On the call, read them the current headline and opening sentence and ask what they thought when they read it.
5. Tag every answer as a targeting problem, a pain point problem, a uniqueness problem or a credibility problem.
6. Look for a theme repeated by more than one person, and treat that as the finding rather than any single quote.
7. Test the new framing live on the phone: say the replacement phrase and note whether the person reacts with enthusiasm.
8. Rewrite the headline and opening sentence around the theme before changing anything else.

**Pitfall:** Surveying only existing customers. They already accepted the positioning, so they cannot tell you what turned everyone else away.

**Apply at Pabau:** Pabau should survey demo no-shows and trial drop-offs about why they did not book, then feed the repeated phrasing into the hero copy of the pricing and book-demo pages.

**Apply anywhere:** Survey the people who saw your offer and did not convert, then call a few of them. Feed the repeated phrasing straight into your hero copy.

### 23. Irreplaceable value (tool, transaction, service) predicts surviving updates  `43.5`
*core · content insights · source 43*

Rand's read of Cyrus Shepard's factor analysis is that the strongest predictor of surviving Google algorithm updates was not a classic SEO tactic but whether a site offers 'value that cannot be replaced in the search result itself' — a tool, an input system, an actual product or service, a way to transact, or genuine human connection. His logic: no matter how aggressively Google keeps users on its own results page, some actions structurally require leaving Google, since you still have to go to Ticketmaster to buy concert tickets or eBay to buy a used item. Conversely, sites whose entire value is 'pure information or news or content' (his example: affiliate sites and pure publishers) are structurally vulnerable, because Google and AI Overviews can increasingly answer or summarize that information without sending a click.

> "value that cannot be replaced in the search result itself"

**Evidence:** Cyrus Shepard's traffic-growth factor analysis identifying 'value that cannot be replaced in the search result' as predictive; concrete examples given: Ticketmaster (concert tickets) and eBay (a vintage necktie) as transactions Google cannot complete on its own results page.

**Apply at Pabau:** Pabau's core product (software you must sign up for and use) already has structural protection that pure content publishers lack — David should lean into content that leads to actual product actions (signup, demo booking, in-app tools) rather than purely informational pages that Google or AI Overviews could fully answer without a click.

**Apply anywhere:** Your core product (software you must sign up for and use) already has structural protection that pure content publishers lack — you should lean into content that leads to actual product actions (signup, demo booking, in-app tools) rather than purely informational pages that Google or AI Overviews could fully answer without a click.

### 24. Judge CAC against 6-18 months of revenue, not against LTV  `152.2`
*core · best practices · source 152*

Grow and Convert reject the common CAC < LTV test as almost meaningless. If LTV is $300 and CAC is $299 you make one dollar over the customer's whole life. They cite Jason Lemkin of Storm Ventures and SaaStr saying successful SaaS companies spend 20 to 30 percent of LTV to acquire a customer. Their preferred test is more intuitive: how many months of monthly recurring revenue does it take to pay back the acquisition cost. The benchmarks they keep seeing are 18 months for large enterprise businesses and 6 to 12 months for smaller consumer businesses. Applied to their own app Wordable at $19 a month, that means an acceptable CAC of roughly $120 to $200. The payback test only holds if average customer tenure comfortably exceeds the payback window.

> "18 months is typical for large enterprise businesses"

**Evidence:** Jason Lemkin's 20-30% of LTV benchmark; $100-$500 typical SaaS CAC also cited by Ada Chen Rekhi; Wordable at $19/month gives a $120-$200 ceiling.

**How to do it**

1. Take your average monthly recurring revenue per customer, not annual contract value.
2. Pick a payback window: 6 to 12 months for self-serve or consumer, 18 months for enterprise.
3. Multiply MRR by that window to get your maximum acceptable CAC.
4. Check average customer tenure and churn; if tenure is shorter than the payback window, cut the window until it fits.
5. Cross-check the result against the 20 to 30 percent of LTV rule as a second opinion.
6. Compare your measured content CAC to that ceiling and label content as viable, borderline or failing.
7. Repeat the check when pricing changes, since the ceiling moves with MRR.

**Pitfall:** Setting the payback window longer than your actual customer tenure. The number then looks acceptable while the business never recovers the acquisition spend.

**Apply at Pabau:** Pabau should set an explicit CAC ceiling from its own average subscription value and payback window, then hold blog and template pages to it. That ceiling decides whether more freelance writing is worth commissioning.

**Apply anywhere:** Set an explicit CAC ceiling from your own average monthly revenue and a payback window that is shorter than your customer tenure, then hold each acquisition channel to it.

### 25. Judge paid search on MQLs and cost per MQL, not leads  `158.1`
*core · concrete actions · source 158*

Grow and Convert took over an ecommerce development agency's Google Ads account and found the previous agency's reporting looked healthy: 26 leads in three months at roughly $1,077 per lead, a 6.25% average CTR and about 55,000 impressions. Once the client filtered those leads against its own MQL criteria for company size, industry and project needs, only 2 survived, which works out to 0.67 MQLs a month at about $14,000 each against a target acquisition cost of $8,000. The agency rebuilt the account around buying intent and after six months reported roughly 1.4 MQLs a month at $3.2k per MQL. The lesson is that up-funnel metrics like CTR, CPC and raw lead count can mask a failing account, so the only two numbers worth reporting are total MQLs and cost per MQL.

> "the metrics that truly matter: total MQLs and cost per MQL"

**Evidence:** Ecommerce dev agency client: 0.67 MQLs/month at ~$14k each before, ~1.4 MQLs/month at $3.2k each after six months.

**How to do it**

1. Write down the qualification criteria a lead must meet to count as an MQL, covering company size, industry and project scope.
2. Export the last 90 days of form fills from the ad account and tag each one against those criteria.
3. Delete solicitous form fills and other junk leads before any counting, so the denominator is real.
4. Divide total ad spend for the period by the surviving MQL count to get true cost per MQL.
5. Compare that figure to the acquisition cost the business can actually afford, not to CPC benchmarks.
6. Rebuild the reporting dashboard so MQLs per month and cost per MQL sit at the top and CTR, CPC and impressions sit below as diagnostics.
7. Re-run the same calculation monthly and refuse to judge any keyword or campaign on lead volume alone.

**Tools:** Google Ads

**Pitfall:** Agencies report leads, CTR and CPC because they look good. A 6.25% CTR and $1,077 leads hid a $14,000 cost per qualified lead. The signal you have hit this is a sales team saying the leads are unusable while the dashboard says the campaign is winning.

**Apply at Pabau:** Pabau should not report demo-request volume from paid or organic as the headline number. Define an MQL as a practice of the right size and specialty, tag every form fill from /book-demo/ against it in the CRM, and report cost per qualified practice by channel.

**Apply anywhere:** Do not report raw lead volume as your paid search headline. Define what a qualified lead is for your business, tag every form fill against it, and report cost per qualified lead by channel instead.
