# Conversion & Monetization — supporting (part 5 of 5)

19 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Strip graphical sidebar and in-content CTA blocks from blog posts  `144.3`
*useful · concrete actions · source 144*

Grow and Convert say they often see companies crowd blog pages with graphical CTAs in sidebars and through the body, and that these graphics are counterproductive in three specific ways. They hurt readability, which makes it less likely readers finish the post. They distract readers from learning how the product solves their problem. And they look like ads, which readers are trained to ignore. Their recommendation is to optimize blog design for readability instead: fewer graphical CTAs and email opt-in boxes, a more minimalist layout, clear text that keeps attention on the content. They tie the recommendation directly to the writing advice, arguing that if the body copy already sells the product then ad-looking CTA graphics are not needed in the first place.

> "crowd their blog pages with graphical CTAs"

**Evidence:** Grow and Convert name three mechanisms from client work: reduced readability and post completion, attention pulled from the product argument, and banner blindness because the blocks read as ads.

**How to do it**

1. Open a representative bottom-funnel post and list every graphical element that is not part of the argument: sidebar banners, in-content promo boxes, email opt-in blocks, floating widgets.
2. Remove the sidebar CTA graphics first, since they take attention without appearing in the reading flow.
3. Remove or consolidate mid-article promo boxes down to one, placed where the argument naturally reaches a decision point.
4. Replace what you removed with plain-text contextual CTAs written into the copy.
5. Keep the navigation bar CTA button, which is unobtrusive and always reachable.
6. Check the post on mobile, where stacked graphical blocks interrupt the reading column worst.
7. Compare scroll depth and conversion for the cleaned post against a control post over a few weeks before rolling the change out site-wide.

**Pitfall:** Stripping graphics without strengthening the copy. The graphics were a substitute for a product argument, so removing them from a post that never sells the product just leaves a post with no conversion path at all.

**Apply at Pabau:** Pabau blog templates should keep the book-demo block and the download box, which are part of the contract, but David should resist adding further promo graphics or newsletter boxes into article bodies. The reading column on a comparison article is where the Pabau argument gets made.

**Apply anywhere:** Keep one deliberate in-content CTA block and resist adding further promo graphics or newsletter boxes into article bodies. The uninterrupted reading column is where the product argument gets made.

### 2. Structure the content partnership so it can't be taken back  `57.3`
*useful · concrete actions · source 57*

Jackie's contract terms are deliberately aggressive because he has been burned: he takes 50% of everything generated, owns the IP to the content created, and the subdirectory is effectively a 50/50 split. His reasoning is behavioural - at 15k a month the client doesn't care that they're paying you 7k, but at 200k a month they start looking at the line item and asking how to cut you loose. So he builds in barriers that make replacement expensive: a custom Amazon rate card means that if the client switched to their own Amazon account, their revenue would divide by four overnight. He is clear this has to be communicated very upfront, and calls it a hard balancing act. Cody's read is that you have to treat these partners as clients throughout, precisely because success creates the incentive to remove you.

> "our contract states that we just take 50%"

**How to do it**

1. Agree the revenue split before any work, and be explicit that it applies to everything generated.
2. Retain the IP to the content you create rather than transferring it on payment.
3. Define the boundary of what you control (in his case the subdirectory) in the contract, not informally.
4. Identify the thing you have that they can't replicate - a rate card, a relationship, an integration - and make it structural to the arrangement.
5. Communicate that dependency at the start, not when they try to leave.
6. Assume the relationship gets harder as it gets more successful, and service them like clients throughout.

**Pitfall:** He notes the same barrier that protects the deal also makes the client feel trapped, which is why he stresses communicating it upfront - discovering it during an exit attempt turns a partnership into a dispute.

**Apply at Pabau:** Relevant to Pabau mainly for partnerships and affiliate arrangements: whoever owns the content IP and the commercial rate card is who holds the relationship, and both should be settled in writing before the traffic exists.

**Apply anywhere:** Relevant mainly to partnerships and affiliate arrangements: whoever owns the content IP and the commercial rate card is who holds the relationship, and both should be settled in writing before the traffic exists.

### 3. Swap standard exit popups for full-page ones to roughly double opt-ins  `148.5`
*useful · concrete actions · source 148*

