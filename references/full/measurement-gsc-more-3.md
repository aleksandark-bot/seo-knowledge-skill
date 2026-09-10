# Measurement & GSC — supporting (part 3 of 4)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Name the four questions your conversion reports must answer  `154.8`
*useful · best practices · source 154*

Grow and Convert scope the whole exercise by writing down what they want to know before opening any report. At the top level: how many leads came from content, from paid media and from social media. Then one level deeper inside each: which blog posts brought in the most leads, which paid campaigns brought in leads at the lowest acquisition cost, which social platforms brought in leads, and across all three, which landing pages or calls to action convert best. Google Analytics already has built-in reports that answer each of those, so the work is mapping question to report rather than building anything custom. Writing the questions first is what stops the exercise turning into a dashboard project that produces charts nobody asked for.

> "Which landing pages or calls to action are converting the best?"

**How to do it**

1. Write the four questions down before opening Analytics: leads by channel, best converting blog posts, cheapest paid campaigns, best converting calls to action.
2. Map each question to its report: channels for the first, Landing Pages for the second, Source/Medium and campaign for the third, Landing Pages plus on-page CTA variants for the fourth.
3. Confirm the thank you page goal is live, since every one of those reports is empty without it.
4. Answer each question once, in writing, with the number and the date range.
5. Delete any report that does not answer one of the four questions.
6. Revisit the question list quarterly and add one only when a decision actually needs it.

**Tools:** Google Analytics

**Pitfall:** Starting from the reports rather than the questions produces a dashboard full of metrics that never changes a decision, and it buries the two or three numbers that would.

**Apply at Pabau:** For Pabau the fourth question is the underused one: which CTA placement inside articles produces demo requests. Compare articles where the Pabau CTA block sits before the conclusion against those where it appears earlier.

**Apply anywhere:** The fourth question is usually the underused one: which in-article CTA placement produces conversions. Compare articles where the CTA sits near the end against those where it appears mid-article.

### 2. NavBoost's "base rank" vs "test rank" means Google actively tests your position  `25.10`
*useful · content insights · source 25*

Koray points to the content warehouse API leak's 'RankLab' module family as evidence that click data, not links or content alone, is Google's most important ranking factor. Within it, a model called 'rank lab title' tracks two attributes per page: 'base rank' (your normal, current rank) and 'test rank' (an experimental rank Google is trialing you at), meaning Google actively tests pages at different rank positions to measure click response before committing. He notes the module name isn't coincidental: Alexander Grushetsky's LinkedIn describes him as an 'end-to-end ranking system founder, aka RankLab' at Google, and this system feeds into 'NavBoost,' the collection of click data, PageRank, and topicality combined into one hybrid ranking factor, reinforcing Koray's broader argument that holistic SEO beats any single lever.

> "click data, page rank, and topicality all together"

**Evidence:** Google's content warehouse API leak: a 'rank lab title' model with 'base rank'/'test rank' attributes; LinkedIn profile of Alexander Grushetsky describing himself as 'end-to-end ranking system founder, aka RankLab'; NavBoost defined as combining click data, PageRank, and topicality.

**Apply at Pabau:** Expect Google to actively test Pabau pages at different rank positions (base rank vs. test rank) to gauge click response, meaning short-term ranking volatility after a content update may just be a NavBoost test cycle rather than a penalty — judge success over longer windows in GSC instead of reacting to week-to-week swings.

**Apply anywhere:** Expect Google to actively test your pages at different rank positions (base rank vs. test rank) to gauge click response, meaning short-term ranking volatility after a content update may just be a NavBoost test cycle rather than a penalty — judge success over longer windows in GSC instead of reacting to week-to-week swings.

### 3. Pair a rank tracker with a topic-level AI tracker on the same keyword set  `81.10`
*useful · concrete actions · source 81*

Grow and Convert run two measurements side by side for Constitution Lending. Ahrefs Rank Tracker shows the Google positions, including where the site holds first place inside AI Overviews, and Traqer, the tool they built, shows brand visibility per topic across ChatGPT, Perplexity and Google AI Overviews. The pairing is what makes the data usable, because it turns a claim into a check: for 'LLC mortgage lenders' the site ranks number one and appears in all three AI surfaces, and for the newer cash-for-houses topics the ranking is absent and so is the AI visibility. They also track close variations of the same head term, such as 'best DSCR lenders', 'top DSCR lenders', 'DSCR lenders' and 'best DSCR providers', because AI visibility is measured per topic rather than per phrase.

> "the tool we developed to track AI search visibility"

**Evidence:** Grow and Convert show Constitution Lending consistently in the top one to three brands cited across the DSCR lenders prompt set, matched against first-page Ahrefs positions for four DSCR variations.

**How to do it**

1. Build a keyword list of your bottom-of-funnel targets plus their close variations in a rank tracker.
2. Group the variations into topics, one topic per buying decision rather than per phrase.
3. Create a matching prompt basket of eight to twelve prompts per topic in an AI visibility tool.
4. Run both on the same weekly cadence so positions and AI mentions line up in time.
5. Build one sheet with topic, best Google position, and mention rate per engine as columns.
6. Flag rows where the Google position is top three but AI mention rate is low, and investigate those individually.
7. Flag rows where AI mention rate is high but rankings are weak, and check whether third-party pages are carrying you.
8. Report AI visibility at topic level only, never as a single-prompt result.

**Tools:** Ahrefs, Traqer, ChatGPT, Perplexity

**Pitfall:** Reporting AI visibility for one prompt per topic. Users run long multi-turn conversations, so nobody knows the exact phrasing, and a single prompt result moves week to week for reasons unrelated to your work.

**Apply at Pabau:** Pabau should hold one sheet joining Ahrefs positions to AI mention rates by topic, and use the mismatched rows to decide whether a page needs a rankings fix or a third-party mention push.

**Apply anywhere:** Track rankings and AI mentions on the same keyword set, grouped into topics rather than phrases, and refresh both weekly. The rows where the two disagree tell you whether to work on rankings or on third-party mentions.

