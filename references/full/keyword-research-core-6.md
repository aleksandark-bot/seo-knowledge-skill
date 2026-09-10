# Keyword Research — core (part 6 of 7)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Score each pain-point query on buying intent and ranking realism  `107.4`
*core · concrete actions · source 107*

Grow and Convert say the best topics come from the pain-point interviews, not from a keyword tool. A tool tells you what is searched and how often, but not whether the searcher is a buyer, a researcher, a student or a competitor. Their workflow is to take each pain point from the sales and CS interviews, translate it into the query a buyer would actually type, then confirm real volume in Ahrefs or Semrush. Each query is then scored on two dimensions: how specific the buying intent is, and how realistic it is for your site to rank. High on both is where you start. High intent but low ranking realism goes on a longer-term list. High volume but low intent is what they call the TOF trap that creates cost-center content. The order matters: interviews first, tool second as verification only.

> "how specific the buying intent is, and how realistic it is"

**How to do it**

1. List every pain point surfaced in the sales and CS interviews, one per row.
2. For each, write the query a buyer would type at that moment, in their words not your product vocabulary.
3. Plug the queries into Ahrefs or Semrush to confirm there is real search volume behind them.
4. Score each query 1 to 5 on buying-intent specificity.
5. Score each query 1 to 5 on ranking realism, based on the authority of the sites currently on page one.
6. Start with the queries scoring high on both, and put high-intent low-realism queries on a long-term list.
7. Delete or demote high-volume low-intent queries rather than letting them fill the calendar.

**Tools:** Ahrefs, Semrush

**Pitfall:** Starting in the keyword tool inverts the process and the volume column dominates the decision. The symptom is a calendar full of trend and best-practice posts with strong volume and no demo requests.

**Apply at Pabau:** For Pabau, queries like clinic software for a specific treatment or a named competitor alternative score high on intent even at low volume, while aesthetic industry trend keywords score high on volume and low on intent. David should keep the scoring sheet as the gate before any brief is written.

**Apply anywhere:** Translate each interview pain point into a buyer's query, verify volume in a keyword tool, then score every candidate on intent specificity and ranking realism and start only where both are high.

### 2. Score every candidate keyword 0-100 against your brand profile  `50.2`
*core · ai workflows · source 50*

Before a newly discovered topic or keyword is allowed into the working keyword set, the system scores it from zero to 100 for relevance against the business's own "Brand DNA" profile, and gives a stated reason for borderline calls — the transcript's own example is "free and local SEO tool system" being flagged as not relevant to an SEO-tool business, and "free SEO tools versus paid" being flagged as a maybe. Keywords that clear the threshold are marked relevant and proceed into clustering, while low scorers can be manually overridden and marked relevant if the automated call was wrong. This scoring step exists specifically to keep a fast-growing, automatically-populated keyword database from drifting off-topic as it scales, which is the main risk of any "discover everything automatically" keyword system.

> "it scores that from zero to 100"

**How to do it**

1. Write or assemble a structured brand/business profile covering products, audience, and positioning to serve as the scoring reference, a "Brand DNA" document.
2. For every newly discovered candidate keyword or topic, run it against that brand profile using an LLM prompt that outputs a 0-100 relevance score plus a short stated reason (inferred exact prompt structure, since the source describes the output but not the literal prompt).
3. Set a minimum score threshold below which a keyword is auto-excluded from the working set rather than only flagging it.
4. Log the stated reason alongside every score so a human reviewer can quickly sanity-check edge cases without re-researching each keyword from scratch.
5. Build a manual override so a human can mark an auto-excluded keyword as relevant after all, correcting false negatives.
6. Re-run the scoring pass periodically as the brand profile is updated, since relevance can shift as the business's product line or audience changes (inferred maintenance step).

**Tools:** an LLM such as Claude or ChatGPT

**Pitfall:** An automatically-growing keyword database left unscored will drift off-topic; explicit 0-100 relevance scoring against a real brand profile is what keeps the universe manageable as it scales rather than accumulating irrelevant keywords.

### 3. Score every keyword on two independent axes: long-tail and buying intent  `104.1`
*core · concrete actions · source 104*

Grow and Convert argue the standard long-tail logic is wrong. The usual claim is that more specific means closer to a purchase. Their counter-example is 'how to cook turkey tail mushroom kabobs over a fire', which is extremely specific and shows no intent to buy anything. Meanwhile 'turkey tail mushroom spawn' is less specific but clearly commercial, and head terms like 'car insurance', 'buy flowers' and 'baby stroller' carry huge buying intent at huge volume. Their conclusion is that specificity and buying intent are two separate properties of a keyword, and the keywords worth building are the ones scoring high on both. They call the resulting prioritization Pain Point SEO: intent first, volume second. When a low-intent term has more traffic than a high-intent one, they still take the high-intent one.

> "Buying-intent and long-tail are two independent characteristics"

**Evidence:** Grow and Convert compared conversion rates across 95+ articles that generated thousands of conversions for multiple clients, and high buying-intent keywords converted at a much higher rate in every keyword type.

**How to do it**

1. Put every candidate keyword in a sheet with two separate columns: specificity and buying intent, each scored high, medium or low.
2. Score buying intent by asking whether the searcher is shopping for the type of product you sell, not by counting words in the query.
3. Search each term and read the top 10; treat product and pricing pages ranking above blog posts as confirmation of commercial intent.
4. Sort by buying intent first, then by keyword difficulty, and only use search volume as the tiebreaker within a band.
5. Build the high-intent, low-competition terms first, even where a low-intent term shows ten times the volume.
6. Park high-intent head terms like the category noun on a phase-two list rather than deleting them.
7. Track conversions per published article by target keyword, and use that data to recalibrate your intent scoring each quarter.

**Tools:** Ahrefs, Semrush

**Pitfall:** Teams equate word count with intent and fill the calendar with very specific how-to queries. Those rank quickly and convert at close to zero, which makes the whole program look like it failed on traffic when it failed on intent.

**Apply at Pabau:** David should add a buying-intent column to Pabau's keyword sheet and stop ranking candidates by volume. 'Aesthetic clinic software with inventory tracking' outranks 'what is a chemical peel' for priority, even though the second has more traffic.

**Apply anywhere:** Score keywords on specificity and buying intent as two separate columns, then build the high-intent terms first regardless of which has more volume. A very specific query with no commercial signal converts no better than a broad informational one.

### 4. Screen a new B2B account for 20 to 40 buying-intent keywords in minutes  `129.2`
*core · concrete actions · source 129*

