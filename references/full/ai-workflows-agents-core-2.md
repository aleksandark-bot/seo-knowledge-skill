# AI Workflows & Agents — core (part 2 of 2)

18 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Log the exact prompt behind every AI-generated asset  `01.7`
*core · best practices · source 01*

Every AI-generated creative asset should have its generating prompt, model, and cost stored in the same database row the moment it's created, because once an asset starts performing well weeks later, the only question that matters is exactly what produced it — and that information is unrecoverable after the fact if it wasn't captured at generation time. The article flags this as a rule nobody ever retrofits later, so it has to be built into the generation function from day one rather than added once it seems useful.

> "the only question that matters is what made it"

**How to do it**

1. Add `prompt`, `model`, and `cost` columns (or a JSONB metadata column) to whatever table logs generated creative assets.
2. Populate these columns at the moment of generation, inside the same function call that creates the asset, never as a later manual step.
3. Also log the specific model version used, since prompt behavior can shift between model versions.
4. When any asset (ad, video, email) starts outperforming others, query this table first to see the exact prompt and model combination that produced it.
5. Use the identified winning prompt as the new template or baseline for generating further variations, rather than reverse-engineering it from the asset alone.

**Tools:** Postgres

**Pitfall:** "Nobody ever goes back and adds it later" — if the generating prompt isn't captured at creation time, a breakout-performing asset becomes unreproducible because there's no record of what actually created it.

### 2. Never generate AI content from a single prompt  `20.16`
*core · best practices · source 20*

The most common AI-content mistake is prompting a system with no supporting information/data and letting it fill the gaps itself, producing inaccuracy or shallow research depth. The fix is a genuine human-in-the-loop content strategy: never generate a full piece from a single prompt; instead map the piece to a defined content model, write individual prompts per component/section, and build a custom retrieval index of your own best content — plus curated best-in-class external sources like white papers and PDFs when your own coverage is thin — for the system to pull from via retrieval-augmented generation. Subject matter experts should write the outline and review the output; a plain 'give me the blog post and I'll publish it' request is explicitly called out as the failure mode.

> "you probably should not be doing a piece of content"

**How to do it**

1. Before prompting any AI system for a content draft, assemble supporting source material: your own best existing content plus curated best-in-class external sources (white papers, PDFs) if your own coverage is thin.
2. Have a subject matter expert, not a generalist writer, draft the content outline first, rather than asking the AI to generate an outline from scratch.
3. Break the piece into your defined content model's components (intro, each subheading/section, FAQ, conclusion) rather than requesting the whole piece from one single prompt.
4. Write and run an individual, well-sourced prompt for each component separately, feeding it the specific supporting sources relevant to that section.
5. Where feasible, build a custom retrieval index of your curated source material so the AI can perform retrieval-augmented generation against it rather than relying on general training knowledge alone.
6. Have a subject matter expert review every AI-generated component against the outline and sources before it's assembled into a final draft.
7. Never accept a single-prompt 'give me a 500/1,000-word blog post on this subject' output as publishable as-is.

**Tools:** ChatGPT

**Prompt / template:**

```text
Hey, ChatGPT, give me a 500 or 1,000-word blog post on this subject.
```

**Pitfall:** Prompting a single request for a complete blog post and publishing the output directly — 'you can't just say give me the blog post and publish it,' since unsupported, single-prompt generation skips the sourcing and expert review needed for accuracy and depth.

### 3. Never let an AI publishing agent go live without a human pass  `08.14`
*core · best practices · source 08*

Even with an automated 'humanizing' and AI-tell-removal check built into the content pipeline, the agent (Manus) is never given permission to distribute a press release or publish content on its own — it only creates a draft, which is then manually reviewed and lightly edited before going live (checking the right image, links, and social links are attached). This matters because explicit formatting rules given to the agent aren't reliably followed even after the agent confirms it understands them — a stated example is instructing it not to use an em dash, having it acknowledge the rule, and then having it violate the rule again anyway. For content produced at scale (e.g., dozens of blog posts in one batch), the error rate is higher, so batch output specifically needs dedicated manual QA time rather than assuming per-item quality holds constant.

> "I never have Manus actually distribute a press release on its own"

**How to do it**

