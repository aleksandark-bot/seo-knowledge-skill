# Keyword Research — supporting (part 4 of 4)

24 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Stop approximating buyer context with long-tail keyword variants  `78.12`
*useful · content insights · source 78*

Grow and Convert argue that the old SEO answer to buyer variation, targeting longer-tail variants such as 'enterprise project management software' or 'project management software for small business', is insufficient. Those variants do not capture that one buyer is already on Jira and wants something specific Jira lacks, while another is buying a first tool having used pen and paper. There are effectively infinite specific requests and pain points for any solution, and Google had no good way to handle that personal context. AI search does. The practical consequence for keyword work is that the long-tail modifier is no longer a proxy for buyer situation, so situation-based content has to be planned separately from the keyword list.

> "going after a few longer tail variants when they exist"

**Evidence:** Grow and Convert contrast an enterprise buyer switching from Jira with a first-time buyer on pen and paper, both served the same ten blue links.

**Pitfall:** Treating segment modifiers like 'for small business' as full coverage of buyer context. You end up with a handful of pages standing in for dozens of distinct situations, none of which the page actually describes.

**Apply at Pabau:** Pabau's keyword plan should stop treating 'for med spas' or 'for clinics' modifiers as the segmentation layer. Situations like switching from a named competitor or moving off paper records need their own pages.

**Apply anywhere:** Segment modifiers on a keyword are not a substitute for buyer situation. Plan situation-based pages separately from your keyword list, since the specific circumstances buyers share with an LLM have no keyword equivalent.

### 2. Stop arguing about what counts as long-tail and use the two principles instead  `104.10`
*useful · content insights · source 104*

Grow and Convert are blunt that the long-tail definition is vague. The term comes from a curve plotting search volume against specificity, with head terms high-volume and low-specificity and long-tail terms the opposite. But what counts as low volume and how specific is specific enough both vary by industry, and rules such as three or more words equals long-tail are arbitrary. Their resolution is to stop classifying. If a term feels specific and has lower volume than the obvious head terms in your industry, it probably counts, and the label changes nothing about what you do. What matters is applying the two underlying principles: pick terms that are relatively easy to rank for, and pick terms that bring traffic which converts. The label is a taxonomy argument; the principles are the strategy.

> "those rules are arbitrary"

**Evidence:** Grow and Convert: what counts as low volume and highly specific differs between industries, so the definition stays deliberately loose.

**How to do it**

1. Drop any fixed word-count rule for classifying keywords as long-tail.
2. Set your own low-volume threshold relative to the head terms in your industry, not to a universal number.
3. Judge every candidate on two questions only: can we realistically rank for it, and will the traffic convert.
4. Keep a single prioritized keyword list rather than separate head and long-tail lists.
5. Order it by buying intent first and achievable ranking second.
6. Skip labeling entirely in briefs; specify the target query, the intent and the page type instead.
7. Revisit the volume threshold annually, since industry volumes shift.

**Pitfall:** Teams spend planning meetings deciding which bucket a keyword belongs in. The classification has no effect on what gets written, so the time is pure overhead and it delays the terms that actually convert.

**Apply at Pabau:** David should not maintain separate long-tail and head-term lists for Pabau. One list ordered by buying intent and winnability, with a note on page type, does the same job with less argument.

**Apply anywhere:** Abandon word-count definitions of long tail. Keep one keyword list ordered by buying intent and by whether you can realistically rank, and set your low-volume threshold relative to your own industry.

### 3. Stop using domain authority as a ranking ceiling  `120.9`
*useful · best practices · source 120*

Grow and Convert explain keyword difficulty and domain authority as the two metrics that decide what you can realistically target, then immediately limit how much weight either should carry. Both run 0 to 100. Higher difficulty means more competition; higher authority means a better chance of ranking. But they point out that if you look at the results for any keyword, the top listings are never sorted by domain authority, and lower-authority sites routinely outrank higher-authority ones. So authority is not the sole ranking factor and should not be treated as the end-all of ranking potential. Their instruction is to experiment with different difficulty levels and different competing authority scores to learn empirically what your own site can rank for, rather than filtering the list by a formula.

> "the top results are never sorted by DA"

**Evidence:** Grow and Convert note it is common to see lower domain authority sites ranking above higher authority sites for any given keyword.

**How to do it**

1. Pull keyword difficulty for your shortlist and your own domain authority from Ahrefs or Moz.
2. Open three or four target SERPs and note the authority score of each of the top ten results.
3. Confirm for yourself that the order is not authority-sorted, and note any low-authority page in the top three.
4. Read what that low-authority page does well: exact intent match, page type, specificity.
5. Publish deliberately across three difficulty bands rather than only below your assumed ceiling.
6. Record which band you actually reach the top ten in after three to six months.
7. Reset your working difficulty ceiling from that record, not from the tool's suggestion.

**Tools:** Ahrefs, Moz

**Pitfall:** Filtering the keyword list by a difficulty threshold before ever testing it. You discard winnable buying-intent terms and never learn where your real ceiling sits.

**Apply at Pabau:** Pabau should not drop high-difficulty buying-intent terms just because a tool score looks out of reach. David should run a deliberate spread of difficulty bands and set the ceiling from what pabau.com actually reaches.

**Apply anywhere:** Treat difficulty and authority scores as rough guides, not gates. Top results are never sorted by authority, so publish across several difficulty bands and set your ceiling from where you actually reach the top ten.

### 4. Swap head-term informational queries for branded comparison queries  `28.10`
*useful · concrete actions · source 28*

