# Conversion & Monetization — supporting (part 2 of 5)

21 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Disable automated extensions and smart campaigns in account settings  `157.7`
*useful · concrete actions · source 157*

Grow and Convert accept that ad extensions work when you build them deliberately, because they make the ad stand out and give the searcher useful extra information. The problem is Google's automated version, which generates extensions itself and can produce clicks for services you do not offer or locations you do not serve. They point out this is switchable off in account settings. They give the same treatment to Smart campaigns, which they describe as Dynamic Search Ads with fewer controls: the ad shows in more places than search, it can show to users outside your designated search area, and you cannot control bidding details such as your max bid or CPC. Losing max bid control is the specific reason they reject them for SaaS lead generation.

> "attempts to automate these, which can cause irrelevant clicks"

**Evidence:** Grow and Convert note automated extensions can cause irrelevant clicks for services or locations that should not be on the ad, and that Smart campaigns remove max bid control entirely.

**How to do it**

1. Open Google Ads account settings and find the automated extensions or automated assets controls.
2. Turn off automated assets account-wide, or at minimum turn off the dynamic sitelink, dynamic callout and automatically created asset types.
3. Build the sitelinks, callouts and structured snippets manually so each names a real product area you sell.
4. Pause any Smart campaign in the account and rebuild it as a standard search campaign.
5. Set a manual max CPC or a portfolio bid strategy with a bid cap so max bid stays under your control.
6. Confirm the campaign's location targeting is set to presence rather than presence-or-interest.
7. Re-check these settings after each Google interface update, since automated assets are re-enabled by default.

**Tools:** Google Ads

**Pitfall:** Leaving automated assets on while manually building extensions. Google mixes both, so an ad you carefully wrote still shows a machine-written line about a service you do not sell.

**Apply at Pabau:** If Pabau advertises, build sitelinks manually to the real product areas such as online booking, and keep location targeting to the countries Pabau actually sells in rather than letting Google widen it.

**Apply anywhere:** Turn off automated assets and rebuild extensions by hand so every line names a service you actually sell. Avoid Smart campaigns, which remove your control of max bid and location.

### 2. Do not expect double-digit conversion on a page taking heavy organic traffic  `146.11`
*useful · content insights · source 146*

Grow and Convert give a volume argument for why organic pages sit far below paid landing page benchmarks. Far more people click organic listings than ads, tens of thousands of visitors in the example they analyzed, and pages taking that kind of traffic are not going to convert at 10% or more. The population is simply broader. On top of that, someone scrolling past the ads to click an organic result is slightly higher in the funnel and in research mode rather than ready to buy. The practical consequence is that a conversion rate is only meaningful next to the traffic volume and source behind it. A 1.13% rate on tens of thousands of organic visitors is not a worse result than 10% on a few hundred qualified ad clicks.

> "Pages getting that kind of traffic aren't going"

**Evidence:** Grow and Convert cite tens of thousands of organic visitors on the pages in their client comparison, against paid landing pages converting above 10% on much smaller click volumes.

**Pitfall:** Judging a high-traffic organic page against a low-traffic, high-intent benchmark and rebuilding it to chase a rate it can never reach. The usual result is a stripped-down page that also loses the ranking.

**Apply at Pabau:** When David reviews conversion rates on Pabau's highest-traffic blog articles, he should read rate and volume together and compare only against other organic pages of similar traffic.

**Apply anywhere:** When reviewing conversion rates on your highest-traffic articles, read rate and volume together and compare only against other organic pages of similar traffic.

### 3. Do not hand keyword and ad creation to Dynamic Search Ads  `158.4`
*useful · best practices · source 158*

Grow and Convert advise against Google's Dynamic Search Ads. DSA picks keyword groups, writes ad text and matches ads to landing pages automatically, which means running the campaign with almost no input from the advertiser. In their experience DSA produces campaigns that are not relevant to the business goal, for example targeting the wrong market, and that contain inaccurate claims, such as advertising a service a competitor offers but the client does not. It also produces ad text that does not match either the landing page or the search term. Their whole argument is that keyword, ad copy and landing page have to be chosen by someone who knows the product and the market, so any automation that removes that judgement defeats the setup.

> "You may be tempted to use Dynamic Search Ads"

**Evidence:** Grow and Convert report DSA campaigns targeting wrong markets and advertising competitor services across client audits.

**How to do it**

1. Check the campaign type column in Google Ads for any campaign labelled Dynamic Search Ads.
2. Export the auto-generated headlines and the landing pages DSA selected for the last 90 days.
3. Read each headline against your actual service list and flag any that promise something you do not sell.
4. Pause the DSA campaign rather than trying to constrain it with page feeds.
5. Rebuild the same coverage as manual search campaigns with hand-picked phrase and exact keywords.
6. Write ad copy yourself for each ad group and point each to a landing page you chose deliberately.
7. Keep DSA off permanently unless you can staff a weekly review of what it generated.

