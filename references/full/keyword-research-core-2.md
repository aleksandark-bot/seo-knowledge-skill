# Keyword Research — core (part 2 of 7)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Compare two SERPs before deciding new article versus re-optimization  `116.6`
*core · concrete actions · source 116*

Once Grow and Convert have a list of lost secondary keywords, they decide per keyword whether to write a new article or update the existing one. The test is SERP similarity between the primary keyword and the lost secondary keyword. They run a free SERP comparison tool, then read the ranking pages themselves rather than trusting the percentage alone. On their own post they compared 'saas content marketing' with 'b2b saas content marketing strategy': the two SERPs shared the same number one result, were 60% similar, and their single post appeared in both. That made re-optimization the answer. When the SERPs diverge enough, the secondary keyword earns its own article. They add a second source of new-article candidates: secondary keywords the post ranked for but never inside the top 10.

> "The SERPs are also 60% similar"

**Evidence:** Grow and Convert's 'saas content marketing' versus 'b2b saas content marketing strategy' comparison: same number one result, 60% SERP similarity, their post ranking in both at positions 5 and 8, so they chose re-optimization.

**How to do it**

1. Take each lost secondary keyword and pair it with the post's primary keyword.
2. Run both through a free SERP comparison tool such as Keyword Insights to get an overlap percentage.
3. Check whether the two SERPs share the same number one result.
4. Check whether your existing page appears in both SERPs at all.
5. Read the top-ranking pages for each keyword and note what they are positioning, not just which URLs match.
6. If overlap is high, the top result is shared, or your page ranks in both, re-optimize the existing post.
7. If the ranking pages address a different buyer, use case or solution type, commission a new article.
8. Add secondary keywords that never reached the top 10 to the new-article list as well.

**Tools:** Keyword Insights, Ahrefs

**Pitfall:** Deciding on the overlap percentage alone. Two SERPs can share URLs while the ranking pages address different buyers, in which case one page cannot serve both intents.

**Apply at Pabau:** Before Pabau splits a page, David should compare the two SERPs. Terms like practice management software and clinic management system usually overlap heavily, so one page serves both; where the SERP shows different buyers, build the second page.

**Apply anywhere:** Before splitting a page, compare the two SERPs. Near-synonyms usually overlap enough that one page serves both; where the ranking pages address different buyers, build the second page.

### 2. Confirm buying intent by checking what page type ranks first  `104.6`
*core · concrete actions · source 104*

Grow and Convert use the SERP itself as the intent test rather than reasoning about the wording. Their example is 'turkey tail mushroom spawn'. The phrase is less specific than a long how-to query, but the top result is a product page from a company selling mushroom spawn, and that is what confirms the searcher is shopping. The rule that falls out is simple: the page type Google ranks first tells you what Google has decided the query means. Product and pricing pages at the top mean commercial intent, so a comparison or use-case page can compete. A SERP full of blog posts and forum threads means informational intent, and a product page there will not rank no matter how well it is written. This check takes seconds and it overrides your own reading of the words.

> "the top result is a product page from a company"

**Evidence:** Grow and Convert confirm the buying intent of 'turkey tail mushroom spawn' from a product page ranking in position one.

**How to do it**

1. Search each shortlisted keyword in an incognito window set to your target country.
2. Classify each of the top five results as product page, category page, comparison post, how-to article or forum thread.
3. Mark the keyword commercial when product, pricing or comparison pages hold two or more of the top five spots.
4. Mark it informational when how-to articles and forums dominate, and demote it in the priority order.
5. Note any SERP feature present, since a shopping pack or product carousel is further confirmation of buying intent.
6. Match your planned page type to the dominant result type rather than to your preferred format.
7. Re-run the check before any refresh, because Google reclassifies query intent over time.

**Tools:** Google Search

**Pitfall:** Judging intent from word count or from the presence of 'buy' in the phrase. Plenty of commercial queries contain no purchase verb, and plenty of long specific queries are pure curiosity; only the ranking page types settle it.

**Apply at Pabau:** Before Pabau commissions a page, David should check whether the SERP for that term is software listicles and vendor pages or clinical how-to articles. A clinical SERP means the page belongs on /blog/ and will not drive demos.

**Apply anywhere:** Read intent off the SERP, not off the words. If product, pricing and comparison pages hold the top spots the query is commercial; if how-tos and forums hold them, it is not, whatever the phrasing suggests.

### 3. Cover category and comparison keywords in the first two months, JTBD after  `121.2`
*core · concrete actions · source 121*

Grow and Convert organize buying-intent keywords into three buckets and work them in a fixed order. In the first couple of months of a client engagement they focus heavily on category keywords and comparison or alternative keywords, because those have the clearest buying intent and the highest conversion rates. Only after the obvious bottom-of-funnel terms are covered do they add jobs-to-be-done keywords, and only after that do they consider moving up the funnel to broader awareness topics. The reason for the order is pool size against conversion rate. The category and comparison pools are small and finish quickly, and leaving them until later means the highest-converting pages get built last and the program's conversion numbers look weak in its first year.

> "we focus heavily on category keywords and comparison keywords"

**Evidence:** Grow and Convert's stated engagement sequence across dozens of SaaS clients.

**How to do it**

1. Split the keyword list into three tabs: category, comparison and alternatives, jobs-to-be-done.
2. Schedule every category and comparison term into months one and two, regardless of volume.
3. Publish the comparison and alternatives pages first inside that window, since they convert highest.
4. Mark the category and comparison pools finished only when every named competitor and every product-category phrasing has a page.
5. Move to jobs-to-be-done terms once those two pools are exhausted.
6. Delay top-of-funnel awareness topics until the whole bottom-funnel set is live.
7. Review conversions per bucket each quarter and reweight the next quarter's calendar on that split.

**Tools:** Ahrefs

**Pitfall:** Starting with jobs-to-be-done because the volume looks bigger. The program then spends its first year on mid-funnel pages while the highest-converting terms sit unbuilt.

**Apply at Pabau:** Pabau should finish the category pages and every competitor comparison and alternatives page before scaling the how-to library. Those pages are what a practice owner reads immediately before booking a demo.

**Apply anywhere:** Work your buying-intent keywords in order: category terms and competitor comparisons in the first two months, jobs-to-be-done terms after those are exhausted, and awareness topics last.

### 4. Cross-reference Google Ads conversion data with Search Console impressions  `08.10`
*core · concrete actions · source 08*

