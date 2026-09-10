# Keyword Research — core (part 4 of 7)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Mine fan-out queries to match how AI researches answers  `07.7`
*core · concrete actions · source 07*

Fan-out queries are the sub-questions a generative engine silently asks itself before synthesizing a final answer — e.g., asking ChatGPT 'should I install an EV charger at home?' triggers internal follow-ups like installation cost, permit requirements, and installer options, which the model researches before responding. These internal queries are normally invisible, but a DataForSEO-backed tool (Datawise) can surface them directly, returning a full list with per-query AI volume, total volume, and trend (195 queries in the worked example). Capturing and answering these sub-questions inside your content is a direct lever on getting cited, because you're pre-answering exactly what the AI is going to research anyway. The data is currently limited to United States/English queries, so treat it as directionally useful rather than complete for other markets.

> "questions the AI search engines ask themselves internally"

**How to do it**

1. In Datawise (or an equivalent DataForSEO-backed tool offering fan-out data), go to Keyword Research and select your seed transactional keyword.
2. Click 'Fan-out queries' and set location to United States and language to English, since that is currently the only reliably supported combination.
3. Review the returned list of sub-questions, each shown with an AI volume, total volume, and trend.
4. Discard any queries that are clearly irrelevant or nonsensical for your business.
5. Download the full fan-out query list as a CSV, even without manually vetting every row.
6. Upload the CSV into your ChatGPT/Claude project sources alongside your people-also-ask export.
7. When later drafting content, explicitly instruct the AI to ensure every relevant fan-out sub-question is answered somewhere in the piece.
8. Repeat this process for every seed/service keyword. (inferred: re-pull fan-out data periodically since the creator notes these queries 'will change quite substantially' over time)

**Tools:** Datawise, DataForSEO, ChatGPT, Claude

**Pitfall:** Assuming fan-out coverage exists for your market — the data is explicitly limited to U.S./English queries today ('if you're speaking Spanish or another language, I'm sorry'), so non-U.S. teams should treat it as directional signal, not complete coverage.

### 2. Mine paid service delivery for the problems that become product content  `170.2`
*core · concrete actions · source 170*

Campbell argues the heavy services phase was the real advantage, not a detour. 'We were learning more about these companies than anyone else,' he says, and 'we would not have learned what we needed to learn if we did not do the more heavy services.' The key point for anyone doing research is that the learning came from being inside the client's numbers while being paid, not from a survey sent to strangers. The product idea for ProfitWell came out of that access: sitting in a client's boardroom, and repeatedly failing to get clean financial data out of Google Analytics or a client's CRM. Both observations were only available to someone doing the work.

> "It was an incredible customer development opportunity"

**Evidence:** Campbell: 'We were learning more about these companies than anyone else.' The ProfitWell product idea came directly from service delivery observations.

**How to do it**

1. List every paid engagement your team runs where you touch the customer's own systems or data.
2. Add a standing five-minute debrief at the end of each engagement, capturing what the client got wrong and what data was hard to get.
3. Keep the debriefs in one shared sheet with columns for client, problem, and how often you have seen it before.
4. Flag any problem seen three or more times as a candidate topic or product feature.
5. Check each flagged problem for search demand, but do not drop it if volume is zero — a repeated real client question proves demand.
6. Write the article or page in the client's own words from the debrief, not in industry jargon.
7. Review the sheet quarterly and retire problems that stop recurring.

**Tools:** Google Analytics

**Pitfall:** Teams that outsource delivery early lose this channel entirely. If nobody on the strategy side has touched a live client account in six months, the problem log stops refreshing and topic selection reverts to keyword tools.

**Apply at Pabau:** Pabau's support and onboarding teams see what aesthetic practices actually get wrong every day. David should run a monthly export of support tickets, cluster them by problem, and let the top clusters set the blog and template queue instead of tool-generated keyword lists.

**Apply anywhere:** Your support and delivery teams sit on the best topic research you will ever get. Debrief every engagement, log recurring client problems in one sheet, and let anything seen three times or more set the content queue.

### 3. Mine your own product page copy for long-tail keyword modifiers  `112.3`
*core · concrete actions · source 112*

Grow and Convert's starting point for keyword expansion is not a tool but the client's own product page. Working through the Truwild supplement example, they say they would begin with the specific keywords already on the hydration product page, terms like amino acids, electrolytes and no sugar. Those attributes are hints at long-tail opportunities, and people searching for a hydration drink with those specific qualities are a closer match to the product than people searching the general category term, which produces higher conversion rates. They then combine the product term with each attribute and check what surfaces in Clearscope: 'amino acids drink mix', 'sports drink with amino acids', 'amino acids with electrolytes', 'no sugar hydration drink', 'no sugar hydration powder', 'best no sugar sports drink'. Anything the product page is not already ranking for becomes a target.

> "we'd likely start with the specific keywords that they have included on their product page"

**Evidence:** Grow and Convert generated over 10 bottom-of-funnel keyword opportunities from a single Truwild product page, and estimated 50-100+ across the four product lines.

**How to do it**

1. Open the product page and copy out every attribute, ingredient, format and qualifier used to describe it.
2. Write each one as a modifier next to the generic product noun, for example 'hydration drink with amino acids'.
3. Run every combination through Clearscope or your keyword tool and record the related terms it returns.
4. Check current rankings for each term; discard any the product page already ranks in the top 10 for.
5. Keep the rest as targets, weighting the ones whose attribute is a genuine differentiator for your product.
6. Repeat the whole loop for every product line rather than only the flagship one.
7. Group near-duplicate terms so you build one page per intent, not one page per phrasing.

**Tools:** Clearscope

**Pitfall:** Attributes that every competitor also claims produce terms with no differentiation, so the page has nothing to say. Keep the modifiers where your product genuinely differs.

**Apply at Pabau:** Pabau's feature pages already list attributes: online booking, medical records, e-prescriptions, HIPAA compliance, iOS app. David should combine each with the category noun and check demand, since 'practice management software with online booking' style terms are exactly the long-tail purchase-intent pages the site does not yet have.

**Apply anywhere:** Read the attributes off your own product page, pair each with the generic product noun, and run the combinations through a keyword tool. The terms you do not already rank for are your long-tail purchase-intent list, and the closest matches convert better than the category head term.

### 4. Mine your paid search account for keywords that already convert  `114.5`
*core · concrete actions · source 114*

