# Troubleshooting Plan

## Issue

- Repo: storybookjs/storybook
- Issue: https://github.com/storybookjs/storybook/issues/35213
- Video angle: Next.js Link mock calls preventDefault before user onClick

## Phase 1 — Root cause investigation

- [ ] Read the full issue body.
- [ ] Read maintainer/user comments.
- [ ] Clone repository and read `CONTRIBUTING`, test docs, and package/build files.
- [ ] Run baseline tests before changes.
- [ ] Reproduce issue with the smallest command or example.
- [ ] Capture failing output.

## Phase 2 — Pattern analysis

- [ ] Find nearby tests for similar behavior.
- [ ] Find existing implementation patterns in the same package/module.
- [ ] Compare broken and working paths.
- [ ] Identify acceptance criteria from issue plus tests.

## Phase 3 — Hypothesis testing

- [ ] Write one failing test.
- [ ] State the root-cause hypothesis on camera.
- [ ] Make the smallest code change to test it.

## Phase 4 — Implementation

- [ ] Finalize minimal patch.
- [ ] Run targeted test.
- [ ] Run formatter/linter.
- [ ] Capture final passing output.
- [ ] Prepare PR description.

## PR description skeleton

```markdown
## Summary
- 

## Fix
- 

## Tests
- [ ] 

Fixes #35213
```
