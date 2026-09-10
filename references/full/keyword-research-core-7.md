# Keyword Research — core (part 7 of 7)

23 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Target the spreadsheet or manual tool customers used before you  `113.4`
*core · concrete actions · source 113*

Grow and Convert's Timetastic example turns the incumbent workaround into a keyword bucket. Timetastic's team told them most customers had previously managed time off with Excel spreadsheets and Outlook calendars. That led them to target keywords like staff leave planner for excel, google sheets annual leave template, and how to add annual leave to outlook calendar. The reasoning is that these searchers are already using a competitor, even when the competitor is just a spreadsheet, and are likely frustrated with it. This is a distinct move from the usual competitor-alternative page, because the incumbent is not a rival vendor and nobody would list it as a competitor. It also produces template and how-to queries with real volume, in a place where no software vendor is defending the SERP.

> "managing time off with Excel spreadsheets"

**Evidence:** Timetastic, staff leave planning software: keywords chosen from the finding that most customers previously used Excel spreadsheets and Outlook calendars.

**How to do it**

1. Ask the sales and onboarding teams what customers were using to do this job before they bought, and write down the actual tool names.
2. Include manual and generic tools in that list: Excel, Google Sheets, Outlook, paper, WhatsApp, a shared inbox.
3. Build keyword variants around each: [job] template for excel, [job] google sheets template, how to [job] in [tool].
4. Check the SERP for each variant; if it is dominated by template downloads and how-to posts rather than vendors, the gap is open.
5. Publish a genuinely useful template or walkthrough for the incumbent tool, so the page satisfies the query rather than baiting it.
6. Inside that page, name the point where the spreadsheet method breaks down and position your product as the next step.
7. Track signups per page, not traffic, since these queries pull in people who will never buy alongside the frustrated ones.

**Tools:** Ahrefs, Semrush

**Pitfall:** Publishing a thin page that pretends to offer the spreadsheet solution and immediately pivots to a pitch. The query intent is the template, so a page that fails to deliver it will not hold the ranking.

**Apply at Pabau:** Pabau's template pages already fit this shape. David should ask which spreadsheets and paper forms new practices arrive with, then build template pages for those exact artifacts, each showing where the manual method fails.

**Apply anywhere:** Ask what customers used before they bought, including spreadsheets and paper. Build template and how-to pages for those exact artifacts, deliver the template properly, then show where the manual method breaks.

### 2. Test Google Ads fit by searching your own category term first  `157.1`
*core · concrete actions · source 157*

Grow and Convert's qualifying question for any SaaS considering Google Ads is whether people already know about and actively search for the product category you sell. Their cheap test is to type your category name into Google and look at who is there. If other SaaS companies in your category are bidding on the category term, and you also see them in the organic results below the ads, that spend is evidence of a working market and there is very likely room for you. If your product is genuinely category-creating and nobody searches the term, paid search is the wrong channel and the budget belongs in outbound or other channels. They frame this as a go/no-go check to run before building a single campaign.

> "type the category name of your product into Google"

**Evidence:** Grow and Convert use competitor bidding plus organic presence on category terms as their fit test across SaaS clients.

**How to do it**

1. Write down the plain category name a buyer would use for your product, such as 'project management software'.
2. Search that term in Google in your target country with personalization off.
3. Count how many competing SaaS vendors are running ads on it; two or more paying vendors is your signal of a live market.
4. Scroll to the organic results and confirm the same vendors are also ranking, which shows sustained investment rather than one test.
5. Repeat for three to five adjacent category terms to check the demand is broad, not one keyword.
6. If no competitor is bidding and no vendor ranks organically, treat search demand as absent and put the budget into outbound or another channel.
7. If ads exist, pull the terms into a keyword tool and move on to intent screening before building campaigns.

**Tools:** Google Ads

**Pitfall:** Judging the market from one head term. A single expensive term with no advertisers can mean the category name is wrong, not that demand is missing, so check adjacent phrasings before ruling paid search out.

**Apply at Pabau:** Before David commits budget to paid search for Pabau, search 'practice management software', 'clinic management software' and 'aesthetic clinic software' and record which competitors bid and which rank. The same list also tells the blog which comparison and alternatives pages are worth writing.

**Apply anywhere:** Before committing budget to paid search, search your plain category term and its close variants and record which competitors bid and which rank organically. Sustained competitor spend is the market signal; the same list also shows which comparison pages are worth writing.

### 3. Test whether an LLM searches the web before targeting a keyword  `86.4`
*core · concrete actions · source 86*

Grow & Convert give a cheap pre-flight test for any keyword you plan to target for AI visibility. Type the query into ChatGPT and watch two things: whether it announces that it is searching the web, and whether the answer contains citations. Their example is 'what is content marketing', which Ahrefs shows at 8,000+ monthly searches with a keyword difficulty of 85. ChatGPT answers it directly, with no search and no links, and has no reason to name any company because the user wants information, not a product. Contrast that with 'what's the best project management software for remote teams', where ChatGPT searched the web without the search button being pressed and returned cited sources. The rule they draw: if the model answers from memory with no citations, no amount of ranking will earn you a mention there. Google now behaves the same way, pushing the first organic result below the fold behind a definition or AI Overview.

> "saying it's searching the web for the prompt above"

**Evidence:** 'What is content marketing' has 8,000+ monthly searches and KD 85 in Ahrefs, yet ChatGPT answers it directly with no links or citations, while the product query triggered a web search and returned citations from FastrackPR and Nova Media Group.

**How to do it**

1. Take each candidate keyword and paste it into ChatGPT as a natural question, without clicking the search button.
2. Watch for the 'searching the web' indicator; note whether it appears.
3. Check the finished answer for citations and named vendor recommendations.
4. Mark keywords that get answered from memory with no citations as no-mention keywords and cut them from the AI-visibility list.
5. Keep keywords where the model searched and cited, and check which domains it cited for the Tier 2 outreach list.
6. Repeat in Perplexity and Google AI Overviews, since coverage differs by engine.

**Tools:** ChatGPT, Perplexity, Ahrefs

**Prompt / template:**

```text
what's the best project management software for remote teams
```