**Tools:** Google Ads

**Pitfall:** DSA can advertise a service you do not offer, which produces leads your sales team has to disqualify on the call. The signal is inbound asking about something not on your site.

**Apply at Pabau:** Pabau should never let DSA generate ads from pabau.com, because the blog and template library would produce headlines about generic clinic topics that imply services Pabau does not sell.

**Apply anywhere:** Do not run Dynamic Search Ads. Letting Google generate keywords, copy and landing page pairings produces ads that promise things you do not sell and copy that does not match the search.

### 4. Eliminate false bottoms and overly clever, benefit-free H1s  `13.9`
*useful · best practices · source 13*

Irwin flags two common failures from his audits: false bottoms, where a page's visual design makes it look like the content has ended when more exists below, compounding the fact that 60 to 70% of visitors never scroll past the first screen at all; and H1 headlines written to be clever or abstract rather than to state the benefit, so visitors do not even know what the page is selling because copywriters are afraid to sell with their writing. Both faults compound the no-scroll statistic: if the one screen visitors do see has a false bottom or a benefit-free headline, the page has effectively failed before the visitor engages with anything else.

> "60 to 70% of people won't even go below the fold"

**How to do it**

1. Screenshot the page exactly as it appears on first load, with zero scrolling, on both desktop and mobile viewport widths.
2. Check for a false-bottom risk: does whitespace, a background color change, or a horizontal rule make the visible area look like a natural page ending? If yes, add a visual cue such as a partially cut-off element, a downward arrow, or a content teaser signaling more follows.
3. Read the H1 in isolation, without surrounding context, and ask whether a first-time visitor would know what is being sold or offered; if not, rewrite it to state the concrete benefit.
4. Remove abstract corporate language from the H1 and replace it with a direct statement of outcome or benefit.
5. Re-screenshot after edits and confirm both issues are resolved before publishing (inferred: have a person unfamiliar with the page view it cold and describe what they think it offers).

**Pitfall:** Writing H1s to sound clever instead of stating the benefit — Irwin's example is a real tagline, 'Your success is our pride,' where he says he has no idea what it means or what the company even sells.

### 5. Every page must answer who, what, trust, contact  `13.1`
*useful · best practices · source 13*

Irwin How's four-part audit framework for any landing page, blog post, or homepage: does it clearly say who you are, what you do, why the visitor should trust or believe you (proof), and how to contact you. He frames it as a first-date test — a date that never introduces itself or never asks for your number fails, and a page skipping any of the four elements loses the visitor the same way. Apply this to every page type, not just conversion pages, since blog posts, about-us pages, and homepages all need the same four elements expressed differently (a blog needs proof via stats/facts, an about page needs proof via credentials). Run this check before any CTA or CRO work, because CTA placement is wasted if the page hasn't first established who/what/trust.

> "boiled down everything into four key things that any page"

**How to do it**

1. Open the page being audited (blog post, landing page, homepage, or about-us page) in a browser without scrolling.
2. Check for element 1: does the visible area state who the business or author is, in plain language, within the first screen?
3. Check for element 2: does it state what the business does or what the article covers, without jargon?
4. Check for element 3 (trust/proof): is there a fact, statistic, credential, or source citation backing the claim, not just an assertion?
5. Check for element 4 (contact): is there a way to get in touch or take the next action visible on this same page, not requiring a click to a separate contact page?
6. Mark the page as failing if any of the four elements is missing or requires scrolling or clicking away to find (inferred: score pass/fail per element in a tracking spreadsheet).
7. Rewrite or add the missing element directly, prioritizing whichever is missing highest up the page.
8. Re-check the page after edits by repeating step 1 with fresh eyes or a colleague who has not seen it.

**Pitfall:** Businesses often nail the first three elements (who/what/trust) but forget the fourth (asking for the contact) — Irwin calls this embarrassing, like going on a date and never asking for the phone number.

### 6. Expect low CPC to signal bad targeting, not good buying  `158.13`
*useful · best practices · source 158*

A recurring mechanism across this case study is that cheap clicks are usually cheap because nobody valuable is competing for them. Grow and Convert note that broad match survives audits precisely because irrelevant terms significantly lower CPC and improve up-funnel metrics, and that Search Partners is attractive because its CPC rates are often much lower than Google search. In both cases the low price reflects low intent, and the account's average CPC falls while the cost per qualified lead rises. The practical rule that follows is to treat a falling average CPC as something to investigate rather than celebrate, and to expect CPC to rise when you tighten match types and turn off partner networks. The client's spend actually fell from about $9k to $7k a month while MQL rate more than tripled.

> "the CPC rates are often much lower"

**Evidence:** Client spend fell from ~$9k to ~$7k a month while MQL conversion rate went from 7.6% to 24%.