Grow and Convert call this their favorite shortcut for anyone already running Google Ads, because it skips the guesswork in keyword research: you already know these terms convert. In Google Analytics with conversion goals configured, open the Model Comparison Tool, click into the paid search channel, then add keyword as a secondary dimension. That produces a list of search terms with the number of conversions each one drove. Take those terms into Ahrefs, Moz, SEMrush or Google Keyword Planner to read difficulty, then prioritize by the combination of easiest to rank and highest conversion volume. The stated goal is to build organic posts that rank for the terms you are currently paying for, so the dependence on ad spend falls over time and the same leads arrive free. They recommend this specifically to content consultants and agency owners as a way to produce high-converting topics fast.

> "you can open up the model comparison tool"

**Evidence:** Grow and Convert use this to shortcut keyword research entirely, on the basis that the conversion data already proves the intent.

**How to do it**

1. Confirm conversion goals are configured in Google Analytics before you start.
2. Open the Model Comparison Tool and click into the paid search channel.
3. Add keyword as a secondary dimension to get search terms against conversions.
4. Export the list and drop any term with zero conversions.
5. Run the surviving terms through Ahrefs, Moz, SEMrush or Google Keyword Planner for difficulty.
6. Score each term on two axes: ranking difficulty and conversions already recorded.
7. Publish first against terms that are low difficulty and high converting.
8. Track organic rank for each published term and lower the paid bid on that term once the page holds a top position.
9. Re-run the export quarterly to catch newly converting terms.

**Tools:** Google Analytics, Google Ads, Ahrefs, Moz, SEMrush, Google Keyword Planner

**Pitfall:** Pulling the paid keyword list without conversion data attached just gives you the terms someone chose to bid on, not the ones that work. The signal is a content queue full of head terms that spend heavily and convert nobody.

**Apply at Pabau:** If Pabau runs Google Ads, David should export the converting search terms and build /blog/ or template pages for each. Terms that pay for demo bookings today are the safest organic bets and eventually cut the ad bill.

**Apply anywhere:** Export your paid search terms with conversions attached from Google Analytics, check difficulty on each, and build organic pages for the low-difficulty high-conversion ones. Reduce the bid on any term once the organic page ranks.

### 5. Multiply category keywords across use cases, verticals, sizes and integrations  `103.1`
*core · concrete actions · source 103*

Grow and Convert treat software category keywords as a matrix, not a list. Start from 'best X software', '[use case] software' and '[industry] software', then build the crosses: '[industry] + [use case] software', '[use case] software for [industry]', '[industry] software for [use case]'. Their client TapClicks has four use cases (analytics, reporting, workflow, order management) and three verticals (agencies, media companies, retail brands), which yields 12 keywords from that one variation alone. They then substitute 'tools' and 'apps' for 'software', and add modifiers for integrations and business size, giving 'best [use case] tools', 'best [use case] software for [integration]' and '[use case] software for [business size]' such as SMB or enterprise. The filter they apply is two-part: the client must not already rank, and the SERP must not overlap with a keyword they have already targeted or plan to target.

> "especially if you have a large feature set"

**Evidence:** TapClicks: four use cases times three verticals produced 12 candidate keywords from a single variation pattern.

**How to do it**

1. List every product use case in one column and every vertical, business size and named integration in another.
2. Cross-multiply into '[industry] + [use case] software', '[use case] software for [industry]' and '[industry] software for [use case]'.
3. Duplicate the whole list three times, swapping 'software' for 'tools' and then 'apps'.
4. Add modifier rows for each integration ('best [use case] software for [integration]') and each business size (SMB, enterprise).
5. Check volume for every variant in Ahrefs, but keep zero-volume rows that name a real buyer situation.
6. Drop any variant where the client already ranks on page one.
7. Search each surviving variant and drop it if the top 10 substantially overlaps a keyword you have already targeted or scheduled.
8. Order what is left by closeness to the product's differentiators and assign one article per row.

**Tools:** Ahrefs

**Pitfall:** Teams build the matrix and then publish near-duplicate articles for two variants whose SERPs are the same. That splits authority and creates cannibalization before the first page ranks.

**Apply at Pabau:** Pabau should build this matrix properly: use cases (booking, charting, invoicing, inventory, marketing) crossed with medical spa, dermatology, aesthetics and multi-site groups, then repeated with 'tools' and 'apps' and with integration modifiers like Stripe or Xero. Run the SERP overlap check before commissioning, because several of those variants will return the same results page.

**Apply anywhere:** Build category keywords as a matrix: use cases crossed with industries, business sizes and integrations, repeated with 'software', 'tools' and 'apps'. Then drop any variant whose SERP duplicates one you already target.

### 6. Multiply features by industries to build a 200-keyword bottom-funnel list  `130.1`
*core · concrete actions · source 130*

Grow and Convert argue that all-in-one software changes the arithmetic of pain point SEO. A point solution may have 5, 10 or 50 high-buying-intent keywords. A feature-rich platform often has 200 or more, because every feature carries its own software, app and long-tail variations, and every one of those can be repeated for each industry the product serves. Their client had 100-plus features and served 20-plus industries. They say the opportunity cost of chasing top-of-funnel guides instead is severe, and that buying-intent keywords alone can satisfy years of content production. The practical output is a matrix, not a list: features down one axis, industries across the other, with software, app, tool and template modifiers applied to each cell.

> "there is a massive opportunity cost to"

**Evidence:** Grow and Convert's client: 100+ features, 20+ industries, and 200+ high-buying-intent keywords available, versus 5-50 for an a la carte product.

**How to do it**

1. List every feature the product ships, taken from the product's own feature navigation rather than from marketing copy.
2. List every industry or vertical the product serves.
3. Build a matrix with features as rows and industries as columns.
4. For each cell, generate the modifier variants: feature + software, feature + app, feature + tool, industry + feature + software, industry + feature + template.
5. Pull volume and difficulty for the full set in Ahrefs or Semrush, but do not delete zero-volume rows.
6. Score each row on buying intent first and volume second.
7. Sequence the matrix so the highest-intent rows in the top verticals are written first.
8. Re-run the matrix each time the product ships a new feature or enters a new vertical.

**Tools:** Ahrefs, Semrush

**Pitfall:** Teams stop generating once the list looks long enough, usually around 30 terms, then fall back on ultimate guides. Grow and Convert call that borderline inexcusable for a feature-rich product; the signal is a content calendar full of general how-tos while feature-plus-industry terms sit unclaimed.

**Apply at Pabau:** Pabau is an all-in-one platform, so David should build this matrix explicitly: every Pabau feature (booking, consent forms, invoicing, inventory, marketing, reporting) crossed with every vertical (aesthetics, dermatology, dental, physiotherapy, hair clinics). That matrix, not a volume-sorted keyword export, should drive the blog calendar.