**Pitfall:** High-volume informational keywords still look attractive in Ahrefs while returning zero AI brand exposure, and they also lose Google clicks as AI Overviews expand. Volume is the trap.

**Apply at Pabau:** Before Pabau commissions another broad aesthetics explainer, run the query through ChatGPT and check for a web search and citations. Terms like 'best clinic management software for medspas' pass this test; 'what is patient management' does not.

**Apply anywhere:** Before commissioning another broad explainer, run the query through ChatGPT and check whether it searches the web and cites sources. Product-evaluation queries pass; definitional queries do not.

### 4. Tie how-to keywords to a single product feature, not the broad job  `111.4`
*core · concrete actions · source 111*

Grow and Convert give a specific test for choosing pain-point keywords: keep the keyword as closely related to your product as possible. Their example is HR software. 'How to manage employees' is the wrong target because it is extremely general and HR software is only a small aspect of that topic. 'How to manage employee payroll' or 'how to manage employee PTO' are much better, because each maps to a feature the product actually has. The mechanism is conversion, not ranking. When the keyword names a job your feature does, the article has a natural place to show the product solving that exact problem, so a portion of readers convert. When the keyword names the whole discipline, the product is a footnote. They contrast this with terms showing no solvable pain at all, naming 'industry trends', 'tips to do X' and 'ultimate guide to Y' as the ones to avoid.

> "The key is to keep these keywords as closely related to your product as possible"

**Evidence:** Grow and Convert's HR software example: 'how to manage employees' rejected, 'how to manage employee payroll' and 'how to manage employee PTO' accepted.

**How to do it**

1. List your product's features one line each, in the words a user would use.
2. For every candidate how-to keyword, name the single feature that would appear in the article.
3. Drop the keyword if no feature maps, or if the mapped feature covers under a third of the topic.
4. Narrow a too-broad keyword by adding the object the feature acts on: 'manage employees' becomes 'manage employee PTO'.
5. Check the narrowed term in Ahrefs and accept lower volume as the cost of the mapping.
6. Reject 'industry trends', 'tips for X' and 'ultimate guide to Y' formats outright.
7. In the brief, state where in the article the mapped feature gets demonstrated.
8. Track conversions per article by mapped feature to confirm the mapping predicts conversion.

**Tools:** Ahrefs

**Pitfall:** A broad how-to ranks and brings traffic, but the product can only be mentioned in a closing paragraph, so conversion rate collapses and the page looks like a win in analytics.

**Apply at Pabau:** For Pabau, 'how to run a clinic' is the wrong /blog/ target. 'How to reduce clinic no-shows', 'how to write aesthetic consultation notes' and 'how to manage staff rotas in a clinic' each map to one Pabau feature and earn a demonstration section.

**Apply anywhere:** Before accepting a how-to keyword, name the single product feature that will appear in the article. If none maps, or the feature is a footnote, narrow the keyword until one does.

### 5. Too many informational posts can hurt commercial-intent rankings  `26.6`
*core · content insights · source 26*

Dooley claims that loading a commercial/service website with too many informational, top-of-funnel articles can actively harm its ability to rank for bottom-of-funnel, revenue-driving keywords, because the site's overall topical signal shifts toward reading as 'an informational blog' rather than 'an actual service-based website.' His teams therefore weight content production heavily toward bottom-of-funnel terms (directly tied to revenue), use some middle-of-funnel terms for cross-sell value, and only add top-of-funnel content selectively to fill specific topical gaps rather than by default.

> "harming your ability to rank for commercial-intent keywords"

**Evidence:** "Understand that some informational articles on your website might actually be harming your ability to rank for commercial-intent keywords, because you're becoming more of an informational blog than an actual service-based website... every single term relates to bottom of the funnel, because that's where your money is made."

**Apply at Pabau:** Pabau should periodically audit the ratio of educational/TOFU blog content to commercial pages (features, comparisons, pricing, integrations) and be deliberate about adding broad informational posts, since an imbalance may dilute the site's topical signal as 'practice management software' rather than a general healthcare-business blog.

**Apply anywhere:** Periodically audit the ratio of educational/TOFU blog content to commercial pages (features, comparisons, pricing, integrations) and be deliberate about adding broad informational posts, since an imbalance can blur the site's topical signal — making it read as a general industry blog rather than as a site about the product category you actually sell in.

### 6. Trade search volume for intent when the SERP shows the wrong searcher  `114.2`
*core · best practices · source 114*

Grow and Convert had a candidate term, 'blog post ideas', at an estimated 4,400 searches a month. They did not target it. Reading the top-ranking pages showed the SERP was filled with lists of blog post ideas, meaning the intent was to grab quick ideas rather than to learn a strategy. That reader profile is a beginner, likely starting a personal blog, and not a buyer for an agency retainer or a course. They targeted 'content ideation' instead, which has far less volume but attracts someone who wants the method. Their stated rule is that they will happily exchange search volume for search intent, and they determine intent by reading the SERP for the specific keyword rather than by guessing from the words. The reasoning is that their business model is not based on pageviews but on selling a service and a course to a defined audience.

> "We will happily exchange search volume for search intent"

**Evidence:** Grow and Convert passed on 'blog post ideas' at 4,400 monthly searches and targeted the lower-volume 'content ideation' instead.

**How to do it**

1. For every shortlisted keyword, open the SERP before you look at volume.
2. Read the top ten titles and classify the dominant format: listicle, definition, strategy explainer, tool page, comparison.
3. Write one sentence naming who wants that format, including their experience level and whether they buy anything.
4. Reject the term if that person is not your buyer, however high the volume.
5. Look for an adjacent phrasing of the same topic that pulls the buyer instead, as 'content ideation' does against 'blog post ideas'.
6. Check that the adjacent term's SERP is genuinely a different format, not the same listicles under another name.
7. Record the volume you gave up and the reason, so the choice is defensible when traffic reporting looks flat.
8. Judge the page on conversions per visit, not sessions, once it ranks.

**Tools:** Ahrefs

**Pitfall:** Marketers check volume and difficulty in the tool and never open the SERP, so they publish a strategy article into a listicle SERP. The signal is a page that ranks but has a bounce pattern and near-zero conversions.

