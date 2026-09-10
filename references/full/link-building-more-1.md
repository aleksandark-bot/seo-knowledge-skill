# Link Building — supporting (part 1 of 3)

20 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. 18 years of SEO ranking factors: content+links, then brand, then UX  `38.8`
*useful · general insights · source 38*

Kalin traces the ranking-factor stack he's observed over 18 years in SEO: it started as content and backlinks, then added brand (trust signals from brand-search volume), then added user-experience/engagement signals like dwell time and not pogo-sticking back to the SERP — with the 'nav boost' user-signal layer only activating once a page already ranks around the top 30, because applying it more broadly would be too computationally expensive. He argues backlinks' relative importance has dipped only slightly over the last five years, not because they matter less intrinsically, but because they now also feed the newer factors: good backlinks drive brand discovery/brand search, and good contextual backlinks send qualified referral traffic that generates strong on-site engagement signals. His core argument for why backlinks remain foundational: top-tier editorial links (BBC, Guardian, NYT, or a homepage link from a government/NGO site) are the one signal on the internet that cannot be cheaply faked with bots, unlike AI-era brand citations.

> "Then it became content, backlinks, brand, and user experience"

**Evidence:** Direct account: 'when I started 18 years ago, it was content and backlinks. Then it became content, backlinks, and brand... Then it became content, backlinks, brand, and user experience.'

**Apply at Pabau:** Continue investing in earned, editorial-grade backlinks (digital PR) even while optimizing for brand and UX signals, since Pabau's argument for links should be that they compound into the other ranking layers (brand search, qualified engagement) rather than being a separate, declining lever.

**Apply anywhere:** Continue investing in earned, editorial-grade backlinks (digital PR) even while optimizing for brand and UX signals, since your argument for links should be that they compound into the other ranking layers (brand search, qualified engagement) rather than being a separate, declining lever.

### 2. 43 nonprofit sponsorships produced 86 newly-ranking keywords  `30.4`
*useful · content insights · source 30*

In a tracked case study, plumbing company Dial One sponsored 43 local nonprofits across its service areas; ZipSprout measured keyword movement afterward and found the target service pages reached the top 10 for their goal terms, 86 new keywords started ranking that hadn't been before, and the average position across tracked keywords improved by about 9 spots. This is offered as one of the few instances where the ranking impact of relevance-based sponsorship links was actually quantified rather than left as an anecdote.

> "86 new keywords end up ranking, and a plus-9 average position increase"

**Evidence:** "They sponsored 43 local nonprofits in the areas where their businesses were located, and we tracked keyword data, movement, and placement. They reached top 10 for the service pages we were building links for. They had 86 new keywords end up ranking, and a plus-9 average position increase."

**Apply at Pabau:** This gives David a concrete benchmark to cite when building an internal case for relevance-based sponsorship or partnership link building (e.g., aesthetics/med-spa trade associations, industry conferences): a moderate-scale campaign (43 placements) produced a measurable ranking lift, useful for setting realistic expectations on required volume and payoff timeline.

