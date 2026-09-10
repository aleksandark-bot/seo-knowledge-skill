# Technical SEO — core (part 2 of 2)

17 insights from the SEO knowledge base (both editions), core-first. Prefer `scripts/kb.py`; this file exists for deliberate whole-theme reads only.

### 1. Move a blog off a subdomain onto a subfolder to consolidate link equity  `108.10`
*core · concrete actions · source 108*

Grow and Convert call subdomain blogs one of the most common technical mistakes they see at SaaS companies. Search engines treat blog.yourcompany.com as a separate website, so authority built by blog content does not fully transfer to the main domain and vice versa. On a subfolder at yourcompany.com/blog, every backlink a post earns strengthens the whole domain, including the homepage and product pages. On a subdomain that equity is siloed. They report seeing companies make significant ranking improvements simply by migrating the blog from subdomain to subfolder, with the caveat that the migration itself has to be handled carefully with proper redirects or existing rankings are lost. Note this sits against source 74, which advises dropping the subdomain question from the SEO plan entirely as a non-issue. Grow and Convert treat it as a live and worthwhile migration.

> "search engines treat subdomains as separate websites"

**Evidence:** Grow and Convert report significant ranking improvements at companies that migrated a blog from subdomain to subfolder.

**How to do it**

1. Check whether your blog resolves at blog.domain.com or domain.com/blog.
2. If it is on a subdomain, export the full URL list and current rankings before touching anything.
3. Pull each post's referring domains so the equity at stake is quantified.
4. Map every old subdomain URL to its new subfolder URL one to one, with no chains.
5. Set up a Search Console property for both the subdomain and the root domain before the move.
6. Deploy server-side 301s from every subdomain URL to its subfolder equivalent.
7. Update internal links, the XML sitemap and canonical tags to the new paths on the same day.
8. Keep the subdomain redirects live indefinitely rather than retiring them after a quarter.
9. Monitor rankings weekly for eight weeks and compare against the pre-migration baseline.

**Tools:** Google Search Console, Ahrefs, Screaming Frog

**Pitfall:** Running the move without a complete one-to-one redirect map. Grow and Convert warn the migration itself is where existing rankings get lost, which turns an upside into a setback.

**Apply at Pabau:** Pabau's blog is already on pabau.com/blog, so this is a check rather than a project. Confirm no help centre, careers or resource section sits on a separate subdomain and quietly collects links that never reach pabau.com.

**Apply anywhere:** Host the blog on a subfolder, not a subdomain, so backlinks strengthen the whole domain. If you migrate, build a complete one-to-one 301 map first, because the migration is where rankings are usually lost.

### 2. Move the blog to a subfolder and expect rankings in one month, traffic in three  `133.2`
*core · concrete actions · source 133*

Circuit moved their blog off a subdomain and back onto a subfolder of the main domain on June 14, 2020. Grow and Convert publish the lag. Average tracked position bottomed at worse than 50 at the end of May. Rankings started climbing immediately after the move and became visible in July and August. The organic traffic jump landed in September, and trial signups rose in September too, about three months after the move. Their conclusion is that Google has always said subdomains do not matter, but they have now seen this same large improvement on multiple clients, including Leadfeeder. The useful part for planning is the timeline: one month to see rankings move, three months to see traffic and conversions move. That is what you tell a client or a CEO before the move, so the flat month after it does not get read as failure.

> "The blog was moved to a"

**Evidence:** Circuit: blog moved to a subfolder June 14 2020; average tracked position was worse than 50 at end of May, climbed steadily from July, organic traffic jumped in September, and trial signups rose in the same month. Grow and Convert saw the same effect on Leadfeeder.

**How to do it**

1. Confirm the blog is on blog.example.com rather than example.com/blog before anything else.
2. Pull the average position of your tracked keyword set and record it as the pre-move baseline.
3. Move the blog to a subfolder on the parent domain with server-side 301s from every old subdomain URL to its exact subfolder equivalent.
4. Keep the URL slugs identical so the redirect map is one-to-one with no chains.
5. Add both properties in Search Console and submit the new sitemap the day of the move.
6. Tell stakeholders up front to expect roughly one month before rankings move and three before traffic does.
7. Watch average tracked position weekly as the leading indicator, not sessions.
8. Report conversions alongside traffic, since on Circuit both moved together in the third month.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Judging the move on sessions in the first four weeks. Circuit's traffic did not visibly jump until September for a June 14 move, so an early read looks like the migration did nothing and invites a rollback.