**Apply at Pabau:** Pabau should apply this when picking between broad aesthetics terms and buyer terms. A high-volume term like 'clinic marketing ideas' pulls listicle readers, while a lower-volume term about switching software or managing patient records pulls someone evaluating a system.

**Apply anywhere:** Open the SERP before you commit to a keyword. If the ranking format serves a reader who will never buy, take the lower-volume phrasing that pulls a buyer instead, and defend the choice with conversions per page rather than sessions.

### 7. Treat a low-effort domain ranking top 10 as a winnability signal  `71.3`
*core · concrete actions · source 71*

Reviewing the SERP for 'AI content brief generator', Devesh noticed one of the ranking tools had not even bought a domain and was sitting on a Webflow subdomain, brieflygenerator.webflow.io. He reads that two ways at once. It is concerning, because every result is a free tool landing page and he intends to publish a blog post instead. But it also tells him the keyword may be so neglected that nonsense ranks, which means he can probably rank easily. He decides to proceed on that basis. The wider point is that the quality of the incumbents matters more than any difficulty score: a top ten that includes an unbranded subdomain, a thin page or an abandoned site is an opening.

> "didn't even buy their own domain"

**Evidence:** brieflygenerator.webflow.io ranked in the top 10 for 'AI content brief generator', which Devesh read as evidence the keyword was neglected enough to rank for easily.

**How to do it**

1. Pull the top 10 organic results for the target keyword and look at the domains themselves before looking at any difficulty score.
2. Flag any result on a free platform subdomain such as webflow.io, wixsite.com, notion.site or github.io.
3. Flag any result whose page is thin, undated or clearly abandoned.
4. Count the flags: two or more low-effort results in the top 10 means the keyword is neglected and winnable.
5. Separately check whether your intended page format matches the dominant format in the SERP, and note the mismatch as the real risk.
6. If the formats mismatch but the incumbents are weak, publish anyway and treat it as a test rather than a certainty.
7. Recheck the SERP eight to twelve weeks after publishing to see whether the format mismatch or the weak incumbents won.

**Tools:** Google

**Pitfall:** Weak incumbents do not cancel a format mismatch. Devesh notes that every result was a tool page while he was publishing a blog post, so the neglected-keyword read is a reason to try, not a guarantee.

**Apply at Pabau:** When Pabau targets aesthetic-practice software terms, David should scan the SERP for free-platform subdomains and abandoned pages before trusting a difficulty score, since those terms often have weak incumbents that keyword tools score as hard.

**Apply anywhere:** Look at who actually ranks before you trust a difficulty score. A free-platform subdomain or an abandoned page in the top ten means the keyword is neglected and you can probably take it.

### 8. Treat mini-volume comparison posts as days-to-rank low-hanging fruit  `95.3`
*core · concrete actions · source 95*

Matt Goolding checked historic ranking positions in Ahrefs for Circuit's mini-volume competitor comparison articles and found they ranked almost immediately. Route4Me Alternative hit position 2 within 7 days. Postmates vs Onfleet hit position 1 within 4 days. RoadWarrior Alternative hit position 4 within 30 days and later position 2. RoadWarrior vs Circuit hit position 1 within 3 days. All of them reached the top 5 in under 30 days. By contrast, Grow and Convert's articles targeting keywords with more than 1,000 monthly searches took 3 to 5 months to reach the top 3, and their published benchmark for a first piece on a new site is around 5 months. The mechanism is simple: low volume is unappealing to marketers, so the SERP has less competition.

> "Position 2 within 7 days"

**Evidence:** Circuit: Route4Me Alternative position 2 in 7 days, Postmates vs Onfleet position 1 in 4 days, RoadWarrior vs Circuit position 1 in 3 days; all top 5 within 30 days.

**How to do it**

1. Open Ahrefs Site Explorer for your own domain and go to Organic Keywords, then Position History for each published mini-volume page.
2. Record days from publication to first top-5 position for each page.
3. Do the same for your pages targeting keywords above 1,000 volume to get a contrast benchmark.
4. Sequence the next quarter's calendar so mini-volume comparison and alternatives pages ship first, ahead of the slow head-term pieces.
5. Check each candidate SERP manually for whether any result is a dedicated page on that exact term; if none is, expect a fast rank.
6. Publish and check position after 7 days rather than waiting the usual month.
7. If a page is not top 10 after 30 days, treat it as a competition problem and add internal links from pages that already rank.
8. Keep the head-term pieces running in parallel, since they need 3 to 5 months anyway.

**Tools:** Ahrefs

**Pitfall:** Fast ranking on an uncontested term makes teams assume all low-volume pages rank in a week. Terms where a competitor already has a dedicated comparison page behave like normal competitive keywords.

**Apply at Pabau:** Pabau should front-load competitor alternative and versus pages in the publishing queue because they return rankings within weeks, while broad terms like practice management software need months. That changes what gets written in the first sprint after a keyword refresh.

**Apply anywhere:** Put low-volume comparison and alternatives pages at the front of your publishing queue. They routinely reach the top 5 within 30 days, while head terms above 1,000 volume take 3 to 5 months.

### 9. Treat tool volume estimates on long-tail JTBD terms as 20x too low  `131.2`
*core · content insights · source 131*

Grow and Convert argue that Ahrefs and similar tools grossly underestimate long-tail volume, and they put a number on it from the Smartlook engagement. The phrase 'tracking user activity on website' showed 40 searches a month in Ahrefs. In the final nine months of the engagement, the page targeting it took nearly 7,000 organic sessions, roughly 20 times what the estimate implied. It was also one of their top 10 performers by conversion volume across all the content they produced. Their point is that many agencies skip these keywords precisely because the tool shows low monthly traffic, so the terms stay uncontested. The related point is that paid search cannot reach these queries either, because Google often does not show ads on them for lack of volume, which they say they have tested.

> "grossly underestimate the volume"

**Evidence:** 'tracking user activity on website' showed 40 searches/month in Ahrefs but produced nearly 7,000 organic sessions in nine months, about 20x the estimate, and was a top 10 converter.

**Tools:** Ahrefs

**Pitfall:** The failure is dropping a keyword because the tool shows 10 to 50 searches a month. The signal that you have hit it is a published page quietly pulling hundreds of sessions a month for a term your research file said was worthless.

