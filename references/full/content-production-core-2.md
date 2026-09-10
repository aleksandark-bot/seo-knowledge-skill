# Content Production — core (part 2 of 8)

25 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Build the agent a walled garden, not a blank page  `56.9`
*core · best practices · source 56*

Cody's framework for getting quality out of any AI tool is to define the sandbox it lives in rather than the task alone. He describes providing 'all of my noes' - the constraints that define what a yes looks like - because an open instruction like 'do this' leaves the agent free range and the output could go anywhere. The contrast he draws: 'here is this walled garden that you can live within, here are the resources you have available, now go do this thing' produces output he actually wants. He applies the same logic to writing (persona plus source corpus plus explicit instruction on where to sell) and to agents generally: 'these agents can do anything so they will do anything, so you have to create that boundary for them to live within.' His email-newsletter example makes the persona point concrete - 'write me an email newsletter' is terrible, 'write me an email newsletter as a top 1% direct response marketer, educational and conversational, don't start soft-selling until about 75% of the way down' is not.

> "here is this like walled garden that you can live"

**How to do it**

1. Before writing the task instruction, write the constraints: what the output must not do, what tone is off-limits, what claims are not allowed.
2. Give the agent an explicit persona at the level of expertise you want ('a top 1% direct response marketer'), not a generic role.
3. Attach the resources it is allowed to draw on - source material, transcripts, style guide - and say that it should not go outside them.
4. State structural rules explicitly, including where in the piece it is allowed to sell.
5. For agents rather than one-shot prompts, restrict the tools and the data it can reach as part of the same boundary.
6. Iterate on the boundary rather than the task wording when the output is wrong.

**Tools:** Claude, ChatGPT

**Prompt / template:**

```text
Write me an email newsletter as a top 1% direct response marketer would write it - educational and conversational in tone. Do not start soft-selling until about 75% of the way down the piece. Write only from the source material provided below; do not introduce facts that are not in it.
```

**Pitfall:** He is explicit that poor output usually isn't a knowledge gap - it's not having the vocabulary to transfer what you know into the instruction. If you can't articulate what good looks like in your own field, the agent can't either.

**Apply:** Pabau's content prompts should carry the constraint set - the non-negotiables, the terminology rules, the claims that are off-limits - not just the topic, because the guardrails are what separate usable output from generic AI copy.

### 2. Build the paid test project from a piece you already published  `167.5`
*core · concrete actions · source 167*

Grow and Convert make the test project an exact replica of real client work, only shorter and never used for anything. They reuse a past published piece and hand the applicant the same inputs they had when writing it, so the submission can be compared directly with what they produced. They use the same piece for every applicant so responses can be benchmarked against each other as well. The deliverable is deliberately partial: the angle of the article is given, and the writer produces a list of pain points, a full introduction, and an outline. They say they do not need a full article to judge fit. Those three pieces answer how the writer positions the client product, whether the positioning is specific, and whether it matches house style. They warn against copying their exact test and say to use the same prompt and level of information you give your current writers.

> "an exact replica of our actual client work"

**Evidence:** Grow and Convert reuse a single past client piece as the standard test project so applicants can be benchmarked against their own published version and against one another.

**How to do it**

1. Pick one article you have already published and still consider good.
2. Gather the exact inputs you had at the time: the angle, the interview notes, the keyword, the client background.
3. Write the test brief with that same information and no more, so it mirrors real conditions.
4. Ask for three deliverables only: a list of pain points, a full introduction, and an outline.
5. Use the same test article for every applicant so you can rank submissions against each other.
6. Compare each submission against your own published version as the benchmark.
7. Score three things separately: how they position the product, how specific it is, and how close it sits to your style.
8. Keep the test unpublished so nobody is doing unpaid production work.

**Pitfall:** Inventing a bespoke test brief for each candidate, or copying someone else's test. Both destroy the benchmark. Without one fixed piece and one fixed set of inputs you cannot tell a strong applicant from an easy brief.

**Apply at Pabau:** David should keep one published Pabau article as the permanent writer test: hand over the same brief and expert notes, ask for pain points, intro and outline, and compare against the live piece.

**Apply anywhere:** Turn one article you already published into a permanent test project. Give applicants the same inputs you had, ask for pain points, an intro and an outline, and benchmark against your own version.

### 3. Build the paid test project from an article you already published  `164.4`
*core · concrete actions · source 164*

Grow and Convert's second filter is a paid test project that is an exact replica of real client work, shortened and never published. They use a piece they already produced for a client and give the applicant the same inputs they had when writing it, so they can compare the applicant's output directly to their own. They deliberately use the same piece for every applicant so responses benchmark against each other. They do not ask for a full article. They ask for a list of pain points, a full introduction and an outline, which they say is enough to judge how the writer positions the client's product, whether it is specific, and whether it matches house style. Their warning is not to copy their exact brief but to hand over the same prompt and level of information your current writers get, so you see real performance.

> "an exact replica of our actual client work"

**Evidence:** Grow and Convert use one previously published client piece for all applicants so submissions can be benchmarked against each other and against their own version.

**How to do it**

1. Pick one article you have already published and keep it as the fixed test piece for all applicants.
2. Gather the original inputs you had when writing it: the angle, the keyword, the interview notes.
3. Ask the applicant for three deliverables only: a list of pain points, a full introduction, and an outline.
4. Give exactly the brief and level of information your current writers receive, no more.
5. Compare each submission side by side against your published version and against other applicants.
6. Judge three things: how the product is positioned, whether the detail is specific, and style fit.
7. Tell the applicant upfront the work will not be published, and pay for it regardless.

**Pitfall:** Asking for a whole article. It costs the applicant hours, costs you more to pay for, and Grow and Convert say pain points plus intro plus outline already answers every question you have.

**Apply at Pabau:** David should keep one already-published Pabau article, with its original brief, as the standing test project. Applicants deliver pain points, intro and outline only, which takes an hour to review.

**Apply anywhere:** Build your paid test from an article you already published, hand over the original inputs, and ask only for pain points, an introduction and an outline. Use the same piece for everyone so submissions benchmark against each other.

### 4. Build webinar topics from named knowledge gaps and outside experts  `168.9`
*core · concrete actions · source 168*

