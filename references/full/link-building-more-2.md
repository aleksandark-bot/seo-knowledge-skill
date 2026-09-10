# Link Building — supporting (part 2 of 3)

20 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Judge every link by whether it would pass real traffic  `24.5`
*useful · best practices · source 24*

The recommended filter for any prospective link — paid, exchanged, or earned — is whether a real person would actually click it, not merely whether it exists. Good examples given: a SaaS paying for a Beta List launch specifically for the referral traffic, a local business sponsoring an event whose sponsorship page sends people to the site, or a roofing company giving relevant expert commentary in an article people are actually reading. The quality bar is two-tiered: the minimum is that the linking page is indexed by Google, the higher bar is that it's indexed and still receiving real clicks — and a simple relevance sanity check (would an outside observer understand why this business is linked here?) helps flag likely spam placements.

> "they get links that don't pass traffic because they're just obsessed"

**How to do it**

1. For every prospective backlink, ask first whether a real person would actually click through it, not just whether it exists.
2. Favor paid placements tied to real traffic mechanisms (e.g. a product-launch listing site, an event sponsorship page, relevant expert commentary in an article people read) over placements chosen purely for authority metrics.
3. Apply a relevance sanity check to any placement: would an outside observer immediately understand why this business is linked here?
4. Rank placement quality on a two-tier bar: minimum is that the linking page is indexed; the higher bar is that it's indexed and still receiving real clicks.
5. Reject listings/placements confirmed (via a traffic check) to get no meaningful traffic, even if the link itself looks technically fine.
6. Treat "does this pass traffic" as a more reliable filter than raw authority metrics when allocating a link-building budget.

**Tools:** Ahrefs, Semrush

**Pitfall:** Pursuing links purely for their existence or authority metric ("obsessed with the backlink") instead of the real traffic and relevance they pass.

### 2. Judge link value by ranking ability, not DA/DR scores alone  `04.1`
*useful · best practices · source 04*

The core claim of this webinar-promo page is that popularity-style link metrics, Domain Authority, Domain Rating, Trust Flow, Citation Flow, and similar third-party scores, are commonly used to buy and sell links, but are meaningless when relied on in isolation, since a domain can carry a low trust flow or DA/DR score and still be a genuinely valuable link source. The stated alternative signals to check instead are whether the domain or page actually ranks in Google, whether it drives real organic traffic, and whether it holds a large, relevant query profile — these behavioral and performance signals are said to carry more real weight than raw popularity scores. The historical framing given is that link popularity became a ranking signal because early-2000s search engines were comparatively simple, so "more links, more popular" was an easy stand-in for quality, a heuristic the source argues no longer holds now that Google has grown far more sophisticated.

> "Weak domains can rank, can drive traffic and can have a large"

**How to do it**

1. Before dismissing a potential link source, or an existing backlink, based on a low DA, DR, Trust Flow, or Citation Flow score, check whether that domain or specific linking page actually ranks in Google for relevant terms (inferred check: search a few of its target keywords or use a rank-tracking tool).
2. Check whether the linking domain or page is genuinely receiving organic traffic using a traffic-estimate tool such as Ahrefs, Semrush, or SimilarWeb (inferred tool choice).
3. Check the size and relevance of the domain's query profile, i.e., how many distinct relevant keywords it actually ranks for, rather than relying on a single popularity score (inferred: use a ranked-keywords report such as Ahrefs' Organic Keywords or Semrush's Organic Research).
4. Weigh these ranking, traffic, and query-profile signals more heavily than the raw DA/DR/TF/CF number when deciding whether to pursue or keep a link.
5. Apply the same check in reverse during a link audit: don't assume a high-DA linking domain is automatically a valuable link if its individual linking page shows no ranking ability, traffic, or query profile of its own.
6. Document this evaluation criteria as a standing checklist so it's applied consistently across every future link-prospecting or audit decision, rather than re-deciding case by case (inferred operational step).

**Tools:** Ahrefs, Semrush, SimilarWeb

**Pitfall:** Treating DA, DR, Trust Flow, or Citation Flow as a standalone proxy for link value is explicitly called out as a mistake common in the spam-riddled link-selling industry — these metrics "in isolation are meaningless," since a domain with a low score can still rank, drive real traffic, and hold a large genuine query profile, which the source says carries more weight than popularity scores alone.

### 3. Learn expired domains through GoDaddy auctions before building anything  `67.16`
*useful · concrete actions · source 67*

