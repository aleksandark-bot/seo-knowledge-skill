# AI Workflows & Agents — supporting

27 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. A purpose-built cron agent beats a general-purpose one  `56.22`
*useful · general insights · source 56*

Cody's contrarian position on general-purpose agent platforms is that almost everything he sees people do with them could be a specific piece of software running on a cron job with an LLM doing the thinking step - and that the specific version is simpler, safer, cheaper and more malleable. His definition: 'all an agent is, is something that's doing a loop that's on a cron job. It's just software, and then you have the LLM thinking about something, analyzing something for you within that process.' The example he gives is a podcast booking agent he built: it was terrible, but it booked 35 calls in a week and got 112 yeses out of a cohort of 2,000 - and when people spotted it was a bot because it replied instantly, he changed the code to wait a random 45-60 minutes. That malleability is the argument. He also warns about surface area: prompt injection and, in a case he saw, an agent hooked up to Gmail deleting everything. His stack for this is Claude Code plus Railway for deployment, then a hardening pass asking the agent to identify security vectors.

> "all an agent is something that's doing a loop"

**How to do it**

1. Write down the loop you actually want: the trigger, the steps, the decision the LLM makes, the output.
2. Build it as plain software with Claude Code rather than as a configuration inside a general agent platform or an automation tool.
3. Deploy it somewhere it can run perpetually - he uses Railway's API to spin up the server and put the software on it.
4. Ask the agent to harden it: what vectors make this unstable or insecure.
5. Run it, watch the failure modes, and fix them by editing code - his instant-reply giveaway became a randomised 45-60 minute delay.
6. Keep the tool and data access narrow, specifically to limit prompt-injection and destructive-action surface.
7. Resist coupling it to high-consequence systems (like an email account with delete permissions) until it has earned that trust.

**Tools:** Claude Code, Railway

**Pitfall:** He is describing personal software, not products - unpublished tools he owns. The security shortcuts that are acceptable for a private cron job are not acceptable for anything customer-facing.

**Apply at Pabau:** For Pabau, the pattern to copy is narrow and boring: small purpose-built jobs (a weekly Search Console pull, a link-status check, a decay report) running on a schedule, rather than one general agent with broad access to production systems.

**Apply anywhere:** The pattern to copy is narrow and boring: small purpose-built jobs (a weekly Search Console pull, a link-status check, a decay report) running on a schedule, rather than one general agent with broad access to production systems.

### 2. Access older model versions via API when the newest underperforms  `27.10`
*useful · concrete actions · source 27*

When a consumer chat interface like ChatGPT only exposes the most recent model version, and that newest version is producing worse writing or analysis output than an older version did, the fix described is to bypass the consumer app: older model versions typically remain available through the provider's API, or through a third-party routing platform like OpenRouter, letting you select the specific model version directly rather than whatever the app defaults to. Model fit is also framed as partly a matter of prompting compatibility — a given user's prompting style may simply pair better with one model than another, one example given is a preference for DeepSeek — so switching models is worth testing empirically rather than assuming the newest release is always the best fit for a given writing or analysis task.

> "those older models are still available through the API"

**How to do it**

1. Identify a task, e.g., SEO analysis or content drafting, where the current default model in your chat app is producing worse output than an earlier version used to.
2. Check whether the consumer app, e.g., ChatGPT's interface, only exposes the latest model, since older versions are often hidden from that UI.
3. Sign up for API access with the model provider, or set up an account with a routing platform such as OpenRouter, to select a specific older or alternate model version directly.
4. Run the same task through the older/alternate model and compare output quality against the current default before switching your workflow over.
5. Keep track of which model version paired best with your specific prompting style for which task type, since fit is described as partly preference-based, not purely a capability ranking.

**Tools:** ChatGPT, OpenRouter, DeepSeek

**Pitfall:** Assuming the newest model version is automatically the best choice for every task is a mistake the source explicitly pushes back on — for writing and analysis tasks specifically, a benchmark showed an older model (Opus 4.6) outperforming a newer one (4.8) because the newer release had been tuned more heavily toward coding.

### 3. Always fill every data cell to stop AI hallucinating  `46.11`
*useful · ai workflows · source 46*

Travis's practical rule from using AI on real SEO and business data: when you feed AI a table or spreadsheet to analyze, for example to build an SEO workbook or group keyword and content data, it hallucinates specifically in any cell left blank — 'if you don't have a number in a cell, it'll make a number up.' His fix, learned from direct experience, is to always populate every cell with an explicit value, using zero rather than leaving it empty when there's genuinely no data. He pairs this with using an AI tool connected via MCP to a data source such as Ahrefs to help group and synthesize data for content strategy once the input table itself is clean.

> "don't have a number in a cell, it'll make a number up"

**How to do it**

1. Before feeding any spreadsheet or table to an AI tool for analysis, scan every column for blank cells.
2. Replace every genuinely empty or not-applicable cell with an explicit 0, or another defined placeholder value, rather than leaving it blank.
3. Only then paste or upload the table into the AI tool for grouping, summarizing, or analysis.
4. When the AI returns a data-derived claim or number, spot-check it against 2-3 raw source rows before using it in a client-facing workbook or report (inferred).
5. Where possible, connect the AI tool directly to your data source via MCP, such as an MCP server attached to Ahrefs, so it queries structured, complete data directly instead of working from manually pasted tables.

**Tools:** Ahrefs, MCP

**Pitfall:** Any blank cell in a data table handed to an AI model is treated as an invitation to invent a plausible-looking number — always default empty values to zero rather than leaving them blank.

### 4. Auto-bucket form leads into archetypes with Zapier's AI  `55.5`
*useful · ai workflows · source 55*

After a prospect submits the seven-field form, Zapier automatically logs every response into Google Sheets, then Zapier's built-in AI classifies each lead into one of four to five predefined customer archetypes based on their form answers, triggering a distinct email flow per archetype. Zapier alone can run the whole email sequence as a "quick and dirty" option, or leads can be routed into a dedicated email tool like Mailchimp for richer reporting — either way, more archetypes (up to a practical four or five) means better-targeted follow-up content.

> "you use Zapier's AI to bucket leads based on their answers"

**How to do it**

1. Define four to five distinct customer archetypes for your offer in advance, based on the different situations or problems your typical customers have.
2. Design the seven form fields so their answers contain enough signal to distinguish between these archetypes.
3. Connect the form to Zapier so every submission is logged as a new row in a Google Sheet automatically.
4. Configure a Zapier AI step that reads each new form response and assigns it to one of the predefined archetypes.
5. Build one automated email flow per archetype, either directly in Zapier (fast, minimal reporting) or in a dedicated email tool like Mailchimp (more data and reporting).
6. Trigger the correct archetype's email flow automatically based on the AI's classification the moment a new lead is added.