1. Configure any AI publishing agent (press releases, blog posts, social copy, etc.) to output to a draft state only — never grant it permission to auto-publish or auto-distribute live.
2. Build an automated 'humanizing'/AI-tell-removal check into the agent's process before content even reaches the draft stage.
3. Give the agent explicit formatting rules (e.g., 'don't use an em dash'), but don't treat its acknowledgment of the rule as proof it will comply.
4. Always perform a manual final read before publishing, even if it's a quick glance rather than a full edit.
5. During the manual pass, specifically verify the correct image is attached, all links resolve correctly, and social media links are correct.
6. For content produced in large batches, budget extra manual QA time specifically for that batch rather than assuming the error rate stays the same as single-item output.
7. Keep this human-review step non-delegated for your highest-value clients or pages, reviewing that content personally rather than assigning it to junior staff.

**Tools:** Manus

**Prompt / template:**

```text
don't use an em dash
```

**Pitfall:** Assuming an AI agent will reliably follow a stated formatting rule — in a direct example the agent confirms compliance ('I'm sorry, em dash won't happen again') and then violates the rule again anyway, so automated checks must be paired with human review, never trusted alone.

### 4. Only point AI at tasks where you already know the desired outcome  `88.6`
*core · ai workflows · source 88*

The author's rule for when AI actually works: you already have expertise, you already know what you want the outcome to be, and you use AI to get there faster or to build something you could not have built before. He contrasts this with the dominant usage pattern, asking AI to write a case study about a client, which he says is how most people use it right now. In his own workflow AI did not know what story to tell or which arguments would resonate; he did. This gives a concrete gate for deciding whether to hand a task to a model. If you cannot state the target output in a sentence before you start, the model will pick a generic target for you and you will not notice it was wrong.

> "which is how most people are using it right now"

**Evidence:** The author reports the AI-assisted case study was sharper and faster than what he could have produced alone, precisely because he defined the story and arguments first.

**How to do it**

1. Before opening the tool, write one sentence stating the outcome you want and the argument the output must support.
2. If you cannot write that sentence, do the research or thinking first; do not delegate the decision.
3. Classify the task: does AI make it faster, or does it make something possible that was not? Only those two qualify.
4. Give the model the raw inputs (data, transcripts, exports) rather than a topic brief.
5. Ask it for analysis, options or components, not the finished artifact.
6. Judge every output against the sentence you wrote at step one and discard anything that drifts from it.
7. Keep the writing, angle and final structure decisions with the human who holds the expertise.

**Pitfall:** Handing a model an open brief like 'write me a case study about X client' produces something plausible that argues nothing. The signal is output you cannot disagree with, because it made no claim strong enough to be wrong.

**Apply at Pabau:** Pabau's /generate and /SEO flows already force a human-approved outline before writing. Hold that gate: no agent starts an article until the angle and the originality nugget are decided by a person.

**Apply anywhere:** Gate every AI task on whether you can state the target outcome in one sentence first. Give the model raw inputs and ask for analysis or components, never the finished argument.

### 5. Operate it before you automate it - and most agents are automations with AI inside  `61.10`
*core · best practices · source 61*

The discipline both hosts insist on. Jordan states it plainly: you need to operate a process before you can automate it. Cody's version is that you can't automate anything if you don't know what outcome you're trying to create or even that it will work - people start by saying they're going to automate, without having a goal to get to. So the sequence is: do things that don't scale, figure out what works, then automate as much of it as possible. What's different now is that instead of linear automation you can have dynamic automations with logic built in - and to him that's all an agent is: a process where the decision that used to be made by a human is now made by AI. Their shared deflation of the category is the useful part: Jordan says most agents are automation with embedded AI, and when you take the word agent out, it's really a human in the loop being presented curated data. Cody says he has talked to hundreds of people and seen two or three things he'd genuinely call an agent - and calls a lot of the rest vaporware. Cody's fully worked example of what a real one looks like: scrape Reddit for pain points about a competitor, generate 100 static ads with an image API, auto-add them to a campaign, have an agent turn off the bottom 90% of performers, promote the winners into a conversion campaign, analyse what the winners have in common, repeat.

> "can't automate anything if we don't know what the outcome"

**How to do it**

1. Define the outcome you're trying to create before designing any automation.
2. Run the process manually until you know it works and know what good output looks like.
3. Write down where a human currently makes a judgement call - those are the only places AI belongs.
4. Automate the mechanical steps first and leave the judgement steps for last.
5. Keep a human in the loop reviewing curated output rather than aiming for full autonomy.
6. Close the loop: feed performance data back in so the next cycle is informed by the last.

**Tools:** OpenAI API

**Pitfall:** Both hosts are describing a field with very few real examples - Cody's count is two or three genuine agents out of hundreds of conversations, so any vendor claim should be read against that base rate.

**Apply at Pabau:** Before Pabau automates any marketing process, someone should have run it by hand long enough to know what a good output looks like - otherwise the automation just produces volume nobody can evaluate.

**Apply anywhere:** Before automating any marketing process, someone should have run it by hand long enough to know what a good output looks like - otherwise the automation just produces volume nobody can evaluate.

### 6. Pull PAA questions from AlsoAsked, draft answers with an exact prompt  `51.1`
*core · ai workflows · source 51*

Edward describes a repeatable AI-assisted pipeline for turning Google's People Also Ask (PAA) box into ranking content. First, gather real PAA questions for your topic using Mark Williams Cook's tool AlsoAsked.com, which pulls questions directly from live Google search results (not guessed or generated) and lets you click into a question to reveal a tree of further related PAA questions; start with only 10-12 of these questions at a time, deliberately going slow so a newer, lower-authority site doesn't trigger a spam-style penalty for scaling too fast. Second, feed all 10-12 questions into Perplexity with a specific prompt asking for roughly 120-word plain-text answers with no citations, returned in a single code block, then manually edit every answer for brand voice, factual accuracy, and to strip out AI writing tells such as em dashes and generic buzzwords.

> "write around 120-word plain text answers for each question returned inside a"

**How to do it**

1. Go to alsoasked.com (built by Mark Williams Cook) and search your target topic to pull real People Also Ask questions directly from Google's live results.
2. Click into individual questions in the AlsoAsked results tree to reveal further related PAA questions and expand your list.
3. Copy only the 10-12 most relevant questions to your topic; do not start with more than that, especially on a newer or lower-authority site.
4. Open Perplexity and paste in all 10-12 questions together in one request.
5. Use the prompt: 'write around 120-word plain text answers for each question returned inside a single code block with no citations.'
6. Copy the returned answers out of the code block.
7. Edit every answer manually for brand voice and factual accuracy before publishing.
8. Remove AI writing tells from each answer, specifically em dashes and generic buzzwords, so it reads as genuinely human-written (inferred: scan for other common AI patterns too).

**Tools:** AlsoAsked.com, Perplexity

**Prompt / template:**

```text
write around 120-word plain text answers for each question returned inside a single code block with no citations
```

**Pitfall:** Starting with more than 10-12 questions at once, especially on a newer site — Edward warns Google penalizes low-authority sites that scale their SEO footprint too fast, so pace the rollout deliberately rather than publishing every PAA question you find at once.

### 7. Put an idempotency key on outreach to stop double-sends  `01.8`
*core · ai workflows · source 01*

The marketing database needs five core tables — leads, outreach, creative_assets, agent_runs, and api_costs — with a unique constraint on `leads.email` and an `upsert_lead` merge function so re-enrichment never errors out. The single most important constraint in the whole system is an idempotency key on the `outreach` table, because agents retry and cron jobs overlap, and without that key the resulting failure mode is emailing the same person multiple times — explicitly called out as the one mistake that actually costs you a customer.

> "emailing the same person four times, which is the one mistake"

**How to do it**

1. Give Claude Code the database-build prompt (see prompt field) to create five core tables: `leads`, `outreach`, `creative_assets`, `agent_runs`, and `api_costs`.
2. On `leads`, add columns for email, name, company, domain, title, source, enrichment_status, verification_status, and a JSONB raw column for whatever the enrichment API returned.
3. Add a unique constraint on `leads.email` and an `upsert_lead` function that merges new data into an existing row instead of throwing an error on conflict.
4. On `outreach`, add lead_id, channel, campaign_id, sent_at, status, and reply_classification columns.
5. Add an idempotency key on the `outreach` table so a retried run can never send the same message twice to the same lead.
6. Add indexes on every foreign key across all five tables.
7. Create a database role for the agents with read/write privileges only, explicitly withholding DROP/DDL permissions.
8. Log every paid API call to the `api_costs` table (provider, endpoint, units, cost_usd, agent, timestamp) inside the same wrapper that makes the call, not as a later add-on.

**Tools:** Claude Code, Postgres

**Prompt / template:**

```text
Set up a Postgres database for our marketing agents and write the schema. Tables: (1) `leads` — email, name, company, domain, title, source, enrichment_status, verification_status, and a JSONB raw column for whatever the enrichment API returned. (2) `outreach` — lead_id, channel, campaign_id, sent_at, status, reply_classification. (3) `creative_assets` — as defined in the object storage step. (4) `agent_runs` — agent, started_at, finished_at, exit_code, actions_taken JSONB. (5) `api_costs` — provider, endpoint, units, cost_usd, agent, timestamp. Requirements: a unique constraint on `leads.email`, an `upsert_lead` function that merges new data into an existing row instead of erroring, an idempotency key on `outreach` so a retried run can't double-send, and indexes on every foreign key. Give the agents a read/write role that cannot DROP anything.
```

**Pitfall:** Without an idempotency key on outreach, agents retrying and cron jobs overlapping will produce the failure mode of emailing the same person four times — called out as the one mistake that actually costs you a customer.

### 8. Require any AI writing tool to read the SERP before it generates  `72.20`
*core · best practices · source 72*

Khanal's second evaluation factor, and one he wants in his own product, is that a tool must analyze search intent and the SERP before writing. His argument as published: if you are producing SEO content, the tool should help you understand who is searching, what problems they have and what is already ranking, and it should read and understand the ranking pages for that query before it generates a single word. He states the failure directly, that a tool going straight from keyword to article has by definition skipped a critically important part of high-quality SEO writing, namely SERP analysis. This is the same discipline he applies manually at the start of the session, elevated into a requirement for any tool in the stack.

> "straight from keyword to article has by definition skipped"

**Evidence:** Khanal built SERP reading into his own tool's brief stage after eight years of doing the analysis manually at his agency.

**How to do it**

1. Before adopting an AI writing tool, ask whether it fetches and reads the live SERP for the target keyword.
2. Check it identifies who is searching and what problems they have, not only which terms to include.
3. Check it surfaces the shared weaknesses of the ranking pages, since that is where your angle comes from.
4. Reject tools that map keyword to article with no retrieval step in between.
5. Distinguish on-page optimizers that grade a draft against ranking pages from tools that analyze the SERP before writing.
6. If your tool cannot do it, run the SERP read manually and paste the findings into the brief.
7. Confirm the generated outline actually reflects the SERP findings rather than restating the keyword.

**Pitfall:** Confusing term-grading with SERP analysis. Khanal separates tools whose DNA is telling you which terms and entities to include from tools that read what is ranking and why before writing.

**Apply at Pabau:** Pabau's generation pipeline already pulls SERP data. Make it a hard gate: no outline is approved unless the ranking pages' formats, pain points and shared weaknesses are in the brief.

**Apply anywhere:** Require any AI writing tool in your stack to fetch and analyze the live SERP before generating, and treat keyword-to-article tools with no retrieval step as unfit for SEO content.

### 9. Right context at the right time beats stuffing the window - and fewer tools beat more  `56.21`
*core · best practices · source 56*

Asked how to avoid hallucinations, Cody says the right context at the right time is the most important thing, and describes learning it the hard way: they started by stuffing the entire ontology into the context and telling the agent to figure it out. What worked better was a tool that holds the ontology and pulls in only the pieces needed for the current decision - implemented with a vector database over the mapped information. He personifies it deliberately as an explanatory device: give a human everything at once and tell them to work, and they're overwhelmed; he sees the same pattern in the output quality. The paired finding is tool count: 'the more tools you have, the worse it gets', so the question becomes what is the least number of tools that still produces the outcome. He cites an interview with the Claude Code lead saying they are very deliberate about tools and try at all costs not to ship more, only doing so when it's 100% necessary.

> "right context at the right time is the most important"

**How to do it**

1. Stop loading your whole knowledge base or schema into the context window as a default.
2. Map the information once - definitions, relationships, how sources relate to each other - as a retrievable structure.
3. Put it behind a retrieval tool (vector database) the agent calls for just the pieces it needs at the moment it needs them.
4. Count the tools your agent has and ask what the minimum set is that still produces the outcome.
5. Remove tools and re-test rather than adding tools when quality drops.
6. Watch where the agent actually fails and feed those specific cases back as examples, rather than adding more general context.

**Tools:** Claude Code

**Pitfall:** The instinct when an agent gets something wrong is to give it more context and more tools. Both of his findings point the other way, and he treats the reduction as the optimisation he is always doing.

**Apply at Pabau:** Any Pabau agent - content, reporting, link auditing - should retrieve from a structured knowledge source on demand rather than being handed the whole style guide and data schema up front, and should be given the smallest tool set that does the job.

**Apply anywhere:** Any agent you build - content, reporting, link auditing - should retrieve from a structured knowledge source on demand rather than being handed the whole style guide and data schema up front, with the smallest tool set that does the job.

### 10. Run Claude Code headless in Docker with a hard timeout  `01.5`
*core · ai workflows · source 01*

Claude Code can run headless via `claude -p "prompt"` with no TTY, which is the mechanism that lets it execute inside a container on a schedule indefinitely rather than only when a human is watching a laptop. The runtime needs a persistent volume mounted at `/data` (container filesystems alone don't survive redeploys), a hard 30-minute wall-clock timeout per run to stop a stuck retry loop from silently burning tokens for hours, and a `runs` table logging every execution so a slow-moving metric change can be traced back to exactly what an agent did on a specific day.

> "The persistent volume is the difference between an agent and a goldfish"

**How to do it**

1. Run Claude Code headless using `claude -p "prompt"` (no TTY needed), which allows execution inside a container on an unattended schedule.
2. Give Claude Code the runtime-build prompt (see prompt field) to Dockerize this on a Node base image with the Claude Code CLI installed and `ANTHROPIC_API_KEY` read from the environment.
3. Structure an `/agents` directory where each agent is its own folder containing a `CLAUDE.md`, a `.claude/skills/` directory, and a `run.sh` entrypoint.
4. Build a container entrypoint that accepts an agent name, runs that agent headless, and streams stdout to the container logs.
5. Mount a persistent volume at `/data` so caches, cursors, and state written between runs survive redeploys.
6. Enforce a hard wall-clock timeout of 30 minutes per run that kills the process and sends an alert if exceeded.
7. Write one row per run to a `runs` table recording agent name, start time, end time, exit code, tokens used, and a summary of actions taken.
8. On any non-zero exit, post the agent name and the last 50 lines of output to Slack.
9. Deploy to Railway for the fastest path, Fly.io if proximity to users matters, or a $20/month Hetzner box with Docker Compose as the cheapest option.

**Tools:** Claude Code, Docker, Railway, Fly.io, Hetzner, Slack

**Prompt / template:**

```text
Build a Dockerized runtime for headless Claude Code agents and deploy it to Railway. Requirements: (1) Node base image with the Claude Code CLI installed and an ANTHROPIC_API_KEY from env. (2) An `/agents` directory where each agent is a folder with its own `CLAUDE.md`, `.claude/skills/`, and a `run.sh`. (3) An entrypoint that takes an agent name, runs it headless inside the container, and streams stdout to the container logs. (4) A persistent volume mounted at `/data` for caches, state files, and anything the agent writes between runs. (5) A hard wall-clock timeout per run — kill at 30 minutes and alert. (6) Every run writes a row to a `runs` table: agent name, start time, end time, exit code, tokens used, and a summary of actions taken. (7) On non-zero exit, post the agent name and last 50 lines of output to Slack.
```

**Pitfall:** Without a persistent volume, state like enrichment caches and 'which leads have I already emailed' is lost on every redeploy since container filesystems don't retain it; without a hard timeout, an agent stuck in a retry loop against a rate-limited API will keep burning tokens for hours unattended.

### 11. Run a data-driven case study end to end with AI instead of a three-person team  `88.1`
*core · ai workflows · source 88*

The Grow and Convert author describes building a client case study alone that previously needed an analyst, a designer and a writer. He started with spreadsheets of conversion data broken out by month and by individual article, had AI analyze them and surface patterns he would not have spotted by hand, then had AI build the data visualizations his designer used to make. He also queried Ahrefs for the keywords the client ranked for before and after the engagement and used AI to analyze the shift. He never asked AI to write the case study. He decided the story and the arguments; AI removed the resource constraint that made that depth impractical. He says the analysis would have been less thorough and the arguments less sharp without it.

> "I built data visualizations that previously would have required our designer"

**Evidence:** The finished analysis showed every keyword the client previously ranked for was informational and top-of-funnel, while the keywords the agency won were almost entirely buying-intent.

**How to do it**

1. Export the conversion or revenue data you already hold, broken out by month and by individual page or article, into a CSV.
2. Decide the story and the argument yourself before opening any AI tool; write the thesis in one sentence.
3. Upload the CSV and ask the model to surface patterns, outliers and correlations you did not ask about, not to summarize the file.
4. Pull the client or site's ranked keywords from Ahrefs for a date before the engagement and a date after, and export both.
5. Ask the model to classify each keyword by intent (informational, commercial, transactional) and report the before/after mix.
6. Have the model generate the chart code (HTML/CSS or a plotting library) for the two or three patterns that support your thesis.
7. Write the narrative yourself, dropping in the charts and the quantified conversion impact.
8. Fact-check every figure the model reports back against the source spreadsheet before publishing.

**Tools:** Ahrefs, ChatGPT

**Pitfall:** Asking the model to write the case study rather than to analyze the data. The author is explicit that AI did not know what story to tell or which arguments would land; models handed a raw brief invent a generic narrative and sometimes misread the numbers, so every figure needs checking against the source file.

**Apply at Pabau:** David has months of Pabau conversion and demo-booking data by article sitting unused. Run this on the pabau.com blog: export per-article conversions by month, have AI find the pattern, then publish the result as a case-study or data post with original charts, which also satisfies the one-original-visual rule.

**Apply anywhere:** Run this on your own performance data: export per-page conversions by month, have AI find the pattern you would have missed, generate the charts, and publish the analysis as an original data piece. You decide the story; AI only removes the analyst and designer bottleneck.

### 12. Run the whole SEO content loop as a five-stage agent  `77.1`
*core · ai workflows · source 77*

Cody Schneider describes an agent that runs organic content end to end for an AI startup, and the value is that it is one continuous loop rather than a set of disconnected prompts. The five stages are: research bottom-of-funnel keywords through a keyword data API, research the topic by scraping page one of the live SERP, write the article from that scraped research, publish it straight into the CMS over the API, then re-enter the same article on a 30-day cycle and refresh it against live performance data. Nothing in the chain hands a document to a human between stages. The design point is that publishing is not the end state; the refresh stage closes the loop and turns the agent into something that maintains a library rather than one that only adds to it.

> "Then writes the article based on research"

**Evidence:** Schneider says the pipeline is live for an AI startup and is sold as a product at graphed.com.

**How to do it**

1. Stand up one agent with five ordered stages rather than five separate prompt sessions.
2. Stage one: query a keyword data API for bottom-of-funnel keywords tied to the product's service offering.
3. Stage two: scrape page one of Google for the chosen keyword and pass the scraped pages in as the research corpus.
4. Stage three: write the article strictly from that scraped research, not from model memory.
5. Stage four: POST the finished article to the CMS over its REST API rather than pasting it in.
6. Stage five: schedule the same article for re-entry 30 days after publication.
7. Store the keyword, the URL and the publish date in a state file so the refresh stage knows what is due.
8. Insert a human review gate before stage four, which Schneider's description omits and which the rest of this base treats as mandatory.

**Tools:** DataForSEO, Serper, Strapi, Google Search Console

**Pitfall:** Schneider's chain has no human checkpoint anywhere between keyword and live URL. Fully autonomous publishing is the single most common way these pipelines produce the fast-rank-then-crash pattern; the signal is a batch of pages that all gain impressions in week two and lose them by week six.

**Apply at Pabau:** Pabau could wire the same five stages for /blog/ and /templates/ pages, but the publish stage must write a WordPress draft, not a live post, so the factcheck-flow guides and the block contract are applied by a human before anything goes public.

**Apply anywhere:** Build your content automation as one loop with a refresh stage, not a chain that ends at publish. Keep the publish step writing drafts so a person applies house style and checks facts before the page goes live.

### 13. Sync GTM data hourly into a warehouse via dlt  `01.3`
*core · ai workflows · source 01*

Rather than letting an agent hit live marketing APIs whenever it needs data, build a scheduled pipeline that pulls from every go-to-market source on a schedule and lands it in the same shape every time, using the open-source Python library dlt as the connector layer (about 20 lines of code per source) since heavier options like Airbyte (350+ connectors, has a UI) or Meltano/Singer cost more setup time. The pipeline should run hourly, since ad platforms' and CRMs' own conversion data already lags by a few hours, so syncing more frequently buys nothing but wasted API calls.

> "pagination, token expiry, and schema drift will eat your entire build"

**How to do it**

1. Install the dlt Python library (`pip install dlt`) as the connector framework for the pipeline.
2. Give Claude Code the full data-pipeline prompt (see prompt field) naming every GTM source to sync: Facebook Ads, Google Ads, GA4, Stripe, and HubSpot.
3. Require incremental loading with a state file so each run pulls only new rows instead of re-pulling all history.
4. Require one schema per source plus a `_synced_at` timestamp column on every table.
5. Require retry logic with exponential backoff specifically on HTTP 429 and 5xx responses.
6. Package the whole pipeline as a single job runnable via cron.
7. Require that any failure posts the source name and error message to a Slack webhook and exits non-zero.
8. Schedule the job hourly rather than more frequently, since ad-platform and CRM conversion data lags by a few hours regardless.
9. If a needed source lacks a dlt connector, evaluate Airbyte (350+ prebuilt connectors, has a UI) or Meltano/Singer instead. (inferred)

**Tools:** Claude Code, dlt, Airbyte, Meltano, Facebook Ads API, Google Ads API, GA4, Stripe, HubSpot, Slack

**Prompt / template:**

```text
Set up a data pipeline that syncs our GTM sources into a warehouse hourly. Use dlt (the open source Python library) for the connectors. Sources: Facebook Ads (campaigns, adsets, ads, daily insights at the ad level), Google Ads (campaigns, keywords, search terms report, daily metrics), GA4 (sessions, source/medium, landing page, conversions), Stripe (customers, subscriptions, invoices), and HubSpot (contacts, deals, deal stage history). Requirements: incremental loading with a state file so we only pull new rows, one schema per source, a `_synced_at` column on every table, and a retry with exponential backoff on 429s and 5xxs. Write the whole thing as a single job I can run on a cron. On failure, post the source name and error to a Slack webhook and exit non-zero.
```

**Pitfall:** Re-pulling all of history on every run instead of loading incrementally will blow through API quotas by week two, and the sync will eventually take longer to run than the interval between syncs.

### 14. The seven-piece infrastructure stack behind a real agent factory  `01.2`
*core · ai workflows · source 01*

The gap between a Claude Code demo and a working autonomous agent is exactly seven pieces of infrastructure: a data pipeline, a data warehouse, a runtime, object storage, a database, scheduled cron agents, and an API gateway. The author's claim is that once these seven pieces are wired together (roughly a weekend of work), every subsequent agent becomes 'just a config file' rather than a new build — the entire point of the factory metaphor is that the infrastructure is built once and reused.

> "difference between a demo and an agent is seven pieces of infrastructure"

**How to do it**

1. Install Claude Code globally via `npm install -g @anthropic-ai/claude-code` and obtain an Anthropic API key.
2. Provision a place to run containers — Railway, Fly.io, or a $20/month Hetzner box.
3. Provision a Postgres database to serve as agent memory/state.
4. Provision S3-compatible object storage — Cloudflare R2, AWS S3, or Backblaze B2.
5. Obtain API keys for every generation, enrichment, and outreach provider you'll actually use (e.g., Kie AI or fal.ai for Nano Banana/Seedance, Apify, Apollo, Million Verifier, Instantly).
6. Create a Slack workspace with an incoming webhook for run alerts and digests.
7. Block out one weekend to wire the seven pieces together end-to-end: pipeline, warehouse, runtime, object storage, database, cron, and gateway.
8. Once built, treat every new agent afterward as a config file added on top of the shared infrastructure rather than a fresh build.

**Tools:** Claude Code, Railway, Fly.io, Hetzner, Postgres, Cloudflare R2, AWS S3, Backblaze B2, Kie AI, fal.ai, Apify, Apollo, Million Verifier, Instantly, Slack

**Pitfall:** Most people 'run Claude Code on their laptop, get one great output, post a screenshot, and then the laptop closes' — without the shared infrastructure, nothing runs on a schedule, writes to a database, or can be re-run tomorrow, so it never becomes a real system.

### 15. The ten-minute GTM engineering setup: a folder, an .env, and a CLAUDE.md  `63.1`
*core · ai workflows · source 63*

Cody's crash course reduces the whole setup to two files. Create a working folder, then get Claude Code to create an environment file where every API key for your entire stack is stored, and a CLAUDE.md instructing it that whenever you provide a new API key, it should add it to that environment file so the keys accumulate and get reused. That's the entire infrastructure requirement. He works from the terminal rather than the desktop app specifically so he can have multiple windows open at once and jockey between them - his working pattern is five terminals open, conducting agents. His definition of what changes: GTM engineering is all the middle work you previously did hands-on-keyboard, handed to the agent, so your role becomes having ideas and being the polish at the endpoint. He also uses dictation (Superwhisper, option-space) rather than typing the instructions.

> "the first thing that you need to do is build a folder"

**How to do it**

1. Create a dedicated folder for your go-to-market work and cd into it in a terminal.
2. Run Claude Code inside that folder.
3. Ask it to create an environment file in the directory for your API keys.
4. Ask it to create a CLAUDE.md containing the instruction that any API key you provide should be added to the environment file for future reuse.
5. Add keys as you go, one per tool in your stack, so the folder becomes your whole marketing stack.
6. Work from the terminal rather than a desktop app so you can run several sessions in parallel.
7. Use dictation to give instructions - he uses Superwhisper on option-space - since instructions get long.

**Tools:** Claude Code, Superwhisper

**Prompt / template:**

```text
Make an environment file for me within this directory. Also add a CLAUDE.md file and include instructions in it that any time I provide an API key, you add that key to the environment file so it can be used in the future as well.
```

**Pitfall:** A single environment file holding every API key for your entire stack, in a directory an agent can read, is a large blast radius - keys should be scoped to the minimum permissions the task needs.

**Apply at Pabau:** This is the cheapest possible starting point for Pabau: one folder, one env file with read-only keys, and a CLAUDE.md - and it's worth doing with scoped read-only credentials first before anything with write access.

**Apply anywhere:** This is the cheapest possible starting point - one folder, one env file, and a CLAUDE.md - and it's worth doing with scoped read-only credentials first, before anything with write access.

### 16. Use Claude + GSC query gaps to add new H2s  `31.1`
*core · ai workflows · source 31*

The core workflow: in Google Search Console's Performance report, click Pages to sort by most-clicked pages, pick one to expand, open its query report, and export the full CSV of queries it currently ranks for. Paste the full article plus that CSV into Claude with a specific prompt asking it to find keyword clusters with meaningful impressions that the article doesn't cover well, and to suggest new H2 sections that would let the page rank for more of the queries it's already partially matching. The process is deliberately split into two Claude turns - first request just the top suggested H2 and where to insert it without writing content, then approve the placement before asking Claude to write the section - and repeated two to three times per session to add multiple new sections to the same article.

> "identify keyword clusters with meaningful impressions that aren't well covered"

**How to do it**

1. In Google Search Console, open the Performance report and click Pages (next to Queries) to see pages sorted by most clicks.
2. Pick one high-performing page you want to expand.
3. Click into that page's report to see every query it currently ranks for, then click Export and download the CSV.
4. Open a new Claude chat, paste in the full existing article text, attach the exported GSC query CSV, and use the prompt: "I'm attaching my article and a CSV of Google Search Console queries it currently ranks for. Analyze the queries against the article's existing content, identify keyword clusters with meaningful impressions that aren't well covered in the article, and suggest new H2 sections to add so the article can rank for more of the queries it's already partially matching."
5. From Claude's suggestions, ask for just the first H2 plus where to insert it, explicitly adding "Don't write the rest of the content yet" so you can approve placement before full copy is generated.
6. Once satisfied with the placement, have Claude write the full section content.
7. Heavily edit Claude's draft before publishing rather than pasting it in as-is.
8. Repeat the prompt-and-approve cycle to add two to three total new H2 sections to the article in one session.

**Tools:** Google Search Console, Claude

**Prompt / template:**

```text
Prompt 1 (attach article + GSC query CSV): "I'm attaching my article and a CSV of Google Search Console queries it currently ranks for. Analyze the queries against the article's existing content, identify keyword clusters with meaningful impressions that aren't well covered in the article, and suggest new H2 sections to add so the article can rank for more of the queries it's already partially matching." Prompt 2 (after reviewing suggestions): "Okay, give me the first H2 to add and tell me where to insert it. Don't write the rest of the content yet."
```

**Pitfall:** Letting Claude write a new section before you've confirmed exactly where it will be inserted risks content that doesn't fit its surrounding context - asking for the placement first, and generating full copy only after approving where it goes, keeps each new section contextually consistent with what's around it.

### 17. Write Claude skills as goals, not fixed steps  `16.8`
*core · ai workflows · source 16*

The recommended way to avoid re-prompting Claude or Codex from scratch for recurring tasks is to convert a repeated prompt into a skill, but the skill itself should be written as a goal, a definition of what success looks like, and the necessary context — explicitly not as a rigid "do this, then do this" instruction sequence. The stated reasoning is that as underlying models improve, the best process for achieving any given goal keeps changing, so hard-coding today's process into a skill "hobbles" future performance; a smarter model will find a better process on its own as long as it clearly understands the goal and has the context it needs. This reframes skill-writing as specification-writing (define the destination and constraints) rather than script-writing (define the exact route).

> "don't write a prompt twice, make a skill"

**How to do it**

1. Notice when you've sent essentially the same prompt to Claude/Codex more than once for a recurring task.
2. Instead of reusing the raw prompt text, ask Claude to convert that request into a reusable skill.
3. Draft the skill as a goal, a definition of success, and all relevant context (data sources, examples, edge cases) — not as a numbered procedure.
4. Run the skill on a real task and review the output in detail.
5. Give specific feedback on what was wrong or missing rather than just re-running it unchanged.
6. Ask Claude to update the skill based on that feedback so it performs better next time.
7. Repeat the run-feedback-update cycle across multiple real uses so the skill accumulates edge cases and context.
8. When a new model version ships and behavior visibly changes, re-run and refine the skill again rather than assuming identical performance (inferred).

**Tools:** Claude Code, Codex

**Pitfall:** Writing a skill as a fixed, numbered procedure locks in today's best method and prevents a smarter future model from finding a better one — the fix is specifying the goal and success criteria, not the steps.

### 18. Write the process down before you automate any of it  `46.e7`
*core · best practices · source 46 · universal-edition only*

Tallent, who now runs an AI change-management company, says the bulk of that work is helping companies identify and write down their processes before they ever touch an AI tool. The sequence he describes for a team is: get hiring and onboarding right (worth 70-80% of later headache avoided), then set decision rights and information flows, then standardize knowledge storage on one platform — and only then ask which projects are worth automating. The interviewer corroborates it with a second-hand account from someone who moved into automation consulting and concluded that most companies do not actually need it, because they either do not know what should be automated or lack a process coherent enough to automate.

> "let's write down those processes before you ever even touch AI tools"

**How to do it**

1. Pick the workflow you want to automate and write it down end to end, by hand, before evaluating any tool.
2. Confirm the process is stable enough that a colleague could pick it up cold if the owner were out sick.
3. Fix hiring and onboarding first if those are the unwritten processes — they compound into everything else.
4. Settle decision rights and where knowledge is stored before adding automation on top.
5. Only then triage which of the written processes are genuinely worth automating, and which are not.
6. Treat 'we want to do this with AI' without a written process as a signal to stop and document.

**Tools:** Notion, Claude, Spreadsheet (Sheets/Excel)

**Pitfall:** Buying tooling to paper over an undocumented process — you cannot automate a workflow that is not written down or commonly understood, and the automation will encode the confusion.