**Apply at Pabau:** Pabau's keyword sheets should stop filtering on volume for problem-phrased queries. Terms like 'keeping track of client consent forms' or 'reminding patients about follow-up appointments' will show near-zero volume and still be worth a page, because that is how practice managers actually search.

**Apply anywhere:** Stop filtering long-tail, problem-phrased keywords on tool volume. Estimates on these terms run far below reality, and the low number is exactly why nobody else has built the page.

### 10. Triage the Ahrefs content gap report in three passes, not one  `118.1`
*core · concrete actions · source 118*

Grow and Convert walk through the mechanics of a competitor gap analysis on HiverHQ against Zendesk, Freshdesk and HelpScout. They open Ahrefs Site Explorer, paste their own domain, then use the Content Gap tool to add competitor URLs. The report returns pages and pages of keywords, so the work is the triage, not the export. Their triage runs in three passes: strike out obvious duds such as 'Uber customer service number' and the competitor's own branded terms; strike out top-of-funnel traffic keywords however tempting the volume; keep only keywords that map to one of their three buying-intent shapes. They say volume and difficulty columns help filter 'to a degree' but that search and buying intent outrank both. They admit the pass costs real time and argue that is the point, because it stops the team spending months writing content with no business potential.

> "Content gap" tool to add competitor URLs"

**Evidence:** Grow and Convert demonstrate the pass on HiverHQ, an unaffiliated help desk brand, against Zendesk, Freshdesk and HelpScout.

**How to do it**

1. Open Ahrefs Site Explorer and enter your own domain first so the gap is measured against what you already rank for.
2. Open the Content Gap tool and add the two or three competitors whose offering is closest to yours, not the biggest brands in the space.
3. Export the full report rather than reading it in the interface, so you can mark rows as you triage.
4. Pass one: delete competitor-branded terms and keywords for products or audiences you do not serve.
5. Pass two: delete high-volume top-of-funnel terms, even the tempting ones your competitor gets most of its traffic from.
6. Pass three: tag every surviving row as category, comparison/alternative, or jobs-to-be-done, and delete anything that fits none of the three.
7. Use the volume and keyword difficulty columns only to order the surviving rows, never to select them.
8. Budget a working day for the triage on a mature competitor set and treat that cost as cheaper than writing the wrong articles.

**Tools:** Ahrefs, Semrush, Moz

**Pitfall:** Teams run the report and paste the top rows straight into the content plan because the list is long and the volume column is the only easy sort. The signal you have done this is a plan whose top ten rows are the same ten head terms every competitor in the space already ranks for.

**Apply at Pabau:** David should run the Content Gap tool with Pabau against the two closest practice management competitors, not against large horizontal CRM brands, and triage into category, alternatives and JTBD buckets before anything reaches the blog calendar.

**Apply anywhere:** Run the content gap report against your closest competitors, then triage it in three passes: cut duds, cut top-of-funnel volume, and keep only rows that fit a buying-intent bucket.

### 11. Turn a clinician's most common recurring symptom into the target keyword  `117.7`
*core · concrete actions · source 117*

Grow and Convert did not find 'post-concussion headaches' in a keyword tool first. They found it in conversation with the doctors at Cognitive FX, who said headaches were one of the most common recurring, long-lasting symptoms of concussion, and that many patients had lived with them for years and described them as different from normal headaches. Only then did they check the tool, where 'what does a concussion headache feel like' showed 1,600 monthly searches in Ahrefs. That confirmed the topic fitted the ideal patient profile. The order matters: the clinician supplies the symptom that correlates with becoming a patient, and the keyword tool only validates that people search it. They rank #2 for that phrase, ahead of Mayo Clinic and the CDC.

> "headaches were one of the most common recurring, long lasting symptoms"

**Evidence:** 'What does a concussion headache feel like' gets 1,600 monthly searches per Ahrefs; the post ranks #2, above the Mayo Clinic and the CDC, and brought 32 leads in year one.

**How to do it**

1. Ask your clinicians which symptom or complaint most often precedes someone becoming a patient.
2. Ask how long people typically live with it before seeking treatment, and whether they describe it differently from the everyday version.
3. Write the phrasing patients use for that symptom as a candidate query.
4. Check the candidate and its variants in Ahrefs for volume; accept anything with real volume, even 1,600 a month.
5. Confirm the SERP is patient-facing rather than academic before committing.
6. Write the article against the clinician interview, not against the ranking pages.

**Tools:** Ahrefs

**Pitfall:** Running the tool first surfaces the condition name and misses the symptom phrasing, which is where the pre-patient sits.

**Apply at Pabau:** For Pabau, ask customer-facing staff which operational complaint most often precedes a clinic switching software, then check that phrasing in Ahrefs before writing.

**Apply anywhere:** Get your target keyword from the experts who talk to customers daily. Ask which recurring problem precedes a purchase, then use the keyword tool only to confirm people search that phrasing.

### 12. Turn each solved customer pain point into a dedicated ranking page  `102.4`
*core · concrete actions · source 102*

Grow and Convert use pain points twice. First, as a keyword source: list the challenges you solve, then look for search terms that indicate the searcher has that challenge, and build a dedicated page to rank for the term. Their example is a book ghostwriting client whose customers worried about whether their book idea was original. They found keyword opportunities around that worry and created one piece of content aimed at ranking for it, reasoning that if a decent share of customers ask that question, some fraction of the searchers are ready to become customers. Second, they use pain points inside every article, to open by showing the reader their problem is understood and then to explain in depth how the product solves it. They point to their Pain Point SEO article for the frameworks.

> "these pain points can inform the topics and keywords"

**Evidence:** A book ghostwriting client: the pain point was whether the customer's book idea was original, and Grow and Convert built a dedicated page to rank for the matching terms.

**How to do it**

1. List the pain points your product removes, one per row, phrased as the customer would say it.
2. For each, search for the query a person in that state would type, and pull the variants from a keyword tool.
3. Keep the variants that only someone with that pain point would search, and drop generic category terms.
4. Build one dedicated page per kept pain-point query rather than folding several into a hub.
5. Open that page by naming the pain point and its consequence, before any definition.
6. Inside the page, explain specifically how your product resolves that pain point, then place the call to action.
7. Track conversions per pain-point page, and expand the ones that convert into adjacent variants.

