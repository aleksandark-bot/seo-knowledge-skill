# E-E-A-T & Authority — core (part 1 of 2)

17 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Add notability and transparency to E-E-A-T as the NEEATT frame  `76.7`
*core · best practices · source 76*

The paper argues E-E-A-T has a structural limitation under agentic search: machines cannot assess credibility without an identity. If the engine cannot identify who you are, it cannot apply any credibility signal to what you say, so credibility requires a prior step the authors call understandability. That is the logic behind Jason Barnard's NEEATT, which extends E-E-A-T with notability and transparency. Notability is recognition across third-party sources and functions as a multiplier: an expert's claim is weighted substantially more if that expert is frequently cited across disparate high-authority datasets. Crucially it is comparative, not absolute, so a niche brand can outscore a large company that is diffusely present across many domains. Transparency is clarity about ownership, authorship and intent, delivered through structured data, consistent entity descriptions and machine-readable markup, which the paper calls prerequisites for credibility evaluation to happen at all.

> "machines cannot assess credibility without an identity"

**Evidence:** NEEATT as developed by Jason Barnard: six components, adding notability as a comparative multiplier and transparency as a prerequisite to E-E-A-T's original four.

**How to do it**

1. Treat transparency as the gate, not a tick-box: publish ownership, authorship and intent in machine-readable form before doing any other credibility work.
2. Add organization and person schema, plus a consistent entity description reused verbatim everywhere.
3. Measure notability comparatively inside your niche, counting third-party citations of your named experts within that domain, not across the whole web.
4. Get your named experts cited across several disparate high-authority datasets rather than repeatedly in one publication.
5. Attach direct experience evidence to content: case studies, firsthand accounts and practitioner data, which the paper says LLMs use to separate human-verified from secondhand content.
6. Audit for contradictory claims across your properties, since inconsistency erodes trustworthiness and gets content filtered during grounding.

**Pitfall:** Investing in expertise signals on a site whose ownership and authorship are not machine-parsable. The engine cannot map the content to an entity, so none of the credibility work is applied.

**Apply at Pabau:** Pabau is in a narrow vertical, which is where comparative notability pays. Get named Pabau clinical and product experts cited across aesthetics trade publications rather than chasing broad tech coverage.

**Apply anywhere:** Comparative notability pays inside a narrow vertical. Get your named experts cited across that vertical's trade publications rather than chasing broad mainstream coverage.

### 2. Add sitewide transparency info before ranking competitively  `18.5`
*core · best practices · source 18*

Google's actual manual-action language for the 'transparency' penalty (quoted verbatim in the transcript) names four missing elements: clear dates, bylines, author/publisher/company/network information, and contact information — not vague 'EEAT' concepts like expertise claims or author bios alone. The speakers' case study (a football-betting site that reached page one for 'Bet365' around position 7) got hit with exactly this manual action within roughly a day of a Rater Hub visit, and it demoted the entire site, not just the offending page. Because roughly 90%-plus of sites they've seen get a Rater Hub visit are later penalized, and the penalty only seems to trigger once a site is ranking for genuinely competitive terms, treating this checklist as mandatory 'insurance' (not a ranking booster) before or as you break into page one is cheap relative to the downside of a sitewide demotion.

> "lacks clear dates, bylines, information about the authors"

**How to do it**

1. Audit every page template (About, Team, Article, Privacy Policy) for four elements: a visible publish/update date, a named byline/author, a company/publisher identity block, and findable contact information.
2. Add or confirm a company/publisher information page listing legal entity name, registered address or company number, and a way to contact the business. (inferred)
3. Add author bylines to editorial content, linking each to a real author or company profile page.
4. Add visible last-updated/published dates to every article template sitewide, not just cornerstone pages, since the manual-action wording explicitly cites 'clear dates.'
5. Prioritize this audit before or as soon as a page starts ranking on page one for a competitive or YMYL-adjacent keyword, since that's the trigger point quality raters reportedly review.
6. Treat this as mandatory in gambling, finance, health, or other YMYL-adjacent verticals; keep it as cheap ongoing insurance even for lower-stakes sites.
7. If a manual action ever appears in Search Console, save the exact wording so you can confirm which specific element (dates/bylines/author/publisher/contact) was flagged and fix that gap directly.

