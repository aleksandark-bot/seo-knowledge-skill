# Digital PR — supporting

31 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. A/B test viral stunt ideas before committing budget  `24.9`
*useful · concrete actions · source 24*

Modeled on Red Bull (DA 93, earning backlinks from top-tier sites through constant viral stunts), the suggested low-cost adaptation for a smaller business with its own social following is to A/B test stunt ideas before spending real money on them: announce a bold idea, put up a simple landing page for it, post about it on social media, and measure how many people visit the page. Only the idea(s) that generate the strongest traffic/engagement signal get fully executed, letting a business validate viral potential cheaply before committing budget — the source notes this specific episode also covers many lower-cost, grassroots sponsorship tactics beyond Red Bull's scale.

> "you can A/B test different viral stunt ideas"

**How to do it**

1. Come up with a bold, attention-grabbing stunt idea related to your brand, scaled to your own budget.
2. Build a simple landing page announcing the stunt before committing resources to actually execute it.
3. Post about the planned stunt on your social media channels, directing followers to the landing page.
4. Measure landing-page visits and engagement (shares, comments, sign-ups) as a proxy for viral potential.
5. Repeat the test across multiple different stunt ideas rather than committing to just one upfront.
6. Only fully execute and invest real budget in the idea(s) that generated the strongest signal.
7. Note this approach assumes you already have some social media following to generate a meaningful read on interest. (inferred prerequisite)

**Pitfall:** Committing budget to execute a viral stunt idea without first cheaply testing audience interest via a landing page and social post.

### 2. Add native sharing so users build backlinks for you  `46.3`
*useful · concrete actions · source 46*

Any SaaS tool or linkable asset should include a built-in share feature that lets users post links back to content hosted on your own domain, because — as Edward puts it — 'your users are building links for you' once that becomes a habit. Travis adds that journalists are people too, scrolling their own LinkedIn and Facebook feeds, so seeing an asset organically shared and commented on by real users signals it's worth citing in an upcoming piece. This is also why strong original statistics/data content on your own domain matters outside active campaigns: journalists Google for stats like anyone else, and whichever domain is already the visible, cited resource — including showing up inside an AI Overview — keeps collecting natural inbound links without any outreach at all.

> "your users are building links for you"

**How to do it**

1. For every calculator, generator, or interactive linkable asset you ship, add a one-click 'share result' feature that generates a unique, indexable URL on your own domain rather than just sharing the homepage.
2. Add direct share-to-social buttons (LinkedIn, X, Facebook) next to each result so sharing takes zero extra steps for the user.
3. Identify the statistics or data questions most commonly searched in your niche via keyword research and make sure you have the single best, most current, most citable page answering each one (inferred).
4. Check whether those pages already appear in Google AI Overviews or get cited by ChatGPT/Perplexity for the relevant queries (inferred).
5. When pitching journalists, lead with the fact that your data page is already a live, cited resource and send the direct URL.
6. Track backlinks originating from shared or user-generated links over a rolling quarter using a backlink tool to quantify this 'free' link acquisition (inferred).

### 3. Amplify a real testimonial via a titled guest post  `40.13`
*useful · concrete actions · source 40*

To seed a specific reputational claim into AI Overview citations, Kasra describes commissioning a guest post on a real, decent-metrics marketing-relevant site, not a random low-quality one, titled directly around the claim - his example: 'Kasra Dash review by Edward Sturm,' amplifying a genuine positive comment Edward had made about him. The post is published under a generic or site-admin byline rather than the brand's own name, since the goal is ranking the long-tail brand-plus-reviewer query, not establishing personal authorship. Kasra reports this got the page cited inside Google AI Overviews, and notes this style of long-tail, two-named-entity query is 'very easy' for a single new page to rank for. He explicitly flags the tactic as 'a little bit gray hat.'

> "another thing you can do to manipulate AI Overviews"

**How to do it**

1. Identify a genuine, strong piece of praise or testimonial your brand has received from a recognizable, relevant person or another brand.
2. Find a real, relevant guest-post or outreach site with decent authority metrics - a genuine marketing or industry site, not a random low-quality site.
3. Pitch or commission a guest post on that site with a title structured as '[Your Brand] review by [Named Person/Brand],' directly naming both parties.
4. Write the post's body around amplifying the specific genuine quote or testimonial rather than inventing new claims.
5. Publish the post under a generic or site-admin byline rather than your own name, since the target ranking query is the brand-plus-reviewer phrase, not a personal authorship claim.
6. Check the brand-plus-reviewer long-tail query in Google AI Overview, ChatGPT, and Perplexity every few weeks to see if the page gets picked up as a citation.
7. Only use genuinely real testimonials and quotes for this, both for editorial integrity and because the tactic is explicitly gray-hat, so treat it as amplification of real praise, not a fabrication method.

**Prompt / template:**

```text
Edward absolutely loves my service, Edward said this about me. / Kasra Dash review by Edward Sturm
```

**Pitfall:** Kasra explicitly labels this 'a little bit gray hat' - it works because a specific brand-plus-named-person query is extremely long-tail and easy to rank a single page for, regardless of whether the underlying claim is genuine, so use it only to amplify real testimonials, not manufacture false ones, to stay within Pabau's editorial standards.

### 4. Automated contact-form submission at scale, and why they keep URLs out of it  `59.17`
*useful · general insights · source 59*

The most abusive channel in their branded-search campaign, and the technical detail in it is genuinely instructive. Jackie describes dusting off GSA - a tool the older generation of SEOs will recognise - whose function is submitting to other sites' contact forms automatically, and reports 70,000 contact-form fills in seven days. The design choice worth noting is that the message contains no URLs at all: it says only to search their brand term to find the business, specifically so that no domain gets blacklisted. That single detail is why the campaign shows up as Search Console impressions rather than referral traffic, and it's the reason their manufactured-branded-search numbers look the way they do. He is upfront that the conversions are zero - 'it's not even about conversions' - the entire point is the search volume and the resulting clickstream. He also volunteers that email is the safer channel for the same message because contact-form submission makes people angry, and he doesn't use a real name or a real email address on the form fills.

> "it spams people's contact forms"

**How to do it**

1. Recognise the signature if you are on the receiving end: high-volume contact-form submissions with no links, no real reply address, and a message instructing the reader to search a brand term.
2. Understand what it is optimising for - Search Console impressions and clickstream, not replies - which is why the messages look pointless and why blocking them by URL filtering doesn't work.
3. Defend your own forms: rate-limit by IP, add a challenge that is expensive for automated submitters, require a verified email before the message reaches a human, and log submissions so patterns are visible.
4. If you are evaluating a supplier who mentions 'form outreach' or 'contact-form marketing', treat it as this, and decline - the operator's own view is that it makes people angry and that email is the safer channel.
5. Run the legitimate version of the underlying idea instead: the owned-channel branded-search play in this collection produces the same Search Console effect through email signatures, job descriptions, podcast CTAs and webinar closes.
6. If you receive these at scale, they are reportable to the platform hosting the sender and, in the UK and EU, to the data-protection regulator, since the submissions process personal data without a lawful basis.