CPC Strategy never used a standard webinar framework. Nii Ahene describes a single north star instead: education. Topic selection worked by scanning the industry for subjects that appeared to have gaps in knowledge, then building a session specifically to fill that gap. To fill it credibly, each webinar featured subject-matter experts, drawn either from partners such as Google or from CPC Strategy's own staff. The two rules together are what make it repeatable without a template. The gap scan supplies the topic, so the calendar is never invented from thin air, and the expert supplies the authority, so the session teaches something the audience could not get by reading a blog post. Tinuiti now runs this weekly, at 60 webinars in 2019.

> "target any subjects that appeared to have gaps in knowledge"

**Evidence:** Tinuiti runs a new webinar every week and hosted 60 in 2019, with dedicated full-time staff responsible only for webinar coordination and outreach.

**How to do it**

1. Each month, list the questions your team is answering repeatedly on sales and support calls that no good public resource covers.
2. Add the platform or regulatory changes where the vendor's own documentation is thin or confusing.
3. Score each candidate on how many people it affects and how badly the existing public explanation fails.
4. Assign each chosen topic a named subject-matter expert, either from a partner organization or from your own staff.
5. Invite the platform or vendor itself onto the session when the topic is their change, since their presence is the differentiator.
6. Set the session goal as the audience being able to act afterward, not as a product demo.
7. Fix a cadence and hold it, weekly if you have the staff, and staff the coordination and outreach as a dedicated role.
8. Publish the recording and slides, then turn each session into a blog post and a clip series.

**Pitfall:** Picking topics you can present rather than gaps the audience has produces well-run webinars with low attendance. The signal is repeat registrants declining while your topic list looks internally sensible.

**Apply at Pabau:** Pabau can run monthly sessions on the exact operational gaps aesthetic practices face, with a named clinician or practice manager as the expert rather than a Pabau product person. Each session then becomes a blog article and a set of clips.

**Apply anywhere:** Build the webinar calendar from gaps your sales and support calls reveal, assign a named subject-matter expert or the vendor itself to each one, hold a fixed cadence, and repurpose every recording into written content.

### 5. Buy Facebook clicks to a pain-point piece before it ranks  `110.4`
*core · concrete actions · source 110*

Grow and Convert describe a client four months into an engagement. One of their early mid-funnel pain-point pieces produced eight conversions, split across two URLs because of ad UTMs, entirely from paid Facebook promotion, on only 600 sessions. That matched the highest-converting piece already on the client's blog, and it happened before the piece ranked for its intended keyword. They note 600 sessions is cheap to buy for that company, with click costs typically between $0.30 and $0.75. The mechanism is that the topic, not the channel, sets the conversion rate. If the topic is a pain point their best customers genuinely have, paid traffic to it converts, so you do not have to wait weeks or months for the ranking to arrive before the piece pays back.

> "we typically see click costs of $.30 to $.75"

**Evidence:** New client, four months in: one mid-funnel pain-point piece produced eight conversions from 600 paid Facebook sessions, matching the client's best existing post, before ranking for its keyword; click costs $0.30 to $0.75.

**How to do it**

1. Pick a newly published mid-funnel pain-point piece, not a top-of-funnel explainer.
2. Confirm the pain point came out of customer research, so the topic itself filters for buyers.
3. Set up a Facebook traffic campaign targeting the job titles and interests matching your best customers.
4. Tag the ad URLs with UTMs and expect the analytics report to split the page across URLs.
5. Budget for roughly 600 sessions at $0.30 to $0.75 per click, so around $180 to $450.
6. Track conversions on the piece against your blog's baseline conversion rate, not against the ad's cost per click.
7. Compare the paid result to the highest-converting existing post on the blog to decide whether to scale.
8. Keep the piece in the SEO plan; the paid push is a bridge until it ranks, not a replacement.

**Tools:** Facebook Ads, Google Analytics

**Pitfall:** Running this on a top-of-funnel piece wastes the budget. Paid traffic does not fix a topic with no buying intent, and the tell is a normal blog-baseline conversion rate on paid sessions.

**Apply at Pabau:** Pabau can bridge the ranking wait on new pain-point articles for aesthetic practices with a small paid social push. Test it on one newly published article aimed at a practice-owner pain point before committing budget across the blog.

**Apply anywhere:** Bridge the ranking wait on a new pain-point article with paid social. Budget roughly 600 clicks at typical B2B rates, UTM-tag the ads, and judge the piece by its conversion rate against your blog baseline rather than waiting months for organic traffic.

### 6. Buy Facebook clicks to three new articles a month and cull by conversion  `140.4`
*core · concrete actions · source 140*

Lewis paired every publish with paid distribution rather than waiting for rankings. She built the Facebook audience directly from the kickoff research, targeting by the job titles and interests that came out of the customer research questions, then tested which of those audiences produced engagement and, more importantly, conversions. Her cadence was fixed: three new articles get ads each month, and at the end of the month each article is either kept on the budget or dropped for a new one based on whether it converted. Click costs came in as low as $0.70. The reason she gives for distributing is not traffic. Paid clicks tell you which pieces convert months before organic rankings would, so you learn which topics to double down on early. She wound the ads down once organic traffic to the same articles started rising.

> "Every month, I would run ads to three new articles"

**Evidence:** ADA Compliance Pros saw click costs as low as $0.70, traffic peaking in October from a June start, and organic traffic rising as paid was wound down.

**How to do it**

1. Build the Facebook audience from the kickoff answers, targeting the buyer job title and the interests those answers imply.
2. Launch two or three audience variants per article so you are testing audiences, not just creative.
3. Run ads to exactly three newly published articles each month, and keep the budget per article equal.
4. Track conversions per article, not clicks, using the site's actual lead action.
5. At month end, keep ads running on any article that converted and swap the non-converters for three new pieces.
6. Watch cost per click and treat anything near $0.70 in a niche B2B audience as healthy.
7. Taper paid spend on an article once its organic traffic starts climbing.
8. Feed the converting topics back into the next month's keyword list.

**Tools:** Facebook Ads

**Pitfall:** Judging the test on engagement or pageviews instead of conversions picks the entertaining article over the commercial one. Also, paid traffic on a low-volume BOFU piece will never look impressive in a traffic graph, so a stakeholder reading traffic alone will kill a winner.