**Apply anywhere:** If your product does many things for many industries, build a feature-by-industry matrix and apply software, app, tool and template modifiers to every cell. A feature-rich platform typically has 200 or more buying-intent keywords, which is years of content, so there is no reason to fall back on general guides.

### 7. Open the engagement with four questions that name the buyer  `140.1`
*core · concrete actions · source 140*

Lashay Lewis took over content for ADA Compliance Pros knowing nothing about web accessibility. Before any keyword work she ran Zoom kickoff calls using the Grow and Convert interview method, and she names the four questions she asked: what were some of your largest deals closed in the last year, what is the most common job title of someone buying the service, what were some of the most common reasons someone decided to buy, and who do you view as your best customers. The answers collapsed a vague market into one describable buyer: IT professionals at midsize to large businesses who had already been sued over an inaccessible website. She only moved to pain points and keywords after that. The point of the four questions is a job title and a triggering event, not a persona document.

> "What is the most common job title of someone buying the service?"

**Evidence:** The four questions identified IT professionals at midsize to large businesses facing accessibility lawsuits, and the resulting content produced 5-15 blog leads a month within four months at over $1,000 average order value.

**How to do it**

1. Book a 45-60 minute Zoom kickoff with the founder or the person who closes deals, and record it.
2. Ask what the largest deals closed in the last year were, and get the company size and the deal value for each.
3. Ask what the most common job title of the buyer is, and push for one title rather than a list.
4. Ask what the most common reasons someone decided to buy were, in the buyer's own words.
5. Ask who they view as their best customers, and why those accounts are better than the rest.
6. Write a one-sentence buyer statement combining job title, company size and triggering event.
7. Reject any keyword later in the process that this buyer would not plausibly search.
8. Re-run the four questions after six months, because the answer moves as the offering matures.

**Tools:** Zoom

**Pitfall:** Teams skip this when the service is new and the positioning is unsettled, which is exactly when it matters most. Without a job title and a trigger you end up choosing keywords by volume.

**Apply at Pabau:** David should run these four questions with Pabau's sales team per vertical, separately for medical spas, dermatology and injectable clinics. The answer for each is a different job title, practice owner versus clinic manager, and that decides whether a template page is written for the owner or the front desk.

**Apply anywhere:** Before any keyword research, run a recorded kickoff call and ask four questions: the largest deals closed last year, the most common buyer job title, the most common reasons people bought, and who counts as a best customer. Reduce the answers to one sentence naming a job title, a company size and a triggering event, and use that sentence to reject keywords later.

### 8. Order the topic list by buying intent first, search volume second  `136.2`
*core · best practices · source 136*

Grow and Convert changed their prioritization rule after the Leadfeeder finding. For every ideation round they sorted candidate topics by buying intent first, and only used search volume as a tie-breaker within that sort. The ideal candidate had intent, volume and low competition together, but many topics they pursued showed no volume in any SEO tool and were published anyway because the searcher was obviously choosing a product. The sequencing rule that follows: work the most bottom-of-funnel, highest-intent terms until they run dry, then move up funnel to how-to posts related to the product, then to top of funnel. Note this is a reversal of the usual tool-led workflow, where the volume column drives the sheet and intent gets checked afterwards, if at all.

> "we'd prioritize the topic ideas by buying intent first and then by search volume"

**Evidence:** Grow and Convert applied intent-first ordering at Leadfeeder over eight months and scaled attributed signups past 225 a month, about 12% of total signup volume.

**How to do it**

1. Collect topic candidates from customer interviews, sales calls and competitor SERPs before opening any volume tool.
2. Score every candidate on buying intent alone: is the searcher choosing or comparing products, solving a live problem, or just reading.
3. Sort the sheet by that intent score and only then pull volume and difficulty from Ahrefs into a second column.
4. Within each intent tier, publish the higher-volume, lower-competition terms first.
5. Keep zero-volume terms in the tier rather than deleting them when the intent is unambiguous.
6. Do not open a lower intent tier until the tier above it is exhausted.
7. When the bottom-funnel tier runs out, move to how-to topics about the problem your product solves, not to generic industry guides.
8. Record conversions per published article by tier so the ordering can be defended with your own data.

**Tools:** Ahrefs

**Pitfall:** Sorting by volume first means the zero-volume comparison and alternatives terms never reach a brief, because they get filtered out before anyone judges the intent.

**Apply at Pabau:** Pabau's keyword sheets should be sorted by intent tier before volume, with competitor comparisons and 'software for X practice' terms above general aesthetics how-to topics. Only start the how-to backlog once the comparison and alternatives pages exist.

**Apply anywhere:** Sort your topic list by buying intent before you look at search volume, and use volume only to order within each intent tier. Zero-volume comparison terms stay on the list when the searcher is clearly picking a product.

### 9. Over 70% SERP overlap means merge to a single page  `49.3`
*core · concrete actions · source 49*

To decide whether two similar keywords genuinely need separate pages or should be consolidated, compare the actual top-10 Google results for each keyword — if more than 70% of the ranking URLs overlap between the two SERPs, Google is treating them as the same search intent, and the fix is to pick the higher-volume keyword and target it with a single page rather than splitting effort across two.

> "more than 70% overlap in the top 10 results"

**How to do it**

1. For each pair of suspected overlapping or similar keywords, run both as separate Google searches, ideally in an incognito window or a rank-tracking tool to avoid personalization.
2. Record the top 10 organic URLs for each keyword.
3. Count how many of those 10 URLs appear in both keywords' top 10 lists.
4. Calculate the overlap percentage (shared URLs divided by 10).
5. If the overlap exceeds 70%, treat the two keywords as one search intent rather than two.
6. Check search volume for both keywords using your keyword research tool and choose the higher-volume one as the primary target.
7. Consolidate your content onto that single chosen keyword rather than maintaining separate pages for both.

### 10. Pick keywords that name your product's differentiator, not the category  `94.1`
*core · concrete actions · source 94*

Grow and Convert's Underdog SEO starts by mapping keywords to a competitive advantage the product actually has. Their QA testing client's differentiator was building automated tests without code, so they skipped 'qa testing' and targeted 'codeless test automation' and 'automated web application testing'. Their helpdesk client was one of the few self-hosted options serving email-based support teams, so they targeted 'self-hosted help desk' and 'customer service email management software' instead of 'help desk software', which Zendesk, Help Scout and Helpdesk own. The reasoning is that anyone typing the qualifier is looking specifically for a tool like theirs, so buying intent is extremely high and the incumbents are not competing for it. Head category terms stay on the roadmap for later, once domain authority builds.

