# Branded Search

17 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Branded search CTR is a huge indirect ranking signal  `18.6`
*core · content insights · source 18*

The claim is that branded search functions as a powerful indirect ranking signal through click-through rate: a highly competitive, unbranded term like 'best horse betting site' might see click-through rates as low as 0.8%, requiring constant authority-building and topical expansion just to hold position, whereas branded searches ('[Bar Name] Manchester' style queries) come in at a 40-88% minimum click-through rate. Because CTR feeds into the ranking calculation, that magnitude difference means branded-search volume carries an outsized 'authority calculation' effect compared with competing purely on unbranded terms. The speaker is explicit that this isn't Google 'understanding' or rewarding brands as an entity — it's a byproduct of the CTR math — but the practical effect looks identical to a brand-rewarding algorithm from the outside.

> "branded searches come in at 40-88% minimum click-through rates"

**Evidence:** Cited click-through-rate figures: about 0.8% CTR for a highly competitive unbranded term ('best horse betting site') versus a 40-88% minimum CTR for branded queries, plus an example of an 80% CTR for a branded local-business search.

**Apply:** Prioritize brand-awareness activity (PR, social, review generation, category ownership) alongside content production, since the CTR gap between branded and unbranded search is large enough to function as a major indirect ranking lever even without Google 'rewarding brands' directly.

### 2. Branded search is a moat competitors can only rent  `65.3`
*core · content insights · source 65*

The strategic argument for why branded search is worth optimising for rather than just measuring. Cody's point is defensibility: it is very hard for competitors and incumbents to take away the branded search you've developed and cultivated over years. The only way they can take it from you is to bid on your brand name - which means renting it, continuously, at a cost. That asymmetry is what makes it a moat and, in his framing, a genuinely good investment when deciding how to allocate marketing resources. It's the counterpoint to arbitrage-based acquisition, where any advantage you find is temporary because competitors can find the same one.

> "hard for your competitors"

**How to do it**

1. Treat branded search volume as an asset on the balance sheet rather than a vanity metric.
2. Check whether competitors are bidding on your brand name - that's the only route they have.
3. Decide whether to defend your own brand terms in paid search, and price that as the cost of the moat.
4. Compare the durability of branded search against the decay rate of your paid arbitrage when allocating budget.
5. Keep investing in the activities that create new brand discovery, since the asset only grows that way.

**Tools:** Google Search Console

**Pitfall:** The moat only holds if the brand is actually distinctive - a generic or descriptive brand name produces branded queries that competitors can rank for organically, not just bid on.

**Apply at Pabau:** Pabau's brand name is distinctive enough for this to hold, which makes competitor bidding on 'Pabau' the one thing worth monitoring - and defending brand terms in paid search is the cost of keeping the moat.

**Apply anywhere:** If your brand name is distinctive, competitor bidding on it is the one thing worth monitoring - and defending brand terms in paid search is the cost of keeping the moat.

### 3. Branded search is the trailing indicator for everything you can't attribute  `65.2`
*core · best practices · source 65*

This is Cody's headline argument and he states it as his only real KPI. When people discover a product on social, the first thing they do is Google the product name - and that branded search shows up in Search Console. So branded search is the trailing indicator that a new discovery has occurred. He says this has quickly evolved over six months into the only thing he cares about: is branded search going up month over month for the company. The logic is that it converts unattributable activity - founder marketing, creator sponsorships, organic social - into a measurable output, because the activities on social are what create the new organic searches. He frames the whole resource question around it: marketing resources are time, money and mental energy, and branded search is the measure of whether you're allocating them well.

> "trailing indicator for a new"

**How to do it**

1. Define what counts as a branded query for you, including misspellings and 'brand + word' variants.
2. Pull impressions for queries containing the brand name from Search Console.
3. Chart it month over month and make it a standing KPI rather than an occasional check.
4. Read it as the output of your unattributable top-of-funnel work, not as an SEO metric.
5. When it flattens, look at what changed in the social and creator activity two to three months earlier.
6. Report it alongside the self-reported signup field so the two corroborate each other.

**Tools:** Google Search Console

**Pitfall:** Branded search also rises from paid remarketing and from PR spikes, so attributing all of it to organic social will overstate that channel - the trend is the signal, not the level.