### 4. Pair attribution with the time lag and path length reports  `151.5`
*useful · concrete actions · source 151*

Devesh adds two supporting reports to the model comparison view. The Time Lag report shows how many days it typically takes people to convert; in his screenshot the majority sign up within a couple of days but a decent number wait over two weeks. The Path Length report shows how many interactions with the site it typically takes before someone converts. Together these turn the first-versus-last gap into an actual number of days and touches you can plan around. He frames these as getting 'even more ninja' than the base report, but the practical payoff is concrete: they tell you how long to hold a lookback window open, how long to wait before judging a new post, and how many touches your nurture path needs to supply.

> "You can get even more ninja by combining this"

**Evidence:** Grow and Convert's Time Lag screenshot shows most conversions within a couple of days, with a meaningful tail beyond two weeks.

**How to do it**

1. Open the Time Lag report alongside the model comparison report for the same goal and date range.
2. Record the share of conversions that happen within one day, within two weeks, and beyond two weeks.
3. Open the Path Length report and record the modal number of site interactions before conversion.
4. If most conversions need three or more interactions, plan retargeting or email capture rather than a single-post CTA.
5. Set your minimum evaluation window for a new post to at least the ninetieth-percentile time lag.
6. Re-check both reports whenever pricing or the funnel changes, since the lag moves with deal size.

**Tools:** Google Analytics

**Pitfall:** Judging a new post's conversion performance before the typical time lag has elapsed reads a partial number as a final one and kills posts that were still converting.

**Apply at Pabau:** David should measure Pabau's own time lag from first blog visit to demo booking, then use it as the minimum wait before judging whether a new article converts.

**Apply anywhere:** Measure your own typical days-to-convert and interactions-to-convert, then use those figures as the minimum evaluation window for any new page.

### 5. Place the ad pixel on the thank-you page, not just the landing page  `155.18`
*useful · concrete actions · source 155*

Grow and Convert note a measurement gap in Erika's setup that they had to work around. In her Facebook reporting, a conversion is only a click through to the landing page, because the ad pixel was never placed on the thank-you page. Facebook therefore never tracked the step from landing page to opt-in, and the authors had to pull opt-in numbers from LeadPages instead. She also never put the Google Analytics snippet on the LeadPage, which is why the comparison against her main site traffic had to be made from two separate tools. The consequence is that Facebook's optimization had nothing but clicks to learn from, and the reported cost per conversion of six cents is really cost per visitor.

> "The ad pixel was not placed on the Thank You page"

**Evidence:** Erika's reported six cents per conversion was cost per landing page visitor; opt-in counts had to come from LeadPages instead.

**How to do it**

1. Install the ad platform pixel on the landing page and the thank-you page before the first dollar is spent.
2. Define the conversion event on the thank-you page URL, not the landing page.
3. Add your web analytics snippet to the hosted landing page too, since hosted tools do not inherit it.
4. Set the campaign objective to that conversion event so the platform optimizes for opt-ins, not clicks.
5. UTM tag every ad URL so sessions can be reconciled across tools.
6. Label the platform's cost per conversion as cost per visitor whenever the pixel only fires on the landing page.
7. Reconcile platform conversions against the landing page tool's opt-in count weekly.
8. Fix any gap before scaling budget, since the platform cannot optimize toward an event it cannot see.

**Tools:** Facebook Ads, LeadPages, Google Analytics

**Pitfall:** With the pixel only on the landing page, the platform optimizes for cheap clickers rather than subscribers, and the reported cost per conversion silently means something else than the team assumes.

**Apply at Pabau:** Any Pabau paid test using a hosted landing page needs the pixel and the analytics snippet added to both the page and the confirmation page before launch, otherwise the channel report cannot be compared with organic.

**Apply anywhere:** Fire the ad pixel on the thank-you page and optimize the campaign toward that event, or the platform will buy clicks instead of subscribers.

### 6. Plan around Google sunsetting the rules-based attribution models  `149.11`
*useful · general insights · source 149*

Grow and Convert record that in May 2023 Google announced it would start sunsetting first click, linear, time decay and position-based attribution models. Their response is not to abandon rules-based reporting but to narrow it: keep using the model comparison tool for last click, which survives, and move the first-click and influenced-conversion work into an any-touchpoint exploration built from a sequence segment. That matters because the segment approach does not depend on GA4's attribution model list at all. It defines users by behavior, landed on these URLs then converted, so it keeps working regardless of which named models Google retires next.

> "they'd start sunsetting functionality for first click"

**Evidence:** Google announced in May 2023 that it would begin sunsetting first click, linear, time decay and position-based attribution models.

**How to do it**

1. Assume first click, linear, time decay and position-based will not be available long term.
2. Keep the model comparison tool in the reporting stack for last click only.
3. Move first-touch and assisted-conversion reporting into an Explore sequence segment instead.
4. Build that segment from behavior, landing page then conversion event, so it does not depend on a named model.
5. Re-verify each report at the start of a quarter, since deprecations arrive without warning in the interface.
6. Archive a screenshot or export of any model-dependent report before its model is retired, so history is not lost.

**Tools:** Google Analytics 4

**Pitfall:** A reporting stack built on a deprecated model breaks quietly, and the first sign is usually a client asking why a familiar number disappeared.

**Apply at Pabau:** Pabau should not build its content reporting on GA4's named attribution models; base the demo-attribution report on a behavioral segment that survives deprecation.

**Apply anywhere:** Base content conversion reporting on behavioral segments rather than GA4's named attribution models, which are being retired.

### 7. Quantify the AI share of leads before reallocating content budget  `80.10`
*useful · best practices · source 80*

Grow and Convert opened with their own number: in the past month alone, 71% of their new leads came through ChatGPT, measured by a 'How did you hear about us?' survey response, and they show a chart of ChatGPT referrals over time. They add a second, softer signal, that clients mention the same shift in emails and on monthly calls. The base already says to ask 'how did you hear about us'. What this adds is using the answer as the trigger for a strategy change rather than as a reporting curiosity, and the caution that this is one agency's mix, not a benchmark to copy.