**Tools:** Google Search Console

**Pitfall:** Treating 'EEAT' as vague content-quality signals (generic author bios, keyword-stuffed expertise claims) instead of the specific, narrow checklist Google's actual manual-action notice cites: dates, bylines, author/publisher/company info, and contact information.

### 3. Budget four to nine months, and longer for an established company  `73.12`
*core · general insights · source 73*

Barnard gives concrete timelines rather than a vague promise. Google has focused on people for the last three or four years, so people are relatively easy and corporations relatively hard. His two recent cases: a well-established company took nine months, while a brand new company took four to five months, because they could build it from nothing and every profile was correct from the very beginning. The longer case was slower because the footprint was bigger and messier, and sorting out the mess and letting the machine digest it is a process that takes time. His overall expectation, given the entity home plus the platform set, is a knowledge panel in three months to a year, with an explicit caveat that this is his firm's experience and not a guarantee. He also notes search volume for the name is irrelevant to whether you get one: Google is trying to understand everything, and if it understands, it gives you a panel.

> "It took 9 months but for a new company it took four or five months"

**Evidence:** Barnard's two named cases: an established company at nine months, a new company at four to five months, against a general expectation of three months to a year.

**How to do it**

1. Decide whether you are building a new entity or cleaning up an established one, since that decides the timeline.
2. For a new entity, create every profile correct on day one rather than fixing them later, and budget four to five months.
3. For an established entity, budget nine months or more and spend the first phase auditing and correcting the existing footprint.
4. Inventory every existing mention you control and record where the facts disagree with the intended entity home.
5. Correct the contradictions before adding any new profiles, so the machine is not digesting old and new versions at once.
6. Set stakeholder expectations at three months to a year and state plainly that it is not guaranteed.
7. Do not use low search volume for the brand name as a reason to skip the work, since volume does not affect whether a panel is created.

**Pitfall:** Promising a knowledge panel on a quarter's timeline for a company with an existing footprint. Cleaning up contradictions is the bulk of the work, and Barnard's established-company case ran to nine months.

**Apply at Pabau:** Pabau is established with a large existing footprint, so plan a knowledge panel effort as a nine-month programme starting with a footprint audit, not a quarter-long project.

**Apply anywhere:** Budget four to five months for a brand new entity built correct from scratch, and nine months or more for an established one with a messy footprint. Spend the first phase correcting contradictions, not creating new profiles.

### 4. Build a branded off-site trust and awards stack  `15.7`
*core · concrete actions · source 15*

To make a site 'brandable,' James builds out a stack of off-page trust signals: 20-50 business-listing citations, review profiles on third-party sites like Trustpilot and Yelp, a Google Business Profile actively collecting reviews, and a library of case studies. He deliberately researches what awards exist in the specific industry and applies to win them, since a genuine award earns a legitimate 'award-winning' claim to use in marketing once won. He then builds a 'branded social fortress' - consistently-branded profiles across Twitter/X, Facebook, LinkedIn, Flickr, and other Web 2.0 properties - to distribute that proof point and accumulate real firsthand-experience and reputation signals rather than isolated marketing assets.

> "I need to make certain I'm getting citations built out"

**How to do it**

1. Build out roughly 20-50 business-listing citations across standard directories for consistent brand name/address/phone presence.
2. Set up profiles on third-party review platforms such as Trustpilot and Yelp so customers can leave reviews there.
3. Claim and optimize a Google Business Profile and actively collect reviews onto it.
4. Produce a library of case studies documenting real client/customer results.
5. Research what industry awards exist in your specific vertical and apply to win them.
6. When you win an award, distribute that proof point across all social media channels immediately.
7. Build a 'branded social fortress' - claim and actively maintain consistently-branded profiles on Twitter/X, Facebook, LinkedIn, Flickr, and other Web 2.0 properties.
8. Treat the accumulated stack (citations, third-party reviews, GBP reviews, case studies, awards, social fortress) as the basis for real firsthand-experience and reputation signals, not isolated one-off marketing assets.

**Tools:** Trustpilot, Yelp, Google Business Profile, Twitter/X, Facebook, LinkedIn, Flickr

### 5. Build brand and entity pages as the canonical, verifiable record  `66.10`
*core · concrete actions · source 66*