**How to do it**

1. Chart average CPC and cost per qualified lead on the same timeline for the last 12 months.
2. Investigate every period where CPC fell, and check what match type or network change preceded it.
3. Remove average CPC from the headline of any performance report.
4. When tightening match types or disabling networks, warn stakeholders in advance that CPC will rise.
5. Set the success criterion for the change as cost per qualified lead before you make it.
6. Hold the change for at least one full sales cycle before reading the result.

**Tools:** Google Ads

**Pitfall:** A team optimizing toward lower CPC will systematically reintroduce broad match and partner networks, because both do exactly that while destroying lead quality.

**Apply at Pabau:** Pabau should never set a CPC target for paid search. Set a cost-per-qualified-demo target instead, and expect CPC to climb when targeting tightens onto practice owners.

**Apply anywhere:** Treat a falling average CPC as a warning sign. Cheap clicks usually mean you are reaching people who are not buying. Set your target on cost per qualified lead and accept a higher CPC.

### 7. Expect most of your blog to generate no business at all  `110.17`
*useful · best practices · source 110*

Grow and Convert point out something in their client screenshot that is easy to skip past. Looking at the landing pages report as a whole, the vast majority of blog posts generate almost no business. They state this is not an anomaly, it is the status quo for almost all SaaS companies, and that for most companies it is worse than the example shown, because they have all the non-converting posts without any of the high-converting ones. The planning consequence is that a blog is not a portfolio of roughly equal assets. A small number of pieces do the work and the rest are cost. Knowing that changes what you do with a decline: you stop maintaining the dead majority and concentrate effort on the few topic types that clear the baseline.

> "the vast majority of blog posts generate almost no business"

**Evidence:** Grow and Convert's client landing-pages report shows the vast majority of posts producing almost no business, which they describe as status quo for SaaS blogs.

**How to do it**

1. Pull twelve months of conversions by landing page for the blog.
2. Count the posts with zero conversions and express it as a share of the archive.
3. Rank the remaining posts and find how few account for most conversions.
4. Stop scheduled refreshes on the zero-conversion set unless they serve another purpose.
5. Reallocate that maintenance time to the converting topic type.
6. Report the concentration figure to stakeholders so publishing volume stops being the headline metric.
7. Reassess yearly, since a page can move into the converting set once its rankings mature.

**Tools:** Google Analytics

**Pitfall:** Treating every post as an asset worth maintaining. Refresh cycles spread evenly across a blog spend most of their budget on pages that have never produced a conversion.

**Apply at Pabau:** David should measure what share of pabau.com's articles produced zero demo requests in the last year. If the concentration is as skewed as Grow and Convert describe, the refresh queue should be limited to the converting set plus the template pages.

**Apply anywhere:** Measure what share of your blog produced zero conversions over twelve months. Concentrate refresh effort on the small set that clears the baseline and stop maintaining the dead majority, and report that concentration figure instead of publishing volume.

### 8. Expect name-and-email landing pages to convert at 10-20%, usually 10%  `155.8`
*useful · content insights · source 155*

The author, who A/B tests sites for a living, gives the working benchmark for a simple opt-in page. Landing pages asking only for name and email typically convert between 10% and 20%, with 10% far more common. He says he cannot recall a 20%-plus PPC landing page off the top of his head. Erika's page converted at 16%, which places it near the top of the observed range. He is careful to frame the benchmark as secondary though: the honest answer to 'is my conversion rate good' is whether the funnel is meeting profit goals at that percentage, because offer, industry, age of offer, ad platform, ad creative and ad targeting all move the number too much for a single benchmark to settle it.

> "convert between 10 – 20%"

**Evidence:** Practitioner benchmark from an A/B testing consultant: 10-20% for name-and-email opt-ins, 10% most common, 20%+ rarely seen on PPC pages. Erika's page: 16%.

**Pitfall:** Treating a benchmark as a target leads teams to keep testing a page that is already profitable, or to kill one that is unprofitable for reasons that have nothing to do with the page.

**Apply at Pabau:** When Pabau tests a gated template download, set the go or no-go on cost per qualified demo rather than on hitting a 16% opt-in rate.

**Apply anywhere:** Use 10-20% as the range for a simple name-and-email opt-in page, but decide whether to keep or kill the funnel on profit, not on the percentage.

### 9. Expect one blog post to outconvert the homepage over its lifetime  `142.10`
*useful · content insights · source 142*

Grow and Convert use Geekbot, a tool for running online standup meetings and a past client, as the proof that a single article can carry a business. A long-form post they wrote ranks second for 'Slack standup bot' and has a lifetime conversion rate of 8.36%, against the roughly 3% they cite for an average homepage. Their argument is that a long-form post can speak to a specific pain and a specific query in a way a homepage cannot, because the homepage carries high-level brand and product information and is not tailored to any one audience. Unless a reader already knows the brand, that generic framing does not hold attention or drive action. The practical consequence is that the highest-converting asset on a site is often a blog post ranking for one commercially loaded term, not the page the whole team spends its time redesigning.