**Apply:** Branded search month over month is arguably the right single headline number for Pabau's marketing, because it's the one output that all the unattributable work - podcast, social, events, PR - eventually shows up in.

### 4. Detect and take down brand-squatting exact-match domains early  `67.21`
*core · concrete actions · source 67*

Dirk describes a squatting pattern he has seen generate 50,000 traffic views from nothing purely by ranking on another company's brand, and calls it totally illegal while noting that removing it through DMCA is its own headache. The mechanism is simple: register brand-plus-modifier or a ccTLD version of a live brand, replicate the brand's content, and outrank it in a specific geo. Detection signatures are a third-party page appearing in the top five for your exact brand name in one country, duplicated passages of your own copy on a domain you do not own, and a recently registered ccTLD carrying your name. The correct posture is defensive rather than retaliatory: brand-plus-modifier registration is trademark infringement and content replication is copyright infringement, so the remedies are UDRP or the registry's dispute process, a DMCA notice to the host and to Google, and a trademark filing in the markets you operate in. Dirk's own point is that even weeks of being outranked is revenue you never recover, so the prevention is worth more than the remedy.

> "they generate 50,000 legitimate from ranking on someone else's brand"

**Evidence:** Dirk reports seeing a brand-squatting domain generate 50,000 traffic views from nothing, and says he has multiple client cases where squatters outrank the official site in particular geos.

**How to do it**

1. Run a monthly exact-brand SERP check in every country you sell in, not just your home market, and record any third-party domain in the top five.
2. Set up a domain-monitoring alert for new registrations containing your brand string across common TLDs and ccTLDs.
3. Run a duplicate-content check on your highest-value pages to catch replicated copy on domains you do not own.
4. When you find one, capture dated screenshots of the infringing pages and the WHOIS record as evidence before contacting anyone.
5. File a DMCA notice with the host and a separate removal request with Google for the copied content.
6. Where the domain itself carries your trademark, use UDRP or the relevant registry's dispute procedure rather than the copyright route.
7. Register the trademark in each market you operate in, since the dispute processes depend on having one.
8. Do the prevention in parallel: buy the remaining brand-plus-modifier and ccTLD variants yourself so there is nothing left to take.

**Pitfall:** Relying on takedowns as the strategy. Dirk says DMCA removal is a headache in its own right, and that even a few weeks of being outranked is money you will not get back.

**Apply at Pabau:** Pabau should run a monthly exact-brand SERP check across every market it sells in and alert on new domain registrations containing the Pabau string, so a squatter is caught in weeks rather than after the traffic loss shows up.

**Apply anywhere:** Run a monthly exact-brand SERP check in every market you sell in and alert on new registrations containing your brand string. Prevention through registration beats a DMCA takedown, which is slow and does not recover the lost revenue.

### 5. Invent the category term, then manufacture searches for it  `59.11`
*core · concrete actions · source 59*

Cody's extension of the branded-search play is to create the phrase in the first place. His examples are Hightouch coining 'reverse ETL' for what is really just data warehousing and movement, and HubSpot coining 'inbound marketing' - in both cases the company invented the term, pushed it, and therefore led the category. Applied to a manufactured-search strategy, you invent a phrase that describes what you do, push people to search it, and rank for it - creating a whole new space you own by definition. Jackie confirms they'd done exactly that: the virality idea became a product called Browser Blast, and he explains what it does - it mimics virality, because driving a lot of traffic to a single URL alongside the other positive signals will move rankings up two or three pages at a time. That's his explanation for outranking five-year-old competitors after two months.

> "invent a new category term"

**How to do it**

1. Name the thing you do in a phrase that doesn't exist yet and describes the category rather than your product.
2. Use it consistently everywhere - content, sales calls, job titles, product naming.
3. Create the definitive page for the term so you're the answer when anyone searches it.
4. Push the term through owned channels so searches for it begin to exist.
5. Watch Search Console for the term appearing at all, which is the first proof the category is forming.
6. Expect competitors to adopt the term, which is the goal - by then you own the definitional page.

**Tools:** Google Search Console