Before taking on a new B2B client, Grow and Convert run quick keyword research with one question: can we easily find 20 to 40 keywords with decent buying intent? They are explicit that the point is not to finalize the target list, only to test how hard the list is to build. If you can drop a couple of obvious terms into any keyword tool and surface dozens of clearly high-intent variants within minutes, the account passes. If getting to roughly 20 is a struggle, they say you may be in a niche where SEO is not the best channel — not that SEO is worthless, but that it should be treated as a short-term project to capture the few high-intent terms that do exist, then stopped. Their best and longest-running clients have hundreds of keywords carrying some buying intent.

> "we typically do some quick keyword research to see if we can easily find"

**Evidence:** Grow and Convert use a 20 to 40 keyword threshold on new B2B accounts; their longest-running clients have hundreds of keywords with some buying intent.

**How to do it**

1. Put two or three obvious category terms into Ahrefs, Semrush or Clearscope and open the variations report.
2. Set a timer of a few minutes; the test is speed of discovery, not completeness.
3. Count only keywords where simple logic says the searcher is close to buying, and ignore volume at this stage.
4. Pass the account if you reach 20 to 40 such keywords easily; flag it if you barely scrape 20.
5. On a flagged account, scope SEO as a fixed short-term project to cover the few high-intent terms, with an explicit stop point.
6. Add the higher-funnel-but-still-commercial queries before you declare a shortage, since use-case and how-to questions often carry intent.
7. Recheck the count annually, because a growing category adds keywords.

**Tools:** Ahrefs, Semrush, Clearscope

**Pitfall:** Turning the screen into full keyword research. Spending a week building the perfect list defeats the test, which is whether the list is easy to build. The other failure is padding the 20 with informational terms that no buyer types.

**Apply at Pabau:** Run this count per Pabau page family rather than for the site. Aesthetic-practice software terms will clear 40 easily, but a narrower family such as a specific integration or a single diagnostic-code group may not — in which case build the handful of pages that exist and stop rather than commissioning a monthly cadence.

**Apply anywhere:** Test a new market by how quickly you can find 20 to 40 buying-intent keywords. Drop two or three obvious category terms into a keyword tool and count only near-purchase queries. Easy dozens means fund SEO as an ongoing channel; a struggle to reach 20 means run it as a short capped project instead.

### 5. Search the gap report by term to surface each buying-intent bucket  `118.2`
*core · concrete actions · source 118*

Rather than scrolling a multi-thousand-row content gap report, Grow and Convert use the tool's term filter to pull out each buying-intent bucket in turn. They type 'software' to surface every category keyword that names a software category, then feature names such as 'AI Chatbot' to surface product-led category terms, then each competitor's brand name to surface the alternatives and versus keywords. Jobs-to-be-done rows come out by filtering on 'how to' plus the verbs that describe the tasks your product performs. The point is that the three Pain Point buckets each have a predictable lexical signature, so a filter finds them faster than reading. They flag one caveat during the walkthrough: 'AI Chatbot' is only a real opportunity if your product actually has that feature.

> "You can filter the keyword research tool by term"

**Evidence:** Grow and Convert's worked example surfaces 'AI Chatbot' and 'enterprise customer service software' from the help desk gap report using term filters.

**How to do it**

1. Open the exported gap report in the tool's filter view or in a sheet with text filters.
2. Filter on 'software', 'tools', 'system' and 'platform' to pull the category keywords.
3. Filter on each feature name you actually ship, such as 'AI chatbot' or 'online booking', for product-led category terms.
4. Filter on every competitor brand name, plus 'alternatives', 'vs' and 'competitors', for the comparison bucket.
5. Filter on 'how to' and on the verbs describing tasks your product performs, for the jobs-to-be-done bucket.
6. Filter on 'template', 'checklist' and 'example' for the narrow asset keywords that sit under the JTBD bucket.
7. Copy each filtered set into its own tab so the three buckets stay separate through briefing.
8. Delete any row surfaced by a feature filter where you do not actually ship that feature.

**Tools:** Ahrefs

**Pitfall:** Filtering on a feature name your competitor has and you do not produces a list of keywords you cannot win a conversion from. The signal is a briefed article whose only honest conclusion is that the reader should buy the competitor.

**Apply at Pabau:** When Pabau runs a gap report, filter it on the feature names Pabau actually ships, so blog and template briefs come from real product surface rather than from a competitor's roadmap.

**Apply anywhere:** Use the gap report's term filter to pull each buying-intent bucket out separately, filtering on category words, your own feature names, competitor brands and 'how to' phrasing.

### 6. Seed the first organic topics from keywords already converting in Google Ads  `133.3`
*core · concrete actions · source 133*

Circuit had grown through Google Ads before hiring Grow and Convert, which gave the content team something most new accounts lack: keyword-level conversion data. Rather than starting from a volume-led keyword export, they pulled the terms that were already converting in the ads account and reasoned that ranking organically for those same terms would produce conversions too. From that pool they picked six topics deliberately spread across keyword difficulty, so that the easy ones could prove the process works early while the competitive ones matured. This is a different starting point from the usual Grow and Convert pain-point research, and it is the fastest available on any account with ad history. The conversion data settles the intent question with money rather than inference.

> "we could see what keywords were already converting for them via Google Ads"

**Evidence:** Grow and Convert identified six starting topics for Circuit from Google Ads conversion data, chosen with varying keyword difficulty.

**How to do it**

1. Export the search terms report from Google Ads filtered to conversions greater than zero over the last 12 months.
2. Strip branded terms and keep only non-brand queries with at least one conversion.
3. Sort the survivors by conversions and by cost per conversion, since expensive converters are the ones organic rankings save the most money on.
4. Pull keyword difficulty for each survivor in Ahrefs.
5. Pick roughly six starting topics spread deliberately across the difficulty range, not just the easiest.
6. Write one article per topic rather than combining several converting terms into one page.
7. Track those exact keywords in the rank tracker from the publish date.
8. Report organic conversions per article against the ads cost per conversion for the same term, to show the saving.

**Tools:** Google Ads, Ahrefs

**Pitfall:** Taking the whole converting-keyword list and chasing the highest-volume terms first. On a low domain rating site those are the slowest to move, and with nothing ranking for months the program looks dead before the easy wins land.

**Apply at Pabau:** Pabau should export the converting non-brand search terms from its Google Ads account and check each against the existing blog and template pages. Any term converting in paid with no organic page behind it is a commissioning candidate, and the paid cost per conversion is the business case for writing it.