**Apply at Pabau:** David should run a small Facebook budget to each new Pabau comparison or template page for its first month, targeting practice owner and clinic manager job titles. Demo requests per article decide which topics get more pages, long before rankings settle.

**Apply anywhere:** Put a small paid budget behind three newly published articles each month, targeting the job titles your customer research surfaced. Measure conversions per article rather than clicks, keep the converters on budget and swap the rest, and taper spend once organic traffic to that article starts rising.

### 7. Cut a 134-name expert list down to the 10-15 you personally want to learn from  `162.2`
*core · concrete actions · source 162*

Peralta's first move for the client Codementor.io was to list 134 well-known startups whose founders matched the audience's aspirations, then cut that to 10-15 companies he was genuinely curious about. His stated reason is that the more interested he was in learning about the company, the better the finished article would be. The selection rule is aspiration: the audience wants to learn from a more successful version of themselves, so for seed-stage founders he targeted founders who had passed Series A or grown without venture capital. He then put the shortlist in a plain spreadsheet and started hunting contact details. The cut matters because a shortlist of 10-15 lets you spend real research time per target, which is what the rest of the process depends on.

> "whittled that down to 10-15 companies"

**Evidence:** For Codementor.io, Peralta cut 134 well-known startups to 10-15 companies and landed interviews with 60% of those he contacted.

**How to do it**

1. Write down your audience's three or four sharpest pain points before naming any expert.
2. Define the aspirational profile: the person who has already solved those exact pain points one stage ahead of your reader.
3. Brainstorm a long list, 100 or more names, of companies or people fitting that profile.
4. Cut the list to the 10-15 you personally most want to learn from, using your own curiosity as the filter.
5. Put the shortlist in a spreadsheet with columns for name, company, angle, Twitter, email and outreach stage.
6. Only start hunting contact information once the shortlist is fixed, so research time is not spread across 134 names.

**Tools:** Google Sheets

**Pitfall:** Keeping the full long list and mass-mailing it. You cannot research a unique angle for 134 people, so the pitches go generic and the response rate collapses.

**Apply at Pabau:** For Pabau, build the expert list from aesthetic practice owners one growth stage ahead of the reader (multi-room clinics, multi-site groups), cut it to 10-15, and use your own curiosity about each practice as the tiebreak.

**Apply anywhere:** Build a long list of experts who are one stage ahead of your reader, then cut it to the 10-15 you are personally most curious about, because curiosity is what produces a good interview.

### 8. Decide whether you need a writer or a content strategist before hiring  `164.13`
*core · general insights · source 164*

Grow and Convert say companies constantly advertise for a writer while actually wanting someone to run search engine optimization and data analysis too. They separate the roles cleanly. A content strategist, commonly titled Content Marketing Manager or SEO Manager, owns long-term organic traffic: SEO, keyword research, page rankings and analytics. A writer owns content creation, the actual article writing. Expecting one person to produce your content strategy is unrealistic and most will not do both well. If you do find someone genuinely strong at both, do not expect to pay them a writer's rate. Their harder version of the point is that almost no freelance writer is going to single-handedly open content as a channel for you, so if that is the goal you are building a content operation, not hiring a writer.

> "It's unrealistic to expect your writer to produce your content strategy"

**Evidence:** Grow and Convert list the four strategy duties they see companies wrongly assign to writers, drawn from many client conversations about in-house writers, agencies and freelancers.

**How to do it**

1. Write down what you actually want from the hire: traffic and leads, or drafted articles.
2. If it includes keyword choice, rankings and analytics, advertise a content strategist or SEO manager role, not a writer role.
3. List the four strategy duties explicitly: picking keywords and topics, coordinating expert interviews, final quality and on-page pass, and measuring leads per piece.
4. Decide who owns those four before you brief any writer, whether in-house, agency or you.
5. If you hire one person for both roles, budget well above a writer's per-article rate.
6. Do not judge a content channel's failure on the writer when nobody owned strategy.

**Pitfall:** Hiring a freelance writer to open content as a lead channel. When it fails, the writer takes the blame for the absence of a strategy function nobody staffed.

**Apply at Pabau:** David already owns keyword selection and measurement for Pabau. Any outside hire should therefore be scoped as a writer against a supplied keyword, and briefs should say strategy is not in scope.

**Apply anywhere:** Separate the writer role from the content strategist role before hiring. Someone must own keyword and topic choice, expert interviews, the final quality pass and lead measurement. A freelance writer will not open content as a channel alone.

### 9. Derive your 'factors to consider' from your own product's differentiators  `72.4`
*core · concrete actions · source 72*

Khanal's second intro framework is 'factors to consider', which he says his agency uses a lot on bottom-funnel posts. He is open that he pulls the factors directly from his product's feature set, then frames each as a question the reader should ask of any tool. His three: does it understand the arguments about your product or only imitate tone and style, does it read the SERP or invent arguments from a short keyword, and does the output actually sound like you or take a long time to fix. He anticipates the objection that this is inauthentic because you are setting up questions only you answer well. His counter: those are honestly what you think matters, which is why you built the product that way. If they are not, the problem is your product, not the article.

> "All of these I get from Waves features"

**Evidence:** Khanal built three intro factors directly from Wave Writer's feature set, and found the AI draft independently proposed the same three in the same order.

**How to do it**

1. List your product's three or four genuine differentiators, the ones you built deliberately.
2. Rewrite each as a question a buyer could ask any vendor in the category, not as a feature claim.
3. Cap the list at three so the intro sets up a structure the body can follow.
4. Order the questions so the body sections match them one to one.
5. Leave price out of the list unless being cheapest is your actual value proposition.
6. State that this is your view of what matters, so the framing is declared rather than hidden.
7. Check each question is one you would still ask if you sold nothing, and drop any that fails.

**Pitfall:** Choosing factors you cannot defend outside your own sales pitch. Khanal's test is that a poorly designed product produces factors nobody would accept, and no framing fixes that.

**Apply at Pabau:** For Pabau comparison pages, build the evaluation criteria from what Pabau actually does differently, for example that every subscription includes every feature, and phrase each as a question a clinic owner should ask any vendor.

**Apply anywhere:** Build your comparison page's evaluation criteria from your product's real differentiators, phrased as questions any buyer could ask any vendor in the category.