**Pitfall:** A coined term with no search demand behind it is a branding exercise, not an SEO asset - the Hightouch and HubSpot examples worked because they pushed the term across an entire market for years.

**Apply at Pabau:** Pabau has a real opportunity here around the workflows it uniquely joins up - naming a process clinics already do but have no name for, and owning the definitional page for it, is a durable position no competitor can outrank.

**Apply anywhere:** There's real opportunity in naming a process your customers already do but have no name for, and owning the definitional page for it - a position no competitor can outrank.

### 6. Make month-over-month branded search impressions your single success metric  `68.21`
*core · concrete actions · source 68*

Cody says the metric of success at graphed.com is branded search increasing month over month, and he has built a specific chart for it: a Google Search Console data source filtered to keywords containing the brand name, plotting whether impressions and clicks for those keywords are rising. His reason is ownership. Everything else he built earlier, particularly print-on-demand, made good money on channels he did not own and left no asset behind. Branded demand cannot be taken away, because a competitor has to fight hand to hand for every person who is already searching your name. He credits a former boss with drilling this into him and says he wishes he had understood it earlier. This adds a concrete measurement setup to what the base already says about branded search being the trailing indicator for unattributable work.

> "is the impressions for keywords that contain Graphed increasing"

**Evidence:** Cody's stated success metric at graphed.com is a Search Console chart of impressions and clicks for keywords containing 'Graphed', rising month over month.

**How to do it**

1. Connect Search Console as a data source in your reporting tool.
2. Filter the queries report to keywords containing your brand name, including common misspellings.
3. Chart impressions and clicks for that filtered set by month, not by day.
4. Set the review cadence to monthly, since the signal is too noisy week to week.
5. Correlate the trend against content and campaign launches to see which activity moves it.
6. Report this number to leadership as the primary content metric, ahead of sessions.
7. Watch for a flat brand line while total traffic rises, which means you are renting demand rather than building it.

**Tools:** Google Search Console

**Pitfall:** Judging content on sessions instead of branded demand rewards traffic you have to keep buying or re-earning. Cody's own earlier businesses made money on channels he did not own and left no durable asset.

**Apply at Pabau:** Pabau should run this exact chart, filtered on 'Pabau' plus misspellings, as the headline number for content, since it captures the value of blog and template pages that AI answers and direct navigation would otherwise hide.

**Apply anywhere:** Build one Search Console chart of impressions and clicks for queries containing your brand name, review it monthly, and treat it as the primary measure of whether marketing is building an asset or renting traffic.

### 7. Manufactured branded search: 6.5k Search Console impressions on a 1.9k keyword  `59.10`
*core · concrete actions · source 59*

This is the most striking measurement in the episode. Local Rank ranks fourth for 'local rank tracker' on a business about a month old, beating Semrush, against competitors who have been around five years. The mechanism is that everything they do tells people the keyword to search rather than giving them a link: the cold email signature, job descriptions ('search local rank tracker to find out more about our company'), and a contact-form campaign using GSA that produced 70,000 contact-form fills in seven days containing no URL at all, just the instruction to search the term. The measurable result: Semrush estimates roughly 1,900 monthly searches for the keyword, while their Search Console shows about 6,500 - roughly three times the market estimate, generated by their own campaigns. Cody's read on the mechanism is that they're modifying the clickstream data Google measures: rank for the keyword, then tell people to search it, and the resulting click behaviour pushes the page higher. Jackie's summary is that their site is 'pretty much constantly viral in Google's eyes', and they productised the idea as Browser Blast.

> "search local Rank tracker on Google"

**How to do it**