> "look for keywords that map to a competitive advantage"

**Evidence:** Grow and Convert's QA client (Rainforest) ranked in positions 1-3 for a spread of these qualified terms, shown in a public rankings screenshot, without ranking for 'QA testing software'.

**How to do it**

1. Write out every feature or delivery model where you differ from the two or three biggest players in your category.
2. Turn each differentiator into the qualifier a buyer would actually type, such as 'codeless', 'self-hosted', 'for email support teams'.
3. Attach that qualifier to the category noun to build candidate terms, e.g. 'codeless test automation', 'self-hosted help desk'.
4. Search each candidate and check whether any incumbent has a page genuinely built for the qualifier, not a broad page ranking by default.
5. Drop candidates where a top-three incumbent already has a tailored page; keep the rest regardless of low volume.
6. Rank the survivors by how close the qualifier sits to the thing you win deals on.
7. Park the one to three category-definition head terms as a phase-two list, not the starting point.
8. Revisit the head terms only after several qualified pages rank and can link to them.

**Tools:** Ahrefs

**Pitfall:** Teams pick the qualifier that sounds good in marketing copy rather than one buyers type into Google. If nobody outside your company uses the word, the term has no searchers and no SERP to read.

**Apply at Pabau:** Pabau should build its keyword list from what it genuinely does differently, not from 'clinic management software'. Terms like practice management software with built-in charting, or booking software for injectable clinics, are where a dedicated page can win.

**Apply anywhere:** Build your keyword list from the things your product does that the market leaders do not. Turn each into the qualifier a buyer would type, check that no incumbent has a page built for it, and target those before the category head term.

### 11. Pick keywords where the SERP underserves the job, not where you can copy the leader  `75.4`
*core · concrete actions · source 75*

The author's third recommendation is to stop the standard practice of studying what ranks and producing more of the same. He says explicitly that he wants that advice thrown out. Instead, define what would genuinely serve the job for each candidate keyword using the worksheet, then open the SERP and check whether anything ranking actually does that. Where nothing does, you have a market gap and a near-guaranteed win. His framing borrows Nielsen's line that a great product nails a poorly performed, very specific job, and he claims the same holds for content. This is a selection filter, not a writing tip: it changes which keywords enter the calendar, favoring specific queries with weak formats over high-volume queries with strong incumbents.

> "look at what's already ranking for the search term and do more of the same"

**Evidence:** The author's rule that great content, like great product, nails a poorly performed very specific job, attributed to Nielsen.

**How to do it**

1. Shortlist candidate keywords from your usual research, ignoring difficulty scores for now.
2. For each one, fill the JTBD worksheet with the team to define the ideal experience before looking at the SERP.
3. Open the SERP and score the top 10 on whether any result delivers that experience, not on word count or domain strength.
4. Flag keywords where every result is a generic explainer and the job needs a tool, template, database or interactive page.
5. Deprioritize keywords where an incumbent already delivers the job well, even if volume is high.
6. Rank the flagged gaps by how specific and how poorly performed the job is, per Nielsen's rule.
7. Brief the gap keywords with the format the SERP is missing, not with a longer version of the ranking pages.
8. Recheck the SERP after publishing to confirm no competitor has closed the same gap.

**Pitfall:** Reverting to competitor-parity briefs because the gap format costs more to build. You then publish the eleventh identical article for a query where the format, not the depth, was the deciding factor.

**Apply at Pabau:** When choosing Pabau keywords, add a SERP format check: if the top 10 for a query like patient intake form are all prose explainers, the gap is a usable template or interactive form builder page, which fits Pabau's /templates/ route.

**Apply anywhere:** Add a format-gap check to keyword selection. Define the ideal experience for the job first, then reject keywords where an incumbent already delivers it and prioritize those where every result is a generic explainer.

### 12. Pick keywords where your site is the most narrowly focused result  `153.4`
*core · concrete actions · source 153*

Grow and Convert's first of three ranking factors is choosing keywords where you already have topical relevance. Their case is client Cognitive FX, a concussion treatment center with an Ahrefs DR of 51. For the keyword 'memory loss after injury' the page ranks first with zero backlinks, beating results with 137, 40 and 1,417 backlinks, including Mayo Clinic at DR 92. Their hypothesis is that Google recognizes the domain as solely about concussions, while the competitors cover spinal injuries and burns, general emotional support, or all of medicine. The operational read is that keyword selection is where you win or lose the authority fight, and the filter is whether your whole site is narrower on that topic than every ranking competitor.

> "outpacing sites like Mayo Clinic, which has a domain rating of 92"

**Evidence:** Cognitive FX (DR 51) ranks #1 for 'memory loss after injury' with no backlinks to the page, above results with 137, 40 and 1,417 backlinks and above Mayo Clinic at DR 92.

**How to do it**

1. Write one sentence naming the single topic your entire domain is about.
2. Build a keyword list only from terms that sit inside that sentence, favoring bottom-of-funnel terms tied to your product or service.
3. For each candidate, open the top 10 and note what each ranking domain covers overall, not just the page.
4. Keep the keyword if every ranking domain covers a broader subject area than you do.
5. Drop the keyword if a ranking competitor is as narrowly focused as you and also stronger.
6. Ignore Domain Rating gaps at this stage; check backlink counts on the ranking pages instead of on the domains.
7. Publish and give the page months before adding links, since relevance is doing the work.
8. Re-run this filter before every quarter's keyword list so the list stays inside your topical lane.

**Tools:** Ahrefs

**Pitfall:** Chasing high-volume terms adjacent to your niche. On those SERPs you are the broad generalist and the topical-relevance advantage flips against you.

**Apply at Pabau:** Pabau's advantage is being narrowly about running aesthetic and healthcare practices. David should weight the keyword list toward practice-operations terms where general software and general business sites rank, and drop broad clinical or generic business-software terms where Pabau is the wider result.

**Apply anywhere:** Define the one topic your whole domain covers, then only target keywords inside it where every ranking competitor is broader than you are. Narrow focus beats domain authority on those SERPs, even with no links to the page.

### 13. Pick low-volume product-adjacent topics when the goal is sales  `102.2`
*core · best practices · source 102*

Grow and Convert map each goal to a topic profile. For traffic and brand awareness, target topics with broad audience appeal and relatively high search volume for the space. For leads and sales, target more specific topics closely tied to the product or service you sell, and accept that these naturally have lower search volume. Their argument is that if the topics do not serve the goal, content quality cannot rescue the result. The high-intent topics pull people in later stages of the buyer's journey, either looking for the product category or trying to solve a problem the product solves. This is the topic-selection half of their Pain Point SEO position, and it explains why they treat search volume as a filter that actively misleads sales-driven programs.