**Apply anywhere:** This gives you a concrete benchmark to cite when building an internal case for relevance-based sponsorship or partnership link building (your sector's trade associations, industry conferences): a moderate-scale campaign of 43 placements produced a measurable ranking lift, useful for setting realistic expectations on required volume and payoff timeline.

### 3. A defined entity's unlinked mention functions like a backlink  `26.11`
*useful · content insights · source 26*

Dooley confirms a claim put to him as a 'rumor' — that once a brand is a well-defined, known entity, an unlinked mention (brand name cited with no hyperlink, e.g., in a news article) carries value 'almost equal to a backlink,' and he says it's even stronger when the mention is phrased as a semantic triple (naming the entity as subject alongside a fact). He gives the example of a brand being named in the BBC or Telegraph with no link, noting there's a measurable 'lift' to the brand a week later even without any link at all.

> "an unlinked mention is almost equal to a backlink"

**Evidence:** "if your entity is defined, so you're a known entity, an unlinked mention is almost equal to a backlink" — confirmed by Dooley with "Yeah, it is," adding it's stronger still "if it's defined within a semantic triple."

**Apply at Pabau:** Pabau shouldn't only chase do-follow links from PR outreach — earning unlinked brand namechecks in trusted press (trade publications, healthcare/med-spa industry sites) is worth pursuing on its own once Pabau's entity is well-established, especially if the coverage states the brand name alongside a clear fact rather than a vague reference.

**Apply anywhere:** You shouldn't only chase do-follow links from PR outreach — earning unlinked brand namechecks in trusted press (trade publications, healthcare/med-spa industry sites) is worth pursuing on its own once your entity is well-established, especially if the coverage states the brand name alongside a clear fact rather than a vague reference.

### 4. A real Penguin-era wipeout is why anchor-text ratios still matter  `08.17`
*useful · general insights · source 08*

Before Google's 2012 Penguin update, aggressive exact-match anchor text linking won a #3 national Google ranking for 'movers,' generating over $25,000/month from that single keyword for about four months — until Penguin hit and wiped out the entire linked network overnight, forcing a full rebuild and migration to new domains. This first-hand account is the lived origin of the anchor-text-ratio discipline the same operator still practices today (pairing every anchor-text link with a brand-mention link and a bare-URL link in the same batch). It's presented as a caution that algorithmically-punished tactics can produce real short-term wins before a correction erases them entirely, not just a theoretical risk.

> "an entire network gone overnight, and you had to rebuild"

**Evidence:** First-person account: an exact-match anchor-text link network held the #3 U.S. ranking for 'movers,' worth over $25,000/month, for about four months before 'Penguin came along and wiped our entire network out — wiped out everything,' requiring migration of all affected properties to new domains.

**Apply at Pabau:** David should treat 'avoid over-optimized exact-match anchor text ratios' as a rule grounded in a real, catastrophic historical penalty event rather than pure theory, and apply the same scrutiny when reviewing any backlink or digital PR vendor's anchor-text practices being proposed for Pabau.

**Apply anywhere:** You should treat 'avoid over-optimized exact-match anchor text ratios' as a rule grounded in a real, catastrophic historical penalty event rather than pure theory, and apply the same scrutiny when reviewing any backlink or digital PR vendor's anchor-text practices being proposed for your own site.

### 5. Automate link-building vetting and outreach with an Ahrefs-connected AI agent  `08.8`
*useful · ai workflows · source 08*

An AI agent (the source uses Manus, comparable to Claude or Codex operating agentically) is connected to an Ahrefs MCP integration so it can independently examine candidate linking domains — pulling real organic traffic and keyword-ranking data rather than relying on surface metrics. Given that data access, the agent is tasked with building the entire link-acquisition plan itself: selecting domains, drafting the guest-post articles, handling submission to guest-post marketplaces, and then checking back on each site afterward to confirm the link actually went live and that it carries the correct dofollow attribute. This automates what would otherwise be a fully manual vetting-and-outreach workflow, while still relying on real backlink-data verification rather than trusting the marketplace's own listings.

> "examines all the domains and makes the whole plan"

**How to do it**

1. Set up an AI agent with agentic/tool-use capability (the source uses Manus; equivalents include Claude with computer-use/agent tooling, or Codex) and connect it to an Ahrefs MCP connector or API.
2. Supply the agent with your target pages that need links (e.g., specific directory listing URLs).
3. Point the agent at candidate linking domains from a guest-post marketplace (e.g., iCopify, PressWhizz) or an outreach list.
4. Instruct the agent to pull each candidate domain's organic keyword count and traffic via the Ahrefs connection before considering it viable.
5. Have the agent build a complete link-placement plan: which domains to use and what anchor text to apply.
6. Have the agent draft the actual guest-post articles required for submission.
7. Have the agent handle the submission process to each site or marketplace.
8. Have the agent check back on each published placement to confirm the link is live and verify whether it correctly carries a dofollow attribute.
9. Review the agent's domain-vetting output yourself before high-value placements go live, especially for larger link spends. (inferred human sign-off step, consistent with the source's general practice of reviewing AI output elsewhere in the interview)

**Tools:** Manus, Ahrefs, MCP, iCopify, PressWhizz

**Pitfall:** Trusting a guest-post marketplace like iCopify at face value — it 'has a lot of trash sites on it that'll ruin your link profile,' so every candidate domain must be independently checked for real organic traffic and keyword rankings before use.

### 6. Build a shared community asset and get the whole local group to link to it  `74.11`
*useful · concrete actions · source 74*