The concrete keyword shift behind the recovery was moving from broad 'before' queries like 'how to sign hello' or 'American Sign Language (ASL)', informational head terms fully answerable by an AI Overview, to 'after' queries like 'Does Duolingo have ASL?', a comparison and branded query positioned at the bottom of the funnel that both became the highest-performing article in the US and drove the most app-download conversions alongside a related 'alphabet in sign language' query.

> "The after query, taking the bottom-of-funnel example, would be"

**How to do it**

1. List your current top-performing informational or head-term queries, the 'before' set, and flag any showing the decoupling signature in GSC, meaning impressions steady, clicks falling.
2. For each flagged topic, identify an adjacent bottom-of-funnel comparison query a competitor or alternative product's name would appear in, such as 'Does [competitor] have [capability]?' or 'Is [competitor] good for [use case]?'.
3. Draft or prioritize content for these comparison-style 'after' queries ahead of further investment in the informational 'before' queries.
4. Track both query sets separately in GSC or rank tracking to confirm the comparison queries hold clicks better over time than the informational ones (inferred: create separate query filters or labels for 'before' versus 'after' style terms).
5. Once a comparison query proves to be a strong download or conversion driver, build closely related variants to compound the same effect.

**Tools:** Google Search Console

### 5. Tag single-keyword clusters as open, don't force-close them  `50.3`
*useful · best practices · source 50*

When auto-clustering keywords into topics at scale, the system ran into a specific failure mode: a new topic might start with just one matching keyword, and closing that cluster immediately, treating it as final, meant losing the ability to add more keywords to it later as new data arrived. Their fix was a distinct status called a "singleton," a cluster explicitly marked as still open even with only one keyword in it, so the system or a human can revisit it, actively search for more matching keywords, and populate it further over time instead of treating a one-keyword cluster as a dead end. This keeps the overall clustering system "dynamic" rather than static, which matters most for a database that's meant to keep growing indefinitely rather than being clustered once and left alone.

> "we created something called a singleton"

**How to do it**

1. When your clustering process produces a topic group with only one keyword in it, do not treat it as a finished or final cluster.
2. Add a distinct status value, such as "singleton" or "open," specifically for these thin, one-keyword clusters, separate from your normal active or closed cluster statuses.
3. Periodically re-run keyword discovery specifically against your list of open/singleton clusters to try to find more keywords that belong in each one.
4. Promote a singleton to a normal, fully populated cluster once it accumulates enough related keywords (inferred promotion threshold/rule).
5. Review your singleton list on a regular cadence, such as monthly, rather than letting them sit unexamined indefinitely (inferred maintenance cadence).

**Pitfall:** Treating a one-keyword cluster as closed or final silently caps how much a topic area can grow even when more matching keywords exist and just haven't been discovered yet.

### 6. Take category keywords from your closest competitors, not the biggest  `118.5`
*useful · best practices · source 118*

Grow and Convert add a selection rule most gap-analysis writeups omit: for the category bucket specifically, look at the competitors whose offering is most similar to yours, because their category keywords will actually map to your product. Their reasoning is the same one behind dropping features you lack. A large adjacent brand ranks for category terms describing products you do not sell, so its gap rows import noise. A near-identical competitor's category rows are close to a ready-made list. They also note the different names buyers use for the same category: an HR user searches 'email ticketing system' while a support user searches 'customer service software', and both are looking for help desk software. The closest competitor is the one most likely to have already found those synonyms for you.

> "We recommend looking at your closest competitors here"

**Evidence:** Grow and Convert's help desk example: 'help desk software', 'email ticketing system' and 'customer service software' are all the same category under different role vocabularies.

**How to do it**

1. Rank your competitor set by how closely their product overlaps yours, not by traffic or domain rating.
2. Use the top two or three of that ranking as the inputs for the category-keyword pass.
3. Pull the larger adjacent brands in a separate run, and use them only for the comparison and JTBD buckets.
4. From the close competitors' category rows, list every distinct name the market uses for your category.
5. Check each synonym against the buyer persona it belongs to, since different roles name the same product differently.
6. Assign one page per distinct category name rather than stuffing synonyms into a single page.
7. Ignore synonyms that describe a neighbouring category you do not compete in.

**Tools:** Ahrefs

**Pitfall:** Running the gap against the market leader because it has the most keywords. You get a long list dominated by their branded terms and by categories they sell into and you do not.

**Apply at Pabau:** Pabau's category pass should run against the practice management tools closest to Pabau's feature set, and the synonym list should cover how clinic owners, front-desk staff and injectors each name the software.

**Apply anywhere:** Pull category keywords from the competitors whose product is closest to yours, and use their rows to collect every role-specific synonym the market uses for your category.

### 7. Take long-tail terms organically because Google shows no ads on them  `131.6`
*useful · content insights · source 131*

Grow and Convert make an argument for organic over paid on very specific queries, and say they have tested it. Many long-tail buying queries do not have enough search volume for Google to decide to show ads at all, so a PPC program cannot buy that traffic even if it wants to. Rank organically for the same terms and the traffic and leads are enough to matter. They pair this with the point that paid display and paid social can target roughly the right person but cannot catch them at the moment they are looking for a solution, whereas a long-tail organic result appears exactly when the searcher has the pain point. They also note that long-form content gives the space to explain advanced features properly, space a paid unit or a short landing page does not have.

> "for Google to decide to show ads for"

**Evidence:** Grow and Convert say they tested this and found many long-tail queries carry no ads; ranking organically for them still produced meaningful traffic and leads for Smartlook.

**Tools:** Google Ads

**Pitfall:** Assuming a keyword is worthless because it has no ads and no CPC data. The absence of ads on a long-tail term is often a sign of an uncontested organic opportunity, not of no demand.

