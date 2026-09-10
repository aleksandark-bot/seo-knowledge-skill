# AI Workflows & Agents — core (part 1 of 2)

18 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. A short, plain ChatGPT prompt beat a long, data-rich one for titles  `19.12`
*core · ai workflows · source 19*

To generate episode titles, the host switched from writing them himself to feeding the full episode transcript into ChatGPT with a very short, plain prompt, and reports the AI-generated titles performed "a huge amount better" than his own, after switching roughly a year and a half prior. Critically, he has to turn personalization off in ChatGPT before running this, because otherwise it draws on feedback from past conversations and gets "too informed by that," producing a worse result. He separately tested giving ChatGPT a much longer, thorough prompt loaded with historical show performance data, and found that more elaborate prompt performed worse than the very short one. Sometimes the short prompt one-shots a great title immediately, other times it takes several tries or up to 20 minutes of refinement, but the short version is still his standing approach for every daily episode.

> "My prompt is disgustingly simple"

**How to do it**

1. Export or copy the full raw transcript of the content you want a title for.
2. Open ChatGPT and turn off personalization or memory features before submitting the prompt, so past-conversation feedback doesn't skew the output.
3. Paste the transcript into the chat along with a short, plain-language prompt describing the content and its distribution channels.
4. Read the generated title suggestion or suggestions and judge whether one "one-shots" a usable title immediately.
5. If no suggestion works, re-run or refine the prompt conversationally rather than expanding it into a long, detailed brief with historical data.
6. Cap your iteration budget, sometimes up to about 20 minutes, before either picking the best option so far or trying a fresh short prompt.
7. Avoid the temptation to feed ChatGPT a longer, more thorough prompt with performance history and analysis, since that was tested and found to perform worse than the short version.

**Tools:** ChatGPT

**Prompt / template:**

```text
I have a daily SEO podcast, this is the transcript for the podcast I just recorded, give me a title for it. The podcast comes out on YouTube, Spotify, and Apple Podcasts. YouTube is especially important. Give me a title for it.
```

**Pitfall:** Leaving ChatGPT's personalization or memory turned on causes it to lean on feedback from unrelated past conversations and get too informed by that, producing a worse title; likewise, expanding the prompt into a long, thorough brief with historical performance data was tested and performed worse than the short version.

### 2. Build a persistent brand brief so the model stops forgetting your product  `72.18`
*core · ai workflows · source 72*

Khanal's stated reason for building a separate tool rather than using a Claude project is that projects forget. He says stuff you put into Claude projects eventually starts to forget, and that this was the frustration he heard back from Reddit commenters too: you create a project, you give it all these instructions, and it does not actually do them. His answer is a persistent brand document generated once from real source material, then reused on every piece. The sources are not marketing copy: sales demo call transcripts and similar recordings. The document is structured to cover named things, an explanation of what the product is, the features that matter, customers and use cases, differentiators, and competitors and alternatives. That brief is then combined with fresh SERP analysis per keyword.

> "Eventually, it starts to forget"

**Evidence:** Khanal cites Reddit commenters saying a trained ChatGPT 'never listens to my writing instructions' as the same problem his tool was built to solve.

**How to do it**

1. Collect real source material about the product: sales demo call transcripts, support threads, founder interviews.
2. Generate a brand summary from those sources with a fixed structure rather than a free-form summary.
3. Require the structure to cover what the product is, features that matter, customer types and use cases, differentiators, and competitors and alternatives.
4. Store that summary as a versioned file, not as chat context that decays across a session.
5. Attach the file explicitly at the start of every writing job rather than relying on project memory.
6. Combine it per article with fresh SERP analysis for that specific keyword.
7. Re-generate the summary when the product changes, and diff it so stale claims do not persist.

**Tools:** Claude

**Pitfall:** Relying on a chat project's persistent instructions. Khanal and the Redditors he quotes report the same failure: instructions are given, appear accepted, and are silently ignored later in the session.

**Apply at Pabau:** Pabau should maintain a versioned brand brief file covering products, pricing model, differentiators and competitors, drawn from demo calls, and attach it to every article-generation run rather than depending on project instructions.

**Apply anywhere:** Maintain a versioned brand brief generated from real sales and support material, covering product, features, customers, differentiators and competitors, and attach it explicitly to every writing run instead of trusting project memory.

### 3. Build a two-URL Claude Code/Codex agent to test visual chain-of-reasoning  `25.9`
*core · ai workflows · source 25*