David Quaid describes how he built authority for Primary Position in the early 2000s. He went to Limerick Open Coffee, ran BarCamp in 2008, shared ideas on Twitter, blogged about them, and wrote about people who did not even have websites and the ideas they were working on. The group built BarCamp as a website, and all 26 bloggers in that community linked to it. He says it then ranked for everything, including queries like how to start a company. His point is that this third place on the internet has been lost, partly because comment spam killed blog comments and partly because forums like Reddit do not welcome self-posting even while advising people to post in forums. He also acknowledges people get fatigued by promotion. The tactic still works where a real geographic or vertical community exists.

> "All of the bloggers that were in the community, there were 26 of us"

**Evidence:** David's BarCamp site in 2008 with 26 community bloggers linking to it, which he says ranked for broad queries such as how to start a company.

**How to do it**

1. Identify a real community you can join, either geographic or a tight vertical, and attend or participate in it consistently before asking for anything.
2. Blog about the people and ideas in that community, including those with no website of their own.
3. Propose one shared asset the group needs: an event site, a directory, a public resource.
4. Build and host that asset on its own domain so it is neutral and everyone is comfortable linking.
5. Ask every participant to link to it from their own site, since each of them has a reason to.
6. Publish the outputs of the community, such as talks and notes, on the shared asset so it keeps earning links.
7. Point your own money pages to the shared asset with a contextual link so its authority flows into your site.

**Pitfall:** Building the shared asset before the relationships exist. Without a real community behind it, nobody links and you own a dead microsite.

**Apply at Pabau:** Pabau could sponsor or build the shared resource for aesthetic practice owners, such as a public compliance calendar or an event site, hosted separately and linked by every participating clinic and vendor. That is a different bucket from the blog and should be resourced separately.

**Apply anywhere:** Join a real community, build the one shared public asset the group needs, and let every participant link to it from their own site.

### 7. Build the citation outreach list from the domains cited for your own prompts  `81.15`
*useful · concrete actions · source 81*

Grow and Convert's fourth step is securing brand mentions on sites that already appear as citations for the AI prompts they want to win. Their rule is explicit: brands should not build citations from just any website in their industry, only from sites LLMs actually cite. The mechanism is the same grounding process. When the model searches for solutions matching a query, appearing across multiple cited sources, including your own site, raises overall visibility. Worth noting they had not yet started this for Constitution Lending, and the case study's results came from owned content alone, which is why they treat the missing third-party mentions as the explanation for weaker ChatGPT performance.

> "only from sites that LLMs actually cite"

**Evidence:** Grow and Convert attribute Constitution Lending's weaker ChatGPT visibility to having no third-party brand mentions yet, since all results so far came from owned content.

**How to do it**

1. Run each of your tracked prompts through ChatGPT, Perplexity and Google AI Overviews and record every cited domain.
2. Build a frequency table of domains across the whole prompt set and sort by citation count.
3. Drop your own domain and the ones you cannot realistically get onto, such as regulators and news wires.
4. For each remaining domain, find the specific cited URL and check whether it is a listicle you could be added to.
5. Pitch inclusion in that exact URL, offering the differentiator sentence and a concrete reason you belong on the list.
6. Where a link is refused, still take the unlinked brand mention, since mentions feed the model.
7. Re-run the prompt set six to eight weeks after a placement and check whether that domain now names you.
8. Repeat the citation scrape quarterly, because the cited set shifts as rankings change.

**Tools:** ChatGPT, Perplexity

**Pitfall:** Running generic industry link building instead. A link from a relevant site that never appears in the citation list does nothing for the prompts you are trying to win.

**Apply at Pabau:** Pabau should scrape the domains cited for aesthetics and practice-software prompts, then pitch inclusion in those specific roundups rather than pursuing general healthcare link building.

**Apply anywhere:** Scrape every domain cited in AI answers for your target prompts, rank them by frequency, and pitch inclusion only in those specific pages. A link from a relevant site that never gets cited will not move your AI visibility.

### 8. Buy fewer, better expired domains rather than catching in bulk  `67.17`
*useful · best practices · source 67*

Asked for his prediction on the future of exact-match domains and drop catching, Dirk says the discipline remains beneficial but the market is being cleaned up and the good ones will be harder to find. His resulting rule is strict: quality over quantity. He would rather take a smaller number of domains that genuinely meet every parameter than catch a thousand. His filter is deliberately paranoid, that anything looking even semi-questionable should be eliminated rather than investigated further, because the cost of a bad domain in a network is higher than the cost of missing a good one. He closes by restating the gate that makes the whole thing conditional: without your own pages and proper structured data, you will not be cited by AI anyway.