> "has a lifetime conversion rate of 8.36%"

**Evidence:** Geekbot's post ranks #2 for 'Slack standup bot' with a lifetime conversion rate of 8.36%, against a cited homepage average near 3%.

**Pitfall:** Judging blog content on average blog conversion rate. The average is dragged down by informational posts, and the one or two commercial posts carrying the result disappear inside it.

**Apply at Pabau:** David should identify Pabau's single highest-converting article and give it the maintenance attention usually reserved for the homepage: refreshes, internal links and a direct demo path.

**Apply anywhere:** Identify your single highest-converting article and give it the maintenance attention usually reserved for the homepage: refreshes, internal links and a direct path to the sales action.

### 10. Find newsletter sponsors via Perplexity directory search, then skip the paywall  `68.17`
*useful · concrete actions · source 68*

Cody's method for finding brands that pay to advertise in email newsletters. He searches Perplexity for directory websites of brands that are sponsoring email newsletters. That surfaces aggregators which scrape newsletters, identify the sponsoring brands, and then charge for the contact details. His point is that you only need the aggregator for the brand list. Once you have the brand names, go to their websites yourself and find the person to contact, which avoids the per-contact charge entirely. He notes the whole flow could be automated. He values newsletter inventory over podcast inventory because a newsletter click is UTM-tagged and traceable to conversion, so the buyer can see attributable revenue rather than an unmeasurable impression count.

> "directory websites of brands that are sponsoring email newsletters"

**Evidence:** Cody describes the aggregators' business model directly and says the contact information is what they charge for, not the brand list.

**How to do it**

1. Search Perplexity for directory websites listing brands that sponsor email newsletters.
2. Open the aggregators it returns and pull the brand names from the free listing view.
3. Ignore the paid contact-detail upsell.
4. Look up each brand's own site and find the media buyer or growth marketer directly.
5. Send the media kit pitch referencing the specific newsletter you saw them sponsor.
6. Make sure every link you sell is UTM-tagged so the sponsor can attribute revenue.
7. Automate the brand-list-to-contact step once the manual version is proven.

**Tools:** Perplexity

**Prompt / template:**

```text
Find directory websites that list brands sponsoring email newsletters.
```

**Pitfall:** Paying the aggregator per contact for information you can find on the brand's own site in two minutes, at the volume this prospecting needs, gets expensive fast.

**Apply at Pabau:** The same Perplexity directory search identifies which newsletters aesthetics and healthcare software buyers already sponsor, which tells Pabau where its competitors are spending and where a placement would reach practice owners.

**Apply anywhere:** Use Perplexity to find directories of newsletter sponsors, take the brand list for free, and source the contacts yourself from each brand's site. Sell UTM-tagged newsletter links, because attribution is what commands the higher rate.

### 11. Fund promotion from the retainer to remove the client's spend decision  `178.14`
*useful · concrete actions · source 178*

Grow and Convert fund both halves of their promotion process, the paid ads and the manual link building, from their own budget with no extra spend passed to clients. They present that as what makes them a truly full-service agency and as markedly different from other top content marketing agencies. The mechanism worth copying is commercial rather than tactical. When promotion sits on a separate ad-spend line, every campaign becomes a client approval, and approvals stall in the months before results exist. Absorbing promotion into a single retainer removes the recurring decision, so promotion actually happens during the pre-ranking window when it matters most. The trade is that the supplier carries the cost risk and must therefore be disciplined about which pages get promotion budget, which is the same discipline that improves results.

> "from our own budget, with no extra spend for our clients"

**Evidence:** Grow and Convert say funding paid ads and link building from their own budget is markedly different from other top content marketing agencies and something they are proud to offer.

**How to do it**

1. Price promotion into the retainer as a single number instead of a pass-through ad-spend line.
2. Set an internal per-article promotion cap so the absorbed cost stays predictable.
3. Decide allocation on evidence: paid spend on new pages, link spend on pages already ranking.
4. Show the client the promotion activity in the monthly report even though they are not approving each spend.
5. Review the absorbed cost against the breakeven chart quarterly and adjust the retainer if it drifts.
6. If you are the buyer, ask which model the agency uses, because pass-through spend means recurring decisions on your side.

**Pitfall:** Absorbing promotion cost with no per-article cap. Margin disappears on the accounts that need the most amplification, which are usually the weakest domains and the longest engagements.

**Apply at Pabau:** If Pabau uses an outside content supplier, David should ask whether promotion is retainer-funded or pass-through, since pass-through means Pabau carries an approval step every month during the window when promotion matters most.