**Apply at Pabau:** When Pabau's keyword research shows a specific practice-workflow query with no CPC and no ad coverage, that is an argument to publish, not to skip. Paid cannot reach those searchers, so an article is the only way to be there.

**Apply anywhere:** When a specific buying query shows no ads and no CPC, treat that as an organic-only opportunity rather than as proof of no demand. Paid search often cannot serve these queries at all.

### 8. Target a definitional term only when the term is insider jargon  `135.8`
*useful · concrete actions · source 135*

Grow and Convert targeted 'rough cut video editing' even though a definitional term looks top of the funnel. Their reasoning was that 'rough cut' is not a common phrase outside video editing, so anyone searching it already has some experience with the craft. The term is also narrower than 'video editing': it names one specific part of the job, distilling footage down, which is exactly what the product does. They add a general observation from their experience that a fraction of searchers on definitional terms genuinely want a tool for the task even though they did not type 'tool' or 'software'. The title served both readings: 'What Is Rough Cut Video Editing? (And a Simple Tool to Do It)'. This is a usable filter for any 'what is X' term.

> "is not a super common term outside of the video editing realm"

**Evidence:** Grow and Convert cite the 'rough cut video editing' post as one of the mid-funnel set averaging 1.06% conversion, inside a program of 120+ conversions.

**How to do it**

1. Collect the 'what is X' terms in your space that describe a task rather than a concept.
2. Test whether the phrase is jargon by asking whether a layperson outside the field would use it; drop it if they would.
3. Check that the term names a narrower slice of the job than the head category term.
4. Confirm your product does that exact slice, not the whole category.
5. Read the top ten results and check whether any answer the definition and then recommend a tool; a SERP of pure definitions is the opening.
6. Title the post as the definition question plus a bracketed clause promising the tool.
7. Answer the definition properly in the first section, then move to the tool for the remainder.
8. Track conversion rate separately, expecting it below your bottom-funnel average but well above broad informational posts.

**Pitfall:** Applying this to a genuinely popular definitional term. If laypeople use the phrase, the traffic is students and browsers, and the post converts around the top-funnel rate of 0.5%.

**Apply at Pabau:** Pabau should treat clinical and operational jargon as fair game for definitional posts, for example 'what is a SOAP note' or 'what is a treatment plan template', while skipping broad terms like 'what is patient care' that anyone might search.

**Apply anywhere:** Target 'what is X' terms only when X is jargon insiders use, when it names a narrower part of the job than the category term, and when the current SERP is definitions with no tool recommendation.

### 9. Target competitor-vs-competitor comparisons your brand is absent from  `93.17`
*useful · concrete actions · source 93*

Goolding adds a move to comparison keywords that most brands miss. The obvious targets are terms containing your name, like quickbooks vs xero. He also recommends taking related searches that do not contain your brand at all, for example honeybook vs freshbooks, and inserting your product into that conversation. The searcher is already comparing two tools in your space, so they are actively evaluating, and a page that adds a third option meets them mid-decision. He gives the parallel for Asana: target trello alternative, podio alternative and monday.com alternative, plus the plural, plus 'alternative to' and 'alternatives to' phrasings, and note that some people search 'competitors' instead, with asana competitors at 2k monthly volume.

> "We might also tap into related searches that don't contain QuickBooks"

**Evidence:** Goolding cites asana competitors at 2k monthly volume, and honeybook vs freshbooks as an example of a pair to enter without owning either brand.

**How to do it**

1. List every named rival in your space, including ones you rarely lose to.
2. Generate every pairwise '[rival A] vs [rival B]' combination, not only pairs containing your brand.
3. Check volume for each pair and keep the ones with real search demand.
4. Write a genuine comparison of the two named tools, with disclosed criteria and who each one wins for.
5. Add your product as a third option in the same page, clearly labelled as yours.
6. Separately generate '[rival] alternative', '[rival] alternatives', 'alternative to [rival]' and 'alternatives to [rival]'.
7. Add the '[rival] competitors' phrasing, which carries its own volume, such as 2k for asana competitors.
8. Fact-check every claim you make about a named rival against their current public documentation.

**Tools:** Ahrefs

**Pitfall:** A comparison of two rivals that exists only to pitch you reads as a bait page and loses on intent. The comparison of the two named tools has to be fair and complete before your product appears.

**Apply at Pabau:** Pabau should build comparison pages for rival-versus-rival pairs in aesthetic practice software, not only Pabau-versus-rival pages, and add Pabau as a third option inside each.

**Apply anywhere:** Build comparison pages for rival-versus-rival pairs you are not named in, compare the two fairly, then add your product as a third option.

### 10. Target the hiring and in-house-build queries your service replaces  `93.15`
*useful · concrete actions · source 93*

Goolding extends the alternatives idea past software to people. For StrataPT, the alternative to physical therapy billing software is an outsourced team of humans who create claims, submit them and chase insurers, and building an in-house team to do the job is equally a competitor. He applies the same logic to Grow and Convert themselves, listing how to hire freelance writers, how to build a content team and how to write seo content, plus non-category alternatives like how to get more customers via social media. His illustration for SimpliSafe is hiring security and how to hire a security guard, with a teardown of the traditional approach: pros, cons, ways to recruit, then the modern alternative. The post gives real hiring guidance and then argues the reader can avoid the hassle, cost and risk of poor results by using the product instead.

> "how to hire freelance writers, how to build a content team"

**Evidence:** Goolding names StrataPT's outsourced billing teams and Grow and Convert's own targets: how to hire freelance writers, how to build a content team, how to write seo content.

**How to do it**

