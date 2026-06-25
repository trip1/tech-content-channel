# Tech Content Channel

Planning hub for a software development, server infrastructure, homelab, and general tech content channel across Twitch, Kick, YouTube, Shorts, TikTok, and related platforms.

## Channel pillars

| Pillar | Focus | Example formats |
|---|---|---|
| Software Development | Apps, automation, tooling, debugging, architecture | build-alongs, code reviews, sprint recaps |
| Server Infrastructure | Linux, Docker, Proxmox, networking, deployment | live rebuilds, explainers, troubleshooting |
| Homelab | Rack/server projects, media stacks, backups, monitoring | lab tours, upgrade logs, incident breakdowns |
| Tech Experiments | AI tooling, gadgets, workflows, productivity | first looks, experiments, comparison videos |

## Repository map

```text
.
├── 00-admin/              # Strategy, brand, platform setup, creator ops
├── 01-ideas/              # Raw ideas, validated concepts, research notes
├── 02-video-pipeline/     # Backlog, scripts, outlines, production checklists
├── 03-streaming/          # Live stream plans, run-of-show docs, overlays notes
├── 04-projects/           # Content-driven technical project task boards
├── 05-assets/             # Asset notes, thumbnail briefs, b-roll shot lists
├── 06-publishing/         # Platform-specific publishing checklists/templates
├── 07-analytics/          # Metrics reviews and post-mortems
└── templates/             # Reusable docs for ideas, episodes, projects
```

## Weekly workflow

Follow the full walkthrough in `02-video-pipeline/video-production-walkthrough.md`.

1. Capture raw ideas in `01-ideas/inbox.md`.
2. Validate strong ideas in `01-ideas/validated-ideas.md`.
3. Promote promising ideas into `02-video-pipeline/backlog.md`.
4. Create an episode folder from `templates/episode-brief.md`.
5. Copy `templates/production-checklist.md` into the episode folder.
6. Package the video before scripting: title, thumbnail, first 30 seconds, open loops.
7. Record proof/result first, then walkthrough, then talking head.
8. Publish using `06-publishing/publishing-checklist.md`.
9. Review performance in `07-analytics/metrics-review.md`.

## Status tags

- `idea` — raw concept, not validated
- `researching` — collecting sources/examples
- `ready-to-script` — title, hook, and outline are clear
- `recording` — currently filming/streaming
- `editing` — post-production in progress
- `scheduled` — uploaded and scheduled
- `published` — live
- `repurpose` — needs Shorts/TikTok/thread cuts