1. Pick one keyword you can realistically reach page one for, and make it the single term every channel asks people to search. Theirs is 'local rank tracker'.
2. Get the page ranking first. The instruction only converts into clicks if you are findable when they search - they were position four on a business about a month old.
3. Replace links with the search instruction everywhere you control the message: email signatures, job descriptions ('search local rank tracker to find out more about our company'), video CTAs, podcast sign-offs, webinar closes, conference slides.
4. Ask your own audience directly. Both hosts do exactly this on the episode, asking listeners to search the term and click the result.
5. Use owned surfaces with volume. Job listings are the sly one he calls out, because a job description is read by hundreds of candidates and nobody reads it as marketing.
6. Keep URLs out of the outbound messages deliberately, so there is nothing to blacklist and the only available action is the search itself.
7. Compare your Search Console impressions for the term against third-party volume estimates. Semrush put the keyword at roughly 1,900 monthly searches while their Search Console showed about 6,500 - the gap is what the campaigns created.
8. Track position alongside impressions, so you can see whether the manufactured demand is actually moving the ranking rather than just adding impressions.
9. Watch the second-order effect Cody names: you are modifying the clickstream data Google measures, and their read is that the resulting click behaviour is what pushed them past five-year-old competitors.
10. Productise it if it works - they turned the idea into a tool called Browser Blast, whose function he describes as mimicking virality, on the basis that driving a lot of traffic to a single URL alongside the other positive signals moves rankings two or three pages at a time.

**Tools:** Google Search Console, Semrush

**Pitfall:** One of their channels was GSA-driven contact-form submission - 70,000 form fills in seven days - which is automated abuse of third parties' infrastructure and is covered separately in this collection. Every other channel in the list is an owned surface, and the measurement gap between Search Console and third-party estimates is the same either way.

**Apply at Pabau:** For Pabau there's a clean version worth running: pick one term Pabau ranks for, and use owned channels - podcast CTAs, webinar sign-offs, job descriptions, email footers - to ask people to search it rather than handing them a link, then watch Search Console impressions against the third-party estimate.

**Apply anywhere:** There's a clean version worth running: pick one term you rank for, and use owned channels - podcast CTAs, webinar sign-offs, job descriptions, email footers - to ask people to search it rather than handing them a link, then watch Search Console impressions against the third-party estimate.

### 8. Pixel every site visitor across Reddit, Taboola and every ad network  `68.13`
*core · concrete actions · source 68*

Cody calls the goal digital gravity: enough mass on the internet that a prospect falls into orbit around the brand. Operationally that means the moment someone hits the site he pixels them everywhere he can, naming Reddit, Twitter, LinkedIn, Facebook and Taboola specifically. Then every time that person appears on Instagram, Reddit or anywhere else, he is in front of them with a different angle, either naming their problem directly and offering a solution, or naming the outcome they want and positioning the product as the bridge. The strategic point is that this works alongside the content, not instead of it. The show and the clips create the reach; the pixel makes sure the reach compounds into repeated exposure rather than a single visit. He pairs this with his own success metric, which is branded search impressions and clicks rising month over month.

> "as soon as they hit the site, I'm pixeling them everywhere"

**Evidence:** Cody's own success metric at graphed.com is a Search Console chart of impressions and clicks for keywords containing the brand name, rising month over month.

**How to do it**

1. Install the retargeting pixel for every network your buyers use, including Reddit and Taboola, not just Google and Meta.
2. Fire the pixel on all site pages, including blog and resource pages, so content readers enter the audience.
3. Build separate retargeting audiences by page type, so blog readers see different creative from pricing-page visitors.
4. Write two creative tracks: one that names the visitor's problem directly, one that names the outcome and positions you as the bridge.
5. Cut those creatives from podcast or interview clips where a real person states the pain.
6. Cap frequency per network so repeated exposure does not become irritation.
7. Track branded search impressions and clicks in Search Console month over month as the outcome measure.

**Tools:** Reddit, Taboola, LinkedIn, Facebook, Google Search Console

**Pitfall:** Pixeling only on the money pages misses the blog audience, which is the bulk of the reach the content earns. In healthcare-adjacent markets, check the privacy and consent rules before firing pixels on pages tied to clinical intent.

**Apply at Pabau:** Pabau's blog and template pages are the largest retargeting audience the company has and are probably under-used for it. Confirm consent handling first, since the audience is healthcare.

**Apply anywhere:** Pixel every visitor across every network your buyers use, including the cheap ones like Taboola and Reddit, and split retargeting creative between problem-naming and outcome-naming angles. Measure the result as rising branded search.

### 9. Avoid brand names built from a verb that doubles as a noun  `73.9`
*useful · best practices · source 73*