> "71% of our new leads came through ChatGPT"

**Evidence:** Grow and Convert report 71% of new leads in one month came through ChatGPT, based on their signup survey.

**How to do it**

1. Make 'how did you hear about us' a required free-text or option field at signup or first contact.
2. Include the named AI tools as explicit options so people do not answer 'internet'.
3. Chart the AI share month over month rather than reading a single month.
4. Cross-check against referral traffic from the AI domains, knowing the two will not match because many arrive untracked.
5. Ask the same question on sales calls to catch the ones who skipped the form.
6. Only shift content budget toward AI-first work once the share has held for several months.
7. Report your own number rather than citing anyone else's percentage as a benchmark.

**Tools:** ChatGPT

**Pitfall:** Copying someone else's percentage into your own plan. A marketing agency's audience is unusually AI-native, and a healthcare or local buyer base will show a very different share.

**Apply at Pabau:** Pabau should keep the source-of-lead question mandatory with ChatGPT, Perplexity and Gemini as named options, and chart the share monthly before deciding how far to tilt the blog toward AI-first content.

**Apply anywhere:** Make the source-of-lead question mandatory with AI tools named as options, chart the share over several months, and use your own trend, not a published percentage, to decide budget shifts.

### 8. Re-rank converting posts under first-click before judging a framework  `90.11`
*useful · concrete actions · source 90*

Grow and Convert do not settle the question on last-click alone. After ranking posts by last-click conversions they run Google Analytics' model comparison tool over a fixed window, in their example 1 January to 29 August, to see which content frameworks yield the most new trial signups when first-click conversions are also counted. This matters because bottom-of-funnel comparison and category pages tend to win under last-click while jobs-to-be-done posts often did the introducing and only show up under first-click. Running only one model systematically over-credits one framework and would lead you to cut the other. In their case the conclusion held under both models: only three of the top ten posts were top of funnel and those three accounted for 10% of conversions. This also sits against Grow and Convert's later advice, in their AI SEO material, to measure organic conversions site-wide rather than article by article. Here they do the per-article analysis and use it to set the content mix.

> "let's look at GA's model comparison tool"

**Evidence:** Grow and Convert ran the model comparison tool over 1 January to 29 August on their own site and found three of the top ten converting posts were top of funnel, contributing 10% of conversions.

**How to do it**

1. Fix a window of at least six months so slower-converting posts have time to appear.
2. Export the top converting organic landing pages under last-click attribution.
3. Run the same window through GA's model comparison tool with first-click as the second model.
4. Build one table with both numbers per post and note which posts change rank sharply between models.
5. Label every post in the table with its framework: category, comparison, jobs-to-be-done, or top of funnel.
6. Sum conversions by framework under each model rather than reading individual posts.
7. Only cut a framework if it underperforms under both models; posts that rise under first-click are doing introduction work.
8. Set the next quarter's publishing mix from the framework totals, not from the single best post.

**Tools:** Google Analytics

**Pitfall:** Judging jobs-to-be-done posts on last-click alone. They frequently start the relationship and finish it nowhere, so a last-click-only report makes the mid-funnel framework look worthless and pushes you into comparison pages only.

**Apply at Pabau:** Pabau's blog reporting should show demo requests under both first-click and last-click. Clinic-task how-to articles will look weak on last-click and are likely doing the introduction that the comparison pages close.

**Apply anywhere:** Rank your converting posts under both first-click and last-click attribution over a six-month window, total the results by content framework, and only cut a framework that loses under both models.

### 9. Read qualitative survey data as test hypotheses, not as significant findings  `161.10`
*useful · best practices · source 161*

Khanal preempts the objection that segmented survey data is not statistically significant. He agrees it is not, and says that misses the point. The output is indicators on areas to explore, not conclusions. The process should give you ideas to test: feature improvements, product improvements, messaging, marketing channels. His instruction for reading the data is mechanical. Take all responses to each question, look for patterns among the answers, write down the things that stand out per question, and turn those into tests. That reframing matters because teams either dismiss small-sample research entirely or over-trust it. The correct treatment is to let it generate the hypothesis and let a live test settle it.

> "this is just supposed to give you indicators on areas to explore"

**Evidence:** Khanal concedes segmented data is not statistically significant and reframes the purpose as generating ideas for tests across features, messaging and marketing channels.

**How to do it**

1. Stop counting responses as percentages once a segment drops below roughly thirty answers.
2. Read every answer to one question in a single sitting before moving to the next question.
3. Write down anything that stands out, in the respondent's own wording, in a notes column.
4. Group the notes into patterns and name each pattern in one sentence.
5. Convert each pattern into a testable statement, such as 'leading with X in the headline will beat Y'.
6. Rank the hypotheses by how cheap and fast the test is, not by how confident you feel.
7. Run the cheapest tests first as ad copy or landing page variants.
8. Log the result of every test in one sheet so the research is judged by what it produced.

**Pitfall:** Two failure modes sit either side of this. Teams either discard the research because n is small, or quote a three-person theme as proven customer insight in a strategy deck. Both skip the test.

**Apply at Pabau:** Pabau should treat survey themes as candidate hypotheses logged in a test sheet, then validate them as title tag or hero copy tests on existing pages before rewriting a whole content cluster around them.

**Apply anywhere:** Treat small-sample survey themes as hypotheses. Log each one, test the cheapest ones as ad or headline variants, and record what the test returned.

### 10. Read repeated email opens as an internal forwarding signal before following up  `162.10`
*useful · best practices · source 162*

Peralta uses open tracking for more than a binary opened or not opened. When he emailed Amplitude's Content Marketing Manager, the tracker showed the message had been forwarded and opened 35 times in three days. He read that count as proof that the pitch was circulating internally and that interest was real, so he timed a follow-up a few days later rather than giving up or chasing immediately. The general rule this implies: an open count far above one means the thread is being discussed by more than one person, and the correct response is patience plus one well-timed nudge. A single open followed by silence means something different, and a zero-open means the subject line failed, which is a separate fix.