For anyone who wants the skill without the infrastructure, Dirk gives a low-cost entry route. Subscribe to GoDaddy auctions, watch which domains are about to expire, and observe how the bidding wars actually run. Then practise valuation: take a batch of ten expiring domains, review each one properly, pick the three you think carry weight, and take that shortlist to a more experienced SEO to check your reasoning. His framing question is the useful part, which is to understand why a domain is weighted before it expires. He also plants a warning about the source: the domains still sitting on public auctions are there for a reason, and asking why they were left is part of the analysis.

> "subscribe to the example GoDaddy auctions"

**Evidence:** Dirk offers this as the alternative to building infrastructure, and says doing drop catching manually at scale is a waste of time unless you are doing it for fun.

**How to do it**

1. Create a GoDaddy Auctions account and subscribe to the expiring-domain lists in your niche.
2. Watch several live bidding wars end to end without bidding, and record the final prices.
3. Take a batch of ten expiring domains and run the full check on each: ownership count, Wayback timeline, niche continuity, live backlinks.
4. Write down which three of the ten you think carry real weight, and the specific reason for each.
5. Take that shortlist to a more experienced SEO and ask whether your reasoning holds.
6. For every domain still sitting unsold on the auction, write down why you think nobody took it.
7. Only after your picks start matching the experienced verdict, start bidding with a written maximum.
8. Turn the checks you used into a written SOP naming the tool and threshold at each step.

**Tools:** GoDaddy Auctions, Wayback Machine

**Pitfall:** Treating public auction listings as the good inventory. Dirk points out the contested domains never reach open auction, so what is left is there for a reason and needs the same scrutiny at a lower expected value.

**Apply at Pabau:** If Pabau wants to understand the expired-domain market before ever spending on it, one person can shadow GoDaddy auctions for a month and build the valuation SOP at almost no cost.

**Apply anywhere:** Learn expired-domain valuation by shadowing GoDaddy auctions for a month: review batches of ten expiring domains, pick your three, and have an experienced SEO check your reasoning before you bid.

### 4. Location relevance beats domain-authority minimums for these links  `30.5`
*useful · content insights · source 30*

Clients frequently ask for a minimum domain authority (e.g., DA 40) before accepting a link placement, but Ellen and Garrett say that's the wrong filter for local/relevance-based links — geographic and topical relevance outweighs raw website authority metrics, to the point that even an online-only nonprofit with no real website infrastructure or Google Business Profile is still a worthwhile placement because of how heavily location relevance is weighted for local businesses.

> "relevance is going to outweigh any website metrics"

**Evidence:** "'we want a minimum domain authority of 40 for these links' — and it's like, okay, that's not necessarily relevant, because location relevance is going to outweigh any website metrics."

**Apply at Pabau:** When evaluating potential partnership, guest-post, or association-membership links for Pabau, don't filter out an otherwise topically relevant placement purely for having a low DR/DA score — relevance to the target audience or industry can matter more than the metric, especially for signals that may feed AI-answer evaluation rather than classic link-authority ranking.

**Apply anywhere:** When evaluating potential partnership, guest-post, or association-membership links for your own site, don't filter out an otherwise topically relevant placement purely for having a low DR/DA score — relevance to the target audience or industry can matter more than the metric, especially for signals that may feed AI-answer evaluation rather than classic link-authority ranking.

### 5. Make the alternatives listicle a hub linking to each head-to-head page  `130.4`
*useful · concrete actions · source 130*

Grow and Convert ran competitor keywords in three shapes and connected them. Head-to-head pages targeted 'our client vs competitor' with long-form pieces built from interviews with the client's sales, product and competitive intelligence teams. Three-way pages targeted existing 'competitor vs competitor' queries and inserted the client as a third option. Alternatives pages targeted 'competitor alternatives' with list articles that feature the client at the beginning, and inside those lists they linked to the in-depth comparison piece written on each of the other competitors named. That last detail is the structural point: the alternatives listicle acts as a hub that feeds internal links to every head-to-head page, so the cluster reinforces itself instead of each page standing alone.

> "list articles that feature our client at the beginning"

**Evidence:** Grow and Convert: 11 comparison pages in the top 3 positions and 14 on page 1, with significant demo signups despite low search volume on the terms.

**How to do it**

1. Get the full competitor list from the sales team, not from a keyword tool.
2. Interview sales, product and competitive intelligence staff for each competitor's real weaknesses and your differentiators.
3. Write one head-to-head page per competitor from those interview notes.
4. Write one three-way page for each 'competitor vs competitor' query that already has volume, adding your brand as the third option.
5. Write one alternatives listicle per major competitor, with your product in the first slot.
6. Inside each alternatives listicle, link every other competitor named to its own head-to-head page.
7. Link each head-to-head page back to the relevant alternatives listicle.
8. Ignore search volume on these terms and judge them on demo requests instead.