Barnard describes a discovery he made testing text in an entity-recognition tool: a word that works as both verb and noun is hugely confusing to LLMs, which struggle to decide which sense is meant. His example is 'engineers', which can be several people who engineer things, or the act of engineering your brand authority. The related trap is capitalization on brand names built from what the company does. For a client he calls Car Sales, the first letter of a sentence is always capitalized, so the model assumes the capital on the first word should have been lowercase, drops the proper-noun signal, and takes 'sales' alone as the proper noun. His fix was to write 'At Car Sales' so the sentence starts with a different word and both capitals survive as part of one proper noun. He calls capitalization a general weak spot: 'Car Sales' is an entity, 'car sales' is just something happening.

> "using a verb that can also be a noun is hugely confusing"

**Evidence:** Barnard's unnamed client, referred to as Car Sales, required the sentence to be rewritten as 'At Car Sales' before the tool recognized the two words as a single proper noun.

**How to do it**

1. Check any brand name or key phrase for words that function as both verb and noun, and prefer a name that does not.
2. Never start a sentence with a multi-word brand name whose first word is a common noun or verb.
3. Prefix the sentence with 'At' or a similar word so the brand's own capitals stay mid-sentence and read as a proper noun.
4. Capitalize every word of the brand name consistently across the site, schema and every profile.
5. Paste the sentence into an entity-recognition tool and check the brand is returned as one entity of the right type, not two common nouns.
6. Change one word at a time and re-run when recognition fails, to isolate what breaks it.
7. Apply the same check to product names built from generic verbs.

**Tools:** Kalicube Pro, Google Cloud Natural Language API

**Pitfall:** A brand name made of common words that reads fine to humans but resolves to a generic activity for the parser. The signal is the recognition tool returning two common nouns instead of one organization entity.

**Apply at Pabau:** Pabau is a coined name, so it is safe, but Pabau's product names are not. Check that Pabau GO and similar names resolve as products and never open a sentence with a product name whose first word is generic.

**Apply anywhere:** Avoid brand and product names built from words that double as verbs. Never open a sentence with such a name; prefix it with 'At' so the capitals survive mid-sentence, and verify with an entity-recognition tool.

### 10. Brand mention potential is an entity-association objective, separate from clicks  `66.9`
*useful · content insights · source 66*

Brand mention potential asks whether the content creates a relevant reason for the brand to be associated with an entity, topic, problem or need. It is scored separately from click resilience and from business value because it pays off differently: the return is the brand being named when an AI system or another publisher discusses that topic, whether or not anyone clicks. The framework's High scores here are revealing — brand and entity pages, official documentation, original research and original reporting — while transaction pages, personalized tools and comparison pages score Medium or Low despite High business value. So the content that makes an AI system associate the brand with a topic is largely not the content that converts, which means a site optimized purely for conversion has no mechanism for building that association, and a site optimized purely for mentions has nothing to convert them on.

> "Brand mention potential is whether the content creates a relevant reason for the brand to be associated with an entity, topic, problem or need."

**Evidence:** The worksheet scores brand mention potential High for brand and entity pages, official documentation, original market research and original reporting, but Medium for transaction pages and Low for personalized tools — the same types that carry High business value, showing the two objectives are served by different content.

**Apply at Pabau:** Pabau's entity pages, feature documentation and original research are the brand-mention engine; the template and pricing pages are the conversion engine. Judge them on different metrics, and keep funding the first group even when it converts poorly, because it is what gets Pabau named in AI answers about practice management.

**Apply anywhere:** Entity pages, feature documentation and original research are the brand-mention engine; template and pricing pages are the conversion engine. Judge them on different metrics, and keep funding the first group even when it converts poorly, because it is what gets the brand named in AI answers about the category.

### 11. Brand recognition is an SEO multiplier  `62.7`
*useful · content insights · source 62*

The episode's closing argument, which connects to the branded-search material elsewhere in this corpus. Canva has built a brand synonymous with creativity, ease of use and accessibility, and that identity has a direct effect on SEO performance: when people search for design tools, Canva is the first name that comes to mind, and that recognition means they are more likely to click the result, more likely to trust the content, and more likely to share the output. So the brand functions as a multiplier on every other SEO effort rather than as a separate channel. The framing to keep is that brand building and SEO are not competing budgets - they compound, and the alignment between them is what produces the result.