> "the email had been forwarded and opened 35"

**Evidence:** A 35-opens-in-3-days count on the Amplitude email told Peralta the pitch was being forwarded internally; the follow-up a few days later landed the interview.

**How to do it**

1. Run every outreach email through a tracker that reports per-open counts, not just a first-open flag.
2. Classify each prospect after 3-4 days as zero opens, one or two opens, or many opens.
3. On zero opens, resend with a new subject line, because the subject failed.
4. On one or two opens with no reply, wait 4-5 days and send the polite reminder.
5. On many opens, treat it as internal forwarding and wait a few days before a single low-pressure nudge.
6. Record the open count in the tracker column so the next person can see the same signal.

**Tools:** Mixmax

**Pitfall:** Treating all non-replies identically. Chasing a thread that is being actively discussed internally can push the group to a fast no; waiting a few days lets the internal conversation finish.

**Apply at Pabau:** Set up per-open tracking on the mailbox Pabau uses for expert and partner outreach, and add an open-count column to the outreach sheet so follow-ups are timed off the signal rather than a fixed calendar rule.

**Apply anywhere:** Use per-open tracking and branch your follow-up on the count: zero opens means fix the subject line, many opens means the pitch is circulating internally and needs patience, not pressure.

### 11. Reconcile Facebook click counts against landing page visits before reporting  `155.10`
*useful · content insights · source 155*

Grow and Convert flag a gap that would break most campaign reports. LeadPages recorded 11,850 unique visitors while Facebook reported 8,395 clicks for the same period. They note it is in Facebook's financial interest to count every click since it charges by them, so under-counting is unlikely to be the cause. Their best explanation is the 219 or so shares of the promoted post. Once a post is shared it sits on the sharer's own timeline, and clicks from that sharer's friends are not charged to the advertiser. She paid for the click that produced the share and got the downstream clicks free. Practically, this means the landing page tool, not the ad platform, holds the real visitor count when a campaign earns shares.

> "further clicks on it aren't charged to Erika"

**Evidence:** LeadPages: 11,850 unique visitors. Facebook: 8,395 clicks. Roughly 3,455 unattributed visits, attributed to 219 post shares.

**Tools:** LeadPages, Facebook Ads

**Pitfall:** Calculating cost per visitor from ad-platform clicks alone understates reach when a post earns shares, and calculating opt-in rate from platform clicks overstates it.

**Apply at Pabau:** Pabau should compute paid campaign cost per visitor from the landing page analytics rather than the ad platform, and note share-driven organic spill as a separate line in the channel report.

**Apply anywhere:** Take the visitor count from your landing page analytics rather than the ad platform, since shared posts send free clicks the platform never records.

### 12. Record both first and last click conversions every month  `150.10`
*useful · concrete actions · source 150*

Grow and Convert's client ROI sheets do not record a single conversion number per month. They record first click and last click conversions side by side, pulled from the Model Comparison Tool, next to the breakeven goal. The reason follows from their argument about multi-session paths: last click shows what closed the deal in that session, first click shows which blog post introduced the customer to the company, and for content the first click figure is usually the honest one. Keeping both in the sheet stops the monthly conversation from turning into an argument about attribution models, because both readings are already on the table. It also gives an early signal, since first click conversions move before last click when a new bottom-of-funnel page starts ranking.

> "record monthly first and last click conversions"

**Evidence:** Grow and Convert record both first and last click conversions monthly in the ROI sheets they build for agency clients.

**How to do it**

1. In the Model Comparison Tool select first interaction and last interaction as the two models compared.
2. Filter to blog URLs only, so brand and direct traffic do not contaminate the figure.
3. Export both conversion counts for the month into the ROI sheet as two separate columns.
4. Never blend or average the two into one number.
5. Plot both as separate series on the conversions chart against the breakeven line.
6. When the gap between them is wide, say so in one line: content is introducing more customers than it closes in-session.
7. Watch first click for early movement when a new page starts ranking, since it moves before last click.

**Tools:** Google Analytics

**Pitfall:** Reporting only last click understates content on any product with a multi-week buying cycle; reporting only first click invites the charge that you are taking credit for the whole funnel. Showing one number alone is what starts the attribution argument.

**Apply at Pabau:** Pabau's monthly content report should show first-click and last-click demo conversions for blog URLs as two columns, since practice owners research over weeks and last-click alone will make /blog/ look weaker than it is.

**Apply anywhere:** Record first click and last click conversions as two separate columns every month, filtered to blog URLs, and plot both. Showing one number alone turns every review into an argument about attribution.

### 13. Recover Facebook-sourced leads hiding in direct or none traffic via fbclid  `141.8`
*useful · concrete actions · source 141*

On the concussion treatment center, Grow and Convert found leads whose traffic source recorded as direct or none on several URLs. They could still attribute those leads to Facebook because the fbclid parameter was appended to the landing URL. This matters for any program where paid social carries the early months: without the check, the channel that actually produced the lead shows up as unattributed direct traffic, and the paid track looks like it underperformed. The fix is to read the full landing URL on each converting session rather than trusting the reported source, and to look for the click identifier the platform appends. The same logic applies to gclid for Google Ads. Grow and Convert use this alongside their three-model conversion measurement rather than instead of it.

> "those leads originated from Facebook due to the FBclid"

**Evidence:** Grow and Convert identified leads on several concussion-center URLs that reported as direct/none but carried fbclid, confirming Facebook as the origin.

**How to do it**

1. Pull the list of converting sessions with source recorded as direct or none.
2. For each, open the full landing page URL including query string rather than the cleaned page path.
3. Search the query string for fbclid, and for gclid if you also run Google Ads.
4. Reassign any conversion carrying fbclid to Facebook in your own reporting spreadsheet.
5. Repeat the check monthly during any period when paid social is a live channel.
6. If the direct/none bucket stays large after the reassignment, audit for stripped UTM parameters and missing cross-domain tracking.
7. State the reassigned figure separately in the report so the adjustment is visible to the client.