Shour ran standard exit popup templates for content upgrades and they converted at around 2.6%. After switching to a full-page exit popup, the same offers converted at 5.58%, which he describes as nearly 115% better. He is explicit that this is his own preference and recommends anyone still on the standard template test the full-page version rather than assume the result transfers. The full-page unit he uses is a green interstitial that takes the whole viewport on exit intent. Nothing else about the offer changed, so the lift is attributed to the format alone. He closes the article with the same caution applied to every tactic here: use these as a starting point and test your own messages, because what works for SnackNation may not work for you.

> "Those popup templates converted at around 2.6%"

**Evidence:** Standard exit popups converted at about 2.6%; full-page exit popups converted at 5.58%, roughly 115% better, at SnackNation.

**How to do it**

1. Record the current opt-in rate of your standard exit popup over at least two weeks.
2. Build a full-page exit-intent variant in OptinMonster with the same headline and offer.
3. Change only the format, keeping copy, fields and asset identical so the test is clean.
4. Split traffic between the two variants rather than switching everything at once.
5. Run until each variant has enough conversions to separate 2.6% from 5.58%.
6. Check bounce and time-on-page alongside opt-in rate to catch an annoyance cost.
7. Roll the winner out across the posts carrying the same offer.
8. Re-test on mobile separately, where full-page interstitials carry a search penalty risk.

**Tools:** OptinMonster

**Pitfall:** Full-page interstitials on mobile risk Google's intrusive interstitial treatment, which the knowledge base elsewhere warns can derank a site. Test desktop and mobile separately rather than rolling out one setting.

**Apply at Pabau:** Pabau should not run full-page interstitials on mobile blog pages given the deranking risk. If David tests this, restrict it to desktop and to template pages where the download is the point of the visit.

**Apply anywhere:** Test a full-page exit-intent popup against your standard template, changing only the format. Expect a large lift on desktop, but keep mobile on the smaller unit to avoid intrusive interstitial penalties.

### 4. Switch off automated ad assets that Google adds for you  `156.9`
*useful · concrete actions · source 156*

Grow and Convert accept that extensions, now called assets, help ads stand out and give users relevant extra information when done deliberately. What they object to is Google automating them. Google pulls information from your website and from around the web to add assets such as sitelinks it believes match the query, and even location data. They quote Google's own warning that Google Ads may automatically match your business to known locations based on account properties such as landing pages and add that information to create these assets. The risk is concrete: an ad can promote a service you do not sell or a location you do not serve, and you pay for the clicks. The setting can be turned off in account settings.

> "This feature can be turned off in your account settings"

**Evidence:** Grow and Convert quote Google's stated behavior of matching a business to known locations based on account properties such as landing pages.

**How to do it**

1. Open Google Ads account settings and find the automated assets or automatically created assets controls.
2. Review the list of assets Google has generated on your behalf.
3. Turn off automated location assets if you do not serve every location Google has matched you to.
4. Turn off automatically created sitelinks and dynamic assets that point at pages you did not choose.
5. Replace them with manually written sitelinks, callouts and structured snippets per campaign.
6. Point each manual sitelink at a page that matches the campaign's intent.
7. Recheck the automated assets list quarterly, because Google reintroduces new asset types over time.

**Tools:** Google Ads

**Pitfall:** Automated location assets can advertise you in cities you do not serve, generating clicks and calls you can never fulfil, and the spend hides inside asset-level reporting most teams never open.

**Apply at Pabau:** Pabau should disable automated location assets so ads do not imply local presence in regions it does not serve, and write manual sitelinks for booking, EMR and reporting pages instead.

**Apply anywhere:** Turn off automatically created assets, especially location assets, and write your own sitelinks and callouts pointing at pages that match each campaign's intent.

### 5. Test your own site's contact paths every month  `13.7`
*useful · best practices · source 13*

Irwin sets his own website as his browser's default homepage so he immediately notices if it goes down or gets hacked, and every month has someone (staff, or a scheduled AI agent or VA) actually fill in every form and click every phone number through to reception, rather than just checking that fields validate. The point is to catch silent failures analytics never surfaces: his real example is a phone number that displayed correctly but was wired to the wrong tel: link, so it looked fine but every click dialed an incorrect number, and clicks tracked fine while calls failed. He also recommends storing form submissions in the CMS backend (he uses WordPress) independent of email deliverability, so a missing email can be diagnosed as an IT issue rather than a website fault.