1. Write down every human-labour route a buyer could take instead of buying your product: hire, outsource, build in-house.
2. Generate 'how to hire [role]', 'how to build a [function] team' and '[role] job description' keywords for each.
3. Check volume and confirm the searchers are decision-makers, not job seekers looking for the role.
4. Write genuinely useful hiring guidance: where to source, what to pay, how to interview.
5. Add the cost comparison between the hire and your product, using real salary figures.
6. Name the risks of the human route that your product removes, such as turnover or inconsistent output.
7. Close with the product as the alternative, stated openly.
8. Exclude any query where the SERP is dominated by job boards, since that intent is candidates not employers.

**Pitfall:** Hiring queries split between employers and candidates. If the SERP shows Indeed and Glassdoor listings, the traffic is job seekers and will never convert.

**Apply at Pabau:** Pabau should target queries around hiring clinic receptionists and outsourcing patient admin, give real hiring advice, then show what Pabau automates that a hire would otherwise do.

**Apply anywhere:** Target the hiring and outsourcing queries for the work your product replaces, give real hiring guidance, then compare the salary and risk against your product.

### 11. Target the oversized tool category your narrow product replaces  `109.4`
*useful · concrete actions · source 109*

Grow and Convert call this overestimation of needs. Buyers routinely assume they need a large expensive platform when a specific tool would do. The example is Timetastic, an app built only to manage staff leave. It does not handle hiring, resource planning or payroll, but for many small businesses that broader functionality is overkill. People searching 'hr software for leave management' mostly do not need an HR suite. They need something that schedules and records leave. The keyword is deviant because Timetastic is not HR software, yet the searcher is a strong prospect. The article's job is to explain the distinction and show that the narrow tool solves the actual problem faster and cheaper. This only works when your product genuinely covers the searcher's underlying task.

> "Sometimes people assume they need a big expensive tool"

**Evidence:** Timetastic, a staff-leave app with no hiring, resource planning or payroll features, treated as a fit for 'hr software for leave management' searchers.

**How to do it**

1. List the broad software categories customers name when they first contact you, even when you are not in that category.
2. For each, write the specific task inside that category your product actually performs.
3. Search the broad category plus the specific task as a modifier, such as 'hr software for leave management'.
4. Keep terms where the modifier proves the searcher only needs the narrow function.
5. Check the ranking pages: if they are all full-suite vendors, a narrow product page has a differentiation angle.
6. Write the page opening with the distinction between the suite and the single job.
7. Show the cost and setup difference explicitly, since overkill is the reader's real risk.
8. Close by naming the narrow product as the fit for the job they described.

**Pitfall:** The angle collapses if the searcher really does need the wider suite. Read the modifiers: without a narrowing phrase, the query is genuinely a suite search and you will get high bounce and no conversions.

**Apply at Pabau:** Aesthetic practices often search for full EMR or hospital systems when they need appointment, charting and payment handling. Pabau can target those oversized category terms with a narrowing modifier and explain why a full hospital system is overkill for a single-site clinic.

**Apply anywhere:** Find the oversized software categories buyers name when your smaller product is the real fit. Target those categories with a task modifier, then use the page to draw the line between the suite and the single job, including the cost difference.

### 12. Translate the SaaS bottom-funnel patterns into service-business phrasing  `182.4`
*useful · concrete actions · source 182*

Grow and Convert note that the bottom-of-funnel keyword patterns are usually written up for B2B SaaS, and spell out the equivalent for service businesses. Their examples from actual client work are best virtual assistant service and business book ghostwriting service. The point is that the pattern is not software-specific: the searcher who types the service name with a buying modifier, or just the bare commercial service phrase, is as far down the funnel as someone comparing two SaaS tools. This matters for any business that sells delivery rather than a licence, and for products with a service component, where the buying phrase is often the plain name of the job to be done rather than a category plus the word software.

> "business book ghostwriting service"

**Evidence:** Grow and Convert cite best virtual assistant service and business book ghostwriting service as terms they tackled for B2B service clients.

**How to do it**

1. Write down the job your buyer hires you to do, in the buyer's own words, not your category name.
2. Build one target per service phrase with 'best' or 'top' prefixed.
3. Build one target per bare commercial service phrase, since the bare phrase is often already a buying query.
4. Add 'X vs Y' targets against named competing providers, and 'alternatives to X' where an incumbent provider dominates.
5. Check each phrase against sales call recordings or inbound emails to confirm buyers actually say it.
6. Keep the phrase even when the tool reports minimal volume, if the wording shows purchase intent.

**Pitfall:** Service businesses copy the SaaS template literally and end up targeting 'software' terms they cannot satisfy, drawing visitors who want a tool rather than a provider.

**Apply at Pabau:** Pabau sells software but its buyers hire it to do jobs — booking, recalls, consent forms, clinic reporting. Build the plain job phrase and its best-prefixed variant as targets alongside the practice-software category terms.

**Apply anywhere:** Restate the bottom-funnel patterns in the language of the job your buyer is hiring for, then build best-prefixed, bare-phrase, versus and alternatives targets from that language.

### 13. Treat branded 'can you' queries as lower-value but still worth targeting  `93.2`
*useful · content insights · source 93*

Goolding flags a sub-type of JTBD keyword that mixes a job with a brand name: can you use quickbooks for personal finance (150), can you integrate shopify with squarespace (30), can you add grammarly to outlook (20), can you sync asana with google calendar (20). He treats these with more skepticism than unbranded JTBD terms because a higher share of searchers already use the product named, so they are either committed elsewhere or already your customer. He still targets them for two reasons. If the brand is yours, the searcher may be doing final research on one use case and needs a nudge. If the brand is a competitor's, the query proves their current tool may not do the job, which is an opening to explain how switching solves it. Volumes here are small, so treat them as fill-in topics rather than the first pages you build.