**Tools:** Google Analytics, Facebook Ads Manager

**Pitfall:** Reporting the raw direct/none bucket as unattributed hands the paid social track a loss it did not earn, and can get a working channel cut.

**Apply at Pabau:** If Pabau runs paid social to blog or template pages, David should check converting sessions for fbclid before concluding that direct traffic drove the demo requests, otherwise the paid track will look worse than it is.

**Apply anywhere:** Before writing off direct or none conversions as unattributed, open the full landing URL of each converting session and look for fbclid or gclid in the query string. Reassign any that carry one, and report the adjustment separately.

### 14. Reject a blended AI visibility score the way you reject a blended rank  `85.7`
*useful · general insights · source 85*

Grow and Convert offer a test that kills the argument for a single visibility percentage quickly. If a brand ranked number one for one keyword and number sixty for another, nobody in SEO would average the two and report a blended rank, because the average describes no real situation and implies no action. That is exactly what a brand-level AI visibility percentage does. They note the reason it persists is not that anyone defended it: the popular AI search visibility tools default to showing a single overall brand visibility percentage on the dashboard, so it becomes the number that gets reported. The lesson generalizes. When a tool's default view sets your reporting, audit the default before you build the deck around it.

> "what use would it be to average the two and report on a blended rank"

**Evidence:** Grow and Convert note popular AI visibility tools default to a single overall brand percentage, which is why the practice spread.

**Tools:** Peec, Profound

**Pitfall:** The default dashboard number is also the one leadership will have seen if they log in themselves, so replacing it without explaining why reads as hiding a bad result. Show both once, then retire the blended figure.

**Apply at Pabau:** Before Pabau standardizes on any AI visibility tool's headline number, check what the default chart is averaging and whether Pabau chose that denominator or just inherited it.

**Apply anywhere:** Before you standardize on any AI visibility tool's headline number, check what its default chart averages and whether you chose that denominator or simply inherited it.

### 15. Reject brand awareness and social shares as content distribution KPIs  `128.17`
*useful · best practices · source 128*

Devesh's origin story for the whole strategy is a buying experience. Running marketing in-house at a startup, he interviewed content marketing agencies, all of whom said they did content promotion. When he asked what the strategy actually was, the answer was creating social media updates to tweet from the company Twitter or post on the company LinkedIn page. They measured success on brand awareness and social shares, and would not hold themselves accountable to any real KPIs like traffic or leads. He says that never sat well with him because he did not think it would produce results. The rule he built from it is that a distribution strategy has to name the channel, the mechanism and a traffic or lead number it will be judged on, and posting to your own owned accounts is publishing, not distribution.

> "wouldn't hold themselves accountable to any real KPIs"

**Evidence:** Devesh's experience interviewing agencies in-house: all claimed content promotion, all described posting to owned social accounts, none accepted traffic or lead KPIs.

**How to do it**

1. Ask any vendor or internal owner to state the distribution mechanism per article, not the list of platforms.
2. Reject posting to your own social accounts as a distribution plan, since it reaches an audience you already have.
3. Require one primary KPI per channel expressed as traffic or leads, with a target number and a date.
4. Set the secondary metric as cost per landing page view or cost per lead, so scale is comparable across channels.
5. Drop brand awareness and social shares from the reporting template entirely.
6. Report per-article results so a failing channel cannot hide inside a blended total.
7. Review each channel against its stated number quarterly and cut the ones that miss twice.

**Pitfall:** Accepting share counts and impressions as evidence. They rise with volume regardless of whether anyone reached the article, so the channel can look healthy while contributing no traffic and no leads.

**Apply at Pabau:** Pabau content reporting should carry traffic and lead numbers per article and per channel, and any promotion plan that amounts to posting on Pabau's own social accounts should not count as distribution.

**Apply anywhere:** Require every distribution channel to carry a traffic or lead KPI with a number and a date, plus a cost per landing page view. Drop brand awareness and social share counts from reporting, and do not count posting to your own social accounts as distribution.

### 16. Report first-click and last-click, and call first-click a floor  `136.13`
*useful · best practices · source 136*

Grow and Convert attributed Leadfeeder signups to blog posts using both first-click and last-click attribution, and reported the pair rather than picking one. They add a caveat worth copying: even first click attribution is a lower limit estimate, meaning the true number of leads from content is likely higher. The reason is that a lot of content-influenced conversions never leave a click trail, because the reader returns via a branded search, a bookmark or another device. The practical effect on decisions is that content programs are systematically undercredited, and stating the floor explicitly protects the budget without overclaiming. They also note their attributed number, 215-225 signups a month, made up around 12% of Leadfeeder's total signup volume, so the claim was always framed against the whole.

> "even first click attribution is a lower limit estimate"

**Evidence:** Grow and Convert reported 215-225+ monthly signups attributed to Leadfeeder blog posts, about 12% of total signups, and stated that first-click understates the true figure.

**How to do it**

1. Set up goal reporting for both first-click and last-click attribution against your signup or lead event.
2. Report both numbers side by side for each article every month, never a single blended figure.
3. Label the first-click number explicitly as a lower bound in every report.
4. State the attributed total as a percentage of company-wide signups so nobody reads it as the whole picture.
5. Add a 'how did you hear about us' field at signup to catch conversions with no click trail.
6. When a stakeholder disputes the numbers, show the gap between the two models rather than defending one.
7. Re-baseline the report whenever the tracking or the funnel changes, and note it in the report.

**Tools:** Google Analytics

**Pitfall:** Reporting one attribution model makes the content program look either implausibly large or trivially small, and either reading invites the wrong budget decision. The missing piece is always the untracked return visit.

**Apply at Pabau:** Pabau's content reporting should show demo bookings under both first and last touch per article, state the first-touch figure as a floor, and add a 'how did you hear about us' question to the demo form to catch what neither model sees.

**Apply anywhere:** Report content conversions under both first-click and last-click attribution, describe the first-click figure as a lower bound, and express the total as a share of company-wide conversions. Add a self-reported attribution question at signup to catch untracked return visits.