> "every month I get someone in my agency to fill in"

**How to do it**

1. In your browser settings, set the company website as the default homepage or new-tab page so downtime or defacement is visible immediately on open (inferred: Chrome Settings > On startup > Open a specific page).
2. Once a month, assign a team member or a scheduled AI agent/VA to submit every lead form on the site end-to-end using a real but disposable test contact.
3. In the same monthly check, click every clickable phone number on both desktop and mobile and let the call ring through to reception to confirm the tel: link dials the correct number.
4. Compare the visually displayed phone number character-by-character against the actual tel: href in the page source to catch mismatches (inferred: use browser Inspect Element on the phone link).
5. Confirm the CMS stores a backend copy of every form submission independent of the email notification, so a missing email can be diagnosed separately from a missing submission.
6. Repeat the test from a different device type each month (desktop, iOS, Android) since tel: and maps links can behave differently per platform.
7. Log any failure found and assign it to be fixed within the week, since these are typically one-line fixes with outsized conversion impact.

**Tools:** WordPress

**Pitfall:** Assuming a correct-looking phone number is a correctly working link — the visible number can be right while the coded tel: link dials a different number entirely, failing silently on every mobile click.

### 6. Trace the high-converting-landing-page belief back to paid search  `146.3`
*useful · content insights · source 146*

Grow and Convert locate the source of the belief precisely. The landing pages that convert in double digits are PPC landing pages: main navigation stripped out, few clickable options, information on the left and a demo or trial form on the right, all above the fold. They checked the SERP for 'data analytics software' and found four ad slots all pointing at that exact structure. The conversion rate comes mostly from the click, not the page. Someone who Googles a software term and then chooses to click an ad is self-selecting as ready to be sold. Organic clickers are further up the funnel and more in research mode, and organic pages take far more traffic, tens of thousands of visitors in their example, so a 10% rate was never available.

> "if you click an ad, you are self-selecting as someone who is ready to be sold"

**Evidence:** Grow and Convert observed four ad slots on 'data analytics software' all going to identical form-right landing pages, which they say can convert above 10%.

**Pitfall:** Importing a paid-landing-page conversion benchmark into an organic target. The team then judges an organic page a failure at 1%, when 1% may be the top of the range for that traffic.

**Apply at Pabau:** David should set separate conversion benchmarks for Pabau's paid landing pages and its organic pages, and never hold a /blog/ article or a template page to a paid-traffic rate.

**Apply anywhere:** Set separate conversion benchmarks for paid landing pages and organic pages, and never hold an organic article to a paid-traffic rate.

### 7. Track ad frequency against Perry Marshall's five fatigue bands  `155.4`
*useful · best practices · source 155*

Grow and Convert cite the frequency table from Perry Marshall's Ultimate Guide to Facebook Advertising as the standing check on ad fatigue. Frequency is the average number of times the same person has seen the ad. Zero to three is very low risk, three to six low, six to nine moderate, nine to twelve high, and twelve or more very high risk. At the time of writing Erika's ads sat at a frequency of 2.27 and had reached 96,000 of a 700,000 audience, which is 14%. That gave a clear read that the audience was nowhere near exhausted and the campaign could keep running. The article notes the practical symptom of fatigue too: CTR starts dipping while CPC starts rising.

> "Perry Marshall, in his book Ultimate Guide to Facebook Advertising"

**Evidence:** Erika's campaign at frequency 2.27, reaching 96,000 of a 700,000 audience, 14% penetration, after roughly two months.

**How to do it**

1. Add frequency as a column in the Facebook Ads reporting view for every live campaign.
2. Review it weekly against the bands: 0-3 very low, 3-6 low, 6-9 moderate, 9-12 high, 12+ very high risk.
3. Cross-check by plotting CTR and CPC over the same period; a falling CTR with rising CPC confirms fatigue.
4. Compare people reached against total audience size; Erika was at 96,000 of 700,000.
5. Leave a campaign untouched while frequency stays under three and reach is under a fifth of the audience.
6. Refresh the creative once frequency passes six, before CPC has moved.
7. Widen or swap the interest set once reach approaches the full audience.
8. Log the frequency at which each creative started to decay, so the next refresh is scheduled rather than reactive.