**Tools:** Zapier, Google Sheets, Mailchimp

### 5. Automate uncredited-image backlink reclamation with an AI agent  `24.7`
*useful · ai workflows · source 24*

The follow-up step to seeding stock photos is to periodically reverse-image-search each seeded photo on Google Images or TinEye to find sites using it without attribution, then email each one a short, friendly request to add a source-credit link — or, per the source, have an AI agent run this entire pipeline autonomously on autopilot. The described conversion rate on this outreach is very high specifically because the recipient already used the content without permission and implicitly owes the credit, unlike cold link-building outreach to strangers, and the opportunity compounds over time as more images spread into wider use.

> "have an AI agent do the entire process for you on autopilot"

**How to do it**

1. Periodically run a reverse image search on each seeded stock photo using Google Images or TinEye.
2. Compile the list of sites using your image without a credit or backlink.
3. For each uncredited use, send a short, friendly email requesting a source-credit link.
4. To scale this, configure an AI agent to run the pipeline autonomously: search for uses, flag uncredited ones, find a contact address, draft and send the request, and log responses. (inferred agent architecture)
5. Expect a high response rate on this outreach specifically because the recipient already used your content without permission.
6. Repeat on a recurring schedule, since the pool of unattributed uses keeps growing as seeded images continue to spread. (inferred cadence)

**Tools:** Google Images, TinEye

**Prompt / template:**

```text
Hey, love that you used my image. Would you mind adding a source credit link?
```

**Pitfall:** Relying only on one-off manual checks instead of a recurring or automated cadence — the value compounds precisely because image spread is continuous, so a single manual pass misses ongoing new uses.

### 6. Build agents whose job is to improve your other agents  `27.12`
*useful · ai workflows · source 27*

Beyond agents that do the work, the speaker describes building a second layer of agents whose job is to strengthen, repair, and improve the first layer every time it runs, and even a third layer whose job is to improve the improver agents — a recursive hierarchy that stays effective only as long as each layer's decision scope is kept very narrow. He demonstrated a working version of this with coding agents: he typed a customer's requested feature or fix directly into an agent, which filed it to Jira, and coding agents picked up the ticket and carried the change through the entire flow, modifying the program and distributing it end to end, a process he's since run and improved many times. He's explicit that this is slow, judgment-heavy work rather than a quick setup, and that it is specifically the narrow-domain framing that makes it tractable at all.

> "typed into the agent how I wanted it repaired, and it sent"

**How to do it**

1. Build your first layer of task-doing agents, each scoped to one narrow job, consistent with the source's broader narrow-scope principle.
2. Build a second-layer agent whose only job is to review a first-layer agent's runs and strengthen, repair, or improve it over time.
3. Optionally build a third-layer agent whose only job is to improve the second-layer improver agents.
4. Keep every layer's decision scope narrow rather than letting any single layer handle multiple responsibilities.
5. For a coding-agent version of this, route a specific requested feature or fix as a ticket into your issue tracker, e.g., Jira, directly from an agent conversation.
6. Let coding agents pick up that ticket and carry the change through implementation and deployment end to end.
7. Run this process repeatedly on real requests, using each run to further improve the agents involved rather than treating the first version as finished.

**Tools:** Jira, Saga

**Pitfall:** Treating this as a quick setup rather than an ongoing practice is the mistake — the source is explicit that getting a recursive agent-improving-agent hierarchy to work reliably takes a lot of judgment, time, patience, and practice, not a one-time configuration.

### 7. Build drop-catching automation with Claude Code rather than buying a tool  `67.15`
*useful · ai workflows · source 67*

Asked which drop-catching tools he recommends, Dirk says there is no viable off-the-shelf option left. The tools that existed have gone out of business, and the reason is footprint exposure: the server hosting of those services has been mapped, so if one user is exposed the connections expose the rest. His recommendation is to build your own, and he says AI has made this much simpler than it was. He describes plugging in registrar APIs, connecting sheets, and pushing requests through the ICANN channels, and names Claude Code as capable of helping. His repeated condition is that the requirements are the hard part: the AI can build it, but only if you specify the flow properly. He also gates the whole exercise, saying he would only do this as a large company building in-house infrastructure to compete with the likes of Finixio.

> "Claude Code can help, but again, it's a requirement"

**Evidence:** Dirk says every off-the-shelf drop-catching tool he is aware of has gone out of business, primarily because the hosting footprints of their servers were exposed.

**How to do it**

1. Write the requirements document first, describing the full domain lifecycle from non-renewal through grace period to public release.
2. Specify which registrars you will connect and get API access to each one before writing any code.
3. Define the watch list source, such as a sheet of target domains or keyword patterns, and how it is refreshed.
4. Have Claude Code build the polling layer that checks registrar and ICANN endpoints for status changes on the watch list.
5. Have it build the burst registration layer that fires many attempts within the release second, with per-registrar rate handling.
6. Add logging of every attempt and outcome so you can debug which registrar path actually wins.
7. Vary the hosting and network origin of your own infrastructure, since Dirk says exposed server footprints are what killed the commercial services.
8. Before building any of it, confirm the volume case: Dirk says this only pays if you intend hundreds to thousands of domains a month, not ten.

**Tools:** Claude Code

**Pitfall:** Building it for a small portfolio. Dirk says the economics only work at hundreds to thousands of domains a month, and that a badly specified build wastes a lot of money very easily.

**Apply at Pabau:** The transferable lesson for Pabau is that AI coding tools now make a bespoke internal SEO tool cheaper than a subscription, but the requirements document is the actual work. Write the spec before opening Claude Code.

**Apply anywhere:** When no good off-the-shelf tool exists, build a bespoke one with an AI coding assistant, but write the full requirements and data flow first. The specification is the work; the code is the easy part.

### 8. Confine AI to research and interview prep, keep positioning human  `181.9`
*useful · ai workflows · source 181*

Grow and Convert state a boundary rather than a ban. They say many agencies have replaced writers with automated AI content workflows, and that in their experience AI-generated content lacks the strategic thinking and authentic expertise that converts B2B buyers. Their writers use AI to assist in conducting and learning from expert interviews, crafting original arguments, and understanding how to position complex products. The line they draw is explicit: AI assists the research process, but the insights, structure and positioning come from experienced professionals. That is a usable division of labour. The AI does the load-bearing preparation, such as reading the SERP and building the question list, and the human does the parts where being wrong costs a conversion, such as the argument and the competitive framing.