**Tools:** Google Analytics

**Pitfall:** Writing alternatives listicles without the head-to-head pages behind them leaves the list with nothing to link to, and readers who want detail on one competitor leave to find it elsewhere.

**Apply at Pabau:** Pabau's competitor pages should be built as a cluster, not one-offs: an alternatives listicle per major competitor with Pabau first, each competing name in that list linking to its own Pabau-versus page. Source the differentiators from Pabau's sales team.

**Apply anywhere:** Build competitor content as a linked cluster. One head-to-head page per competitor sourced from sales interviews, three-way pages inserting you into existing versus queries, and alternatives listicles that put you first and link out to each head-to-head. Judge them on conversions, not volume.

### 6. Map the ring of industries one step outside your niche  `32.5`
*useful · concrete actions · source 32*

One straightforward niche-industry link-building method is deliberately mapping out every adjacent industry "one step outside" your exact niche and targeting those sites for placements and partnerships — for the petrochemical-manufacturing example, that ring includes engineering, general manufacturing, logistics, material science, sustainability, industrial tech, and B2B operations sites, chosen because they're close enough to the core niche that the link context still reads as believable rather than random.

> "sites one step outside the exact niche"

**How to do it**

1. Write down your exact niche or industry as the center point.
2. Brainstorm every industry, discipline, or business function that regularly intersects with or supplies your niche — suppliers, adjacent technical disciplines, logistics/operations functions, broader category terms.
3. For a manufacturing-type niche, this ring typically includes general engineering, broader manufacturing, logistics, materials science, sustainability, industrial technology, and B2B operations — adapt the equivalent ring for your own industry.
4. Build a target list of websites in each of these adjacent categories rather than restricting your list to sites that are exact-topic matches.
5. Before pitching each adjacent site, confirm the link context will still read as believable to that site's readers rather than forcing a connection that seems random.

**Pitfall:** Restricting your outreach list to only sites that are an exact topical match, in an industry too small to support that, produces a target list too short to run a real campaign on.

### 7. Mine competitors' backlink gaps for quick directory wins  `39.2`
*useful · concrete actions · source 39*

Pull a client's or your own backlink profile against the top three competitors' profiles and identify directories and sites that link to the competitors but not to you, since a site already willing to link to a direct competitor is a warm, logical prospect likely to link to you too. This is a fast, simple starting method, but the source explicitly warns that the list of gap opportunities runs out quickly, making it a good short-term win rather than a sustainable long-term link building strategy on its own.

> "pull your client's backlink profile against their top three competitors"

**How to do it**

1. Pull the backlink or referring-domains report for your site and for your top three direct competitors using a backlink tool such as Ahrefs, Semrush, or DataForSEO.
2. Identify referring domains that link to one or more competitors but do not currently link to your site, using a backlink gap or link-intersection analysis.
3. Filter that gap list specifically for directories and listing sites first, since these are typically the fastest and easiest to close.
4. Prioritize outreach or submission to those directories/sites, using the fact that they already link to a direct competitor as the reason they are a logical fit for you too.
5. Treat this as a starting-point tactic to exhaust early in a link building campaign, not a recurring monthly strategy, since the pool of gap opportunities depletes quickly.
6. Once the initial gap list is exhausted, shift effort to other methods, such as adjacent niche outreach or partner features, for ongoing link acquisition. (inferred)

**Tools:** Ahrefs, Semrush, DataForSEO

**Pitfall:** Relying on this as a long-term link building strategy — the list of gap opportunities is explicitly said to run out fast, making it a starting point only, not a sustainable ongoing tactic.

### 8. Negative SEO is real but deliberately unpredictable, can backfire via canonicals  `38.12`
*useful · content insights · source 38*