### 17. Require a multi-week decline before you call a page decayed  `119.12`
*useful · best practices · source 119*

Grow and Convert set an explicit patience threshold on the decay trigger. A drop in one week is not a signal. They only treat a page as needing an update when rankings or traffic decline over the course of many weeks or months. The reasoning is that weekly rank noise is normal, especially for pages Google is still testing or repositioning, and reacting to it produces a queue of updates that were never needed. They pair this with the opposite rule for pages that are fine: if content is performing, there is no obligation to update it because time has passed. The combined effect is a much shorter update queue than a calendar-driven program produces, and every item on it has a documented multi-week trend behind it.

> "not just in one week, but over the course of many weeks"

**Evidence:** Grow and Convert's stated rule that a decline must run across many weeks or months, not one week, before it counts as an update trigger.

**How to do it**

1. Set your rank tracker or GSC export to a weekly cadence and store each week's average position per page.
2. Ignore any single-week move, up or down, no matter how large.
3. Flag a page only when the trend is downward across at least four consecutive weekly readings, or when a 90-day window sits clearly below the prior one.
4. Confirm the decline in both rankings and clicks before adding the page to the queue, so you are not chasing an impressions-only artifact.
5. Record the start date of the decline on the queue item, so you can measure recovery against it later.
6. Leave every page not on that list alone, including pages you personally dislike.
7. Re-scan the full tracked set on the same weekly cadence rather than doing an occasional big audit.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Reacting to one bad week. You rewrite a page that was mid-fluctuation, the rank recovers on its own, and you credit the update, which then locks in a wasteful refresh habit.

**Apply at Pabau:** Pabau's refresh queue should carry a required field for the decline window. No article enters the /SEO refresh flow on a single week's dip, and a page holding steady stays untouched even if it is old.

**Apply anywhere:** Add a required decline-window field to your refresh queue. No page enters it on a single week's dip, and pages holding steady stay untouched however old they are.

### 18. Rerun the same attribution report across acquisition channels  `151.6`
*useful · concrete actions · source 151*

Grow and Convert note that the model comparison tool is not limited to landing pages. The same first, last and linear comparison can be run against other primary dimensions, and they name acquisition channels specifically. That lets you see how many conversions are attributable to social, direct, organic and paid depending on which model you count under. The value is that channels suffer the same distortion as pages: a channel that introduces people to the brand but never closes them looks worthless under last click and substantial under first click. Running the comparison at channel level gives you the budget argument, and running it at landing page level gives you the editorial argument, from one report.

> "like acquisition channels"

**Evidence:** Grow and Convert state the same analysis can be run across dimensions such as acquisition channels to compare social, direct, organic and paid under different models.

**How to do it**

1. Run the attribution report once with Landing Page URL as the primary dimension for editorial decisions.
2. Change the primary dimension to the default channel grouping and rerun the same goal and lookback window.
3. Record first, last and linear conversions per channel in a single table.
4. Flag any channel whose first-click count is more than double its last-click count as an introduction channel.
5. Flag any channel whose last-click count exceeds its first-click count as a closing channel, not a discovery one.
6. Present budget arguments for introduction channels using the first-click figure and label it as a floor.
7. Repeat both cuts monthly at the same 90 day lookback so the series stays comparable.

**Tools:** Google Analytics

**Pitfall:** Reporting channels only on last click makes organic content and social look like they generate nothing, and budget then moves to whatever channel sits closest to the form.

**Apply at Pabau:** When Pabau reviews channel spend, David should show organic content under first click as well as last click, because a first demo request usually follows several earlier visits.

**Apply anywhere:** Run your attribution comparison at channel level as well as page level, so discovery channels are not defunded on last-click numbers.

### 19. Run free rank monitoring in a Search Console spreadsheet when tools are out of budget  `119.3`
*useful · concrete actions · source 119*

Grow and Convert give a no-cost fallback for teams that cannot buy rank tracking software yet. Google Search Console lists your ranking pages, the keywords they rank for and the average position. You copy those keywords and their page URLs into a spreadsheet and refresh it roughly weekly, watching for average position to move. They are honest that this is worse than a dedicated tracker and more time-consuming, but say it works for smaller teams or for anyone not ready to pay for SEO software. The constraint is keyword volume: it only holds up while the tracked set is small. They also warn that Search Console average position is what you are watching, so a single week's change is not a decision.

> "average position. You can add all of the keywords to a spreadsheet"

**Evidence:** Grow and Convert recommend this specifically for smaller teams or teams that do not want to pay for SEO software yet.

**How to do it**

1. Open the Search Console Performance report and filter to the pages you care about ranking.
2. Export queries with their pages and average position for the last 28 days.
3. Paste the keyword, the URL and the average position into a tracking spreadsheet, one row per keyword.
4. Add a new dated column each week and paste the fresh average position beside the old one.
5. Add a formula flagging any keyword that has lost position in three consecutive weekly readings.
6. Cross-check any flagged keyword against impressions before acting, so you do not chase a sampling artifact.
7. Move to a paid rank tracker once the sheet passes the point where weekly updating is a chore.

**Tools:** Google Search Console, Ahrefs

**Pitfall:** Scaling the sheet past a couple of hundred keywords. Updating it weekly stops happening, the data goes stale, and the whole monitoring layer silently dies.

**Apply at Pabau:** Pabau already has Search Console access, so David can stand up this sheet for the money keywords behind the template and code-reference pages before committing to more tooling.

**Apply anywhere:** If you cannot fund a rank tracker, build a weekly Search Console spreadsheet of keyword, URL and average position, and flag keywords losing ground across three readings.

### 20. Run the simple goal for months before upgrading the attribution model  `154.10`
*useful · best practices · source 154*