**Tools:** Facebook Ads

**Pitfall:** Waiting for CPC to rise before acting means paying the fatigue tax first. Frequency moves before cost does, which is why it is the leading indicator.

**Apply at Pabau:** If Pabau runs paid social to template or demo pages, report frequency alongside CPC in the monthly channel review and set a creative refresh trigger at frequency six.

**Apply anywhere:** Report ad frequency weekly and refresh creative once it passes six, rather than waiting for cost per click to climb.

### 8. Treat Smart campaigns as Dynamic Search Ads with less control  `156.10`
*useful · general insights · source 156*

Grow and Convert describe Smart campaigns as Google's option for businesses without time to run their own account. You write an ad describing the business, choose keyword themes, and set a budget, and the ad then shows across Google Search, Google Maps, YouTube, Gmail and Google partner websites. Google also states the ad can show to people outside the designated geographic area if their search includes both a related term and the business location. Their assessment is that this is Dynamic Search Ads with the problems multiplied: the ad appears in even more places than search, it can serve outside the target area, and you cannot control bids or maximum CPC. For anyone who cares about buying intent, that is three separate controls given away at once.

> "You also cannot control things like your bid or max CPC"

**Evidence:** Grow and Convert quote Google's own description of Smart campaigns serving across Search, Maps, YouTube, Gmail and partner sites, including to users outside the target area.

**How to do it**

1. Check whether any live campaign is of the Smart campaign type.
2. List which surfaces it can serve on: Search, Maps, YouTube, Gmail and partner sites.
3. Compare its cost per qualified lead against a manually structured search campaign over the same period.
4. If you need control of bids, geography or placement, rebuild it as a standard search campaign.
5. Keep Smart campaigns only where no one has time to manage an account at all, and cap the budget accordingly.

**Tools:** Google Ads

**Pitfall:** Smart campaigns can serve to searchers outside your service area whenever the query names your location, so geographic targeting is weaker than it appears in the settings.

**Apply at Pabau:** Pabau should not run Smart campaigns for practice management, because bid control and placement control matter more than setup speed at this spend level.

**Apply anywhere:** Treat Smart campaigns as Dynamic Search Ads with fewer controls, and rebuild them as standard search campaigns whenever you need control of bids, geography or placement.

### 9. Treat low login frequency as the churn signal that kills subscriptions  `170.5`
*useful · content insights · source 170*

Campbell is blunt about the category: 'Selling an analytics product is one of the worst businesses to be in. Churn is awful. People aren't willing to pay for it.' The mechanism he names is usage frequency. An accurate analytics product is expensive to build and maintain, and the customer logs in about once a month. Infrequent use means the customer never builds a habit, never feels the loss when they cancel, and churns. The lesson generalizes beyond analytics to any product or content asset that is genuinely useful but rarely opened: reporting dashboards, annual calculators, compliance checkers. The value is real, but it will not sustain a recurring price on its own.

> "Selling an analytics product is one of the worst businesses to be in"

**Evidence:** Campbell's own research on ProfitWell showed analytics customers log in roughly once a month and churn heavily, which is why it was never sold as a standard subscription.

**Pitfall:** Building an expensive, accurate product and assuming accuracy alone justifies a subscription. The signal you have hit it is high build cost, positive reviews, monthly-or-less login frequency and rising churn.

**Apply at Pabau:** Pabau features that practices touch once a month, like reporting, should not carry the pricing argument. Build the plan pages around daily-use workflows such as booking, notes and payments, and position reporting as the reason to stay rather than the reason to buy.

**Apply anywhere:** Check how often customers would actually open the thing you want to charge for. Anything used monthly or less rarely holds a subscription, however accurate it is; sell the daily-use workflow and let the occasional tool support retention.

### 10. Treat published conversion rates as a starting point, then test  `148.13`
*useful · general insights · source 148*

Shour closes by saying the tactics here are a starting point and that you should test different messages to find what converts best for your business, because something working for SnackNation does not mean it works for you, for better or worse. The numbers he publishes carry visible context that limits transfer: SnackNation ships a physical sample box within the US only, which is why only about 18% of its 884 leads qualified, and he says a digital product or service would probably see a better lead-to-sale rate. The structural claims, that scent, a bridge question and a risk-free offer belong on the page in that order, are more portable than the rates. Copy the structure, not the percentages.