**Apply anywhere:** Ask whether promotion is funded from the retainer or billed as pass-through spend. Pass-through creates a monthly approval that usually stalls exactly when new pages need amplification most.

### 12. Gate content behind urgency and genuinely non-AI-obvious value  `13.3`
*useful · concrete actions · source 13*

To convert blog readers into leads, Irwin says content must first trigger an urgent problem rather than merely solving a problem people already feel resolved about, since solving a problem alone makes people say that's good enough and stop there. Once urgency is raised, the value offered behind the gate (an email-gated PDF, a phone-gated call) must be something the reader could not have simply generated in ChatGPT — because handing over contact details means giving up the most personal information a visitor owns (name, phone, email), generic AI-rehashed advice does not justify that exchange. The tactic only works if the practical, applied insight is specific enough that a reader thinks they could not have gotten this from a prompt.

> "don't just give me something you chat-pulled out"

**How to do it**

1. Identify the single most urgent, unresolved pain point in the topic, not the general problem — e.g. not how patient no-shows happen but the specific cost spike the week no-shows peak.
2. Write the top section of the content to surface that urgent angle explicitly, before presenting the solution.
3. Draft the gated asset (PDF, calculator result, extended checklist) so it contains at least one specific, applied detail generic AI output would not produce, such as real benchmark numbers or a proprietary step sequence.
4. Test the draft against a ChatGPT/Claude prompt for the same topic (inferred: paste your outline in and ask it to write the equivalent); if the AI output is indistinguishable, add more proprietary specificity before publishing.
5. Place the gate (email/phone form) immediately after the urgency is established, not before it and not buried at the very end.
6. Monitor the gate's form-fill rate in analytics after publishing to confirm the urgency framing is working (inferred: compare against a page that only solves rather than triggers urgency).

**Tools:** ChatGPT

**Pitfall:** Giving readers something they could have generated themselves in ChatGPT kills the perceived value of the exchange, and they will not hand over contact details for it.

### 13. Gate one downloadable asset per article as a high-intent signal  `56.8`
*useful · concrete actions · source 56*

Cody looks for engagement signals he can send back to Google, and the one he rates highest inside a blog post is a downloadable asset with a promise attached. His reasoning: someone giving their contact details to a site they have just landed on is an unusually strong intent signal, and the click through to a form page plus the form completion is a deeper journey than dwell time. Historically he did the same thing with scroll tracking - firing an event every 10% of the page as the reader descends - and says he has seen that alone lift sites overnight, because Google Analytics 4 sits inside Google's ecosystem and the more signal you can send it the better the page tends to do. Both hosts agree that a click that takes the reader deeper into the site is a positive trust signal.

> "downloadable assets with like some type of promise"

**How to do it**

1. Create one genuinely useful downloadable per article topic - a template, checklist, or calculator, not a rehash of the post.
2. Put the offer inside the article body with an explicit promise of what the reader gets.
3. Send the click to a dedicated form page rather than an inline modal, so the journey is a real page-to-page step.
4. Fire a conversion event on form submission and attach the originating article URL.
5. Separately enable scroll tracking that fires an event every 10% of page depth.
6. Report both by article so you can see which topics produce readers willing to identify themselves.
7. Treat topics with high download rates as your best candidates for supplementary articles and internal links.

**Tools:** Google Analytics 4, Google Tag Manager

**Pitfall:** The signal argument here is his working hypothesis, not documented Google behaviour - the lead capture is worth doing on its own merits, and any ranking benefit should be treated as unproven.

**Apply at Pabau:** Pabau already publishes template articles - make sure each one has a real gated or tracked download and that the form completion is reported back against the article, so template content can be judged on leads rather than sessions.

**Apply anywhere:** Make sure any article built around a template or resource has a real tracked download, and that the form completion is reported back against the article, so that content can be judged on leads rather than sessions.

### 14. Interview interested non-buyers to locate which of five positioning faults you have  `169.8`
*useful · concrete actions · source 169*

Hyam gives a five-item differential diagnosis for a business that gets leads but cannot close: the product does not solve a real problem, you are selling to the wrong customer, nothing about it is truly unique, you are not explaining it clearly and concisely, or it is not easy for someone to prove the solution would work for them. He is specific about how to tell which one applies. Talk to prospects who were interested and did not convert, ask customers who churned, and ask people in your target segment why they are not interested and why they did not purchase. He warns the answers are always humbling. The value of the framework is that it separates a messaging problem, item four, from a targeting problem, item two, and from a product problem, item one, which otherwise all present as the same low close rate.

> "The answers are always humbling"

**Evidence:** Hyam says Grow and Convert went through four pivots before reaching the positioning that worked, and four failed attempts at a product company before the service.

**How to do it**