Kalin recounts his only negative-SEO attempt, around 2014: a client asked him to tank a competitor in the small, competitive visa-services niche by dumping 300 spam links with identical exact-match anchor text onto the competitor's ranking page, intending to trigger a Penguin penalty. Instead, the competitor's site had two near-duplicate pages, and mid-attack Google's canonical selection switched to the OTHER duplicate page, which inherited all 300 links' anchor-text value and rocketed to the number-one position, outranking every result including the relevant government embassy site. He frames this as proof that Google deliberately keeps negative-SEO outcomes ambiguous — combining real algorithmic randomness with loss-aversion-exploiting propaganda ('it doesn't work') — so that neither attackers nor a business tempted to weaponize it against itself can rely on a predictable result.

> "It shot to number one and outranked everything, even the embassy"

**Evidence:** First-hand account: a 300-link exact-match-anchor attack on a visa-niche competitor's ranking page backfired when Google's canonical tag switched to the competitor's duplicate page mid-attack, passing along all the link/anchor value and pushing that page to outrank even the government embassy result.

**Apply at Pabau:** Don't assume a sudden spike of spammy exact-match-anchor links pointing at Pabau (or a competitor) will behave predictably in either direction — monitor Pabau's own anchor-text distribution in Ahrefs for unnatural spikes as a precaution, but don't attempt to replicate this tactic against competitors given how unpredictably it can backfire.

**Apply anywhere:** Don't assume a sudden spike of spammy exact-match-anchor links pointing on your team (or a competitor) will behave predictably in either direction — monitor your own anchor-text distribution in Ahrefs for unnatural spikes as a precaution, but don't attempt to replicate this tactic against competitors given how unpredictably it can backfire.

### 9. One linkable web tool can earn hundreds of thousands of backlinks  `39.8`
*useful · content insights · source 39*

The concept of a linkable asset, a genuinely useful free tool or resource built specifically to attract links on its own merit rather than through outreach, is referenced via a specific outlier example: one simple website or web app is credited with earning 384,000 backlinks purely from functioning as a linkable asset. This dwarfs what any of the outreach-based methods described elsewhere in the same source, such as adjacent niche swaps, competitor gap analysis, guest posts, partner features, or agency swaps, could plausibly produce individually, positioning linkable-asset creation as a fundamentally different order-of-magnitude link building category.

> "a ChatGPT prompt that you can use to come up with"

**Evidence:** A specific referenced case, pointed to via a separate podcast episode not included in this transcript, of one simple website/web app accumulating 384,000 backlinks credited to its function as a linkable asset.

**Apply at Pabau:** Pabau should consider investing in at least one genuinely free, standalone interactive tool, such as a no-show cost calculator, a clinic ROI calculator, or a scheduling-efficiency tool, built specifically as a linkable asset, since this category is shown capable of an outlier backlink count far beyond what relationship-based outreach methods could achieve, and treat it as a distinct, higher-ceiling project separate from routine outreach link building.

**Apply anywhere:** Consider investing in at least one genuinely free, standalone interactive tool — a cost calculator, an ROI calculator, or an efficiency estimator built around a number your buyers already worry about — designed specifically as a linkable asset, since this category is shown capable of an outlier backlink count far beyond what relationship-based outreach could achieve; treat it as a distinct, higher-ceiling project separate from routine outreach link building.

### 10. PageRank is never depleted by linking out, only diluted  `38.1`
*useful · general insights · source 38*

Kalin argues the single biggest SEO mistake is running only one or a few websites, because outbound linking is non-zero-sum: a site with PageRank five can link to a thousand other websites and still retain PageRank five, since those recipient sites just get a very small share of it. The only genuinely bad scenario is having zero outgoing links, because generating outbound links (and now AI citations) is how a site creates transferable value for others without losing any of its own authority. This reframes external linking from a risk to manage into a resource that can be spent freely, exchanged, sold, or rented out over time.

> "PageRank can never be lost"

**Evidence:** Direct claim: 'PageRank can never be lost — it's just not how the algorithm works... You can link to a thousand websites, and you still have PageRank five.'

**Apply at Pabau:** Pabau's content team should stop treating outbound links to authoritative external sources (research, competitors, industry press) as leaking equity — link out generously where it serves the reader, since it does not measurably cost Pabau's own authority and can support digital PR relationship-building.

**Apply anywhere:** Your content team should stop treating outbound links to authoritative external sources (research, competitors, industry press) as leaking equity — link out generously where it serves the reader, since it does not measurably cost your own authority and can support digital PR relationship-building.

### 11. Pick profile sites from a trusted-sources list, not domain authority  `73.24`
*useful · concrete actions · source 73*

Barnard makes a specific point about how to choose which platforms to build profiles on: it is nothing to do with domain authority. Kalicube publishes a trusted sources list, meaning the sources Google's knowledge graph actually uses primarily, or historically trusted, for filling itself up. Getting a profile on one of those helps; a high-DA site that the graph does not draw on does not do the same job. His advice is to start with the obvious ones he already named and then work through the authoritative domains list. Within that, he singles out Muck Rack as very powerful for people who write articles, and TheOrg.com and Crunchbase as working for both people and corporations. This reframes profile-building away from generic citation blasting toward a short, targeted list of sources the graph reads.

> "It's which sources does Google's knowledge graph use primarily"

**Evidence:** Barnard names Muck Rack as very powerful for people who write articles, and TheOrg.com and Crunchbase as working for both people and corporations.

**How to do it**

1. Start with the core set: TheOrg.com, Crunchbase, LinkedIn, Facebook, Twitter/X and one review platform.
2. Add Muck Rack if the entity is a person who publishes articles.
3. Open a trusted-sources list of domains the knowledge graph draws on and work down it rather than sorting prospects by domain authority.
4. For each candidate, check whether the platform lets you state the same fundamental facts and link back to the entity home.
5. Skip any platform whose profile format forces a description that contradicts your canonical facts.
6. Fill each new profile from the modular description master, not from scratch.
7. Add the finished profile to the entity home's outbound link list and to the maintenance spreadsheet.

**Tools:** Kalicube Pro, Muck Rack, TheOrg.com, Crunchbase, LinkedIn

**Pitfall:** Choosing directories by domain authority. Barnard says explicitly that the relevant criterion is whether the knowledge graph draws on the source, which is a different and much shorter list.

**Apply at Pabau:** Rather than buying broad directory citation packages, restrict Pabau's profile work to the handful of sources the knowledge graph actually reads, plus the healthcare software review platforms buyers use.

**Apply anywhere:** Choose profile platforms by whether Google's knowledge graph draws on them, not by domain authority. Start with the core set, add a trusted-sources list, and fill every profile from one master description.

### 12. Point new backlinks at the ranking page, not the homepage  `180.9`
*useful · concrete actions · source 180*

In its agency profiles Grow and Convert singles out ABHMedia's approach: they target backlinks at the pages for the specific keywords the client is trying to rank for, rather than building general backlinks to the homepage. Grow and Convert's own process matches the timing half of this, since they build links only once a piece starts ranking for a keyword, to push it onto page 1 or the top of page 1. Together that gives a rule with two parts. Choose the page by which keyword you are trying to move, and choose the moment by whether the page already has a ranking to improve. General homepage links are the default agency deliverable and they move individual target pages least.

> "rather than general backlinks to your homepage"

**Evidence:** Grow and Convert describe ABHMedia targeting backlinks to pages for specific keywords rather than general homepage links, and describe their own link building as triggered once a piece starts ranking.

**How to do it**

1. List the pages you actually want to move, with the target keyword and current position for each.
2. Filter to pages already ranking somewhere for that keyword, since those respond to links.
3. Write the link target list at page level, never at domain level.
4. Set anchor text around the target keyword and close variants, and cap any single anchor at three uses.
5. Brief outreach on the page's specific value to the linking site's readers, since a deep page needs a reason to be cited.
6. Track position change on the target keyword for eight weeks per page, not sitewide domain metrics.
7. Retire a target page from the campaign once it holds top-of-page-1 and move the budget to the next one.

**Tools:** Ahrefs

**Pitfall:** Buying homepage links as a package because they are easier to place. Domain metrics rise, the pages you actually need to move do not, and there is nothing to point at in a report.

**Apply at Pabau:** Any link work for Pabau should name the article and the keyword before it names a budget. Links to pabau.com's homepage do little for a specific template page trying to reach page 1.

**Apply anywhere:** Aim backlinks at the specific page and keyword you want to move, and only once that page already ranks somewhere. General homepage links raise domain metrics without shifting the pages that matter.

### 13. Qualify guest post targets on real audiences, not just relevance  `108.21`
*useful · best practices · source 108*

Grow and Convert rate guest posting as the most reliable and scalable route to quality backlinks for SaaS, and their reason is control: you decide the context the link sits in and which specific page it points to, which matters when you are pushing one article toward page one for one keyword. Their qualification bar has two parts. The site must be relevant to your industry or an adjacent one, and it must have a real audience rather than existing solely for link building. Links from genuine readerships carry more weight with search engines and also send referral traffic directly, which gives you a second, faster signal on whether the placement was worth it. That referral test is the practical way to tell the two kinds of site apart after the fact.

> "targeting sites that are relevant to your industry and have real audiences"

**Evidence:** Grow and Convert's criteria: industry relevance plus a genuine readership, with referral traffic as the accompanying benefit of a real audience.

**How to do it**

1. Build a prospect list from sites in your industry and one adjacent industry.
2. Discard any site whose content is a mix of unrelated verticals, the standard signature of a link farm.
3. Check each site for signs of a real audience: a newsletter, comments, social distribution, recurring named authors.
4. Check whether the site's own pages rank and pass traffic, rather than trusting a domain rating.
5. Pitch a topic that overlaps the page you want to link to, so the anchor sits in relevant context.
6. Point the link at the specific article you are pushing, not the homepage.
7. Measure referral sessions from each placement over the following 90 days.
8. Drop any publisher that sends no referral traffic from the next round, regardless of its authority score.

**Tools:** Ahrefs

**Pitfall:** Buying placements on sites that exist only to sell links. They look relevant and score well on third-party authority metrics, but they send no referral traffic, which is the signal that the audience is not real.

**Apply at Pabau:** Pabau's guest posting should target aesthetics, dermatology and practice-management publications with genuine practitioner readerships, and each placement should link to the specific article being pushed. Drop any outlet that sends no referrals in 90 days.

**Apply anywhere:** Qualify guest post targets on relevance plus a real readership. Point each link at the specific page you are pushing, then measure referral traffic over 90 days and drop publishers that send none.

### 14. Real, multi-channel marketing signals are the best kind of backlink  `30.11`
*useful · content insights · source 30*

Garrett recounts a former Google search-quality analyst (who worked alongside Matt Cutts) telling him 'we see everything, we know everything,' and argues this is why sponsorship-style links work: Google is looking for links that come with real referral traffic and branded-search lift, which sponsorships generate because they involve a genuine multi-channel presence — a logo at a real community organization, a newsletter mention, a social media post, unlinked brand mentions — rather than a link that exists purely for its own sake.

> "Real marketing is the best type of backlink"

**Evidence:** "the types of links Google wants to see are links that drive referral traffic, branded searches... he said, 'Yeah, we see everything, we know everything.'... all of that is real marketing. Real marketing is the best type of backlink."

**Apply at Pabau:** When Pabau evaluates any link opportunity (guest post, directory, sponsorship, partnership), prioritize ones that plausibly generate real secondary signals — referral clicks, branded search lift, social mentions — over placements that exist purely as a hyperlink, since Google's own former search-quality staff describe the ability to detect the difference.

**Apply anywhere:** When you evaluate any link opportunity (guest post, directory, sponsorship, partnership), prioritize ones that plausibly generate real secondary signals — referral clicks, branded search lift, social mentions — over placements that exist purely as a hyperlink, since Google's own former search-quality staff describe the ability to detect the difference.

### 15. Reject any expired domain that changed niche into a YMYL vertical  `67.12`
*useful · best practices · source 67*

Dirk names two absolute deal breakers when evaluating a drop-caught domain. The first is ownership churn: seeing the number of owners change every year is enough on its own. The second, which he calls the bigger one, is a niche change into any YMYL vertical. If he wants a domain for casinos and its history shows crypto or health, that is a no. He treats a car site that shows a 2021 gambling or adult front page the same way. His third is a heavily abused backlink profile, which he refuses to buy because cleaning it takes too long to be worth the investment. He also argues in the same interview that iGaming itself is a YMYL industry alongside finance and health, so no vertical in that group gets treated leniently.

> "if it's changing niches that's another big no-no for me"

**Evidence:** Dirk gives the concrete signature: a vehicle site with a 2021 front page for gaming or adult content, and rejects it outright.

**How to do it**

1. Define the single niche the domain will be used for before you look at its history.
2. Step through the Wayback front pages year by year and record the niche shown in each year.
3. Reject outright if any year shows gambling, adult, crypto or health when that is not your intended niche.
4. Count the ownership changes and reject anything changing hands every six to twelve months.
5. Pull the backlink profile and judge whether it looks bought in bulk or earned editorially.
6. Skip a heavily abused profile rather than budgeting to clean it, since Dirk says cleaning never pays back.
7. Record the reject reason against each domain so the criteria stay consistent across buyers.

**Tools:** Wayback Machine

**Pitfall:** Assuming a bad history can be scrubbed. Dirk says a savagely abused backlink profile takes so long to clean that the investment never pays back, so the correct move is to skip the domain.

**Apply at Pabau:** Healthcare and aesthetics are YMYL, so any domain Pabau considers acquiring gets rejected if its history shows a jump between unrelated regulated verticals, regardless of how strong the links look.

**Apply anywhere:** Reject any expired domain whose history jumps between unrelated regulated verticals such as health, finance or gambling, and skip any domain with a heavily abused link profile rather than trying to clean it.

### 16. Reverse-engineer a rival's digital PR via Ahrefs anchors  `33.11`
*useful · concrete actions · source 33*

To reverse-engineer a competitor's digital PR campaign, the guest pulls their most recent referring domains in Ahrefs, notes the exact anchor text used, then Googles that exact phrase in quotation marks to surface every other page carrying it. In one example (a Dubai real-estate company's sales-percentage data campaign), this revealed the full list of publications and journalists the campaign was placed with, because the agency running it never varied its anchor text — directly illustrating why anchor-text diversification (see the brand-anchor-text practice above) also protects a campaign from being easily traced and copied by competitors.