> "We use AI to assist our research process, but the insights, structure, and positioning come from experienced professionals."

**Evidence:** Grow and Convert say AI-generated content lacks the strategic thinking and authentic expertise that converts B2B buyers, based on their own testing against a human interview-led process.

**How to do it**

1. Use AI to summarize the ranking pages for the target keyword and list what each one covers, before the interview.
2. Have it draft the interview question list from those gaps, then edit the list yourself and add the questions only you know to ask.
3. Feed the recorded transcript to AI for a clean transcription and a list of the specific claims, numbers and workflows the expert gave.
4. Write the argument and the structure yourself from that extract, rather than asking the model for an outline of the article.
5. Keep competitive positioning entirely human, since it depends on judgement about what the buyer weighs.
6. Use AI on the back end for mechanical checks: internal link candidates, on-page keyword placement, readability.
7. Never let a model produce a published draft unedited, and treat any section you cannot source to the interview as a rewrite candidate.

**Tools:** ChatGPT, Claude

**Pitfall:** Letting AI produce the structure and the argument is where B2B content goes generic. The signal is a draft that reads correct but contains no claim a competitor could not also make.

**Apply at Pabau:** Pabau's writing process should use AI for SERP summaries, interview question lists and transcript extraction, and keep the argument, structure and competitive framing with a person. That matches the existing rule that AI output always gets a human pass.

**Apply anywhere:** Use AI for SERP summaries, interview question lists, transcript extraction and mechanical on-page checks, and keep the argument, structure and competitive positioning with a human writer.

### 9. Distill a small model to diagnose RAG pipeline drop-off  `20.10`
*useful · ai workflows · source 20*

To understand exactly why content fails to gain AI visibility, the speaker's team built a replica of a generative AI system's retrieval-augmented-generation pipeline and tracks precisely which stage a given piece of content 'falls out' of the pipeline at, enabling a direct explanation like 'your content underperformed at stage three, which is why you're not getting visibility.' He proposes 'model distillation' as how GEO tooling should be built generally: run a large volume of prompts through a frontier model (ChatGPT or Gemini) and use those input/output pairs to train a smaller, faster model approximating the same ranking/filtering behavior, making pipeline-stage diagnosis replicable at scale rather than one-off guesswork. He criticizes existing SEO software vendors for bolting an AI chat layer onto legacy tools instead of building this.

> "what's called model distillation, where you use the big model"

**How to do it**

1. Map out the likely stages of a target AI system's retrieval pipeline (query fan-out generation, document retrieval, passage extraction/scoring, comparative filtering, final synthesis) based on published architecture descriptions and observation.
2. Build or adopt a replica pipeline that runs your content and a competitor's content through those same stages.
3. At each stage, record whether your content survives to the next stage or gets filtered out, and log the competitor's outcome at the same stage for comparison.
4. Where your content 'falls out' earlier than a competitor's, treat that specific stage as your diagnosed bottleneck rather than treating 'low visibility' as one undifferentiated problem.
5. For a more advanced, at-scale version, send a large volume of real prompts through a frontier model (ChatGPT or Gemini) and log the input/output pairs.
6. Use those input/output pairs as training data to fine-tune or distill a smaller model that approximates the frontier model's filtering/ranking behavior at each stage.
7. Use the distilled model going forward to run this stage-by-stage diagnosis cheaply and repeatedly across your whole content library. (inferred scaling step)

**Tools:** ChatGPT, Gemini

### 10. Feed Claude a first-party knowledge base to auto-generate topic ideas  `11.13`
*useful · ai workflows · source 11*

Gotch's AI-assisted ideation workflow: build a Claude project, referred to as your 'SEO super intelligence' and set up in a prior video in his series, populated with your own first-party files such as company knowledge, product details, and customer intelligence, then prompt it directly to review that knowledge base and generate a list of topic ideas. Because the ideas are grounded in your own proprietary information rather than generic web knowledge, he classifies the output as 'first-party content ideas,' and reports that a meaningful share of Claude's suggestions in his own St. Louis SEO example were pretty solid starting points needing refinement rather than rejection.

> "review our knowledge base and generate a list of topic ideas"

**How to do it**

1. Set up a dedicated Claude project and upload your company's first-party knowledge files, such as product docs, sales call notes, customer FAQs, and case studies, as project knowledge (inferred: use Claude's Projects feature with the knowledge/files panel).
2. In that Claude project, prompt: 'review our knowledge base and generate a list of topic ideas.'
3. Export or copy Claude's suggested topic list directly into your keyword tracking sheet's idea intake area.
4. Review each suggested topic for intent specificity, since queries like 'B2B SEO St. Louis' needed tightening to 'best B2B SEO agencies in St. Louis' before they were usable.
5. Discard the subset of suggestions that don't make sense or wouldn't get client or stakeholder approval, rather than adding every AI suggestion to the sheet.
6. Tag surviving topics with Source = 'Claude/knowledge base' so you can later evaluate how productive this ideation channel is relative to GSC, Reddit, and Keyword Planner.

**Tools:** Claude

**Prompt / template:**

```text
review our knowledge base and generate a list of topic ideas
```

**Pitfall:** Accepting AI-suggested queries at face value without tightening their specificity or extending them with longtail modifiers — Gotch calls this a really big mistake since seed queries from AI are described as weak on their own.

### 11. Five starter agents to build once the factory runs  `01.12`
*useful · concrete actions · source 01*