1. Pull a list of prospects from the last two quarters who engaged then went silent.
2. Pull a list of customers who churned in the same window.
3. Pull a list of people in the target segment who never engaged at all.
4. Ask each group why they did not buy, or why they left, in their own words and without defending the product.
5. Tag every answer against the five faults: no real problem, wrong customer, no uniqueness, unclear explanation, unprovable.
6. Count the tags and treat the largest pile as the fault to fix first.
7. If the pile is 'unclear explanation' rewrite the messaging; if it is 'wrong customer' change the targeting criteria instead.
8. Re-run the interviews after the fix and check whether the pile moved.

**Pitfall:** Interviewing only churned customers. They tell you about delivery, not about positioning; the never-engaged segment is the group that reveals a targeting or clarity fault.

**Apply at Pabau:** David should run this three-list interview once a year on Pabau demo no-shows, churned practices and clinics that never booked, and use the tag counts to decide whether the fix belongs in messaging on the site or in who the content targets.

**Apply anywhere:** Diagnose a low close rate by interviewing three groups: interested prospects who never bought, churned customers, and target-segment people who never engaged. Tag every answer against the five positioning faults and fix the biggest pile first.

### 15. Judge CRO changes by net conversions, not conversion rate alone  `46.12`
*useful · best practices · source 46*

Travis's top CRO/SEO cross-functional rule: never evaluate a CRO test purely on the conversion-rate lift of the page it changed, because a change can hurt organic discoverability at the same time it improves on-page conversion, and if discoverability drops enough, net conversions still go down even though the rate itself went up. His standard is to require CRO and SEO teams to partner on every significant test, checking traffic and ranking impact alongside conversion-rate impact before declaring a test a win. He also flags 'thinking too small': most CRO teams chase incremental button-color or copy tweaks instead of redesigning entire funnels, which takes three to four weeks of dev work versus a few days but delivers roughly 10x the impact, citing his own example of a 40% online-sales lift for a cell-phone-plan provider from a full purchase-flow redesign tailored to an elderly user base.

> "what is the net sale gain"

**How to do it**

1. Before greenlighting any CRO test on an organic-traffic page, require sign-off or review from the SEO team, not just the CRO or design team.
2. Define the test's success metric upfront as net conversions, meaning organic sessions multiplied by conversion rate, rather than conversion rate alone.
3. Track organic rankings, impressions, and traffic for the tested page in Google Search Console for the duration of the test, alongside the CRO tool's conversion-rate reporting.
4. If conversion rate rises but discoverability falls enough to offset it, treat the test as a net loss and roll it back, even though the CRO dashboard would call it a win.
5. Once a quarter, scope at least one full-funnel redesign test per major conversion path, budgeting three to four weeks of dev time rather than a few days, instead of only queuing small incremental tests.
6. When redesigning a funnel, explicitly design for the actual audience's technical comfort level, such as bigger buttons, larger text, and fewer steps for a less tech-savvy or older audience.

**Tools:** Google Search Console

**Pitfall:** A CRO test can show a positive conversion-rate lift on its own dashboard while silently damaging organic discoverability enough that net conversions actually fall — always check both metrics together, never conversion rate in isolation.

### 16. Keep affiliates on one URL so social platforms count the shares together  `171.9`
*useful · concrete actions · source 171*

Examine wrote their own referral software rather than using an off-the-shelf affiliate platform. Sol Orwell gives a specific reason: tools like ClickBank send each affiliate's traffic to a different URL, and Examine wanted every promoter pointing at the same URL so Facebook treated it as one link. That consolidation is what made the social proof visible. At peak, 105 fitness industry figures shared the link, and Sol credits the launch result to that visible pile-on: you cannot resist looking at something 105 people shared. Split the traffic across 105 tracking URLs and the same activity looks like 105 unrelated posts instead of one thing everybody is talking about.

> "sent you to a different URL and we wanted to redirect everyone to the same URL"

**Evidence:** Examine built custom referral software specifically so Facebook saw one link; 105 people shared it at peak and the launch did roughly 3,000 sales.

**How to do it**

1. Decide the one canonical URL every promoter will link to before the launch.
2. Pass affiliate attribution in a query parameter or cookie on that single URL rather than issuing separate destination URLs.
3. Check how each social platform treats the link: confirm the shares aggregate onto one preview and one share count.
4. Give affiliates copy and creative that all point at the same address.
5. Build or configure the referral tracking to strip the parameter before canonicalization so search engines see one page.
6. Watch the share count on launch day as the social-proof number, and reference it in your own promotion.

**Tools:** ClickBank, Facebook

**Pitfall:** Off-the-shelf affiliate platforms that issue per-affiliate destination URLs fragment the share count, so a coordinated launch looks like scattered unrelated posts and the social proof disappears.

**Apply at Pabau:** When Pabau runs a coordinated launch with partners or educators, David should give everyone the same URL with tracking in a parameter, so the share count aggregates instead of splitting across partner links.