Beyond standard Search Console keyword research, the recommended tactic is to get access to a business's Google Ads account data specifically to see which keywords actually convert, since an advertiser spending heavily 'ranks for everything they want to' and generates real conversion signal that organic data alone doesn't show. A keyword showing strong Search Console impressions but minimal clicks even at position two is flagged as potentially not worth chasing to position one — but the Ads account's conversion data is what actually settles whether that keyword is commercially valuable despite weak organic click-through. The explicit access ask is read-only/reporting access only, never edit permissions, which is framed as an easier ask for a client or stakeholder to grant.

> "You see which keywords actually produce conversions"

**How to do it**

1. Request read-only reporting access to the business's Google Ads account, explicitly clarifying you don't need or want edit permissions.
2. Pull keyword-level Ads performance data: impressions, clicks, and conversions per keyword.
3. Pull the same keywords' Google Search Console data: impressions, clicks, and average position.
4. Flag any keyword showing strong GSC impressions but very low clicks even at a good position (e.g., 600 impressions/day but 3 clicks/month at position 2) as a candidate for further conversion-value checking rather than automatic prioritization.
5. Cross-check that flagged keyword against its Ads conversion data — a term can still be worth targeting in content/SEO if it converts well in paid, even with weak organic click-through.
6. Export the combined Ads-conversion and GSC dataset as CSVs for use in keyword prioritization.
7. Use this combined data set, not Search Console alone, to decide which keywords deserve dedicated SEO investment versus which are vanity-volume terms.

**Tools:** Google Search Console, Google Ads

**Pitfall:** Prioritizing keywords by Search Console impressions/position alone — a keyword can show strong impressions and position but negligible clicks or conversions; only the Ads account's actual conversion data reveals whether a term is commercially worth chasing.

### 5. Define 'easy keywords' as ones competitors don't fully on-page target  `42.1`
*core · concrete actions · source 42*

For a brand-new site, or one early in its SEO journey, the recommended first move is to publish exactly three pages targeting "easy" keywords, all linked from a single hub page or directly from the homepage. "Easy" has a precise operational definition here: a keyword is easy if other ranking websites are not putting that exact keyword phrase in their page titles, H1s, URL slugs, and the beginning of their first sentence, meaning competitors are ranking for it incidentally, not because they deliberately optimized for it. Finding and confirming this gap, rather than just picking low-competition-looking keywords from a tool, is the actual task: manually check the current top-ranking pages for a candidate keyword and confirm none of them hit all four of those on-page placements.

> "keywords where other websites are not taking these keywords"

**How to do it**