Once the seven-piece infrastructure exists, five example marketing functions become simple narrow agents rather than full projects: static ad packs (batch-generate roughly 40 image variations a week via Nano Banana through the gateway, upload to R2, push to the Facebook Ads API as paused drafts for human review); UGC video (script pulled from the warehouse's top-converting angles, rendered via Seedance, captioned, sent to object storage); waterfall lead enrichment (Apify scrapes the TAM, the gateway waterfalls Apollo then GetLeads then email permutation, Million Verifier confirms, rows land in the leads table); cold email plus inbox management (Instantly sends, a webhook classifies replies, the agent auto-answers easy ones and Slacks a human only the ambiguous replies); and analytics (the agent answers questions like cost per qualified lead by channel directly in SQL against the warehouse instead of in a meeting).

> "the agent answers the easy ones and Slacks you the hand raises"

**How to do it**

1. Pick one of the five example agent types (static ad packs, UGC video, waterfall enrichment, cold email/inbox, or analytics) as your first build.
2. Create a new folder under `/agents` containing a `CLAUDE.md`, the relevant `.claude/skills/`, and a `run.sh`.
3. For a static-ad-pack agent, wire it to call the gateway's image-generation endpoint for roughly 40 variations a week, upload outputs to R2, and push them to the Facebook Ads API as paused drafts for human review.
4. For a UGC-video agent, have it pull top-converting angles/scripts from the warehouse via SQL, generate footage and captions through the gateway's video endpoint, and land the output in object storage.
5. For an enrichment agent, have it call Apify to scrape the target market, then run the gateway's enrichment waterfall (Apollo, then GetLeads, then email permutation), then Million Verifier, writing confirmed rows to the leads table.
6. For a cold-email agent, connect Instantly for sending and a webhook for reply classification, letting the agent auto-handle simple replies and Slack a human only the ambiguous ones.
7. For an analytics agent, give it query access to the warehouse and have it answer specific recurring business questions (e.g., cost per qualified lead by channel) directly in SQL.
8. Add a cron line and Slack channel for the new agent, following the same narrow-scope, single-job pattern used for the core infrastructure pieces.

**Tools:** Claude Code, Nano Banana, Seedance, Cloudflare R2, Facebook Ads API, Apify, Apollo, GetLeads, Million Verifier, Instantly

### 12. Give every generated asset a hosted, idempotent URL  `01.6`
*useful · ai workflows · source 01*

The moment agents start generating images or video, they need object storage that produces a public URL, because every ad platform, CMS, and social scheduler requires a hosted file rather than something sitting in a local `/tmp` directory. The upload module should be idempotent on content hash (so regenerating the same asset never creates a duplicate), follow a fixed naming convention, and log every upload — including the generating prompt, model, and cost — to a Postgres table.

> "Generated creative that lives in `/tmp` is creative that doesn't exist"

**How to do it**

1. Set up Cloudflare R2 (no egress fees, useful since ad platforms and CDNs repeatedly re-pull the same video) or S3 if already on AWS.
2. Give Claude Code the object-storage prompt (see prompt field) to create buckets for creatives, video, and exports.
3. Build an `upload(localPath, folder)` function that pushes the file, returns a public CDN URL, and is idempotent on content hash so regenerating the same asset never creates a duplicate.
4. Enforce a naming convention of `{agent}/{yyyy-mm-dd}/{asset-type}/{slug}-{hash8}.{ext}` for every uploaded file.
5. Write every upload to a `creative_assets` Postgres table recording the URL, the agent that made it, the prompt used, the model, and the cost.
6. Add a scheduled cleanup job that deletes anything in the exports bucket older than 30 days.
7. Confirm every downstream integration (Facebook Ads API, CMS, social scheduler) receives the hosted CDN URL rather than a local file path.

**Tools:** Claude Code, Cloudflare R2, AWS S3, Backblaze B2, Postgres

**Prompt / template:**

```text
Set up Cloudflare R2 as object storage and build a small upload module the agents import. Requirements: (1) Buckets for creatives, video, and exports. (2) An `upload(localPath, folder)` function that pushes the file, returns a public CDN URL, and is idempotent on content hash so regenerating the same asset doesn't create duplicates. (3) A naming convention: `{agent}/{yyyy-mm-dd}/{asset-type}/{slug}-{hash8}.{ext}`. (4) Write every upload to a `creative_assets` Postgres table with the URL, the agent that made it, the prompt used to generate it, the model, and the cost. (5) A cleanup job that deletes anything in exports older than 30 days.
```

**Pitfall:** Generated creative left in a local `/tmp` directory is unusable, since every ad platform, CMS, and social scheduler requires a hosted URL rather than a raw file — and without idempotent hashing, regenerating the same asset silently creates duplicates.

### 13. Harden lead-qualification agents by fixing edge cases after each run  `27.5`
*useful · ai workflows · source 27*

The speaker's "front-end sales agent" emails people who book a demo but sign up with a generic address to ask whether they have a domain to demo the product on; replies are often messy and hard to parse programmatically (in one case, someone pasted a screenshot of a JPEG link instead of typing a URL), yet the agent extracted enough signal to search for the business, confirm it with the person, generate a report, and send it. The stated method for building this kind of agent is explicitly iterative: every time it runs, you review the interaction and look for a behavior a human wouldn't have done — in one instance the agent asked an unnecessary confirmation question that bothered the recipient, so it was corrected on the spot. The broader lesson is that edge cases in messy human input can only be built in "bit by bit" through repeated real runs, not anticipated up front, and each fix can surface new edge cases in turn.

> "every time you run one you need to look at it"

**How to do it**

1. Build a narrow agent for one messy-input task, e.g., extracting a business domain from an unstructured email reply.
2. Deploy it on real interactions rather than only synthetic test cases, since messy real-world replies (screenshots, partial links, non-standard phrasing) are what actually breaks parsers.
3. After each run, read the full interaction transcript yourself rather than only checking the final output.
4. Flag any moment where the agent did something a careful human wouldn't have done, e.g., asked an unnecessary question, over-confirmed, or under-confirmed.
5. Update the agent's instructions or logic to specifically handle that one edge case.
6. Repeat this run-review-fix cycle continuously, expecting that fixing one edge case can reveal new ones rather than converging quickly.

**Pitfall:** Assuming you can anticipate all edge cases before launch is unrealistic — the source's process only works because every run is reviewed and each discovered bad behavior, like an unnecessary confirmation email, is patched individually after the fact.

### 14. Have Perplexity write the n8n JSON for you  `61.8`
*useful · ai workflows · source 61*

A specific and cheap trick Cody had found two weeks before recording. n8n workflows are entirely JSON-based, so you can describe the automation you want to Perplexity, tell it to write a JSON file structured for n8n, and paste the result in - the workflow is built out without you doing the connectivity work. His example of what he described: connect an Apify YouTube channel email scraper, give it a list of keywords, scrape the emails from those channels, send them to MillionVerifier to validate, then send them to an Instantly campaign for sending. Research, validation and cold email sending all automated from one description. He's honest that it's super early and not perfect every time. Jordan's reaction is the more useful framing for a reader: he doesn't care about the specific tools in that stack, but hearing it described gives him ten light-bulb moments he can apply to his own processes - the value is in the pattern, not the pipeline.

> "you can basically have Perplexity write"

**How to do it**

1. Write out the automation you want in plain language, naming each tool and the order of operations.
2. Ask Perplexity to output a JSON file structured for n8n that implements it.
3. Paste the JSON into n8n to instantiate the workflow, including the node connections.
4. Add your credentials and test each node, since the generated version won't be perfect.
5. Iterate by re-describing the parts that failed rather than rebuilding by hand.
6. Use the same approach to teach a team the pattern, since the description is the reusable artefact.

**Tools:** Perplexity, n8n, Apify, MillionVerifier, Instantly

**Prompt / template:**

```text
I'm trying to automate this: connect an Apify YouTube channel email scraper, give it a list of keywords, have it scrape all the emails from those YouTube channels, send them to MillionVerifier to validate, then send them into an Instantly campaign. Write a JSON file structured for n8n that builds this workflow.
```

**Pitfall:** Cody says elsewhere in his own material that he prefers going straight to code over automation tools precisely because they're fragile and hard to modify - this trick lowers the cost of building an n8n workflow, not the cost of maintaining one.

**Apply:** Useful for Pabau's one-off internal automations where a visual workflow is genuinely easier to hand over - but anything that has to be maintained long term is better as code.

### 15. Keep AI out of the pitch copy itself  `33.4`
*useful · ai workflows · source 33*

The guest draws a clear automation boundary: topic ideation "still can't be automated" because it needs human judgment about what will actually land or go viral, media-list building is only partly automatable (many niche/industry journalists aren't on Muck Rack and require manually reviewing a trade publication's own writers), and the pitch email itself is deliberately kept manual. The stated reason is reputational: he's active in media/journalist groups where people compare notes and repeatedly complain about receiving obviously AI-generated pitches, so he always takes a final manual look before sending rather than risk his name and company being flagged as an AI-pitch source. In practice, personalization is done efficiently rather than manually from scratch, using the outreach tool's browser extension to view the journalist's own article alongside the email draft while writing.

> "worried about it sounding super AI-generated and fake"

**How to do it**

1. Do not rely on full automation for topic ideation — treat it as requiring human judgment about timing and virality potential.
2. Use Muck Rack to semi-automate media-list discovery for well-covered beats, but manually supplement it for niche/industry journalists not listed there by visiting the trade publication directly and reviewing its writers' other bylines.
3. Do not generate the outward-facing pitch email copy with AI, even though it is technically possible.
4. Instead personalize each pitch using a side-by-side workflow: open the outreach tool's browser extension (e.g. BuzzStream's Chrome extension) so the journalist's own article shows on one side while you draft the email on the other.
5. Always take a final manual read-through and edit pass on every pitch before sending, regardless of what was tool-assisted earlier in the process.
6. Reserve AI use for lower-risk, internal tasks elsewhere in the pipeline (e.g. drafting survey questions) rather than the external-facing pitch text.

