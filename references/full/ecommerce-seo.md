# Ecommerce SEO

5 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Reframe category pages around intent, not product type  `47.4`
*core · concrete actions · source 47*

Edward cites a case he covered previously on his podcast about Pretty Little Thing, a women's fashion e-commerce site, restructuring its category-page taxonomy away from plain product-type categories, such as 'jeans,' toward occasion or intent-driven categories, such as 'airport outfits,' and reports this produced an 841% traffic uplift. He adds a striking secondary result: every single item featured on these new intent-driven category pages sold out of stock, suggesting the intent-matched framing didn't just capture more search traffic but converted at an unusually high rate because it matched exactly what the searcher had in mind, an occasion or use case, rather than a generic product attribute. This illustrates that intent-driven category taxonomy can outperform plain product-type taxonomy on both traffic and sell-through simultaneously, not just one or the other.

> "and this led to an 841% uplift"

**How to do it**

1. Audit your current e-commerce or content category structure and list every category currently framed purely around a product type or attribute, such as 'jeans,' 'dresses,' or a generic feature name.
2. Research the actual occasions, use cases, or situations customers associate with those product types, via keyword research, on-site search queries, or customer interviews, to find intent-driven framings such as 'airport outfits' for travel wear.
3. Build new category or landing pages framed around the identified occasion or intent rather than the plain product type, while keeping the underlying product type as a secondary filter or tag.
4. Curate the specific products or content featured on each new intent-driven page to genuinely match the stated occasion or use case, rather than just relabeling the same generic grid.
5. Compare traffic and conversion or sell-through rates on the new intent-driven pages against the old product-type category pages to quantify the uplift (inferred).
6. Roll out the intent-driven framing pattern to additional categories once it's validated on an initial batch, rather than converting the entire site at once (inferred).

### 2. Build collection pages from the product catalogue and Search Console gaps  `57.12`
*useful · concrete actions · source 57*

Jackie's newer company builds tens of thousands of Shopify collection landing pages at scale from long-tail keywords derived from a store's own product catalogue. The process: ingest the catalogue, generate every variation from the catalogue plus Search Console data, then pair the right products to each page. The selection logic is the interesting part - find what the store isn't ranking for but is already getting impressions for, filter to page two and three, spin up a collection page for it, and he reports seeing those pages move up overnight. Cody's addition is why it works commercially: if someone searches 'best XYZ product' and lands on a page that is exactly 'best XYZ product' and buys, the whole search journey is coherent and every signal supports Google trusting that result. The technical enabler he flags is crawl budget - they built the pages extremely lightweight and cached globally so they load instantly, which means thousands of pages fit inside the crawl budget Google allots.

> "tens of thousands of Shopify collection"

**How to do it**

1. Ingest the product catalogue and generate the full set of attribute and category combinations it supports.
2. Pull Search Console query data and find queries earning impressions where no page ranks well.
3. Filter to positions on page two and three - existing impressions with no page is the highest-yield signal.
4. Cross-reference each opportunity against the catalogue to confirm you have products that genuinely satisfy it.
5. Generate the collection page with the matched products, so the page delivers exactly what the query asked for.
6. Keep the pages extremely lightweight and cached at the edge, so crawl budget stretches across thousands of URLs.
7. Monitor which pages get crawled and indexed, and prune combinations that produce empty or near-empty collections.

**Tools:** Google Search Console, Shopify

**Pitfall:** The gating condition is that products actually exist for each combination - generating attribute pages the catalogue can't fill is how programmatic collection pages become thin-content liabilities.

**Apply:** Pabau's directory-style and location-style pages are the analogue: build them only where there's real data to fill the page and existing impressions to justify it, and keep them fast enough that crawl budget isn't the limiting factor.

### 3. Build new products for the pain points your content keeps surfacing  `138.10`
*useful · concrete actions · source 138*

Cup & Leaf did not stop at matching existing stock to article topics. Nat Eliason says most of their content planning is now focused on the specific problems people are trying to address with tea, and that they created new products aimed at those problems, naming a 'happy tummy tea' and a 'sleepy time mint tea'. This closes the loop the other way: content research becomes product research. The pain-point keyword list is a ranked, quantified list of what customers want solved, gathered at scale and for free, and the recurring entries with no matching SKU are product gaps. Most teams treat the keyword list as a publishing queue only and never pass it to the people who decide what to build.

> "most of our content planning is focused on these specific problems"

**Evidence:** Cup & Leaf created a 'happy tummy tea' and a 'sleepy time mint tea' specifically to serve the pain points their content research surfaced.

**How to do it**