**Pitfall:** Writing about the pain point in the abstract without targeting a query someone actually types, so the page ranks for nothing and only serves existing readers.

**Apply at Pabau:** Pabau should mine support and onboarding tickets for practice pain points such as no-shows, consent-form handling and stock counts, and build one article per pain-point query rather than one long practice-management guide.

**Apply anywhere:** Mine your support and sales conversations for the exact worries customers voice, find the query each worry produces, and build one dedicated page per worry. Use the same pain point to open the page and to justify the product later on.

### 13. Turn product attributes into pain-point keywords using PAA and suggest  `112.5`
*core · concrete actions · source 112*

Grow and Convert show the ideation loop for pain-point keywords by reading the product page and inverting each quality into the worry it answers. For Truwild's pre-workout they list: worries about pre-workout being bad for you, jitters from a current pre-workout, uncertainty about ingredients, wanting a plant-based option, needing gluten-free, and crashing after use. Each of those goes into Clearscope, Google Suggested Search, Google Related Searches and People Also Ask, and the questions that come back become article targets. The jitters pain point surfaces 'how do you get rid of jitters from pre-workout', which the brand can answer by explaining why pre-workouts cause jitters and presenting its alternative. They argue these still convert far better than top-of-funnel terms, because nobody searches 'can vegans take pre-workout' unless they are a vegan interested in buying one.

> "we'd start searching for these terms in the various tools we use"

**Evidence:** Grow and Convert estimate the pain-point and use-case loop together yields an additional 50-100+ keywords for a single supplement brand.

**How to do it**

1. List the qualities the product page advertises, plant-based, no crash, gluten-free, clean ingredients.
2. Invert each quality into the customer worry it answers and write that worry as a sentence.
3. Type each worry into Google and record the Suggested Search completions and Related Searches.
4. Open the People Also Ask box on each result and record every question it expands into.
5. Run the same phrasings through Clearscope to confirm demand and find sibling terms.
6. Keep only questions where your product is a credible answer, not general category education.
7. Outline each article as: why the problem happens, what causes it, then your product as the alternative.
8. Repeat the whole loop separately for each product line's own pain points.

**Tools:** Clearscope, Google Search Console

**Pitfall:** Pain points that your product does not actually solve produce articles with no natural place to introduce it, and those revert to top-of-funnel performance. Drop any worry you cannot answer with the product.

**Apply at Pabau:** Pabau's feature list inverts cleanly into practice-owner worries: no-shows, lost paper records, staff scheduling clashes, insurance claim rejections. David should run each through People Also Ask and build the article as cause, explanation, then Pabau as the fix, which is exactly the structure the Pabau section before the Conclusion already expects.

**Apply anywhere:** Read the qualities off your product page, invert each into the customer worry it answers, then run those worries through Google Suggest, Related Searches and People Also Ask. Build an article per question that explains the cause and presents your product as the alternative.

### 14. Turn the disqualifying customer criterion into the keyword filter  `137.9`
*core · concrete actions · source 137*

The key discovery in Grow and Convert's Cognitive FX research was that the ideal patient is defined by lingering symptoms, not by a recent injury. If symptoms have not gone away or have worsened over time, and they interfere with daily life, the person is a fit. Cognitive FX is not a replacement for the emergency room or a first call to a primary care doctor. That single criterion became the keyword filter. It is why they targeted 'what does a concussion headache feel like' at 1,600 searches a month and 'multiple concussions' at 600, rather than acute-injury terms with far more volume. The strategic bet they name is that the act of searching for that specific article by itself indicates a more qualified potential customer.

> "The key discovery about their ideal patient profile is"

**Evidence:** Filtering on lingering symptoms led to 'what does a concussion headache feel like' (1,600 a month), which produced 32 leads in its first year, and 'multiple concussions' (600 a month), which produced 91 conversions.

**How to do it**

1. In the kickoff interviews, ask directly which customers the business is not for and why.
2. Write the one criterion that separates a qualified buyer from an unqualified one, in the customer's own language.
3. Generate keyword candidates that only someone meeting that criterion would type, such as duration, recurrence or failed-treatment phrasing.
4. Discard candidates that a disqualified person would search just as readily, even at higher volume.
5. Test each survivor by asking whether searching it, by itself, proves the person is qualified.
6. Check volume in Ahrefs last, and accept terms in the hundreds per month if the qualification test passes.
7. Confirm after six months by comparing conversion rates across the qualified and unqualified terms you published.

**Tools:** Ahrefs

**Pitfall:** Teams write the ideal customer profile as a demographic description, which produces no keyword filter at all. You need the behavioral criterion that a search query can reveal.

**Apply at Pabau:** For Pabau the equivalent criterion is a practice that has outgrown paper or spreadsheets, so David should target queries only that owner types, such as problems with double-booking, no-show rates or consent-form chasing, rather than generic clinic-management terms.

**Apply anywhere:** Find the one behavioral criterion that separates a qualified buyer from an unqualified one, then keep only keywords that a person meeting that criterion would search and an unqualified person would not.

### 15. Use how-to task keywords as the main volume source for a new category  `135.6`
*core · concrete actions · source 135*

When the innovation itself has almost no search demand, Grow and Convert move up one level to mid-funnel how-to keywords describing the task their product performs. They call these their bread and butter for innovative products, because the searcher has the problem but has not settled on any product, which is exactly when a new solution can be introduced. Their example is 'how to edit an interview video'. That searcher is probably a researcher or a marketer, almost certainly not a professional editor, because a professional would not search it. They expect articles about Adobe or iMovie, which is the opening: the post names those tools, explains why they are wrong for someone without editing experience, then introduces the new method. These terms convert less than bottom-funnel terms but far more than broad category terms.

> "style keywords are our bread and butter"

**Evidence:** Grow and Convert report mid-funnel pain-point keywords averaged a 1.06% conversion rate against roughly 0.5% for top-of-funnel terms.

**How to do it**

