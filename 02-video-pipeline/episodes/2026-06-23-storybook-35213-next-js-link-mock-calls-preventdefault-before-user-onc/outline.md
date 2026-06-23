# Outline: Next.js Link mock calls preventDefault before user onClick

## Cold open

Show the GitHub issue and the one-line challenge: **[Bug]: @storybook/nextjs-vite next/link mock calls preventDefault before onClick**

## Segment 1 — Triage the issue

- Repo credibility: storybookjs/storybook with 90,416 stars.
- Labels: bug, nextjs, needs triage.
- Read the issue body and comments.
- Extract expected behavior, actual behavior, and likely files/tests.

## Segment 2 — Setup

```bash
git clone https://github.com/storybookjs/storybook.git
cd storybook
git checkout -b fix/35213-next-js-link-mock-calls-preventdefa
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
- Keep commit focused on issue #35213.

## Segment 6 — Verify

- Run targeted tests.
- Run formatter/linter if required.
- Run a broader suite only if it is feasible in recording time.

## Segment 7 — PR package

- Explain what changed.
- Include test evidence.
- Link the issue with `Fixes #35213` in the PR body.

## Possible title ideas

- `Fixing a Real Bug in storybook: From GitHub Issue to PR`
- `I Tried Solving storybookjs/storybook #35213 in One Day`
- `How to Debug an Open Source Issue Without Knowing the Codebase`