> "Google that exact same anchor text in quotation marks"

**How to do it**

1. Enter the competitor's domain into Ahrefs and pull their most recent referring domains report.
2. Note the exact anchor text used on their newest or most relevant backlinks.
3. Search that exact anchor text phrase on Google wrapped in quotation marks.
4. Review the results to find every other publication carrying the identical phrase, revealing the campaign's full placement list.
5. Compile the resulting publications/journalists as a starting target list for your own version of a similar campaign in that niche.
6. Repeat on any competitor whose link pattern you want to study.

**Tools:** Ahrefs, Google Search

**Pitfall:** This method only works cleanly when the competitor reused identical anchor text across placements, as in the source's example — a competitor that varies anchor text per campaign is much harder to trace this way.

### 17. Rotate link building across a different set of published articles each month  `121.12`
*useful · concrete actions · source 121*

Grow and Convert treat link building as a recurring rotation rather than a campaign pointed at one page. Each month they build links to different articles they have published, as an ongoing effort, and they report that links to individual articles often give a measurable ranking boost and help push content onto the first page. The rotation is combined with their selection rule: they prioritize the articles that have already proven they convert, which they learn by running paid promotion to the piece before it ranks. So the monthly list is not the newest posts, it is the posts with demonstrated business value that are still short of page one. They are explicit that this is a supporting element. If dedicated pages and intent match are wrong, no amount of outreach fixes it.

