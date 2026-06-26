# Production checklist: Stop prompting coding agents. Build them a loop.

Copy this file into every new episode folder as `production-checklist.md`.

Episode folder:

```text
02-video-pipeline/episodes/2026-06-25-agentic-loops-from-scratch/
```

## 0. Project setup

- [ ] Episode folder created
- [ ] `brief.md` copied from `templates/episode-brief.md`
- [ ] `script.md` copied from `templates/video-script.md` or created as block script
- [ ] `production-checklist.md` copied into episode folder
- [ ] Active project added to `02-video-pipeline/production-board.md`
- [ ] Backlog status updated in `02-video-pipeline/backlog.md`

## 1. Idea validation

- [ ] Source/link captured in `research.md`
- [ ] Audience is specific
- [ ] Hook is clear in one sentence
- [ ] Viewer outcome is clear
- [ ] Recording/demo plan is feasible
- [ ] Timeliness noted: trending / evergreen / build tutorial
- [ ] Idea scored against click, fit, demonstrability, tension, reuse

## 2. Packaging

- [ ] `packaging.md` created
- [ ] Core promise written
- [ ] Viewer transformation written: before -> after
- [ ] 5+ title options drafted
- [ ] Best title selected
- [ ] 2+ thumbnail concepts drafted
- [ ] Thumbnail text selected
- [ ] First 30 seconds drafted
- [ ] Open loops defined
- [ ] CTA/follow-up idea selected

## 3. Research

- [ ] Primary sources saved in `research.md`
- [ ] Key claims verified
- [ ] Any numbers/stats sourced
- [ ] Counterpoint or limitation captured
- [ ] For technical videos: docs/readme/install notes checked
- [ ] For trend videos: source date and current relevance noted

## 4. Script

- [ ] Block script complete
- [ ] Cold open starts with result, conflict, or strong premise
- [ ] No generic intro or throat-clearing
- [ ] Each block has timestamp range
- [ ] Each block has on-screen visuals or commands
- [ ] Each block has voiceover/talking-head copy
- [ ] Each block has a retention beat or open loop
- [ ] Recommendation/decision section included
- [ ] CTA included
- [ ] Chapters drafted
- [ ] Shorts moments marked

## 5. Technical proof / build prep

Use this section for setup, software, server, homelab, and coding videos.

- [ ] Versions captured
- [ ] Install/setup commands captured
- [ ] Config files captured
- [ ] Before state captured
- [ ] After state captured
- [ ] Verification commands captured
- [ ] Failure or limitation captured
- [ ] Rollback/cleanup commands captured, if relevant
- [ ] Working result recorded before teardown

Useful proof examples:

```bash
pveversion
docker compose ps
curl localhost:8080/health
git diff
systemctl status service-name
```

## 6. Shot list

- [ ] `shot-list.md` created
- [ ] Talking-head shots listed
- [ ] Screen recordings listed
- [ ] B-roll listed
- [ ] Graphics/diagrams listed
- [ ] Thumbnail screenshot/source image planned
- [ ] Any sensitive info/redaction needs noted

## 7. Recording

- [ ] Final result recorded first
- [ ] Technical walkthrough recorded
- [ ] Talking head recorded
- [ ] Cold open recorded
- [ ] Recommendation/CTA recorded
- [ ] Pickup lines recorded after reviewing rough cut
- [ ] Audio checked
- [ ] Screen capture resolution checked
- [ ] Important terminal text readable

## 8. Edit

- [ ] `edit-notes.md` created
- [ ] Rough cut complete
- [ ] First 30 seconds tightened
- [ ] Title/thumbnail promise reaffirmed immediately
- [ ] Boring waits trimmed
- [ ] Visual state changes every 30-45 seconds where possible
- [ ] Diagrams/callouts added
- [ ] Captions or code callouts added where useful
- [ ] Music/SFX balanced
- [ ] Audio cleaned
- [ ] Final export complete

## 9. Publish package

- [ ] `publish-notes.md` created
- [ ] Final title selected
- [ ] Thumbnail exported
- [ ] Description written
- [ ] Links added
- [ ] Chapters added
- [ ] Tags/keywords added
- [ ] Pinned comment drafted
- [ ] End screen selected
- [ ] Cards selected
- [ ] Visibility/schedule set
- [ ] Upload checked after processing

## 10. Repurpose

- [ ] Short 1 selected
- [ ] Short 2 selected
- [ ] Short 3 selected
- [ ] Community post drafted
- [ ] X/Twitter/Bluesky/thread drafted
- [ ] Follow-up video idea added to backlog
- [ ] Repo notes updated with published link

## 11. Analytics

### 48-hour review

- [ ] Views checked
- [ ] CTR checked
- [ ] First 30-second retention checked
- [ ] Average view duration checked
- [ ] Comments/questions reviewed
- [ ] Immediate packaging lesson written

### 7-day review

- [ ] Views checked
- [ ] CTR checked
- [ ] Average view duration checked
- [ ] Retention drop-offs reviewed
- [ ] Subs gained/lost checked
- [ ] Follow-up decision made
- [ ] `07-analytics/metrics-review.md` updated

## 12. Final status updates

- [ ] `02-video-pipeline/production-board.md` updated
- [ ] `02-video-pipeline/backlog.md` status updated
- [ ] `01-ideas/validated-ideas.md` status updated, if needed
- [ ] Episode folder complete
- [ ] Git commit created for final notes/checklist updates