The framework's cheapest high-return content type: pages that establish the canonical facts about the organization — what it is and what it offers, who owns or represents it, where it operates and why it can be trusted. Its role is entity clarity and verification, explicitly not detailed product instructions, live availability or conversion. It covers about, organization, leadership, author, trust, location and product or service overview pages, and the quality bar is consistent facts, disclosed ownership or authorship, verifiable claims and a clear internal hierarchy. It scores High on citation potential, brand mention potential, business value and proprietary advantage at Low expected effort — the best ratio in the entire worksheet — with only Medium click resilience, because an AI system can state who you are without sending a visit. That trade is the point: you are funding the accuracy of what gets said about you, not the click.

> "Its role is to provide entity clarity and verification"

**How to do it**

1. Inventory the entity pages you already have: about, company, leadership, author bios, trust and security, locations, and the top-level product or service overview.
2. Pick one page per fact as the canonical source, and make every other mention of that fact point to it rather than restating it.
3. Write the facts plainly and consistently: legal entity name, what the organization does, who owns or operates it, where it operates, when it was founded, and the markets it serves. Use identical wording across pages.
4. Disclose ownership and authorship explicitly, with named people, real roles and links to their profiles, rather than a generic 'our team'.
5. Make every trust claim verifiable — certifications, registrations, customer counts, compliance standards — each with a date and a source a third party could check.
6. Give the set a clear internal hierarchy: one top-level entity page linking down to leadership, authors, locations and product overviews, and each of those linking back up.
7. Mirror the same facts in structured data (Organization, plus Person for authors and LocalBusiness for locations) and keep the markup and the visible copy identical.
8. Cross-check the same facts on off-site profiles that AI systems read — the business profile, LinkedIn, Crunchbase, review platforms — and correct any that disagree.
9. Set a review date, because the value of this content type is entirely in its being current and consistent.

**Tools:** Google Business Profile, Schema.org, Screaming Frog

**Pitfall:** Loading the entity pages with product instructions, live pricing or conversion copy. The framework assigns those jobs to other content types, and mixing them in is what makes entity facts inconsistent across the site — the one failure that breaks the whole type's purpose.

**Apply at Pabau:** This is the highest-ratio work available to Pabau: Low effort, High on four of five value dimensions. Make one page the canonical source for what Pabau is, who runs it, which markets it serves and the customer figures, then make every other page defer to it instead of restating the numbers differently.

**Apply anywhere:** This is the highest-ratio work in the framework: Low effort, High on four of five value dimensions. Make one page the canonical source for what the organization is, who runs it, which markets it serves and the customer figures, then make every other page defer to it instead of restating the numbers differently.

### 6. Build domain-wide topic coverage because ChatGPT reuses the same brands  `87.13`
*core · content insights · source 87*

Grow and Convert cite SparkToro's finding that the top three most-mentioned brands were cited 64% of the time for the same prompt on ChatGPT, meaning a small set of brands dominates repeat answers. Their own data points the same way: counting domain matches rather than URL matches lifted overlap from 27% to about 50%, which they read as ChatGPT favoring domains it treats as topically authoritative even when the exact ranking page is not the cited one. The takeaway they draw is that your domain's broader presence across a topic may matter more than whether one page ranks for one query. The route they name to that authority is consistently publishing detailed, substantive content on the real pain points customers have, not meta tags and FAQ schema.

> "top 3 most mentioned brands were cited 64%"

**Evidence:** SparkToro: top 3 brands cited 64% of the time for the same ChatGPT prompt. Grow and Convert: domain-match overlap ~50% versus 27% URL-match.

**Pitfall:** Spreading coverage thinly across many topics. Authority in this model is depth within one topic area, so a wide shallow library builds none of it.

**Apply at Pabau:** Pabau should concentrate publishing on aesthetic and healthcare practice management rather than drifting into general small-business topics. Depth in one area is what gets the domain recognized.

**Apply anywhere:** Concentrate publishing depth inside one topic area rather than spreading across many. Domain-level topical recognition is what drives repeat citation.

### 7. Build one entity home and make every third-party profile echo it  `76.6`
*core · concrete actions · source 76*