### 10. Diagnose which of four content problems you are hiring to solve  `165.14`
*core · best practices · source 165*

Hyam frames the hiring mistake as a diagnosis error. Companies hire a writer because it solves the immediate problem, which is that they need to start publishing. That view treats content marketing as writing. He lists the four bigger problems instead: knowing who you are writing for, which is user research; knowing what to write that will resonate, which is content strategy; figuring out how to drive traffic to those articles, which is content promotion; and turning that traffic into customers, which is conversion strategy. He calls writing the least challenging of the set. The practical use is as a pre-hire checklist. Naming which of the four you are actually short on decides whether you need a writer, a strategist, a promoter or a conversion person, and stops the default reflex of hiring whoever can produce words.

> "Getting content written is only one of the challenges"

**Evidence:** Hyam calls hiring a writer to run content marketing the number one mistake, drawn from running content operations at three companies and an agency.

**How to do it**

1. Write the four problems down: user research, content strategy, content promotion, conversion strategy.
2. Mark honestly which ones your team already does well and with whose name against them.
3. Audit last quarter's output as evidence: all introductory guides means the strategy function is missing.
4. Check whether any post had a written distribution plan; if not, promotion is the gap.
5. Check whether any post is attributed to a lead; if not, conversion is the gap.
6. Hire against the marked gap and write the job description around it, rather than posting a generic content role.
7. If writing is genuinely the only gap, hire freelance writers instead of a manager, and keep the four functions where they are.

**Pitfall:** Hiring against the symptom, an empty publishing calendar, rather than the cause. You get output and no strategy, and the blog stalls once the obvious topics run out.

**Apply at Pabau:** Before adding Pabau content headcount, David should mark which of the four functions pabau.com is actually short on. Given the blog already publishes, the likely gaps are promotion and conversion rather than production.

**Apply anywhere:** Name the four content problems — user research, strategy, promotion and conversion — and mark which you are short on before hiring. Audit last quarter's output for evidence, then write the job description around the real gap.

### 11. Do a four-part SERP analysis before you outline anything  `96.3`
*core · concrete actions · source 96*

Grow and Convert call SERP analysis the single most essential step in SEO content creation, and they specify four passes. First, review the titles, page types and sources of the page-one results: list posts, how-to articles, guides, landing pages, and whether the competitors are direct rivals, news sites or adjacent products. Second, read or scan each result and log the topics that recur, especially those in subheadings, because recurring topics are what your piece likely needs to rank. Third, note what each page does well and badly, which tells you what to copy and where you can beat them. Fourth, write a one-line summary of the searcher's actual intent. They note what ranks tells you what Google already thinks is best, so the safe move is to use one of those content types, though it is not a hard rule.

> "the #1 most essential step to SEO content creation"

**Evidence:** The article's TapClicks case: this analysis produced a piece that sits at position 2 for 'paid search dashboard'.

**How to do it**

1. Open page one for the target keyword and record every result's title, page type and domain type.
2. Classify the mix: how many list posts, how-to posts, guides, product or landing pages.
3. Open each result and list its subheadings; tally topics that appear across three or more results.
4. Write a strengths and weaknesses line for each result, naming what is thin or missing.
5. Summarize the searcher's intent in one or two sentences before outlining.
6. Pick your post type from the dominant ranking type unless you can argue a better fit.
7. Carry the recurring-topic tally straight into the outline as required sections.

**Pitfall:** Reading only the titles. Grow and Convert say titles alone reveal intent, but the recurring subtopics that decide ranking only surface when you open the pages and read the subheadings.

**Apply at Pabau:** Add a mandatory SERP-analysis artifact to Pabau's brief template with these four sections filled in, so the writer inherits the recurring-topic list rather than guessing at coverage.

**Apply anywhere:** Before outlining, audit page one four ways: page types and sources, recurring subheadings, per-page strengths and weaknesses, and a written intent summary.

### 12. Feed GSC data to an AI agent, never auto-publish  `08.11`
*core · ai workflows · source 08*

To refresh an existing page, the workflow is to export its Search Console query data (queries, impressions, clicks, position), pull its current live code/URL, and feed all three into an AI agent (Manus, or equivalently Claude/Codex) to regenerate the page around the keywords that already carry meaningful impressions. The critical governance rule is that the agent is never trusted to apply changes directly — it's required to output an explicit list of every change it's about to make, page by page, which is then manually reviewed before anything goes live. The stated reason is that unsupervised AI edits reliably introduce errors: over-stuffing or under-using keywords, or silently dropping content elements that were supposed to stay.

> "I don't trust AI to make changes on its own"

**How to do it**

1. Export the target page's Google Search Console query data (queries, impressions, clicks, position) for a recent date range.
2. Pull the page's current live content/code (e.g., the WordPress source) and its URL.
3. Feed the GSC data, current page code, and URL together into an AI agent (Manus, Claude, or Codex).
4. Set your own threshold for which queries are worth targeting in the rewrite (e.g., keywords with meaningful impressions ranking close to page one) rather than accepting the agent's own judgment of significance.
5. Instruct the agent to output a full list of every change it intends to make before editing anything live.
6. Manually review that change list, specifically checking for keyword over-insertion, keyword under-insertion, or dropped content elements.
7. Only after manual approval, have the agent apply the approved changes to produce the updated page.
8. Process pages individually rather than as one bulk batch, so each page gets its own reviewed change list rather than an undifferentiated mass pass.

**Tools:** Manus, Codex, Google Search Console, WordPress

**Pitfall:** Letting an AI agent apply on-page changes directly without a review step — unsupervised, it 'normally messes up if you don't pay attention, puts in way too many or too few keywords, or ignores some elements you want in there.'

### 13. Feed it what already ranks, because that's Google's own signal  `63.3`
*core · best practices · source 63*

The reasoning he repeats in every version of this workflow, stated most cleanly here: what is currently ranking is Google signalling 'this is what we think a good search result looks like' for that query, so those pages are the correct constraint set for the writing. He is upfront that this baseline output is 'pretty good' and will rank, and then names the upgrade explicitly: have an AI interview you for about 30 minutes so you have a transcript carrying your perspective, opinions and point of view on the topic, and incorporate that alongside the scraped source material plus a style guide. Writing from all three is what he says produces an unbelievable piece rather than a merely rankable one. He also confronts the objection directly - that this is AI slop - and calls it a skill issue: you get bad output because you aren't providing guardrails for what good content looks like.