**Pitfall:** Automated bulk submission to third parties' contact forms is unauthorised use of their systems - actionable under the Computer Fraud and Abuse Act in the US and the Computer Misuse Act in the UK, alongside UK GDPR and PECR exposure for the unsolicited messages - and the deliberate omission of URLs is abuse-detection evasion rather than a technical nicety. Documented here as a mechanism and a defence, not a build guide.

**Apply at Pabau:** Two takeaways for Pabau: harden the site's own contact forms against this pattern, and note that every legitimate channel in the branded-search play - signatures, job posts, podcast and webinar CTAs - produces the same Search Console effect without the exposure.

**Apply anywhere:** Two takeaways: harden your own contact forms against this pattern, and note that every legitimate channel in the branded-search play - signatures, job posts, podcast and webinar CTAs - produces the same Search Console effect without the exposure.

### 5. Build the outreach email from angle, audience, credibility and one simple ask  `162.6`
*useful · concrete actions · source 162*

Peralta's email template has four fixed parts. It leads with the unique angle he found, then references any interview, article or podcast of theirs he came across, which proves the research. It names who the audience for the piece will be, since that is the exposure the expert is buying with their hour. It adds credibility boosters such as blog traffic figures or the names of other well-known experts already interviewed for the blog. It closes with one simple ask plus a note that he does the heavy lifting on creating and promoting the piece. He is explicit that a new or unknown blog should drop the credibility boosters rather than fake them, and just explain what the company does instead.

> "Credibility boosters (such as impressive blog stats"

**Evidence:** Peralta uses this structure across the outreach that produced a 60% positive response rate, including the CEO of Buffer.

**How to do it**

1. Open the email with the unique angle in the first sentence, before any introduction of yourself.
2. Reference a specific interview, article or podcast of theirs you actually read or heard.
3. Name the audience the piece is written for, in terms of who they are and what they do.
4. Add one credibility booster: a blog traffic number, a client name, or two experts you have already interviewed.
5. Make one ask only, with a concrete time commitment such as a 45-minute call.
6. Add a line saying you will handle writing, editing and promotion.
7. If the blog is new, delete the credibility line and describe what your company does instead of inflating numbers.
8. Track opens so you know which follow-up branch to use next.

**Tools:** Mixmax

**Pitfall:** Stacking multiple asks (interview, plus a quote, plus a share) into one email. It raises the perceived cost and the reply rate drops; a single ask with a stated duration converts better.

**Apply at Pabau:** Pabau's outreach emails should lead with a specific angle about the clinician's own practice and cite Pabau blog readership plus previously interviewed practitioners, and should drop credibility stats entirely for any new template or code-reference series.

**Apply anywhere:** Structure every outreach email as angle, proof you did research, the audience they reach, one credibility booster, and a single ask with a stated time commitment.

### 6. Check posting frequency before choosing Twitter over email for outreach  `162.5`
*useful · concrete actions · source 162*

Peralta opens on Twitter because people respond quickly and a tweet costs almost no effort to send. His qualifying rule is posting frequency: if the target posts roughly once a day or every few days, Twitter is the right first channel; if they post once a week or less, skip it and go straight to email or LinkedIn. He sends the message using the 'Tweet to' button from their profile and includes the unique angle in the message itself. If the pitch needs more than one tweet, he replies to his own first tweet so the target sees the continuation. Benji adds two reasons the channel works: a tweet is a lighter, less intrusive ask than an email, and the ask is public, which he believes raises the response rate.

> "posting regularly once a day or every few days"

**Evidence:** Peralta landed an interview with Hotjar founder David Darmanin from a tweet; that article ran on Codementor's blog and drew over 6,800 pageviews in under two weeks.

**How to do it**

1. Google the expert's name plus Twitter to find the account.
2. Check the profile's recent posting frequency before writing anything.
3. If they post daily or every few days, use Twitter first; if weekly or less, skip to email or LinkedIn.
4. Use the 'Tweet to' button on their profile and put the unique angle inside the message.
5. If the pitch runs over the character limit, reply to your own tweet so the thread stays visible to them.
6. Wait 3-4 days for a reply before moving to the email step.

**Tools:** Twitter

**Pitfall:** Tweeting at someone who logs in monthly. The message is never seen, you burn 3-4 days waiting, and you conclude the tactic does not work.

**Apply at Pabau:** For Pabau, apply the same frequency test to Instagram and LinkedIn, where aesthetic practitioners are actually active, and only fall back to email for people whose social accounts are dormant.

**Apply anywhere:** Check how often the target actually posts before choosing a social channel for outreach, and go straight to email for anyone posting weekly or less.

### 7. Do original reporting from first-hand sources  `66.21`
*useful · concrete actions · source 66*

Content built on original reporting: interviews, event access, documents, observation or specialist analysis. Its role is to explain what happened and why using first-hand sources — not to summarize another publisher's report, and not to turn a dataset into a market benchmark, which is the original-research type's job. It covers interviews, event coverage, investigations, expert analysis and behind-the-scenes reporting supported by first-hand sources or media. It scores High on click resilience, brand mention potential and proprietary advantage at High effort, with Medium citation potential and Medium business value. The score profile makes the trade explicit: this is expensive, converts indirectly, and is bought mainly for entity association — being the brand that gets named when the topic comes up. Its direct opposite sits in the deprioritized list as third-party news rewrites, and the only structural difference is whether a first-hand source was obtained. Access is the moat, not the writing.

> "This content is original reporting: interviews, event access, documents, observation or specialist analysis"

**How to do it**

1. Pick a development in your category where you have access no one else has: a person, an event, a document, or a vantage point.
2. Secure the first-hand source before planning the piece, since without it the output is a rewrite regardless of effort.
3. For interviews, prepare questions that only this person can answer, and record and transcribe so you can quote precisely.
4. For events, report what you observed rather than what the programme said, and capture your own media.
5. For documents, publish or excerpt the source alongside your reading of it, so the analysis can be checked.
6. Add the specialist layer: what this means for your specific audience, informed by expertise a generalist publication lacks.
7. Attribute every claim to its source, and distinguish clearly between what a source said, what you observed, and what you conclude.
8. Publish supporting media — photographs, recordings, screenshots, the document itself — since first-hand material is what makes the piece hard to reproduce.
9. Timestamp it and update it as the story develops, rather than leaving a superseded account standing.
10. Distribute it to the people covering the same beat, since the brand-mention return depends on other publishers picking it up.

**Pitfall:** Publishing without a genuine first-hand source. Analysis layered on someone else's reporting is the deprioritized press-release-rewrite type at reporting cost — High effort with the Low scores of the rewrite, the worst trade in the worksheet.

**Apply at Pabau:** For Pabau this means access, not commentary: interviews with practice owners and regulators, first-hand coverage of industry events, and reading of regulatory documents as they land. A post reacting to someone else's news story is the deprioritized rewrite type, whatever analysis is added on top.

**Apply anywhere:** This means access, not commentary: interviews with operators and regulators, first-hand coverage of industry events, and reading of regulatory documents as they land. A post reacting to someone else's news story is the deprioritized rewrite type, whatever analysis is added on top.

### 8. Find 90-95% of expert emails by stacking Voila Norbert and Email Hunter  `162.11`
*useful · concrete actions · source 162*