**Apply anywhere:** If you run paid search, export the search terms that already convert and use them as the seed list for organic content. Strip brand terms, pull difficulty for the rest, and pick a starting batch spread across easy and hard so early wins arrive while the competitive pages mature.

### 7. Skip funnel steps for bottom-of-funnel video/landing-page keywords  `55.8`
*core · concrete actions · source 55*

Alongside the multi-step TOFU-to-close funnel, run a simpler parallel track for bottom-of-funnel keywords, which the host says are both less competitive (fewer people and videos target them) and much higher intent, since the searcher is already warmed up by the act of searching that specific term. For these, build dedicated bottom-of-funnel SEO landing pages and matching videos targeting the same keywords, but skip most of the funnel machinery (archetype segmentation, multi-day video sequence) — the video can point directly to the landing page or straight to a purchase/signup, since the multi-step trust-building isn't needed for someone already searching a high-intent term.

> "Bottom-of-funnel keywords are less competitive"

**How to do it**

1. Identify bottom-of-funnel keywords for your product — high commercial intent, typically lower search volume and lower competition than TOFU questions.
2. Build a dedicated SEO landing page for each bottom-of-funnel keyword.
3. Produce a short video targeting the same bottom-of-funnel keyword, following the same low-competition-question targeting and Descript editing workflow used for TOFU videos.
4. Point that video's call to action either directly to the matching landing page or straight to a purchase/signup flow, skipping the form-to-archetype-to-call sequence used for TOFU leads.
5. Prioritize this simplified path for any keyword where the searcher's intent is already commercial enough that additional trust-building steps would just add friction.

### 8. Source post topics by sitting in on SDR, AE and success calls  `97.6`
*core · concrete actions · source 97*

Grow and Convert are explicit that topic selection belongs to whoever runs content marketing, not to the freelance writer, because the content manager has a better idea of the pain points prospects and customers actually have. Their method for getting those pain points is not a keyword tool. It is user research with customers plus sitting in on sales development, account executive and customer success phone calls to hear the questions and pains prospects raise. That raw material then gets mapped to different parts of the sales funnel so the blog covers the buying journey rather than one stage. This puts the content manager in the room where objections are spoken aloud, which is where the specific language and specific problems come from.

> "sit in on SDR (Sales Development Representative)"

**Evidence:** Grow and Convert credit this process, run across three companies, with producing hundreds of leads that converted to sales conversations.

**How to do it**

1. Book a standing slot to listen to at least two SDR calls, two AE calls and two customer success calls each week.
2. Log every question a prospect asks and every objection raised, in the prospect's own words, in a single sheet.
3. Tag each entry with the funnel stage where it came up: awareness, evaluation, or post-purchase.
4. Cluster repeated entries and turn each cluster into a post topic, keeping the prospect's phrasing in the working title.
5. Check each topic against search volume afterwards, not before, so a real recurring question with low volume still gets written.
6. Hand the topic to the writer with the raw quotes attached so the draft carries the customer's language.
7. Re-run the listening cycle quarterly, since the objections change as the product and market move.

**Pitfall:** Delegating topic choice to the writer produces topics that sound plausible but miss the real objections, because the writer has never heard a prospect speak. The signal is posts that rank but generate no sales conversations.

**Apply at Pabau:** David should sit in on Pabau demo and onboarding calls and log the questions clinic owners ask, then build blog and template topics from that log rather than from keyword exports alone.

**Apply anywhere:** Take topic selection away from writers and source it yourself by listening to sales and customer success calls, logging every question in the prospect's own words.

### 9. Source tool and content topics from user research, then check volume  `100.20`
*core · concrete actions · source 100*

Grow and Convert describe user research as critical to their entire content marketing process, and the Pilot example shows the order of operations. They learned through user research that Pilot's customers were really into figuring out their burn rate. Only then did they check that 'burn rate calculator' was a popular search term on that topic, and only then did they build the calculator. The sequence matters because it prevents both failure modes. Starting from a keyword tool produces topics nobody in your customer base cares about; starting from research alone produces assets with no search demand. They tie the same logic to the mobile checkout study, noting that mobile ecommerce is a known pain point of their ideal clients, ecommerce executives trying to raise conversion, which is their pain point SEO principle.

> "we learned through user research"

**Evidence:** Pilot's burn rate calculator came from user research that identified burn rate as a customer preoccupation, then confirmation that 'burn rate calculator' was a popular search term; it ranked #2 within weeks.

**How to do it**

1. Run interviews with current customers and ask what numbers or decisions they keep struggling with.
2. Write each struggle down in the customer's own words, not in your product vocabulary.
3. Check search demand for each phrasing, including calculator, template and best-practice variants.
4. Keep candidates that are both a stated pain point and a searched term.
5. Confirm the topic is a pain point of your ideal client specifically, not of a wider audience you do not sell to.
6. Decide format from the query type: calculator terms want a tool, best-practice terms want data.
7. Drop research-only topics with no demand into social and email instead of the blog.

**Pitfall:** Skipping the research step means you code or write something useless. Grow and Convert warn explicitly that the value of a tool depends on doing the user research first.

**Apply at Pabau:** Pabau's topic pipeline should start with clinic owner interviews and support tickets, then confirm demand in the keyword tools. That ordering also decides whether a topic becomes a blog article, a template page or a calculator.

**Apply anywhere:** Start topic selection from customer interviews, record the struggle in the customer's own words, then check search demand for those phrasings. Let the query type decide whether you build an article, a template or a tool.

### 10. Split near-identical keywords when their SERPs rank different pages  `143.4`
*core · concrete actions · source 143*

Grow and Convert call this one of their key learnings of recent years and a differentiator of their agency strategy: build a dedicated page for each high-intent keyword, even when two keywords mean nearly the same thing. Their worked example is 'sick leave tracking' versus 'sick leave app'. The intent looks identical, both searchers want a tool to track employee sick leave, but the top results for the two terms are different pages. That difference is the signal that a separate page is available to win. They add the supporting mechanism from their conversation with Bernard Huang of Clearscope: you only get one SEO title, one H1 and one meta description, so a post aimed at several target keywords usually ranks for one of them, or matches none of the intents and ranks for none. This extends the existing one-page-per-keyword entry in the base by giving the actual SERP comparison test that decides when to split.

> "Although intent is very similar, Google is ranking different pages"