**Apply at Pabau:** Pabau's blog already sits on pabau.com/blog, so the action is defensive: never let a redesign or platform migration push the blog, templates or code-reference sections onto a subdomain, and check any newly acquired or localized property for the same pattern before content spend starts.

**Apply anywhere:** If your blog is on a subdomain, move it to a subfolder on the parent domain with one-to-one server-side 301s. Brief stakeholders that rankings take about a month to respond and traffic about three, and track average position rather than sessions as the early signal.

### 3. Never change the URL of a money page, even for a cosmetic fix  `67.3`
*core · concrete actions · source 67*

Dirk's most costly personal mistake was cosmetic. A brand's homepage URL used an underscore while the rest of the site structure used hyphens, so the team standardized it and redirected brand_name.com to brand-name.com. The redirect was implemented properly, the content was identical and the backlinks were unchanged. The new URL indexed quickly, but traffic dropped immediately and never came back. Reverting the change did not restore it either, so they left it on the intended URL. His read is that the extra hop in the funnel cost something the like-for-like content and links did not replace. His resulting rule is absolute: when anyone asks whether they can change the URL of a money page, the answer is no. This is a sharper position than the base's general finding that server-side 301s do not lose PageRank.

> "Can we redirect the URL of a money page?"

**Evidence:** Dirk's own case: underscore-to-hyphen URL standardization on a main brand page, correct 301, identical content and backlinks, immediate and permanent traffic loss.

**How to do it**

1. Treat the URL of any page that earns revenue as frozen, regardless of how untidy it looks next to the rest of the structure.
2. When a URL convention is inconsistent, apply the new convention only to new pages and leave the earning pages alone.
3. If a change is genuinely forced, do it on a low-traffic page first and measure for a full month before touching anything that converts.
4. Log baseline clicks, impressions and position for the page in Search Console before any change, so you can prove what happened.
5. Implement any unavoidable change as a single server-side 301 with identical content and identical internal links.
6. Do not assume the change is reversible: Dirk reverted his and the traffic still did not return.
7. Watch for the specific failure signature, which is fast reindexation of the new URL alongside an immediate traffic fall.

**Tools:** Google Search Console

**Pitfall:** Fast indexation of the new URL reads like success and hides the loss. Dirk's page indexed quickly, lost traffic instantly, and did not recover even after the change was reversed.

**Apply at Pabau:** Pabau should not re-slug any article or template page that already earns clicks, even when the slug breaks the current naming convention. Apply new slug conventions only to newly published pages.

**Apply anywhere:** Do not re-slug a page that already earns traffic, even to fix a naming inconsistency. Apply new URL conventions only to pages you have not published yet.

### 4. No-index and confirm removal before 301-ing a changed slug  `45.12`
*core · concrete actions · source 45*