Peralta does outreach on Twitter and by email, so those are the only two contact details he hunts. For Twitter and LinkedIn, he simply googles the expert's name plus the platform name. For email, he uses a combination of Voila Norbert and Email Hunter, and says the pair gets him 90-95% of the addresses he needs. The point of stacking two finders rather than one is coverage: each tool misses different domains, so running the residue of one through the other closes most of the gap. He records everything in a plain spreadsheet alongside the target list, which is what makes the multi-step follow-up sequence trackable later.

> "a combination of Voila Norbert and Email Hunter"

**Evidence:** Peralta says the two tools together return 90-95% of the emails he looks for.

**How to do it**

1. Google the expert's name plus 'Twitter' to get the handle, and the name plus 'LinkedIn' for the profile.
2. Run the name and company domain through Voila Norbert first.
3. Run every target Voila Norbert failed on through Email Hunter.
4. For the remaining 5-10%, fall back to the company's generic press or marketing address and ask for a forward.
5. Paste handles and addresses into the same spreadsheet row as the target and their angle.
6. Add columns for outreach stage, date sent and open count so follow-ups are driven by the sheet.

**Tools:** Voila Norbert, Email Hunter, Google Sheets

**Pitfall:** Guessing address patterns instead of verifying. Bounces damage sending reputation and, worse, they look like non-opens in your tracker so you follow up on a prospect who never received anything.

**Apply at Pabau:** Pabau's outreach sheet should carry a verified-email column, since aesthetic clinics often use shared info@ addresses and a bounce is indistinguishable from a clinician ignoring you.

**Apply anywhere:** Stack two email-finding tools rather than relying on one, verify before sending, and store handles and addresses in the same tracking sheet as the outreach stage.

### 9. Host a niche podcast as a remote networking substitute  `24.11`
*useful · concrete actions · source 24*

For industries with relevant in-person events, the recommended path is to attend them specifically to network and identify partners, since the resulting relationships generate users, industry allies, press, and eventually backlinks — described as "the best backlinks." For anyone not located near such events (a remote city or town), the substitute is to host your own industry-focused podcast and invite people from the industry on as guests, which builds the same relationship dynamic remotely; the host runs his own show this way (three to seven SEO guests weekly) and has published a companion workflow article, "How I Produce Guest Podcasts in 90 Minutes That Helped Me Rank in Google," describing the exact process.

> "you can also host a podcast with people in your industry"

**How to do it**

1. If your industry has relevant in-person events, attend them specifically to network and identify potential partners.
2. Use those relationships to generate users, industry allies, press opportunities, and backlinks over time.
3. If you're not located near relevant industry events, start your own podcast focused on your industry instead.
4. Invite people from your industry on as guests to build the same relationship dynamic remotely.
5. Use the resulting relationships the same way as event-based networking: for users, allies, press mentions, and backlinks from guests' own sites/networks.
6. Reference the source's own workflow article ("How I Produce Guest Podcasts in 90 Minutes That Helped Me Rank in Google") for the exact operational process. (inferred)

**Pitfall:** Assuming you must be near physical industry events to build these relationships — hosting your own niche podcast is framed as a fully viable substitute for anyone in a remote location.

### 10. Ignore universal most-cited-domain lists and derive your own  `86.9`
*useful · best practices · source 86*

Grow & Convert push back on the common advice to chase mentions on Reddit, Wikipedia and Forbes because infographics show those as the top-cited domains for AI. Their objection is that such a list assumes one universal set of most-cited sites applies to every business, and there is no such set. When someone asks for the best dispatch software for trucking companies, the model searches for that query and cites whatever is most relevant to it, which will be sites that review trucking software rather than a random Reddit thread. Their own research found that for product-related queries LLMs cite industry-specific sites 86% of the time and generic sites like Reddit only 16% of the time. The operational consequence is that your off-site target list is derived per query, from the engines themselves, not copied from a published chart.

> "there's a universal list of most-cited sites that applies to all businesses"

**Evidence:** Grow & Convert's citation research: for product-related queries, LLMs cite industry-specific sites 86% of the time versus generic sites like Reddit 16% of the time.

**How to do it**

1. Take the bottom-of-funnel keywords from your Tier 1 list and phrase each as a natural prompt.
2. Run each prompt in ChatGPT, Perplexity and Google AI Overviews and record every cited domain.
3. Count how often each domain appears across your prompt set and rank by frequency, not by domain authority.
4. Cut generic mega-domains from the list unless they actually appeared for your prompts.
5. Pitch the top-ranked industry sites for inclusion in an existing listicle, an expert quote, or a guest post.
6. Re-run the prompt set quarterly, since the cited set shifts as those sites' own rankings move.

**Tools:** ChatGPT, Perplexity, Traqer

**Prompt / template:**

```text
what are the best dispatch software options for trucking companies
```

**Pitfall:** Chasing Reddit and Forbes burns a PR budget on domains that never get cited for your category's prompts, and the effort is invisible in AI mention rate.

**Apply at Pabau:** Pabau's outreach list should be built by prompting the engines for aesthetic and medspa software questions and recording who gets cited. Aesthetic-industry publications and clinic-software review sites will outrank Reddit or Forbes placements every time.

**Apply anywhere:** Build your outreach list by prompting the engines with your category's product questions and recording who gets cited. Industry publications and category review sites will beat Reddit or Forbes placements.

### 11. Industry trust converts into partner-led distribution during a market shock  `168.10`
*useful · general insights · source 168*

CPC Strategy's webinar program started because Google needed help. In late 2012 Google turned Froogle, a free comparison shopping channel retailers had relied on for a decade, into a pay-to-play product with 90 days notice. The change caused widespread panic, and Google needed someone to educate the market. It approached CPC Strategy, whose first webinar explained how the new paid product worked. The mechanism worth noting is that the agency did not pitch for this. It had spent years being the trusted news and data source for exactly that audience, and when the platform needed a credible educator the shortlist was short. Platform disruptions create a distribution opportunity for whoever already holds the audience's trust, and that position has to exist before the shock.

> "Google reached out to Nii and his co-founders"

**Evidence:** Google gave the market 90 days notice when converting Froogle to a paid product in late 2012, then approached CPC Strategy to help educate retailers; that became the agency's first webinar.

**How to do it**

1. Establish the news and data position in your niche before any shock, since it cannot be built inside a 90-day window.
2. Monitor the platforms your audience depends on for deprecation notices, pricing changes and policy shifts.
3. When a shock lands, publish the plain explanation within days, before the platform's own guidance is clear.
4. Contact the platform's partner or developer relations team offering to run the education session for the affected segment.
5. Frame the offer as reducing their support load, not as a co-marketing ask.
6. Run the session with the platform's own person on it, which is what makes it the definitive version.
7. Convert the recording into an evergreen guide that continues to rank after the shock passes.

**Pitfall:** Approaching a platform for co-marketing before you hold audience trust reads as a vendor pitch and gets routed to partner sales. The position has to be earned in advance.

**Apply at Pabau:** Pabau should build the trusted-explainer position for the platforms aesthetic practices depend on, such as payment processors, booking channels and regulators. When one changes its rules, Pabau publishes first and offers the vendor a joint session.

**Apply anywhere:** Build the trusted news position in your niche before a platform shock, publish the plain explanation within days when one lands, then offer the platform's partner team a joint education session framed as reducing their support burden.

### 12. Launch linkable assets on Product Hunt, Betalist, and to journalists  `48.5`
*useful · concrete actions · source 48*