> "their brand is an SEO multiplier"

**How to do it**

1. Decide the two or three attributes you want the brand to be synonymous with in your category.
2. Make those attributes consistent across the product, the content and the marketing, not just the marketing.
3. Measure branded search volume as the indicator that recognition is growing.
4. Watch click-through rate on non-branded queries as the second-order effect of recognition.
5. Judge brand and SEO investment together, since the episode's claim is that one amplifies the other.

**Tools:** Google Search Console

**Pitfall:** This is a plausible mechanism rather than a measured one in the episode - the checkable version is whether your click-through rate on non-branded queries improves as branded search grows.

**Apply at Pabau:** For Pabau, the testable version is straightforward: track branded search volume alongside click-through rate on non-branded queries, and if recognition is genuinely compounding, both should rise together.

**Apply anywhere:** The testable version is straightforward: track branded search volume alongside click-through rate on non-branded queries, and if recognition is genuinely compounding, both should rise together.

### 12. Differentiate an identical product by coining a category term  `159.16`
*useful · content insights · source 159*

Grow and Convert use Drift and Intercom to show positioning doing the work a product cannot. They are blunt that the two have an almost identical product. Intercom positions to a wide audience of marketing, sales and support with 'a new and better way to acquire, engage and retain customers'. Drift went all in on marketers and salespeople, coined 'conversational marketing', and positioned the entire product around customer acquisition, a uniquely marketing issue. Their framing is that you can use both products for the same job, so this is a matter of emphasis, not capability. This adds a live competitive example to the base's existing note that a coined position can create its own search volume: Drift's coined term is what let a narrower audience choice read as a category rather than as a limitation.

> "an almost the identical product"

**Evidence:** Drift positioned as 'the world's first and only conversational marketing platform' against Intercom's wider acquire-engage-retain framing, with substantially the same product.

**Pitfall:** Coining a term without narrowing the audience behind it. The phrase then reads as jargon rather than as a category, and nobody searches it.

**Apply at Pabau:** If Pabau wants a term of its own, it has to be tied to a narrowed audience and repeated everywhere, the way Drift tied conversational marketing to marketers and salespeople. A coined phrase used only in one blog post does nothing.

**Apply anywhere:** If your product is close to a competitor's, differentiate by narrowing the audience and naming the category around that audience's issue, then use the term consistently everywhere.

### 13. Do not name a company after the thing it sells  `73.17`
*useful · content insights · source 73*

Barnard argues the exact-match-domain naming approach worked well historically but now creates a dominant interpretation problem. If your company is called Barn Doors, Google will conclude the dominant interpretation of that query is barn doors the product, not you the company. To become the dominant interpretation and rank first for your own name you have to do an enormous job, of the kind Apple, Booking and Windy managed - he singles out Windy, a weather application, as a huge achievement for ranking first on the generic term. He named Kalicube a unique name eleven years ago specifically so he would not have to compete for his own brand term against the generic meaning. The host adds the scaling argument: Austin Plumbers cannot expand to San Francisco, and if you are a good enough marketer to dominate Austin you will regret the name. Barnard also connects this to ambiguity, which he calls the biggest problem in entity work.

> "what is the dominant interpretation?"

**Evidence:** Barnard named Kalicube a unique word eleven years ago specifically to avoid competing on the generic terms of his own business.

**How to do it**

1. When naming a company, choose a coined or unrelated word rather than the category you sell.
2. Test any candidate name by searching it and judging whether a generic meaning already owns the SERP.
3. Check whether the name limits geographic or category expansion before committing.
4. If you already own a descriptive name, accept that you are competing against the generic meaning and plan for a long brand-building effort.
5. Use consistent capitalization on every mention so the name reads as a proper noun rather than an activity.
6. Prefix sentences with 'At' when the descriptive name would otherwise start the sentence.
7. Track your rank for your own brand name as the measure of whether you are winning the dominant interpretation.

**Pitfall:** Assuming that ranking first for your descriptive name is achievable with normal effort. Barnard's counter-examples - Apple, Booking, Windy - each required an enormous job, and most descriptive brands never get there.