**Evidence:** Grow and Convert show Google SERP screenshots for 'sick leave tracking' and 'sick leave app' returning different top results despite near-identical intent.

**How to do it**

1. List the high-intent keyword variants for one topic, including ones that look like synonyms.
2. Search each variant and record the top 10 URLs.
3. Compare the result sets: if the overlap is low, treat the variants as separate targets.
4. If the same URLs rank across both, keep one page and target the higher-volume variant.
5. For each split target, create a dedicated page whose SEO title, H1 and meta description use that exact keyword.
6. Write each page against the specific SERP you profiled, matching format and depth of the pages already ranking.
7. Interlink the split pages so the cluster is navigable without cannibalizing the title tags.
8. Recheck the SERPs after three months to confirm the split pages hold distinct positions.

**Tools:** Google Search Console

**Pitfall:** Splitting on volume alone rather than on SERP difference produces two thin pages competing for the same results. The signal is both URLs flickering in and out of the same positions in Search Console.

**Apply at Pabau:** Before David creates another Pabau page for a variant like 'clinic software' versus 'practice management software', he should run the two SERPs side by side. Only split when the ranking URLs actually differ, otherwise consolidate into the stronger existing page.

**Apply anywhere:** Before creating a page for a near-synonym keyword, run both SERPs side by side. Only build a separate page when the ranking URLs actually differ; otherwise consolidate into the stronger existing page.

### 11. Start ideation from customer pain points, not from a keyword volume list  `96.2`
*core · best practices · source 96*

Grow and Convert invert the usual ideation order. Most teams ask what keywords they want to rank for, which of them have the highest volume, and what content ideas fit those keywords. Grow and Convert instead ask what the customers' pain points are, which of those pain-point topics can carry compelling content that weaves in the product as the solution, and only then which keywords match those topics. Their reasoning is that top-of-funnel high-volume terms have low purchase intent, so conversions and conversion rates stay low even when traffic arrives. Bottom-of-funnel long-tail terms have lower volume but much higher purchase intent and higher conversion rates, which usually produces higher conversion volume overall. They stress this is not SaaS-only; they use it for B2B and B2C, ecommerce and service businesses.

> "What are our customers' pain points?"

**Evidence:** Grow and Convert's stated agency experience across dozens of brands over four years, and the case studies in their Pain Point SEO and SaaS content marketing articles.

**How to do it**

1. List the pain points customers actually describe, from sales calls, support tickets and interviews.
2. Cut the list to pain points where your product is a credible, specific solution.
3. For each, write the content idea before touching a keyword tool.
4. Find the keyword that matches that idea, accepting low volume if purchase intent is high.
5. Drop any candidate where you cannot weave the product in as the solution.
6. Sequence bottom-of-funnel terms first and only add top-of-funnel guides once those are built.

**Pitfall:** Volume-first ideation fills the calendar with awareness posts that rank but do not convert, and the failure shows up as good traffic with almost no pipeline attributed to content.

**Apply at Pabau:** Pabau's keyword selection should start from what practice owners complain about, not from aesthetics-industry volume. Mine support tickets and demo-call notes for phrasing, then match keywords to those, especially for /templates/ and comparison pages.

**Apply anywhere:** Start ideation from the pain points your customers name, choose the content idea, then find the keyword that fits. Volume comes last.

### 12. Start with two bottom-funnel keyword families: best-category and comparison  `182.3`
*core · concrete actions · source 182*

Grow and Convert give the two concrete keyword shapes they attack first in B2B SaaS. The first is top and best product category keywords, with their own examples: best marketing analytics software, best visitor identification software, best video transcription software. The second is brand and product comparison keywords, with the examples HubSpot vs. Pipedrive and QuickBooks alternatives. They say most people searching these terms are actively looking to buy, which is why conversion rates run far above top-of-funnel content. The sequencing rule is that these come first, before anything higher in the funnel, because they produce results faster. Only when the bottom-funnel list is genuinely exhausted do they move up the funnel.

> "Best visitor identification software"

**Evidence:** Grow and Convert cite roughly 10x conversion rates on these terms versus top-of-funnel content across dozens of B2B clients.

**How to do it**

1. List every category label a buyer could use for your product and build a 'best <category> software' target for each.
2. Add the same list with the modifiers top, cheapest and for <segment>.
3. List every competitor and build one head-to-head 'X vs Y' target per pairing that includes you.
4. Add an 'X alternatives' target for every competitor and for every incumbent tool you displace.
5. Publish these before any category explainer, and only expand upward once the list is genuinely used up.
6. When you do move up, pick pain-point topics that have a direct product tie-in rather than general industry topics.

**Pitfall:** Teams stop after one 'best software' listicle and one competitor page, then declare the bottom of the funnel exhausted. It is usually dozens of pages once you enumerate every category label, segment and competitor pairing.

**Apply at Pabau:** Pabau should audit which of the two families is thinner: the best-software listicles by treatment and segment, or the competitor comparison and alternatives set. Fill the thinner one before commissioning more blog explainers.

**Apply anywhere:** Enumerate the two bottom-funnel families in full — best-category terms for every label and segment, comparison and alternatives terms for every competitor — and publish those before moving up the funnel.

### 13. Stop killing keywords with the volume times CTR times conversion math  `95.2`
*core · best practices · source 95*

Matt Goolding names the exact calculation that kills low-volume keywords in planning meetings: this keyword gets 20 searches a month, best case we rank first and take about 30 percent of clicks, so 7 clicks, and at a 2 percent conversion rate that is 0.14 leads a month, therefore not worth it. He says the logic looks sound and is wrong in practice, for two reasons. Monthly search estimates consistently understate the traffic a page gets once it ranks, often by a lot. And a mini-volume keyword chosen through pain point SEO carries far higher conversion intent than the 2 percent a top-of-funnel post gets. His replacement is to forecast conversions from comparable published pages you already own, not from the tool's volume figure.

> "that's 0.14 leads a month"

**Evidence:** Grow and Convert's Circuit comparison articles average a 2 percent conversion rate, with Route4Me Alternative at 4.5 percent, against a modelled 0.14 leads a month.

**How to do it**

1. Ban the volume times CTR times conversion-rate estimate as the sole reason to reject a keyword.
2. Pull three or four already-published pages that target keywords of similar intent and similar reported volume.
3. Record each one's actual monthly organic sessions and actual conversions, not its estimate.
4. Divide actual sessions by reported volume for those pages to get your own underestimate multiplier.
5. Apply that multiplier to the candidate keyword, then apply the conversion rate of your bottom-of-funnel cohort rather than a site-wide 2 percent.
6. Multiply the result by average deal value to get a monthly revenue figure.
7. Compare that figure with the cost of writing the article, and only then decide.
8. Recheck the forecast against reality three months after publication and update the multiplier.