**Tools:** Muck Rack, BuzzStream

**Pitfall:** Fully automating pitch copy with AI risks being recognized as an AI-generated pitch by journalists who compare notes in professional groups, which can permanently damage outreach credibility with that entire network.

### 16. Layer agent reports and set proactive exception alerts  `27.11`
*useful · ai workflows · source 27*

For multi-agent systems, the described QA method is to require every single agent output to be checked, starting with logging: each agent run generates its own report of what it actually did, and when multiple agents run in parallel, the example given is five at once, their five individual reports get rolled up into one summary report, letting a human review a large multi-agent operation in layers instead of reading every underlying chat. On top of that, agents are configured to proactively message the user's inbox the moment a defined trigger condition is met, "if you see this, message me immediately," regardless of how deeply nested that agent is in the system — used in practice so that a stalled or failed front-end sales agent, e.g., one that can't get a prospect's domain, or gets no response, surfaces immediately instead of requiring the human to dig through the full chat history to notice the problem.

> "If you kick off five of them, you get five reports"

**How to do it**

1. Configure every agent in your pipeline to generate a structured report of its own actions at the end of each run.
2. When running multiple agents in parallel on one job, collect all of their individual reports.
3. Build or prompt a summary agent/step that rolls those individual reports up into one top-level report for human review.
4. Review the top-level summary report first, and only drill into an individual agent's full report or chat log when the summary flags a problem.
5. Define specific trigger conditions that matter for your use case, e.g., a stalled task, a missing required input, no response from a contact.
6. Configure each relevant agent to send an immediate inbox or message alert the moment one of those trigger conditions is met, rather than waiting for the next scheduled review.

**Pitfall:** Relying on reading full chat transcripts to catch problems in a multi-agent system doesn't scale — the source's fix is layered summary reports plus real-time trigger-based alerts, so problems surface without a human having to read through everything.

### 17. Marketing tasks are now API calls, not one-off campaigns  `01.1`
*useful · general insights · source 01*

The article's central thesis is that nearly every marketing task has an API-shaped equivalent: a UGC video is Seedance JSON, a static ad is an image-model API call, data analytics is a SQL query, cold-email inbox management is a webhook, and waterfall enrichment is API calls in a for loop. Because of this, the author argues the thing worth building isn't any single campaign but 'the factory that makes campaigns' — persistent infrastructure that produces campaign-shaped outputs on demand, rather than treating each campaign as a bespoke one-off project.

> "Every marketing task worth doing is now an API call"

**Evidence:** "A UGC video is just Seedance JSON. A static ad is just an image model API call. Data analytics is just a SQL query. Cold email inbox management is just a webhook. Waterfall enrichment is just API calls in a for loop."

**Apply:** You should audit recurring marketing/SEO tasks (keyword-research pulls, GSC reporting, internal-link audits, content briefs) for which ones are essentially 'an API call, a database row, or a cron job' in disguise, and prioritize building small persistent automations for those rather than repeatedly re-running one-off Claude Code sessions by hand.

### 18. Pipe an Airtable video/metadata base into YouTube via n8n and an agent  `28.7`
*useful · ai workflows · source 28*

To bulk-upload thousands of videos with metadata already prepared, the team's first attempt was to point an AI agent directly at an Airtable base containing all video links and metadata and ask it to publish them to YouTube, which failed outright at the time because, in Endre's telling, the agents weren't as good and the pipeline wasn't as developed in 2025. The setup that actually worked was an n8n workflow that read from the same Airtable, holding all metadata, and drove an agent to upload the maximum allotted number of videos each day, applying the on-page optimization such as titles and descriptions automatically as part of the same run, described as the gold standard approach at the time.

> "the gold standard was an n8n workflow going from"

**How to do it**

