# Video production walkthrough

Use this guide to move a video from raw idea to published upload without losing the story, proof, or packaging along the way.

The repo is the source of truth. Every major video should have an episode folder, a clear status on the production board, and a checklist copied from `templates/production-checklist.md`.

## Pipeline overview

```text
Idea -> Validation -> Packaging -> Script -> Production plan -> Record -> Edit -> Review -> Publish -> Repurpose -> Analyze
```

Repo map:

```text
01-ideas/inbox.md
  -> 01-ideas/validated-ideas.md
  -> 02-video-pipeline/backlog.md
  -> 02-video-pipeline/episodes/[episode]/
  -> 02-video-pipeline/production-board.md
  -> 05-assets/
  -> 06-publishing/
  -> 07-analytics/
```

## 1. Capture the idea

Start in `01-ideas/inbox.md`.

Capture messy ideas quickly. Do not overwork them yet. A useful raw idea only needs:

- source/link
- one-line premise
- why it might matter
- possible audience
- whether it is timely, evergreen, or a build/tutorial

Example:

```markdown
- Zero-downtime Docker Compose deploys
  - Source: HN
  - Premise: deploy without Kubernetes
  - Audience: homelab, small SaaS, self-hosters
  - Possible hook: You probably do not need Kubernetes for this
```

## 2. Validate before scripting

Move an idea to `01-ideas/validated-ideas.md` only when it has:

| Requirement | Question |
|---|---|
| Audience | Who specifically cares? |
| Hook | Why would they click? |
| Outcome | What do they learn, build, or decide? |
| Feasible recording plan | Can you show something on screen? |
| Timeliness | Is this trending, evergreen, or tied to current news? |

Score each idea 1-5:

| Category | What to look for |
|---|---|
| Click potential | Clear curiosity gap or useful promise |
| Audience fit | Homelab/dev/server/AI/tooling viewers |
| Demonstrability | Can you show it working? |
| Story tension | Is there a tradeoff, risk, failure, or surprising result? |
| Reuse potential | Can it become Shorts, follow-ups, or a series? |

As a rule, prioritize ideas scoring **18+ out of 25** unless there is a strategic reason to make the video anyway.

## 3. Promote to the backlog

Add validated ideas to `02-video-pipeline/backlog.md`.

Recommended statuses:

```text
idea
researching
ready-to-script
scripting
ready-to-record
recording
editing
scheduled
published
repurpose
```

Then add active work to `02-video-pipeline/production-board.md`.

## 4. Create the episode folder

Create one folder per major video:

```text
02-video-pipeline/episodes/YYYY-MM-DD-working-slug/
```

Recommended files:

```text
brief.md
research.md
packaging.md
script.md
shot-list.md
edit-notes.md
publish-notes.md
production-checklist.md
assets/
```

Start by copying:

```bash
cp templates/episode-brief.md 02-video-pipeline/episodes/YYYY-MM-DD-slug/brief.md
cp templates/video-script.md 02-video-pipeline/episodes/YYYY-MM-DD-slug/script.md
cp templates/production-checklist.md 02-video-pipeline/episodes/YYYY-MM-DD-slug/production-checklist.md
```

## 5. Package before scripting

Do **not** write the full script first. Package the video first.

Create `packaging.md` with:

```markdown
# Packaging

## Core promise

## Audience

## Viewer transformation

Before:
After:

## Title options

1.
2.
3.
4.
5.

## Best title

## Thumbnail concepts

### Concept A
Visual:
Text:

### Concept B
Visual:
Text:

## First 30 seconds

## Open loops

1.
2.
3.
```

Good technical title patterns:

```text
I found X. There is one catch.
This solves the annoying tradeoff between A and B.
I tested X so you do not break your server.
You probably do not need Kubernetes for this.
The weird feature I wish was built in.
X is faster than I expected, but I would not use it everywhere.
```

Thumbnail rule: the title and thumbnail should complete each other, not repeat each other.

Examples:

| Title | Thumbnail text |
|---|---|
| Zero-downtime deploys without Kubernetes | `NO K8S` |
| I found container-speed VMs for Proxmox | `FAST VMs?` |
| AI pull request spam is already here | `PR SPAM` |

## 6. Write a block script

Write `script.md` as blocks, not a wall of narration.

Each block should include:

```markdown
## Block 1: cold open

**Time:** 0:00-0:25

**On screen**

**Voiceover / talking head**

**Retention beat**

**Open loop**
```

Recommended 8-11 minute cadence:

| Time | Segment | Job |
|---:|---|---|
| 0:00-0:25 | Cold open | Show result + conflict |
| 0:25-1:20 | Pain/tradeoff | Make viewer feel seen |
| 1:20-2:20 | Tool/concept | Introduce the solution |
| 2:20-3:15 | Prereqs/risks | Build trust |
| 3:15-5:30 | Demo/build | Practical progress |
| 5:30-7:15 | Verification | Show it actually works |
| 7:15-8:45 | Pros/limits | Decision clarity |
| 8:45-10:00 | Recommendation | Should viewer use it? |
| 10:00-10:30 | Next step | Tease follow-up |