1. Write out the tasks your product completes, phrased as the task not the product, for example 'edit an interview video'.
2. Prefix each with 'how to' and check volume; keep terms specific enough that the searcher's situation is visible in the phrasing.
3. For each term, write one sentence naming who searches it and one naming who does not, such as 'a professional editor would never search this'.
4. Drop any term where the searcher would plausibly already own a tool for the job.
5. Confirm the term implies your product's precondition, for example that interview video means dialogue-heavy footage.
6. Open the post by naming the tools the searcher expects to be recommended and why they are wrong for this person.
7. Then teach the task using your product as the method, with enough detail that no other resource is needed.
8. Segment reporting so mid-funnel how-to posts are measured against their own conversion benchmark, not the bottom-funnel one.

**Tools:** Ahrefs

**Pitfall:** Choosing how-to terms so broad that the searcher's situation is invisible, such as 'video editing'. Those readers may be students or hobbyists, and the post converts at roughly a fifth of the rate.

**Apply at Pabau:** Pabau should build how-to posts for tasks a practice does badly by hand: how to run a clinic rota across two locations, how to chase no-shows, how to store consent forms for injectables. Each teaches the task with Pabau as the method.

**Apply anywhere:** When your innovation has no search demand, move up one level to 'how to [task]' keywords describing what your product does, keeping them specific enough that the searcher's role and situation are visible in the phrase.

### 16. Validate GSC page-two impressions against actual page content  `16.10`
*core · concrete actions · source 16*

For choosing keywords to add to an existing page, the process starts in Google Search Console: look for search terms the page already gets impressions for, particularly ones sitting around "page two" (roughly positions 11-20) that don't yet appear in the page's title tag or any heading — that gap is read as a strong signal the page could rank for the term if optimized for it. The explicit caveat is not to trust GSC data alone, since it contains "irrelevant terms... that aren't actually what the page is about"; the term must also be checked against what the page genuinely covers before optimizing for it. This combines a quantitative signal (existing impressions/position) with a qualitative check (actual page relevance) rather than relying on either alone.

> "showing up on page two for a term, and that term isn't"

**How to do it**

1. Open Google Search Console and go to Performance > Search Results, filtered to the specific existing page URL.
2. Review the Queries table for terms already generating impressions on that page.
3. Identify candidate terms sitting around position 11-20 (page two) that do not yet appear in the page's title tag or any heading.
4. Cross-check each candidate term against the page's actual content and topic, discarding terms that show impressions but aren't genuinely what the page is about.
5. Have a person (or Claude, given the page content and the GSC export together) make the final relevance call rather than automating on GSC data alone.
6. For terms that pass both filters, add the term into the title tag or a heading on the page.
7. Re-check GSC performance for that page after the change to confirm the term climbs from page two toward page one (inferred verification step).

**Tools:** Google Search Console

**Pitfall:** Optimizing for any term simply because GSC shows impressions is a mistake — GSC data includes irrelevant/noise terms that aren't truly what the page is about, so relevance must be verified against the actual content before targeting a term.

### 17. Weigh volume against a 10X conversion premium on bottom-funnel terms  `115.1`
*core · concrete actions · source 115*

Grow and Convert put real numbers on the trade between top- and bottom-funnel keywords using a B2B SaaS client selling operational software to HVAC, plumbing and electrical companies. Their traffic-focused examples were 'HVAC business' at 720 searches a month, 'electrician salary' at 33,100 and 'plumbing leads' at 720. Their leads-focused examples were 'HVAC software compatible with QuickBooks' at 50, 'electrical bidding software' at 260 and 'plumbing invoice app' at 50. The 50-a-month term looks 660 times worse on volume than 'electrician salary'. They say in their experience keywords like the second set convert more than 10X higher than the first, because the searcher is in buying mode for exactly the product being sold. So the comparison to run is not volume against volume, it is volume times an assumed conversion multiple, and a 10X multiple flips most of these pairs.

> "can often convert more than 10X higher than the ones above"

**Evidence:** Grow and Convert's HVAC client: 'electrician salary' at 33,100 searches a month against 'HVAC software compatible with QuickBooks' at 50, with the low-volume terms reported to convert more than 10X higher.

**How to do it**

1. Split your candidate keyword list into two columns: terms that describe a buyer looking for your product type, and terms that merely interest your audience.
2. Pull estimated monthly volume for both columns in Ahrefs so the gap is explicit rather than assumed.
3. Apply a 10X conversion multiplier to the buying-intent column and a 1X to the other before ranking anything.
4. Rank the combined list by volume times multiplier, not by raw volume.
5. Accept terms as low as 50 searches a month when they name your product category plus a qualifier, an integration or a job.
6. Commission the top of that ranked list first and leave the high-volume column for a later phase.
7. After six months, record conversions per article by target keyword and replace the assumed 10X with your own measured multiple.
8. Re-rank the remaining backlog using the measured multiple.

**Tools:** Ahrefs

**Pitfall:** Teams run the multiplier in their heads and still pick the 33,100-volume term because the traffic forecast looks better in a plan. The signal is a content calendar where every item has four-figure volume and no item names the product category.

**Apply at Pabau:** David should build the Pabau keyword sheet with a conversion multiplier column so a 40-a-month term like 'aesthetic clinic software with Stripe payments' outranks a 5,000-a-month term like 'botox aftercare'. The high-volume aesthetics topics stay on the list, just in a later phase.

**Apply anywhere:** Score keyword candidates on volume times an assumed conversion multiple rather than volume alone. Buying-intent terms can convert around ten times better, which makes a 50-search-a-month product term worth more than a 30,000-search informational one. Replace the assumption with measured conversions per article once you have six months of data.

### 18. Weight mini-volume keywords by contract value, not by traffic  `95.7`
*core · best practices · source 95*

Matt Goolding makes the case that a high price point makes mini-volume keywords more important, not less. For a marketing agency client, Grow and Convert targeted a B2B SaaS keyword showing 0 to 10 monthly volume. Since publication in September 2021 the post drove 7 organic inquiries and 2 paid inquiries via Google Ads, and with contract sizes in the tens of thousands of dollars that is comfortably worth the article. The same held for an enterprise digital asset management client whose alternatives post generated 11 signups on a non-self-serve, high price point product. He notes it also works in B2C: a competitor keyword for a company selling excessive sweating treatment showed 10 monthly searches and the post generated 15 monthly subscriptions over 12 months. The screening figure is revenue per conversion, not sessions.