> "It's all about going for quality rather than quantity"

**Evidence:** Dirk's stated preference is a bit less domains that are really on par with the parameters wanted, over a thousand caught in bulk.

**How to do it**

1. Write the parameters a domain must meet before you look at any inventory: ownership count, niche continuity, live backlinks, indexation age.
2. Set a hard rule that anything failing one parameter is eliminated rather than investigated further.
3. Cap the number of domains you buy per month at what you can personally review end to end.
4. Run every candidate's backlink check through at least two providers before committing.
5. Reject anything that looks even semi-questionable, since a bad domain in a network costs more than a missed good one.
6. Before restoring any of them, confirm you can put real content and correct structured data on the pages.
7. Review the batch three months later and record which parameters actually predicted performance.

**Pitfall:** Volume buying under a loose filter. Dirk's own team wrote off close to a thousand domains bought this way, and the residual risk is that keeping the bad ones and linking them at money sites damages the money site.

**Apply at Pabau:** The same discipline applies to Pabau's content: a smaller number of pages that fully meet the standard beats volume, and anything that looks marginal should be cut rather than published and monitored.

**Apply anywhere:** Buy fewer expired domains that fully meet your criteria rather than catching in bulk, and eliminate anything that looks even slightly questionable instead of investigating it further.

### 9. Cap exact-match anchor text even on high-performing image links  `14.6`
*useful · best practices · source 14*

Despite the strong evidence for exact-match anchor text (and exact-keyword image alt text) performing well, the explicit standing caution is not to overuse exact-match anchor text at all — a rule that applies generally to all link building, not only to the image-based tactics just described. This is a moderation/ratio rule rather than a rejection of the tactic itself: exact-match remains effective in the right proportion, but overreliance on it across an entire link profile is flagged as a risk.

> "don't overdo it with exact match anchor text links"

**How to do it**

1. When building backlinks via images (stock photo attribution, infographic pickups, guest content, etc.), vary the alt text and surrounding anchor text across placements rather than using the exact target keyword every time.
2. Mix in brand-name and naked-URL style attributions alongside exact-match keyword alt text within your overall link profile.
3. Periodically audit your total backlink profile's anchor text distribution (e.g., via Ahrefs or Semrush) to check that exact-match keyword anchors, including image alt text, don't dominate disproportionately.
4. Apply this same moderation rule to all link building generally, not just image-based tactics, treating it as a standing portfolio-level constraint rather than a per-link decision. (inferred general application)

**Tools:** Ahrefs, Semrush

**Pitfall:** Overusing exact-match anchor text across a link profile — explicitly flagged as a risk to avoid 'not just from images, but in general,' even though exact-match remains one of the best-performing individual link/alt-text types.

### 10. Chain PhantomBuster, Apollo, MillionVerifier and Instantly for cold outreach  `68.14`
*useful · ai workflows · source 68*

Cody published this stack publicly and it is worth recording as a procedure. He takes a LinkedIn post that people commented on and liked, scrapes the engagers with PhantomBuster, finds the email addresses behind those LinkedIn profiles using the Apollo API, validates the addresses with MillionVerifier, then loads them into Instantly AI for the cold email sequence. The targeting logic is that engagement with a specific post is a stronger intent signal than a job-title filter, because the person self-selected into the topic. He shared the whole stack openly and says the return was a stream of DMs from people offering better versions of the same workflow, which is his argument for publishing what works rather than hoarding it. For SEO teams the same chain works for outreach lists built from people engaging with topic-relevant posts.

> "I scrape it using PhantomBuster"

**Evidence:** Cody published the exact stack publicly and received multiple DMs from people running improved versions.

**How to do it**

1. Find LinkedIn posts on your exact topic that got meaningful comments and likes from your target profile.
2. Run PhantomBuster against the post to extract the profiles that engaged.
3. Push those profiles through the Apollo API to resolve work email addresses.
4. Run every address through MillionVerifier and drop anything not marked valid, to protect sender reputation.
5. Load the verified list into Instantly AI with a sequence referencing the specific post they engaged with.
6. Keep volume per sending domain low and warm the domains before sending.
7. Publish the workflow itself as content, since sharing it attracts better versions back from readers.