> "Google is basically signaling"

**How to do it**

1. Scrape the full text of every page ranking on page one for the target keyword.
2. Have an AI interview you (or your subject-matter expert) for about 30 minutes on the topic and transcribe it.
3. Assemble your style guide as a third input.
4. Instruct the model to write from all three: the ranking pages for coverage, the transcript for point of view, the style guide for voice.
5. Ask for the outline first, consolidating what all the ranking pages cover, then write section by section.
6. Run a review pass asking what was missed and how it could be improved.
7. Have a human edit before publication.

**Tools:** Claude, Claude Code

**Pitfall:** Writing only from the scraped pages produces a consolidation of what already exists - it will rank, but it contains nothing a competitor can't reproduce. The interview transcript is the part that makes it defensible.

**Apply at Pabau:** For Pabau this is the difference between rankable and worth publishing: the page-one scrape gives coverage, but the recorded interview with someone who has actually run a clinic is what makes the article original.

**Apply anywhere:** This is the difference between rankable and worth publishing: the page-one scrape gives coverage, but a recorded interview with someone who has actually done the thing is what makes the article original.

### 14. Feed two style exemplars and topic sources rather than trusting a project  `71.10`
*core · ai workflows · source 71*

Before generating the draft, Devesh selected specific past articles for the tool to imitate and separate topic-specific sources to draw substance from. He picked two style exemplars, a blog outline generator post and an SEO content writer post, then added a set of topic-relevant pieces whose full text gets fed into the generation. His reasoning is a direct criticism of the alternative. With a Claude project you are relying on Claude to go look at the stuff in your project, and it is not going to every time. Explicitly attaching the sources per draft forces the material in from scratch on every run. He also notes the payoff: because he had already written these value propositions in earlier posts, the draft made arguments he recognized as his own, including one he had forgotten writing.

> "relying on Claude to go"

**Evidence:** Devesh attached two style exemplars plus several topic-specific articles per draft, and the output reproduced value propositions from his earlier posts, one of which he had forgotten writing.

**How to do it**

1. Pick two published articles whose structure and voice you want the draft to imitate, and attach their full text.
2. Separately pick the articles that carry the substance for this topic, such as prior posts stating the value propositions you want reused.
3. Attach those source articles in full to the generation run rather than storing them once in a project or custom GPT.
4. Re-attach the sources on every new draft, on the assumption the model will not reliably retrieve from persistent storage.
5. Watch the output for arguments lifted from your own earlier posts, and treat their presence as the check that retrieval worked.
6. If the draft reads generically and cites none of your prior arguments, the sources did not make it in and you should regenerate.

**Tools:** Wave Writer, Claude

**Pitfall:** Storing your style guide and source corpus once inside a Claude project or custom GPT feels tidier but the model does not read them reliably on every run. The symptom is a draft that could have been written for any company.

**Apply at Pabau:** Pabau's article generator should attach the specific prior articles that carry the relevant Pabau arguments to each generation run, not rely on the guides being in context, and the check is whether the draft reuses a Pabau argument we have published before.

**Apply anywhere:** Attach the style exemplars and source articles in full to every generation run instead of trusting a saved project to be read. If the draft reuses none of your prior arguments, the sources never reached the model.

### 15. Filter 80 percent of writer applicants on four portfolio questions  `167.2`
*core · concrete actions · source 167*

Grow and Convert say the portfolio stage is where the vast majority, maybe 80 percent, of applicants are removed. The point they stress is that the criteria have to match the content you actually publish, not general writing quality. Because they write bottom-of-funnel product content targeting terms like best accounting software or Google Analytics alternatives, they screen for the ability to contrast value propositions and communicate differentiators between products clearly and persuasively. They do not require a sample that matches exactly what they would publish, because most writers do not have one. They look instead for four signals in whatever the applicant has written: have they covered advanced complex topics, can they sell a product or feature well, do they use filler and fluff, and do they open pieces with needless quotes and stats.

> "Do they start pieces with needless quotes and stats?"

**Evidence:** Grow and Convert report roughly 80 percent of applicants are removed at the portfolio stage.

**How to do it**

1. Write down the type of content you actually publish before reading a single portfolio, for example bottom-of-funnel product comparisons.
2. Convert that into four or five yes or no screening questions rather than a vague quality judgement.
3. Ask whether the writer has handled advanced, complex subject matter, not just readable general topics.
4. Ask whether they can sell a product or feature, since that is a copywriting skill separate from content writing.
5. Mark down filler sentences, padding and throat-clearing openings.
6. Mark down pieces that open with a borrowed stat or quotation instead of the argument.
7. Accept near-misses: look for signs the writer could produce your format, not a sample that already is your format.
8. Note the promising applicants and pass only those to the writing-sample stage.

**Pitfall:** Screening on prose quality alone. A clean writer with no product-copywriting instinct passes the portfolio filter and then fails the test project, which is exactly the pattern that pushed Grow and Convert to add a second application-stage filter.

**Apply at Pabau:** For Pabau, the portfolio screen should ask whether the writer has ever compared two software products on features and pricing, since that is what pabau.com blog and comparison pages need most.

**Apply anywhere:** Turn your portfolio screen into four explicit questions tied to the content you publish, and expect to reject about 80 percent of applicants on that stage alone.

### 16. Fix existing cannibalization before publishing more content  `49.5`
*core · best practices · source 49*

Three recurring mistakes worsen cannibalization instead of fixing it: publishing new content on a topic before resolving existing cannibalization there, which just adds a third competitor rather than solving the problem; creating year-specific URLs (e.g., "best tools 2024," "best tools 2025") that end up competing with each other and with an evergreen version, instead of maintaining one URL updated annually; and treating canonical tags as a genuine fix — canonical tags are better than nothing but don't carry the same authority-consolidating effect as an actual 301 redirect.

> "adding more content just adds more competition"

**How to do it**

1. Before publishing any new article on a topic, check whether existing pages already target that same keyword or topic and are cannibalizing each other.
2. If existing cannibalization is found, resolve it via the consolidation process before adding new content to that topic area.
3. For recurring "best X [year]" style content, maintain a single evergreen URL updated each year rather than publishing a new dated URL annually.
4. Where a canonical tag has been used as the fix for two competing pages, treat it as only a partial or interim measure, and replace it with an actual 301 redirect and content consolidation as the real fix.