> "test different messages to find what converts best"

**Evidence:** Shour's stated caveat that results may differ for better or worse, plus his note that a digital product or service would likely convert leads to sales better than his sample box.

**How to do it**

1. Copy the three-part page structure of scent, bridge question and risk-free offer as your first version.
2. Set your own baseline from your current confirmation page before changing anything.
3. Change one element at a time: bridge wording, offer framing, then proof placement.
4. Run each test until the difference is larger than your normal week-to-week variance.
5. Adjust the offer to your business model, since a digital trial removes the shipping constraint that limited SnackNation.
6. Record the qualified-lead rate alongside the conversion rate for every variant.
7. Write down what you expected before each test so you can tell a real result from a story.
8. Keep a log of tested messages so a future rebuild does not repeat a losing variant.

**Pitfall:** Importing another company's conversion rate as a target. SnackNation's 7.5-11% comes with a US-only physical product and an 18% qualification rate that will not match a software funnel.

**Apply at Pabau:** Pabau should not treat 7.5-11% as the target for a post-download demo offer. Set the baseline from Pabau's own current confirmation pages and test the bridge wording first.

**Apply anywhere:** Take the page structure from published case studies and set your own baseline for the numbers. Test the bridge wording first, and record qualified-lead rate next to conversion rate on every variant.

### 11. Turn off Google Search Partners on every search campaign  `157.5`
*useful · concrete actions · source 157*

Grow and Convert single out Search Partners as a default Google recommends when you create a campaign. It is a network of third-party sites where your ads can appear. They acknowledge the temptation: CPCs on Search Partners are often low, so the channel looks efficient in a cost report. In their experience and testing, Search Partners rarely if ever produces high-quality leads. Their explanation is that the intent of a visitor on a partner site is not the same as someone typing a query into Google, so the cheap click was never a buyer. The practical instruction is to uncheck the option at campaign setup and audit existing campaigns for it, since it is on by default and the cost data alone will make it look like your best-performing placement.

> "we've seen that Search Partners rarely"

**Evidence:** Grow and Convert's testing across SaaS client accounts found Search Partners rarely produced high-quality leads despite low CPCs.

**How to do it**

1. Open each search campaign's Settings and expand Networks.
2. Uncheck 'Include Google search partners' and save.
3. Uncheck the Display Network option in the same panel if it is enabled.
4. Segment historical performance by network to quantify what Search Partners actually delivered in leads, not clicks.
5. Check the setting again after any campaign copy or import, since duplicated campaigns carry the default back in.
6. Add the network check to a monthly account audit checklist.

**Tools:** Google Ads

**Pitfall:** Judging Search Partners by CPC or click volume. It usually looks like the cheapest traffic in the account while producing the worst leads, so only a lead-quality segment reveals it.

**Apply at Pabau:** If Pabau runs search campaigns, disable Search Partners and the Display Network at setup, and segment any existing campaign by network before reading its cost per lead.

**Apply anywhere:** Disable Search Partners and the Display Network on every search campaign, and segment existing campaigns by network before trusting their cost per lead.

### 12. Use a 7-field form — Neil Patel data shows minimal drop-off  `55.4`
*useful · concrete actions · source 55*

For the funnel's lead form, use exactly seven fields rather than a shorter form — citing data Neil Patel shared showing the conversion-rate difference between a 5-field and a 7-field form is only about 0.5%, meaning the extra fields cost almost nothing in volume while letting you filter out low-intent respondents and collect enough detail to segment leads into archetypes later. Pair the form with a sub-45-second video embedded at the top explaining what the form is, what to expect, and that a sales call follows, ending the form with a Calendly booking step (Calendly integrates directly with Typeform).

> "conversion between five form fields and seven form fields is only 0.5%"

**How to do it**

1. Build the lead form with exactly seven fields, covering enough detail to later segment respondents into customer archetypes.
2. Record a video under 45 seconds explaining what the form is for, what happens after submitting it, and that a sales call will follow.
3. Embed that video at the very top of the form.
4. Add a Calendly booking step at the end of the form (using the native Typeform-Calendly integration if the form is built in Typeform) so the prospect books the sales call immediately.
5. Set the call type to either video or audio-only, whichever fits your sales process.
6. Connect the form's submission event to Zapier so every response is logged automatically.

