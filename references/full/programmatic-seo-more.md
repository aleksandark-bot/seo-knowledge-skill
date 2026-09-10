# Programmatic SEO — supporting

7 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Benchmark: 20 minutes to about an hour per AI-drafted article  `50.11`
*useful · ai workflows · source 50*

The task pipeline moves items through a simple status flow: backlog for unscheduled or manual items, queued for created-and-waiting items, in progress for an agent actively researching and writing, and needs review for a finished draft awaiting human sign-off. A new article, from creation to a finished draft ready for human review, takes roughly 20 minutes up to about an hour. The exact time depends on how much other content is already queued in the system at that moment. This gives a concrete throughput benchmark for a multi-agent research-and-drafting pipeline: the bottleneck isn't the writing itself but system load and queue depth, since a single idle system finishes fastest and a busy one takes closer to an hour.

> "It can take from 20 minutes up to like an hour"

**How to do it**

1. Define at least four pipeline statuses for content tasks: backlog, queued, in progress, and needs review.
2. Route any manually-created task, such as typing "best SEO agency buying guide," into the queued status automatically upon creation.
3. Have an orchestrating or project-manager agent pull the next queued item into in progress and assign it to an available task agent.
4. Time how long each task actually takes from in progress to needs review and log it.
5. Track total items currently queued alongside each completion time to establish the relationship between system load and turnaround, the source's own range being roughly 20 minutes to about an hour (inferred measurement approach).
6. Use this benchmark to set realistic expectations with stakeholders about how fast the pipeline can produce review-ready drafts under light versus heavy load.

### 2. Rank thin database entries by building the library, not the article  `75.9`
*useful · concrete actions · source 75*

In his examples of unique content experiences, the author points to two database plays. Gartner's Glossary ranks number one for "channel partners", a 4,300 monthly volume keyword, with just 30 words on the page. His point is that the win came from thinking in terms of a glossary database rather than an article, so the format and the library carry the page rather than the word count. He pairs it with CustomerGauge's NPS benchmarks library, a database of NPS scores from around the world, where he says he worked and can vouch for the monthly organic volume. Yoga Journal's yoga pose finder is his third case. All three replace long-form pages with a browsable, structured collection where each entry is short and the set is the asset.

> "with just 30 words"

**Evidence:** Gartner's Glossary ranks number one for channel partners, 4,300 monthly volume, on about 30 words; CustomerGauge's NPS benchmarks library, which the author worked on, drives what he calls vouchable monthly organic volume.

**How to do it**

1. Find the entity class your audience looks up repeatedly: terms, benchmarks, poses, codes, procedures.
2. Check the head keyword volumes for a sample of those entities to confirm real demand at entry level.
3. Design one page template with a short canonical answer, around 30 to 100 words, plus structured fields.
4. Populate the library from a data source you own or can maintain, not from paraphrased competitor text.
5. Build browse and filter navigation across the whole set so the library is usable as a library.
6. Interlink entries to their parent hub and to closely related entries.
7. Publish in cycles, a batch at a time, and confirm the first batch ranks before scaling the rest.
8. Refresh the underlying data on a schedule, since a stale benchmark library loses its reason to exist.

**Pitfall:** Expanding each entry to article length to look substantial. That destroys the format advantage and turns a maintainable library into hundreds of thin articles you cannot keep current.

**Apply at Pabau:** Pabau already runs /diagnostic-codes/ and /procedure-codes/ as libraries. Treat them as the Gartner Glossary pattern: keep each entry short and canonical, add filtering across the whole set, and resist padding entries into articles.

**Apply anywhere:** For entity classes your audience looks up repeatedly, build a short-entry library with browse and filter navigation rather than long articles. Keep entries around 30 to 100 words and refresh the underlying data on a schedule.

### 3. Run live first-party databases and reference hubs for facts that change  `66.15`
*useful · concrete actions · source 66*

Content that lets users look up current facts that change — price, availability, inventory, status, eligibility, schedules or rates. Its role is current-state reference across a set of relevant items: showing verified facts, rather than calculating a personalized answer (that is the tools type) or creating one URL per keyword variation (that is the deprioritized programmatic type). It covers live inventories, availability databases, status pages, rate or price trackers, store locators, event calendars and frequently updated reference hubs. It scores High on click resilience, citation potential, business value and proprietary advantage at High effort. Click resilience is High for a structural reason: an AI answer cannot be trusted on a fact that changed since it was trained or crawled, so the user still has to check the source. The High effort is almost entirely maintenance — the freshness is the product, and a stale live database is a liability rather than a lower-value asset.

> "lets users look up current product or service facts that change"

**How to do it**