> "we build links to different articles we've published as an ongoing effort"

**Evidence:** Grow and Convert report building links to individual articles gives a ranking boost, and they choose targets from articles that generated conversions under paid promotion.

**How to do it**

1. List every published bottom-funnel article with its target keyword and current position.
2. Run paid promotion to each new article while it waits to rank, and record conversions per article.
3. Filter to articles that converted under paid traffic and sit outside the top ten organically.
4. Rank that filtered list by keyword value, not by publication date.
5. Each month, pick the top two or three from the list as that month's link targets.
6. Run guest posting for those specific pages, since guest posts let you choose the destination URL.
7. Re-check positions six to eight weeks later and drop any page that has reached the top three.
8. Refresh the list monthly as new articles finish their paid promotion test.

**Tools:** Ahrefs

**Pitfall:** Pointing every month's links at the homepage or the newest post. The pages that are one or two positions from page one, and already proven to convert, never get the push that would pay for the work.

**Apply at Pabau:** David should keep a rolling list of Pabau articles that convert but rank outside the top ten, and point each month's outreach at two or three of them rather than at pabau.com generally.

**Apply anywhere:** Rotate each month's link building across a different set of already-published pages, chosen because they convert and sit just outside page one.

### 18. Run promotion as three funded channels, not social sharing  `169.12`
*useful · concrete actions · source 169*

