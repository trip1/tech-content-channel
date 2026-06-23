# Open Source Issue Video Series Plan

## Series concept

Find well-scoped issues in popular open-source projects, reproduce the bug or request, debug it systematically, and submit a clean PR — all while teaching real-world troubleshooting habits.

## Audience promise

Viewers learn how experienced developers approach unfamiliar codebases without pretending everything works on the first try.

## Repeatable video structure

1. **Issue triage** — read the report, labels, maintainer comments, and acceptance signals.
2. **Environment setup** — clone, install, run baseline tests.
3. **Reproduction** — create the smallest failing example or test.
4. **Root-cause trace** — follow data/control flow until the cause is clear.
5. **Patch** — implement one minimal fix.
6. **Verification** — targeted test plus relevant wider suite.
7. **PR prep** — explain diff, risk, and how it closes the issue.

## Candidate episodes

### 1. storybookjs/storybook #35213 — Next.js Link mock calls preventDefault before user onClick

- Issue: https://github.com/storybookjs/storybook/issues/35213
- Focus: React/TypeScript
- Fit: high
- Episode folder: `02-video-pipeline/episodes/2026-06-23-storybook-35213-next-js-link-mock-calls-preventdefault-before-user-onc/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 2. TanStack/query #9681 — Query DevTools multiple instances are not isolated

- Issue: https://github.com/TanStack/query/issues/9681
- Focus: React/TypeScript
- Fit: medium
- Episode folder: `02-video-pipeline/episodes/2026-06-23-query-9681-query-devtools-multiple-instances-are-not-isolated/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 3. eslint/eslint #20987 — prefer-exponentiation-operator autofix can generate SyntaxError

- Issue: https://github.com/eslint/eslint/issues/20987
- Focus: JavaScript
- Fit: high
- Episode folder: `02-video-pipeline/episodes/2026-06-23-eslint-20987-prefer-exponentiation-operator-autofix-can-generate-synta/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 4. caddyserver/caddy #7833 — Resource leaks on error paths found by static analyzer

- Issue: https://github.com/caddyserver/caddy/issues/7833
- Focus: Go
- Fit: high
- Episode folder: `02-video-pipeline/episodes/2026-06-23-caddy-7833-resource-leaks-on-error-paths-found-by-static-analyzer/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 5. keploy/keploy #2601 — Improve GitHub API rate limit handling in stargazers script

- Issue: https://github.com/keploy/keploy/issues/2601
- Focus: Go
- Fit: high
- Episode folder: `02-video-pipeline/episodes/2026-06-23-keploy-2601-improve-github-api-rate-limit-handling-in-stargazers-scrip/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 6. kubernetes/minikube #23163 — Flaky TestDownloadOnly preload tarball missing on Docker

- Issue: https://github.com/kubernetes/minikube/issues/23163
- Focus: Go
- Fit: medium
- Episode folder: `02-video-pipeline/episodes/2026-06-23-minikube-23163-flaky-testdownloadonly-preload-tarball-missing-on-docke/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 7. detekt/detekt #9279 — Allow UnnecessaryFullyQualifiedName ignore packages

- Issue: https://github.com/detekt/detekt/issues/9279
- Focus: Kotlin
- Fit: high
- Episode folder: `02-video-pipeline/episodes/2026-06-23-detekt-9279-allow-unnecessaryfullyqualifiedname-ignore-packages/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

### 8. coil-kt/coil #2779 — Placeholder image changes AsyncImage ContentScale behavior

- Issue: https://github.com/coil-kt/coil/issues/2779
- Focus: Kotlin/Compose
- Fit: high
- Episode folder: `02-video-pipeline/episodes/2026-06-23-coil-2779-placeholder-image-changes-asyncimage-contentscale-behavior/`
- First recording goal: reproduce the behavior and identify the smallest test that should fail.