> "more specific content topics that are closely related"

**Evidence:** Grow and Convert state that lower-volume, product-adjacent topics drive the highest-qualified traffic from later-stage buyers.

**How to do it**

1. List the problems your product removes and the categories a buyer would shop in, in the buyer's own words.
2. For each, find the query that a person with that problem would type, without checking volume first.
3. Sort candidates into two buckets: broad and high-volume, or specific and product-adjacent.
4. If the goal is leads, keep only the product-adjacent bucket and accept volumes in the tens or low hundreds.
5. Rank the kept list by how close the searcher is to buying, not by volume or difficulty.
6. Fill the calendar from the top of that list and revisit the broad bucket only once the high-intent set is covered.

**Pitfall:** Filtering the keyword list by a minimum monthly volume, which deletes exactly the queries that convert. The signal is a calendar full of definitional guides and no page targeting the category you sell in.

**Apply at Pabau:** Pabau should prioritize pages for queries like practice management software for a named specialty over broad aesthetics-industry explainers, and should not drop a keyword because DataForSEO reports 30 searches a month.

**Apply anywhere:** When content is meant to produce leads, choose topics adjacent to what you sell and ignore the low volumes attached to them. Broad high-volume topics belong to the awareness goal, not the sales goal.

### 14. Pick the keyword axis from how the site makes money  `120.6`
*core · best practices · source 120*

Grow and Convert open the guide by refusing the default that traffic growth is the goal of SEO. They split the decision by revenue model. A blog or media site monetized by ads should build the strategy around maximum search volume, because pageviews are the product. A business selling a product or service, where revenue does not come from ads, should prioritize conversions such as leads, sales, trials and add-to-carts instead. Their stated reason is that more traffic does not automatically translate to more conversions, so the two strategies are not versions of the same plan. The practical effect is that the same keyword list gets sorted in opposite directions depending on the answer, and they say the choice has to be made before any research tool is opened.

> "more traffic doesn't automatically translate to more conversions"

**Evidence:** Grow and Convert say they have seen low top-of-funnel lead conversion across thousands of keywords for numerous clients over the years.

**How to do it**

1. Write down how the site actually earns: ad impressions, or purchases and leads.
2. If revenue is ad-based, sort every keyword list by monthly search volume and stop there.
3. If revenue comes from a product or service, sort by buying intent first and treat volume as a tiebreak.
4. Name the conversion event you will judge posts by: demo request, trial, sale or add to cart.
5. Set up that event in Google Analytics before publishing, so per-post conversion data exists later.
6. Re-run the ranking of your existing keyword list under the chosen axis and re-prioritize the queue.
7. Refuse traffic-only reporting for a product business; report conversions per article instead.

**Tools:** Google Analytics

**Pitfall:** Product businesses inherit the media-site playbook because most SEO advice is written for it. The signal is a traffic chart that goes up for a year while demo requests stay flat.

**Apply at Pabau:** Pabau sells software, so pabau.com should sort its keyword queue by buying intent, not volume. David should make demo requests, not sessions, the headline metric on the blog and template pages.

**Apply anywhere:** Decide whether your site earns from ad impressions or from purchases before you sort a keyword list. Ad sites sort by volume; product and service sites sort by buying intent and report conversions per article.

### 15. Pick the low-volume high-intent secondary keyword over the high-volume one  `116.8`
*core · best practices · source 116*

Grow and Convert state the trade-off explicitly. All else equal, they will take a secondary keyword with high buying intent and low search volume over one with low buying intent and high volume. The reason is the whole point of their model: the goal is conversions, not traffic, which is why the recovery process begins in the conversion spreadsheet rather than the traffic report. They apply the same buying-intent filter to recovered secondary keywords that they apply to primary keyword research, whether the term is long tail, a comparison, a category term or a jobs-to-be-done phrase. The filter never relaxes because a keyword arrived by accident. This matters because a lost-keyword diff will surface plenty of informational terms that once sent traffic and never sent a customer.

> "our focus on targeting high buying-intent keywords never goes away"

**Evidence:** Grow and Convert say they start the process from their conversion spreadsheet rather than their traffic report, and would take low volume with high buying intent over the reverse.

**How to do it**

1. Start the recovery process from the conversion report, not the traffic report.
2. For each lost secondary keyword, classify the intent as category, comparison, jobs-to-be-done, use case, or informational.
3. Drop informational terms from the recovery list regardless of how much traffic they once sent.
4. Where two candidates compete for the same rewrite, take the higher-intent one even at a fraction of the volume.
5. Check the CPC on the survivors as a second commercial-intent signal.
6. Rank the final list by proximity to a purchase decision, then by lost traffic.
7. Assign rewrites and new articles from the top of that ranked list.

**Tools:** Ahrefs

**Pitfall:** A lost-keyword diff is dominated by informational terms because those are the easiest to rank for and the first to be lost. Rebuilding those restores the traffic chart and does nothing for conversions.

**Apply at Pabau:** Pabau's refresh briefs should list the recovered keyword's intent type next to its volume. A term like software pricing for a medspa beats a higher-volume definitional term even though the traffic estimate looks worse.

**Apply anywhere:** Put the recovered keyword's intent type next to its volume in every refresh brief. A pricing or comparison term beats a higher-volume definitional one even when the traffic estimate looks worse.

### 16. Pick top-funnel keywords only from three pain-point-linked patterns  `132.4`
*core · best practices · source 132*

Grow and Convert do not treat top-funnel as open season on anything the audience might find interesting. Every Geekbot top-funnel target still connected to a customer pain point, and their examples fall into three usable patterns. First, frustration keywords, where the search itself expresses annoyance with the status quo: 'standup meetings waste of time'. Second, non-software-solution keywords, where the searcher wants a manual workaround: 'daily standup Excel template'. Third, beginner-question keywords about the process your product runs: 'daily standup questions'. Each of those searches implies the person has the problem the product solves, which is what makes tying in the product feel natural rather than forced. A top-funnel topic that is merely audience-adjacent, with no pain point behind it, fails this test and should not be commissioned.

> "good top of funnel topics that still have some chance of generating conversions"

**Evidence:** Geekbot's top-funnel targets: 'standup meetings waste of time', 'daily standup Excel template' and 'daily standup questions', each chosen because the search implies the standup pain Geekbot solves.

**How to do it**