**Pitfall:** Adding canonical tags and calling cannibalization "fixed" is a false sense of security — canonical tags are better than nothing but don't consolidate ranking authority the way a real 301 redirect does.

### 17. Fix the broken process before speeding it up with AI  `174.7`
*core · best practices · source 174*

Khanal's sharpest point about adoption is that AI does not change the content process, it accelerates whatever process you already have. Many companies and agencies are taking the same flawed approach they used before and are now doing it faster with technology. The old version was hiring a freelancer to Google a topic for an hour and regurgitate what the top five results say. The new version is asking a model to do exactly that, faster. So the honest first question is not which tool to buy but whether your current process would produce something original if you removed the time pressure. If it would not, adding AI multiplies the wrong output. He also warns against the framing that dominates the debate: people focus on the speed of work instead of the quality of work, which he calls a dangerous game if you want results from your content investment.

> "produce content and are now doing it faster with technology"

**Evidence:** Khanal argues AI simply makes it easier to produce mirage content at scale, replacing an hour of freelancer Googling with the same operation done faster, and warns that focusing on speed over quality is dangerous for content investment.

**How to do it**

1. Write down your current process for one article, step by step, from topic to publish.
2. Mark each step by its input source: the SERP, an internal expert, first-party data, or a customer conversation.
3. If every input is the SERP, stop and fix the sourcing before introducing any AI tool.
4. Add at least one non-SERP input as a required step, such as a 30-minute interview with someone who does the job.
5. Only then insert AI, and only at steps where the input is already original.
6. Measure the change by originality of claims per article, not by articles published per month.

**Pitfall:** Buying an AI writing tool to fix an output problem that is really a sourcing problem. The tell is that output volume rises while the pages still say what the top five results said.

**Apply at Pabau:** Before David expands AI assistance across pabau.com's production, he should map where each article's facts come from. If a piece is sourced only from ranking competitors, add a required input from Pabau's support or onboarding team, who see how clinics actually work, then apply AI to the drafting.

**Apply anywhere:** Map your current article process and mark where each input comes from. If every input is the pages already ranking, adding AI just produces the same derivative work faster. Add a required non-SERP input first, such as an interview with someone who does the job. Judge the change by original claims per article, not articles per month.

### 18. Fix the three writing failures that make SEO content generic  `115.8`
*core · best practices · source 115*

Grow and Convert name three specific things companies get wrong in the writing itself, and say all three lead to the same result: generic, low-quality content that will not rank. First, they work with freelance writers or agencies that have no process for gaining and expressing subject-matter expertise, so the writer never acquires anything the reader could not find elsewhere. Second, they believe it is not acceptable to sell or talk about the product inside the content, so the article never demonstrates the thing the buyer came to evaluate. Third, they sprinkle keywords into the page and assume that is enough to rank. The three are connected: without an expertise process there is nothing to say, without permission to sell there is no reason for the page to exist commercially, and keyword sprinkling is what fills the gap.

> "lack processes for gaining and expressing subject-matter expertise"

**Evidence:** Grow and Convert list the three failures as the cause of generic low-quality content across the companies they audit: no expertise process, unwillingness to discuss the product, and keyword sprinkling.

**How to do it**

1. Require every writer to have a named expertise source per article: a recorded interview, a customer call, or hands-on product use.
2. Reject drafts where no sentence could only have been written by someone with that access.
3. Write into the brief that the product should be discussed by name where it genuinely answers the query.
4. Give writers the specific product capability the article should demonstrate, not just a keyword.
5. Ban keyword-density targets from briefs and replace them with the required subtopic list from the SERP.
6. Add an editorial check that the article's structure came from a SERP analysis rather than a template.
7. When auditing an agency, ask what their process is for acquiring expertise before asking about volume or price.
8. Kill any article that passes the keyword check but fails the expertise and product checks.

**Pitfall:** Treating the fear of selling as a quality decision. The article reads as neutral and helpful, ranks nowhere near the top because it says nothing specific, and produces no leads even when it does rank.

**Apply at Pabau:** Pabau briefs should name the specific feature the article must demonstrate and the clinic-side source the writer will interview. An article about patient recall that never shows how Pabau handles recall fails both of the first two tests.

**Apply anywhere:** Three writing failures produce generic content: writers with no process for acquiring subject-matter expertise, a belief that mentioning your own product is inappropriate, and sprinkling keywords in place of structure. Require a named expertise source per article, brief the specific capability to demonstrate, and replace density targets with a SERP-derived subtopic list.

### 19. Follow the four-step intro formula: persona, channel, originality, angles  `127.6`
*core · concrete actions · source 127*

Grow and Convert close the piece with an explicit formula they say produces a good introduction basically every time. Step 1 is to describe to yourself who the reader is, as a simple persona, like the sales veteran scene at the top of the article. Step 2 is to work out how they are encountering the post, via search engine or social media, because that changes what they already know and how much patience they have. Step 3, which they call the hard part, is to work out what makes your post specific or original, and they warn it forces a tough question: is there anything specific and original here, or is this the same old content everyone else writes. Step 4 is to pick a few angles of specificity or originality and try them out, writing the most direct statements about why the post is good, with no questions and no background filler.

> "Describe to yourself who the reader is"

**Evidence:** Grow and Convert present the four steps as a formula that works 'basically every time' and reference their own sales-veteran persona exercise as the Step 1 model.

**How to do it**

1. Write the reader persona as a short scene, not a demographic list, and include their experience level in the topic.
2. Write down the channel they arrive from, search or social, and what that implies about their intent and patience.
3. Write one sentence naming what is specific or original in this post; if you cannot, stop and fix the post, not the intro.
4. Draft three or four candidate opening lines, each taking a different angle of specificity or originality.
5. Ban questions and background context from every candidate; write direct statements only.
6. Read each candidate as the persona and pick the one that best signals 'they get me'.
7. For your own blog, test a personal-story opener as one of the candidates.
8. For a guest post on another site, state the exact specific angle the post is taking instead of telling a story.
9. Check the winning line is delivered in the body before publishing.