**Apply anywhere:** For a coordinated launch, give every promoter the same URL and carry attribution in a query parameter. Per-affiliate destination URLs split the share count and destroy the social proof the coordination was supposed to create.

### 17. Keep meeting clients after the sale so they cannot fire a friend  `173.14`
*useful · best practices · source 173*

Dane's retention view is that relationship building does not stop at the signature. 'If you keep meeting with them, keep being friends with them, they'll find ways to keep you on,' he says, closing with 'It's hard to fire a friend.' This is the same instinct that runs through the cold emails and the free audits: treat the client as a friend rather than a transaction, and give honest advice including the parts that do not benefit you. The commercial case is the lifetime value figure he quotes elsewhere, $86,920 over 19 months from a single account. Retention, not acquisition, is where that number comes from, and continued in-person contact is the cheapest lever on it. It also explains why he still spends most of his time on sales, partnerships and brand rather than delegating them.

> "It's hard to fire a friend."

**Evidence:** $86,920 lifetime value over 19 months from one KlientBoost account; Dane still personally runs sales and relationships at $300,000 monthly recurring revenue.

**How to do it**

1. Schedule post-sale contact on a calendar cadence rather than waiting for a reporting cycle to force it.
2. Include at least one in-person or video meeting per quarter that is not a performance review.
3. Give advice in those meetings that does not sell anything, including things they should do elsewhere.
4. Track months retained per account as a headline metric alongside new bookings.
5. Flag accounts that have had no non-reporting contact in 90 days as churn risks.
6. Keep the founder or a senior person in the relationship for the largest accounts.
7. Compare the cost of the contact cadence to average lifetime value to confirm it pays.

**Pitfall:** Letting the relationship narrow to monthly reports means the account is judged purely on this month's numbers, which is exactly when a soft quarter becomes a cancellation.

**Apply at Pabau:** Pabau's customer success should book a quarterly non-reporting call with each practice, focused on their goals rather than product usage. David can feed what comes out of those calls into blog and template topics, since it is the same source of real customer questions that keyword tools miss.

**Apply anywhere:** Put post-sale relationship contact on a fixed cadence, keep at least one meeting a quarter that is not a performance report, and give advice that does not sell anything. Retention drives lifetime value more than acquisition does.

### 18. Keep price out of the criteria you teach the buyer in the intro  `72.6`
*useful · best practices · source 72*

Reviewing an AI-generated list of evaluation factors, Khanal rejects 'does it cost per seat' as an intro criterion. His rule: unless being the cheapest is your explicit value proposition, never put cost into the section where you are teaching the reader what to think about. He says plainly that he does not want them thinking about cost, he wants them thinking about quality. This is a framing decision about where the buyer's attention goes at the top of the page, not an argument for hiding pricing. He separately allows objective comparisons such as starting price and feature set later in the piece, where the numbers are verifiable, but keeps them out of the criteria list that sets the reader's mental model.

> "I don't want them thinking about cost"

**Evidence:** Khanal cut 'does it cost per seat' from the AI's proposed factor list on a live edit, keeping only substance, SERP analysis and editing time.

**How to do it**

1. List the evaluation criteria you plan to teach in the intro of a comparison page.
2. Remove any criterion about price, cost per seat or budget unless you are competing on being cheapest.
3. Replace it with a quality criterion you can defend, such as what the tool understands about your business.
4. Put verifiable pricing facts, like starting price, lower in the page where they support a comparison.
5. Check the body sections still map one to one to the revised criteria list.
6. Re-read the intro and confirm the reader leaves it thinking about outcomes, not budget.

**Pitfall:** Letting an AI draft set your criteria. AI briefs routinely propose cost per seat as a factor because competitors list it, which anchors the reader on price before they understand quality.

**Apply at Pabau:** On Pabau comparison and 'best software' pages, keep the intro criteria about what the software understands and how much admin it removes. Pabau's pricing model, where every subscription includes every feature, belongs further down as a verifiable comparison point.

**Apply anywhere:** Keep cost out of the criteria you teach in a comparison page's intro unless price is your actual differentiator, and move verifiable pricing facts further down the page.

### 19. Kill a paid funnel after roughly 40 clicks with zero opt-ins  `155.9`
*useful · concrete actions · source 155*

The author describes shutting down a Facebook-to-email funnel he built for a real estate agent after 40 views on the page produced no opt-ins at all. His reasoning is arithmetic, not impatience. Even if the very next click had converted, one email from 41 clicks is a 2.4% conversion rate, which was far too low to work financially for that business. He adds the caveat that the same rate might be acceptable for a business with different economics. The value here is the stopping rule: rather than waiting for statistical significance on a page that is clearly outside the viable range, compute the best case implied by the zero-conversion streak and compare it against the rate the funnel needs.

> "got 40 views on the page without a single optin"

**Evidence:** Real estate agent funnel shut off after 40 page views and zero opt-ins; best case 1 in 41 clicks, or 2.4%.

