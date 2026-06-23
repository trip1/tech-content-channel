# Outline: Improve GitHub API rate limit handling in stargazers script

## Cold open

Show the GitHub issue and the one-line challenge: **[feature]: Improve GitHub API Rate Limit Handling for Large Repositories in the stargazers script**

## Segment 1 — Triage the issue

- Repo credibility: keploy/keploy with 17,743 stars.
- Labels: Enhancement, Good First Issue, GSoC, keploy.
- Read the issue body and comments.
- Extract expected behavior, actual behavior, and likely files/tests.

## Segment 2 — Setup

```bash
git clone https://github.com/keploy/keploy.git
cd keploy
git checkout -b fix/2601-improve-github-api-rate-limit-handl
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
- Keep commit focused on issue #2601.

## Segment 6 — Verify

- Run targeted tests.
- Run formatter/linter if required.
- Run a broader suite only if it is feasible in recording time.

## Segment 7 — PR package

- Explain what changed.
- Include test evidence.
- Link the issue with `Fixes #2601` in the PR body.

## Possible title ideas

- `Fixing a Real Bug in keploy: From GitHub Issue to PR`
- `I Tried Solving keploy/keploy #2601 in One Day`
- `How to Debug an Open Source Issue Without Knowing the Codebase`