For getting initial visibility on a newly built linkable asset, the recommended launch channels are Product Hunt and Betalist, described as a very similar app/software/hardware-sharing platform to Product Hunt, both used across the episode's own case studies since sleepyti.me and donothingfor2minutes.com were each launched on Product Hunt. Beyond those launch platforms, the second distribution channel is direct outreach to journalists who have previously covered your niche or similar products, using a separate referenced resource, an article and prompt series described as "The AI system to find relevant journalists, land coverage, and earn ongoing high authority backlinks," which generates story ideas, finds journalists who'd care about those stories, locates their contact information, and drafts the pitches, all as a chained series of prompts that can be adapted to any specific linkable asset by handing the asset to ChatGPT along with those prompts.

> "launch them on Product Hunt, launch them on Betalist"

**How to do it**

1. Finish building the linkable asset (see the vibe-coding and build steps referenced elsewhere).
2. Create a launch listing for the asset on Product Hunt.
3. Create a second launch listing for the asset on Betalist.
4. Separately, compile a list of journalists and bloggers who have previously written about your niche or about similar tools and products.
5. Retrieve the referenced journalist-outreach prompt series, "The AI system to find relevant journalists, land coverage, and earn ongoing high authority backlinks," and feed your linkable asset into ChatGPT along with those prompts, asking it to adapt them to your specific asset.
6. Use the AI-generated story ideas, journalist matches, contact details, and drafted pitches to send personalized outreach to each identified journalist.
7. Track which launch channel and which journalist pitches actually generate coverage or backlinks, to refine future launches (inferred tracking step).

**Tools:** ChatGPT, Product Hunt, Betalist

### 13. Original frameworks earn praise and speaking slots without design budget  `100.18`
*useful · content insights · source 100*

Grow and Convert use their own Customer Content Fit post as a medium-originality example and stress what it is not. It is 2,442 words, which they call not that long, with no fancy design and mostly text. The originality is what earned it praise, and Benji was invited to run a workshop on the framework, evidenced by a public invitation from Claire Suellentrop for the Forget The Funnel series. Their description of the process is the useful part: the hard part was realizing they had stumbled on an original way of thinking about content marketing, and the easier part was writing it up clearly. This is an argument against treating design and length as the drivers of distribution. A named framework that solves a real problem travels on its own, and the naming is what makes it citable and repeatable by other people.

> "It's not that long (2442 words). No fancy design"

**Evidence:** Customer Content Fit: 2,442 words, mostly plain text, no custom design, and it earned public praise plus a Forget The Funnel workshop invitation for Benji Hyam.

**Pitfall:** Naming a framework that just relabels common practice gets ignored and can invite mockery. The signal is that you cannot explain how it differs from an existing named framework.

**Apply at Pabau:** If Pabau develops a repeatable method for aesthetic practices, such as a rebooking or no-show reduction system, name it and write it up plainly. That page becomes the thing partners and podcasts cite, without needing a design budget.

**Apply anywhere:** When you find a genuinely original way of working, name it and write it up in plain text. The naming is what makes it citable; design and length are not what carry it.

### 14. Personalize every journalist pitch to their specific beat  `46.4`
*useful · best practices · source 46*

Cookie-cutter, templated outreach emails to journalists actively burn your sender reputation and get flagged as spam, per both Edward and Travis. Travis emphasizes that a journalist's inbox is even more saturated with pitches than a typical LinkedIn inbox — 'for a journalist, it's that times 10, because their job is literally to be pitched ideas' — so the pitch has to reference specifically what that individual journalist already writes about and how your story piggybacks on their existing beat. He stresses this compounds over time: the digital PR agencies that win consistently are the ones with real, maintained relationships with specific journalists, to the point they can call up their friends directly rather than cold-pitching every time.

> "understand what does that individual journalist talk about"

**How to do it**

1. Before pitching any journalist, pull their last 10-15 published articles via the publication's site or a media database to identify their specific beat and recurring themes (inferred).
2. Write a custom opening line in every pitch email that references a specific recent piece they wrote and explains why your story or data is a natural follow-up.
3. Never send the same subject line or body copy to more than one journalist without at least one personalized paragraph per recipient.
4. Maintain a running spreadsheet or CRM of journalist relationships noting what they cover, past interactions, and outcomes, so future pitches build on history.
5. Prioritize warm relationship-building, such as occasional non-pitch check-ins or sharing their work, over transactional one-off asks.
6. Segment your journalist list by beat, region, or vertical before a campaign so each pitch batch matches the specific data cut relevant to them.

**Pitfall:** Sending cookie-cutter templated pitch emails gets you sent to spam, and even when a journalist does read it, an obviously generic pitch makes them hate you and your brand — genuine personalization is non-negotiable.

### 15. Pick the influencer whose audience matches your buyer job title  `123.9`
*useful · best practices · source 123*

Hyam's selection reasoning for the Vistage launch is precise, and it is not about reach alone. Chris Brogan had over 100,000 engaged Twitter followers, which mattered, but the deciding factor was that he worked in the management coaching space and therefore had the exact audience Vistage was trying to attract for membership: CEOs and executives of large companies. Hyam also notes why the influencer route is efficient. It clears both steps of the launch strategy at once, because an influencer's articles are almost by definition unique and hard to replicate, and the influencer's existing audience is the strategic promotion. The audience-overlap test is what makes the borrowed audience worth borrowing.

> "had the exact same audience that we were trying to attract"

**Evidence:** Brogan's audience of CEOs and executives matched Vistage's membership target, and his first post drove over 3,000 visitors on day one, seeding a year of growth to 20,000 monthly visitors.

**How to do it**

1. Write down the job title and seniority of the buyer you want, not the topic.
2. Shortlist influencers who serve that job title professionally, for example coaches and consultants who sell to them.
3. Check the audience claim rather than the follower count: look at who replies, who they are quoted by, and whether their own content ranks.
4. Discard the largest accounts in your industry if their followers are peers rather than buyers.
5. Confirm the influencer has an owned channel, an email list or a newsletter, not only social followers.
6. Make the approach with a specific non-cash offer and a defined deliverable.
7. Judge the result on email signups from their audience, not on the traffic spike.

**Pitfall:** Buying reach that is mostly your own peers. The post gets shares from other marketers or other vendors, the traffic spikes for a day, and no buyer enters the list.

**Apply at Pabau:** For Pabau the right partner is a consultant or trainer who sells to clinic owners and aesthetic practitioners, not the biggest aesthetics account on Instagram. Check that the person has an email list before offering anything.

**Apply anywhere:** Choose an influencer by whether their audience is the job title you sell to, verify it from replies and citations rather than follower count, insist they have an owned email channel, and judge the collaboration on signups rather than on the traffic spike.

### 16. Pilot-test pitches on real people before mass-sending  `33.6`
*useful · best practices · source 33*

After noticing poor response rates, the guest developed a testing habit: send a new pitch draft first to a small group of real, uninvolved people (his own method — literally family members) to see whether a jaded reader who's seen years of spammy emails still finds it interesting enough to open. Subject lines are kept to roughly five to seven words, and the finished pitch is never blasted to the full media list at once — it's broken into small tranches so open rates and link-clicks can be measured and the copy tweaked before scaling to the rest of the list. This is offered as the antidote to the generic three-paragraph AI-pitch pattern (flattering opener, pitch ask, vague closer) that the host says he receives constantly and immediately recognizes as fake.