**Apply at Pabau:** Pabau is a coined name, which is the right side of this trade. Protect it: avoid launching sub-brands named after what they do, and keep the homepage targeting the brand rather than a category keyword.

**Apply anywhere:** Do not name a company after the product category it sells. A descriptive name puts you in competition with the generic meaning for your own brand query, and it caps geographic and category expansion later.

### 14. Name your offer as a product category, never as consulting  `170.11`
*useful · best practices · source 170*

Campbell refused the word consulting for an offer that clearly involved people delivering work. He called it a 'people powered product' instead. His reasoning is not snobbery about consultants: 'It's not because I don't value consultants, and that consultants don't have their place in the world,' but the vision was a product company, and pure software is what scales. The naming had a concrete recruiting effect. He got his head of sales, Peter, by selling the product vision, and observes that 'not a lot of people want to work for agencies, if they're interested in software.' The category label you claim decides who applies, what buyers compare you to, and what price they expect.

> "I loathe the word consulting"

**Evidence:** Campbell recruited his head of sales on the product-company framing, noting software people avoid agencies.

**How to do it**

1. Write down the category label you want buyers to compare you against, before writing any copy.
2. Check what price range and what competitor set that label implies; if the implied price is wrong, pick a different label.
3. Coin a specific term for your model if no existing category fits, and define it in one sentence on the site.
4. Use the same label on the homepage, in job adverts and in sales conversations, with no variation.
5. Audit existing pages for the label you are trying to leave behind and rewrite those lines.
6. Test whether candidates and buyers repeat your label back to you; if they use the old one, the copy has not changed enough.

**Pitfall:** Letting sales and recruiting drift onto the easier, lower-status label because prospects understand it faster. That resets buyer price expectations to the service category and puts off the hires you need.

**Apply at Pabau:** Pabau content should consistently say practice management software, and qualify products once on first mention, as the house rules require. David should audit older blog posts for language that frames Pabau as a service or a booking tool, since that sets the wrong comparison set.

**Apply anywhere:** Choose the category label you want buyers and candidates to compare you against, then use exactly that label everywhere. If no existing category fits, coin one and define it in a sentence rather than accepting a lower-status label.

### 15. Never target a keyword with the homepage  `73.18`
*useful · best practices · source 73*

Barnard says he would never, and never has, aimed at keywords with a homepage, because the homepage is the brand page. It should be ranking first for the brand name, and people who land on it are expecting the brand, what it offers and why they might want to work with the company. The host agrees. Barnard's structural argument follows from his entity model: the homepage is a signposting page whose job is a hop to somewhere else, never a destination, so loading it with keyword-targeting copy fights that job. Keyword targets belong on separate pages. This also protects the entity: the homepage's promotional register and the entity home's factual register stay separated instead of competing on one URL, which is the same reason he puts the entity home on the About page.

> "never and have never aimed at keywords with my homepage"

**Evidence:** Barnard's own homepage carries audience, offer, reasons to work with them and Trustpilot testimonials, with the factual company description deliberately held back on a separate page.

**How to do it**

1. Set the homepage's only ranking target as the brand name and confirm it holds position one for it.
2. Write the homepage as: here's who our audience is, here's what we offer you, here's why you'd want to work with us, plus proof such as review-platform testimonials.
3. Move every commercial keyword target to a dedicated page rather than the homepage.
4. Link from the homepage to those pages and to the About page, treating it as a routing layer.
5. Keep the factual entity description off the homepage; put it on the About page and link to it.
6. Measure the homepage on brand-query rank and onward click-through, not on non-brand keyword rankings.

**Tools:** Trustpilot

**Pitfall:** Optimizing the homepage for a head commercial term. It dilutes the brand-query result visitors expect, and it puts promotional keyword copy on the page where the machine is looking for a clean brand signal.

**Apply at Pabau:** pabau.com's homepage should be judged on ranking first for 'Pabau' and on routing visitors onward, not on ranking for practice management software terms. Those terms belong on dedicated pages.

**Apply anywhere:** Keep the homepage as your brand page. Target only the brand name with it, write it as audience, offer and reasons to work with you, and move every commercial keyword target to its own page.

### 16. Seed Autosuggest with a branded-plus-keyword search burst  `18.7`
*useful · concrete actions · source 18*