Hyam's second gap in the agency market was promotion: none of the ten agencies he called had a strategy beyond drafting social updates for the client's own accounts. His replacement is a named three-step process, community content promotion, paid Facebook promotion, and targeted link building for SEO. Two details make it more than a list. The paid Facebook spend comes out of the agency's budget, not an extra client line item, which forces the agency to only promote pieces it believes will convert. And promotion was the original engine, done solely through community content promotion before paid and links were added, which is why the agency could raise price when the other two were bundled in. He is blunt that a single employee or agency doing all three plus advanced writing is virtually impossible to find.

> "We have a 3 step promotion process"

**Evidence:** Community content promotion alone carried Grow and Convert's early client work; paid Facebook and targeted link building were added later and helped justify moving from $6,000 to $10,000 a month.

**How to do it**

1. Stop counting social posts on your own accounts as promotion.
2. Build a list of the communities where your buyers actually discuss the topic and earn standing in them before posting anything.
3. Distribute each new piece into those communities as the first promotion step.
4. Set a fixed paid budget per piece and run it as Facebook promotion to the target audience.
5. Fund the paid spend from your own budget so you only promote pieces worth promoting.
6. Run targeted link building at each published piece rather than at the homepage.
7. Assign one owner for all three steps so promotion is not the writer's afterthought.
8. Report traffic per piece by promotion channel so you can cut the step that is not working.