1. Brainstorm a shortlist of keyword candidates relevant to your core offering, prioritizing search terms you believe are under-optimized rather than simply low-volume.
2. For each candidate keyword, search it in Google and open the current top-ranking pages.
3. Check whether each top-ranking page has the exact keyword phrase in its page title tag.
4. Check whether each top-ranking page has the exact keyword phrase in its H1 heading.
5. Check whether each top-ranking page has the exact keyword phrase in its URL slug.
6. Check whether each top-ranking page has the exact keyword phrase at the beginning of its first sentence of body copy.
7. Classify the keyword as "easy" only if none of the current top-ranking pages hit all four placements together.
8. Select three such easy keywords and write one dedicated page for each.
9. Link all three new pages from a single hub or category page, or directly from the homepage, rather than leaving them orphaned (inferred internal-linking requirement, since the source says to link them from a hub or the homepage but doesn't specify the exact link placement).

**Pitfall:** This only works if you actually verify the on-page gap manually — a keyword that merely looks low-competition in a keyword tool isn't the same as one where every top-ranking page is failing to target the exact phrase in title, H1, URL, and opening sentence.

### 6. Define target segments from the one input your product requires  `135.2`
*core · concrete actions · source 135*

Before picking keywords for an innovative product, Grow and Convert defined who could use it at all. The editor works by editing a transcript, so it needs footage containing large amounts of dialogue. That single input requirement produced the segment list: marketers sitting on customer interview footage, user researchers distilling hours of interviews, and documentary filmmakers making rough cuts. Everything downstream, including 'how to edit an interview video', came from those segments rather than from a keyword tool. They then applied a fit test to each candidate keyword: does our product realistically solve this person's pain, and can we picture them signing up for a trial. If the answer was no, they added another layer of specificity rather than keeping the term.

> "teams that have footage with dialogue"

**Evidence:** Grow and Convert published 31 posts from this segmentation and 22 reached positions 1 to 10, with more than 120 conversions.

**How to do it**

1. Write down the input or precondition your product needs to work at all, for example dialogue-heavy footage or an existing patient list.
2. List every job role or team that already has that input sitting unused.
3. For each role, write the task they currently do badly with an inferior tool.
4. Turn each task into candidate search phrases in the words that role would use, not your product's words.
5. For every candidate ask two questions: does our product genuinely solve this pain, and would this searcher plausibly start a trial.
6. Drop or narrow any keyword that fails either question by adding a qualifier tied to the segment.
7. Assign one post per surviving segment-task pair.
8. Review the segment list quarterly as the product picks up features that change the required input.

**Pitfall:** Building the segment list from your total addressable market instead of from the product's hard requirement. You end up targeting people whose footage or data the product cannot process, and conversion collapses even at position one.

**Apply at Pabau:** Pabau's precondition is a practice that books appointments and keeps clinical records. David should build the keyword list from roles inside those practices, such as clinic managers handling multi-location rotas and injectors tracking consent forms, not from generic aesthetics marketing topics.

**Apply anywhere:** Start segmentation from the input your product needs to function, list the roles that already hold that input, and generate keywords from the tasks they currently do with worse tools.

### 7. Diagnose and fix keyword cannibalization using GSC query filters  `21.7`
*core · concrete actions · source 21*

David's cannibalization workflow starts in GSC's Performance report with a 'query containing' filter on a core term to see every page getting impressions for that term family - if one page already holds the large majority of clicks/impressions (his example: ~90%), there's no real cannibalization problem. Where several pages rank close together, he isolates each by the Page filter, checks which query each is actually winning, and shortens the date range (e.g., to 7 days) to rule out normal Google position-testing noise before concluding the competition is real. The resolution is to republish: strip the competing head-term out of the losing page's title/slug/anchor text (or, if the wrong page is winning, retarget that page's title/slug to the term it should own) and consolidate authority by de-indexing or redirecting the loser.

> "change the date range to seven days, to rule out"

**How to do it**

1. In GSC's Performance report, set the Query filter to 'Query containing' plus your core term (e.g., 'expert') to reveal every page getting impressions for that term family.
2. Check whether one page already holds the large majority of clicks and impressions (David's example: ~90%) - if so, treat cannibalization as a non-issue for that term.
3. Where impressions are spread across several pages ranking close together, flag that keyword family as a likely cannibalization case.
4. Switch the filter to Page and isolate one competing page to see exactly which queries it ranks for and at what position.
5. Shorten the date range (David uses 7 days) to rule out normal Google position-testing noise before concluding the competition is real and ongoing.
6. Check whether the page's top-ranking phrase belongs to a different page on your site, and note if its position there is too low to get clicks even though it's winning internally.
7. Check internal anchor text pointing at the competing pages - an internal link using the exact head-term as anchor text can be sending the wrong relevance signal to the wrong page.
8. Rewrite the losing or misfiring page to remove the competing head term from its title, slug, and body copy so it stops directly competing.
9. Alternatively, if the underperforming page should own the term, retarget its title/slug to match the winning query bucket exactly, then de-index or redirect the old duplicate to consolidate authority.
10. Recheck the GSC performance report a few weeks after republishing to confirm the target query's average position and CTR improved. (inferred)

**Tools:** Google Search Console

**Pitfall:** Assuming any two pages ranking for overlapping terms are cannibalizing without first checking click/impression share wastes effort - if one page already holds ~90% of clicks and impressions for the term family there's nothing to fix, and short-term position volatility can look like cannibalization when it's actually just Google's normal testing noise.

### 8. Do not let a technology differentiator change your topic prioritization  `110.8`
*core · best practices · source 110*

Grow and Convert record a specific pushback they get: 'my product is different, we have an AI to automatically add contacts to a CRM'. Companies with a technical advantage or unusual positioning assume they need a unique content approach. Grow and Convert say this is not true. From a search perspective the customer still searches for a CRM, or for the specific use cases a CRM solves. The differentiator belongs in the body of the content and in the trial or demo experience, where it does the work of winning the deal. It does not belong in the keyword selection, because nobody is searching for your unique mechanism. So the differentiator changes what you say on the page, not which pages you build.

> "this doesn't change the content strategy, specifically topic prioritization"

**Evidence:** Grow and Convert's response to the 'we have an AI that adds contacts to a CRM' objection: customers still search for a CRM and its use cases.

**How to do it**

1. Write out your differentiator in one sentence and check whether anyone searches for it in Ahrefs.
2. If volume is negligible, remove it from the keyword list and keep it as a messaging asset.
3. Select keywords on the category noun and the use cases the category solves, exactly as a generic competitor would.
4. Add the differentiator to the brief as a required section inside the body of each piece.
5. Make sure the demo or trial flow demonstrates the differentiator, since that is where it converts.
6. Revisit only if the differentiator starts generating its own branded or category search volume.

**Tools:** Ahrefs

**Pitfall:** Building the content calendar around a proprietary mechanism nobody searches for. The tell is a set of pages targeting your own invented terminology with near-zero impressions in Search Console.

**Apply at Pabau:** Pabau's differentiating features should be argued inside articles and in the demo, not used as keyword targets. Pabau GO and specific automation features belong in body copy on pages targeting the terms practices actually search.

**Apply anywhere:** Keep your technical differentiator out of keyword selection. Target the category noun and the use cases the category solves, and use the differentiator inside the body copy and the demo, where it wins the deal.

### 9. Do not trust Ahrefs traffic potential to explain a low-volume page's sessions  `95.5`
*core · content insights · source 95*

Matt Goolding works through Grow and Convert's own page targeting 'landing page vs blog post', a keyword Ahrefs reports at 10 monthly searches. The page ranks between 4 and 5. Ahrefs estimates 350 traffic for the page because it ranks for 63 other keywords, but when he checks those 63, none of them rank on page 1, and Google Search Console shows no queries delivering clicks in the last three months. The page still takes more than 100 organic sessions a month, 138 in May. Backlinko's CTR curve says position 4 or 5 on a 10-search keyword should give roughly one click a month. His conclusion is that the extra traffic comes from extremely long-tail searches that are not in any tool's database, so neither the volume figure nor the traffic-potential figure explains what a ranked page actually earns.

> "none of them are rankings on page 1"

**Evidence:** Grow and Convert's 'landing page vs blog post' page: 10 reported volume, ranking 4 to 5, 138 organic sessions in May, no page-1 rankings among its 63 other keywords.

**How to do it**

1. Pick five of your own pages that target keywords reported under 20 volume and that rank in the top 5.
2. Pull each page's actual organic sessions for a full month from analytics.
3. Pull the page's other ranking keywords in Ahrefs and check how many actually sit on page 1.
4. Pull the page's GSC query list for 3 months and note how much of the traffic those queries account for.
5. Calculate the gap between reported volume plus explainable rankings and the real session count.
6. Use that gap ratio as your house multiplier when forecasting new low-volume pages.
7. Repeat the check on high-volume pages so you know whether the multiplier is specific to the long tail.
8. Present the ratio to stakeholders when a keyword is challenged for low volume.

**Tools:** Ahrefs, Google Search Console, Google Analytics

**Pitfall:** Quoting Ahrefs traffic potential as the justification for a page backfires when someone checks the underlying keywords and finds they all rank on page 3. Use your own session data instead.

**Apply at Pabau:** When Pabau evaluates whether a published low-volume article worked, the measure is sessions and demo requests in analytics, not the traffic estimate Ahrefs prints next to the URL. Several Pabau template pages likely earn traffic from long-tail queries no tool records.

**Apply anywhere:** Judge a low-volume page on its real sessions, not on a tool's traffic-potential estimate. Ranked pages routinely earn far more than volume predicts, from long-tail queries no keyword database holds.

### 10. Drop any keyword whose SERP is Wikipedia, encyclopedias and scholarly articles  `108.4`
*core · best practices · source 108*

Grow and Convert give a fast disqualification test to run alongside intent classification. They do not prioritize high-volume top-of-funnel terms such as 'what is CRM', 'customer service tips' or 'project management best practices'. On top of that they discard keywords where the SERP itself proves purely informational intent, and their named signal is that the top results are Wikipedia entries, encyclopedias and scholarly articles. If that is what Google chose to rank, the searcher is not buying anything and no amount of product framing will change the page type Google wants. They do not call these keywords worthless. They say the terms build topical authority, add traffic and create internal linking opportunities into bottom-funnel pages, so they belong later in the program once high-intent opportunities are exhausted.

> "If all the top results are Wikipedia, encyclopedias, and scholarly articles"

**Evidence:** Grow and Convert's named disqualifiers: 'what is CRM', 'customer service tips', 'project management best practices', plus any SERP dominated by Wikipedia and scholarly results.

**How to do it**

1. Search each candidate keyword and look only at the domains in the top ten.
2. Mark the keyword informational when Wikipedia, dictionary, encyclopedia or academic domains hold three or more slots.
3. Move those terms to a parked tier rather than deleting them.
4. Keep working the terms whose SERPs show vendor pages, listicles, review sites or comparison posts.
5. Once the high-intent tier is published, revisit the parked tier for topical authority coverage.
6. Write each parked-tier post with internal links pointing into the bottom-funnel pages it supports.
7. Do not judge those posts on conversions; judge them on the rankings they help their link targets reach.

**Pitfall:** Treating an encyclopedic SERP as an opportunity because the volume is large. You can publish a good page and still never rank, because Google has decided the query wants a reference source, not a vendor.

**Apply at Pabau:** Pabau should run this check before commissioning definition-style articles. Terms with medical-reference or Wikipedia-dominated SERPs go to a parked tier, and only get written later as internal-link support for the software and template pages.

**Apply anywhere:** Check the SERP before committing to a definitional keyword. If Wikipedia, encyclopedias and academic sources hold the top slots, park the term and spend the budget on keywords whose SERPs show vendors and comparisons.

### 11. Drop broad match entirely and run phrase plus exact only  `156.3`
*core · best practices · source 156*

Grow and Convert note Google itself pushes broad match, showing an in-product message that says smart bidding plus broad match gets more conversions at similar or better ROI. They reject it. Their reasoning: with broad match, 'accounting software' can serve on 'bookkeeping companies that use quickbooks accounting software in Dallas, TX', which is useless if you sell accounting software. Phrase match on the same term shows for 'what is the best affordable accounting software', which they call a bit better. Exact match returns only that term or a close variant like 'accounting programs'. Their rule is that if you are running long-tail high-intent keywords, broad match has no place at all, and phrase match needs a negative keyword strategy behind it. They add that even when broad match does produce leads, in their experience lead quality is poor.

> "you shouldn't be using broad match at all"

**Evidence:** Grow and Convert cite Google's own interface prompt recommending broad match with smart bidding, and say lead quality from broad match campaigns is usually a poor fit.

**How to do it**

1. Filter the account by match type and list every broad match keyword.
2. Pause all of them rather than converting them in place.
3. Recreate the terms you still want as phrase match and exact match pairs.
4. Build a campaign-level negative list to protect the phrase match versions.
5. Ignore the in-product prompt recommending broad match with smart bidding.
6. Wait a full conversion cycle, then compare cost per lead and lead quality before and after.
7. If volume drops below target, add more long-tail exact terms instead of reopening broad match.

**Tools:** Google Ads

**Pitfall:** Cutting broad match drops impression volume immediately, and accounts under a spend target get talked back into it. Judge the change on lead quality over a full sales cycle, not on impressions in week one.

**Apply at Pabau:** Pabau's paid campaigns for practice management should run phrase and exact only, with negatives for adjacent verticals such as veterinary or dental where the product fit differs.

**Apply anywhere:** Remove broad match from the account, rebuild the terms as phrase and exact pairs, and support phrase match with a negative keyword list.

### 12. Drop competitor bottom-funnel terms that map to features you lack  `118.3`
*core · best practices · source 118*

Grow and Convert make a point most gap-analysis advice skips: a keyword's funnel position is a property of the relationship between the searcher and the vendor, not of the keyword. Their example is 'AI Chatbot' in the help desk gap report. For a competitor that ships an AI chatbot, it is a bottom-of-funnel category term with real revenue behind it. For a vendor that does not ship one, the same term is worthless, because the searcher's buying intent points at a feature you cannot sell them. Their instruction is blunt: if it does not apply, move on. This turns the gap report from a list of things competitors rank for into a list filtered by your own product surface, and it is the reason they insist on choosing the closest competitors rather than the biggest.

> "for your competitor isn't necessarily a relevant keyword"

**Evidence:** Grow and Convert's help desk walkthrough: 'AI Chatbot' is a strong opportunity for tools that offer one and a waste for tools that do not.

**How to do it**

1. Write out your shipped feature list, one row per feature, before opening the gap report.
2. For every category keyword in the report, name the feature or module a converting reader would be buying.
3. Delete the keyword if no shipped feature matches that intent, however high the volume.
4. Mark keywords that map to a roadmap feature as blocked rather than deleted, and revisit them at ship date.
5. For keywords matching a feature you ship weakly, check whether you can honestly claim parity in the article before briefing it.
6. Re-run this filter whenever a competitor ships something new, since their gap report will fill with terms you cannot serve.
7. Keep the deleted rows in a separate tab as product feedback about what the market expects you to have.

**Tools:** Ahrefs

**Pitfall:** Writing the article anyway and hedging the product mention. The reader converts on the feature, finds it missing at demo, and the page produces demos that sales cannot close.

**Apply at Pabau:** Pabau should filter every competitor keyword against the shipped feature list before briefing, and route the rejected rows to product as a record of what the aesthetics market expects.

**Apply anywhere:** Filter competitor bottom-funnel keywords against the features you actually ship, and drop any term whose converting reader would be buying something you do not sell.

### 13. Education and age change how people phrase searches  `47.7`
*core · content insights · source 47*

A Reddit commenter's observation, relayed by Edward, is that searchers with different education levels use meaningfully different search syntax for the same underlying question, which surfaces entirely different results. Their concrete example: someone with a high-school education searching about a celebrity's legal situation might type a gossip-style phrasing, which surfaces gossip-style YouTube videos, while someone with a master's degree might type a more formal phrasing, which surfaces a more analytical article from a publication like The Independent, even though both are asking essentially the same underlying question. The same commenter notes this effect extends beyond education level to age brackets, saying children and seniors search wildly differently from the core 25-to-54 demographic, and credits background reading in library science, specifically how people searched physical card catalogs before computers, with helping them understand the deeper patterns behind how humans phrase information needs.

> "will have very different search syntax when searching for the same thing"

**Evidence:** Direct example given: a gossip-style phrasing such as 'is Puffy going to jail' (high-school-education phrasing) surfaces gossip-style YouTube video results, while a formal phrasing such as 'has Puffy been formally charged' (master's-degree phrasing) surfaces a considered article from The Independent, despite both queries asking about the same underlying news story; the commenter also notes children and seniors search wildly differently from the core 25-54 demographic.

**Apply at Pabau:** When doing keyword research for a given topic, don't settle on a single best phrasing - map out how the same underlying question would likely be phrased by different education levels and age brackets among Pabau's actual buyer roles, such as a solo practitioner versus a practice manager with an MBA, since these different phrasings can return entirely different SERP result-types and may warrant genuinely different content, not just a single article targeting one phrasing.

**Apply anywhere:** When doing keyword research for a given topic, don't settle on a single best phrasing - map out how the same underlying question would likely be phrased by different education levels and age brackets among your actual buyer roles, such as a solo practitioner versus a practice manager with an MBA, since these different phrasings can return entirely different SERP result-types and may warrant genuinely different content, not just a single article targeting one phrasing.

### 14. Enumerate every synonym family for your service noun before touching a keyword tool  `120.2`
*core · concrete actions · source 120*

Grow and Convert argue that most companies badly under-count their own product and service category keywords. Their example is a client selling remote executive assistant services. The obvious term is 'executive assistant service'. But the real list ran across three separate noun families, each with its own modifiers: executive assistant, virtual assistant and administrative assistant, crossed with service, staffing agency, staffing firm, remote, outsourced and for startups. That produces about fourteen distinct high-intent terms out of one category. They say most clients are in the same position, because customers use different words for the same job. This is a different axis from adding a capability or vertical qualifier. Here you are changing the noun itself, not the modifier, and each noun family often has a separate SERP with separate competitors.

> "there are numerous ways people search for what they offer"

**Evidence:** Grow and Convert's remote executive assistant client: one obvious term expanded into roughly fourteen category keywords across three noun families.

**How to do it**

1. Write down the single most obvious noun for what you sell, for example 'executive assistant service'.
2. List every other noun a customer might use for the same job, including outdated and adjacent job titles.
3. Cross each noun with the delivery modifiers: remote, virtual, outsourced, online, managed.
4. Cross each noun with the buyer modifiers: agency, firm, service, software, for startups, for small business.
5. Run the full grid through Ahrefs or Semrush for volume, but keep zero-volume rows on the sheet.
6. Search each surviving term and confirm the SERP is commercial, not informational.
7. Check whether the noun families return different top-10 competitors; if they do, treat each family as its own page group.
8. Assign one dedicated page per term rather than folding synonyms into one page.

**Tools:** Ahrefs, Semrush, Moz

**Pitfall:** Teams stop at the noun their own marketing uses. If your site says 'practice management software' and buyers say 'clinic booking system', the second family never enters the sheet and a competitor owns it uncontested.

**Apply at Pabau:** Pabau's category sheet should not stop at 'practice management software'. Build the grid across clinic software, medical spa software, aesthetics booking system, EMR for aesthetics and salon and clinic management, each crossed with the modifiers Pabau ships, and give each surviving term its own page.

**Apply anywhere:** Do not stop at the noun your own marketing uses. Build a grid of every noun a buyer might use for your category, cross it with delivery and buyer modifiers, and check whether each family returns different competitors. Where it does, that family needs its own page.

### 15. Exhaust every bottom-funnel keyword before commissioning a single top-funnel post  `132.1`
*core · concrete actions · source 132*

Grow and Convert state the sequencing rule flatly at the end of the Geekbot case study: they moved up-funnel only after running out of buying-intent keywords. Over roughly two years with Geekbot they published 64 articles, 22 bottom-of-funnel and 42 top-of-funnel. The 42 top-funnel pieces were not a strategic choice made early; they were what remained once the bottom-funnel list was empty. Grow and Convert are explicit that the bottom-funnel count is company specific: some categories hold far more than 22 buying-intent terms, others far fewer. The practical instruction is to build and fully publish the bottom-funnel list first, treat its exhaustion as the trigger for moving up-funnel, and never let a top-funnel brief jump the queue because it looked more interesting to write.

> "Then, and only then, after we ran out of BOTF, did we move up-funnel"

**Evidence:** Geekbot, worked with since March 2020: 64 articles over about two years, 22 bottom-funnel (34.4%) and 42 top-funnel (65.6%), with top-funnel only starting after bottom-funnel ran out.

**How to do it**

1. Build the full bottom-funnel keyword list first: category software terms, competitor alternatives, brand-vs-brand comparisons, jobs-to-be-done and template terms.
2. Count the list and write the number down; this is your bottom-funnel runway, and it is category specific.
3. Publish every item on that list before commissioning any top-funnel brief, regardless of search volume differences.
4. Track conversions per published post so you can prove the bottom-funnel tier paid out before you spend on the next tier.
5. Declare the list exhausted only when new candidates are duplicates of published pages or have no purchase intent at all.
6. Only then start a top-funnel list, and restrict it to pain points your product addresses.
7. Re-run the bottom-funnel search every quarter, because new competitors create new alternatives and comparison keywords.
8. Move any newly discovered bottom-funnel term to the front of the queue ahead of queued top-funnel briefs.

**Pitfall:** Teams declare the bottom-funnel list exhausted after a dozen obvious terms because those keywords have low volume and feel unexciting. The signal is a content calendar full of guides while competitor-alternatives and template pages remain unwritten.

**Apply at Pabau:** Pabau should inventory every remaining bottom-funnel term before adding another broad aesthetics guide. That means practice management software by specialty, every competitor-alternatives page, every Pabau-vs page, and every code-reference and template page a buyer searches while shopping. David should keep a written count of the unpublished bottom-funnel list and treat a top-funnel brief as blocked while that count is above zero.

**Apply anywhere:** Build the complete buying-intent keyword list for your category and publish all of it before writing anything higher in the funnel. Count the list so you know your runway, and treat exhaustion of that list, not boredom with it, as the trigger to move up-funnel.

### 16. Exhaust the roughly 20 bottom-funnel terms before moving up the funnel  `111.1`
*core · concrete actions · source 111*

Grow and Convert describe the Geekbot engagement as a sequence, not a mix. Geekbot is a Slack app for asynchronous standups. They first targeted bottom-of-funnel terms such as 'daily standup software' (use case plus software) and 'Standuply alternatives' (competitor plus alternative). They say Geekbot had about 20 such terms in total. Only once that pool was exhausted did they move up the funnel to 'standup meetings waste of time', 'daily standup Excel template' and 'daily standup questions'. The count matters as a planning number: a B2B SaaS category typically supports a low double-digit number of true bottom-funnel keywords, so the bottom-funnel phase is a quarter or two of work, not a permanent strategy. Plan the mid-funnel phase in advance because you will reach it.

> "Only once we exhausted their BOF keyword opportunities"

**Evidence:** Geekbot had roughly 20 bottom-of-funnel keyword opportunities in total; Grow and Convert worked all of them before moving up the funnel.

**How to do it**

1. List every use-case-plus-software, industry-plus-software, competitor-alternatives and brand-vs-brand term for your product in one sheet.
2. Count them; expect roughly 15 to 25 for a single-product B2B SaaS, and treat that count as the length of phase one.
3. Order the list by how exactly the term names what you sell, not by search volume.
4. Publish one article per term until the list is empty, before writing any how-to content.
5. Track conversions per published article so the bottom-funnel benchmark is set before mid-funnel work starts.
6. Only when the list is exhausted, open phase two with pain-point and consideration keywords.
7. Re-run the bottom-funnel list every quarter to catch new competitors worth an alternatives page.
8. Keep the bottom-funnel pages refreshed; they stay the highest-converting assets after the pool runs out.

**Tools:** Ahrefs

**Pitfall:** Teams start mid-funnel because the volume looks better, so the small pool of highest-converting pages is built last and the program's conversion rate looks weak for a year.

**Apply at Pabau:** David should count Pabau's true bottom-funnel terms once and publish against that finite list first: practice management software by specialty, competitor alternatives, and brand-vs-brand pages. Everything on /blog/ that is a how-to waits until that list is empty.

**Apply anywhere:** Count your true bottom-funnel keywords once. For a single-product B2B tool it is usually 15 to 25. Publish one page per term until the list is empty, then move up the funnel.

### 17. Expand JTBD keywords across four query shapes, not just 'how to'  `93.1`
*core · concrete actions · source 93*

Matt Goolding of Grow and Convert says most teams stop at 'how to' when they build jobs-to-be-done lists and leave large amounts of demand on the table. He names four shapes. First, 'how to' queries such as how to sell furniture online (1.5k) or how to start a vending machine business (7.2k). Second, the same job without the word how, such as manage staff, hire movers or find therapist. Third, 'way(s) to' variants: best way to manage multiple projects (200), best way to file taxes online (700), easy way to clean oven (2.2k). Fourth, 'can you/can I' and 'should you/should I' questions such as can I manage my own rental property (100) or should I hire an interior designer (250). Each shape has its own volume pool and its own SERP, so run all four expansions before deciding the topic list is finished.

> "you can look into 'how to' keywords without the 'how' attached"

**Evidence:** Goolding lists volumes for each shape: how to screen record with sound 6.2k, ways to conserve energy 4k, should I lease or buy a car 3.8k, can you do your own taxes 300.

**How to do it**

1. Write out every job your product does for a customer in the customer's own words, one row per job.
2. For each job, generate the 'how to [job]' variant and check volume in Ahrefs.
3. Strip the 'how' and check the bare verb phrase separately, for example 'manage staff' or 'find therapist'.
4. Generate 'best way to', 'easy way to', 'safest way to' and 'natural way to' variants of the same job.
5. Generate 'can I', 'can you', 'should I' and 'should you' question forms for the same job.
6. Search each surviving variant and read the top 10 to confirm Google is not defaulting the SERP to a different intent.
7. Keep the bare-verb variant as its own target only when the SERP shows pages built for that exact phrasing, as with 'find a therapist'.
8. Drop any variant where the SERP is dominated by a different job than the one your product does.

**Tools:** Ahrefs

**Pitfall:** Google often collapses the bare-verb variant into the 'how to' SERP, so 'hire movers' returns 'how to hire' posts. Building a separate page for it then creates two pages chasing one result set.

**Apply at Pabau:** Pabau's keyword sheet should run all four expansions over practice jobs: how to reduce clinic no-shows, best way to manage patient records, should I hire a receptionist, plus bare forms like 'book patients online'. Each shape gets its own SERP check before a brief is written.

**Apply anywhere:** Run all four JTBD query shapes over every job your product does, then check each SERP separately before assigning pages, because the bare-verb and question forms often carry demand the 'how to' variant does not.

### 18. Expand category keywords across industry, product and software synonyms  `106.6`
*core · concrete actions · source 106*

Grow and Convert say the obvious category keywords run out after about half a dozen terms, and those few are the most competitive ones. Their expansion method varies one word at a time along three axes. For CRM software for legal professionals, the industry word varies into paralegal, attorney and lawyer. The product word varies into client intake software and practice management software. The word 'software' varies into tool, program and application. Then a fourth axis stacks use case and industry qualifiers, giving CRM software for small businesses, for healthcare, for freelancers. They accept these long-tail variants often have low volume, and argue the buying-intent is very high because the searcher is trying to find a tool to use, so they should not be passed up.

> "there are often more category keywords than appear on the surface"

**Evidence:** Grow and Convert's worked legal CRM example expands three obvious keywords into roughly a dozen variants across law, CRM and software axes.

**How to do it**

1. Write your three or four most obvious category keywords in a column.
2. Split each into its industry word, its product word and its software word.
3. Generate synonyms for the industry word, such as paralegal, attorney and lawyer for legal.
4. Generate synonyms for the product word, such as client intake software and practice management software for CRM.
5. Generate synonyms for the software word: tool, program, application, system, platform.
6. Cross-multiply the three columns into a full variant list.
7. Add a fourth pass of use-case and industry qualifiers, such as for small businesses, for healthcare, for freelancers.
8. Run each variant through the top-ten SERP intent check before pulling volume.

**Tools:** Ahrefs

**Pitfall:** Publishing a near-identical page for every synonym causes cannibalization. Group variants that return the same top ten into one page and only split when the SERPs genuinely differ.

**Apply at Pabau:** Pabau should run this expansion on 'practice management software': vary the vertical (medspa, dermatology, aesthetic clinic, injectables), the product word (patient management, clinic management, EMR), and the software word (system, platform, app), then SERP-check each before building pages.

**Apply anywhere:** Expand each obvious category keyword by varying its industry word, its product word and the word 'software' separately, then cross-multiply and add use-case qualifiers. The expanded list is less competitive and carries the same buying-intent.

### 19. Expand category keywords along feature, industry and format axes  `121.3`
*core · concrete actions · source 121*

Grow and Convert accept that the obvious category keyword is usually dominated by high-authority incumbents, but say there are far more variations than most companies realize. They name three expansion axes. Feature variations break the category into what it does: invoicing software, time-tracking software, payroll software. Industry variations attach a vertical: CRM for real estate, accounting software for nonprofits, HR tools for startups. Format variations swap the noun: scheduling app, scheduling tool, scheduling platform, scheduling system. Their explicit instruction is not to skip the low-volume results. A term like 'CRM software for law firms' might show 50 monthly searches, but if you sell CRM software for lawyers then every one of those searchers is a potential customer. The point of the axes is that they generate terms an incumbent has no page for.

> "expand your list by considering feature variations"

**Evidence:** Grow and Convert cite 'CRM software for law firms' at roughly 50 monthly searches as a term worth a dedicated page for a legal-focused CRM.

**How to do it**

1. Write down the plain category term your product sits in, such as 'scheduling software'.
2. Generate feature variations by listing each thing the product does and pairing it with the category noun.
3. Generate industry variations by pairing the category term with each vertical you actually serve.
4. Generate format variations by swapping the noun across app, tool, platform, software and system.
5. Run every combination through Ahrefs for volume, but keep terms under 50 searches instead of cutting them.
6. Drop any variation naming a feature or vertical you do not genuinely serve, since the page will not convert.
7. Check which variations a large incumbent already has a dedicated page for and deprioritize those.
8. Assign one page per surviving variation and track conversions per term.

**Tools:** Ahrefs

**Pitfall:** Filtering the expanded list by a volume floor deletes exactly the vertical and feature variations you can actually rank for, leaving only the head term you cannot.

**Apply at Pabau:** Pabau should run these three axes over 'practice management software': feature variations such as online booking software and clinic inventory software, industry variations such as med spa and dermatology practice software, and format variations across app, system and platform.

**Apply anywhere:** Break your head category term along three axes before deciding it is too competitive: feature variations, industry variations and format variations. Keep the sub-50-volume results, because those are the ones incumbents have no page for.

### 20. Expand each software category keyword across five variation axes  `108.3`
*core · concrete actions · source 108*

Grow and Convert argue the obvious category terms are only the start, and that the variations are where competitors have left gaps. They name five axes: use case ('[use case] software', 'tools', 'apps'), industry ('[industry] software', '[use case] software for [industry]'), business size ('for small business', 'enterprise [use case] tools'), integration ('[use case] software for QuickBooks', 'tools with Slack integration'), and feature ('time clock app with GPS'). The axes multiply. They point out a company with four use cases serving three verticals already has 12-plus combinations from those two dimensions alone, before integrations and feature qualifiers. This is a generation procedure rather than a filter: build the grid first, then SERP-check. The integration axis in particular is one most teams never build, and it maps directly onto whatever your product connects to.

> "A company with four use cases serving three verticals"

**Evidence:** Grow and Convert's worked example: four use cases across three verticals yields 12-plus category keyword variations before integration and feature axes are applied.

**How to do it**

1. Write down every distinct use case your product serves, in customer language not internal feature names.
2. List every vertical or industry you sell into.
3. Cross the two lists to produce '[use case] software for [industry]' for each pair.
4. Add the size axis to each use case: 'for small business', 'for enterprise', 'for multi-location'.
5. Pull your integrations directory and generate '[use case] software for [integration]' for each named partner.
6. Add feature qualifiers taken from your own differentiators, in the '[use case] software with [feature]' pattern.
7. Run the whole grid through a volume tool but keep zero-volume rows on the list.
8. Spend one to two minutes per surviving term on the SERP to confirm buying intent before assigning a page.

**Tools:** Ahrefs

**Pitfall:** Generating the grid and then cutting everything with no reported volume. The integration and feature variants almost always show zero in tools while carrying the highest purchase intent on the list.

**Apply at Pabau:** Pabau should build this grid explicitly: use cases (booking, consent forms, before-and-after photos, stock, invoicing) crossed with verticals (med spa, dermatology, dental, aesthetics clinics), plus integration terms for Xero, Stripe and Google Calendar, plus size terms for single-room and multi-location practices.

**Apply anywhere:** Do not stop at the obvious category keyword. Expand it across use case, industry, business size, integration and feature axes, then cross the axes, and keep the zero-volume combinations that carry real purchase intent.

### 21. Expand every buying-intent keyword across software, tool, platform and app  `145.1`
*core · concrete actions · source 145*

Grow and Convert argue most brands under-count their buying-intent keywords because people name the same product in several ways. They list four noun variants that each carry their own SERP: software (small business accounting software), tool (project management tool), platform (marketing analytics platform) and app (field service app). Multiply those variants by every industry or vertical the product serves and the list grows again. Their point is that a homepage plus a handful of product pages cannot rank for all of them, so each variant needs its own page. This is a keyword-inventory exercise, not a research exercise: the terms are predictable from your own product category, and each one is bottom-funnel because the searcher already wants to buy the category.

> "several different keyword variations"

**Evidence:** Grow and Convert's five years of conversion tracking across hundreds of client blog posts underpins the claim that these variant keywords are missed.

**How to do it**

1. Write down the product or service category in the plainest words a buyer would use.
2. Generate one candidate per noun variant: software, tool, platform, app, system, service.
3. Add every industry or vertical you serve as a prefix to each variant, so you get a grid rather than a list.
4. Check each candidate in Google and note whether the ranking pages differ between variants; different pages means a separate target.
5. Drop only the variants where the SERP is identical to one you already own with the same page.
6. Map every surviving keyword to a single dedicated page, and record which ones have no page yet.
7. Publish the missing pages as blog posts if the product-page template cannot carry that much specific copy.
8. Re-run the grid every time you add a vertical or a new product line.

**Pitfall:** Teams assume one product page covers all the variants because the intent looks identical. It does not: the SERPs differ, so a single page usually wins only one variant and loses the rest.

**Apply at Pabau:** David should build a keyword grid for Pabau's categories crossed with noun variants and verticals: aesthetic clinic software, medical spa app, patient management platform, injectables booking tool. Each cell that has no dedicated Pabau page is a page to commission.

**Apply anywhere:** Build a grid of your product category crossed with the noun variants buyers use (software, tool, platform, app) and every vertical you serve. Check whether the SERPs differ, then give each distinct SERP its own dedicated page.

### 22. Expand the one converting post into its full 'best X' keyword family  `138.3`
*core · concrete actions · source 138*

When Nat Eliason found 'best oolong tea' converting well on modest traffic, he did not treat it as a single win. He asked how to find more topics like it, then built out the whole product-type family. Cup & Leaf now hold top-three positions for best green tea, best oolong tea, best black tea, best white tea, best rooibos tea, best herbal tea, best pu-erh tea, best tea in the world and best jasmine tea. The procedure is mechanical once you have identified a converting shape: enumerate every value your catalogue takes for the variable in that shape and publish one post per value. Nine terms came out of one observation. This is the cheapest expansion available because the template, the internal structure and the CTA pattern are already proven on the seed post.

> "how do we find more article topics like this"

**Evidence:** Cup & Leaf hold top-three Google positions for nine 'best X tea' terms, expanded from the single converting 'best oolong tea' post.

**How to do it**

1. Identify the single best-converting post from the revenue-sorted audit and write its keyword as a template, for example 'best [tea type]'.
2. List every value the variable takes across your actual catalogue, not the values you wish you stocked.
3. Check volume for each variant in Ahrefs, but keep low-volume variants because the seed proved conversion is the constraint, not traffic.
4. Add the superlative and umbrella variants of the same shape, such as 'best [category] in the world'.
5. Publish one dedicated post per variant, reusing the structure and CTA placement of the converting seed post.
6. Point each post at the matching store collection rather than at a single product.
7. Track positions as a group; the family should reach top three collectively before you move on.
8. Once the family is exhausted, move to the modified shape 'best [category] for [problem]'.

**Tools:** Ahrefs

**Pitfall:** Teams stop after the two or three highest-volume variants because the rest look too small. The seed post already proved traffic is not the constraint, so cutting the tail cuts the highest-converting members of the family.

**Apply at Pabau:** Pabau's converting shape is likely a comparison or template page. Whichever /templates/ or alternatives page converts best, enumerate every value of its variable across aesthetics, dermatology, medspa and multi-location practices and publish one page each.

**Apply anywhere:** Turn your best-converting post's keyword into a template, enumerate every value your catalogue supports for the variable, and publish one page per value using the seed post's structure.

### 23. Expect bottom-funnel articles to convert about 25 times better  `106.2`
*core · content insights · source 106*

Grow and Convert publish the two-year Geekbot numbers as the case for buying-intent over volume. Articles targeting bottom-of-funnel keywords converted at 4.78 percent. Articles targeting top-of-funnel keywords converted at 0.19 percent, a gap they describe as 2,400 percent. The volume comparison is the more useful half. Twenty-two BOTF articles produced 28,190 organic pageviews and 1,348 conversions. Forty-two TOTF articles produced 204,303 visitors and 397 conversions. So roughly twice as many articles and close to ten times the traffic delivered under a third of the leads. They add a caveat that is easy to miss: they do not target BOTF exclusively, they start there and work up the funnel only after exhausting the bottom-funnel list.

> "4.78% conversion rate compared to just 0.19%"

**Evidence:** Geekbot, first two years: 22 BOTF articles, 28,190 pageviews, 1,348 conversions; 42 TOTF articles, 204,303 visitors, 397 conversions.

**Pitfall:** Teams quote the conversion-rate gap and then still commission top-funnel content for 'awareness'. The tell is a blog-to-signup rate under 0.1 percent while traffic charts go up.

**Apply at Pabau:** Pabau should report conversions per article cohort, splitting bottom-funnel pages like software comparisons and /templates/ from general explainers. If the split looks like Geekbot's, the explainer commissioning queue should stop until the comparison and alternatives set is complete.

**Apply anywhere:** Split your published articles into bottom-funnel and top-funnel cohorts and compare conversions, not traffic. Expect the bottom-funnel cohort to produce most leads from a fraction of the pageviews, and let that decide what you commission next.

### 24. Expect one post to rank for around 90 unrelated-looking keywords  `116.11`
*core · content insights · source 116*

Grow and Convert use their own article, written to rank for 'saas content strategy', as the worked example. It sits at position 5 for that target, but Ahrefs shows it ranking for roughly 91 other keywords, most of them synonyms, variations or semantically close phrasings. A good share of the post's traffic comes from that tail rather than from the target term. That is the mechanism behind the whole secondary keyword idea: a post's real footprint is far wider than the keyword it was briefed for, so both traffic and conversions can fall while the target keyword position never moves. They note Ahrefs and SEMrush both do this analysis, but Google Keyword Planner is not enough because it will not show what a specific URL ranks for.

> "it ranks for around 91 other relevant keywords"

**Evidence:** Grow and Convert's own 'saas content strategy' post ranks position 5 for its target and for around 91 further keywords, with a good percentage of traffic coming from those.

**How to do it**

1. Enter the URL, not the domain, into Ahrefs Site Explorer and open Organic keywords.
2. Count how many keywords the page ranks for beyond its briefed target.
3. Sort by traffic to see which keywords actually deliver visitors.
4. Mark the ones that carry buying intent as the page's secondary keyword set.
5. Record that set in the page's brief so future edits do not accidentally remove the language that earns them.
6. Repeat for every page you consider a converter, so its full footprint is documented before it declines.
7. Use a tool that reports per-URL rankings; keyword planners cannot do this.

**Tools:** Ahrefs, SEMrush

**Pitfall:** Judging a page by its target keyword position alone. A post can hold position 5 for its target while quietly losing the tail that was sending most of its traffic and conversions.

**Apply at Pabau:** Every Pabau converting page should have its full ranked-keyword list recorded in the brief. Editors then know which phrasings to preserve, rather than deleting the sentence that earns a secondary aesthetic-software term.

**Apply anywhere:** Record each converting page's full ranked-keyword list in its brief, so editors know which phrasings to preserve rather than deleting the sentence that earns a secondary term.

### 25. Expect one to four points more conversion rate from high-intent keywords  `128.14`
*core · general insights · source 128*

Grow and Convert summarize their pain point SEO approach as prioritizing high purchase-intent keywords over high-traffic keywords, and here they attach a figure to it. They report that articles built around high-intent keywords convert at between one and four percentage points higher on average than articles built around high-traffic keywords. That range is the number worth carrying, because it converts the argument from a preference into arithmetic anyone can run. A high-traffic keyword converting at 0.3% needs roughly ten times the traffic of a high-intent keyword converting at 3% to produce the same number of leads, and high-intent keywords are usually easier to rank for as well since they are medium to long tail. The figure also gives you a threshold to test against rather than accepting on faith.

> "between 1-4% higher"

**Evidence:** Grow and Convert report high-intent keyword articles convert between one and four percentage points higher on average than high-traffic keyword articles.

**How to do it**

1. Build two keyword lists: high purchase intent, and high volume with weak intent.
2. Estimate leads for each candidate as volume times an expected click share times an intent-adjusted conversion rate.
3. Use a one to four percentage point conversion premium for the high-intent list when running that comparison.
4. Order the roadmap by expected leads, not by expected sessions.
5. Set up per-article conversion tracking so you can check the premium on your own data after two quarters.
6. Publish the high-intent set first, since those keywords are usually medium to long tail and easier to rank.
7. Revisit the high-volume list only once the intent-driven set is published and converting.

**Pitfall:** Comparing keyword sets on traffic potential alone. A high-volume term at a fraction of a percent conversion needs an order of magnitude more traffic to match a high-intent term, and it is usually harder to rank for too.

**Apply at Pabau:** David should rank the Pabau content roadmap by expected demo bookings rather than expected sessions, applying a one to four point conversion premium to pain-point and comparison keywords over broad informational ones.

**Apply anywhere:** Rank a content roadmap by expected leads, not sessions, and apply a one to four percentage point conversion premium to high purchase-intent keywords over high-volume weak-intent ones. Then verify the premium on your own per-article conversion data after two quarters.