> "we would send it off to my aunts and uncles"

**How to do it**

1. Before sending a new pitch template to the full media list, send it first to a small trusted group of real people uninvolved in the campaign to gauge whether it reads as genuinely interesting or as spam.
2. Treat a skeptical test reader's willingness to open and engage as a signal the pitch is strong enough to test more broadly.
3. Keep subject lines to roughly five to seven words.
4. Break the media list into small tranches instead of sending to everyone at once.
5. Send to one tranche, measure open rate and link-click rate, then tweak subject line or copy based on results.
6. Send the improved version to the next tranche and repeat until performance is acceptable before rolling out to the remaining list.
7. Avoid the generic three-paragraph AI-pitch pattern (flattering opener about the show/article, then the ask, then a vague closing paragraph), which experienced recipients say they recognize immediately.

**Tools:** BuzzStream

**Pitfall:** Sending the same untested generic template to an entire media list at once, and defaulting to the recognizable "I listened to this episode, it was so insightful" three-paragraph AI-pitch format that experienced recipients say they can spot and ignore instantly.

### 17. Pitch experts on publicity and a link, not on doing you a favor  `162.4`
*useful · best practices · source 162*

Peralta answers the standard objection, 'what is in it for the expert', with two reasons. First, experts genuinely like sharing their advice and experience when the framing is unique and interesting. Second, they get publicity for their company, a link to their site, and some brand building, because your audience should be close to the same audience they want to reach. He notes that the unique angle is what makes both reasons work: it gives them something they have not said before, it shines a positive light on their company and staff, and it signals that the interview will be worth their hour because you clearly did the research. Devesh adds a corroborating detail: one contact mentioned running the interview past their PR team, which confirms the publicity motive is real.

> "They actually like sharing their advice and experience"

**Evidence:** An Amplitude contact referred to running the request by the PR team, which Devesh flags as direct confirmation of the publicity motive.

**How to do it**

1. State in the pitch who the audience for the article will be, in the words the expert would use for their own prospects.
2. Name the specific angle so the expert can see it is not a question they have already answered publicly.
3. Say plainly that they will get a link to their site and coverage of their company.
4. Point out that the angle puts their company and their staff in a positive light.
5. Add that you will do the heavy lifting on writing and promoting the piece.
6. Expect the request to be forwarded to a PR or comms team, and keep the email forwardable: short, specific, no attachments.

**Pitfall:** Framing the ask as a favor or as 'picking your brain'. It reads as an unpaid hour with no return and gets ignored, especially by anyone with a PR team.

**Apply at Pabau:** When Pabau pitches a clinic owner for an article, spell out the audience (other aesthetic practice owners), the link back to their clinic site and the promotion Pabau will do, since that is what gets past a clinic's marketing manager.

**Apply anywhere:** Make the return explicit in every expert pitch: the audience they get exposure to, the link back to their site, and the fact you handle the writing and promotion.

### 18. Pitch your proprietary dataset to journalists in a niche with no other source  `168.4`
*useful · concrete actions · source 168*

After SEO, public relations was CPC Strategy's second traffic tactic, and Nii Ahene explains why it converted at an unusual rate. There were very few reliable sources offering the kind of data the agency held, so eCommerce journalists and bloggers had almost no alternative when they needed a number about comparison-shopping engines. The pitch worked because of scarcity, not because of craft. The order matters: build the proprietary dataset first, then pitch it. Pitching before you have a number nobody else has puts you in the same queue as everyone else. The narrower the niche, the more this works, because the pool of citable sources is smaller and a journalist covering the beat will keep coming back.

> "it wasn't hard to get eCommerce journalists and bloggers to bite"

**Evidence:** Nii Ahene says few reliable sources offered CPC Strategy's kind of data, which made journalist and blogger pitches easy to land.

**How to do it**

1. Build the proprietary dataset first, before writing a single pitch, so the pitch has a number attached.
2. Search your niche for the phrases journalists would need a statistic for and note who currently gets cited, if anyone.
3. Build a list of the 20 to 40 reporters and bloggers who cover that exact beat, not general business press.
4. Pitch a single specific figure from your report with the methodology in one line, not the whole report.
5. Offer the underlying data and an interview with the analyst who ran it, since that is what a general PR pitch cannot offer.
6. Add every reporter who uses your number to a list and send them each new edition of the report before publication.
7. Track which cited figures earn links and build the next report around those dimensions.

**Pitfall:** Pitching a data story into a crowded niche where five vendors already publish benchmarks produces silence. Check who currently gets cited before investing in the dataset.

**Apply at Pabau:** Aesthetic practice operations data is thinly covered in trade press. Once Pabau has an anonymized benchmark report, pitching single figures to aesthetic and medspa trade publications should convert far better than generic product pitches.

**Apply anywhere:** Build the proprietary dataset before you pitch, then check who currently gets cited in your niche. If the answer is nobody, pitch single figures with the methodology to the reporters on that exact beat.

### 19. Rank third-party mention targets by citation frequency, not domain authority  `84.17`
*useful · concrete actions · source 84*

The prospecting rule Grow & Convert set is that the domains worth earning a mention on are the ones the models actually list as sources for the prompts you care about, and nothing else. They accept that any mention in a reputable publication helps overall brand marketing, but separate that from AI search visibility, which is prompt-specific. Their sequence is start with the prompts and topics that matter, then look at which sites are cited for those prompts, then aim to get mentioned there. Ranked by citation frequency, that list will often put a small trade publication above a large mainstream outlet, which inverts the usual authority-metric prospecting order. In the Toro TMS data a single trade title, Transport Topics, was the only non-vendor source in the top-cited set.

> "you should focus on getting brand mentions on the domains that are actually cited"

**Evidence:** In Toro TMS topics, the only non-vendor domain in the top-cited set was the trade publication Transport Topics, about 5% of citations.

**How to do it**

1. Take your logged citation set and strip out your own domain and direct competitors.
2. Count how many of your priority prompts each remaining domain appears in.
3. Sort by that prompt coverage count, not by Domain Rating or traffic.
4. Split the list into publications you can pitch and comparison pages you can request inclusion on.
5. Pitch the top ten by coverage count first, regardless of how small the site is.
6. Keep a separate, smaller budget line for mainstream press as brand marketing rather than GEO.
7. After placements go live, re-run the prompt basket to confirm the mention is being picked up.

**Tools:** Traqer

**Pitfall:** Prospecting by authority metric in a niche vertical sends budget to large outlets that are never in the retrieval set for your prompts.

**Apply at Pabau:** For Pabau, an aesthetic-industry trade site that gets cited for clinic software prompts is worth more than a high-authority general business title that never appears.

**Apply anywhere:** Rank mention targets by how many of your priority prompts cite them, not by authority metrics. A small trade title in the retrieval set beats a large outlet that is never cited.

### 20. Rotate warm-up services before cold-emailing journalists  `33.5`
*useful · concrete actions · source 33*