1. Write down the specific pain your product removes, in the words a customer would use.
2. Generate frustration keywords by combining the current manual method with complaint language: 'waste of time', 'too long', 'hate', 'problems with'.
3. Generate non-software-solution keywords by combining the task with 'template', 'spreadsheet', 'Excel', 'checklist' and 'manually'.
4. Generate beginner-question keywords by listing what a newcomer to the process asks: typical questions, how often, who attends, how long.
5. Discard any candidate where the search does not imply the searcher has the pain your product addresses, no matter how much volume it holds.
6. On frustration keywords, validate the complaint, then present the product as the alternative to the method they are frustrated with.
7. On non-software-solution keywords, actually give the template away, then explain its limits and why the product removes them.
8. On beginner-question keywords, answer the question fully first, then tie the product in where the answer naturally raises it.

**Pitfall:** The failure is picking top-funnel topics because they have volume and are on-theme for the industry. Those pages draw readers who have no version of your problem, and they convert at or below the 0.19 percent floor.

**Apply at Pabau:** Pabau's top-funnel briefs should come from these three patterns applied to practice operations: frustration terms like no-show problems or paper consent forms, non-software-solution terms like a client intake form template or an appointment schedule spreadsheet, and beginner questions about running a clinic day. A general aesthetics-industry trends piece fits none of them and should be cut.

**Apply anywhere:** Restrict top-funnel targets to three patterns that still imply the pain your product solves: frustration keywords about the current manual method, keywords seeking a non-software workaround such as a template or spreadsheet, and beginner questions about the process your product runs. Anything merely adjacent to your industry does not qualify.

### 17. Plan deliberately for the five to fifteen direct buying keywords  `137.3`
*core · concrete actions · source 137*

Grow and Convert say they are shocked at how many companies have no plan to rank for direct buying keywords. Most companies rank for one or two by accident, through the homepage or a feature page. Their figure is that there are usually between five and fifteen more of these keywords per business, depending on the category, that a solid blog post could rank for. These are queries from solution-aware people literally Googling for what you sell, like 'buy flowers online'. Meanwhile B2C marketers publish '10 tips for X in 2020' posts and influencer interviews and push them through email and social, hoping conversions appear. Their instruction is blunt: if you do not have a plan to rank for these keywords, make one and prioritize it above everything else on the content and SEO agenda.

> "there are usually between 5 – 15 more of these keywords, depending on the business"

**Evidence:** Grow and Convert observe most companies rank for only one or two direct buying keywords accidentally, while five to fifteen more are available per business.

**How to do it**

1. Write out how a solution-aware buyer would describe what you sell, in their words rather than your product name.
2. Generate the buying variants for each: 'best [thing]', '[thing] near me', 'buy [thing] online', '[thing] providers', '[thing] cost'.
3. Check in Google Search Console which of these you already rank for accidentally via the homepage or a feature page.
4. Aim for a list of five to fifteen genuine direct buying keywords; if you have fifty, most are not direct buying terms.
5. Assign each remaining keyword either to an existing page or to a new blog post, and record the owner and date.
6. Put this list at the top of the content calendar, ahead of tips posts, interviews and trend pieces.
7. After the list is published and ranking, move the calendar to pain-point topics because this pool is finite.

**Tools:** Google Search Console, Ahrefs

**Pitfall:** Companies leave these terms to the homepage, which is optimized for brand rather than the category query, so it ranks weakly and never gets improved. The signal is a homepage sitting at position 8 to 15 for your main buying term with no dedicated page behind it.

**Apply at Pabau:** David should audit which buying terms pabau.com currently catches on the homepage or a feature page, then build a dedicated /blog/ or comparison page for each of the remaining five to fifteen before commissioning any more general tips articles.

**Apply anywhere:** Build the list of five to fifteen queries a solution-aware buyer types when looking for exactly what you sell, check which you only catch by accident on the homepage, then give each one a dedicated page and rank that work first.

### 18. Point the agent only at bottom-of-funnel keywords for the product  `77.2`
*core · concrete actions · source 77*

The first stage of Schneider's agent does not do broad topical keyword research. It queries a keyword data API specifically for bottom-of-funnel keywords related to the product's service offering. That constraint is doing most of the work in the pipeline: it is what makes the resulting articles capable of producing signups rather than sessions. It also matches the wider position in this base that top-of-funnel material is the first thing AI answers absorb, so an automated publishing program aimed at informational queries is buying the least defensible traffic. Schneider's framing is commercial throughout — the question he closes on is whether AI organic content drives leads, not whether it drives traffic.

> "research the bottom of funnel keywords related to the product"

**Evidence:** Schneider's stated first step is bottom-of-funnel research tied to the product service offering, and the stated success metric is tracked signups.

**How to do it**

1. Write out the product's service offering as a plain list of what it actually does for a buyer.
2. Query the keyword data API for keywords around each offering, not around the industry as a whole.
3. Filter the returned set to commercial and transactional modifiers: pricing, alternatives, versus, software, best, for [segment], near me.
4. Drop informational how-to and definition queries from the agent's queue entirely and route them elsewhere.
5. Use CPC as the commercial-intent filter when volume is ambiguous, keeping keywords that advertisers pay for.
6. Cap the queue so the agent never gets more keywords than the publishing cadence can absorb.
7. Re-run the query monthly so new bottom-funnel terms enter the queue as the product ships features.

**Tools:** DataForSEO

**Pitfall:** Letting an automated pipeline run on whatever the keyword tool returns fills the site with high-volume informational pages that never convert and are the first to be replaced by AI answers. The signal is rising impressions with a flat signup count.

**Apply at Pabau:** Pabau's agent queue should be built from what the software does — consent forms, no-show policies, treatment records, online booking, package pricing — rather than from generic aesthetics-industry terms. Feed those into the template and code-reference page programs where intent is already commercial.

**Apply anywhere:** Restrict any automated content pipeline to bottom-of-funnel keywords tied directly to what you sell. Use CPC as the commercial filter and keep informational topics out of the automated queue.

### 19. Position against spreadsheets as the real incumbent in B2B software  `93.7`
*core · content insights · source 93*

Goolding argues that for most B2B software the biggest competitor is Excel or Google Sheets, and he gives the reasons people stay: they feel they are doing fine, it is free, they do not see the time they lose, and they do not know an affordable better option exists or what better even looks like. With Timetastic from 2021, most new customers arrived because they were fed up managing time off through emails and spreadsheets, yet the vast majority of businesses still used them. With StrataPT, physical therapists ran Excel for patient documentation, treatment notes, billing and financial reporting. He says spreadsheets are a plausible incumbent across project management, workflow planning, documentation, financial reporting and sales prospecting. That makes 'template' and 'how to do X in a spreadsheet' keywords a live acquisition channel rather than a distraction.