**Tools:** Ahrefs, Google Analytics

**Pitfall:** Applying a site-wide conversion rate to a bottom-of-funnel page understates it badly. Grow and Convert see comparison pages convert at 4.5 to 6 percent while blog averages sit near 2 percent.

**Apply at Pabau:** When Pabau rejects a keyword for low volume, the rejection should be based on Pabau's own conversion data for similar comparison or template pages, not on a spreadsheet estimate. Most competitor-alternative terms will pass that test.

**Apply anywhere:** Do not reject a keyword using volume times click-through times conversion rate. Forecast from the actual sessions and conversions of comparable pages you have already published, then compare that against the cost of the article.

### 14. Stress-test a head keyword by listing everyone else who could search it  `105.2`
*core · concrete actions · source 105*

Grow and Convert give a fast disqualification test for high-volume head terms before any brief is written. They take 'project management', which Ahrefs shows at 65,000 searches a month, and write out the other people who plausibly type it: a parent whose child wants to major in it, a student writing a paper, a worker halfheartedly considering a career change, a grandparent trying to understand a job title, and an employee just handed the role. Once that list exists, the buyer is clearly a small fraction of the volume. They then confirm the read against the SERP, where the featured snippet is the Wikipedia definition page. The test is cheap and it stops teams from spending months on a term whose conversion rate will sit under 0.01%.

> "there's tons of searches per month and it's literally the topic"

**Evidence:** 'project management' at 65,000 monthly searches per Ahrefs returns the Wikipedia page as its featured snippet; Grow and Convert put conversion from such terms below 0.01% and often at 0%.

**How to do it**

1. Take the head keyword and write out at least five distinct people who could plausibly type it, other than your buyer.
2. Include the non-commercial cases: students, career-changers, curious relatives, journalists, people newly given the job title.
3. Estimate roughly what share of the volume your actual buyer represents once that list is written.
4. Search the term and read the featured snippet: a Wikipedia or dictionary definition means Google has judged the intent as informational.
5. Read the first ten result types; if none are vendor pages, the term will not convert regardless of position.
6. Add the commercial qualifier ('software', 'services', 'for [industry]') and search again to see whether the SERP flips to vendors.
7. Target the qualified variant and drop the head term to a later phase.
8. Only revisit the head term once the qualified pages rank and have built internal links into it.

**Tools:** Ahrefs

**Pitfall:** Teams justify the head term by arguing the low-intent searcher might buy years later. Grow and Convert point out that requires a chain of low-probability events, and no team has infinite resources. The signal is a high-traffic page with a conversion rate at or near zero.

**Apply at Pabau:** Before Pabau commissions anything on a head term like 'aesthetic clinic' or 'patient management', David should list who else searches it and check the snippet. If it returns a definition, the brief should be reissued against the qualified variant, such as 'aesthetic clinic software for medspas'.

**Apply anywhere:** Before committing to a high-volume head term, write out five non-buyers who could plausibly search it, then check whether the featured snippet is a definition page. If it is, drop the head term and target the qualified commercial variant instead.

### 15. Swap a high-volume homepage keyword for the low-volume exact-intent one  `139.2`
*core · concrete actions · source 139*

Keeper Tax first targeted 'business expense tracker' on the homepage because it had 1,100 searches a month and the client wanted traffic. Brandon found the searchers were business owners wanting full accounting software, not the 1099 contractors Keeper Tax served. On a Grow and Convert monthly Q&A, Benji and Devesh told him to retarget the homepage to '1099 expense tracker', a term with far lower volume but exact intent. The homepage had not been ranking for anything before the change. After retargeting, it jumped straight to position one, and conversions rose. The mechanism Brandon gives is that being the literal answer to the query beats being one of many broad options for a bigger term. He had to sell the pivot to the client first, because the engagement's agreed metric was visitors.

> "were not exactly looking for a 1099 expense tracker"

**Evidence:** Keeper Tax homepage moved from ranking for nothing to position one for '1099 expense tracker' immediately after retargeting; 'business expense tracker' had 1,100 monthly searches.

**How to do it**

1. Write down the exact customer your product serves, using the qualifier that separates them from the broad market.
2. List the homepage's current or intended target keyword and open its live SERP.
3. Read the top 10 titles and ask whether those pages serve your qualified customer or the broad market.
4. If they serve the broad market, generate the qualified variant by prefixing your customer's qualifier to the head term.
5. Check the qualified variant's SERP for whether any page is genuinely built for it.
6. Accept the lower volume and rewrite the homepage title, H1, URL if applicable, and opening copy around the qualified term.
7. Brief the client in advance that volume will look smaller and signups are the metric that will move.
8. Track signups from organic for 60 days after the swap and report conversions, not sessions.

**Tools:** Ahrefs

**Pitfall:** Clients who agreed to a traffic KPI will read the volume drop as a downgrade. Get the metric changed to signups before you make the swap, or the win looks like a loss on the report.

**Apply at Pabau:** Pabau's homepage and category pages should target the qualified term the buyer actually types, such as practice management software for aesthetic clinics, rather than the broad clinic software head term with more volume.

**Apply anywhere:** Retarget your homepage from the broad category head term to the qualified variant your exact customer types, and measure the change in signups rather than sessions.

### 16. Target action-intent long-tail keywords, not informational ones  `42.2`
*core · concrete actions · source 42*

Purely informational keywords are described as losing clicks to AI Overviews and ChatGPT, since searchers increasingly get their answer directly from the AI and never click through to a website. The recommended alternative is to prioritize action-intent keywords, searches where the person is looking to actually do something or call a business, using named examples like "voice notes for dentists," "emergency roofing repair Queens," and "broken boiler repair Tribeca," which combine a specific service, an urgency or specificity modifier, and often a hyper-local qualifier. The claim is that this class of keyword retains real commercial value precisely because an AI-generated summary answer doesn't satisfy someone who actually needs a roofer or a boiler repair right now; they still need to take action with a real business.

> "Voice notes for dentists, emergency roofing repair Queens, broken boiler repair Tribeca"

**How to do it**