Koray recommends building a minimal AI agent using Codex or Claude Code that takes just two URLs as input (e.g., your page vs. a competitor's) and compares how the agent 'perceives' them visually and functionally, not just via their text. He prompts the agent with something like 'just give me the predicates that can be performed on that page,' asking it to enumerate the concrete actions/functions available on each page (e.g., 'read the reviews,' 'compare the products,' 'check the pricing changes') — a metric he calls 'verbalization metrics,' detailed further in a talk he gave in Lithuania. The purpose is to reverse-engineer what an AI agent's chain of reasoning concludes about a page purely from its visual/interactive layout (buttons, sliders, input fields) even with little or no body text, since this is how agentic retrieval systems evaluate pages, not only via keyword-matched text.

> "give it two URLs, and see how the agent perceives"

**How to do it**

1. Open Claude Code or Codex and start a new minimal agent session.
2. Provide the agent with exactly two URLs: your target page and a direct competitor's equivalent page.
3. Prompt the agent to visit both pages and compare them using the prompt: 'just give me the predicates that can be performed on that page' for each URL.
4. Ask the agent to specifically list the distinct functions or actions available on each page (e.g., read reviews, compare products, check pricing, book a demo).
5. Record the count and type of distinct actions/predicates the agent identifies for your page versus the competitor's page.
6. Identify functions the competitor's page signals that yours doesn't (e.g., competitor page offers 'compare pricing' but yours doesn't visually surface that function).
7. Add or make more visually prominent the missing functions/predicates on your page (larger buttons, clearer interactive elements) so an agent parsing the page recognizes those actions.
8. Re-run the same two-URL agent comparison after making changes to confirm the agent now reports the new predicate/function as present on your page (inferred verification step).

**Tools:** Claude Code, Codex

**Prompt / template:**

```text
just give me the predicates that can be performed on that page
```

**Pitfall:** Evaluating pages only on text/keyword content and ignoring that AI agents parse visual and interactive elements (buttons, sliders, input areas) as functional signals — a page can lose an agentic comparison purely on missing visual affordances even if its written copy is strong.

### 4. Build six narrow single-purpose agents, not one broad one  `01.9`
*core · best practices · source 01*

The article explicitly warns against building a single monolithic 'marketing agent' that handles ads, email, and SEO together — the rule is one job, one scope per agent, each running on its own schedule, because narrow agents are the only kind whose impact you can actually attribute: when a metric moves, you can tell exactly which agent moved it. This also draws the line between 'a tool' (something that only runs when a human types a request) and 'an employee' (something that runs autonomously on a cron schedule).

> "Narrow agents are the only kind you can actually judge"

**How to do it**

1. List every distinct marketing job you want automated (e.g., ad creative generation, lead enrichment, cold-email sending, SEO/analytics reporting).
2. For each job, define a single, narrow scope, resisting the urge to combine two related jobs into one agent.
3. Give each narrow agent its own folder, its own `CLAUDE.md`, and its own cron schedule rather than sharing one agent across jobs.
4. When a business metric moves (cost per lead, reply rate, ranking), check the logs of the one specific narrow agent responsible rather than a shared multi-purpose agent.
5. Only consider consolidating agents after each has been validated individually, if consolidation later proves necessary. (inferred)

**Pitfall:** A single broad 'marketing agent' handling ads, email, and SEO together makes it impossible to tell which function caused a given metric to move, defeating the ability to debug or improve any one part of it.

### 5. Chain a review-monitoring, SEO, and writer agent into one content pipeline  `28.13`
*core · ai workflows · source 28*

The team's agentic content-production loop chains multiple specialized agents: a reviews-monitoring agent watches incoming app reviews for recurring questions or pain points, flags the pattern to an SEO agent, which evaluates whether it's a viable content opportunity and hands a brief to a dedicated content-writer agent that drafts the piece, after which a human or brand check confirms it's on-brand, useful, and targets the intended terms before publishing. Beyond production, they describe an emerging second loop using a frontier model to autonomously monitor published-article performance, generate a hypothesis for why a piece is under- or over-performing, and design an A/B test, serving one article variant to part of the audience and the original to the rest, then checking results after two weeks — something that only started working reliably with the newest available model as of the recording.

> "tells the agent responsible for SEO that this is"

**How to do it**

1. Set up a reviews-monitoring agent with access to your app or product review feed, prompted to flag recurring questions or pain points that could become content topics (inferred: run on a daily or weekly cadence).
2. Set up an SEO-evaluation agent that receives flagged topics from the reviews agent and assesses viability, such as whether it fits content strategy or would support existing content.
3. Set up a content-writer agent that receives an approved brief from the SEO agent and drafts the full article, following your brand and style guidelines as context.
4. Insert a mandatory human or in-market partner review step before publishing to confirm the draft is on-brand, factually sound, and correctly targets the intended terms.
5. After publishing, monitor the article's performance in Google Search Console and Analytics on a recurring basis rather than treating publish as the final step.
6. For underperforming articles, prompt a capable model to analyze likely causes and propose a specific, testable hypothesis for why the piece isn't gaining the expected traffic or topical authority.
7. Where the model proposes a hypothesis, set up a simple A/B test, such as variant article B to a percentage of traffic and original A to the rest, and check results after a fixed window like two weeks to confirm or reject the hypothesis.
8. Feed confirmed learnings back into future briefs for the SEO and writer agents so the pipeline improves over successive cycles (inferred).

**Tools:** Claude, Google Search Console, Google Analytics

**Pitfall:** Expecting this fully autonomous monitor-hypothesize-test loop to work with any model — it reportedly did not work with earlier models and only started working reliably with the newest model available at time of recording, so treat this as an emerging capability to pilot, not yet a guaranteed workflow.

### 6. Document every warehouse table's meaning before agents query it  `01.4`
*core · ai workflows · source 01*

The real value of a data warehouse isn't the database itself but the schema documentation sitting next to it — an agent handed dozens of raw tables will write a query that looks correct and returns garbage (e.g., summing a per-ad-per-day `spend` field across a join without knowing that's what it represents). The fix is a `SCHEMA.md` file, written for the agent to read before writing SQL, that documents every table, every column, every join key, and the company's actual internal definitions (what counts as a qualified lead, how MRR is computed on a downgrade), backed by a dbt project and an automated spend-reconciliation test as an early-warning smoke alarm.

> "The real unlock isn't the database, it's the schema documentation"

**How to do it**

1. Stand up ClickHouse as the analytics warehouse (fast, columnar, free to self-host; DuckDB works under a few hundred million rows single-node, Postgres is fine to start).
2. Give Claude Code the warehouse prompt (see prompt field) to create a raw database for pipeline output and a separate analytics database for modeled tables.
3. Require a `paid_performance` table unioning Facebook Ads and Google Ads into one row per channel per campaign per day (spend, impressions, clicks, leads, revenue).
4. Require a `pipeline_daily` table joining HubSpot deals to their originating channel via UTM.
5. Write a `SCHEMA.md` documenting every table, every column, the join keys, and internal definitions (e.g., the exact criteria for a 'qualified lead,' the exact MRR calculation on a downgrade).
6. Add a dbt project so all transformations are versioned and testable.
7. Add an automated test that fails if yesterday's total ad spend computed in the warehouse differs from the platform's own UI by more than 2%.
8. Treat SCHEMA.md as required reading the agent consumes before writing SQL, not human-facing documentation, and keep it updated as tables change.

**Tools:** Claude Code, ClickHouse, DuckDB, Postgres, dbt

**Prompt / template:**

```text
Set up ClickHouse as our warehouse and model the raw pipeline tables into an analytics layer. (1) Create a raw database for pipeline output and an analytics database for modeled tables. (2) Build a `paid_performance` table: one row per channel per campaign per day, with spend, impressions, clicks, leads, and revenue, unioned across Facebook Ads and Google Ads so I can query all paid in one place. (3) Build a `pipeline_daily` table joining HubSpot deals to their originating channel via UTM. (4) Write a `SCHEMA.md` that documents every table, every column, the join keys between them, and our internal definitions — a qualified lead is a demo booking with a company email and a live website; MRR is Stripe active subscriptions at end of day. (5) Add a dbt project for the transformations so they're versioned and testable. Include a test that fails if yesterday's total ad spend differs from the platform UI by more than 2%.
```

**Pitfall:** An agent handed 40 raw, undocumented tables will write a query that 'looks right and returns garbage' — e.g., summing a per-ad-per-day spend field across a join without knowing that's what it is — so definitions must be written down explicitly rather than assumed to be obvious.

### 7. Duplicate instructions and disable chat memory to cut hallucinations  `27.2`
*core · best practices · source 27*

To reduce hallucination rates in SEO agent work, the speaker describes a specific trick: type your instructions, then literally duplicate and paste them a second time in the same prompt — for reasons that aren't fully understood, LLMs respond to the repeated instructions with a measurably lower hallucination rate. He also recommends testing a lower-cost, non-frontier model (naming DeepSeek or MiniMax) instead of a frontier model for a given task, since a cheaper model sometimes produces a more accurate result while also saving money. Separately, to avoid "context poisoning" — where old, irrelevant, or wrong information distorts an agent's read of current intent — he recommends turning off chat memory/recall features entirely, since they silently pull in prior context that shifts the model's probability field away from the task at hand.

> "duplicate it, paste it twice, the hallucination rate drops"

**How to do it**

1. Before sending a task prompt to an agent, write your full instructions once as normal.
2. Copy that same block of instructions and paste it a second time immediately after the first, so the prompt contains the instructions twice.
3. Send the doubled prompt and compare output against a single-pass version on the same task to confirm the hallucination rate drops for your use case (inferred verification step).
4. For tasks that are mainly retrieval or tool-calling rather than complex reasoning, swap the frontier model out for a cheaper model such as DeepSeek or MiniMax and compare accuracy and cost.
5. In your chat platform, locate the memory/recall or persistent-context setting and turn it off for agent work.
6. Start each new agent task in a fresh chat rather than continuing a long-running thread, so unrelated prior context can't leak in and poison the current task.

**Tools:** ChatGPT, DeepSeek, MiniMax

**Pitfall:** Leaving chat memory/recall turned on lets old, unrelated context quietly distort the probability field for a new task — described as "context poisoning" — so agent work should start clean rather than continuing inside a memory-enabled thread.

### 8. Edit every AI keyword suggestion for specificity before using it  `11.14`
*core · best practices · source 11*

Gotch positions himself as 'an editor' of AI-suggested keywords rather than an accepter of them at face value: AI tools reliably surface reasonable seed topics but miss the query-craft nuances an experienced practitioner would catch, such as tightening a generic seed like 'B2B SEO St. Louis' into 'best B2B SEO agencies in St. Louis,' or extending a short query into a longer variant specifically to capture additional longtail traffic the shorter version would miss. He warns that people avoid tweaking AI-suggested queries because doing so changes the reported search volume number, but argues that's the wrong thing to optimize for — query and intent correctness matters more than preserving a volume figure.

> "Only someone with experience can see these details"

**How to do it**

1. Treat every keyword list generated by an AI tool such as ChatGPT, Claude, or Perplexity, or a vendor's built-in AI, as a first draft, not a final list.
2. For each suggested query, check whether it's phrased with enough specificity or intent, such as adding 'best' or a qualifier, rather than a generic head term.
3. Extend short seed queries with one or two additional modifiers to capture longtail variants, even if this changes the reported search-volume figure in your keyword tool.
4. Do not avoid editing a query just because editing lowers its visible search-volume number — judge it on intent match and specificity instead.
5. Have a human with domain or query-crafting experience do this review pass before any AI-suggested keyword enters the approved tracking sheet.

**Tools:** ChatGPT, Claude, Perplexity

**Pitfall:** Leaving AI-suggested seed queries exactly as generated because tweaking them changes the search-volume number shown in the tool — Gotch calls this fear of editing a really big mistake since the untouched seed queries are weak on their own.

### 9. Fix these AI writing tells before publishing Claude's draft  `31.2`
*core · best practices · source 31*

After Claude drafts a new section, expect to rewrite its output rather than publish it as-is. Any strategic advice it gives needs a rewrite, since you are the actual expert and the AI's version won't be expert-level. The prose will also carry recognizable AI tells: the word "actually" shows up constantly in AI writing, so cut it in roughly 90% of its occurrences; AI content tends to be overly verbose, using far more words than a simple concept needs, so actively shorten it; and AI defaults to unconfident hedging phrasing like "this can help" rather than the more confident "this will help," which reads as more trustworthy and makes readers want to keep reading.

> "cut the word "actually" in 90% of situations"

**How to do it**

1. Read through any AI-drafted section specifically checking for strategic/expert advice claims, and rewrite those yourself rather than trusting the AI's version.
2. Search the draft for the word "actually" and delete it in roughly 90% of its occurrences.
3. Reread each paragraph asking whether it could say the same thing in fewer words, and cut verbose phrasing down to the idea it's actually conveying.
4. Search for hedging phrases like "can help" or "may help" and rewrite them into confident, direct phrasing such as "will help" wherever the claim is true and defensible.
5. Read the edited section over once more to confirm it now sounds confident and human rather than hedged and AI-generated. (inferred)
6. Apply this same checklist every time you generate new content with an AI tool, since these are consistent, repeatable tells rather than one-off mistakes. (inferred)

**Tools:** Claude, ChatGPT

**Pitfall:** AI-generated additions will consistently default to hedged, unconfident phrasing ('this can help' instead of 'this will help'), overuse the word 'actually,' run more verbose than the idea requires, and offer strategic advice that isn't actually expert-level - skipping the manual edit pass and publishing the AI's draft as-is leaves all of these tells in the final content.

### 10. Front-load a huge voice-dictated first prompt, then skill-ify it  `16.9`
*core · ai workflows · source 16*

To set up an AI-run site or recurring workflow from scratch, the described method is to use a voice-to-text tool (Whisper Flow is named) and dictate one enormous first prompt into Claude Code — talking for 45 minutes up to two hours, aiming for roughly 10,000-20,000 words covering everything relevant about the business and the task. The reasoning given is that every message after the first reloads the entire conversation into context, so the first prompt is the cheapest place to front-load information; under-loading it means repeatedly re-explaining things later. That first prompt should end by telling Claude it will later be asked to convert the successful process into a reusable skill, and after Claude attempts the task and receives feedback across a few iterations, the user explicitly instructs it to formalize the process as a skill, then keeps updating that skill after every subsequent real use.

> "talk for 45 minutes, two hours if you can"

**How to do it**

1. Download a voice-to-text tool such as Whisper Flow so you can speak instead of typing.
2. Before starting a new AI-built site or recurring task, open Claude Code and prepare to send one very large first message.
3. Talk through everything relevant for 45 minutes up to two hours, aiming for roughly 10,000-20,000 words about the business, the task's purpose, audience, and background.
4. End that first prompt with the instruction to turn the process into a skill once it succeeds.
5. Let Claude attempt the task, review its output, and give detailed feedback on mistakes, repeating until satisfied.
6. Once satisfied, explicitly instruct Claude to turn the process into a skill.
7. Next time the same type of task comes up, load the saved skill and tell Claude you're doing the same thing as last time rather than re-explaining from scratch.
8. After each subsequent run, instruct Claude to update the skill with what it learned so it keeps improving.
9. Whenever a knowledge gap appears mid-conversation, point Claude to the source on the spot (e.g., a Google Drive folder, or connect Gmail, Slack, or Notion).
10. Periodically ask Claude to compile gathered information into a markdown file for later reuse, building a persistent knowledge-base library alongside the skills.

**Tools:** Claude Code, Whisper Flow, Google Drive, Gmail, Slack, Notion

**Prompt / template:**

```text
after we go through this process, I'm going to ask you to turn it into a skill we can use next time. [Later, once satisfied:] go ahead, turn it into a skill. [Next time the task recurs:] we're doing the same thing as last time. [After that run:] take everything you learned from this run and update the skill so you do a better job next time. [To bank source material:] take all that information I just gave you and put it into a markdown file, because we'll need it later.
```

**Pitfall:** Sending short, piecemeal opening prompts wastes the one moment where context-loading is cheapest — since every later message reloads the full conversation, under-loading the first prompt means paying to re-explain the same background information repeatedly across later sessions.

### 11. Gate every AI-agent code change behind review; expect to rebuild until you do  `50.12`
*core · best practices · source 50*

The single biggest lesson from four months of building this system with coding agents, Claude and Codex, plus an autonomous computer-using agent called Open Claw that was given its own dedicated new computer and email account for safety, was that the agents are not reliably good at writing correct code and will not review their own output, so uncaught errors would compound and eventually break the whole platform whenever it tried to scale or add a feature. The fix was to require that everything the agents produce goes through a gated review phase, sending problematic output back to be fixed rather than merging it directly, and the builder now writes the actual code himself while using the agents mainly to generate ideas and help organize the project. He states plainly that he rebuilt the platform from scratch roughly four times before internalizing this lesson, and recommends anyone attempting a similar build learn the error-handling and gating discipline first, before anything else.

> "I created this platform like four times before learning that"

**How to do it**

1. Before building any agent-driven automation pipeline, design an explicit gate or checkpoint for every piece of code or content an agent produces, rather than letting agent output merge or deploy directly.
2. Route agent-generated code changes through this gate for human or automated-test review before they're accepted into the system.
3. When output fails the gate, send it back to the agent or a human to fix rather than patching around the failure.
4. If giving an autonomous agent computer or browser access, isolate it on a dedicated machine and a fresh account rather than your primary work computer or email, to contain any unintended actions.
5. Treat early platform rebuilds as expected: budget for rebuilding core parts of the system multiple times while this discipline is still being established, rather than assuming the first architecture will scale.
6. Once gating is reliably in place, shift your own role toward writing and reviewing the actual code yourself while using agents primarily for ideation and organization, rather than fully delegating implementation.

**Tools:** Claude, Codex, an autonomous coding agent (Open Claw)

**Pitfall:** Skipping a real error-handling and review gate is what caused the platform to break down every time the builder tried to scale it or add a feature — he had to rebuild it about four times before treating this as the first thing to solve, not an afterthought.

### 12. Give each agent one narrow job, then require a self-report  `27.3`
*core · ai workflows · source 27*

The core architecture principle described is to never let one agent handle an entire task end-to-end; instead, split the work into separate narrow steps — for example, one agent updates only the page title, another only the meta description, another only the body content — because keeping each agent's decision scope "limited and narrow" is what makes the output reliable enough to trust. Before any agent-produced material moves forward, especially before it reaches content creation, the agent is required to stop and generate a structured self-report: what action it took, what decisions it made, how it contextualized the information, and which sources it actually used. That checkpoint lets a human catch a bad decision or a wrong data source "at a glance" before it compounds further downstream, rather than discovering the problem after the content is already written.

> "when the agent is done, have it summarize what it did"

**How to do it**

1. Break the SEO task into its smallest independent sub-tasks (e.g., title update, meta update, body-content update, data retrieval) rather than one end-to-end agent.
2. Build or configure a separate agent, or a separate clearly-scoped prompt/skill, for each sub-task, restricting each one's ability to act to only that sub-task.
3. Feed each narrow agent only the information sources it actually needs for its specific job, not the full brand/business context (inferred, consistent with the source's broader information-hygiene guidance).
4. After each agent run completes, require it to output a structured summary answering: what action did you take, what decisions did you make, how did you contextualize the information, and what information did you use.
5. Review that summary before allowing the output to proceed to the next stage, e.g., before a title change goes live, or before a draft moves to the writing step.
6. If the summary shows the agent used information it shouldn't have, or made an unjustified decision, correct it at that checkpoint rather than downstream.
7. Only once the checkpoint passes, allow the narrow output to feed into the next agent or into human writing.

**Tools:** Claude Code, Google Search Console

**Pitfall:** Letting one agent handle multiple decisions at once, e.g., retrieving data, deciding a new title, and rewriting body copy in one pass, removes the checkpoint where a human could catch a bad decision before it compounds into the next step.

### 13. Hoist repeated tool calls out of the agent loop to cut cost  `27.6`
*core · best practices · source 27*

Because agents spend money every time they call an external tool, e.g., pulling Google Search Console or Analytics data, the speaker built his own platform specifically to stop agents from repeatedly re-calling the same tool inside a running chat: as soon as a chat starts, if it detects the agent calling the same tool repeatedly, it moves that call out of the loop so the result is simply injected into context, and the agent spends the minimum tokens actually reasoning over the data rather than re-fetching it. He pairs this with deliberate model selection by task: reserve expensive frontier-model tokens (he cites Opus at roughly $30 per million output tokens) for tasks that need real reasoning, and run repetitive tool-calling or retrieval-heavy SEO tasks on a cheap or free model like DeepSeek instead, since retrieval doesn't require frontier-level intelligence.

> "the agent spends money calling those tools every time"

**How to do it**

1. Audit your agent pipeline for any tool call, e.g., a Google Search Console or Analytics pull, that repeats identically across multiple runs or steps of the same task.
2. Refactor the pipeline so that repeated call is made once and its result is injected directly into the agents' context, instead of letting every downstream agent re-call the same tool.
3. For each task in the pipeline, classify whether it needs frontier-level reasoning or is primarily retrieval/tool-calling.
4. Route reasoning-heavy steps to a frontier model and route retrieval/tool-calling steps to a cheap or free model such as DeepSeek instead of running everything on the same expensive model.
5. Track token/cost spend per pipeline run and re-check it after refactoring to confirm the hoisted tool calls and model-routing changes actually reduced cost (inferred verification step).

**Tools:** DeepSeek, Google Search Console, Google Analytics

**Pitfall:** Running every pipeline step on the same expensive frontier model, and letting every agent independently re-call the same data source, both burn money on work a cheap model or a single cached tool call could handle just as well.

### 14. Interview an AI agent about your business to build a 'Brand DNA' profile  `50.9`
*core · ai workflows · source 50*

Rather than filling out a static intake form, the recommended way to build the foundational business profile that gates the whole system is to have an open-ended conversation with an AI agent about the business, telling it what you sell, who buys it, and answering its follow-up questions, and letting the agent research and fill out the structured profile sections itself, which the builder says it does "better than me." The resulting profile covers brand score, market positioning, target audience, product and service catalog, trust signals, and proof themes such as case studies, and Claude is specifically called out as strong at extracting brand identity and voice and tone from this kind of conversation. A related layer, the "project brain," continuously absorbs corrections and new information from ongoing conversations, such as "this isn't correct" or "we want to talk about this topic," and stores each as a confidence-scored item tagged as an issue, a working fact, research, a preference, a strategy, or an insight.

> "recommend talking to an AI agent about your business"

**How to do it**

1. Open a conversation with an LLM such as Claude and tell it plainly what your business sells, who your current customers are, and who you want your future customers to be.
2. Let the AI ask follow-up questions and answer them conversationally rather than trying to pre-write a comprehensive brief yourself.
3. Ask the AI to output a structured profile covering brand positioning, target audience, product and service catalog, trust signals, and proof points or case studies.
4. Review the AI's draft profile and correct anything inaccurate directly in conversation.
5. Store each correction or new fact as a separate, tagged entry, such as issue, working fact, research, preference, strategy, or insight, rather than only editing the original document in place, so you retain a history of why decisions were made (inferred structured-logging mechanism).
6. Re-open and update this profile whenever the business's positioning, audience, or product line changes materially, since every downstream keyword and content decision depends on it staying current.

**Tools:** Claude

### 15. Iterate entity copy in an NLP sandbox until every entity is recognized  `73.16`
*core · ai workflows · source 73*

Barnard's writing loop uses a text analysis sandbox on kalicube.pro that runs text through Google's natural language processing API. You paste a draft, it tells you which entities Google managed to recognize, what type it assigned each one (corporation, work of art, person), whether the entity is in the knowledge graph, and how many mentions it found in the text. You then keep rewriting until it recognizes the things and the words you want, with your name or company name right at the top of the recognized list. He discovered the verb-noun ambiguity problem this way, changing one word at a time to see what changed in the output. He also notes the tool merges co-references: in 'Jason Barnard is the CEO and founder of Kalicube', it identifies CEO as the same thing as Jason Barnard. This is the drafting step for every entity description before it goes on any platform.

> "use the text analysis copywriting sandbox"

**Evidence:** Barnard found the verb-noun ambiguity effect by changing single words in the sandbox and watching both the recognized entities and their assigned types change.

**How to do it**

1. Draft the entity description with the semantic triple, the audience, the trust anchor and the explicit conclusion sentences.
2. Paste the draft into the copywriting sandbox on kalicube.pro, or send it to Google's Natural Language API directly.
3. Check that your brand or personal name is recognized and appears at the top of the salience-ordered entity list.
4. Check the assigned type for each entity: organization, person, location, work of art. Fix the wording if the type is wrong.
5. Check whether each recognized entity resolves to a knowledge graph item, and prefer wordings that resolve.
6. Change one word at a time and re-run, so you can attribute any change in recognition to that word.
7. Look for words used as verbs that were parsed as nouns, or vice versa, and replace them.
8. Only publish the text to the entity home and every platform once the recognition output matches what you intended.

**Tools:** Kalicube Pro, Google Cloud Natural Language API

**Pitfall:** Rewriting several sentences between runs. The output changes and you cannot tell which edit caused it, which is precisely why Barnard changes one word at a time.

**Apply at Pabau:** Run Pabau's About page opening paragraph and the standard boilerplate through this loop before they go into any directory listing, and confirm Pabau is returned as an organization at the top of the list.

**Apply anywhere:** Before publishing any entity description, run it through an NLP entity-recognition sandbox. Confirm your brand is recognized, ranked top and typed correctly, then change one word at a time until the whole text parses as intended.

### 16. Keep a mandatory human review stage before any AI-written page publishes  `50.4`
*core · best practices · source 50*

Even though the entire pipeline, from keyword discovery through drafting, could be run fully automatically end to end, the builder deliberately keeps a "needs review" stage where a human reviewer opens every AI-generated article in an editor, checks that the underlying signals and content are correct, requests specific changes via comments, and only then approves it for upload. He's explicit that this human gate is what keeps the output from being "scaled AI content" in the negative sense — the agents are good at finding signals such as missing entities, information gain, and SERP gaps, and drafting from them, but a person still has to confirm the result is actually good before it goes live. His stated design principle, after building and rebuilding the platform, is that a fully automatic run is technically possible, since you can "just connect it to your storage," but he does not recommend it.

> "you need to have a step in there that's human"

**How to do it**

1. Design your content pipeline so every AI-drafted page lands in a distinct "needs review" status rather than auto-publishing.
2. Give reviewers an editor view that shows the drafted content alongside the underlying research or signals the agent used, such as missing entities, competitor gaps, or information gain, so they can judge context, not just prose quality.
3. Assign a specific named reviewer, not "whoever's free," to each piece so accountability is clear.
4. Let the reviewer either approve the piece for upload, or leave inline comments describing exactly what needs to change and send it back into the pipeline.
5. Only move a piece to published after a human has explicitly clicked approve, never on a timer or automatic default.
6. Periodically audit a sample of already-approved pieces to confirm reviewers are actually catching problems, not rubber-stamping (inferred quality-control step).

**Pitfall:** The system is technically capable of running with zero human involvement end to end, but the builder explicitly avoids that: skipping the human review gate is what turns this into ungoverned scaled AI content.

### 17. LLMs pattern-match riddles; false SEO 'facts' become consensus  `21.12`
*core · general insights · source 21*

David tests LLMs with a classic lateral-thinking riddle (a father dies in a car crash; the operating surgeon says 'I can't operate, that's my son' - the answer is that the surgeon is the boy's mother). When he flips the setup so the driver killed is explicitly female and asks an LLM to solve it, the model still answers 'the surgeon is the mother' even though that is logically impossible given the stated premise, proving it is matching the well-known riddle pattern rather than reasoning through the actual facts given. He connects this directly to SEO misinformation: if Google publishes one primary-source statement and a hundred blog posts all repeat a different claim (e.g., 'Google uses E-A-T as a ranking factor on every crawl'), an LLM will reflect the repeated claim as fact, because there is no objective test separating popular-but-wrong SEO claims from true ones in its training data.

> "it's not thinking, it's still using pattern recognition"

**Evidence:** David's own repeated live test of a gender-reversed surgeon riddle against LLMs: the model answers 'the surgeon is the mother' even when that contradicts the stated premise (the mother already died), showing pattern-matching rather than genuine reasoning; he links this to how volume-repeated but unverified SEO claims (e.g., broad E-A-T ranking-factor claims) get treated as fact by LLMs and by SEOs citing AI Overviews in debates.

**Apply at Pabau:** Treat LLM-generated SEO advice and AI Overview summaries on contested topics (like E-A-T) with real skepticism, and verify claims against primary sources (e.g., Google's own statements) rather than trusting an LLM's answer or a frequently-repeated blog claim - this applies both to research David does with AI tools and to any AI-assisted content Pabau publishes that repeats unverified industry 'conventional wisdom.'

**Apply anywhere:** Treat LLM-generated SEO advice and AI Overview summaries on contested topics (like E-A-T) with real skepticism, and verify claims against primary sources (e.g., Google's own statements) rather than trusting an LLM's answer or a frequently-repeated blog claim - this applies both to research you do with AI tools and to any AI-assisted content you publish that repeats unverified industry 'conventional wisdom.'

### 18. Lock, gate, and digest: three safety rails for cron agents  `01.10`
*core · ai workflows · source 01*

Scheduled agents need three specific safety mechanisms: an advisory lock per agent so a slow-running job can never overlap with its own next scheduled run (skip and log instead of stacking), a `HUMAN_APPROVAL_REQUIRED` list of specific risky actions (raising a daily budget more than 20%, emailing more than 500 people in a run, deleting anything) the agent must pause and ask about, and a daily 8am Slack digest reading the `agent_runs` and `api_costs` tables to summarize every agent's status and prior-day spend. The overlap lock isn't theoretical — a single enrichment run taking 70 minutes on an hourly schedule is enough to produce two agents writing to the same table with the same cursor.

> "autonomous agent with an unbounded budget lever is how you lose $10k"

**How to do it**

1. Define each scheduled job in a `schedule.yaml` specifying agent name, cron expression, timeout, and a target Slack channel.
2. Implement an advisory lock per agent so that if a run is still in progress when the next trigger fires, the new run is skipped and logged rather than allowed to stack.
3. Define a `HUMAN_APPROVAL_REQUIRED` list per agent naming specific high-risk actions (raising a daily budget more than 20%, emailing more than 500 people in a run, deleting anything) that must be paused on rather than executed.
4. Require every run to post a Slack summary to its channel covering what it did, what it spent, what changed, and anything it flags for human review.
5. Build a daily 8am digest job reading `agent_runs` and `api_costs` and posting one consolidated Slack message with every agent's status and the prior day's total spend across all APIs.
6. Review the daily digest each morning and intervene only on the specific agent or action flagged as needing approval, leaving the rest running unattended.

**Tools:** Claude Code, Slack

**Prompt / template:**

```text
Set up scheduled agent runs on the runtime server. Each job is defined in a `schedule.yaml`: agent name, cron expression, timeout, and a Slack channel. Requirements: (1) An advisory lock per agent so a slow run can never overlap with the next scheduled run — skip and log instead of stacking. (2) Every run posts a Slack summary to its channel: what it did, what it spent, what changed, and anything it wants a human to look at. (3) A HUMAN_APPROVAL_REQUIRED list per agent — actions it must ask about instead of doing, like raising a daily budget more than 20%, emailing more than 500 people in a run, or deleting anything. (4) A daily 8am digest job that reads `agent_runs` and `api_costs` and posts one message with every agent's status and yesterday's total spend across all APIs.
```

**Pitfall:** An autonomous agent with an unbounded budget lever and no approval gate is how you lose $10k in a single day unattended; without an overlap lock, a run that exceeds its own scheduled interval produces two concurrent agents writing to the same table with the same cursor.