Case study: for the EMD freeloadbalancer.com, the team mobilized LinkedIn partners to literally search 'Kemp free load balancer' in a concentrated burst; because the domain name matched the target phrase 'free load balancer' and thousands of real searches hit at once, the site reached the top three within under a day and, as of the recording, still ranks despite not being edited since 2016. The broader mechanism described elsewhere in the discussion: a 'known entity' (has a Google Knowledge Panel) reportedly needs only 3,000-5,000 branded-plus-keyword searches to start influencing Autosuggest and related-searches, while an unknown/unestablished brand needs roughly 10 times that volume. This is distinct from bot-based CTR manipulation, which the speakers flag as fragile — the recommended version uses real people performing real searches, and the effect is framed as compounding over time.

> "We went on LinkedIn and got partners to share it"

**How to do it**

1. Pick the exact target keyword phrase you want to rank for and pair it with your brand or domain name (e.g. '[Brand] [target keyword]').
2. Recruit a network of real people (partners, employees, customers, LinkedIn contacts) via a direct outreach post or message asking them to type that exact phrase into Google.
3. Time this as a concentrated burst of searches rather than a slow trickle, since the source's case reached top-3 in under a day from a burst of 'thousands' of searches.
4. Check whether you're a 'known entity' with a Google Knowledge Panel first — known entities reportedly need only 3,000-5,000 searches to influence autosuggest, unknown entities roughly 10x that, so size your outreach accordingly. (inferred estimate of participants needed)
5. After the burst, monitor Google Autosuggest and 'related searches' for the target phrase appending your brand, and rank-track the core keyword for movement. (inferred verification step)
6. Sustain a lower trickle of branded-plus-keyword searches over time afterward, since the source claims continued volume correlates with the keyword ranking better over time, not just a one-off spike.

**Tools:** LinkedIn

**Pitfall:** Using bot networks or click-farm tools to fake branded search volume — the source says this kind of manipulation (thousands of clicks from non-aged, non-logged-in accounts with no dwell time) causes rankings to crash below baseline the moment it stops, unlike a burst of real searches from real people.

### 17. Steal your one-line company description from how customers refer you  `161.5`
*useful · concrete actions · source 161*

Question five asks whether the customer has recommended the product and, importantly, how they described it when they did. Khanal says the second half is what matters. Companies write long, abstract descriptions of themselves; hearing the words a customer uses when recommending you to a friend gives you a description a human understands. He contrasts two CRM vendors. Pegasystems describes its product as helping you optimize customer interactions to return maximum value, which nobody says out loud. Base CRM's messaging is clear and, more subtly, shows they learned there are two distinct users to satisfy, salespeople and sales managers, who want different things. The referral phrasing also reveals audience splits you did not know you had.

> "hearing how your customers describe what you do to others"

**Evidence:** Khanal contrasts Pegasystems' abstract CRM messaging with Base CRM's clearer messaging, which visibly separates salespeople from sales managers as two distinct audiences.

**How to do it**

1. Ask whether the customer has recommended you, then ask exactly what words they used.
2. Collect at least twenty of these descriptions before drawing any conclusion.
3. Strip out your own brand and category jargon and see what plain nouns and verbs remain.
4. Group the descriptions by who the recommender said it to, since different roles get pitched differently.
5. If two clearly different groups emerge, write separate messaging for each rather than one blended line.
6. Draft a one-sentence description using only words that appeared in the responses.
7. Read it aloud; if it is not something a person would say to a colleague, it is still jargon.
8. Put it on the homepage, in the meta description and in the first sentence of the About page.

**Prompt / template:**

```text
Have You Recommended (Product or Company Name) to anyone? How did you describe it?
```

**Pitfall:** Abstract value-language like 'optimize customer interactions to return maximum value' tests fine internally because everyone already knows what the product does. It fails for a stranger reading the SERP snippet, and it never appears in a search query.

**Apply at Pabau:** Pabau should ask practice owners how they describe Pabau to another practice owner, then use that phrasing in title tags and the first sentence of the homepage. It will also show whether owners and front-desk staff need different messaging.

**Apply anywhere:** Ask customers exactly how they described you when recommending you, and build your one-line description from the words that repeat.