1. For each core service or product you offer, brainstorm variations that add an action or urgency modifier such as "emergency," "same-day," "24/7," "repair," or "book."
2. Layer in hyper-local qualifiers, specific neighborhoods or districts rather than just city-level, to further narrow the intent, following the pattern of the given examples.
3. Filter out keyword candidates that are purely definitional or educational in nature, such as "what is" or "guide to" phrasing, since these are the ones most likely to be fully answered by an AI Overview without a click.
4. Prioritize the action-intent list over the informational list when deciding which three, or six, pages to build next.
5. Write each page so it clearly enables the action being searched for, such as a booking form, a phone number, or a clear call-to-action, rather than just explaining the topic (inferred page-design implication of "action-intent").

### 17. Target alternatives keywords for both categories your product displaces  `135.5`
*core · concrete actions · source 135*

Grow and Convert argue an innovative product is rarely in a category of its own, so competitor keywords still exist even when the category name does not. Their client competed with traditional video editors and with transcription sites, so both sides of the keyword landscape were available. They researched 'Rev alternatives' early because Rev is a popular transcription site, and they also found a smaller text-based editor with overlapping features and targeted its alternatives term. That second post became the top performer of the engagement, with 32 organic conversions in nine months and a 2.62% conversion rate. Their advice is to squeeze the competitor category for everything it has, because the pool of terms is small but the intent is the highest available.

> "was one we researched early on because Rev is a popular"

**Evidence:** The text-based editor alternatives post was Grow and Convert's top performer: 32 organic conversions in 9 months at a 2.62% conversion rate.

**How to do it**

1. List every tool your buyers currently use to do the job, split by the categories they belong to.
2. Add the near-competitors that share your specific mechanism, even if they are small and low-volume.
3. Generate 'X alternatives' and 'us vs X' for every name on both lists.
4. Ignore the volume estimate on the small direct competitors; the intent is worth more than the number.
5. Prioritize the direct-mechanism competitor over the big category leader, since those searchers already understand your approach.
6. Write each alternatives post as a fair comparison that names where the competitor is genuinely better.
7. Include the switching path: what happens to existing files, projects or data when they move.
8. Track conversions per alternatives post and expand into the runner-up names once the first ones rank.

**Tools:** Ahrefs

**Pitfall:** Only targeting the famous category leader. The alternatives term for the obscure competitor with your exact mechanism converts better, because those searchers have already accepted the new way of working.

**Apply at Pabau:** Pabau should keep alternatives pages for the big names but add them for smaller aesthetics-specific systems with overlapping workflows. Those searchers already want a clinic-specific record system, so the switching-path section matters more than the feature grid.

**Apply anywhere:** Build alternatives pages for both the category leaders you displace and the small tools that share your exact mechanism, and treat the small ones as higher priority despite lower reported volume.

### 18. Target alternatives to tools you do not actually replace  `109.8`
*core · concrete actions · source 109*

Grow and Convert extend the alternatives play to competitors that are not really competitors. The test is user overlap, not feature overlap. Their example: Leadfeeder identifies which businesses visit a B2B website. At the time it was built on top of Google Analytics and did not replace it, touching none of Google Analytics' traffic analytics or core features. They targeted 'google analytics alternatives' anyway. It converted very well, and the post, heavily edited since first publication, still ranks in the top five for the term. The reasoning is that a share of people searching for an alternative to a big adjacent tool are dissatisfied for a reason your product addresses, even though your product is not a substitute. The same logic points to targeting a term like 'payhawk alternatives' from a travel management tool.

> "which converted very well for them"

**Evidence:** Leadfeeder's 'google analytics alternatives' post converted very well and still ranks in the top five for the keyword years later, after heavy editing.

**How to do it**

1. List the large adjacent tools your customers already use, including ones you sit on top of rather than replace.
2. For each, estimate the share of its user base whose needs overlap with what you do.
3. Keep the ones where a meaningful subset would be better served by you for the job they care about.
4. Search 'competitor name alternatives' and check whether existing pages are generic roundups.
5. Write a genuine alternatives roundup that includes real substitutes, not only your own product.
6. Place your product in the list with an honest description of what it does and does not replace.
7. State plainly which reader should pick you and which should stay with the incumbent.
8. Track signups from the page rather than rankings alone, since the intent mix is wide.

**Tools:** Google Analytics

**Pitfall:** A dishonest roundup that positions you as a drop-in replacement for a tool you do not replace gets refuted in the first paragraph the reader checks. Say what you do not do.

**Apply at Pabau:** Pabau can target alternatives searches for adjacent tools aesthetic clinics use but that Pabau does not replace, such as standalone booking apps or accounting tools, as long as the article says clearly what Pabau covers and what it does not.

**Apply anywhere:** Target 'alternatives to X' for large adjacent tools whose users overlap with yours, even when you do not replace X. Write an honest roundup that names real substitutes and states plainly which readers should choose you.

### 19. Target buying-intent keywords even when the tool says under 20 searches  `106.3`
*core · best practices · source 106*

Grow and Convert's second named mistake is skipping high buying-intent keywords because a tool reports low volume. Two reasons: tools underestimate true volume, and the conversion rate more than compensates for the smaller audience. Their client Circuit ranked for dozens of keywords Ahrefs showed at under 20 searches a month and still got conversions from them. Six competitor comparison articles produced 149 organic signups in two years. One niche how-to produced 31 conversions in six months. A use-case article produced 12 conversions in four months. Their 'routific alternatives' post showed 0 to 10 monthly searches in Ahrefs but averaged around 70 pageviews a month. They add a secondary benefit: almost nobody targets these terms, so they are easier to rank for.

> "less than 20 organic searches per month"

**Evidence:** Circuit: 6 comparison articles produced 149 signups in 2 years; a niche how-to produced 31 conversions in 6 months; 'routific alternatives' showed 0-10 searches in Ahrefs but ~70 pageviews a month.

**How to do it**

1. Keep every candidate with clear buying-intent in the list regardless of reported volume.
2. Rank the list as high-intent high-volume first, then high-intent low-volume, and put low-intent high-volume last.
3. Publish the low-volume high-intent pages rather than parking them, since few competitors target them.
4. After three months, compare each page's actual GA or Plausible pageviews against the tool's reported volume.
5. Record the multiple you find between real sessions and tool volume and use it to discount the tool going forward.
6. Track conversions per page rather than sessions per page so low-traffic winners stay visible.
7. Re-run the list every quarter and promote any low-volume term whose real traffic beat the estimate.

**Tools:** Ahrefs, Google Analytics

**Pitfall:** Judging these pages on traffic dashboards kills them. A page with 70 sessions a month looks like a failure next to a 5,000-session explainer until you look at signups.