Grow and Convert give an explicit sequence rather than a choice. Start with the thank you page goal, run it for a few months, build the organizational habit of pulling the data and referring to it when making strategic decisions, and only then move to fancier attribution. Their phrasing is that you should not try to build a spaceship when the bicycle has not been invented yet. The habit is the deliverable in that first phase, not the accuracy. They concede that an organization already fluent with this data may be right to move to a more sophisticated model for assigning leads across channels, but they put that at under 10% of the companies they meet. So the upgrade trigger is behavioural: people are quoting the numbers unprompted and asking a question the simple report cannot answer.

> "don't try to build a spaceship when the bicycle hasn't been invented yet"

**Evidence:** Grow and Convert put the share of companies ready for sophisticated attribution at under 10%, and prescribe a few months of the simple method first.

**How to do it**

1. Ship the thank you page goal and nothing else in week one.
2. Put a recurring monthly slot in the calendar to pull channels, Landing Pages and Source/Medium with the goal applied.
3. Present the same three views every month, unchanged, for at least three months.
4. Log each decision that the data changed, such as pausing a campaign or refreshing a post.
5. Watch for the upgrade trigger: someone asks a question last touch cannot answer, such as which article first introduced a customer.
6. Only then add multi-touch or model comparison, and keep the simple views running alongside it.
7. If the monthly slot gets skipped twice, simplify the report further rather than adding to it.

**Tools:** Google Analytics

**Pitfall:** Upgrading the model while the habit is still fragile means the whole exercise stalls, because the new setup takes longer to produce and nobody has yet learned to ask for the number.

**Apply at Pabau:** David should treat a monthly Pabau content conversion review as the deliverable for the first quarter, not a better attribution model. The model upgrade waits until someone asks a question the last-touch view cannot answer.

**Apply anywhere:** Treat a monthly content conversion review as the deliverable for the first quarter, not a better attribution model. The upgrade waits until someone asks a question the last-touch view cannot answer.

### 21. Run the three-layer content reporting stack: conversions, ranks, traffic  `115.7`
*useful · concrete actions · source 115*

Grow and Convert name the exact tools behind their client reporting, one per layer. Conversions are tracked and reported using the Model Comparison Tool in Google Analytics, which lets them see how content performs under different attribution models rather than last click only. Keyword rankings are monitored in the Ahrefs rank tracker, one target keyword per article, so each piece is judged against the single term it was commissioned for; they note Semrush or Google Search Console would also work. Overall pageviews and organic traffic sit in Google Data Studio dashboards covering the articles. The structure matters more than the specific vendors: one tool per layer, and the layers ordered so conversions are the headline and traffic is the context.

> "We use Ahrefs rank tracker to monitor rankings progress"

**Evidence:** Grow and Convert's client reporting stack: Model Comparison Tool in Google Analytics for conversions, Ahrefs rank tracker per article target keyword, Google Data Studio dashboards for pageviews and organic traffic.

**How to do it**

1. Set your lead conversion as a goal in Google Analytics and review it through the Model Comparison Tool, not last-click alone.
2. Add every published article's single target keyword to the Ahrefs rank tracker at publication time.
3. Keep one tracked keyword per article so no piece can hide behind a variant it happens to rank for.
4. Build a Google Data Studio dashboard segmented to the article URLs, showing pageviews and organic sessions.
5. Order the monthly report conversions first, rankings second, traffic third.
6. Review each article's tracked keyword at 30, 60 and 90 days after publication before judging it.
7. Flag any article whose keyword sits outside the top ten at 90 days for a SERP re-analysis.
8. Substitute Semrush or Search Console for the rank layer if you do not run Ahrefs.

**Tools:** Google Analytics, Ahrefs, Google Data Studio, Semrush, Google Search Console

**Pitfall:** Tracking a basket of keywords per article instead of one. The article looks like it is ranking because some loosely related variant moved, and the term it was actually commissioned for never gets checked.

**Apply at Pabau:** David should add each Pabau article's single target keyword to a rank tracker at publish time and report it beside demo requests. A dashboard filtered to /blog/ and /templates/ URLs gives the traffic layer without mixing in product pages.

**Apply anywhere:** Run one tool per reporting layer: multi-model conversion tracking in your analytics platform, a rank tracker holding exactly one target keyword per article, and a dashboard filtered to the article URLs for traffic. Report them in that order, conversions first.

### 22. Run three separate reporting layers: conversions, per-article rank, traffic  `121.11`
*useful · concrete actions · source 121*

Grow and Convert name the exact stack they use to report on a SaaS engagement, and they keep the three layers separate rather than merging them into one dashboard. Conversions are tracked and reported using the Model Comparison Tool in Google Analytics. Keyword rankings are monitored in Ahrefs rank tracker, and per article against that article's own target keyword rather than as a site-wide keyword pool. Overall pageviews and organic traffic sit in a Looker Studio dashboard. Their point is that most SEO teams do the second and third layers, which are easy, and skip the first. Skipping it means conceding your strategy is traffic-focused and being unaware of whether it contributes revenue at all. Note that Google Analytics 4 moved model comparison under attribution reporting.

> "using the Model Comparison Tool in Google Analytics"

**Evidence:** Grow and Convert's own agency reporting stack across their SaaS client base.

**How to do it**

1. Set up conversion events for the actions that matter: demo request, trial start, sales form fill.
2. Open the attribution model comparison report in Google Analytics and filter it to your article URLs.
3. Compare first-click and last-click credit per article so assisted conversions are not lost.
4. In Ahrefs rank tracker, create one tracked keyword per published article, tagged with that article's URL.
5. Never judge an article against a keyword it was not written for; the one-keyword-per-page rule applies to reporting too.
6. Build a Looker Studio dashboard for pageviews and organic sessions by article.
7. Lead every monthly report with the conversions layer and put traffic last.
8. Review any article ranking top five with zero conversions, since the keyword choice rather than the page is usually wrong.

**Tools:** Google Analytics, Ahrefs, Looker Studio

**Pitfall:** Tracking rankings for a bag of keywords at site level. Average position improves while the specific query each page was built for is stuck on page two, and nobody notices.

**Apply at Pabau:** Pabau should track one target keyword per blog and template page in the rank tracker, tied to the URL, and lead reporting with demo requests attributed through the attribution comparison report.