Every script needs:

- a cold open
- a visible payoff
- a risk, tradeoff, or failure
- a recommendation
- a follow-up idea

Do not make flat tutorials. Make decision stories.

## 7. Build the production plan

Create `shot-list.md`:

```markdown
# Shot list

## Talking head

- [ ] Cold open
- [ ] Setup
- [ ] Recommendation
- [ ] CTA

## Screen recordings

- [ ] GitHub/project page
- [ ] Install commands
- [ ] Config files
- [ ] Before state
- [ ] After state
- [ ] Verification commands

## B-roll

- [ ] Server rack
- [ ] Proxmox dashboard
- [ ] Terminal closeups
- [ ] Diagrams
- [ ] Error/failure moment

## Graphics

- [ ] Architecture diagram
- [ ] Decision matrix
- [ ] Before/after comparison
- [ ] Warning card
```

Technical proof to capture when relevant:

```text
version commands
install commands
config files
working proof
failure/rollback notes
```

Examples:

```bash
pveversion
docker compose ps
curl localhost:8080/health
git diff
systemctl status service-name
```

## 8. Record in layers

Do not record the entire video linearly.

Recommended order:

1. **Record the result first**: working app, successful deploy, benchmark, before/after, terminal proof.
2. **Record the technical walkthrough**: commands, configuration, errors, verification.
3. **Record talking head last**: by then you know what actually happened.
4. **Record pickup lines**: short connective lines after the rough edit exposes gaps.

Useful pickup lines:

```text
This is where I hit the first problem.
Here is the part I would not do on a production server.
This worked, but not for the reason I expected.
```

## 9. Edit for retention

Create `edit-notes.md`.

Editing priorities:

| Priority | What to do |
|---|---|
| First 30 seconds | No intro fluff. Reaffirm title immediately. |
| Every 30-45 seconds | Change visual state: talking head, terminal, diagram, b-roll. |
| Every 1-2 minutes | Resolve or deepen an open loop. |
| Midpoint | Show a real result or real problem. |
| Final third | Give decision clarity, not more setup. |

Before export, check:

- [ ] Does the first 10 seconds match the title/thumbnail?
- [ ] Is there a reason to keep watching after the hook?
- [ ] Does the video show the result early?
- [ ] Is there a visible payoff?
- [ ] Are the boring commands trimmed?
- [ ] Did you leave in one useful failure?
- [ ] Did you give a clear recommendation?

## 10. Build the publishing package

Create `publish-notes.md`:

```markdown
# Publish notes

## Final title

## Thumbnail

## Description

## Chapters

00:00
00:30
01:20

## Links

## Pinned comment

## Tags

## End screen

## Cards

## Shorts to cut

1.
2.
3.

## Follow-up video
```

Description structure:

```markdown
One-sentence promise.

In this video:
- Point 1
- Point 2
- Point 3

Links:
- Project:
- Article:
- Repo:

Chapters:
00:00 ...
```

Good pinned comment:

```markdown
Commands, links, and corrections are here.

If you want the follow-up, comment `[keyword]` and I will build it next.
```

## 11. Release and repurpose

After publishing, immediately create:

| Asset | Purpose |
|---|---|
| 2-3 Shorts | Fast discovery |
| 1 community post | Ask a question |
| 1 X/Twitter/Bluesky thread | Summarize lesson |
| 1 follow-up idea | Keep series momentum |

Shorts should come from:

- best cold open line
- biggest mistake
- strongest opinion
- before/after result
- surprising command/output

Example:

```text
AI makes writing pull requests cheap. It does not make reviewing them cheap.
```

## 12. Analyze after 48 hours and 7 days

Use `07-analytics/metrics-review.md`.

Track:

| Metric | Why it matters |
|---|---|
| CTR | Packaging strength |
| First 30-second retention | Hook match |
| Average view duration | Story strength |
| Drop-off points | Boring/confusing sections |
| Comments | Audience demand |
| Subs gained | Channel fit |
| Returning viewers | Series potential |

Post-mortem format:

```markdown
# Metrics review: [video title]

## Packaging

Title:
Thumbnail:
CTR:

## Retention

First 30 seconds:
Average view duration:
Biggest drop:

## Audience signal

Comments:
Questions:
Follow-up requests:

## What worked

## What to change next time

## Follow-up decision
```

## Weekly production rhythm

| Day | Job |
|---|---|
| Monday | Research and select one main video + 2 Shorts |
| Tuesday | Package and script |
| Wednesday | Build/demo and screen record |
| Thursday | Talking head and pickups |
| Friday | Rough/final edit |
| Saturday | Publish package and schedule/upload |
| Sunday | Repurpose and analytics review |

## Definition of done

A video project is production-ready when:

- [ ] Packaging is done before recording.
- [ ] Script has blocks, visuals, and retention beats.
- [ ] Technical proof is captured.
- [ ] Thumbnail concept exists before the edit is final.
- [ ] Publish notes include title, description, chapters, links, pinned comment, and Shorts.
- [ ] Production checklist is complete through the current stage.