Outreach is sent from a dedicated branded domain rather than the client's, since a client's domain would take too long to warm up and clients are rarely willing to grant email access. The domain is warmed using services like Warmy or Mailtoaster (a self-built attempt using GMass reportedly "didn't work out well"), rotating to a different provider roughly monthly because each warm-up service cycles through a limited, repeating pool of seed inboxes over time. Warm-up needs real opens, replies, and occasional flags across many inboxes spanning multiple providers (Gmail, Outlook, Yahoo, company domains) and IPs, ramping naturally from 0-2 emails/day to roughly 30-40/day by the end of a month; separately, real contacts are asked to check whether test sends land in the primary inbox or spam/promotions and to manually correct placement for a few weeks before a real campaign goes out. Bounced addresses are auto-blacklisted, and if two or more addresses on the same domain bounce, that whole domain is dropped from future targeting to protect sender reputation.

> "I personally use Warmy, and there's Mailtoaster"

**How to do it**

1. Set up a dedicated branded sending domain rather than using the client's domain.
2. Sign up for an email warm-up service such as Warmy or Mailtoaster rather than attempting to self-build warm-up with a generic tool like GMass.
3. Use one warm-up service for about a month, then switch providers, rotating through a third, because each service tends to cycle through the same limited pool of seed inboxes.
4. Confirm the warm-up is generating real opens, replies, and occasional flags across a large number of inboxes, not just raw volume.
5. Ensure warm-up activity spans multiple providers (Gmail, Outlook, Yahoo, company domains) and IP addresses, not one inbox type.
6. Separately run a manual placement test: send to real contacts and ask them to check primary-inbox vs. spam/promotions placement, manually correcting it for a few weeks before the first real send.
7. Let sending volume ramp naturally from roughly 0-2 emails/day to about 30-40/day by month's end before scaling further.
8. Auto-blacklist bounced addresses, and stop targeting an entire domain if two or more of its addresses come back as undelivered.

**Tools:** Warmy, Mailtoaster, GMass

**Pitfall:** Trying to fully self-build warm-up with a single tool like GMass instead of rotating multiple dedicated warm-up services — the source tried this and "it also didn't work out well."

### 21. Scale into an 'SEO-informed media company': PR hire, retargeting, linkable assets  `42.7`
*useful · concrete actions · source 42*

Once the core SEO cycle is producing results, the recommended next stage is to hire a dedicated person to run press and PR. Stay active on social media specifically to build branded search volume, which makes even your less-relevant, lower-value backlinks look better to Google because they're paired with real brand signal. Retarget your organic visitors with paid media, since people already arriving via qualified organic searches are your most pre-qualified retargeting audience. On top of that, use a newsletter, podcast, or YouTube channel specifically to promote "linkable assets" in order to earn more backlinks, deliberately diversifying marketing channels so the business doesn't depend on SEO alone, while every one of those channels still ultimately reinforces the SEO foundation.

> "hire a dedicated person to do different types of press"

**How to do it**

1. Once your SEO cycle is consistently producing ranking pages, hire or assign a dedicated person to run ongoing press and PR outreach rather than treating it as an occasional project.
2. Increase posting cadence and consistency on social media specifically to grow branded search volume, tracking brand-name search volume as a KPI, for example in GSC or a rank tracker.
3. Set up a retargeting pixel or audience specifically for visitors who arrived via organic search, since they've already shown qualified interest.
4. Build paid retargeting campaigns aimed at that organic-visitor audience rather than a cold audience (inferred campaign-structure detail).
5. Identify or create at least one "linkable asset," such as a tool, study, or template, worth actively promoting rather than just publishing normal articles.
6. Use a newsletter, podcast, or YouTube channel as the specific promotion vehicle to get that linkable asset in front of people likely to link to it.
7. Track which channel, press, social, retargeting, or newsletter/podcast/YouTube promotion, is actually converting into new links or branded searches, and double down on whichever is working (inferred measurement/prioritization step).

### 22. Send 100 handwritten cold emails rather than thousands of templated ones  `173.2`
*useful · best practices · source 173*

Dane's explicit contrast is volume versus custom. He sent roughly 100 cold emails in the first month, all written and sent manually, and describes staying up until 3AM finding contacts. He was not automating sequences or buying lists. Grow and Convert calculate a 3% deal rate from those 100 emails, which they attribute to the quality of the advice inside rather than any subject-line trick. Dane's own summary of the whole strategy, two years and $300,000 a month later, is 'Be more personal. Be more custom. But above all else, start doing.' The relevant threshold for anyone starting is that 100 genuinely researched emails is a month of work, and it is enough to replace a salary if the research is real.

> "he sent about 100 of these custom cold sales emails"

**Evidence:** 100 emails, 3 deals, first month of KlientBoost, 2015.

**How to do it**

1. Set a target of 100 researched prospects, not 1,000 addresses.
2. Budget 20 to 40 minutes per email for research plus writing, and schedule that time explicitly.
3. Ban merge fields beyond the first name; every email must contain a detail that could only apply to that company.
4. Send from a personal address with your real name, not a marketing subdomain.
5. Log each send with the specific observation you made, so you can review which observation types drew replies.
6. Review after 25 sends and rewrite the approach if reply rate is under 10%.
7. Keep sending manually until you have paying clients; only consider automation once the manual version converts.

**Pitfall:** Founders skip to automation because 100 manual emails feels slow, then read the resulting 0.2% reply rate as proof cold email does not work for their market.

**Apply at Pabau:** If Pabau runs founder-led or partnership outreach to practice groups, David should measure it on deals per 100 researched emails, not on sends. A hundred well-researched practices beats a list buy, and the research notes feed the sales team's discovery calls.

**Apply anywhere:** Treat cold outreach as a research task with a hundred-prospect budget rather than a volume channel. Manual sends with one genuinely specific observation each outperform automated sequences at a fraction of the list size.

### 23. Send a personal email to newsletter operators, not just social influencers  `172.8`
*useful · concrete actions · source 172*

Alongside the influencer route, Benji Hyam names a third distribution path: send the piece to the influencer yourself, in a carefully written personal email. He did this with Hiten Shah, who ended up sharing the post in his newsletter, and that single share drove over 1,000 people to the article. Hyam's condition is that the email has to be personal and take time to write, which is the same standard he applies to the asset itself. The newsletter angle matters because a newsletter share is an owned-audience recommendation rather than a social post that decays in an hour, and the traffic tends to arrive from readers who trust the sender. This is the fallback when no warm intermediary exists.

> "take the time to craft a personal email"

**Evidence:** Hiten Shah shared Hyam's post in his newsletter and it drove over 1,000 people to that article alone.

**How to do it**

1. List the newsletters your buyers actually read, including individual operators rather than only brand newsletters.
2. Subscribe and read three recent issues to learn what each one links to and in what format.
3. Write one email per target that references a specific item they linked recently and explains why your piece fits that slot.
4. Keep the ask to one line: a look, not a demand for a share.
5. Link directly to the asset with no gate, form or tracking clutter.
6. Send from a named person, and time it a few days before their usual send day.
7. Measure referral traffic from each newsletter separately so you know which operators are worth a relationship.
8. Follow up once, three to four days later, with a different subject line and nothing else added.

**Pitfall:** Sending a templated note to a newsletter operator. They read pitches all week and a generic email gets deleted, which costs you the one channel where a single share can send four figures of traffic.