**Pitfall:** Step 3 is where the formula usually breaks: writers skip it because the honest answer is that the post has no original angle, then produce a generic intro anyway. A hard intro is a signal to kill or rework the piece.

**Apply at Pabau:** David should encode these four steps as an intro sub-brief in the Pabau content process, run before drafting. The Step 3 answer for each article becomes the originality nugget the house rules already require.

**Apply anywhere:** Before writing an intro, run four steps: sketch the reader as a scene, note the channel they arrive from, state in one sentence what is original about the post, then draft three or four direct opening lines from different angles of that originality and pick the one your reader would recognize.

### 20. Follow the three-step start-small routine for adding originality  `100.11`
*core · concrete actions · source 100*

Grow and Convert close with an explicit step-by-step for integrating the framework, and it starts by deliberately avoiding heavy pieces. Use Pain Point SEO and their content ideation guide to find topics that are likely high converting but not particularly competitive from an SEO standpoint. Then think of a piece you can produce in days or weeks, not months. Then think of how to add originality nuggets, and specifically do not think of one thing: think of multiple angles and use one or more. Their reasoning is that the heavy examples they showed are hard to produce, and the point of the framework is versatility, producing good content without always resorting to a massive six-month project. The multiple-angles instruction matters because a single nugget can turn out to be weaker than it looked once you check the SERP.

> "think of a piece you can produce in days or weeks, not months"

**Evidence:** Grow and Convert's own recommendation after showing heavy examples they describe as hard to produce and reproduce.

**How to do it**

1. Generate topics from customer pain points and buying-intent modifiers, not from volume rankings.
2. Filter to keywords that are high converting but low competition, so a modest piece can rank.
3. Set a production budget in days or weeks and reject any topic that needs months at this stage.
4. Brainstorm at least three possible nuggets per topic: arrangement, viewpoint, first-person account, original data, interview, tool.
5. Check each nugget against the current top 10 and drop any that a competitor already has.
6. Use more than one surviving nugget in the piece.
7. Ship, measure leads, and only then decide whether the topic deserves a heavy follow-up.

**Pitfall:** Starting with a heavy piece burns months before you know whether the topic converts. The signal is a six-month project on a keyword you have never tested with a smaller article.

**Apply at Pabau:** Pabau should test new topic areas with fast, lightly original articles before committing to a study or an interactive tool. David can hold the heavy budget for topics that already show qualified traffic and demo requests.

**Apply anywhere:** Pick high-converting, low-competition topics, cap the first piece at days or weeks of work, and brainstorm at least three possible nuggets before choosing which to use.

### 21. Front-load the keyword, then answer it immediately (top-funnel)  `44.3`
*core · concrete actions · source 44*

For a top-of-funnel keyword (the worked example: "Why is my sink draining slowly?"), the formula is to open the first sentence with the keyword or a close, natural variation of it, then answer it in the same breath. If the keyword is long-tail, awkward to quote verbatim, or a plain sentence fragment, and it isn't a competitive term other sites are targeting exactly, the source says to paraphrase closely rather than force an exact match — e.g. writing "if you're wondering why your sink is draining slowly, it's probably because of a build-up somewhere in the pipe" instead of quoting the literal question, since this stays "close enough to the original keyword that there will still be a lot of relevance." The full worked answer then names common causes (hair, grease, soap scum, food particles, mineral deposits) and the easiest fixes (flushing with hot water, a plunger, or a drain snake) within the first couple of sentences, after which the source says trust is established and the page can go deeper into each cause before moving the reader toward a lead magnet, newsletter, or offer.

> "the keyword at the beginning of your first sentence"

**How to do it**

1. For a top-of-funnel/informational keyword, open the first sentence with the keyword itself or a close, natural variation of it.
2. If the keyword is long-tail, awkward to embed verbatim, or a fragment, and it isn't a competitive exact-match term, paraphrase it closely rather than forcing the literal phrase in as a quoted question.
3. Immediately state the direct answer in that same sentence or the next one.
4. Follow the immediate answer with a short elaboration naming the common causes or contributing factors, to demonstrate depth.
5. Add the easiest fix or solution right after, so the reader has both the "why" and the "what to do" within the first couple of sentences.
6. After delivering the immediate answer and solution, use the rest of the page to go deeper into each cause/detail, since the source says trust is now established and readers will follow further.
7. Use that established trust to move the reader toward a lead magnet, newsletter signup, or product/service offer further down the page.

**Pitfall:** Forcing an awkward exact-match keyword phrase into the sentence (e.g. quoting a long-tail question verbatim) when a natural close paraphrase would read better and still carry enough relevance, especially for non-competitive long-tail keywords.

### 22. Get narrative, title and intro right before writing any body copy  `91.2`
*core · best practices · source 91*

Grow and Convert say a disruption story succeeds or fails on three elements, and they list them in priority order. First the overarching narrative: a two to three sentence pitch for why the business exists, the pain it was designed to solve and how you solve it. Getting this right, and making it a problem the audience genuinely cares about, is the single most important factor. Second the title, which matters more here than on an SEO post because the reader arrives from social with no query to satisfy, so the title has to earn the click on its own. Third the introduction. They point out that on a typical 'Top 10 Time Management Tools' post many readers skim the intro and jump to the list, but on a disruption story the reader does not know what is coming, so the intro is read in full and decides whether they continue. Once those three are set, they say the rest of the post is straightforward.

> "three things that you need to get right in order to have a successful disruption story"

**Evidence:** Grow and Convert's stated process across dozens of client disruption stories.

**How to do it**

1. Write the two to three sentence narrative first and stop until it names one primary pain, not a feature list.
2. Pressure-test that the pain is something the target audience actively complains about, not something you find interesting.
3. Only then write the title, aiming for provocative but literal, so a stranger scrolling social understands the problem you solve.
4. Write the intro next, opening on the specific pain in the reader's own terms.
5. Do not begin the body until narrative, title and intro are all signed off.
6. Write the body as the continuation of that narrative, tying every feature back to the pain you named.
7. Re-read the finished piece and cut anything that does not either prove you have lived the pain or show how you fix it.

**Pitfall:** Writers start with the body because it is the easiest part, then bolt on a title at the end. The tell is a title that describes the article ('Our approach to QA') rather than the disruption, and a piece that reads like a feature tour.