**Tools:** PhantomBuster, Apollo, MillionVerifier, Instantly AI, LinkedIn

**Pitfall:** Skipping the verification step burns the sending domain on bounces. Scraping LinkedIn engagers and emailing them without consent also carries GDPR exposure in the EU and UK, which Cody does not address.

**Apply at Pabau:** If Pabau ever runs outreach for links or partnerships, engagement-based targeting beats title-based lists, but the healthcare and EU customer base makes consent and data handling the binding constraint, not the tooling.

**Apply anywhere:** Build outreach lists from people who engaged with a topic-specific LinkedIn post rather than from title filters: PhantomBuster to scrape, Apollo to resolve emails, MillionVerifier to clean, Instantly to send. Check your jurisdiction's consent rules first.

### 11. Choose guest posting when you need a specific page linked, PR when you need authority  `121.13`
*useful · best practices · source 121*

Grow and Convert separate their two main link tactics by what each one can control. Guest posting is described as one of the most consistent and scalable approaches because you control the context around your link and can direct it to whichever pages you are trying to rank. Digital PR and media mentions bring links from high-authority domains such as major publications and well-known industry sites, which meaningfully lifts domain authority, but the tradeoff is that PR is harder to predict than guest posting and you have less control over which pages get linked. The practical consequence is that these are not interchangeable line items. A page that needs to move from position twelve to position four needs guest posts. A domain that needs to compete for a hard category keyword needs PR. Budgeting them as one pot means the page-level work never happens.

> "you have less control over which pages get linked"

**Evidence:** Grow and Convert's stated tradeoff: guest posting is consistent and directable, PR is high-authority but unpredictable in which pages get linked.

**How to do it**

1. Split the link budget into two named buckets before the quarter starts: page-level and domain-level.
2. Assign guest posting to the page-level bucket and set the destination URL for each placement in advance.
3. Qualify guest post targets on whether the site has real readers who could click through, not on domain rating alone.
4. Assign digital PR to the domain-level bucket: expert commentary to journalists, original research, or something genuinely newsworthy.
5. Accept that PR links will mostly land on the homepage or a research page, and plan internal links from there to the money pages.
6. Set different success measures per bucket: position change for guest posts, referring domains gained for PR.
7. Do not fund PR before the dedicated pages and intent matching are right, since neither tactic fixes a wrong keyword.

**Tools:** Ahrefs

**Pitfall:** Running digital PR to lift a specific article's ranking. The coverage lands on the homepage or an About page, the target article gains nothing, and the campaign is judged a failure for the wrong reason.

**Apply at Pabau:** Pabau should treat guest posts as the tool for pushing specific template and comparison pages onto page one, and reserve PR or original research for building pabau.com's overall authority.

**Apply anywhere:** Use guest posting when a named page needs to move up, and digital PR when the whole domain needs authority. Budget and measure them separately.

### 12. Concentrate link building on bottom-of-funnel pages for topical authority  `28.11`
*useful · best practices · source 28*

Rather than spreading link-building effort broadly, the team's SEO lead focused it specifically on bottom-of-funnel articles, using very selective and specific target sites rather than volume. The read on the strategy, from a peer familiar with the practitioner's usual approach, is that this reinforces topical authority around the core product concept, such as being an app for sign language, which in turn makes it structurally easier for the whole site to rank for other bottom-of-funnel, conversion-driving terms — link equity concentrated at the bottom of the funnel lifts the topical authority signal the entire cluster benefits from, not just the linked page.

> "it was also focused on bottom-of-funnel articles and text"

**How to do it**

1. Identify your highest-value bottom-of-funnel pages, the ones directly tied to conversions or signups, not top-of-funnel educational pages.
2. Build a shortlist of highly relevant, specific target sites for outreach rather than pursuing broad, generic link volume.
3. Prioritize link-building campaigns toward this bottom-of-funnel shortlist before allocating effort to top-of-funnel or informational pages.
4. Monitor whether topical-authority-adjacent bottom-of-funnel terms improve in ranking as this link equity accumulates (inferred: track rank movement for the specific cluster of bottom-of-funnel terms tied to the linked pages).

### 13. Confirm every backlink is actually indexed, or it's worthless  `32.2`
*useful · concrete actions · source 32*