> "With contract sizes in the tens of thousands of dollars"

**Evidence:** Marketing agency client: 7 organic and 2 paid inquiries from a 0 to 10 volume keyword, against contract sizes in the tens of thousands of dollars.

**How to do it**

1. Get the average contract value or lifetime value per closed deal from finance or sales.
2. Set the minimum conversions a page must produce to pay for itself: article cost divided by value per conversion.
3. For most high-ticket businesses this lands at one or two conversions, which a mini-volume page clears.
4. Screen every candidate keyword against that conversion threshold rather than against a volume floor.
5. Delete any volume minimum from the keyword brief template and replace it with the conversion threshold.
6. Attribute inquiries by landing page so single-digit conversion counts are visible in reporting.
7. Include paid inquiries that land on the same page, since the asset serves both channels.
8. Review annually and raise the threshold only if production costs rise.

**Pitfall:** Low-ticket or ad-funded sites cannot use this rule. If revenue per conversion is a few dollars, a page producing 7 inquiries a year genuinely does not pay for itself.

**Apply at Pabau:** Pabau sells subscription software with meaningful annual value per practice, so a page producing a handful of demo requests a year pays for itself. That justifies building narrow pages for specific treatment types and practice models that no volume filter would approve.

**Apply anywhere:** Set your keyword floor in conversions needed to pay back the article, using your average deal value, rather than in monthly search volume. High-ticket businesses clear that bar with a handful of inquiries a year.

### 19. Work deviant keywords only after the three core Pain Point groups  `109.2`
*core · concrete actions · source 109*

Grow and Convert set an explicit sequence for their Pain Point SEO program. Category keywords first, then comparisons and alternatives, then jobs-to-be-done, and only then the deviant variants inside each of those three groups. The reason is intent density. Most deviant keywords behave as mid-funnel: either the buying intent is inherently lower, or the searcher pool is mixed, with some ready to buy and some not. Spending early budget there costs conversions you could have had from the obvious bottom-of-funnel terms. The author names one exception. Deviants inside the category group, specifically inaccurate descriptions of the product, can be the highest-intent keywords on the whole list, because the searcher is ready to buy and has only got the terminology wrong. Those jump the queue.

> "Targeting deviant keywords usually makes sense when you've already covered"

**Evidence:** Grow and Convert's stated prioritization order across client programs, with inaccurate-description category deviants named as the exception that can be highest intent.

**How to do it**

1. Build four keyword lists: category, comparisons and alternatives, jobs-to-be-done, and deviants.
2. Publish every category keyword page first, since these searchers want your product type now.
3. Move to comparison and alternative pages, including competitor-name terms.
4. Work the jobs-to-be-done list next, one page per task the customer is trying to complete.
5. Pull deviant category keywords forward out of turn when the deviance is only wrong terminology for the same buying intent.
6. Hold the remaining deviants, treat them as mid-funnel, and start them once the three core lists are published.
7. Track conversions per published page so you can tell when core-list returns have flattened.
8. Revisit the order if a deviant term shows conversion rates matching your category pages.

**Pitfall:** Teams find deviant keywords novel and start there because they are more interesting to write. That leaves the highest-converting obvious terms unclaimed while a rival takes them.

**Apply at Pabau:** Pabau should finish the plain category and comparison pages before commissioning deviant-keyword articles. The exception applies: if aesthetic practice owners search a wrong-but-common phrase for practice management software, that page moves to the front of the queue, not the back.

**Apply anywhere:** Sequence your keyword program: category terms, then comparisons and alternatives, then jobs-to-be-done, then the unusual variants within each. The one exception is a wrong description of your own product category, which is often the highest-intent term you have and should be published early.

### 20. Write alternatives and versus pages before general category pages  `142.2`
*core · concrete actions · source 142*

The single most surprising finding in Grow and Convert's study is that comparison and alternative keywords convert better than any other type, at 8.43% average, above even main category keywords at 4.85%. Versus keywords in the form Brand A vs Brand B averaged 5.45%. Their explanation is that these searchers already know the industry, already know the competitors, and are actively comparing solutions with a purchase in mind. They warn the spread is wide: across the 23 competitor and alternative keywords analyzed, most posts converted at under 4%, and the closer the named competitor is to a direct rival, the higher the rate. They also note many of these terms have very low search volume, and argue the conversion rate makes them worth targeting anyway.

> "the majority of these posts convert at less than 4%"

**Evidence:** 8.43% average across 23 competitor and alternative keywords, versus 5.45% for versus keywords and 4.85% for main category keywords.

**How to do it**

1. List every competitor a prospect actually shortlists you against, taken from sales call notes and lost-deal reasons.
2. Rank that list by how directly each product substitutes for yours, closest first.
3. Create one '[Competitor] alternatives' page per name, starting at the top of the ranked list.
4. Create '[You] vs [Competitor]' and '[Competitor] vs [Competitor]' pages for the same set.
5. Ignore search volume as a filter here; accept terms with double-digit monthly volume.
6. Put a side-by-side feature and pricing table on each page and state plainly who each tool suits.
7. Measure conversion per page after 90 days and expect a wide spread, with a few pages carrying the average.

**Pitfall:** Targeting loosely related competitors to inflate the page count. Grow and Convert found keywords naming distant competitors convert far worse than those naming direct rivals.

**Apply at Pabau:** Pabau should have a dedicated alternatives page for each aesthetic and healthcare practice software it is compared against, plus versus pages, even where the monthly volume looks negligible. These belong ahead of another broad 'best clinic software' post.

**Apply anywhere:** Build a dedicated alternatives page for every product you are genuinely compared against, plus versus pages, even when monthly volume looks negligible. These belong ahead of another broad category listicle.

### 21. Write comparison posts even when tools report zero search volume  `90.3`
*core · concrete actions · source 90*