> "the old adage about Excel being your biggest competitor"

**Evidence:** Timetastic's 'staff leave planner for excel' and 'google sheets annual leave template' posts generated more than 40 free trial signups from organic visitors across 9 months.

**Pitfall:** A post that just mocks spreadsheets converts nothing. The reader is using one because it works well enough, so the page has to concede that and quantify what it costs them.

**Apply at Pabau:** Pabau should treat the spreadsheet and paper diary as the named incumbent in aesthetic practices, and reference them explicitly in blog posts and template pages rather than only comparing against software rivals.

**Apply anywhere:** Treat spreadsheets as your named incumbent competitor in B2B software and reference them explicitly across your content, because most of the market still uses them.

### 20. Prioritize bottom-funnel terms even when there are few of them  `110.9`
*core · best practices · source 110*

Grow and Convert make a point that gets lost in the volume argument. Their bottom-of-funnel-first strategy is about prioritization, not about how big the bottom-funnel pool is. Even if your product genuinely has few buying-intent keywords, you should still go after those first, and they say there is no excuse not to. The reasoning is ordering: producing top-funnel content that has no product intent before you own every term that does have product-buying intent means you left the highest-converting traffic on the table while spending on the lowest. So a small bottom-funnel list does not justify starting at the top; it just means you exhaust the small list faster and move up the funnel sooner.

> "our bottom of funnel first strategy is about"

**Evidence:** Grow and Convert state plainly that even a product without many bottom-funnel keywords should go after them first, framing the strategy as prioritization rather than pool size.

**How to do it**

1. Build the full list of product-intent terms even if it only runs to ten or twenty keywords.
2. Publish against that entire list before commissioning any top-of-funnel piece.
3. Track which of those pages rank and convert before moving up a funnel stage.
4. When the list is genuinely exhausted, move to mid-funnel pain points, not straight to broad category education.
5. Keep the exhausted list under review, since new competitors create new alternative terms every year.
6. Document the ordering rule so a new marketer cannot restart the calendar at the top of the funnel.

**Pitfall:** Using a short bottom-funnel list as permission to start at the top. The result is a blog full of education content while competitors quietly own the ten terms that convert.

**Apply at Pabau:** If Pabau's product-intent keyword list is short, that shortens the phase rather than skipping it. Finish the alternatives, comparison and feature-software pages on pabau.com before adding more general aesthetic-practice explainers.

**Apply anywhere:** Treat bottom-funnel-first as an ordering rule, not a volume argument. Even a list of ten buying-intent keywords gets published in full before any top-of-funnel piece enters the calendar.

### 21. Prioritize keywords already ranking positions 2-15 over new targets  `11.9`
*core · concrete actions · source 11*

Gotch's opportunity-scoring system automatically flags any keyword where the tracked URL already ranks between position 2 and 15 as 'low-hanging fruit' that should always outrank a brand-new keyword target in priority, because the effort to refine an existing page, add topic support, and drive a few more links is far smaller than building a new page from zero, and moving a page from position 5 to position 2 is 'a dramatic increase in visibility.' This gives a specific, checkable numeric threshold for triaging a keyword list rather than a vague 'improve what's ranking' instinct.

> "go after keywords ranking anywhere between positions 2 and 15"

**How to do it**

1. Pull current ranking positions for every keyword/URL pair in the working list from the GSC Performance report or a rank tracker.
2. Flag every keyword ranking between position 2 and 15 as 'low-hanging fruit' priority in the Opportunity column of the tracking sheet.
3. Move all low-hanging-fruit keywords to the top of the execution queue, ahead of brand-new, untapped keyword targets in the same cluster.
4. For each low-hanging-fruit page, plan the specific improvement action: refine on-page content, add topical support sections, or acquire additional links, rather than building a new URL.
5. Re-check position monthly by re-pulling the GSC or rank-tracker report, and re-triage the list as pages cross the position-2 threshold and graduate out of active priority.

**Tools:** Google Search Console

**Pitfall:** Chasing brand-new, unranked keyword targets while ignoring pages already sitting at positions 5-15 that could be pushed to page-one-top with far less effort than starting a page from zero.

### 22. Prompt ChatGPT to surface debated niche rumors, then target the top phrasing  `17.3`
*core · ai workflows · source 17*

To systematically find "debated rumor" content opportunities, feed ChatGPT both your own landing page and the Reddit comment describing this tactic, then ask it directly what the highly debated rumors are in your niche; because ChatGPT does its own web search to answer, it surfaces what people are actively discussing. From there, do normal keyword research to find the most common phrasing of each rumor and identify which phrasing has the highest search volume, then apply the same exact-match on-page formula used elsewhere in this playbook: the target keyword phrase goes in the page title, URL slug, H1, and the beginning of the first sentence. Critically, the page must open with a TLDR above the fold that gives a clear, confident, non-hedging answer, explicitly avoiding "yes, but no" wishy-washy framing, since the whole opportunity exists because competing pages are failing to commit to a real answer.

> "What are some of these highly debated rumors in my"

**How to do it**

1. Open ChatGPT and paste in your own landing page or a description of your niche for context.
2. Paste in the Reddit comment or a description of this "debated rumor" tactic as additional context.
3. Ask ChatGPT the specific question: "What are some of these highly debated rumors in my niche?"
4. Review the list of rumors ChatGPT returns, which it generates using its own web search of current discussion.
5. Take each rumor into a keyword research tool and find the most common ways people phrase it, plus the search volume for each phrasing.
6. Select the highest-search-volume phrasing as your target keyword for a new page.
7. Place that exact keyword phrase in the page title, URL slug, H1, and the beginning of the first sentence.
8. Write a TLDR directly above the fold that gives one clear, confident, unambiguous answer to the question, explicitly avoiding hedged "yes, but no" language.
9. Publish the page and monitor rankings and link acquisition over the following days to weeks, since the earlier PS5 example reached number one within days (inferred verification timeframe).

**Tools:** ChatGPT

**Prompt / template:**

```text
What are some of these highly debated rumors in my niche?
```

**Pitfall:** The whole opportunity depends on giving an unambiguous answer — copying the same wishy-washy "yes, but no" framing that every other ranking competitor is already using, including, in the PS5 case, Sony itself, forfeits the exact gap that makes the tactic work.

### 23. Prove content ROI by classifying before-and-after ranked keywords by intent  `88.2`
*core · ai workflows · source 88*

