# Outline: Allow UnnecessaryFullyQualifiedName ignore packages

## Cold open

Show the GitHub issue and the one-line challenge: **Allow configuring UnnecessaryFullyQualifiedName to ignore certain packages**

## Segment 1 — Triage the issue

- Repo credibility: detekt/detekt with 6,979 stars.
- Labels: help wanted, feature, good first issue.
- Read the issue body and comments.
- Extract expected behavior, actual behavior, and likely files/tests.

## Segment 2 — Setup

```bash
git clone https://github.com/detekt/detekt.git
cd detekt
git checkout -b fix/9279-allow-unnecessaryfullyqualifiedname
```

Then follow the repository's contributing docs before guessing commands.

## Segment 3 — Reproduce

- Run the smallest relevant test/demo first.
- If there is no test, write one from the issue's reproduction steps.
- Capture the failing output for the video.

## Segment 4 — Root cause

Use the 4-phase debugging process:

1. Read error/output carefully.
2. Trace from failing behavior to source.
3. Compare with a working path.
4. Form one hypothesis before changing code.

## Segment 5 — Fix

- Make one minimal change.
- Avoid opportunistic refactors.
- Keep commit focused on issue #9279.

## Segment 6 — Verify

- Run targeted tests.
- Run formatter/linter if required.
- Run a broader suite only if it is feasible in recording time.

## Segment 7 — PR package

- Explain what changed.
- Include test evidence.
- Link the issue with `Fixes #9279` in the PR body.

## Possible title ideas

- `Fixing a Real Bug in detekt: From GitHub Issue to PR`
- `I Tried Solving detekt/detekt #9279 in One Day`
- `How to Debug an Open Source Issue Without Knowing the Codebase`