The paper works through Jason Barnard's 'Entity Home': a single authoritative brand-owned property where the retrieval, synthesis and validation layers can find definitive facts about the brand's identity, purpose and activities. Typically it is the homepage or a dedicated About page, but the concept is more precise than having a website. It is the canonical reference point against which the Knowledge Graph corroborates third-party information. The paper's requirements are specific: explicit machine-readable statements of what the brand is, what it does, what category it belongs to and who it serves; organization schema at minimum, mapping to Knowledge Graph entity types; consistent maintenance so the page is reliably current; and external corroboration. Its example is blunt. If the homepage says the brand is an enterprise SaaS company specializing in supply chain logistics, that same characterization must appear on LinkedIn, Crunchbase, press mentions, directory entries and Wikipedia. Inconsistencies erode the confidence score and delay or prevent recognition.

> "the canonical reference point against which the Knowledge Graph corroborates information"

**Evidence:** Barnard's framework as summarized in the paper: the Knowledge Graph builds confidence through corroboration, and inconsistencies erode the entity's confidence score.

**How to do it**

1. Pick one page as the entity home, either the homepage or a dedicated About page, and say so internally so nobody adds a second.
2. Write four explicit statements on it: what the brand is, what it does, what category it belongs to, who it serves.
3. Add organization schema mapping those statements to Knowledge Graph entity types.
4. Inventory every external profile: LinkedIn, Crunchbase, review platforms, directories, press mentions, Wikipedia.
5. Diff each profile's description against the entity home wording and list every disagreement.
6. Correct the contradicting profiles before adding any new ones, so the graph is not digesting two versions at once.
7. Put the entity home on a maintenance schedule so its facts stay current, since staleness reads as unreliability.

**Pitfall:** Adding new profiles while old ones still carry an outdated category or description. Corroboration is what builds confidence, so contradictory sources actively lower the entity's score rather than being ignored.

**Apply at Pabau:** Pabau needs one named entity home with a single agreed one-line category description, then a sweep of LinkedIn, Crunchbase, review sites and directory listings to make them all repeat it word for word.

**Apply anywhere:** Name one entity home with a single agreed one-line category description, then sweep every external profile so they all repeat it word for word.

### 8. Build proof before you have clients by publishing your own experiments  `169.7`
*core · concrete actions · source 169*

Criteria four in Hyam's framework is proving the positioning is true, and he is direct that a new business will be weak here and that this is normal. Grow and Convert had no client case studies at launch but it was not zero: they had success stories from past work, Hyam's from ThinkApps and Vistage and Khanal's conversion work with Backlinko and Bryan Harris at Video Fruit. On top of that they manufactured proof. They published case studies of their own promotion techniques, published case studies of their conversion tactics, ran a live public challenge growing the site from scratch, and gave talks and podcast interviews about content strategy. Today the proof is a library of case studies, some published on the site and some emailed to prospects after a call. The sequence matters: get first customers by any honest route, then convert them into the proof asset.

> "We did a live challenge of us growing this site from scratch"

**Evidence:** Grow and Convert launched with prior-employer results plus self-published promotion and conversion case studies, a live growth challenge, talks and podcasts, and now maintains a case study library split between published and emailed.

**How to do it**

1. List every past result you personally own, including work done at previous employers or for named clients.
2. Publish a case study of one technique you use, showing the method and the numbers, before you have client results.
3. Run a public build-in-public challenge on your own property and report the numbers as they come in.
4. Book podcast interviews and talks on the specific method rather than on your company.
5. Land the first few customers using that borrowed and self-generated proof.
6. Turn each early engagement into a written case study with the metric the buyer cares about.
7. Split the library: publish some case studies openly and hold others to email after a sales call.
8. Refresh the published set as results improve so the strongest proof is the public one.

**Pitfall:** Waiting for client results before publishing anything. Hyam's point is that proof at launch is never strong, so a company that treats proof as something clients give it stays invisible until someone takes a risk on it.

**Apply at Pabau:** Pabau should publish case studies of its own marketing and product experiments alongside clinic case studies, and keep a set of deeper results to email prospects after a demo. That gives the blog proof pages the E-E-A-T signals a vendor site otherwise lacks.

**Apply anywhere:** Manufacture proof before customers give you any. Publish case studies of your own techniques, run a public growth challenge on your own site, do talks and podcasts on the method, then convert your first customers into written case studies.

### 9. Check GA's Audience report for Rater Hub visits  `18.4`
*core · concrete actions · source 18*