To quantify the value of a content engagement, the Grow and Convert author pulled the client's ranked keywords from Ahrefs for the period before the agency started and for the period after, then used AI to analyze the shift. The finding was clean: every keyword the client ranked for previously was informational and top-of-funnel, while the keywords the agency helped them rank for were almost entirely buying-intent. Pairing that intent shift with the conversion data quantified the business impact and made the case study far stronger than a traffic-went-up chart. This is a repeatable measurement pattern, not just a storytelling trick. It answers the question traffic totals cannot: did the portfolio move toward keywords that convert.

> "I queried Ahrefs to compare the keywords the client ranked for"

**Evidence:** Grow and Convert case study: pre-engagement keywords were entirely informational and top-of-funnel, post-engagement almost entirely buying-intent, paired with per-article conversion data.

**How to do it**

1. In Ahrefs Site Explorer, open Organic Keywords and set the date to the month before the content work started; export to CSV.
2. Export the same report for the current month.
3. Feed both CSVs to an AI model and ask it to label every keyword informational, commercial-investigation or transactional, with a one-line reason.
4. Ask for the percentage split by intent for each period and the list of keywords that are new in the after period.
5. Join the after-period keywords to conversion counts per landing page so each intent bucket carries a revenue or demo number.
6. Chart the two intent mixes side by side as the headline visual.
7. Spot-check 20 random intent labels manually; models over-call transactional intent on ambiguous head terms.
8. Repeat the same export quarterly so the intent mix becomes a standing KPI, not a one-off.

**Tools:** Ahrefs

**Pitfall:** Volume and traffic can rise while the intent mix stays informational, which looks like success and produces no revenue. The reverse also traps you: an intent shift with no conversion data attached is still an unproven claim.

**Apply at Pabau:** Pabau should run this quarterly across the blog and template pages. Report the informational-to-buying-intent mix alongside sessions, so an article ranking for 'what is a SOAP note' is not counted as equal to one ranking for 'clinic booking software'.

**Apply anywhere:** Export your ranked keywords before and after a content push, label them by intent with AI, and report the intent mix as a KPI next to traffic. Attach conversions per bucket or the shift is only a story.

### 24. Publish keywords Ahrefs shows as N/A when buying intent is high  `140.9`
*core · content insights · source 140*

Lewis reports conversions from keywords where Ahrefs displayed N/A or very low search volume, and names two specific pages: a siteimprove vs monsido article that drove two conversions and an accessible vs audioeye article that drove one. Those are single-digit conversion counts, which is exactly the point at an average order value over $1,000. She ties this to Grow and Convert's mini-volume keyword argument, that low volume terms make sense when buying intent is high. The broader framing she gives is that the client was not chasing traffic growth. Because the methodology selects for converting visitors rather than volume, leads arrived far sooner than a volume-led plan would have delivered. Anyone reporting on this work needs the value per lead in the report, because the traffic line will look unimpressive for months.

> "despite the low search volume that Ahrefs displays"

**Evidence:** For ADA Compliance Pros, the siteimprove vs monsido article produced two conversions and the accessible vs audioeye article produced one, on keywords Ahrefs reported as N/A or low volume, at over $1,000 average order value.

**How to do it**

1. Keep every competitor-versus-competitor and alternatives term in your list regardless of reported volume, including N/A rows.
2. Estimate value per conversion for the service before ranking the list.
3. Sort candidates by estimated revenue per page, calculated as plausible monthly conversions times order value, not by volume.
4. Publish one page per competitor pairing rather than a combined roundup.
5. Track conversions per landing page in analytics from day one so single-digit wins are visible.
6. Report leads and revenue alongside traffic, and warn stakeholders the traffic line will stay flat.
7. Expand into more mini-volume pairings once any one of them converts.

**Tools:** Ahrefs, Google Analytics

**Pitfall:** Volume filters in keyword tools delete exactly these terms before a human sees them. If your report is a traffic graph, these pages look like failures while they are quietly producing the revenue.

**Apply at Pabau:** David should build one page per named Pabau competitor pairing even where DataForSEO reports no volume, and report those pages by demo requests rather than sessions. A page with 30 visits a month is a success if two of them book.

**Apply anywhere:** Do not filter keywords by volume when buying intent is high. Keep competitor-versus-competitor and alternatives terms even at N/A volume, rank them by order value times plausible conversions, and give each pairing its own page. Report these pages on leads and revenue, because their traffic will always look negligible.

### 25. Publish one comparison page per named competitor even at sub-20 volume  `95.4`
*core · concrete actions · source 95*

For Circuit, an app for delivery drivers, Grow and Convert published 6 competitor comparison articles, every one targeting a keyword under 20 monthly searches, pitching Circuit against Routific, Route4Me and RouteXL. Over the two years between the start of the engagement and the article, those 6 pages collectively drove 149 organic free trial signups at an average 2 percent conversion rate, with Route4Me Alternative converting at 4.5 percent. Circuit is self-serve B2B SaaS with teams of 10 to 15 drivers, so once the free-trial-to-paid rate is applied, Matt Goolding puts the value at tens of thousands of dollars of MRR from mini-volume keywords alone. The same angle worked for an enterprise digital asset management client, where one alternatives post produced 11 signups on a high price point.

> "these 6 articles have collectively driven 149 organic signups"

**Evidence:** Circuit: 6 sub-20 comparison articles, 149 organic signups over 2 years, 2 percent average conversion rate, Route4Me Alternative at 4.5 percent.

**How to do it**

1. Ask sales for every competitor named in lost or competitive deals and list them.
2. Generate two keywords per competitor: '[competitor] alternative' and '[competitor] vs [you]'.
3. Check volume in Ahrefs but publish regardless of a sub-20 or zero reading.
4. Write one dedicated page per competitor rather than a single roundup, so each ranks for its own term.
5. Include the concrete differences a buyer is checking, such as pricing tiers, plan limits and integrations.
6. Put the trial or demo CTA above the fold, since the traffic is already at the decision point.
7. Track conversion rate per comparison page separately from the blog average.
8. Multiply signups by your trial-to-paid rate and average contract value to report the pages in revenue, not traffic.

**Tools:** Ahrefs

**Pitfall:** Rolling all competitors into one roundup post loses the individual '[competitor] alternative' rankings, which are the terms that actually convert. One page per competitor is the point.

**Apply at Pabau:** Pabau should have a dedicated alternatives page for every practice management competitor it loses deals to, not a single comparison roundup. Each one is a decision-stage page that ranks fast and feeds the demo form.

**Apply anywhere:** Publish a separate comparison page for every named competitor, even when the tool shows under 20 searches. Roundups do not capture the individual alternatives rankings, and those are the ones that convert.