**Tools:** Typeform, Calendly, Zapier

**Pitfall:** More form fields generally reduce conversion, so don't assume adding fields is free — but per the cited Neil Patel data point, the drop from 5 to 7 fields is negligible (about 0.5%), so under-collecting information to "protect conversion" isn't worth it at this specific margin.

### 13. Use annual deal value for breakeven, not monthly or lifetime  `150.8`
*useful · best practices · source 150*

Grow and Convert address the choice of which deal value goes into the lead-value calculation. Monthly value is, in their opinion, an unreasonably short payback period for content, since content takes months to rank at all. Lifetime value is too long, because nobody wants to wait three to five years to start making money on a customer, and a breakeven date that far out cannot hold executive buy-in. They settle on the annual value of a closed deal, on the reasoning that for most B2B businesses one year is a generally accepted period in which to recoup customer acquisition cost. The choice matters because it moves the breakeven lead target by an order of magnitude in either direction, and picking LTV is the easy way to make a weak program look viable on paper.

> "an unreasonably short payback"

**Evidence:** Grow and Convert use annual value of a closed deal for clients because one year is generally considered a reasonable recoup period for B2B customer acquisition.

**How to do it**

1. Ask finance for three figures: average monthly revenue per customer, average first-year revenue, and LTV.
2. Use the first-year figure in the lead-value calculation by default.
3. Reject monthly value, which sets a payback window shorter than the time content takes to rank.
4. Reject LTV unless your executives have explicitly agreed to a three-to-five-year payback horizon.
5. State the chosen basis in one line on the ROI sheet so nobody silently swaps it later.
6. If someone proposes switching to LTV, show both breakeven targets side by side before agreeing.
7. Re-check the first-year figure annually, since churn and pricing changes move it.

**Pitfall:** Switching the basis to lifetime value quietly cuts the breakeven lead target and makes an underperforming program look on track. The signal is a breakeven number that fell without spend or pricing changing.

**Apply at Pabau:** Pabau's subscription model has a long lifetime value, which makes LTV a tempting and misleading basis. David should fix the ROI sheet on first-year subscription value and note the basis in the sheet header.

**Apply anywhere:** Base your lead-value calculation on the first-year value of a closed deal. Monthly value sets a payback window shorter than content takes to rank, and lifetime value pushes breakeven three to five years out, where nobody will hold the budget.

### 14. Use content upgrades when first and last click match  `151.8`
*useful · concrete actions · source 151*

When Grow and Convert compared five of their own posts for the goal of email list signup, the first and last click numbers were almost the same, with first click only slightly higher on some posts. Their reading is that the majority of email conversions happen in the same session as the landing, which makes sense because people decide to join a blog's list immediately rather than talk to their boss and come back. The direct instruction they draw is that if you are chasing opt-ins, set up conversion CTAs like content upgrades so people opt in on the spot, and do not count on anyone returning multiple times before opting in. The measurement decides the CTA design, not the other way round.

> "Don't count on anyone coming back multiple times before opting in."

**Evidence:** Across five Grow and Convert posts, first-click email opt-in conversions were only slightly higher than last-click, meaning most opt-ins happened in the landing session.

**How to do it**

1. Run the model comparison for your email signup goal across your top posts.
2. Confirm the first and last click counts are within roughly ten percent of each other before treating opt-ins as immediate.
3. Build a content upgrade specific to each high-traffic post rather than one site-wide newsletter box.
4. Place the upgrade CTA inside the post body where the reader has just got value, not only in the footer.
5. Skip long retargeting sequences aimed at pushing return visits for email capture specifically.
6. Recheck the two columns after the change to confirm last-click opt-ins rose.

**Tools:** Google Analytics

**Pitfall:** Spending retargeting budget to bring readers back for an email opt-in wastes money on a decision that people make in the first session or not at all.

**Apply at Pabau:** Pabau's template pages already offer a download, so David should treat that download as an immediate-decision CTA and place it in the body rather than relying on return visits.

**Apply anywhere:** Treat email and download opt-ins as same-session decisions: put a post-specific content upgrade inside the body instead of funding return visits.

### 15. Use inline text-link CTAs on articles, buttons on landing pages  `36.5`
*useful · concrete actions · source 36*