**Apply at Pabau:** Pabau should publish alternatives and use-case pages for aesthetic-practice software terms that DataForSEO reports at 0 to 20 searches, and judge them on demo requests rather than sessions.

**Apply anywhere:** Publish the buying-intent pages your tool reports at near-zero volume, and judge them on signups or enquiries rather than sessions. Tool volume is an underestimate and these terms have almost no competition.

### 20. Target keywords competitors aren't putting in their titles  `47.8`
*core · concrete actions · source 47*

Edward's own signature tactic, core to his paid course, Compact Keywords, is deliberately searching for keywords that competing websites are not targeting, meaning competitor pages don't have that specific keyword phrase in their page titles, URL slugs, H1s, or the beginning of their first sentence. His claim is that once you find such a keyword and then place it correctly in those exact four locations on your own page, you will rank for it relatively easily, because you're not competing against pages that have already claimed that exact phrase in their core on-page signals. He layers a second filter on top: prioritize overlooked keywords that also carry purchase or commercial intent, rather than just any untargeted phrase, since that combination of nobody targeting it plus people buy when searching it is what he considers the highest-value keyword-research hack.

> "find keywords that people aren't targeting"

**How to do it**

1. Pick a target topic or product area and pull a broad list of candidate keyword phrases, using a tool such as Google Keyword Planner, Ahrefs, Semrush, or DataForSEO (inferred).
2. For each candidate keyword, check the top-ranking competitor pages and note whether that exact phrase appears in their page title, URL slug, H1, and the beginning of their first sentence.
3. Flag any keyword where competing pages are not using that exact phrase in those four locations as an overlooked keyword opportunity.
4. Cross-reference the overlooked-keyword list against purchase or commercial intent signals, such as shopping ads or transactional modifiers like 'buy,' 'price,' or 'for [role]', to prioritize the highest-value subset.
5. Write or update a page targeting each prioritized overlooked keyword, placing the exact phrase in your own title, URL slug, H1, and first sentence.
6. Track rankings for these specific pages after publishing to confirm the pattern of ranking relatively easily holds (inferred).
7. Repeat this process systematically across your keyword universe rather than as a one-off exercise, since there are reportedly a very large number of these overlooked opportunities available.

### 21. Target long-tail purchase-intent terms your product pages cannot rank for  `112.2`
*core · concrete actions · source 112*

Grow and Convert's core B2C move is to find purchase-intent keywords that a general product page will structurally never win, then build a dedicated page for each. They use running shoes as the worked example. The head term is contested by every brand in the category, but variations such as 'running shoes with arch support', 'running shoes for flat feet' and 'running shoes with wide toe box' have lower competition and identical buying intent. Checking the SERP for 'running shoes with wide toebox' shows no general product pages in the top results; every ranking result is a page dedicated to that specific topic. Their reasoning is that Google ranks on ability to satisfy intent, and a specialized page does that better. They stress this is not solved by sprinkling the terms into an existing product page.

> "There are no general product pages ranking in the top search results"

**Evidence:** Grow and Convert's Clearscope pull on 'running shoes' surfaced flat feet, track and wide-toe-box variations, and the SERP for the wide-toebox term contained only dedicated pages.

**How to do it**

1. List your product category head terms, the ones your product pages already target.
2. Run each through a keyword tool such as Clearscope or Ahrefs and pull the modifier variations, not the head term.
3. Keep only variations that still describe a product someone would buy, and drop informational spin-offs.
4. Search each surviving variation in Google and count how many top-10 results are general product or category pages.
5. Prioritize the terms where zero or one general product page ranks, because that gap is what a dedicated page fills.
6. Decide per term whether it needs a single dedicated page or a list-style post presenting options.
7. Write the page so it explains how and why your product fits that specific use case, not just that it exists.
8. Do not attempt this by adding the phrases to an existing product page; build the separate page.

**Tools:** Clearscope, Ahrefs

**Pitfall:** If general product pages already own the top 10 for a variation, the gap is not there and a new page will just cannibalize your own listing. Check the SERP before writing.

**Apply at Pabau:** Pabau's product and feature pages target head terms like practice management software. David should pull the modifier variations around them, aesthetic clinics, medspas, physiotherapy, multi-location, and check which SERPs are held by dedicated pages rather than vendor homepages. Those are the ones that justify a new /blog/ or template page rather than an edit to the feature page.

**Apply anywhere:** Find the long-tail variations of your category keywords, check which of their SERPs contain no general product pages, and build a dedicated page for each of those. Adding the phrases to an existing product page does not work, because Google rewards the page that most specifically satisfies the query.

### 22. Target the customer's specific question, not the category definition  `126.15`
*core · best practices · source 126*

Grow and Convert restate a rule from one of their oldest posts: topics need to be as specific as possible, because most companies' best customers have very specific pain points. Their example is that a cloud security company's best leads are not asking what is cloud security, they are asking what does it take to become SOC-2 compliant. Yet most companies produce more of the former and less of the latter. They pair this with two other conditions for the content they are discussing: it must be closely related to the product or service, which they call bottom of the funnel, and it must not be journalism or entertainment but must address the specific questions or pain points of the company's target customer. Their examples of real client targets are concrete: alternatives to standup meetings, delivery software for small business, post-concussion nausea, time clock app with gps, enterprise reporting tool.

> "What does it take to become SOC-2 compliant?"

**Evidence:** Grow and Convert list client pieces ranking #1 for 'alternatives to standup meetings', 'delivery software for small business' and 'post-concussion nausea', and #6 for 'time clock app with gps'.

**How to do it**

1. For each category term you were going to target, write the specific operational question a buyer asks instead.
2. Check that question has its own search demand, even at low volume.
3. Verify the topic is close enough to the product that you can name the product in the piece without straining.
4. Reject topics you could not connect to the product in one sentence.
5. Build the calendar from the specific questions, and keep category definitions to a single reference page at most.
6. Track conversions per topic, not sessions, so specificity gets credited.

**Pitfall:** Filling the calendar with category-definition keywords because they carry higher volume. They attract researchers, not buyers, and produce content indistinguishable from every competitor's.

**Apply at Pabau:** Pabau should favor targets like how to migrate patient records from a specific system, or what consent forms an aesthetic practice legally needs, over broad terms like clinic management. Those questions let the product appear naturally and attract owners who are actively buying.