**Apply at Pabau:** Pabau should keep a short list of aesthetics and medspa newsletters, and send each a personal note when a genuinely useful template or data piece publishes, tracking referral traffic per newsletter in GA4.

**Apply anywhere:** Build a list of newsletters your buyers read, subscribe and study what they link, then send each operator a personal email referencing a recent item and explaining the fit. Track referral traffic per newsletter so you know which relationships to keep.

### 24. Send a short apologetic reminder 4-5 days after an opened but ignored email  `162.8`
*useful · concrete actions · source 162*

This is the second follow-up branch. If the expert did open the first email but did not reply, Peralta waits 4-5 days, longer than the 3-4 days he waits on non-opens, and sends a short polite reminder that opens along the lines of 'I'm sure you've got a lot on your plate'. He landed an interview with Asana's Head of Customer Journey this way. The useful detail is what the reply produced: he had originally contacted Asana's Head of Product Management, and after the follow-up she recommended Michael Nguyen instead, who turned out to be the right person. So a follow-up on an opened email often returns a referral rather than a yes, and the referral is frequently the better interview. That article drew over 3,400 pageviews in just under four weeks.

> "wait 4-5 days and send a polite"

**Evidence:** An opened-but-unanswered email to Asana's Head of Product Management produced a referral to Michael Nguyen; the resulting article got over 3,400 pageviews in under four weeks.

**How to do it**

1. Confirm from your tracker that the email was opened but not answered.
2. Wait 4-5 days, longer than you would wait on an unopened email.
3. Reply in the same thread so the original angle is visible underneath.
4. Open by acknowledging their workload rather than restating the ask.
5. Restate the angle in one sentence and repeat the single ask.
6. Add a line inviting them to point you to a better-placed colleague if they are not the right person.
7. Treat any referral as a fresh prospect and restart the sequence with a warm mention of who sent you.

**Pitfall:** Following up with the same person repeatedly instead of offering the referral exit. You lose the colleague who would have said yes, and the original contact stops opening your mail.

**Apply at Pabau:** When a Pabau outreach email is opened but ignored, follow up once at 4-5 days and explicitly offer the referral exit, since a clinic manager will often hand you the practice owner or lead injector who is the better source anyway.

**Apply anywhere:** When an outreach email is opened but not answered, wait 4-5 days, reply in-thread, and explicitly invite a referral to a better-placed colleague.

### 25. Summarize an influencer's long video series into posts, then send them  `172.3`
*useful · concrete actions · source 172*

Benji Hyam ran this at ThinkApps. YCombinator published How to Start a Startup, a 20-lecture video series featuring well-known Silicon Valley figures, with each video running about an hour. His team had writers watch the videos and summarize each lecture into a blog post. They then sent each post to the person who taught that lecture, and shared with YC via Twitter and HackerNews. The speakers often shared the write-up with their own audience. The mechanism is that a summary is a genuine service to a busy audience and flattering to the speaker, so it is easy to share and costs the speaker nothing. It also gives you a repeatable pipeline: 20 lectures is 20 assets and 20 warm outreach targets, all created from a single public source.

> "summarize the lectures into blog posts"

**Evidence:** ThinkApps summarized YCombinator's 20-lecture How to Start a Startup series, and the featured speakers often shared the write-ups with their own audiences.

**How to do it**

1. Find a long-form video or podcast series in your niche whose speakers are people you want to reach.
2. Assign one writer per episode and have them watch the full recording rather than skimming a transcript.
3. Write each summary as a standalone post with the speaker's key points, numbers and examples, credited by name.
4. Link back to the original video in each post so the summary complements rather than replaces it.
5. Send the finished post directly to the speaker featured in that episode, with no ask beyond a look.
6. Post it to the series publisher's community channels, such as their Twitter account and relevant subreddits or HackerNews.
7. Repeat down the whole series so one source produces a run of assets and a run of warm contacts.

**Pitfall:** Summarizing so thoroughly that there is no reason to watch the original. The speaker sees it as scraping their work rather than promoting it, and declines to share.

**Apply at Pabau:** Pabau could summarize sessions from aesthetics industry conferences and webinars into blog posts, credit and notify each speaker, and pick up shares from practitioners who already have clinic-owner audiences.

**Apply anywhere:** Turn a long video or podcast series in your niche into one summary post per episode, credit and link the original, then send each post to the speaker it features. One public source yields a run of assets and a run of warm outreach contacts.

### 26. This week: create free profiles on reactive-PR platforms  `33.12`
*useful · concrete actions · source 33*

Asked for one tactic anyone could implement immediately, the guest's answer is to set up free expert profiles on reactive-PR platforms — Qwoted, Connectively, Source of Sources, Featured, and Source Bottle (noting these platforms frequently merge and rebrand) — to start receiving free journalist pitch requests. To stand out as a credible real person rather than an AI-generated placeholder, a profile just needs a couple of photos of you doing your service and a few lines about your experience (a photo of a diploma is offered as an example); from there, response speed to incoming requests matters more than crafting a perfect pitch, since journalists work on deadlines. The guest frames even minimal, consistent participation as outperforming inaction entirely.

> "set up a profile on Qwoted, Connectively"

**How to do it**

1. Create free expert profiles on Qwoted, Connectively, Source of Sources, Featured, and Source Bottle (or whichever of these platforms is currently active, since they frequently merge and rebrand).
2. Fill in each profile with your name, credentials, business, and areas of expertise.
3. Add proof-of-real-person elements: a couple of photos of you doing your service/work and a few lines about your experience or credentials.
4. Subscribe to daily pitch-request emails or notifications for your relevant topic categories on each platform.
5. Each day, scan incoming requests for matches to your expertise and respond quickly with a genuine, specific answer rather than polishing it extensively.
6. Treat this as ongoing baseline activity even before investing in any paid or active PR campaign.

**Tools:** Qwoted, Connectively, Source of Sources, Featured, Source Bottle

**Pitfall:** Over-polishing a pitch response instead of sending it quickly — the source says response speed matters more than a perfect answer, since journalists on deadline often go with whoever responds first with usable material.

### 27. Title migration press releases on your ranking claim, not your brand name  `45.5`
*useful · concrete actions · source 45*

David identifies a common mistake in SEO-driven press releases: leading with the company's brand name in the headline, which only makes sense if you're already a globally recognized brand like Apple or Microsoft. For any other company, the press release title should instead lead with the specific, provable ranking or category claim (e.g., 'the number one app in the App Store for networking'), because that framing is more likely to earn pickup and clicks and, critically, drives more visitors through Chrome — and Chrome reporting all the URLs visitors land on is one of the signals that helps ensure your site's pages get crawled during a migration window.

> "putting their brand name front and center"

**How to do it**

1. Before writing a migration-period press release, identify a specific, factual, provable ranking or category claim about your product (e.g., a real marketplace or category ranking).
2. Draft the press release headline around that specific claim rather than the company brand name, unless your brand is already a top-tier household name.
3. Distribute the release to maximize actual visitor click-throughs to the site, not just impressions, since visitor traffic through Chrome is what generates the crawl signal.
4. Time this release to land within your migration window so the resulting visitor traffic helps Google crawl and prioritize the migrated site's pages (inferred, ties to the broader crawl-priority goal).

**Tools:** Chrome (as a crawl-signal source)