1. Identify the facts in your business that genuinely change — availability, price, status, capacity, schedules, rates — and that users currently have to ask for.
2. Define the item set the hub covers, and confirm each item is a real entity a user would look up rather than a keyword variant.
3. Wire the data to its live source so the page reflects the system of record automatically, rather than being updated by hand.
4. Show the timestamp of the last update on every record, since the freshness is the reason the page is worth visiting.
5. Make each record readable without JavaScript, so AI systems and agents can read the current value rather than an empty shell.
6. Add filtering and lookup that matches how users actually search the set — by location, by date, by model, by status.
7. Mark records up in structured data with the fields that change (availability, price, event date, opening hours) and keep the markup live too.
8. Monitor the pipeline: alert on stale data, failed syncs and records that have not changed when they should have.
9. Publish a history where it is useful — a change log or price trend — because that turns a current-state lookup into a citable dataset.
10. Cap the item set at entities you can genuinely keep current, since maintenance cost scales with the set and stale records erase the type's advantage.

**Tools:** Schema.org, Screaming Frog

**Pitfall:** Letting the set grow past what the pipeline can keep fresh. A live database whose records are stale has the maintenance cost of this type and the credibility of the deprioritized programmatic type — the worst position in the worksheet.

**Apply at Pabau:** Pabau's genuinely changing facts are what to build here: which markets and integrations are live, current status, supported hardware, and what each subscription includes. Wire them to the source of record with a visible last-updated date instead of hand-maintaining a page that will silently go stale.

**Apply anywhere:** The genuinely changing facts are what to build here: which markets and integrations are live, current status, supported hardware, and what each plan includes. Wire them to the source of record with a visible last-updated date instead of hand-maintaining a page that will silently go stale.

### 4. Ship a three-hour data-extraction tool as your link magnet  `68.27`
*useful · concrete actions · source 68*

Cody's alternative to the AI-domain play is deliberately unglamorous: build something stupid and simple that does data extraction. His example is a YouTube email extractor that scrapes channel URLs and pulls out the email addresses behind the capture. He says the stack is Claude Code plus RapidAPI endpoints plus a Supabase connection plus Stripe, and you can have it out the door in about three hours. His argument for extremely small product scope: do one thing, charge for it, and people will find value. He backs it with a Chrome extension he owns that has paid his rent for eight years, and notes these dumb tools run at 90 to 95 percent margins with one customer support employee. For SEO teams the relevant read is that a genuinely useful single-purpose tool is now a few hours of work, which changes the economics of building a link magnet.

> "go and build a YouTube email extractor"

**Evidence:** Cody estimates roughly three hours to ship the YouTube email extractor on that stack, and cites a Chrome extension that has paid his rent for eight years at 90-95% margins.

**How to do it**

1. Pick one narrow extraction or conversion job your audience does manually today.
2. Check RapidAPI for an existing endpoint that does the heavy lifting so you are not building the data layer.
3. Build the interface and logic with Claude Code, targeting a few hours rather than a few weeks.
4. Use Supabase for storage and Stripe for payment so there is no custom backend.
5. Ship it doing one thing only, with no settings and no roadmap.
6. Charge from day one, since a price tells you whether the value is real.
7. Point links and content at the tool rather than at a money page, since a working tool earns links a blog post cannot.

**Tools:** Claude Code, RapidAPI, Supabase, Stripe

**Pitfall:** Widening the scope is the failure mode. Cody says these tools work because the product scope is extremely small and warns directly against complicating them.

**Apply at Pabau:** Pabau's code-reference pages already attract a technical audience; a single-purpose free tool for one recurring practice task would earn links and mentions those pages cannot, and now costs hours rather than a sprint.

**Apply anywhere:** Build a single-purpose tool that does one extraction or conversion job, using an existing API plus a code agent, and ship it in hours. One genuinely useful tool earns more links than a quarter of blog posts.

### 5. The Pinterest pin-variation play for owning a visual SERP  `57.18`
*useful · concrete actions · source 57*

Cody's account of work for a bathtub and shower-base manufacturer, which he says became their best lead-generation channel by a wide margin. The mechanic: take the product render photos, generate hundreds of different pin variations from them, and keyword-stuff the pin descriptions, because Pinterest does not police keyword stuffing the way a search engine does. All you then need is repins for a pin to rank, so a small amount of paid traffic - he puts it at about $100 - gets a pin ranking for its target phrase. The outcome he describes is owning the entire front page of Pinterest for a term like 'best shower base for RV', with every pin looking different but all linking back to the same piece of content. He notes he hasn't run it recently so can't confirm it still works, and Jesper's separate observation in source 58 is that Pinterest was historically enormous, that he predicts it comes back, and that he knows an operator currently using AI-generated images with an auto-pin generator to drive a recipe site monetised with display ads - printing money on Pinterest traffic alone, without ranking in Google or Bing at all.

> "We used to do this on Pinterest"

**How to do it**

1. Identify the commercial long-tail phrases in your category that have a visual buying decision attached - product selection, design choice, room or setting.
2. Assemble the source imagery: product renders, photography, or generated images.
3. Generate many visual variations per target phrase rather than one pin per product, so the same destination is represented by different-looking assets.
4. Write keyword-dense descriptions for each pin against its target phrase.
5. Point every variation at the same destination page, so the traffic consolidates even though the pins differ.
6. Seed repins with a small amount of paid promotion - his figure is around $100 per pin to get it ranking.
7. Check the Pinterest search results page for your target phrase and keep adding variations until you occupy most of the visible grid.
8. Track it as its own acquisition channel. His point about Pinterest users is that they arrive buyer-ready and mentally in a discovery state, which is why it converted for a category as unglamorous as shower bases.
9. Automate the generation step if it works - Jesper's contact pairs image generation with an auto-pin tool to run it continuously.