> "We treat these with more skepticism because a higher proportion"

**Evidence:** Goolding's own volume estimates: 150, 30, 20 and 20 monthly searches for the four branded examples he gives.

**Pitfall:** These terms carry tiny volume, so a team that builds them early spends production capacity on 20-search-a-month pages before the category and comparison pages exist.

**Apply at Pabau:** Pabau should keep branded integration questions like 'can you sync [EHR] with Google Calendar' on a later tier of the roadmap, and when they are written, aim them at competitor-brand searchers rather than at existing Pabau users.

**Apply anywhere:** Keep brand-plus-job questions on a later tier of the content roadmap, and when you do write them, aim the page at people using a rival tool that cannot do the job.

### 14. Treat cost, timing and benefit questions as convertible consideration keywords  `111.5`
*useful · content insights · source 111*

Grow and Convert name a fourth keyword category for when bottom-funnel terms run out: consideration keywords, where the searcher is on the border of entering the market. Their four patterns are 'how much does it cost to [X thing your product does]', 'when to use [category]', 'how can [category] help me', and 'what are the benefits of [category]'. They give a worked example. A client sold book ghostwriting services to entrepreneurs, so they wrote 'how much does it cost to ghostwrite a book'. The post walked through every step, the monetary costs, and the time and effort of self-managing the ghostwriting and publishing process. By portraying how much work is involved in doing it yourself, the article made the case for the service without pitching it. That is the mechanism: an honest cost breakdown of the DIY route is the argument for the paid route.

> "How much does it cost to do [X thing your product or service does]?"

**Evidence:** Grow and Convert's ghostwriting client: a 'how much does it cost to ghostwrite a book' post that itemized the DIY steps, money, time and effort.

**Pitfall:** Writing the cost article as a vague range with no breakdown. Without the step-by-step of the DIY effort, there is no argument for buying, and the page reads as a top-funnel definition post.

**Apply at Pabau:** Pabau should own 'how much does practice management software cost' and 'how much does it cost to run an aesthetic clinic' style queries, with the full itemized DIY breakdown of spreadsheets, paper notes and separate booking tools that Pabau replaces.

**Apply anywhere:** Target cost, timing and benefit questions about the job your product does, and answer them with a full itemized breakdown of the do-it-yourself route. The effort you document is the argument for buying.

### 15. Treat near-synonym category terms as separate keywords with separate intent  `113.5`
*useful · concrete actions · source 113*

Grow and Convert warn against collapsing category keywords into one head term plus synonyms. Their example is a remote executive assistant service, where some prospects search executive assistant service, others virtual assistant service, and others administrative assistant service. They describe these as keywords that might be synonyms but have unique intent, and all pointing at what the business offers. The instruction is to identify all the different ways people might search for your category, including variations that indicate a slightly different intent or use case, not just synonyms. They add that long-tail variations such as executive assistant for startups or remote administrative assistant capture more specific intent and are often easier to rank for.

> "These keywords might be synonyms, but have unique intent"

**Evidence:** Grow and Convert's remote executive assistant client: three distinct search phrasings for the same service, each with its own intent.

**How to do it**

1. List every phrase a prospect might use for your category, including the terms your own team never uses internally.
2. For each phrase, run the SERP and compare the top five results; if the page types or angles differ, the intent differs and it needs its own page.
3. Add modifier variants to each root: for [industry], for [company size], for [use case], remote, free, near me.
4. Score each variant on how specific the intent is, and prioritize the specific ones because they are easier to rank for.
5. Map one page per distinct intent rather than one page stuffed with all the synonyms.
6. Check for cannibalization once published: if two of these pages swap positions for the same query, merge them.

**Tools:** Ahrefs, Semrush

**Pitfall:** Building one page for the head term and treating the synonyms as secondary keywords. Where the SERPs differ, that page half-serves each intent and ranks for none of them well.

**Apply at Pabau:** Pabau's category is searched as practice management software, clinic software, medical spa software and salon software, among others. David should check whether each of those SERPs looks the same before assuming one page can hold them all.

**Apply anywhere:** List every phrase people use for your category, compare the SERPs, and give each distinct intent its own page instead of stuffing synonyms into one.

### 16. Turn an informational keyword commercial by appending a product word  `106.5`
*useful · concrete actions · source 106*

Grow and Convert give a one-line repair for a candidate that fails the SERP intent check. If the keyword reads too top-of-funnel, add a version of 'software' or 'tool' to it and the intent flips. Their example pair is 'helpdesk' against 'helpdesk software'. The same move converts 'mental health journaling' into 'mental health journaling app'. This is worth doing before discarding a keyword, because the underlying topic is usually right and only the phrasing is wrong. The point is that the modified query pulls a different SERP, one made of product lists where a vendor page can plausibly rank and where your product can be pitched alongside the others rather than mentioned at the end of an explainer.

> "you often just need to add some version of 'software'"

**Evidence:** Grow and Convert contrast 'helpdesk' with 'helpdesk software' as the canonical example of the flip.

**How to do it**

1. Take any candidate that failed the top-ten SERP intent scan.
2. Append each of 'software', 'tool', 'app', 'platform' and 'system' to it in turn.
3. Search each variant and check whether the top ten flips to product lists and comparisons.
4. Keep the variant with the most commercial SERP and the most listicle-style titles.
5. Check the variant's volume in your keyword tool, expecting it to be lower than the informational parent.
6. Write the page as a product-category page for the variant, not as the explainer the parent term wanted.
7. Keep the informational parent in a parked list for after the buying-intent set is published.