Rater Hub is described as the portal Google's outsourced Quality Raters (via vendors like Lionbridge) use when manually reviewing a site, and these visits show up as a traffic source inside Google Analytics' Audience report, with the specific pages visited also visible (typically About, meet-the-team, and privacy-policy pages). Per the speakers, roughly 90%-plus of the sites they've observed getting a Rater Hub visit went on to be penalized, and the pattern reportedly only triggers once a site starts ranking for genuinely competitive keywords — they've seen it on about a dozen of their 'thousands' of sites. Their case study: a football-betting site ('Away Grounds') reached page one for 'Bet365' around position 7, Rater Hub hit shortly after, and a transparency-related manual action followed within roughly 24-48 hours.

> "if you go into Analytics, into your Audience section"

**How to do it**

1. Open Google Analytics for the property in question and navigate to the Audience section of the report.
2. Look for a referrer/source segment labeled 'Rater Hub' — the vendor portal (e.g. Lionbridge) Google's human Quality Raters use to view sites.
3. Check which specific pages were visited; per the source these are typically the About page, meet-the-team page, and privacy policy page.
4. Cross-reference the visit date against your ranking history to see if the site recently broke into page one for a competitive keyword, since that's the reported trigger point.
5. If a Rater Hub visit appears, immediately check Google Search Console's Manual Actions report over the following 24-48 hours for a transparency-related manual action.
6. If a manual action appears, audit the site for the specific transparency elements Google's notice cites (dates, bylines, author/publisher info, contact info) rather than assuming it's a generic content-quality issue. (inferred)
7. Set a recurring check (e.g. monthly) on GA's Audience report for any site newly ranking on competitive terms, since the reported pattern hits roughly 90%+ of visited sites. (inferred)

**Tools:** Google Analytics, Google Search Console

**Pitfall:** Assuming a ranking drop is purely algorithmic or content-quality-related when it may actually be an incoming Rater-Hub-triggered manual action — check the Manual Actions report in Search Console rather than only rewriting content.

### 10. Dec 2025 core update folds social/video channels into Search Console  `25.14`
*core · content insights · source 25*

Koray highlights that Google's December 2025 core update (announced December 12) began integrating social/video channel performance directly into Google Search Console; he reports already seeing this show up in Search Console for some of his sites, letting him see clicks generated through his YouTube channels. Notably, even without publishing new videos, some sites (he cites travel) are getting more clicks because Google has started promoting video content more heavily in travel-related queries, meaning this is a ranking-surface shift, not just a reporting change. He ties this to a broader 'web entity vs. website' distinction covered earlier in the same discussion, where a Google 'About this source' panel attributes LinkedIn and Reddit profiles to the entity/brand name rather than to linkedin.com or reddit.com, and notes TikTok can now show up as a crawl referrer in server log files, meaning it is being actively crawled as a discovery/freshness source.

> "that they're integrating social channels into Search Console, and I have"

**Evidence:** Google's December 12, 2025 core update integrating social channels into Search Console (Koray reports seeing YouTube-driven Google clicks appear in GSC for some sites); travel-industry sites getting more clicks with no new video uploads, attributed to Google promoting video content more in travel queries; TikTok appearing as a crawl referrer in server log files.

**Apply at Pabau:** Check Google Search Console on Pabau's properties for any new social/video-channel breakdown, and treat Pabau's YouTube presence as a live ranking/traffic input rather than a purely separate marketing channel; also check server logs for TikTok crawler activity as an early freshness/discovery signal.

**Apply anywhere:** Check Google Search Console on your properties for any new social/video-channel breakdown, and treat your YouTube presence as a live ranking/traffic input rather than a purely separate marketing channel; also check server logs for TikTok crawler activity as an early freshness/discovery signal.

### 11. Document customer outcomes with the starting point, actions and measured result  `66.16`
*core · concrete actions · source 66*

Content that documents what changed after a real product, service or approach was used, including the starting point, actions, constraints, timeline and measured outcome. Its role is 'Show me that it worked in a comparable situation' — explicitly not teaching the general process, testing one product in isolation, or comparing alternatives. It covers customer case studies, before-and-after analyses, documented experiments and implementation stories supported by real inputs, screenshots, outputs and measurable results. It scores High on click resilience, business value and proprietary advantage at Medium effort, with Medium citation potential and Medium brand mention potential. The five required components are the whole quality bar, and the starting point is the one most often missing: without it the outcome has no scale, and a reader cannot tell whether the situation was comparable to theirs. That comparability is what the type sells — the reason click resilience is High is that an AI summary of 'it worked' cannot substitute for inspecting whether it worked for someone like you.