**Tools:** Pinterest

**Pitfall:** Keyword-stuffed descriptions and bulk near-duplicate pins breach Pinterest's spam policies, and the account is the thing at risk. Cody's own caveat is more practical: he hasn't run this in years and doesn't know whether the loophole still holds, so test on a throwaway account before building a programme on it.

**Apply at Pabau:** Pinterest is genuinely under-used for aesthetics and treatment content, where the buying decision is visual - before-and-after imagery and treatment guides are exactly the kind of asset that earns repins, and it reaches consumers rather than clinic owners.

**Apply anywhere:** Pinterest is genuinely under-used in any category where the buying decision is visual - before-and-after imagery, design guides and product comparisons are exactly the assets that earn repins, and it reaches consumers rather than trade buyers.

### 6. The curve-then-trickle publishing pattern, and pruning what doesn't belong  `56.17`
*useful · concrete actions · source 56*

For the sites where he does go hard, Cody describes the shape rather than a number. He will publish a large batch simultaneously - his example is 10,000 articles inside a month, dumped at once - and what he sees is a small bump, then bouncing around in the SERPs, and then a curve in impressions and clicks as the signal gets healthier with Google. He starts the rewriting process only once that curve appears, on a monthly cadence, looking at both the best articles and the ones falling off. Content that no longer feels like it belongs in the catalogue gets no-indexed, or 301-redirected to the homepage if it must be removed - he avoids drafting pages because he doesn't want to create 404s. After the curve lifts, publishing switches from batch to a trickle, so the blog reads as something ongoing. His justification for the batch is that this is how sites launch anyway: you build a whole website, publish it all at once, and then manage and mould it. Keyword selection for a batch that size took a team member about three weeks of filtering for cannibalisation, done partly manually and partly with Claude Code over a database of the whole set.

> "I'll dump all of those simultaneously"

**How to do it**

1. Do the cannibalisation work before publishing - map the full keyword set into clusters and remove overlaps (he budgeted about three weeks of a person's time for a 10,000-page set).
2. Load the whole keyword set into a database and use an agent over the top of it to map clustering and catch overlaps.
3. Publish the batch and expect noise: a small bump, then movement around the SERPs, not a clean climb.
4. Wait for a genuine curve in impressions and clicks before touching anything.
5. Once the curve appears, start a monthly rewrite cycle covering both the best performers and the decliners.
6. No-index pages that no longer fit the catalogue; 301 to the homepage if they must go, and avoid drafting pages into 404s.
7. Switch from batch to a steady trickle of new posts once the curve is established, so the site looks actively maintained.

**Tools:** Claude Code, Google Search Console

**Pitfall:** He says twice that he isn't suggesting anyone do this. The transferable parts are the pre-publication cannibalisation work, the wait-for-the-curve discipline, and the pruning rule - not the batch size.

**Apply at Pabau:** The reusable pattern for Pabau is the pruning and cadence half: monthly review of both risers and decliners, no-index rather than delete, and a steady publishing rhythm that signals an actively maintained site.

**Apply anywhere:** The reusable pattern is the pruning and cadence half: monthly review of both risers and decliners, no-index rather than delete, and a steady publishing rhythm that signals an actively maintained site.

### 7. Turn your own site content into embeddings to auto-seed new topics  `50.8`
*useful · ai workflows · source 50*

One of the five keyword-universe sources works by scraping every page on the client's own site and converting its content into a vector database, turning the words on each page into numerical embeddings that an LLM can compare mathematically rather than by exact keyword matching. The system then runs a cosine similarity function against that vector database to infer what topic or seed keyword each existing page should really be about, which the builder says is especially valuable on product and service pages because it surfaces additional real commercial-intent keywords tied to pages you already have rather than only pages you don't. He notes this specific piece was easy to build once the surrounding data pipeline already existed, such as a data warehouse and ingestion pipelines, since a coding agent could implement the embedding/similarity function itself without much difficulty.

> "uses a cosine similarity function to find what the page should be"

**How to do it**

1. Scrape or export the full text content of every page on the target site.
2. Generate vector embeddings for each page's content using an embeddings model or API and store them in a vector database.
3. For a target keyword or topic, generate its own embedding using the same model.
4. Run a cosine similarity comparison between the topic's embedding and every page's embedding to find the closest-matching existing pages.
5. Use the closest matches to auto-suggest what topic or seed keyword each page is really about, surfacing commercial-intent keywords tied to product/service pages specifically.
6. Feed the surfaced keywords back into the main keyword universe or clustering pipeline for relevance scoring rather than treating this as a standalone report (inferred integration step).

**Tools:** a vector database, an embeddings model