Charles Floate's rule — "an unindexed backlink passes exactly zero PageRank" — means a backlink sitting on a page Google hasn't indexed contributes nothing to rankings no matter how good the site or content is; more broadly, even among indexed pages, backlinks on pages that themselves get organic search traffic matter more than backlinks on indexed-but-traffic-less pages. This makes indexation checking a mandatory final step of any link-building campaign, not an assumption.

> "An unindexed backlink passes exactly zero PageRank"

**How to do it**

1. After a link placement goes live, check whether the hosting page is actually indexed by Google (e.g., via a `site:` search or a URL-inspection tool).
2. If the page isn't indexed within a reasonable window, submit it through an indexing tool to force crawling rather than waiting passively.
3. Where possible, prioritize placements on pages that already receive organic search traffic themselves over placements on pages with no search visibility.
4. Periodically re-check previously acquired links' indexation status, since a page can lose its indexed status over time.

**Pitfall:** Treating a link as valuable the moment it's live, without confirming the hosting page is indexed, risks counting backlinks toward your link-building efforts that are actually passing zero ranking value.

### 14. Earn links and mentions by making friends or news  `20.5`
*useful · best practices · source 20*

The stated scalable philosophy for earning both links and mentions is to 'make friends or make news' — build real relationships or create something genuinely newsworthy — with everything else characterized as manipulation of the web (paid links, mass guest posting, comment spam). The approach is to build something compelling enough that people want to do the promotional work themselves rather than manually scaling outreach or paid placement. This is a strategic principle rather than a specific tactic — practical execution (linkable assets, PR-worthy campaigns) follows from committing to it first.

> "make friends or make news"

**How to do it**

1. Before running any new link- or mention-building initiative, categorize it as either 'make friends' (relationship/partnership-based) or 'make news' (create something genuinely newsworthy) — if it fits neither, treat it as manipulation and deprioritize it.
2. For the 'make news' path, identify a linkable asset you could build: original research/data, a genuinely useful free tool, a bold creative campaign, or content compelling enough that journalists want to cover it unprompted.
3. For the 'make friends' path, identify real relationships to build with journalists, creators, or complementary brands rather than transactional outreach requests.
4. Explicitly deprioritize scalable-but-manipulative tactics (paid link packages, mass guest-posting networks, comment/forum spam) as a primary strategy.
5. Design the asset or campaign so sharing/covering it benefits the sharer (a journalist gets a story, an industry peer gets useful data), not only you.
6. Track earned mentions/links generated from the asset separately from any paid/manufactured links, so you can see which channel is actually compounding over time.
7. Reinvest in whichever specific asset or relationship type is generating the most organic pickup rather than spreading effort evenly across many one-off pushes. (inferred prioritization step)

**Pitfall:** Treating scalable link-acquisition shortcuts (paid links, mass guest posting, comment spam) as a viable strategy — the speaker calls this 'manipulation of the web' and 'low-vibration work,' rejecting it in favor of building something people want to talk about on their own.

### 15. Everyone buys backlinks; sequence it after content and indexing  `07.18`
*useful · general insights · source 07*

The creator states plainly that 'everybody buys backlinks, especially in competitive niches,' framing Google's official anti-paid-link stance as real but widely disregarded in practice — a claim he supports by noting the paid-link industry wouldn't be worth billions if it didn't move rankings. Despite that, the explicit sequencing advice is not to buy links on day one: free tactics (local citations, Connectively) should come first, and paid backlink acquisition should only start once the site is built correctly, has good content, is indexed, and is still failing to outrank competitors identified in earlier competitor backlink-profile research. When that threshold is reached, the recommendation is a budgeted, vetted agency engagement rather than ad hoc marketplace purchases, with an explicit warning to get on a call with the provider first to confirm link quality and topical relevance before paying.

> "Google states they don't condone purchasing backlinks, and that's fine"

**Evidence:** Direct claim: 'everybody buys backlinks, especially in competitive niches... Google states they don't condone purchasing backlinks, and that's fine, but it wouldn't be a multi-billion-dollar industry by now if it didn't work.'

**Apply at Pabau:** David shouldn't treat 'buy some links' as a first move for a new or underperforming Pabau page — only escalate to paid links once on-page/content work is confirmed solid, the page is indexed, and it's still losing to specific competitors whose backlink profile was already sized up in competitor research; when that happens, vet any agency by call before paying, checking for topical relevance to Pabau's niche.