> "documents what changed after a real product, service or approach was used"

**How to do it**

1. Pick a real customer or a real internal experiment where you can access the actual numbers, not an anonymized composite.
2. Record the starting point first: the metric before, the situation, the size of the operation, and the market. Without this the result has no scale.
3. Describe the actions taken in enough detail that a comparable reader could follow them, including what was tried and abandoned.
4. State the constraints — budget, team size, regulation, existing systems — because they are what make the case comparable or not.
5. Give the timeline, with dates, so the reader can judge how long the result took to appear.
6. Report the measured outcome against the same metric as the starting point, and show the raw figure alongside any percentage.
7. Include the evidence: real inputs, screenshots, exported reports, and outputs from the systems involved.
8. Get written approval from the customer for every figure and screenshot, and agree in advance what can be named.
9. Describe who this case does not apply to, since that is what makes the comparability claim credible.
10. Link to the general how-to and the product documentation rather than teaching the process inside the case study.

**Tools:** Google Analytics, Google Search Console

**Pitfall:** Publishing the outcome without the starting point. A result with no baseline cannot be judged for scale or comparability, which is the single job of this content type — and it reads as marketing rather than evidence.

**Apply at Pabau:** Pabau case studies need the practice's before figure, its size and market, the constraints it worked under, the timeline and the after figure from the same metric — with the customer's written sign-off on each number. A case study that only reports the improvement is not doing this type's job.

**Apply anywhere:** A case study needs the customer's before figure, their size and market, the constraints they worked under, the timeline and the after figure from the same metric — with written sign-off on each number. A case study that only reports the improvement is not doing this type's job.

### 12. Don't stretch topical authority into unrelated informational content  `37.5`
*core · content insights · source 37*

Jotform's informational-keyword clicks are spiking dramatically site-wide, including pages like /blog/rsvp-meaning targeting 'what does RSVP stand for?' - still plausibly related to Jotform's forms product, but edging toward marginal relevance. Edward flags this as the same pattern that preceded HubSpot's collapse: HubSpot, a CRM, expanded into informational content increasingly unrelated to its core product (like generic inspirational quotes), stretched its topical authority too far, and its rankings broke as a result.

> "HubSpot stretched its topical authority too much, and then it broke"

**Evidence:** Named precedent: HubSpot (a CRM) chased informational keywords unrelated to its core product (e.g., quotes content) until its topical authority broke; Jotform is currently showing a similar spike in informational clicks, including tangentially-related pages like an RSVP-meaning blog post, which the video flags as an early warning sign of the same pattern.

**Apply:** When expanding into informational content to capture rising search volume, continuously check each new topic's genuine relevance to your core product rather than chasing volume alone - a spike in informational clicks should be treated as a metric to watch cautiously, since HubSpot's precedent shows topical overreach can eventually collapse a whole site's authority, not just the tangential pages.

### 13. Due-diligence buyers skip on-site reviews but trust others  `47.1`
*core · content insights · source 47*

Edward highlights a specific, easy-to-miss due-diligence behavior: prospective customers who are actively vetting a brand deliberately skip the reviews posted on that brand's own website, and many won't even look at an on-site reviews section at all. His inference is that on-site reviews are treated as self-selected marketing and therefore discounted as untrustworthy by a skeptical buyer doing real diligence. His conclusion is that the fix isn't writing better on-site reviews, it's relocating the exact same review content onto third-party platforms and social channels, since people will read and trust the identical review text once it appears somewhere other than the brand's own domain.

> "don't want to look at the reviews that are on your website"

**Evidence:** Edward's direct observational claim, presented as 'something that a lot of people don't know': buyers in due-diligence mode skip on-site reviews and many of them won't even look at a website's own reviews section, while being receptive to the same review content found elsewhere.