1. Take the ranked 'best [category] for [problem]' keyword list produced by the pain-point research.
2. Mark every problem where your catalogue has no product built specifically for it.
3. Rank the gaps by combined search demand and how often the problem appears in support tickets and reviews.
4. Take the top gaps to whoever owns the product roadmap as a demand brief, with the search and ticket numbers attached.
5. When a new product ships, name it after the problem, as with 'happy tummy tea', so the article-to-collection-to-product path uses one vocabulary.
6. Create the matching collection and publish or refresh the article at the same time as the launch, not months after.
7. Review the gap list each quarter as new problem keywords appear.

**Pitfall:** Passing raw keyword volume to the product team without the customer evidence. Volume alone is a weak case for building anything, and the request gets ignored; the ticket and review counts are what make it land.

**Apply at Pabau:** The problems Pabau's aesthetics content keeps circling, such as no-shows, consent compliance and inventory tracking, should be fed to Pabau's product team as a demand brief with search and support-ticket counts attached.

**Apply anywhere:** Feed the pain-point keyword list to whoever owns the roadmap, flagged for problems with no matching product. Attach support-ticket and review counts so the demand case is not resting on search volume alone.

### 4. For low-priced ecommerce, send ads to a category page instead of an opt-in  `155.16`
*useful · content insights · source 155*

Grow and Convert close the case study with the counter-case. For a business without a major nurtured sale waiting at the end, the email-capture step can cost more than it earns. Their example is a new menswear ecommerce store: the shirts and jeans are the final product, so there is no large B2B contract or coaching program to nurture toward. In that situation you may find that sending ad traffic straight to a category page makes more money in both the short and long term than capturing an email first. The exception they name is when ads will not run profitably on their own but you know subscriber lifetime value is high. Then run ads to the list and add a cheap, popular item as an upsell purely to cover the media cost.

> "just sending ad traffic to a category page"

**Evidence:** Grow and Convert's own qualification of the case study, given for stores whose products are the final sale rather than a step toward one.

**Tools:** Facebook Ads

**Pitfall:** Adding an email capture in front of a direct-purchase product inserts a step that loses buyers who were ready to check out, and the list built that way may never be monetized.

**Apply at Pabau:** Pabau sells a nurtured subscription, so the opposite applies, but the same test is worth running on template pages: compare direct-to-demo paid traffic against email capture first on matched spend.

**Apply anywhere:** If your product is the final sale rather than a step toward a larger one, test paid traffic straight to a category page before building an email-capture funnel in front of it.

### 5. Prepare for AI initiation by exposing machine-readable product data  `76.14`
*useful · concrete actions · source 76*

The paper identifies three tiers of agent involvement in transactions. AI recommendation, where the agent suggests products but takes no transactional action. AI initiation, where the agent populates a checkout form or assembles a cart but requires a human to confirm. AI transaction, where the agent autonomously executes a purchase within a predefined budget. The authors argue AI initiation is the most viable configuration, because a one-click confirmation inside an LLM interface is functionally equivalent to one-click purchase on the brand's own site: the user retains final authority while the agent does everything else. They warn that full AI transaction risks accidental purchases with no explicit confirmation, creating logistical problems for businesses while users may still be liable under existing regulatory frameworks on electronic fund transfers. The infrastructure is already live or deploying: Anthropic's Model Context Protocol, OpenAI's Agentic Commerce Protocol, Google's Universal Commerce Protocol and the Agent-to-Agent standard. McKinsey estimates up to $1 trillion in US B2C retail revenue could be orchestrated by AI agents by 2030.

> "AI initiation represents the most viable configuration"

**Evidence:** McKinsey estimate of up to $1 trillion in US B2C retail revenue orchestrated by AI agents by 2030; four named protocols described as live or in active deployment.

**How to do it**

1. Publish product or plan data in structured, machine-readable form: names, prices, inclusions, availability and fulfillment terms.
2. State fulfillment and cancellation terms explicitly on the page rather than in a linked policy PDF.
3. Design signup and checkout so an agent can populate the form and a human can confirm in one click.
4. Do not build flows that let an agent complete a purchase without an explicit human confirmation step.
5. Track the four protocols already live or deploying: Model Context Protocol, Agentic Commerce Protocol, Universal Commerce Protocol and Agent-to-Agent.
6. Treat the current recommendation-only period as the build window, since the paper calls it the most strategic window available.

**Pitfall:** Building for fully autonomous agent purchasing. Accidental purchases with no explicit confirmation create liability questions under electronic fund transfer rules and operational mess for the merchant.

**Apply at Pabau:** Pabau sells subscriptions rather than retail goods, so the actionable piece is machine-readable plan and pricing data plus explicit terms, and a demo-booking flow an agent can fill for a human to confirm.

**Apply anywhere:** For a subscription business the actionable piece is machine-readable plan and pricing data plus explicit terms, and a signup flow an agent can fill for a human to confirm.