For the common case of changing only a URL slug on an existing page (David's example: 'best fidget spinners 2025' to '...2026') while keeping the content the same, David warns a simple 301 redirect alone is not enough and can leave the new page stuck, because Google may treat the new slug as an exact duplicate of the still-indexed old page and refuse to update. His fix requires a specific sequence: run a live test on the old URL via GSC's URL Inspection tool, no-index the old page, submit a re-indexing request for it, and wait for Google's crawler to actually pull the no-index signal and drop the old URL from the index (a roughly 24-hour window if done correctly) — only then republish the content on the new slug, wait for that new URL to be confirmed indexed, and only then apply the 301 redirect. Skipping the no-index step and relying on the 301 alone, he says, can leave the page stuck as an unrecognized 'duplicate' for five to six weeks instead of resolving in about a day.

> "go through a roughly 24-hour window where you no-index the page"

**How to do it**

1. In Google Search Console, use the URL Inspection tool to run a live test on the existing old-slug page and confirm its current index status.
2. Add a noindex tag to the old-slug page once the live test confirms it is currently indexed.
3. Submit a re-indexing request for the old-slug page via GSC's URL Inspection tool's 'Request Indexing' option.
4. Wait for Google's crawler to process the request and actually drop the old URL from the index (expect roughly 24 hours if the sequence is followed correctly).
5. Confirm via URL Inspection or a site: search that the old-slug URL is no longer indexed before proceeding.
6. Only after the old URL is confirmed dropped, publish the content on the new slug.
7. Submit the new-slug URL for indexing via URL Inspection and wait until GSC confirms it is indexed.
8. Only once the new URL is confirmed indexed, add the 301 redirect from the old slug to the new slug.
9. Do not rely on the 301 alone as the first step — without the no-index step first, a duplicate-detected page can take five to six weeks to resolve instead of about a day.

**Tools:** Google Search Console (URL Inspection tool)

**Pitfall:** Applying the 301 redirect immediately, assuming it will help the new page get indexed by passing authority — David explains that if Google's crawler decides the new page is a duplicate of the still-indexed old page, the 301 will not override that classification, and the page can get stuck for five to six weeks.

### 5. Reclaim DNS entries before decommissioning old cloud infrastructure  `54.3`
*core · concrete actions · source 54*

The client's technical lead explained the actual root cause: their site never used www and all monitoring pointed at non-www, but their www subdomain still had a live DNS entry pointing at an old Azure web app that had helped with redirects. When they decommissioned that old web app, they forgot about the www DNS entry - and as soon as Azure released the app's name and corresponding DNS entry, someone else claimed it and pointed it at their spam/gambling site, silently hijacking the www subdomain with no warnings or flags triggered on the client's side. Fixing the DNS entry itself was easy once found, but DNS propagation plus Google re-crawling and recognizing the fix took real additional time.

> "someone else grabbed it and pointed it at their spam site"

**How to do it**

1. Before decommissioning any old cloud app, subdomain, or piece of infrastructure (e.g., an old Azure/AWS/GCP web app used for redirects), inventory every DNS entry (CNAME, A record, etc.) pointing at it.
2. Explicitly reassign or safely remove each DNS entry pointing at the resource being decommissioned, rather than simply deleting the cloud resource and leaving the DNS record dangling.
3. Pay special attention to subdomains you consider 'unused' (e.g., www, when your canonical site is non-www) - these can still have live DNS pointing at real infrastructure with no content team actively managing them.
4. Understand that cloud providers can release a decommissioned resource's name/identifier for public re-registration, meaning anyone can claim that exact name and inherit your old, still-pointing DNS entry.
5. If you discover this has already happened, fix the DNS entry immediately to point away from the hijacked resource, and budget real time for DNS propagation plus Google re-crawling to confirm the fix.
6. After any infrastructure decommissioning project, run a follow-up check a few weeks later specifically confirming no now-orphaned DNS entries still resolve to anything unexpected. (inferred)
7. Add 'confirm no dangling DNS entries' as a formal checklist item in your infrastructure decommissioning process going forward.

**Tools:** Azure (or equivalent cloud DNS/hosting provider)

**Pitfall:** Decommissioning a cloud web app without also removing or reassigning the DNS entry that points to it leaves a live vulnerability - once the provider releases the app's old name/identifier, anyone else can claim it and inherit your still-active DNS pointer, silently hijacking that subdomain with no warnings triggered on your end.

### 6. Redirect page to page into a niche-matched target, never site to homepage  `67.4`
*core · best practices · source 67*

Dirk still believes in 301s in 2026, but with conditions. He says the 2025 update cleaned up parasite sites and sites running mixed niches, so what survives has a much cleaner portfolio. His conditions for a redirect to still pass value: check the source domain's history first, redirect only into a niche-related site or page, map page to page rather than dumping an entire site onto a homepage, and update canonicals to match. Bulk site-to-homepage redirects are the thing he says kills him every time. He also advises being less aggressive than the industry was, because niche mixing is now what gets caught.

> "You don't just redirect the whole blessed website to a homepage"

**Evidence:** Dirk credits the 2025 update with cleaning out parasite sites and mixed-niche sites, and says surviving sites have visibly cleaner portfolios.

**How to do it**

1. Run the history check on the source domain before planning any redirect, using the ownership and Wayback checks.
2. Confirm the destination site sits in the same niche as the source, not merely an adjacent vertical.
3. Map each source URL to its closest matching destination URL rather than pointing everything at the homepage.
4. Where no close match exists, leave that URL to 404 rather than forcing it to the homepage.
5. Update canonical tags on the destination pages so they agree with the new redirect map.
6. Keep the redirect volume conservative, since Dirk says aggressive mixed-niche redirecting is exactly what the 2025 update cleaned out.
7. Recheck rankings on the destination for two to three months, since a mixed-niche redirect damage shows up at the next core update, not immediately.

**Tools:** Wayback Machine

**Pitfall:** Pointing a whole acquired site at one homepage. Dirk names this as the most common and most damaging version of the tactic, and mixed-niche redirects only surface as a problem at the next core update.

**Apply at Pabau:** When Pabau retires or merges content, map each old URL to its nearest topical equivalent and update canonicals, rather than sweeping retired posts into the blog index or the homepage.

**Apply anywhere:** When you retire or merge content, map each old URL to its nearest topical equivalent and update canonicals. Never sweep a whole retired site or section into the homepage.

### 7. Relevance is measured as distance in vector embedding space  `20.3`
*core · content insights · source 20*

Google represents pages, passages within pages, whole site sections, entire websites, and even individual authors as coordinates ('vector embeddings') in a shared multi-dimensional space, and determines relevance by measuring the geometric distance between a query/prompt's embedding and a content embedding — the closer the two points, the more relevant Google considers the content. This is framed as more foundational to modern ranking/retrieval than the link graph, which the speaker says 'isn't even as important as we've historically believed.' The same embedding-and-distance mechanism builds a network of related-entity understanding independent of explicit links.

> "pages are converted to coordinates in multi-dimensional space"

**Evidence:** 'We know that they have vector embeddings that represent people, websites, entities, and individual pages, and we also know that they roll those up on various levels.'

**Apply at Pabau:** For Pabau, optimizing for topical/semantic proximity to target queries (comprehensive, tightly-topical passages and entity associations) is at least as important as link acquisition — David should think in terms of whether a passage sits close to the target query in meaning, not just keyword-matching or link-counting.

**Apply anywhere:** For your site, optimizing for topical/semantic proximity to target queries (comprehensive, tightly-topical passages and entity associations) is at least as important as link acquisition — you should think in terms of whether a passage sits close to the target query in meaning, not just keyword-matching or link-counting.

### 8. Republish a stuck page under a new URL to re-rank it  `22.1`
*core · concrete actions · source 22*

For a page targeting an easy, low-competition keyword that should be indexed and ranking but isn't (or that ranked briefly then vanished), the fix is to keep publishing related content and building a few topical backlinks over time, then take the original page down and republish essentially the same content under a modified URL (just adding a word or two to the slug), with a 301 redirect from the old URL to the new one. In the source's own case, a page created in March 2023 that never ranked at all was republished this way in March 2025, and it began ranking number one for its target keyword in less than a month, holding that position since.

> "You 301 redirect the old page's URL to the new page's URL"

**How to do it**

1. Identify a page targeting an easy, low-competition keyword (one that doesn't appear in competitors' URL slugs or page titles) that should be indexed/ranking but isn't, or ranked briefly then dropped out.
2. Confirm in Google Search Console that the page is stuck in a non-indexed state (e.g. "Crawled – currently not indexed" or "Discovered – currently not indexed").
3. In the meantime, keep publishing more content on the same topic to build topical relevance and authority for your site around that subject.
4. Build a few backlinks relevant to that topic over time, in parallel with the added content.
5. Once more topical authority has accumulated (this may take months), take down the original page and republish essentially the same content under a modified URL, adding a word or two to the slug while still targeting the same keyword.
6. Set up a 301 redirect from the old URL to the new URL.
7. Leave the content itself unchanged — the only variable being changed is the URL/slug.
8. Monitor Search Console and rank tracking after republishing to confirm indexing and ranking movement.

**Tools:** Google Search Console

**Pitfall:** Assuming a simple recrawl request on the same stuck URL will fix it — Google's tools can confirm a page "can be indexed" on a manual crawl request and still not index it, because the URL itself carries the original, insufficient topical-authority judgment; only a genuinely new URL gets re-evaluated fresh.

### 9. Run site audits as parallel per-source sub-chats, then synthesize  `27.4`
*core · ai workflows · source 27*

One user of the speaker's SEO agent tool reportedly cut a full site audit (roughly 50 pages: all blog content plus the landing page) from about 16 hours down to 8 minutes. The mechanism is architectural rather than one giant context: when the tool is given a job, it spins up separate sub-chats per data source — one pulls backlinks, another a domain overview, another a content audit — hooked into Semrush, Ahrefs, Google Search, and Google Analytics, then synthesizes all of that into one report the human can read quickly. Critically, the report is built to reference the underlying source data again rather than just asserting conclusions, specifically so hallucinations can be caught, and the professional using it still spends about an hour QA-ing both the report and the base data it drew from — the tool compresses retrieval-and-synthesis time, not verification time. The speaker flags this single case as unverified and wants independent replication before treating the 16-hours-to-8-minutes ratio as reliable.

> "it creates a sub-chat and calls the tools, doing backlinks in one"

**How to do it**

1. Connect your audit agent/tool to each relevant data source separately: Semrush, Ahrefs, Google Search Console/Search, and Google Analytics.
2. When a new audit job starts, have the tool open a separate sub-chat per data source, one for backlinks, one for a domain overview, one for a content audit, rather than one shared context (inferred as the mechanical setup behind the source's described behavior).
3. Let each sub-chat complete its retrieval and analysis independently, then have the tool roll all sub-chat outputs up into a single synthesized report.
4. Require the synthesized report to cite back to the specific source data behind each claim, not just state conclusions, so hallucinations are easier to catch.
5. Read the synthesized report, then budget real human QA time (the source's benchmark is about an hour for a ~50-page site) checking both the report and the underlying source data it cites.
6. Do not treat the time-savings ratio as reliable until you've replicated it yourself on at least one real audit, since the source explicitly flags this as needing independent verification.

**Tools:** Semrush, Ahrefs, Google Search Console, Google Analytics

**Pitfall:** Trusting a synthesized audit report without QA-ing the underlying source data it was built from defeats the purpose — the reported time savings only hold if a human still verifies both the report and its sources, since the source explicitly still spends about an hour doing exactly that.

### 10. Run the five-plus-one on-page audit with SEO Wallet and Lighthouse  `07.13`
*core · concrete actions · source 07*

This is a fast, repeatable on-page SEO health check usable on any CMS page: five elements (title tag, meta description, H1, H2s, schema) checked via the free 'SEO Wallet' Chrome extension, plus a sixth — page speed — checked via Chrome's built-in Lighthouse tool. The creator's own site example shows what 'good' looks like (one clear H1 targeting the main keyword, logical H2 structure covering secondary keywords, Course/FAQ/Organization schema present) versus minor fixable issues (a meta description running slightly too long). Schema is explicitly unnecessary on every page but required at minimum on all money pages, and a plugin like Yoast or RankMath generating schema automatically still needs manual validation rather than blind trust. The explicit framing is that on-page SEO 'isn't a set-and-forget deal' — this six-point check should be rerun periodically, not just at launch.

> "title tag, meta description, H1, H2s, and schema"

**How to do it**

1. Install the free 'SEO Wallet' Chrome extension (or an equivalent on-page checker plugin).
2. Open the target page and hover the mouse to the left edge of the browser window to trigger the extension's floating toolbar.
3. Check the Title tag: confirm the primary target keyword is present and the phrasing reads naturally; tighten if generic.
4. Check the Meta description: confirm it isn't running long enough to be truncated in search results.
5. Open the Headings tab: confirm exactly one H1 exists and states the page's true focus; confirm H2s/H3s cover secondary keywords from your keyword research.
6. Open the Structured Data/schema tab: confirm relevant schema is present, applying at minimum to every money page.
7. If using Yoast SEO or RankMath, manually validate the schema it generated rather than assuming it's automatically correct.
8. Separately open Chrome DevTools (three-dot menu > More Tools > Developer Tools), select the 'Lighthouse' tab, and click 'Analyze page load.'
9. Review the Performance, Accessibility, Best Practices, and SEO scores, targeting as close to 100 as possible on each.
10. Re-run this entire six-point check periodically, not only at page launch. (inferred cadence, per the source's 'not a set-and-forget deal' framing)

**Tools:** SEO Wallet, Google Chrome DevTools, Lighthouse, Yoast SEO, RankMath

**Pitfall:** Treating on-page SEO as a one-time launch checklist — the creator warns it 'isn't a set-and-forget deal... it can change depending on what you've added to your site,' so scores need periodic re-checking.

### 11. Set up every GSC property variant, not just canonical  `54.1`
*core · concrete actions · source 54*

Glenn Gabe's lessons-for-site-owners section states plainly: set up every version of your site as a Google Search Console property - a domain property, https www, https non-www, http www, http non-www, and important directories - and monitor all of them from both a security and performance perspective. In this case, the client only actively monitored the canonical https-non-www property, which looked completely normal; the domain property (which does exist and covers all protocols/subdomains) had captured a huge, obvious spike in clicks and impressions, but nobody was checking it, and no https-www property existed at all. That missing property and unmonitored data is specifically what let a hacked, non-canonical homepage go unnoticed for a full day.

> "Make sure to set up all versions of your site"

**How to do it**

1. In Google Search Console, add a Domain property for the root domain, which covers all protocols, subdomains, and www/non-www variants in one view.
2. Additionally add separate URL-prefix properties for every individually resolvable variant: https www, https non-www, http www, http non-www.
3. Add URL-prefix properties for important subdirectories as well if your site structure warrants it.
4. Do not skip the non-canonical version of your domain (e.g., www, if your canonical is non-www) just because you don't intentionally serve content there - it can still resolve, get indexed, and be hijacked.
5. Regularly check performance data in every property you've set up, not only the canonical one, since anomalies on a non-canonical version won't appear in the canonical property's report at all.
6. Specifically watch the Domain property for sudden spikes or drops in clicks/impressions that don't match your canonical property's normal trend, since that is often the first visible sign something is wrong on a variant you're not directly watching.
7. Re-review your full property list after any infrastructure change (e.g., decommissioning an old app or redirect service) to confirm every resolvable domain variant still has an active, monitored property.

**Tools:** Google Search Console

**Pitfall:** Only monitoring your canonical URL-prefix property leaves non-canonical but still-resolvable versions of your domain as a complete blind spot - in this case, a hacked www homepage redirecting to a gambling site went undetected because neither an https-www property nor the existing domain property were being checked.

### 12. Technical SEO is the highest-leverage hour on large sites  `46.14`
*core · best practices · source 46*

Asked for the highest-leverage SEO activity per hour worked, Travis answers technical SEO without hesitation, and Edward agrees because 'the reach on that kind of work is so vast' — a single fix can propagate across every template-driven page on a large site at once, unlike content work, which typically only affects the page it's written on. Travis separately flags that technical SEO around JavaScript rendering remains chronically under-invested on large sites: content sitting behind accordions, pop-ups, or other interactive/JS-dependent components needs to be verified as actually crawlable, rendered, and understood by search engines, not just visible to a human clicking through the page. This matters because rendering failures are invisible in normal manual QA — a human clicking an accordion sees the content, while a crawler that doesn't execute the same JavaScript may never see it at all.

> "technical SEO continues to be under-invested"

**How to do it**

1. Run a full technical crawl of the site with JavaScript rendering enabled, comparing the rendered DOM against the raw HTML response (inferred).
2. Specifically audit every accordion, tab, modal, and pop-up component on key pages, such as pricing, feature, and comparison pages, to confirm the content inside is present in the rendered HTML, not just revealed on click.
3. Use Google Search Console's URL Inspection tool to view the rendered screenshot and confirm Googlebot's rendered version actually shows the interactive content (inferred).
4. For any content confirmed hidden from rendering, work with development to either server-side render it or ensure it's present in the initial DOM rather than injected only on user interaction.
5. Prioritize technical SEO fixes on shared templates or components over one-off content edits when time is limited, since a single template-level fix propagates across every page using that template.
6. Re-crawl after each template-level technical fix to confirm the change actually applied site-wide as expected.

**Tools:** Screaming Frog, Google Search Console

**Pitfall:** Content hidden behind accordions, pop-ups, or tabs can look completely normal to a human visitor while being invisible or poorly understood by search engines — this class of JS-rendering issue is easy to miss because manual QA rarely tests it from a crawler's perspective.

### 13. Treat every tracked keyword sitting at >100 as a technical fault, not weak content  `133.1`
*core · concrete actions · source 133*

Grow and Convert's diagnostic on the Circuit account came from their rank tracker, not from a crawl. They expect a new client's articles to appear somewhere in the first ten pages within a few months. On Circuit only one article registered anywhere in the top 100 spots; every other tracked post read Position '>100'. Their rule is explicit: sitting on page 3, 5 or 7 is fine because those posts climb over time, but a whole cohort of posts showing >100 is a red flag that something is structurally wrong. That reading is what sent them looking for the cause, which turned out to be the blog living on a subdomain. The distinction matters because the default reaction to no rankings is to blame content quality or domain rating and write more posts, which on Circuit would have wasted another six months.

> "having all of those posts show up as"

**Evidence:** Circuit, a DR 18 domain: only one article appeared anywhere in the top 100 after months of publishing; all others showed Position >100, which traced to the blog being on a subdomain.

**How to do it**

1. Put every target keyword for every published article into a rank tracker on the day you publish, using Ahrefs Rank Tracker or equivalent.
2. Check the tracker weekly rather than monthly, so a pattern shows up inside two months.
3. Sort by position and count how many tracked posts sit at '>100' after two months live.
4. Treat scattered page-3 to page-7 positions as normal and leave them alone to climb.
5. Escalate when the majority of a cohort reads '>100': that is a structural fault, not a content fault.
6. Check the obvious structural causes in order: blog on a subdomain, noindex tags, blocked robots.txt paths, canonicals pointing elsewhere, unindexed URLs in Search Console.
7. Confirm indexation with a site: query or the URL Inspection tool before blaming the content.
8. Do not commission more articles until the cohort starts registering, because every new post inherits the same fault.

**Tools:** Ahrefs, Google Search Console

**Pitfall:** Reading a >100 cohort as 'SEO takes time' and continuing to publish. Circuit went four months with zero organic conversions before the tracker pattern was read correctly, and every article published in that window inherited the same defect.

**Apply at Pabau:** Pabau should keep a rank tracker with every target keyword from every published article and review it weekly. If a batch of new pabau.com articles shows nothing in the first ten pages two months after publication, stop the content queue and audit indexation and site structure before commissioning more.

**Apply anywhere:** Track every target keyword from the day you publish and review the tracker weekly. Positions on pages 3 to 7 are normal and will climb, but a whole batch of posts reading '>100' after two months is a structural fault. Check subdomain placement, noindex, robots.txt and canonicals before writing anything else.

### 14. Unannounced domain migration caused a 6-7 month ranking crisis  `46.13`
*core · content insights · source 46*

Travis's worst SEO disaster: a client secretly launched a full rebrand onto a brand-new domain three months ahead of the agreed roadmap, telling the agency only after the fact because 'my developer said they could just get this domain live, no problem, and port over all the content.' Because the new domain went live and got indexed while the old branded domain was also still fully live, Google had two indexed copies of the same content under different branding at once, creating simultaneous cannibalization, duplicate-content, and cross-branding problems. The team's emergency fix was a robots.txt disallow directive, not noindex and not nofollow, to force the premature new domain out of the index while the real site build was finished properly; even so, rankings were damaged for six to seven months, the client's revenue, driven mainly by that website, collapsed badly enough that the client nearly went bankrupt, investors got involved, and the CEO nearly lost their job.

> "you had a cannibalization issue, you had duplicate content issues"

**Evidence:** Specific case, unnamed client: a premature, undisclosed domain migration three months ahead of roadmap left both the old branded domain and the new domain fully indexed simultaneously; the fix was a robots.txt disallow to force the new domain out of the index; rankings stayed damaged for six to seven months; the client, whose main lead source was that website, nearly went bankrupt, with investor meetings and the CEO's job on the line as a direct result.

**Apply:** Any domain or rebrand migration must be gated on the SEO team's sign-off and a technical checklist, such as staged robots.txt control on the new domain until cutover and a ready redirect map, before a developer is allowed to push it live — treat 'we just launched the new domain' as an emergency, not a heads-up.

### 15. Use Bing/IndexNow as a proxy for Google indexing  `29.11`
*core · concrete actions · source 29*

Hank's specific pro-tip for diagnosing Google indexing problems is to use Bing's tools as a proxy, since Bing Webmaster Tools 'has nothing to lose' and surfaces far more diagnostic detail than Google does. Concretely: get the site verified with IndexNow so page changes ping Bing's index promptly, then use Bing Webmaster Tools' crawl/render reports to confirm a bot can actually reach and properly render the specific page in question. A clean result there is strong evidence the page is technically fine, so if Google Search Console's URL Inspection tool still won't index it after a manual Request Indexing submission, the real cause is very likely a value/quality judgment by Google's algorithm rather than a technical crawl failure. Hank cautions this manual submission shouldn't become a daily habit - needing to do it constantly is itself a sign of a bigger, foundational site problem rather than a one-off page issue.

> "Bing Webmaster Tools has nothing to lose"

**How to do it**

1. Verify your site with Bing Webmaster Tools, separate from Google Search Console.
2. Enable IndexNow support so page-change pings reach Bing's index (and the wider IndexNow network) promptly.
3. Use Bing Webmaster Tools' crawl and render reports to confirm a bot can reach and properly render the specific problem page.
4. Treat a clean IndexNow/Bing render result as evidence the page is technically accessible.
5. Submit the individual URL via Google Search Console's URL Inspection tool and select Request Indexing.
6. If GSC indexes the page shortly after that request, treat the case as resolved. (inferred)
7. If Google still won't index the page despite a confirmed-clean technical render on Bing, treat that as a value/quality judgment by Google's algorithm rather than a crawl failure, and shift effort to improving or consolidating the page.
8. Avoid making manual URL Inspection submissions a daily habit - needing to do this constantly signals a bigger, foundational site problem rather than a single-page issue.

**Tools:** Bing Webmaster Tools, IndexNow, Google Search Console

**Pitfall:** Resubmitting the same non-indexing pages through GSC's URL Inspection tool every day treats a symptom as the disease - if it keeps failing, the underlying problem is foundational (architecture or content value), and repeated resubmission won't fix it.

### 16. Use server-side 301s, avoid chains, keep the destination relevant  `34.2`
*core · best practices · source 34*

When implementing redirects, use a server-side redirect rather than a client-side one, because the server tells Googlebot that the URL has moved before the page even loads, making it the easiest type of redirect for Google to crawl and understand. Separately, still avoid redirect chains, such as four 301s firing back-to-back-to-back-to-back, not because of authority loss but because chains slow down page load and crawling. And while a 301 redirect does pass link signals including anchor text, redirecting a page to an irrelevant destination doesn't make backlinks pointing at the old page magically relevant to the new one; the destination must still make topical sense to the users following that link, and the cleanest redirect is one where every other element of the page, such as title, content, and structure, stays the same and only the URL changes.

> "server tells Googlebot that the URL moved before the page even loads"

**How to do it**

1. When setting up any redirect, implement it at the server level, via your CMS, .htaccess, or server configuration, or your hosting platform's redirect rules, rather than a client-side JavaScript or meta-refresh redirect.
2. Confirm the redirect returns an HTTP 301 status code specifically for any permanent URL change, using a header-checking tool (inferred verification step).
3. Before finalizing any redirect, map the old URL to the single most topically relevant new destination available, rather than defaulting to the homepage.
4. Check your existing redirect map for chains, where URL A redirects to B which redirects to C which redirects to D, and collapse each chain down to a single hop from the original URL straight to the final destination.
5. After any site migration or URL restructuring, keep the page title, main content, and overall structure as close to identical as possible, changing only the URL, to make the redirect as clean as possible for both users and Google.
6. Spot-check a sample of redirects post-launch by loading old URLs directly and confirming they land on the intended relevant page with a 301 status (inferred QA step).

**Pitfall:** Using a 301 redirect to send an irrelevant page's backlinks to an unrelated destination does not make those backlinks suddenly relevant — the redirect target still has to make topical sense, or users following the link end up confused or disappointed.

### 17. XML sitemaps don't force indexing; fix limits a month early  `45.3`
*core · best practices · source 45*

David flags that an XML sitemap is commonly misunderstood as something that helps Google index content, when its real function is closer to a 'crawl, not index' signal — having a sitemap does not mean Google prioritizes indexing what's in it. As part of the same pre-migration prep window, he flags a specific technical limit that trips people up: an XML sitemap cannot exceed 50,000 lines, and if you don't already know this, you need to find out and restructure it at least a month before migrating, not discover it mid-migration. He bundles this with two other must-do items in the same prep window: force your site consistently onto www (or non-www) and force everything onto HTTPS/SSL, so none of these configuration questions are still open when the migration itself begins.

> "XML sitemaps don't pass authority — we've discussed this before"

**How to do it**

1. Confirm you have both an XML sitemap and an HTML sitemap in place before migration (most sites only have the XML one).
2. Check your current XML sitemap's total URL count; if it is approaching or exceeds 50,000 URLs, split it into multiple sitemap files referenced by a sitemap index file.
3. Verify your site consistently forces all traffic to a single www/non-www version, with no mixed accessibility on both.
4. Verify your site forces all traffic to HTTPS with no accessible HTTP versions of any page.
5. Complete all of the above at least one month before the migration date, not during or immediately before it.
6. Re-check all four items (HTML sitemap present, XML sitemap under the line limit, www forcing, HTTPS forcing) right before freeze/migration to confirm nothing regressed (inferred verification step).

**Tools:** XML sitemap, HTML sitemap

**Pitfall:** Assuming that having an XML sitemap means Google will prioritize indexing its contents — David says people report 'I have a sitemap' and expect that to solve indexing problems, when Google 'just doesn't care' about the sitemap forcing anything.