**Apply anywhere:** You shouldn't treat 'buy some links' as a first move for a new or underperforming page — only escalate to paid links once on-page/content work is confirmed solid, the page is indexed, and it's still losing to specific competitors whose backlink profile was already sized up in competitor research; when that happens, vet any agency by call before paying, checking for topical relevance to your niche.

### 16. Expired-domain redirects rank fast but risk a manual penalty  `17.5`
*useful · content insights · source 17*

A documented case study describes an affiliate site outranking major, established brands for high-volume keywords purely by buying old expired domains from relevant, previously-authoritative news outlets and 301-redirecting them directly to specific product pages, inheriting the expired domain's accumulated authority almost instantly. The rankings reportedly jumped very fast, but the case study is explicitly cited as a cautionary example: a manual penalty hit before long, undoing the gains. The host's own framing is that this kind of shortcut isn't actually necessary, since many valuable, high-intent keywords are under-targeted enough that you don't need heavy domain authority to rank for them at all if you target them with conversion-focused landing pages that clearly satisfy search intent.

> "301 redirecting them straight to specific product pages"

**Evidence:** Case study cited: an affiliate site bought expired domains from relevant authority news outlets and 301-redirected them to specific product pages, producing fast keyword ranking jumps for high-volume terms against major brands, until a manual penalty was applied.

**Apply at Pabau:** For Pabau, treat expired-domain 301 redirects as a high-risk, penalty-prone shortcut rather than a core tactic; the more durable, lower-risk path the host recommends instead is finding still-under-targeted, high-intent keywords in the category and winning them with clear, conversion-focused landing pages that satisfy search intent, since real domain authority isn't required for many of those terms.

**Apply anywhere:** For your site, treat expired-domain 301 redirects as a high-risk, penalty-prone shortcut rather than a core tactic; the more durable, lower-risk path the host recommends instead is finding still-under-targeted, high-intent keywords in the category and winning them with clear, conversion-focused landing pages that satisfy search intent, since real domain authority isn't required for many of those terms.

### 17. Four fundamental paths to acquiring backlinks  `24.1`
*useful · general insights · source 24*