1. Build an Airtable base with one row per video asset, including the source file link and all metadata needed for the destination platform, such as title, description, tags, and target keyword.
2. Build an n8n workflow that reads unprocessed rows from that Airtable base on a schedule (inferred: a daily trigger, matching the platform's daily upload cap).
3. Within the n8n workflow, call an upload/agent step that pushes each video to YouTube via its API, applying the title and description fields directly from the Airtable row.
4. Cap the daily batch size in the workflow to match your current platform upload limit so the workflow doesn't fail on rate limits.
5. Mark each Airtable row as uploaded once the workflow confirms success, so the next scheduled run only processes remaining rows.
6. Spot-check a sample of uploaded videos manually against their Airtable source to confirm metadata mapped correctly before scaling to the full catalog (inferred).

**Tools:** n8n, Airtable, YouTube

**Pitfall:** Pointing a general AI agent directly at the Airtable base without a structured workflow, their first attempt, failed outright — the more reliable pattern was an explicit n8n workflow driving the agent step by step, not an open-ended agent operating on its own.

### 19. Save a recurring GSC-to-Claude analysis as a reusable Claude skill  `02.6`
*useful · best practices · source 02*

Once the export-and-classify process (Analytics Edge export, then Claude analysis with the AI Mode prompt) is working correctly for one site, it should be converted into a saved, reusable Claude skill rather than rebuilt from scratch each time, so the same AI Mode query analysis can be run again quickly across other sites or client accounts in the future.

> "you can easily turn it into a skill that can be used"

**How to do it**

1. After successfully running the export-and-classify workflow manually once, identify the exact working steps used (data source, prompt text, output format) as the basis for a skill.
2. Save the working prompt and process as a Claude skill (inferred: use Claude's skill-creation feature to persist the project setup and prompt so it can be invoked by name later).
3. Test the saved skill against a second, different site's exported GSC data to confirm it generalizes rather than being hard-coded to the first dataset's specifics.
4. Reuse the skill on a recurring basis (inferred: monthly or quarterly) across every site or client account where AI Mode visibility needs tracking, rather than re-writing the prompt each time.

**Tools:** Claude

### 20. Split multi-agent pipelines into stateless workers and one stateful orchestrator  `50.5`
*useful · ai workflows · source 50*

The content pipeline's agent architecture deliberately separates two agent types. "Stateless" agents, the example given is one named Sage, wake up, are assigned exactly one task such as researching and drafting one specific article, complete it, and go back to sleep with no persistent memory of anything else. A single "stateful" agent, named Open Claw in this system, maintains ongoing memory, context, and an overarching mission across the whole pipeline, effectively acting as the project manager that assigns work to the stateless workers and tracks the bigger picture. This split keeps individual task-execution agents simple, cheap, and easy to reason about, since they only ever need context for their one task, while concentrating all long-term context and coordination logic in a single orchestrating agent.

> "these are what we call stateless agents"

**How to do it**

1. Map out every discrete task in your content pipeline, such as researching one topic, drafting one article, or checking one page's information gain, as a candidate for a stateless worker agent.
2. Build or configure each stateless worker so it receives only the specific task's inputs, has no memory of prior tasks, completes its one job, and terminates or returns to idle.
3. Designate one agent as the stateful orchestrator, giving it persistent memory, an overarching mission definition, and the ability to assign tasks to the stateless workers.
4. Route all task creation and prioritization decisions through the stateful orchestrator rather than letting stateless workers pick their own next task.
5. Give the stateful orchestrator visibility into task status, such as backlog, queued, in progress, and needs review, so it can move work through the pipeline (inferred status-tracking requirement).
6. Test the split by removing or resetting a stateless worker's context between tasks to confirm it truly carries no memory forward, catching accidental state leakage (inferred verification step).

### 21. The harness matters more than the model - and lets you swap in a cheap clone  `56.10`
*useful · ai workflows · source 56*

Cody explains the quality gap people notice between a chat UI and a raw API call as being entirely about the harness - the tooling around the model that lets it do recursive loops and think through actions. He estimates Claude Code exposes around 38 tools to the agent, and says the same model gets measurably smarter inside that harness because the harness is built to use the model at full capability. Straight to the API he has to write section by section to get quality; inside the harness he can often get it first try. The arbitrage he had just found: Claude Code ships an SDK, so you can use the harness anywhere - including in the cloud rather than on your laptop - and hot-swap in an open-source model trained on Opus (he names MiniMax 2.5, which he says identifies itself as Claude Opus 4.6 at temperature zero) at roughly a twentieth of the cost. He is candid that he doesn't have polished workflows for this yet.

> "It really depends on the harness"

**How to do it**

1. Stop comparing raw API output to chat UI output - assume the difference is the harness, not the model.
2. For anything multi-step, run the model inside an agent harness with tool access rather than making single API calls.
3. If you must use the raw API, force the work into stages - outline, then section by section, then a revision pass - to compensate.
4. To scale, use the harness's SDK so it can run in the cloud instead of on a laptop.
5. Test whether a cheaper open-source model distilled from the frontier model gives acceptable quality inside that same harness.
6. Benchmark on your own outputs before switching, and keep the expensive model for the stages where quality gaps show.

**Tools:** Claude Code, Claude, MiniMax

**Pitfall:** Cheap clone models inside a good harness is an experiment he was two weeks into, not a validated setup - and switching model families (OpenAI to Anthropic or back) forced a full retooling of his agents because the failure modes changed.

**Apply at Pabau:** For Pabau, the lesson is to invest in the harness and the context, not in chasing models - and to expect real rework if an agent's underlying model family is ever changed.

**Apply anywhere:** Invest in the harness and the context rather than chasing models - and expect real rework if an agent's underlying model family is ever changed.

### 22. Treat SEO agents as productized software, not bespoke automations  `77.8`
*useful · general insights · source 77*

Schneider closes by pointing readers to a commercial product that packages the pipeline he described. The wider signal matters more than the specific vendor: the keyword-to-research-to-write-to-publish-to-refresh loop is now something bought off the shelf rather than built. That changes the competitive picture in any commercial niche. If the loop is purchasable, assume competitors are running it, which means bottom-funnel keywords with obvious commercial value get covered by machine-generated pages quickly and continuously refreshed on a 30-day clock. The defensible response is not to run the same loop faster. It is to put things in the content that a scrape-and-write agent cannot produce: original data, first-hand product knowledge, built visuals, and named expertise.

> "If you want this get it here"

**Evidence:** Schneider markets the described agent as a purchasable product at graphed.com.

**Pitfall:** Reading a productized pipeline as a reason to buy one is the wrong conclusion. Everyone buying it publishes against the same scraped page-one corpus, so the output converges and the differentiator moves to whatever the scrape cannot see.

**Apply at Pabau:** Pabau's advantage over a scrape-and-write competitor is what only Pabau has: product screenshots, real workflow knowledge from aesthetic practices, original built visuals and named authors. Every article should carry at least one of those, which is already the house rule.

**Apply anywhere:** Assume competitors can buy the same scrape-and-write pipeline. Compete on what an agent reading page one cannot produce: original data, first-hand operational knowledge, purpose-built visuals and named expertise.

### 23. Use Claude/ChatGPT to turn articles into gated conversion quizzes  `13.14`
*useful · ai workflows · source 13*

Edward's repeatable content-to-conversion pipeline: take a finished article, feed it to an AI model such as Claude, and prompt it to generate quiz questions based on that article's content; he had Claude additionally build a quiz template matching his site's existing design system. The quizzes are embedded into articles, and on successful completion the quiz delivers a sales pitch framed as a reward rather than a cold CTA. Both speakers caveat that current AI tools are weak at this without heavy prompting and iteration, noting it takes a lot of prompting and that AI is similarly clumsy at generating infographics or animations on the first pass, so the workflow requires iterative refinement rather than a single-shot prompt.

> "give it to the AI of your choice, and say"

**How to do it**

1. Select a finished, published article that already gets meaningful traffic as the candidate for a quiz.
2. Open Claude or ChatGPT and paste the full article text into the chat.
3. Prompt the model to come up with a few quiz questions based on this article, expanding the prompt with a desired question count and format such as multiple-choice if the first output is too generic.
4. Separately, prompt Claude to generate an HTML/CSS quiz template matching your site's existing visual design, providing brand colors, fonts, or a reference page as context (inferred: describe or attach your design system in the prompt).
5. Review the generated questions against the source article for accuracy; do not publish AI-generated quiz content unchecked, since this workflow is explicitly described as needing heavy iteration.
6. Embed the finished quiz within the article body as a mid-content break rather than only at the end (inferred placement).
7. Configure a pass end-state that leads into a sales pitch or offer framed as a reward for completing the quiz, rather than a generic CTA.
8. Iterate the prompt across two to three rounds if the first draft of questions or design feels generic, since both speakers note this format needs more prompting effort than typical AI content tasks.

**Tools:** Claude, ChatGPT

**Prompt / template:**

```text
come up with a few quiz questions [based on this article]
```

**Pitfall:** Expecting a single prompt to produce a good quiz or infographic — Edward says AI is bad at this on the first attempt and it takes a lot of prompting, especially for animations and infographics, so budget for iteration rather than one-shot generation.

### 24. Use a Google Sheets AI formula to pre-filter hundreds of job applicants  `35.5`
*useful · ai workflows · source 35*

To hire a video editor, Edward posted on YTJobs.co with an external application form feeding a Google Sheet (rather than the platform's built-in application flow), collecting around 20 free-text questions from roughly 300 applicants. Instead of reading every answer, he picked two diagnostic questions whose answers reveal an underlying trait rather than a simple fact — knowing how to inspect element in Chrome (a proxy for technical curiosity/effort) and owning a MacBook (a proxy for creative orientation) — and scored every applicant's free-text answer to each with a Google Sheets `=AI()` formula carrying a strict yes/no evaluation prompt, cutting 300 applicants down to 40 for manual review.

> "do you know how to inspect element in Chrome"

**How to do it**

1. Post the job opening on YTJobs.co (or an equivalent niche job board) using an external application form (e.g., a Google Form) instead of the platform's built-in apply flow, so every response lands in one Google Sheet.
2. Design the application with up to about 20 questions, including open free-text fields rather than only yes/no checkboxes, so nuance can be captured and scored later.
3. Include at least one or two 'diagnostic' free-text questions whose answer reveals an underlying trait rather than a simple fact (e.g., 'Do you know how to inspect element in Chrome?' or 'Do you have a MacBook?').
4. In a new column beside each diagnostic question's responses, add a Google Sheets `=AI(...)` formula referencing that response cell with a strict evaluation prompt such as: 'Does what this person said mean that they know how to inspect element in Chrome? Only answer yes or no.'
5. Drag/fill that formula down the entire column so every applicant row is scored automatically against the same yes/no prompt.
6. Repeat the formula setup for the second diagnostic question in its own column.
7. Filter or sort the sheet on the resulting yes/no columns to shortlist applicants who pass the diagnostic checks.
8. Manually review only the shortlisted applicants (300 down to about 40 in this case) in depth to make the final hiring decision.

**Tools:** Google Sheets (=AI formula), YTJobs.co, Google Forms

**Prompt / template:**

```text
Does what this person said mean that they know how to inspect element in Chrome? Only answer yes or no.
```

**Pitfall:** Trying to manually read every open-ended answer across hundreds of applicants (20 questions times roughly 300 respondents) instead of pre-filtering with one or two targeted diagnostic questions scored automatically by AI first.

### 25. Work out of the agent, not the SaaS UIs  `56.23`
*useful · ai workflows · source 56*

Asked which automation gave him the most alpha, Cody's answer is email access via Claude Code - he OAuth'd all of his email accounts into it and now triages out of the agent, which matters because he gets around 100 cold emails a day. Connected to the rest of his tooling it compounds: with the Notion API wired in he can point at a meeting-recording link and have the follow-up email written and dropped into his inbox as a draft. The broader shift, which he says happened over about six weeks, is that he doesn't really touch UIs anymore. His product-email example runs end to end without opening the vendor's interface: internal conversation transcript in, Claude Code writes the copy using the skill he has for it, pushes it as a draft into SendGrid, sends him a test, takes his design notes, and revises - all without him being in the SendGrid UI. He runs five windows at once, jockeying agents. He also rebuilt a whole LinkedIn-engager-to-cold-email pipeline (PhantomBuster, Apollo or Lead Magic for enrichment, MillionVerifier for validation, Instantly for sending) in about 30 minutes, now running perpetually on a server. His internal joke is 'friends don't let friends do n8n' - going straight to code is more malleable and the system can evolve, where automation tools are fragile and hard to modify.

> "having access to my email via Claude Code"

**How to do it**

1. Start by connecting the highest-volume, lowest-value surface you touch - for him, email triage across multiple accounts.
2. Put every API key for your stack into an environment file the agent can read, and add each new one as you go.
3. Connect the adjacent systems (notes, CRM, sending tools) so the agent can chain steps rather than doing one.
4. Have the agent write into drafts and staging states rather than sending, so a human stays in the loop.
5. Re-implement existing multi-tool automations directly in code instead of in a visual automation tool, so they can be modified later.
6. Deploy the ones that need to persist onto a server rather than running them from your laptop.
7. Run several agent sessions in parallel and treat your job as conducting them, not doing the middle work.

**Tools:** Claude Code, Notion, SendGrid, Apollo, MillionVerifier, Instantly

**Prompt / template:**

```text
Here's the Notion link to the meeting recording. Write the follow-up email and put it as a draft into my inbox.
```

**Pitfall:** OAuthing an agent into every email account is exactly the broad-permission setup he warns about elsewhere in the same conversation, having seen an agent delete a Gmail account's contents. Draft-only permissions and narrow scopes are the mitigation.

**Apply at Pabau:** The transferable idea for Pabau is drafting rather than doing: an agent that assembles the pull request, the WordPress draft, or the outreach email and leaves it for review captures most of the speed with none of the risk of letting it publish.

**Apply anywhere:** The transferable idea is drafting rather than doing: an agent that assembles the pull request, the CMS draft, or the outreach email and leaves it for review captures most of the speed with none of the risk of letting it publish.

### 26. Wrap every external API in one internal gateway service  `01.11`
*useful · ai workflows · source 01*

Instead of letting every agent hold its own API keys and write its own fetch/retry logic for image generation, video generation, scraping, enrichment, verification, and sending, build one internal gateway service that all agents call, which then calls the actual vendor. This centralizes key storage (so keys can actually be rotated, instead of being 'sprayed across nine agent folders' where they 'never get rotated, they just leak'), adds a response cache keyed on the request body that the author says 'pays for the whole build in about a month' since agents constantly re-request the same domain or prompt, and lets you swap an enrichment provider by editing one YAML waterfall config instead of six agents.

> "The response cache pays for the whole build in about a month"

**How to do it**

1. Give Claude Code the gateway-build prompt (see prompt field) to wrap every external provider the agents use: image generation (Nano Banana via Kie AI or fal.ai), video generation (Seedance), scraping (Apify actors), enrichment (Apollo, GetLeads), email verification (Million Verifier), and sending (Instantly, HeyReach).
2. Expose one consistent internal interface: POST /generate/image, POST /generate/video, POST /scrape/{actor}, POST /enrich/contact, POST /verify/email, POST /send/email.
3. Store all vendor API keys only inside the gateway's environment; issue agents a single internal token instead of vendor keys.
4. Add per-provider rate limiting and exponential-backoff retry logic on 429/5xx responses inside the gateway, not in each individual agent.
5. Add a response cache keyed on the request body so re-enriching the same domain, or regenerating the same prompt/actor input, within a window costs nothing.
6. Log every call to the `api_costs` table with provider, units, and dollar cost.
7. Implement a waterfall mode specifically for enrichment: try providers in a configured order and stop at the first result that passes verification.
8. Add a health check per provider that triggers a Slack alert when a provider starts failing or a key expires.
9. When swapping an enrichment provider later, change the waterfall order in one YAML config file rather than editing every individual agent.

**Tools:** Claude Code, Kie AI, fal.ai, Apify, Apollo, GetLeads, Million Verifier, Instantly, HeyReach, Slack

**Prompt / template:**

```text
Build an internal API gateway service that wraps every external provider our agents use. Providers and methods: image generation (Nano Banana via Kie AI or fal.ai), video generation (Seedance), scraping (Apify actors), enrichment (Apollo, GetLeads), email verification (Million Verifier), sending (Instantly, HeyReach). Requirements: (1) One consistent interface — POST /generate/image, POST /generate/video, POST /scrape/{actor}, POST /enrich/contact, POST /verify/email, POST /send/email. (2) All vendor API keys live only in the gateway's env — agents get a single internal token. (3) Per-provider rate limiting and exponential-backoff retry on 429/5xx. (4) A response cache keyed on the request body, so re-enriching the same domain twice in a week is free. (5) Every call writes a row to `api_costs` with the provider, units, and dollar cost. (6) A waterfall mode for enrichment: try providers in a configured order and stop at the first result that passes verification. (7) Health check per provider and a Slack alert when one starts failing or a key expires.
```

**Pitfall:** Keys sprayed across nine separate agent folders never get rotated, they just leak — decentralizing provider API keys across every agent both duplicates retry logic and makes key rotation practically impossible.

### 27. n8n as the backend, Lovable as the marketer-facing dashboard  `61.9`
*useful · ai workflows · source 61*

The pattern Cody describes as the practical answer to internal tooling marketers will actually use. The functionality lives in an n8n backend; the front end is generated with Lovable, connected back via HTTP/REST endpoints so data pulled by the workflow displays in the interface. The example he cites came from a head of growth who used it to automate her own job: rather than hiring a VA, she had it screenshot every competitor's ads daily, identify which ads were new and what competitors were trying that she wasn't, and built a dashboard so all the insights sat in one place. His framing of why this matters: it's internal tooling a marketer would actually want to use - 'I don't want to touch Retool, I don't want to touch Metabase.' Jordan's parallel is that he no longer opens Figma for a product or dashboard idea; he mocks the interface up in Bolt or Replit knowing the backend is throwaway, because the developer can see the vision and start from that ground level. He also sends clients Netlify-hosted proposals with an ROI slider built in Bolt.

> "using n8n as the back end"

**How to do it**

1. Define the recurring analysis you want and build the data collection as an n8n workflow.
2. Expose the results over an HTTP/REST endpoint the front end can call.
3. Generate the interface with Lovable and wire it to that endpoint - no backend work.
4. Keep the interface aimed at the person who'll use it daily rather than at a BI tool's conventions.
5. For product ideas rather than dashboards, mock the interface in Bolt or Replit and treat the backend as disposable.
6. Hand the mock to a developer as the specification instead of a written brief.

**Tools:** n8n, Lovable, Bolt, Replit, Netlify

**Pitfall:** Jordan is explicit that the vibe-coded backend is trash and shouldn't be deployed - it's a specification device, and treating a mock as production is where this goes wrong.

**Apply at Pabau:** For Pabau, this is how to prototype an internal marketing dashboard or a customer-facing calculator quickly - build the mock to communicate the idea, then have it built properly rather than shipping the prototype.

**Apply anywhere:** This is how to prototype an internal marketing dashboard or a customer-facing calculator quickly - build the mock to communicate the idea, then have it built properly rather than shipping the prototype.