**Apply anywhere:** Keep three reporting layers separate: conversions through attribution model comparison, one tracked keyword per article, and a traffic dashboard. Lead with conversions.

### 23. Save the model comparison report by copying its share link  `149.10`
*useful · concrete actions · source 149*

The GA4 model comparison tool has no Save button, unlike the Universal Analytics version. Grow and Convert's workaround is to click Share this report once the table is configured, copy the link, and store it. Opening that link later reproduces the report configuration without rebuilding the source, medium, landing page and attribution model choices by hand. They contrast this with the Explore exploration report, which does save automatically when you exit back to the Exploration reports page. Practically, that means the model comparison view is only as durable as wherever you stored the link, so it belongs in the reporting document rather than in a browser tab.

> "you can click the Share this report button"

**Evidence:** Grow and Convert note the GA4 model comparison tool has no Save option like the Universal Analytics version, while the Explore report saves on exit.

**How to do it**

1. Finish configuring the model comparison table before sharing, since the link captures the current state.
2. Click Share this report and copy the share link.
3. Paste the link into the client or internal reporting document with a one-line label of what it shows.
4. Include the attribution model and the conversion events selected in that label.
5. Re-open the link at the start of each reporting cycle and adjust only the date range.
6. Rebuild and re-share the link whenever you change the URL filter, since the old link no longer matches.
7. Use Explore for anything you want GA4 itself to persist, because explorations save automatically.

**Tools:** Google Analytics 4

**Pitfall:** Rebuilding the report by hand every month invites configuration drift, where one month uses first click and the next uses last click and nobody notices the comparison is invalid.

**Apply at Pabau:** Pabau's monthly SEO report should carry the stored share links for each GA4 view, so the same configuration is read every month rather than rebuilt from memory.

**Apply anywhere:** Store the share link for each configured model comparison view in the reporting document so the same configuration is read every month.

### 24. Search Console data outgrows its API before an agent can use it  `56.3`
*useful · ai workflows · source 56*

Cody runs this whole refresh loop through Claude Code with Search Console data connected, and he is specific about where the naive version breaks. Hitting the Search Console API directly works only while your data volume is small; past that you hit rate limits, pagination issues that silently truncate results, and finally the model's context window limit. At that point you have to build a data pipeline and warehouse and give the agent access to that instead. The open-source version he names is Airbyte for ingestion into a ClickHouse warehouse, both runnable on a host like Railway, with Claude Code able to set the whole thing up for you. The failure mode he flags is duplication errors when Airbyte writes to ClickHouse, and it gets worse with multiple data sources.

> "you'll hit rate limits, like you'll hit pagination issues"

**How to do it**

1. Start by hitting the Search Console API directly from your agent - for a small site this is enough and needs no infrastructure.
2. Watch for the three specific failure signals: API rate limiting, result sets that look suspiciously round or short (pagination truncation), and the agent running out of context.
3. When you hit them, stand up an ingestion tool (he names Airbyte, open source) to pull Search Console into a warehouse rather than querying the API live.
4. Use an analytical warehouse that handles wide query loads - he uses ClickHouse, also open source.
5. Host both on something with a simple deploy story (he uses Railway) and let Claude Code do the setup wiring.
6. Watch specifically for duplication errors on the Airbyte-to-ClickHouse write path, which is where he sees breakage.
7. Only then point the agent at the warehouse, so it queries with SQL instead of trying to hold the dataset in context.

**Tools:** Google Search Console, Claude Code, Airbyte, ClickHouse, Railway

**Pitfall:** Silent truncation is the dangerous one - pagination limits return a partial query set that looks complete, so the agent confidently optimizes against a fraction of your actual data.

**Apply:** Before wiring any Pabau reporting agent to Search Console, decide whether the query volume fits the API - if reports come back suspiciously small or the agent's answers drift between runs, assume truncation rather than a model problem.

### 25. Segment the site before comparing organic conversion rate to paid  `143.6`
*useful · best practices · source 143*

Grow and Convert say clients repeatedly report that their organic conversion rate feels low, and the cause is usually the comparison rather than the performance. Companies see roughly 3% from Google Ads and 0.1% to 0.3% site-wide from organic search, then conclude organic is broken. Grow and Convert's answer is that the site-wide organic figure is a blend: it mixes different parts of the site and different traffic mediums, which skews the number in both directions. Paid traffic lands on a purpose-built landing page from a bid on a commercial term, so the two numbers are not measuring the same thing. Before drawing any conclusion, split organic into blog versus product and landing pages, and split the blog into buying-intent and informational posts.

> "using paid conversion rates as a benchmark"

**Evidence:** Grow and Convert cite the common client pattern of about 3% from Google Ads against 0.1%-0.3% site-wide organic, and say the organic figure is unsegmented.

**How to do it**

1. Build a GA4 exploration segmented by landing page group: blog, product pages, landing pages, docs.
2. Add a second split inside the blog between buying-intent posts and informational posts.
3. Report conversion rate for each segment separately and never quote the site-wide organic figure alone.
4. Compare paid only against the equivalent organic segment, meaning buying-intent pages, not the blog average.
5. Exclude branded organic traffic from the comparison, since it converts like direct rather than like a paid click.
6. Restate the benchmark to stakeholders as 1-5% per bottom-funnel page rather than a single site number.
7. Re-run the segmentation each quarter so a growing informational archive does not silently drag the average down.

**Tools:** Google Analytics 4, Google Ads

**Pitfall:** An unsegmented organic conversion rate falls every time you publish informational content, so a healthy content program can look like it is failing while its commercial pages improve.

**Apply at Pabau:** Before David reports Pabau's organic conversion rate, he should split it by page type and by blog intent bucket. Comparing the whole blog against a paid landing page will always make organic look weak.

**Apply anywhere:** Never compare a site-wide organic conversion rate to paid. Segment by page type and by blog intent bucket first, then compare paid only against the equivalent buying-intent organic pages.