Banner blindness and sidebar-blindness are real: a simple text link placed mid-paragraph converts better than a flashy button on informational content because it does not register as an ad or interrupt reading. The page-type distinction matters: on an informational or blog-style page, embed the CTA as a natural inline text link within the body paragraphs written conversationally; on a bottom-of-funnel landing page, use a visually prominent button instead, and place it above the fold before the visitor has to scroll.

> "A simple text link mid paragraph converts better than any flashy button"

**How to do it**

1. Classify each page as informational/blog-style or bottom-of-funnel/landing-page style.
2. On informational pages, remove or de-emphasize sidebar and banner CTAs, since these are routinely ignored.
3. On informational pages, insert the CTA as a short, natural inline text link placed mid-paragraph within relevant body content, phrased conversationally rather than as an ad.
4. On bottom-of-funnel landing pages, use a visually distinct button-style CTA instead of an inline text link.
5. Place that button-style CTA above the fold, before the point where visitors need to scroll. (inferred: confirm fold position via a real device/viewport check, not just a desktop preview)
6. Audit existing pages for the mismatched pattern, such as a flashy button on an informational article or a buried inline link on a bottom-of-funnel page, and swap the CTA style to match the page type. (inferred)

**Pitfall:** Using a flashy banner or sidebar CTA on informational content — banner blindness means these are ignored regardless of design quality, while a plain inline text link mid-paragraph converts better precisely because it does not look like an ad.

### 16. Use outbound calls and emails as the cheapest cold-positioning test  `160.11`
*useful · concrete actions · source 160*

Grow and Convert define selling to a cold audience as selling to someone who has never heard of you and was not introduced through a connection, and they list three qualifying channels: inbound from content, paid channels, and outbound sales by email and phone. They make the point that outbound counts, because you are still pitching a stranger and seeing if you can close them, which tests whether your positioning closes cold people. That makes outbound the fastest and cheapest of the three to run, since it needs no traffic and no ad budget. Their underlying claim is that positioning and messaging which close warm people are not guaranteed to close cold people, and they say they have seen this repeatedly.

> "positioning and messaging that can close warm people is not always guaranteed to close cold people"

**Evidence:** Grow and Convert say they have seen positioning that closes warm audiences fail on cold ones time and again, including at a client with multiple millions in referral revenue.

**How to do it**

1. Write the pitch exactly as your website states it, not as you say it on referral calls.
2. Build a list of 50 to 100 prospects with no connection to anyone at the company.
3. Run the pitch by email or phone with no social proof from mutual contacts.
4. Log every objection verbatim and note where in the pitch the conversation stalls.
5. Compare the close rate against your referral close rate on similar deals.
6. If the cold close rate collapses, rewrite the site messaging to answer the objections a referrer normally handles for you.
7. Re-run a second cold batch with the rewritten pitch before scaling content or paid spend.

**Pitfall:** Counting warm intros or existing-customer expansions as proof of cold-channel sales. The pitch still relies on someone else vouching for you, so the test proves nothing about your site messaging.

**Apply at Pabau:** Before Pabau commits to a content push into a new geography or specialty, David can have sales run a short cold outbound batch using the exact website pitch for that segment. The objections it surfaces belong in the landing page copy before the articles are written.

**Apply anywhere:** Test your positioning on strangers with a short outbound email or call batch before spending on content or ads. Use the pitch exactly as your website states it, log the objections, and fix the site copy before scaling traffic.

### 17. Watch 50 Microsoft Clarity recordings to find conversion friction  `36.6`
*useful · concrete actions · source 36*

A concrete, free experiment is to install Microsoft Clarity and watch 50 session recordings of real visitors on the site, specifically looking for where they rage-click (a sign of a broken or confusing element) and where they stop scrolling (a sign of lost interest or a confusing layout) — this is described as revealing more than any analytics dashboard could on its own. This connects to a broader point made elsewhere in the same thread: roughly half of a site's conversion gains come from fixing this kind of post-click friction rather than from SEO itself, so tracking what happens after the click, not just rankings and traffic, is where much of the overlooked opportunity sits.

> "install Microsoft Clarity, watch 50 session recordings of real people"

**How to do it**