**Apply anywhere:** Replace category-definition targets with the specific operational question your best customers actually ask. Check the topic is close enough to your product to mention it in one sentence, and judge each topic on conversions rather than sessions.

### 23. Target the direct service term, the highest-intent bucket of the three  `117.8`
*core · concrete actions · source 117*

Grow and Convert's Pain Point SEO framework has three buying-intent buckets: category keywords, competitor and alternatives keywords, and jobs-to-be-done keywords. This source adds their ranking of them for a service business. For almost every business they have worked with there is a handful of keywords with even higher intent than the pain-point ones: direct product or service terms, where the searcher is literally looking for the best option for a solution they have already decided on. For Cognitive FX that was 'best concussion clinic', targeted with a blog post titled 'How to Find the Best Concussion Clinics Near You', which ranks #1. The pattern is a blog post that reviews the category rather than a service page, because the SERP wants a guide.

> "there are a handful of even higher intent keywords than the pain point"

**Evidence:** Cognitive FX's 'How to Find the Best Concussion Clinics Near You' ranks #1 for 'best concussion clinic'.

**How to do it**

1. List every way a buyer would search for the solution category you sell: best X, X near me, top X providers.
2. Check what page type ranks for each; if guides rank, write a blog post, not a service page.
3. Write the post as a genuine buyer's guide covering how to evaluate options, criteria first.
4. Include your own service inside the guide with a clear statement of what makes it different.
5. Keep the set small; there are usually only a handful of these terms per business.
6. Track leads from these posts separately, since they convert at a higher rate than pain-point posts.

**Pitfall:** Firms answer these terms with a sales page and lose, because the SERP is showing comparison guides and the searcher wants evaluation criteria.

**Apply at Pabau:** Pabau should own the direct-service bucket for aesthetics: best practice management software, best clinic software, alternatives to named competitors. These are the smallest and highest-return set of pages on the blog.

**Apply anywhere:** Find the handful of direct product or service terms where the searcher is already shopping, and answer each with a genuine buyer's guide that includes your own offering.

### 24. Target the job done in a competitor or free tool, then argue the switch  `93.4`
*core · concrete actions · source 93*

Goolding's higher level of JTBD keyword combines the job with a competitor or a low-tech alternative. Timetastic knew people managed staff leave in Outlook, so they wrote 'How to add annual leave to your Outlook Calendar' even though Timetastic does not solve that problem directly. The link was that the Outlook process is convoluted, so anyone searching it is primed for something better, and Timetastic syncs to Outlook anyway. Circuit did the same with 'How to Plan the Shortest Route for Multiple Destinations in Google Maps'. Google Maps caps at 10 stops, the searchers are delivery drivers and reps, and Circuit integrates with Google Maps. He recommends this only after the pure category, comparison and 'how to' terms are covered, since it sits further up the funnel.

> "we wrote a post combining a job-to-be-done with an alternative"

**Evidence:** Timetastic's Outlook post: 20 free trial signups in 6 months. Circuit's Google Maps post: thousands of free trial signups since 2020, part of a case study scaling 920 to 14,577 sessions in 6 months.

**How to do it**

1. List the tools your customers use instead of you, including free ones like Excel, Google Sheets, Outlook and Google Maps.
2. For each, list the tasks people force that tool to do that it was not built for.
3. Search each task and confirm there is a real 'how to do X in [tool]' SERP with volume.
4. Keep only tasks where the incumbent method is genuinely awkward or capped, since that is what makes the reader switchable.
5. Confirm your product either integrates with that tool or removes the need for it, and write down which.
6. Write the full walkthrough for the incumbent tool, then the limits, then your product.
7. Track free trial or demo signups per post rather than traffic, so the topic's value is judged on conversions.
8. Only start this tier after your category, comparison and plain 'how to' keywords are already covered.

**Pitfall:** The keyword looks irrelevant on paper because your product does not do the thing being searched, so it gets cut in review. The test is whether the searcher is primed for a better solution, not whether you solve that literal query.

**Apply at Pabau:** Pabau should write how-to posts for the jobs clinics do in spreadsheets, paper diaries and Google Calendar: how to build a client record spreadsheet, how to track appointments in Google Calendar, how to make a treatment consent form in Word. Each ends with the Pabau argument.

**Apply anywhere:** Write how-to posts for the jobs people currently do in spreadsheets, calendars and other free tools, then use the limits of those tools as the argument for your product.

### 25. Target the manual workaround your product replaces, then argue the switch  `109.7`
*core · concrete actions · source 109*

Grow and Convert call these non-ideal alternatives. The searcher has named a solution that is not yours and, on a literal reading, is the opposite of your product. The example is a corporate travel tool such as TravelPerk and the keyword 'travel request form'. Anyone searching it is trying to organize business travel, either as an employee or as HR formalizing a process. A form is the antithesis of the software, so the keyword does not describe the product at all. The author argues it is still worth targeting because the search proves the pain point. He disagrees with the common advice not to sell hard to people who are not yet product-aware. In his experience, someone who demonstrates a pain point is open to a product that solves it, even when their search named something else entirely.

> "is an example of a non-ideal alternative"

**Evidence:** TravelPerk ranks for the term with an explainer; the author argues for either a downsides-led angle or targeting 'travel request form template' with a real template attached.

**How to do it**

1. List the manual methods, spreadsheets, forms and paper processes your customers used before buying you.
2. Turn each into a search query in the customer's words, such as 'travel request form' or 'staff rota template'.
3. Pull volume and check the SERP is dominated by generic templates rather than vendors in your category.
4. Decide the angle: either lead with the downsides of the manual method, or provide the template and argue the alternative alongside it.
5. Prefer the template variant of the keyword where one exists, because it gives you an asset to hand over.
6. Deliver the manual method properly first, including the actual template or steps, so the page satisfies the query.
7. Add a section naming the specific failure points of the manual route: version control, errors, time per request, approval delays.
8. Position your product as the way to stop doing it manually, without deleting the help you promised.

**Pitfall:** Publishing only the downsides without delivering the thing the searcher asked for causes pogo-sticking. The author notes TravelPerk's existing page on this term and argues the template variant would serve it better.

**Apply at Pabau:** Aesthetic clinics still run consent forms, treatment records and appointment books on paper and in spreadsheets. Pabau's template pages should target those manual-method searches, hand over a usable template, then show where paper consent and spreadsheet scheduling break down.

**Apply anywhere:** Target the manual workarounds your product replaces, in the customer's own wording. Give them the template or steps they asked for, then name the specific failure points of doing it that way and make the case for the software.