**Tools:** Google, Ahrefs

**Pitfall:** Adding the product word to the title while writing the same explainer underneath. The SERP for the commercial variant is full of product lists, so a definition post with a commercial title ranks for neither.

**Apply at Pabau:** When a Pabau candidate fails the intent check, try the software variant before dropping it: 'patient intake' becomes 'patient intake software', 'clinic scheduling' becomes 'clinic scheduling software'. Those variants map to product-category pages Pabau can actually win.

**Apply anywhere:** When a keyword's SERP comes back informational, append 'software', 'tool' or 'app' and re-check. The variant usually pulls a commercial SERP you can rank a product page on, at lower volume but far higher intent.

### 17. Use CPC as a commercial-intent filter, not an ad-relevance check  `11.6`
*useful · concrete actions · source 11*

Gotch corrects a common misreading of cost-per-click data: CPC, pulled directly from Google Ads, isn't useful because you plan to advertise, it's useful as a signal that real advertisers are willing to spend money on that topic, which correlates with commercial intent. He explicitly warns against the 'blue ocean' instinct of treating a topic with zero advertisers as an untapped opportunity — his read is closer to the opposite: no advertiser spend on a topic more likely means it's informational intent or that advertisers already tested it and learned it doesn't convert, so 'no CPC data' should be treated as a caution flag, not a green light.

> "I wouldn't see that as an advantage or a blue ocean"

**How to do it**