**Apply at Pabau:** Add a three-part gate to Pabau's brief template for any non-keyword article: narrative, title, intro approved before drafting. For disruption-style pieces the narrative should be signed off by the founders, not the content team.

**Apply anywhere:** For any article that has to earn its own click, lock the two to three sentence narrative, then the title, then the intro, before writing a word of the body. The body is the easy part once those three agree.

### 23. Give AI the scaffolding jobs and keep examples and argument human  `107.9`
*core · best practices · source 107*

Grow and Convert answer the question of how much writing to hand to AI with a specific split rather than a yes or no. They say they have tested this across client work and their own content. AI drafts are useful as structural scaffolding, meaning turning an approved outline into prose. They are not useful for the parts that make a post rank and convert: the specific examples, the customer language, the originality nuggets and the argumentation that comes from subject-matter expertise. Those have to come from a human who did the interview work. The tasks they name as genuinely worth handing over are drafting meta descriptions, summarizing long sections, generating multiple headline options and structuring outlines. This is a narrower allocation than most teams use, and it puts the interview material, not the model, at the center of the draft.

> "useful for structural scaffolding"

**Evidence:** Grow and Convert say they tested this extensively across client work and their own content.

**How to do it**

1. Write the approved outline yourself from the SERP research and interview notes.
2. Use AI to generate several headline options and a meta description, then pick and edit.
3. Use AI to summarize long source documents or transcripts into usable notes.
4. Draft the connective prose from the outline with AI if it saves time, then rewrite every claim-bearing paragraph.
5. Insert the specific examples, customer quotes and originality nugget by hand from the interview transcripts.
6. Read the finished piece for any argument that could have been written without your company's expertise, and replace it.

**Tools:** ChatGPT, Claude, Gemini

**Pitfall:** Shipping the AI draft with light editing keeps the structure and loses exactly the parts that differentiate. The signal is a post that covers everything the top ten cover and gives a reader no reason to prefer it.

**Apply at Pabau:** Pabau's writing process already requires a human pass. The useful addition here is naming which tasks AI may own outright, meta descriptions, headline options, section summaries and outline structuring, so effort concentrates on examples and practice-specific detail.

**Apply anywhere:** Restrict AI to headline options, meta descriptions, section summaries and outline structuring. Write the examples, customer language and argumentation yourself, because those are what make a post rank and convert.

### 24. Give one round of detailed feedback and grade the revision  `167.7`
*core · concrete actions · source 167*

Grow and Convert treat the response to feedback as a separate signal from the first draft. After the test project they provide one round of revisions, delivered as comments or a recorded video, with detailed explanations of what they are looking for. They do this even when the first attempt is poor, because some applicants respond really well to feedback and come back with a solid revised version. Responding well to feedback is one of the characteristics they are explicitly hiring for. This connects to the fifth mistake they name in the article: many of their writers report that before joining, clients gave them a draft response of thanks or I do not like it and nothing more. Their conclusion is that a writer who never sees your editing process cannot improve, so the feedback round is both a test and the beginning of training.

> "We provide one round of revisions via comments or a recorded video"

**Evidence:** Grow and Convert give one revision round on every test project, including poor attempts, and say some applicants recover into a solid revision.

**How to do it**

1. Budget one revision round into every test project rather than making a pass or fail call on the first draft.
2. Deliver feedback as inline comments or a recorded screen video, not as a one-line verdict.
3. Explain what you are looking for and why, not only what is wrong.
4. Give the feedback even when the draft is weak, because the revision is the data you actually want.
5. Grade the revision on whether the writer applied the principle or only patched the specific sentences you flagged.
6. Record whether they argued, ignored or absorbed the feedback, and weight that alongside writing quality.
7. Carry the same feedback habit into live work: share your edits with the writer instead of silently fixing drafts.
8. Track deadline adherence during this round as a second hiring signal.

**Tools:** Loom, Google Docs

**Pitfall:** Silently editing a writer's draft and saying thanks. Grow and Convert say many writers arrive having never received real feedback, so quality never improves and you keep paying an editor to rewrite the same mistakes.

**Apply at Pabau:** For Pabau, every fact-check and editorial pass on an outsourced article should be sent back to the writer as comments, so the same corrections are not repeated in the next commission.

**Apply anywhere:** Give one detailed round of feedback on every test project and judge the revision. A writer who absorbs feedback is worth more than one whose first draft was slightly cleaner.

### 25. Give one round of feedback in the test and judge the revision  `164.6`
*core · concrete actions · source 164*

Grow and Convert build a feedback round into the paid test project rather than scoring the first draft alone. They provide one round of revisions through comments or a recorded video, giving detailed explanations of what they are looking for, and they do this even when the applicant's first attempt is poor. Their reason is that some writers respond really well to feedback and come back with a solid revised version, and coachability is a key characteristic they are hiring for. This links to their view that writers who match your voice from day one are extremely rare, so what you are actually screening for is the slope, not the starting point. The four traits they say predict a long-term fit are responding well to feedback, making sensible revisions, writing across multiple brands or topics, and hitting deadlines.

> "we see how they respond to feedback"

**Evidence:** Grow and Convert give one round of revisions via comments or a recorded video on every test project, including poor attempts.

**How to do it**

1. Score the applicant's first test submission but do not decide on it.
2. Record a short video or leave inline comments explaining specifically what you wanted and why.
3. Send the feedback even to applicants whose first attempt was poor, so you see the slope.
4. Set a revision deadline and treat missing it as a fail on its own.
5. Score the revision on whether the changes were sensible, not merely compliant.
6. Note whether the writer applied the principle beyond the exact lines you flagged.
7. Rate each finalist on the four traits: feedback response, sensible revisions, range across topics, and deadlines.

**Pitfall:** Cutting a weak first draft without sending feedback. Grow and Convert say some of the poor first attempts produce solid revisions, and those coachable writers are the ones who last.

**Apply at Pabau:** David should send one recorded-video feedback round on every Pabau writer test, covering the same points the factcheck-flow guides enforce, and hire on the revision rather than the draft.

**Apply anywhere:** Give every test-project applicant one detailed round of feedback, by comment or recorded video, and judge the revision. Coachability predicts long-term fit better than the quality of a first draft.