1. Install Microsoft Clarity (free) on the site if it is not already running.
2. Let it collect session recordings for a representative period across the site's key pages.
3. Watch at least 50 individual session recordings, prioritizing top-traffic and top-converting-intent pages first.
4. While watching, log two behaviors specifically: rage-clicks (repeated rapid clicking, indicating a broken or confusing element) and the exact point where each visitor stops scrolling.
5. Cross-reference the pages or elements with the most rage-clicks or earliest scroll-stops against that page's conversion rate to prioritize fixes.
6. Fix the highest-impact friction points identified before investing further in new SEO content for that page. (inferred)
7. Track conversion rate and rankings separately after fixes, since post-click friction fixes are framed as roughly half of the total optimization opportunity, distinct from SEO or ranking work.

**Tools:** Microsoft Clarity

**Pitfall:** Only tracking rankings and traffic while ignoring post-click behavior — roughly half of realistic conversion gains are said to come from fixing post-click friction rather than from SEO itself, so a purely SEO-focused audit misses half the opportunity.

### 18. Weave the product into top-of-funnel guides too, not just bottom-funnel posts  `96.10`
*useful · content insights · source 96*

Grow and Convert pre-empt the objection that product weaving only makes sense for clear purchase-intent queries like 'paid search dashboard' and not for an ultimate guide. They say that is not true. They are seeing cases where top-of-funnel pieces convert really well when the product is woven in and sold within the piece. The conversion rate is lower than on a bottom-funnel piece, but because top-of-funnel guides carry higher search volume, they can still produce solid conversion volume. The practical consequence is that an awareness-stage guide should not be written as neutral education with a banner at the end. It should carry the same pain-point opening, positioning and product demonstration as a bottom-funnel post, accepting a lower rate on much larger traffic.

> "top-of-funnel pieces actually convert really well"

**Evidence:** Grow and Convert report seeing top-of-funnel pieces convert well when the product is woven in, with lower rate but higher volume producing solid conversion counts.

**Pitfall:** Assuming a lower conversion rate means product mentions are wasted. Judging a guide on rate alone hides the fact that volume can make total conversions competitive with a bottom-funnel page.

**Apply at Pabau:** Pabau's broad /blog/ guides should still open on a practice-owner pain point and demonstrate Pabau inside the workflow, not just carry the book-demo CTA at the end. Track conversions per article, not conversion rate alone.

**Apply anywhere:** Weave the product into top-of-funnel guides as well. The rate is lower, but the volume can make the total conversions worthwhile.

### 19. Write the offer text directly onto the Facebook ad image  `155.6`
*useful · concrete actions · source 155*

Erika made the ad image herself in Canva for one dollar and wrote the offer out on the image itself. Grow and Convert flag that they cannot isolate how much this contributed, but note ad images are well known to drive Facebook ad performance, and writing the offer on the image means someone scrolling a feed sees what is being offered at a glance rather than having to read the body copy. The same creative earned 566 reactions, 59 comments and 219 shares, and averaged a 6.37% CTR. The cost of the asset is the striking part: a one-dollar Canva image carried a campaign that produced 1,892 subscribers, so creative quality here is about clarity, not production budget.

> "She made the image with Canva for $1."

**Evidence:** A $1 Canva image drew 566 reactions, 59 comments, 219 shares and a 6.37% CTR.

**How to do it**

1. Write the offer as one short line before you design anything, for example the name of the free course.
2. Build the image in Canva using a template; budget a dollar and an hour, not a design brief.
3. Overlay the offer text on the image so it is legible at feed thumbnail size.
4. Use a photo that shows the outcome the reader wants, not a product shot or logo.
5. Reuse the same image on the landing page so the click feels continuous.
6. Check Facebook's text-on-image warnings before publishing and trim wording if flagged.
7. Track reactions, comments and shares per creative, not just CTR.
8. Produce two or three offer-on-image variants and keep the one with the highest link CTR.

**Tools:** Canva, Facebook Ads

**Pitfall:** Stock imagery with no offer text makes the reader rely on body copy that most scrollers never read, which drops CTR and raises cost per click.

**Apply at Pabau:** For Pabau's paid social, produce the creative in Canva with the offer written on the image, for example the name of the free clinic template, rather than commissioning polished brand imagery.

**Apply anywhere:** Put the offer in words on the ad image itself and build it cheaply in Canva, since clarity at thumbnail size drives more clicks than production value.