A popular Reddit answer (from "Grumpy SEO Guy," relayed and endorsed by the host) frames backlink acquisition as four distinct paths: (1) earn them passively by doing nothing once you're already ranking on page one, since people naturally link to pages they find while researching their own content — this only works after you've already broken through; (2) buy them directly, repeatedly flagged as requiring real expertise to do safely; (3) do link outreach/guest posting, which reliably works but is time-intensive; and (4) build and own additional websites specifically to link from, which resembles a PBN (private blog network) — controversial (some say PBNs still work, others don't like them) but, per the source, the most effective path long-term despite being the most expensive to set up initially.

> "it's best in the long run, most expensive to start"

**Evidence:** Sourced from a single top-upvoted Reddit comment on r/SEO plus the host's own commentary endorsing it, not a controlled test.

**Apply:** Use this as a framework for allocating effort by stage: for a site not yet ranking, "do nothing" isn't viable yet, so budget should split between disciplined outreach/guest-posting and, if resourced for it, owned-property building — while treating direct link-buying as something to only attempt with real expertise in avoiding penalty risk.

### 18. Google's tolerance for gray/black-hat tracks niche economics, not morality  `38.9`
*useful · general insights · source 38*

Kalin frames Google's actual concern as economic rather than moral: in 'fun' niches (games, movies) natural backlinks accumulate on their own, so fully white-hat strategies work; in non-fun, high-value commercial niches (his example: roofing in Manchester, or iGaming/casino) essentially no one links naturally, forcing paid links or PBNs as the only realistic path, and Google tolerates this because the real threat it wants to filter out is cheap, infinitely scalable spam from unsophisticated actors — not expensive gray-hat tactics used by serious, well-funded operators. As evidence he cites his own company selling PBN links to Bet365 for about $100 when the brand needed a link in a 'fringe country in a fringe niche,' showing that even large, legitimate brands buy gray-hat links once a market gets competitive enough.

> "no one will put natural backlinks"

**Evidence:** Direct claim: 'If it's not a fun niche — let's say roofing in Manchester — no one will put natural backlinks, so we can't afford to be completely white hat.' Supporting example: 'We've sold PBN links to brands like Bet365 in the past... they end up on our blog and buy a link for $100.'

**Apply at Pabau:** When assessing link-building risk for a given Pabau content topic, judge it by whether the topic naturally attracts editorial coverage (practice-management/healthtech has real trade press, awards, and case studies, so genuine digital PR is viable) rather than assuming all paid or non-organic link activity is equally risky across every niche.

**Apply anywhere:** When assessing link-building risk for a given content topic, judge it by whether the topic naturally attracts editorial coverage — a sector with real trade press, awards, and case studies makes genuine digital PR viable — rather than assuming all paid or non-organic link activity is equally risky across every niche.

### 19. Guest posting and digital PR still move rankings most in 2026  `26.14`
*useful · general insights · source 26*

Asked which link tactics still move rankings at scale, Dooley ranks guest posting (done as a genuine extension of the brand's entity, not generic filler) and digital PR as the two that 'move the needle the most,' despite digital PR's expense, because access to highly trusted sites others won't pay for is a differentiator. He adds that PBNs have started working again after a period of decline, local and industry citations still perform well, and press releases remain valuable for a fast 'link sprint of 300 referring domains' — but only when the resulting pages are force-indexed, tying back to his indexing-first workflow.

> "the link sprint of 300 referring domains pretty quickly"

**Evidence:** "Press releases can do very well, because you get the link sprint of 300 referring domains pretty quickly, as long as you force-index them... the main ones I'd say are guest posting and digital PR — those still move the needle the most."

**Apply at Pabau:** When allocating Pabau's link-building budget, prioritize digital PR placements on genuinely trusted, hard-to-get sites and guest posts written as real extensions of Pabau's entity (proof points, case studies) over generic guest posting, and treat press releases as a quick-but-shallow referring-domain boost rather than a primary strategy.

**Apply anywhere:** When allocating your link-building budget, prioritize digital PR placements on genuinely trusted, hard-to-get sites and guest posts written as real extensions of your entity (proof points, case studies) over generic guest posting, and treat press releases as a quick-but-shallow referring-domain boost rather than a primary strategy.

### 20. Judge SERP competition by reading the top ten, not by a difficulty score  `128.7`
*useful · best practices · source 128*

Devesh is blunt that on the judgment half of link prioritization he rarely relies on any tools. Instead he opens the first page for the keyword, scrolls through the ranking articles and reads them, asking a fixed set of questions: is the article genuinely good, does it solve the problem for the reader, and is it organized in a helpful fashion. That reading tells him how hard the keyword should be. The decision rule he derives is a single question, do we truly think our article is better than everything out there, and if the answer is yes he commits heavy link-building effort. This is a direct contradiction of the difficulty-score approach: a high keyword difficulty on a page of weak, unhelpful articles is not a reason to skip, and a low score on a page of genuinely strong pieces is not a reason to spend.

> "I rarely rely on any tools"

**Evidence:** Devesh of Grow and Convert says he rarely uses tools for SERP competition and judges by reading the first-page articles for genuine reader value.

**How to do it**

1. Open the SERP for the target keyword and read the top ten results properly, not just the titles.
2. For each result ask whether the article is genuinely good, whether it actually solves the reader's problem, and whether it is organized helpfully.
3. Note which results are thin, generic overviews or badly structured, since those are the ones you can beat on content alone.
4. Compare your article against that set honestly and answer one question: is ours better than everything on this page.
5. If yes, commit heavy link building to it and expect the links to close an authority gap, not a quality gap.
6. If no, fix the article before spending anything on links.
7. Use keyword difficulty only as a rough sanity check on how many referring domains the winners carry, never as the go or no-go.

**Pitfall:** Deferring to a difficulty score. It reads the link graph, not the content, so it tells you to skip beatable SERPs full of weak articles and to spend on SERPs where your piece is genuinely worse.

**Apply at Pabau:** Before David commissions links for a Pabau comparison or template page, he should read the top ten manually and confirm the Pabau page is the better answer. If it is not, the fix is the article, not the outreach.

**Apply anywhere:** Assess SERP competition by reading the top ten results and judging whether each genuinely solves the reader's problem. Commit a link budget only when you can honestly say your page is the best on that page. Difficulty scores read the link graph, not the content, so they mislead in both directions.