**How to do it**

1. Work out the opt-in rate your funnel needs before launching, from cost per click and value per subscriber.
2. Send paid traffic and watch the running count of clicks and opt-ins daily.
3. Once a zero-conversion streak reaches about 40 clicks, compute the best case rate as one divided by clicks plus one.
4. Compare that best case against the required rate; 2.4% against a 10% requirement is a clear kill.
5. Turn the campaign off rather than adding budget to reach significance.
6. Change the offer or the audience next, not the button color.
7. Relaunch and apply the same stopping rule to the new version.
8. Record each killed variant with its click count and required rate, so the rule stays consistent across tests.

**Tools:** Facebook Ads, LeadPages

**Pitfall:** Spending to statistical significance on a page whose best possible rate is already below the viability threshold wastes the whole test budget on a foregone conclusion.

**Apply at Pabau:** Set the same stopping rule on Pabau's paid tests of gated content: if 40 clicks produce no downloads, switch the offer instead of buying more traffic.

**Apply anywhere:** Define the opt-in rate your funnel needs in advance, then kill any paid test whose best-case rate after about 40 zero-conversion clicks still falls below it.

### 20. Launch the service your inbound questions keep asking for within a week  `183.5`
*useful · concrete actions · source 183*

During and after their course launch, Grow and Convert kept receiving the same question through their landing page and by email from business owners: do you offer a done-for-you content marketing service. They had not planned this and it did not match the offer on the page. Rather than filing it, they launched a done-for-you content marketing service the week after the course launch. They landed the first client within a few days of announcing it and a second a few weeks later. The whole agency business came from reading repeated inbound questions as demand. The speed matters: the announcement went out while the audience attention from the launch was still live.

> "launched a done-for-you content marketing service the week after our course launch"

**Evidence:** First agency client landed within a few days of the announcement, a second a few weeks later, and the agency became the company's main focus.

**How to do it**

1. Keep a single running log of every inbound question that does not match the offer currently on your page.
2. Group them by what the asker actually wants delivered, not by how they phrased it.
3. When one group repeats across several unrelated prospects, treat it as a validated request.
4. Write the new offer as one announcement to your existing list and one section on the site, with no build-out.
5. Ship it inside a week of the launch it emerged from, while the audience is still paying attention.
6. Take the first one or two clients manually and deliver without productizing anything.
7. Only build process, pricing tiers and hiring after the second client proves it repeats.

**Pitfall:** Waiting to build the delivery machine before announcing. Announce first and deliver the first clients by hand; a service that needs a system before it can be sold usually never gets sold.

**Apply at Pabau:** Pabau's inbound already carries requests for things outside the product, such as setup help, migration or marketing support. David should log those centrally, and where one repeats, test a named service page rather than answering each request individually.

**Apply anywhere:** Log inbound questions that do not match what you sell. When one repeats across several prospects, announce that service to your list within a week, deliver the first clients manually, and only build process once a second client proves it repeats.

### 21. Limit ad groups per campaign because budget is set at campaign level  `158.8`
*useful · best practices · source 158*

Grow and Convert point out a structural detail advertisers miss: the daily budget in Google Ads is set at campaign level, not per ad group or per keyword. So every ad group in a campaign competes for the same pot. If a campaign carries many ad groups, the ones producing qualified leads have to share budget with the ones that do not, and the best performers get throttled by the weakest. Their recommendation is to keep the number of ad groups in each campaign low so spend concentrates where it works, and to promote a particularly strong ad group into a campaign of its own so it gets a protected budget. This sits alongside their rule of few keywords per group, and the two together are what let spend follow performance.

> "your daily budget is set at the campaign level"

**Evidence:** Grow and Convert recommend giving a particularly well-performing ad group its own campaign.

**How to do it**

1. List every campaign with its ad groups and each group's cost and qualified-lead count for 90 days.
2. Calculate cost per qualified lead per ad group, not per campaign.
3. Identify campaigns where a strong group sits beside two or more weak ones.
4. Move the strongest ad group into its own campaign with its own daily budget.
5. Pause or reduce the weak groups instead of leaving them drawing from the shared pot.
6. Keep remaining campaigns to a small number of ad groups so budget is not diluted.
7. Review budget allocation monthly against cost per qualified lead, not against clicks.

**Tools:** Google Ads

**Pitfall:** A high-performing ad group can look budget-constrained in reporting while the real cause is a sibling group in the same campaign eating the daily budget.

**Apply at Pabau:** If one Pabau ad group, say medspa software terms, produces most qualified demo requests, split it into its own campaign so generic clinic-software groups stop consuming its daily budget.

**Apply anywhere:** Because Google sets daily budget at campaign level, keep few ad groups per campaign and promote any consistently strong ad group into its own campaign so it stops sharing budget with weak ones.