**Pitfall:** Leading a press release with your own brand name when you aren't already a globally recognized brand — David calls this 'a big mistake a lot of companies make,' since a generic brand name in the headline doesn't earn the attention or clicks that a specific, provable ranking claim does.

### 28. Use Connectively (ex-HARO) for free expert-source backlinks monthly  `07.17`
*useful · concrete actions · source 07*

Connectively (the current name for HARO — Help A Reporter Out) matches subject-matter experts to journalist/publisher queries, and is presented as one of the best free backlink sources for anyone with genuine expertise. After creating an account and linking LinkedIn (used for query-matching), users receive daily publisher queries, some pre-flagged as good profile matches; answers go through a pitched-selected-published pipeline, and published answers include a citation and backlink to the expert's site. The creator's own benchmark — 5 of 12 pitches published, roughly a 40% hit rate — is presented as a normal, acceptable outcome rather than a disappointing one, on a free tier capped at about three answers per month (with a paid tier available for higher volume).

> "Make an account, answer a few questions, and you'll get"

**How to do it**

1. Create a free account on Connectively (the rebranded HARO).
2. Connect/link your LinkedIn profile so the platform can match incoming journalist queries to your expertise.
3. Review the daily list of publisher/journalist queries, prioritizing any flagged as matching your profile.
4. Answer up to three queries per month on the free tier (or upgrade to the paid tier for higher volume), writing specific, substantive answers rather than generic marketing copy.
5. Submit each pitch and track its status through the pipeline: pitched, selected, published.
6. Once a piece is published, search for your name or brand to confirm it links back to your site, and log the resulting URL.
7. Treat roughly a 40% publish rate (about 5 of every 12 pitches) as a normal benchmark rather than a failure signal.
8. Repeat this monthly as an ongoing habit rather than a one-off campaign. (inferred cadence)

**Tools:** Connectively, LinkedIn

**Pitfall:** Expecting every pitch to get published and giving up after early rejections — the creator's own ~40% hit rate (5 of 12) is presented as a solid, normal outcome, not evidence the tactic doesn't work.

### 29. Use SparkToro's "take action" feature to build a ranked influencer list  `43.3`
*useful · concrete actions · source 43*

Rand describes a specific SparkToro workflow for influencer/PR targeting: go into the tool, use its 'take action' feature, and ask it something like 'tell me the most influential Instagrammers who reach this particular audience,' and it returns a ranked top-20 list of accounts. He's explicit about the tool's limits: SparkToro tells you the 'where' (which channels your audience over-indexes on) and the 'who' (which specific accounts reach them), but not the 'how' or 'how much' — cost, approachability, and outreach execution remain manual legwork after you get the list.

> "go into SparkToro, click "take action," and say"

**How to do it**

1. Log into SparkToro and define your target audience using demographic, behavioral, or keyword-based filters matching your actual buyer persona (e.g., clinic managers, aesthetic practice owners).
2. Run the audience-research query first to confirm which social platforms and content sources that audience over-indexes on.
3. Click the tool's 'take action' feature within the audience report.
4. Enter a request naming the specific platform and audience, e.g., 'tell me the most influential [LinkedIn/Instagram/YouTube] accounts that reach this audience.'
5. Review the returned top-20 ranked list of influencer/publisher accounts.
6. Manually research each of the top 20 for outreach cost, responsiveness, and fit, since SparkToro does not provide pricing or approachability data (inferred, stated as a gap by Rand).
7. Prioritize outreach to the accounts with the best combination of relevance (from SparkToro) and feasibility (from your manual research) (inferred).

**Tools:** SparkToro

**Prompt / template:**

```text
Tell me the most influential Instagrammers who reach this particular audience
```

**Pitfall:** Expecting SparkToro to tell you cost or ease of access to an influencer — it only answers the 'where' and 'who,' not the 'how much,' so budget and outreach planning still require separate manual research.

### 30. Use aipodcastmatcher.com to land 30 podcasts in 90 days  `24.3`
*useful · concrete actions · source 24*

The host's own pre-fame growth tactic was using aipodcastmatcher.com, a platform that matches guests seeking podcast appearances with hosts seeking guests, to book roughly 30 podcast appearances within 3 months specifically for SEO/backlink and relationship-building purposes. He frames this as a high-volume, low-selectivity sprint rather than a slow, curated approach, and notes the payoff extended beyond backlinks into other business benefits he only discovered afterward. He has a companion guide, "How to Get on Podcasts as a Guest in 2026 the Easy Way," on his own site detailing the pitching workflow.

> "go on 30 podcasts in 3 months"

**How to do it**

1. Create a guest profile on aipodcastmatcher.com describing your expertise and topic areas.
2. Respond to and accept matched podcast opportunities broadly rather than being highly selective, especially before you're well-known in your space.
3. Aim for a high-volume sprint — the source's own benchmark is roughly 30 appearances within 3 months — to compound backlinks and relationships quickly.
4. On each appearance, confirm the show links back to your site in its notes/website to capture the backlink value.
5. Track secondary benefits beyond backlinks (audience exposure, relationships, future reciprocal guest invites), since the source found value there he hadn't anticipated.
6. Read the source's own companion guide ("How to Get on Podcasts as a Guest in 2026 the Easy Way") for the detailed pitching workflow. (inferred)

**Tools:** aipodcastmatcher.com

### 31. Embed NAP data in every press release as a stronger citation  `08.13`
*context · concrete actions · source 08*

For local businesses with a Google Business Profile, appending the full NAP block (Name, Address, Phone) to the bottom of every press release is described as a stronger citation than most dedicated citation/directory sites, because most citation sites never actually get indexed by Google unless they separately earn reviews and inbound links, whereas press releases get indexed and syndicated more easily. The source's benchmark cadence via EIN Newswire is roughly $50 per release, purchased in batches of about 15 (roughly twice a month, around $3,000/month total), built around genuine news hooks (settlements, awards, review-count milestones) with keyword and geo terms varied across each headline. An index-check pass on new clients' existing 'citation' listings often revealed only 3-4 out of a claimed 100 listings were actually indexed, reinforcing that indexed status — not listing count — is what matters.

> "it's basically a citation, actually a stronger citation than most citation sites"

**How to do it**

1. For any local business with a Google Business Profile, add the full NAP (Name, Address, Phone) block at the bottom of every press release distributed, not only on directory listing sites.
2. Distribute releases via a wire service such as EIN Newswire, budgeting roughly $50 per release purchased in batches of about 15 (roughly twice a month).
3. Anchor each release to a genuine news hook: case settlements, awards, or milestones (e.g., a review-count threshold reached).
4. Vary the keyword and geo terms used in each release's title so repeated releases don't read as literal duplicates.
5. Before investing further in any existing directory/citation listings, run an index-check pass to confirm which listings are actually indexed by Google rather than assuming a claimed listing count is real.
6. For any award or milestone without a press release in the last 6-12 months, reissue a new release about it so it stays fresh in what LLMs and search engines have indexed.
7. If a release stops staying indexed, prioritize building real links directly to that release page over relying on paid 'indexer' tools, which were tested and found to make no measurable difference.

**Tools:** EIN Newswire, Manus

**Pitfall:** Assuming paid 'indexer' tools will keep syndicated press releases indexed long-term — testing showed 'the indexers just weren't making a difference'; real backlinks or fresh re-publication work better.