1. Pull CPC for every keyword in the working list from Google Ads Keyword Planner, already part of the template columns.
2. Flag any keyword with meaningful CPC (inferred: above a threshold you set relative to your niche's typical CPC) as having validated commercial intent.
3. For keywords showing zero or near-zero CPC, do not treat this as a low-competition opportunity by default — check the other demand signals first.
4. Weight CPC as one input into the overall keyword score rather than a standalone go/no-go filter.

**Tools:** Google Ads Keyword Planner

**Pitfall:** Treating a zero-CPC, no-advertiser topic as a 'blue ocean' opportunity — Gotch's experience is the opposite: it's more often a sign advertisers already tried it and it doesn't convert, or that the query is purely informational.

### 18. Use competitor keyword lists only for brainstorming, never as a plan  `106.10`
*useful · best practices · source 106*

Grow and Convert's third named mistake is exporting every keyword a competitor ranks for or bids on and working down the list. Two reasons it fails. First, a competitor having lots of first-page rankings says nothing about whether those pages convert, so you inherit their low-intent terms along with the good ones. Second, relevance does not transfer. Their example: you sell scheduling software for lawyers, Calendly targets 'scheduling software for recruiting' and converts well from it, and you would convert almost nothing from the same term because you have no recruiting features. Their sequencing is explicit. Exhaust your own three frameworks first, and only look at competitors when you hit a roadblock generating ideas, then screen every borrowed keyword for intent and relevance.

> "This should only be used as a brainstorming tool"

**Evidence:** Grow and Convert's worked case: legal scheduling software copying Calendly's 'scheduling software for recruiting' would convert far fewer readers, if any.

**How to do it**

1. Build your own category, comparison and JTBD lists to exhaustion before opening a competitor export.
2. When ideas run out, pull a competitor's ranking and paid keyword lists in Ahrefs or Semrush.
3. Delete every borrowed keyword whose SERP fails the buying-intent scan.
4. Delete every borrowed keyword aimed at a segment or feature you do not actually serve.
5. For each survivor, write one sentence on why your product wins for that searcher; drop it if you cannot.
6. Check whether the competitor's ranking page is a category, comparison or JTBD page, and reuse the shape, not the topic.
7. Add survivors to the bottom of your own prioritized list rather than the top.

**Tools:** Ahrefs, Semrush

**Pitfall:** Assuming a competitor's rankings prove commercial value. They may be running the same volume-first strategy, in which case you are copying a list that is not converting for them either.

**Apply at Pabau:** Pabau should not work down a competitor's ranked-keyword export. Any borrowed term must name a segment Pabau serves, aesthetic and healthcare practices, and pass the SERP intent check before it enters the content queue.

**Apply anywhere:** Treat competitor keyword exports as a brainstorming source of last resort. Screen every borrowed term for buying-intent and for whether your product actually serves that searcher, and never work down the list unfiltered.

### 19. Use competitor rankings as the validation check on qualified keywords  `135.16`
*useful · concrete actions · source 135*

When Grow and Convert built the qualified bottom-funnel list, the last check on 'video text editing', 'online video editor' and 'collaborative video editor' was that competitors already ranked for them. That mattered more than volume for a product with no established category: if a comparable tool is ranking on a term, the term carries commercial demand and the SERP already accepts product pages as the answer. It also gives the strategic frame they used, which was to enter those spaces and pitch a more modern solution against what is ranking. This is a cheap validation step, run after generating qualifier variants and before committing to a post, and it also surfaces the competitor set for the alternatives keywords in the next stage of the plan.

> "these were all keywords that we noticed our competitors rank for"

**Evidence:** Grow and Convert used competitor rankings to confirm the bottom-funnel list that went on to average 2.7% conversion.

**How to do it**

1. Take the qualified keyword list you generated from your capabilities and put it into a rank-tracking or organic-research tool.
2. Run each of your named competitors through Ahrefs or Semrush organic research and export their ranking keywords.
3. Intersect the two lists and mark every keyword where a comparable product ranks in the top ten.
4. Read those SERPs and confirm the ranking pages are product or category pages, not general guides.
5. Prioritize the intersection over keywords with higher volume that no competitor ranks for.
6. Note the specific competitor pages ranking, and outline your post to beat that page rather than the abstract keyword.
7. Add every competitor surfaced by this exercise to the alternatives keyword list.
8. Re-run the intersection each quarter to catch terms competitors have newly moved into.

**Tools:** Ahrefs, Semrush

**Pitfall:** Treating a keyword no competitor ranks for as an untapped opportunity. Often the SERP simply does not reward product pages there, and you rank without converting.

**Apply at Pabau:** Before commissioning a Pabau page for a qualified term, check whether competing practice-management vendors already rank for it. If none do, read the SERP and confirm it is not an informational-only result set.

**Apply anywhere:** Validate qualified keywords by checking whether comparable products already rank for them and whether the ranking pages are product pages, and prioritize that intersection over higher-volume terms nobody in your category ranks for.

### 20. Use the alternatives angle for B2C products, not only B2B SaaS  `95.14`
*useful · concrete actions · source 95*

Matt Goolding notes that the competitor alternatives angle is not restricted to B2B software. Grow and Convert targeted the competitor of a company selling excessive sweating treatment products, a consumer purchase. The keyword showed only 10 monthly searches when they went after it. Over the following 12 months the post generated 15 monthly subscriptions to the treatment. That is a recurring consumer revenue stream from a single page on a 10-volume term. The mechanism is the same as in SaaS: someone typing a competitor's brand name plus alternatives has already decided to buy something in the category and is only deciding from whom. Consumer categories tend to have fewer companies willing to write these pages, so the SERP is often thinner than in software.

> "we targeted the competitor of a company that sells excessive sweating treatment products"

**Evidence:** Excessive sweating treatment client: a 10-volume competitor keyword produced 15 monthly subscriptions over a 12-month period.

**How to do it**

1. List the branded products or treatments customers compare yours against, including retail and clinic brands.
2. Generate '[brand] alternative', 'alternatives to [brand]' and '[brand] vs [yours]' for each, and check volume.
3. Keep the rows showing 10 or fewer searches; consumer alternatives terms rarely read higher.
4. Check the SERP for whether any competitor has written a dedicated page; in consumer categories often nobody has.
5. Write an honest comparison covering price, ingredients or specification, results timeline and who each option suits.
6. Include the qualifying detail a buyer needs, since consumer buyers convert on specifics rather than feature lists.
7. Place the purchase or subscription CTA above the fold and again at the comparison table.
8. Track subscriptions or orders per page monthly rather than judging on sessions.

**Tools:** Ahrefs

**Pitfall:** Consumer health and treatment comparisons carry claim risk. Anything about outcomes needs to be accurate and substantiated, or the page becomes a regulatory problem rather than a conversion one.

**Apply at Pabau:** Pabau's audience includes practices whose patients compare treatments, so comparison content works on both sides. On pabau.com the direct application is alternatives pages against other practice management vendors; the same logic can be recommended to practices for their own treatment comparison pages.

**Apply anywhere:** Run the alternatives play in consumer categories too. Competitor brand comparison terms often read 10 searches or fewer and still produce recurring orders, and consumer SERPs are usually thinner because fewer brands write these pages.

### 21. Use the incumbent tool's hard limits as the switch argument  `93.13`
*useful · concrete actions · source 93*

In the Circuit example Goolding names the specific mechanism that makes a JTBD-plus-alternative post convert. Google Maps can plan a route across multiple destinations, but it caps at 10 stops at once, and it is fiddly. Anyone searching that keyword who needs more than 10 stops has hit a wall the incumbent cannot move, which is a far stronger switch trigger than a general claim that the product is nicer. He pairs it with an audience read: a significant share of searchers are managing delivery routes or visiting multiple customers in a day, which is exactly Circuit's audience. And Circuit integrates with Google Maps, so the reader keeps navigating in the tool they know. The pattern is a documented hard limit, an audience match, and an integration that lowers the switching cost.

> "maximum 10 stops at once) that Circuit doesn't have"

**Evidence:** Circuit's Google Maps post has generated thousands of free trial signups since 2020, part of a case study scaling 920 to 14,577 sessions in 6 months.

**How to do it**

1. For each incumbent tool your buyers use, find its documented hard limits: row caps, stop caps, seat caps, feature gaps.
2. Verify the limit on the vendor's own documentation and cite it in the post.
3. Check the SERP for that job to confirm the searchers are your audience, not a different segment.
4. Write the walkthrough for the incumbent method up to the point the limit bites.
5. State the limit as a fact with a source, not as a complaint.
6. Show how your product removes it, with the specific number where you have one.
7. Name the integration that lets the reader keep using the incumbent alongside you.
8. Measure signups from the post to confirm the limit was the real trigger.

**Pitfall:** A limit that most searchers never hit is not a switch trigger. If the average searcher has 6 stops and the cap is 10, the argument lands on nobody.

**Apply at Pabau:** Pabau should document the hard limits of Google Calendar, spreadsheets and consumer booking tools for clinic workflows, such as no clinical notes and no consent capture, and use those exact limits in the how-to posts.

**Apply anywhere:** Find the documented hard limit in whatever tool your buyers use for the job, cite it, and use that limit as the switch argument rather than a general quality claim.

### 22. Use the suggested search hack plus Quora to source pain-point topics  `98.7`
*useful · concrete actions · source 98*

The research method Grow and Convert use to fill out a pain-point list when they cannot rely on lived experience. Hyam says to think of all the reasons someone would search for advice on the subject, and names two sources: the suggested search hack, meaning Google's autocomplete and related suggestions, and Q&A forums such as Quora. He adds a validation rule that matters more than the sourcing: if the specific reasons are corroborated by your own user research surveys or customer conversations, that is better than search data alone. In practice they used the suggested search hack over several weeks with Carob Cherub and surfaced 'Why Am I Fat' as a highly searched question, then checked it against the founder's own experience of having searched for that exact thing before committing to the post.

> "You could use the suggested search hack to figure out what people are"

**Evidence:** Carob Cherub's 'Why Am I Fat' topic came from several weeks of suggested-search work and was confirmed because the founder had searched for it herself.

**How to do it**

1. Type the broad topic into Google and record every autocomplete suggestion, then repeat with each letter of the alphabet appended.
2. Repeat with question stems: why, how, what, should, is.
3. Search the same topic on Quora and record the questions with the highest follower and answer counts.
4. Group the collected questions into the pain points they represent, not into keyword clusters.
5. Cross-check each pain point against your own user research surveys or customer conversations and mark the ones that are corroborated.
6. Prioritize the corroborated pain points, and treat the uncorroborated ones as a second tier.
7. Confirm the person the content is for has actually asked the question themselves before writing it.

**Tools:** Google, Quora

**Pitfall:** Autocomplete gives you phrasing, not demand or intent. A question that appears in suggestions but that no customer has ever raised in a conversation is the weaker bet, and Hyam ranks corroborated pain points above raw search data.

**Apply at Pabau:** When Pabau plans a cluster, run autocomplete and Quora on the seed topic, then check the resulting questions against what practice owners actually ask sales and support. Prioritize the overlap.

**Apply anywhere:** Source pain-point topics from Google autocomplete and Quora, then rank them by whether real customers have raised the same question in conversation. Corroborated questions beat high-suggestion-volume ones.

### 23. Validate with Keywords Everywhere or Semrush, then filter for the modifier  `64.2`
*useful · concrete actions · source 64*

The validation step, run two ways at two price points. He searches the seed term, uses the Keywords Everywhere Chrome extension's find-long-tail-keyword function, and separately runs the same term in Semrush looking for broad match keywords with low keyword difficulty - things he knows he can rank for quickly. His filter criteria are explicit: low competition, but with at least some search volume, because he doesn't want to write for a keyword with none. He discards the location-based results because they don't relate to the product. The move that finds the actual target is searching the list for the modifier pattern 'content strategy for' which surfaces 'content strategy for nonprofits', 'for SaaS', 'for inbound' - the audience-qualified variants are where the low-difficulty, real-intent terms live. In Keywords Everywhere the equivalent filter is the competition column, where higher means harder.

> "search that again"

**How to do it**

1. Search your seed term with the Keywords Everywhere extension active and use its find-long-tail-keyword function.
2. Run the same seed in Semrush filtered to broad match with low keyword difficulty.
3. Discard location-qualified results unless location is genuinely part of your offer.
4. Search the resulting list for the pattern 'seed term for' to surface audience-qualified variants.
5. Apply the two-sided filter: low competition, but non-zero search volume.
6. Pick the variant whose audience matches a segment you actually serve.

**Tools:** Keywords Everywhere, Semrush

**Pitfall:** He rejects one good low-competition term purely for having too little volume - the discipline is that low difficulty alone isn't the criterion, and neither is volume alone.

**Apply at Pabau:** The 'X for Y' modifier search is directly useful for Pabau: filtering any seed term for the 'for' pattern surfaces the segment-qualified variants - for med spas, for physios, for multi-location clinics - which is where low-difficulty, high-intent terms sit.

**Apply anywhere:** The 'X for Y' modifier search is directly useful: filtering any seed term for the 'for' pattern surfaces the segment-qualified variants - for small teams, for enterprises, for a specific vertical - which is where low-difficulty, high-intent terms sit.

### 24. Weak-authority sites should target 2 high-volume query templates first  `03.7`
*useful · concrete actions · source 03*

For a comparatively weaker brand (less budget, less historical data, less PageRank, less brand recognition than top competitors), the strategy is to deliberately target just a couple of high-volume query templates rather than spread thin — in the addiction-rehab example, does entity cause addiction, and can I take substance with substance. These were chosen because they are rich enough to generate high search volume and engagement across many entity variations, and every click, impression, and engagement event compounds to make the whole web entity more authoritative and trustworthy for its other query variations, which matters because a weaker brand needs to accumulate historical trust data faster than an established competitor would. This is combined with full entity-attribute coverage (30-plus addiction-type entities, each covered with the same set of sub-attributes: substances, habits, therapies, withdrawal symptoms, causes, risk factors, treatment durations) and internal links connecting these informational template pages back to commercial rehab-in-locale pages. The relationship is bidirectional: whenever an informational page's rankings improve, the commercial page it links to also ranks better.

> "you need stronger historical click data to convince search engines"

**How to do it**

1. If a site is a comparatively weaker authority in its vertical, do not try to cover every possible query template at once.
2. Identify the two (or a small handful) of query templates in the vertical that are rich enough to generate high search volume and engagement across many entity variations.
3. Build full entity-attribute coverage under those chosen templates: list every entity in the relevant class and cover each with the same set of sub-attributes.
4. Internally link each informational/templated page back to its corresponding commercial page, using both a within-page and a site-wide contextual connection.
5. Monitor whether ranking improvements on informational pages correspond to ranking improvements on the linked commercial pages, since the relationship is described as bidirectional.
6. Track historical click/impression/engagement data accumulation on the chosen templates over time as the leading indicator of increasing trust for the whole web entity. (inferred: via Google Search Console Performance report filtered to those query patterns)

**Tools:** Google Search Console

**Pitfall:** Spreading a lower-authority site's limited resources across too many query templates at once, instead of concentrating on the small number of rich-enough templates that can accumulate historical click/engagement trust data fast enough.