**Apply at Pabau:** Don't treat an on-site testimonials or reviews section as sufficient proof for Pabau - actively republish and distribute the same positive customer feedback to third-party channels, such as review platforms, YouTube, and social, where a skeptical buyer doing vendor due diligence is actually willing to read it.

**Apply anywhere:** Don't treat an on-site testimonials or reviews section as sufficient proof for your own site - actively republish and distribute the same positive customer feedback to third-party channels, such as review platforms, YouTube, and social, where a skeptical buyer doing vendor due diligence is actually willing to read it.

### 14. E-A-T is algorithmic only within a narrow YMYL scope  `21.10`
*core · content insights · source 21*

David cites Google's John Mueller speaking at the Search Central Live New York City event stating flatly that E-A-T 'is not something you can add to a website' - it was built as a rubric for third-party quality raters to judge search result quality, not a rank-factor checklist for SEOs, and Mueller explicitly said that is not how it works. Mueller further stated E-A-T only comes into play algorithmically for sites affecting health or finance - Google's defined 'your money or your life' (YMYL) topics - and does not apply to any other topic at all. David backs this with his own experience across hundreds of domains and several real client projects: the only case where he ever saw YMYL actually gate rankings involved COVID-vaccine-technology content, where just 7-12 competing pages existed industry-wide and identical content would not rank on a domain lacking the right authority signals.

> "E-A-T comes into play algorithmically for sites that affect health or finance"

**Evidence:** Primary-source citation: John Mueller at Search Central Live NYC stating E-A-T cannot be added to a site and applies algorithmically only to YMYL topics; supporting anecdote: across David's hundreds of domains and client projects, the only confirmed YMYL-gated ranking case was COVID-vaccine-related content with just 7-12 competing pages worldwide.

**Apply at Pabau:** For a B2B SaaS site like Pabau, don't treat E-A-T as an on-page checklist (author bios, expert quotes, outbound citations) expected to directly move rankings - per Google's own stated position it isn't algorithmic outside genuine YMYL topics, so prioritize relevance, authority, and intent-match fundamentals over performative trust-signal additions, reserving genuine rigor for any content straying into regulated health/financial claims.

**Apply anywhere:** For a B2B SaaS site like your site, don't treat E-A-T as an on-page checklist (author bios, expert quotes, outbound citations) expected to directly move rankings - per Google's own stated position it isn't algorithmic outside genuine YMYL topics, so prioritize relevance, authority, and intent-match fundamentals over performative trust-signal additions, reserving genuine rigor for any content straying into regulated health/financial claims.

### 15. Heavy brand mentions can outweigh the link graph  `20.4`
*core · content insights · source 20*

Brand/entity mentions build Google's confidence in what a brand or person is known for — the more consistently a topic is associated with you across many pages (the example given: 100,000 mentions), the more that becomes part of Google's understanding of you as an entity, whereas a sudden topical pivot isn't recognized without that contextual buildup. Links still function as a supporting signal for entity association, but heavy, consistent mentions across the web typically outweigh what the link graph alone would indicate, because Google can corroborate the association across many independent sources. This weighting is applied dynamically per query space by a series of scoring 'microservices,' not one fixed rule.

> "mentioning it heavily across the web will likely overpower"

**Evidence:** 'If you're mentioned in, let's say, 100,000 pages, Google has a lot of consistency potentially in what's said about you or your brand... mentioning it heavily across the web will likely overpower what's happening in the link graph.'

**Apply at Pabau:** For Pabau's E-E-A-T and topical-authority building, David should treat volume and consistency of unlinked brand/topic mentions (press coverage, review platforms, community discussion, citations) as a first-class signal worth tracking and pursuing deliberately, not merely a byproduct of successful link building.

**Apply anywhere:** For your E-E-A-T and topical-authority building, you should treat volume and consistency of unlinked brand/topic mentions (press coverage, review platforms, community discussion, citations) as a first-class signal worth tracking and pursuing deliberately, not merely a byproduct of successful link building.

### 16. Link out from the entity home to every corroborating profile  `73.3`
*core · concrete actions · source 73*