Grow and Convert report that the single highest-converting blog post in one client's analytics targeted a comparison keyword that Ahrefs and Moz both showed as having zero search volume. It had the lowest traffic of any post in the report and still produced more conversions than any other. They repeat the point deliberately because most marketers see a zero and move on. The mechanism is that comparison and alternatives queries are searched by people already choosing between products, so a handful of visits a month can convert at rates an order of magnitude above a traffic post. Volume tools sample clickstream data and simply do not register long-tail phrasings that real buyers type. Grow and Convert call these mini-volume keywords and treat a zero reading as no information rather than as evidence of no demand.

> "showed as having zero search volume"

**Evidence:** The post with the largest number of conversions in Grow and Convert's client screenshot targeted a keyword that Ahrefs and Moz both reported at zero volume.

**How to do it**

1. List every competitor your sales team names, then generate '[you] vs [competitor]' and '[competitor] alternatives' for each.
2. Run the list through Ahrefs or Moz but do not filter out the zero-volume rows.
3. Search each zero-volume phrase manually and check whether real pages exist that target it; existing pages prove someone is searching.
4. Confirm buying intent by checking whether the results are vendor pages, review sites or listicles rather than definitions.
5. Publish the post anyway for any phrase where a competitor is named, regardless of the reported figure.
6. Set up conversion tracking on that page before publishing so you can judge it on signups rather than sessions.
7. Review after 90 days on conversions per month, not pageviews, and keep any page producing signups at single-digit traffic.
8. Feed the winners back into the list by generating further variants of the same competitor pairing.

**Tools:** Ahrefs, Moz

**Pitfall:** Judging the page after launch on traffic will kill it. A page with 40 sessions a month and four signups looks like a failure in a traffic report and is the best page on the blog in a conversion report.

**Apply at Pabau:** Pabau should build a vs and alternatives page for every competitor named by sales, including ones that DataForSEO returns no volume for. Judge these pages on demo requests, not sessions.

**Apply anywhere:** Build a comparison or alternatives page for every competitor your buyers name, even when your keyword tool reports zero volume, and judge each page on signups rather than sessions.

### 22. Write pain points at problem level, not at topic level  `110.11`
*core · best practices · source 110*

Grow and Convert insist the pain points behind pain point SEO are specific, not general. Their contrast for the Pipedrive example is 'getting more of my sales reps to update the CRM' rather than 'sales tips'. The mechanism is filtering. The more specific the topic, the more the topic itself screens for people who look like your best customers and have the exact pain your product solves, and therefore the more likely they are to convert. Generality does the opposite: a broad topic attracts everyone with a loose interest in the industry and leaves the filtering to chance. So the specificity of the pain point statement, written before any keyword tool is opened, sets the ceiling on the conversion rate of everything built from it.

> "These pain points are specific, not general"

**Evidence:** Grow and Convert's worked contrast for a CRM: 'Getting more of my sales reps to update the CRM' rather than 'sales tips'.

**How to do it**

1. Write each pain point as a sentence a customer would say out loud, in the first person.
2. Reject any pain point that could be said by someone who would never buy your product.
3. Include the actor and the blocked outcome, as in 'getting more of my sales reps to update the CRM'.
4. Test each one against a real customer quote from research; discard the ones you invented.
5. Only then search for keywords that match the pain point wording.
6. Score each resulting keyword on how tightly it screens for your best customer, and drop the loose ones.
7. Keep the pain point sentence at the top of the brief so the writer stays at that level.

**Pitfall:** Rounding a specific pain point up into a topic label. 'Getting reps to update the CRM' becomes 'CRM adoption' becomes 'sales tips', and each step up costs conversion rate.

**Apply at Pabau:** Pabau briefs should carry a first-person pain point sentence from a practice owner, such as getting front-desk staff to record consent forms consistently. That sentence, not a topic label, drives the keyword search for pabau.com articles.

**Apply anywhere:** Write pain points as first-person sentences naming the actor and the blocked outcome, and reject any that a non-buyer could also say. Search for keywords only after the pain point is that specific, and keep the sentence at the top of the brief.

### 23. Write pain-point keywords in the customer's own problem phrasing  `120.11`
*core · concrete actions · source 120*

Grow and Convert's third buying-intent category is pain point keywords, phrases showing the searcher has a problem the product solves. Their published examples show the phrasing is literal customer language, not category vocabulary: 'how to edit video fast' for Reduct, 'who is visiting my site' for Leadfeeder, 'keep track of staff holidays' for Timetastic, and 'how do I know if I need an executive assistant' for Persona Talent. Two of the resulting titles name the workaround being replaced, such as keeping track of staff holidays without clumsy spreadsheets, or identifying B2B leads that never fill out a form. That framing catches the reader at the moment they are trying to solve the problem and gives a natural place to present the product. They stress this category depends on deep customer understanding rather than tool output.

> "indicate the person searching has a problem"

**Evidence:** Grow and Convert's client pain point targets included 'keep track of staff holidays' for Timetastic and 'who is visiting my site' for Leadfeeder, each with a published article behind it.

**How to do it**

1. Interview sales, customer success and the executive team for the problems customers describe before buying.
2. Write each problem down in the customer's words, keeping the verb they use: keep track of, know if, figure out.
3. Convert each into a search phrase without adding your product category to it.
4. Check each phrase in Ahrefs and in Google autocomplete, and keep it even at very low volume.
5. Confirm the problem is one your product genuinely resolves, or drop the phrase.
6. Title the article with the phrase plus the workaround it replaces, such as 'without clumsy spreadsheets'.
7. Place the product as the solution inside the article, at the point the problem is diagnosed, not only at the end.
8. Track conversions per pain point page and expand around the problems that convert.

**Tools:** Ahrefs, Google

**Pitfall:** Sourcing pain points from a keyword tool's related terms produces category vocabulary, not problem vocabulary. The tell is a list of 'benefits of X' phrasings, which convert like any other informational post.

**Apply at Pabau:** Pabau's pain point list should read like practice owners talk: 'stop patients no-showing', 'keep track of consent forms', 'how do I know if I need practice management software'. Source it from Pabau support tickets and sales calls.

**Apply anywhere:** Collect the problems customers describe before buying, in their own words, and turn each into a search phrase without your category name in it. Title the article with the phrase plus the clumsy workaround it replaces.
