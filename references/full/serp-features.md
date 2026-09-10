# SERP Features

10 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Click zone thresholds decide whether a page title matters  `21.1`
*core · content insights · source 21*

David defines a 'click zone' as roughly positions one-to-three for small/niche terms, up to one-to-seven for bigger terms, or one-to-sixteen for very large/competitive terms. Outside that zone, the page's title tag is effectively invisible to searchers regardless of how it's written, since nobody scrolls or pages far enough to see it. For low-authority sites specifically, cramming more words into a title increases the risk of dilution because Google has nothing precise to match the page to (his example: a blog titled 'Travel with Dave' won't rank for anything except literal searches for that exact phrase).

> "the click zone is roughly search position one to three"

**Evidence:** David's stated framework from his own SERP-tracking experience across many sites: click zone = positions 1-3 (small terms), 1-7 (big terms), or 1-16 (very big terms); titles on pages outside this zone get zero practical exposure no matter how they're optimized.

**Apply:** Before running any title-tag CTR experiment, first confirm the page already ranks inside its click zone for the target term size - testing title wording on a page ranking outside that zone is wasted effort, and low-authority pages should use narrow, specific titles rather than broad or purely branded ones so they can match to at least one real query.

### 2. Listicles and comparison pages still dominate AI citations  `40.9`
*core · content insights · source 40*

Despite widespread claims in the SEO community that listicles 'don't work' or look spammy, Kasra's own citation-tracking spreadsheet of AI Overview, Perplexity, and Claude citations shows the opposite: reviewing a live sample of 21 citations pulled for a query like 'best B2B marketing agencies,' he counted roughly 16 of them as listicle-format pages. His conclusion is that listicles 'definitely work' for AI citation right now, and that comparison-style content - directly comparing two or more things, pros and cons - is currently 'the easiest way to get into AI Overviews.' He caveats that Google could deprioritize the format at some point, and stresses that nobody actually knows the exact AI Overview formula, so this is an observed current pattern, not a guaranteed permanent one.

> "out of the 21 different citations, maybe 16 of them"

**Evidence:** Kasra's own citation-tracking spreadsheet, built by pulling AI Overview, Perplexity, and Claude citations for test queries: of a live sample of 21 citations he reviewed on screen, he counted roughly 16 as listicle-format pages.

**Apply at Pabau:** Don't deprioritize listicle and comparison/alternatives-page formats for Pabau's content plan based on the general 'listicles are dead' narrative - Kasra's own citation data says the opposite is currently true for AI Overview citation share, so pros/cons comparison formats remain one of the more reliable formats specifically for AI-citation visibility, provided the content stays factually neutral rather than misrepresenting competitors.

**Apply anywhere:** Don't deprioritize listicle and comparison/alternatives-page formats for your content plan based on the general 'listicles are dead' narrative - Kasra's own citation data says the opposite is currently true for AI Overview citation share, so pros/cons comparison formats remain one of the more reliable formats specifically for AI-citation visibility, provided the content stays factually neutral rather than misrepresenting competitors.

### 3. Measure share of page one as pixel area, then fill it  `58.4`
*core · concrete actions · source 58*

The organising idea both hosts use is share of the front page, not position. Cody describes it as a pixel area he is trying to own - what percentage of that visible region is my product - and shows Jesper's own branded SERP as the demonstration: his core site, an optimised landing page, a Reddit post, a Facebook post, a Twitter post, a Qwen chat, his homepage and a YouTube video, all targeting the same term. Historically Cody achieved this with guest blog posts written uniquely for each placement, targeting the same keyword. The second, less obvious reason to do it is defensive: if someone publishes something unflattering about you or your company, you go full force with Reddit, YouTube, Facebook pages, Instagram, Qwen, Manus, Perplexity, Bolt - create a page on each, see what ranks, and push the competition down.

> "pixel area that I'm basically trying to own"

**How to do it**

1. Search your target keyword and screenshot page one, then measure how much of the visible area your brand occupies.
2. List every property type on that page and identify which ones you can publish on.
3. Create one asset per property, each genuinely optimised for the same target keyword rather than duplicated.
4. Include your own site and one optimised landing page as the anchors.
5. Re-measure share of page after the assets index, and fill the remaining gaps.
6. For reputation defence, run the same process at speed across every available property to displace the unwanted result.

**Pitfall:** Duplicating the same content across properties is what gets it filtered - Cody's historical version specifically wrote unique articles for each placement.

**Apply at Pabau:** For Pabau's branded and comparison SERPs, the measurable goal is share of page one - Pabau's own page, its YouTube video, its LinkedIn presence and its listing on review sites all count, and the gaps are where competitors get to speak instead.

**Apply anywhere:** For your branded and comparison SERPs, the measurable goal is share of page one - your own page, your video, your social presence and your listings on review sites all count, and the gaps are where competitors get to speak instead.

### 4. Page one now runs on different rules from page two down  `58.1`
*core · content insights · source 58*

Jesper's central claim is structural: there is one set of rules for page one in Google and the normal ranking algorithm applies from page two down. His characterisation of what page one now contains is social media, YouTube videos, high-authority news sites and high-authority niche sites - and that is why parasite SEO works so well right now. You aren't beating the algorithm, you're qualifying for a different filter. Cody adds the commercial reason this matters more than it used to: the recent reduction in results per page from 100 to 10 means the front page is a smaller piece of real estate, so owning a larger share of it is worth more. The framing both return to is the front page as real estate you try to own with sites you control, guest posts on other sites, and user-generated content you get to rank.

> "certain set of rules for page one"

**How to do it**

1. Look at page one for your target keyword and classify each result by property type, not by domain quality.
2. If page one is dominated by social, video, news and high-authority sites, treat ranking your own page there as a separate problem from ranking it at all.
3. Count how much of the visible pixel area of that page your brand currently occupies.
4. Plan for share of page rather than a single position - your site, plus properties you can publish on, plus UGC you can influence.
5. Re-check periodically; both hosts note the composition of page one changes as platforms change their indexing rules.

**Tools:** Semrush

**Pitfall:** This is a practitioner's model of Google's behaviour, not a documented mechanism - but the observable input (what property types actually occupy page one for your keyword) is checkable and is what should drive the plan.

**Apply at Pabau:** For Pabau's priority keywords, audit what property types actually hold page one - if it's dominated by review sites, directories and YouTube, then getting Pabau represented on those properties matters more than another Pabau-hosted article.

**Apply anywhere:** For your priority keywords, audit what property types actually hold page one - if it's dominated by review sites, directories and video, then getting represented on those properties matters more than another article on your own domain.

### 5. 60,000 SERP snapshots show rankings churn constantly, not hold steady  `25.12`
*useful · content insights · source 25*

Koray built and open-sourced a GitHub repo called 'SERP Heartbeat' to empirically test whether Google rankings are actually fixed at a given moment. His team captured 60,000 snapshots of a single search engine results page taken nearly milliseconds apart and found rankings were not static; a page 'ranking third' might hold that position for only a few hours a day, cycling through first, second, fourth, fifth, sixth, or seventh at other times, with the duration of each position constantly changing. Standard rank trackers only sample a SERP once and report that as your position for a full 24 hours, which hides this constant churn — he calls the overall phenomenon 'liquid results,' and states AI Mode results are even more volatile than classic blue-link SERPs, tying the underlying cause partly to Google's deliberate SERP diversification (spreading impressions/clicks across more domains).

> "We registered 60,000 snapshots of a search engine results page"

**Evidence:** Koray's open-source 'SERP Heartbeat' GitHub repo: 60,000 SERP snapshots captured milliseconds apart on a single results page, showing rankings changing continuously rather than holding a fixed position; an animation was made showing positions swapping.

**Apply:** Treat any single-snapshot rank-tracker reading (e.g., 'we're #3 for X') as one sample of a constantly fluctuating position, not a stable fact — when reporting or troubleshooting rankings, avoid overreacting to one day's rank-tracker snapshot since the true position may be swinging across several spots within that same day.

### 6. AI Overviews and SERP features now directly suppress organic CTR  `11.7`
*useful · content insights · source 11*

Gotch flags organic CTR as 'absolutely huge' to factor into keyword selection because modern SERPs increasingly show an AI Overview, People Also Ask, local packs, and, for ecommerce, dense shopping results — and every one of these features competing for attention reduces the share of clicks that reach an organic listing, regardless of ranking position. His practical rule is that when projecting how much traffic a keyword target will actually drive, you must count the SERP features present and discount click expectations accordingly, rather than projecting traffic from ranking position and volume alone as if the SERP still looked like a plain ten-blue-links page.

> "the more it's going to distract the user from clicking"

**Evidence:** Gotch's framing that 'the more things that appear in the search results — whether it's an AI feature or a search feature — the more it's going to distract the user from clicking on your stuff,' and his later worked example where manually counting SERP features (an ad block, an AI Overview, People Also Ask, and others totaling six) becomes a scoring input that changes a keyword's calculated priority.

**Apply:** Before committing content resources to a keyword, manually check the live SERP for AI Overview presence and count other SERP features, and treat a feature-heavy SERP as a traffic-potential discount, not just a difficulty signal — a page could rank #1 organically and still see suppressed clicks if an AI Overview answers the query directly above it.

### 7. Build a linkable table of contents to earn snippet sublinks without schema  `74.8`
*useful · concrete actions · source 74*

David Quaid demonstrates a SERP result for 'what is Google LLC' where his own entry shows extra sublinks under the snippet. He says he creates those using a table of contents built with the Easy TOC plugin in WordPress. The headings are linkable, so people can link directly to individual questions they commonly ask. His key point is that this expanded result was achieved without any schema markup. He raises it in the context of the starter guide's 'influence how your site looks in search results' section, which he says is mostly about snippets and where you can genuinely make a difference. He pairs it with breadcrumbs: his blog posts show 'SEO blog' in the breadcrumb, FAQ pages show FAQ, term guide pages show term guide, which helps users understand from the snippet what they are getting.

> "I create these using table of contents"

**Evidence:** David's live SERP demo for 'what is Google LLC' showing his page with anchor sublinks, produced with Easy TOC and no schema.

**How to do it**

1. Install a table-of-contents plugin such as Easy TOC in WordPress and enable it on long-form posts.
2. Write H2s as the literal questions readers ask, so each anchor is a query in itself.
3. Confirm each heading generates a stable fragment anchor URL that can be linked externally.
4. Place the table of contents high on the page, above the first body section.
5. Set breadcrumbs so each content type shows a distinct label in the snippet, such as blog, FAQ or guide.
6. Check the live SERP for the page after a few weeks to see whether Google is pulling sublinks from the anchors.
7. Do not add schema to force this; David's example achieved it with no schema at all.

**Tools:** Easy TOC, WordPress

**Pitfall:** Treating schema as the route to rich snippet sublinks. David's example shows the anchors and headings did the work, and schema effort spent chasing this can be wasted.

**Apply at Pabau:** Pabau articles already use question-style H2s. David should confirm the table-of-contents anchors on /blog/ posts produce stable, linkable fragment URLs, and set breadcrumb labels so /templates/, /diagnostic-codes/ and /blog/ each show a distinct path in the snippet.

**Apply anywhere:** Add a linkable table of contents with question-shaped headings and distinct breadcrumb labels per content type, and expect the snippet sublinks without adding schema.

### 8. Google runs CTR competitions; it doesn't judge content quality  `21.4`
*useful · content insights · source 21*

David calls Google 'pretty much a confirmation bias engine': if a searcher looking for validation of one opinion (e.g., 'EMDs are bad for SEO') lands on a page arguing the opposite, they bounce - not because the content is wrong or low quality, but because it doesn't match what they wanted to find. This means two pages holding opposite positions on the same topic can post completely different click-through rates purely because of which exact query phrasing sent the visitor, and there is no dataset that lets Google (or anyone) objectively adjudicate a subjective claim like that. He stresses you cannot 'research' whether such content is objectively good or bad - Google isn't measuring that, it's measuring whether the click-through behavior holds up for that specific query.

> "Google is pretty much a confirmation bias engine"

**Evidence:** David's real GSC example: a page targeting 'EMD good for SEO' and a competing page targeting 'EMD bad for SEO' can hold opposite click-through rates on the same underlying topic, driven by searcher expectation/confirmation bias rather than any measurable difference in content quality.

**Apply:** Don't read a page's click-through rate as an objective quality signal from Google - a low CTR on a specific query phrasing may just mean the page's stance or framing doesn't match what searchers using that exact phrasing expect, which argues for creating distinctly-framed content for opposing search intents rather than one page trying to serve both.

### 9. Order page titles as keyword, then benefit, then brand  `52.5`
*useful · concrete actions · source 52*

For higher click-through rate, the recommended page-title structure is to put the target keyword at the very beginning of the title tag, follow it with the benefit or the searcher's underlying goal, and close with the brand name. Edward states this ordering "gets more clicks" and stresses it's not a new discovery — it's a formula that would have worked equally well 15 years ago — reinforcing his broader point that core on-page and SERP tactics are stable over time rather than constantly shifting.

> "the keyword at the beginning of the page title, then the benefit"

**How to do it**

1. Identify the page's primary target keyword.
2. Write the title tag starting with that keyword as close to the first character as natural phrasing allows.
3. Immediately follow the keyword with a short phrase naming the benefit or the underlying goal the searcher is trying to achieve.
4. Close the title tag with the brand name as the final element.
5. Check the resulting title length against your CMS's SERP snippet preview to confirm it isn't truncated in search results (inferred verification step).
6. Monitor click-through rate in Google Search Console for the page before and after reordering the title to confirm the change is helping (inferred verification step).

**Tools:** Google Search Console

### 10. Read a category SERP for who ranks and which format before commissioning  `103.2`
*useful · concrete actions · source 103*

Before Grow and Convert commit to a bottom-of-funnel category keyword, they read the SERP for three things. Who shows up: usually review sites like G2, Capterra and TrustRadius, plus direct competitors, plus peripheral players such as a marketing consultant ranking for 'best marketing analytics software'. What page types rank: review-site category listings, competitor home pages or product pages, and blog posts from bloggers, thought leaders and consultants. What format dominates: list articles are the most common because searchers want to understand their options, with conversion-focused landing pages second. The presence of a peripheral blogger or consultant in the top 10 is the signal that a blog post can win the term, since it proves Google is not restricting the SERP to review platforms and vendor product pages.

> "Types of pages: Review site pages listing products"

**Evidence:** Grow and Convert report the same three-part pattern recurring across SaaS category and comparison SERPs for their clients.

**How to do it**

1. Search the target category keyword and record the domain type of each of the top 10 results.
2. Tag each result as review site, competitor product or home page, competitor blog post, or peripheral publisher.
3. Count the peripheral publishers; if none appear, expect to need a product or landing page rather than a blog post.
4. Note the dominant format, list article or conversion landing page, and match it rather than inventing a third.
5. If list articles dominate, count how many products the top results cover and match or beat that range.
6. Check whether the ranking competitor pages are product pages, which tells you Google will accept a commercial page for the term.
7. Write the format decision into the brief before any keyword volume is discussed.

**Tools:** G2, Capterra

**Pitfall:** Publishing a blog post into a SERP made up entirely of review platforms and vendor product pages. The intent signal says Google wants a directory or a commercial page, and a listicle will stall outside the top 10.

**Apply at Pabau:** For Pabau's 'best practice management software' style terms, check whether Capterra and vendor pages own the whole SERP. Where a consultant or independent blog ranks, a pabau.com listicle is viable; where they do not, build a product or comparison landing page instead.

**Apply anywhere:** Before committing to a category keyword, classify the top 10 by page type and format. A peripheral blogger ranking means a blog post can win; an all-review-site SERP means you need a commercial page.