Barnard's second-ranked factor after clarity and consistency is outbound linking from the entity home to every profile that corroborates you. He is blunt that hoarding link equity is the wrong instinct here: you cannot keep your link juice in this circumstance if you want to be understood. The mechanism he calls the infinite loop of self-corroboration - the entity home links out to LinkedIn, Crunchbase or TheOrg.com, those platforms link back to the entity home, and the crawler loops between them confirming the same facts. That loop is what he says produces confidence fastest. He also stresses that it is not set-and-forget: the web degrades, profiles get deleted or moved, and LinkedIn only redirects a changed handle for a year before returning a 404. Broken corroboration links have to be found and repaired on a schedule.

> "the infinite loop of self-corroboration"

**Evidence:** Barnard reports a new company reached a knowledge panel in four to five months using this loop, versus nine months for an established company with a messy footprint.

**How to do it**

1. List every profile, directory listing and platform page that describes the entity and that you control.
2. Add outbound links to all of them from the entity home, in visible HTML, not only in schema.
3. On each platform profile, set the website field to point back at the entity home URL, not the homepage, so the loop closes.
4. Drop any profile whose stated facts disagree with the entity home rather than linking to it.
5. Record the full list in a spreadsheet with the profile URL, the back-link URL and the date checked.
6. Re-crawl that list quarterly with a link checker and fix 404s, especially LinkedIn handles, whose redirects expire after one year.
7. Add the link to the entity home every time a new profile is created, as part of the profile-creation checklist.

**Tools:** LinkedIn, Crunchbase, TheOrg.com

**Pitfall:** Treating the link list as a one-time task. Barnard warns the web degrades: profiles move, handles change, and a LinkedIn handle stops redirecting after a year, quietly breaking the corroboration loop you built.

**Apply at Pabau:** Add a linked profile list to the Pabau About page covering LinkedIn, Crunchbase, Trustpilot, G2 and Capterra, make sure each of those points back to the About page rather than the homepage, and re-check the set every quarter.

**Apply anywhere:** Link from your entity home to every profile that corroborates your facts, and make each of those profiles link back to that same page. Keep the list in a spreadsheet and re-check it quarterly, because platform URLs and handles break.

### 17. Make the About page your entity home, not the homepage  `73.1`
*core · concrete actions · source 73*

Jason Barnard says the entity home is the single page where Google reconciles everything it finds about you, and it should be the About page rather than the homepage. His reasoning is a conflict of jobs: the homepage exists to say 'look at us, aren't we wonderful' and then send people onward, so it is a signposting page and never a destination. The entity home has to be the opposite - factual, dry and boring, stating who you are, what you do, who you serve and why you are credible. Trying to do both on one page means fighting yourself over the message. The About page has exactly two audiences: machines trying to understand you, and humans doing due diligence on you. On Kalicube's own homepage there is deliberately little factual company information, just a 'learn more about us' link into the page that carries the facts.

> "the entity home really needs to be on the about page"

**Evidence:** Kalicube's own site: homepage carries audience, offer, reasons to work with them and Trustpilot testimonials, with almost no factual company description; the About page carries the facts plus GDPR information.

**How to do it**

1. Pick the About page on your main website as the entity home and treat every other page as pointing at it.
2. Write the About page to answer four things in plain factual language: who you are, what you do, who you serve, why you are credible.
3. Strip persuasion, adjectives and offers out of the About page; those belong on the homepage and the media kit.
4. Rewrite the homepage as a signposting page: who the audience is, what you offer, why work with you, then links onward.
5. Put one clear 'learn more about us' link from the homepage into the entity home.
6. Add the transparency block to the entity home: legal registration number, VAT number, and a contact address such as a GDPR mailbox.
7. Write a separate media kit page for journalists and hirers, where adjectives and impressiveness are allowed, and accept that it duplicates some About-page facts.
8. Check the first paragraph of each of the three pages and confirm a reader can tell instantly which audience it is written for.

**Pitfall:** Putting the entity facts on the homepage. The homepage's promotional job pulls the wording toward marketing language, and the factual statements get diluted or contradicted, which is exactly the ambiguity that stops a knowledge panel forming.

**Apply at Pabau:** Pabau's About page should become the single canonical entity home: what Pabau is, which practices it serves, where it operates, company registration and VAT numbers, and a contact route. Move promotional framing off it and leave the homepage as the signpost.

**Apply anywhere:** Designate your About page as the entity home and keep it strictly factual: who you are, what you do, who you serve, why you are credible, plus registration details and contact routes. Leave the homepage as a signposting page and put persuasive copy in a separate media kit.