**Tools:** Facebook Ads

**Pitfall:** Treating community promotion as posting links. It only works if the account has standing in the community, which is why Hyam notes it was the one thing only he knew how to do at launch.

**Apply at Pabau:** Pabau's blog and template pages need an owned distribution step beyond social. Pick the aesthetics and practice-owner communities where clinic owners talk, plus a small paid budget per flagship article, and run link outreach at the article rather than the homepage.

**Apply anywhere:** Promotion means three funded channels: community distribution where your buyers already talk, a paid budget per piece, and link building aimed at the article itself. Sharing on your own social accounts is not promotion.

### 19. Seed stock photos on high-DR sites for free backlinks  `24.6`
*useful · concrete actions · source 24*

A three-step tactic shared on the thread: create original niche-relevant images (product shots, location photos, data visualizations, infographics, charts) using your phone camera, Canva, or Photoshop, then upload them to free stock-image platforms — Unsplash, Pexels, Pixabay, Flickr, Creative Commons — filling in the attribution/credit field with a link back to your site. These platforms reportedly carry a domain rating of 90+ and are pulled from daily by bloggers, journalists, and designers, so every future use-with-credit becomes a free, zero-outreach natural backlink, effectively seeding link opportunities at scale with no ongoing pitching required.

> "These stock platforms are domain rating 90 plus"

**How to do it**

1. Take original photos with your phone, or create graphics in Canva or Photoshop — product shots, niche-specific images, location photos, data visualizations, infographics, or charts relevant to your topic.
2. Upload these images to free stock photo sites: Unsplash, Pexels, Pixabay, Flickr, and Creative Commons-licensed repositories.
3. Fill in each platform's attribution/credit field with a link back to your site.
4. Repeat regularly to build a growing library of seeded images across platforms.
5. Prioritize niche-specific and data-visualization-style images over generic stock photography, since these are more likely to be reused by people writing specifically about your topic. (inferred)

**Tools:** Canva, Photoshop, Unsplash, Pexels, Pixabay, Flickr

### 20. Separate PBN hosting footprints before buying the first domain  `67.19`
*useful · concrete actions · source 67*

Dirk describes how drop-caught exact-match domains actually get used: they are assembled into private blog networks, and the whole exercise depends on the footprints between them being unrecognizable. His point is about sequencing. The infrastructure has to be planned before you start buying, including where each site is hosted, because if he can spot the pattern just by looking at the sites and their histories, Google will spot it far more easily. He is blunt that Google has infinite resources and is smarter at this than you are, so the only viable posture is to make it as difficult as possible. His practice on the domains worth keeping is to regenerate the old content that was already indexing on those pages rather than writing something new.

> "you have to have a really well infrastructure in place before you start planning to buy"

**Evidence:** Dirk says some restored PBN domains reindexed so well with a little care on content and new backlinks that they catapulted back up and were promoted into money-site tiers.

**How to do it**

1. Plan the hosting and network layout before buying any domain, not after the batch arrives.
2. Spread hosting across genuinely unrelated providers and IP ranges rather than one host with different accounts.
3. Vary registrar, DNS, CMS, theme and contact details across the network so no two sites share a signature.
4. Restore the old content that was already indexing on each domain rather than publishing fresh generic articles.
5. Rebuild the internal linking of each restored site independently instead of using one template.
6. Audit your own network by inspecting the sites as an outsider would and asking whether you could spot the pattern from the public data alone.
7. Escalate only the domains that reindex well into a money-adjacent tier with real top-list content and new links.
8. Assume detection is a matter of time and never point the network at a page you cannot afford to lose.

**Pitfall:** Buying first and planning hosting afterwards. Dirk says if he can identify the network from the sites and their histories alone, Google finds it far faster, and the exposure of one node exposes the rest.

**Apply at Pabau:** This is documented as intelligence, not a Pabau tactic. Pabau should not build or buy links from a private network, and should treat any agency proposing one as proposing a risk to the main domain.

**Apply anywhere:** This is documented as intelligence rather than a recommendation. If you are evaluating an agency, treat a private blog network proposal as a risk to your main domain, since exposure of one node exposes the whole network.
