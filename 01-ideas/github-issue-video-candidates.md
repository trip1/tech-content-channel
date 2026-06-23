# GitHub Issue Video Candidates

These are starter targets for the open-source troubleshooting video series. The filter favors popular repositories, detailed bug reports or feature requests, labels that suggest contributor friendliness, and topics that can plausibly be investigated in roughly a day.

## Selection criteria

- Focus languages: React, JavaScript/TypeScript, Go, Kotlin/Compose
- Popular or recognizable repo with active issue tracker
- Open issue with enough detail to make a video narrative
- Prefer `good first issue`, `help wanted`, `accepted`, or concrete repro details
- Avoid huge architectural rewrites unless the video can be scoped to investigation plus a minimal PR

## Shortlist

| # | Repo / issue | Focus | Stars | Labels | Body chars | Comments | Fit |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [storybookjs/storybook #35213](https://github.com/storybookjs/storybook/issues/35213) | React/TypeScript | 90,416 | bug, nextjs, needs triage | 2554 | 1 | high |
| 2 | [TanStack/query #9681](https://github.com/TanStack/query/issues/9681) | React/TypeScript | 49,823 | help wanted, package: query-devtools | 1044 | 1 | medium |
| 3 | [eslint/eslint #20987](https://github.com/eslint/eslint/issues/20987) | JavaScript | 27,389 | bug, rule, accepted, autofix | 2044 | 5 | high |
| 4 | [caddyserver/caddy #7833](https://github.com/caddyserver/caddy/issues/7833) | Go | 73,509 | bug :lady_beetle:, good first issue :baby_chick: | 5119 | 7 | high |
| 5 | [keploy/keploy #2601](https://github.com/keploy/keploy/issues/2601) | Go | 17,743 | Enhancement, Good First Issue, GSoC, keploy | 3332 | 6 | high |
| 6 | [kubernetes/minikube #23163](https://github.com/kubernetes/minikube/issues/23163) | Go | 31,894 | area/testing, needs-triage | 1825 | 0 | medium |
| 7 | [detekt/detekt #9279](https://github.com/detekt/detekt/issues/9279) | Kotlin | 6,979 | help wanted, feature, good first issue | 319 | 19 | high |
| 8 | [coil-kt/coil #2779](https://github.com/coil-kt/coil/issues/2779) | Kotlin/Compose | 11,827 | help wanted | 1334 | 3 | high |

## Suggested order

1. **Caddy #7833** — highest confidence: static analyzer report, concrete files/paths, good-first-issue label, likely small resource cleanup tests.
2. **ESLint #20987** — strong JavaScript debugging story: reproduce invalid autofix, write RuleTester case, patch fixer.
3. **Coil #2779** — visual Kotlin/Compose bug with screenshots; good for UI-polish audience.
4. **Storybook #35213** — React/Next.js event-order bug; strong explanation value.
5. **Keploy #2601** — Go CLI/API reliability feature with clear implementation requirements.
6. **TanStack Query #9681** — React DevTools state isolation issue; potentially a clean component-state debugging video.
7. **detekt #9279** — Kotlin static-analysis rule option; compact scope once test harness is understood.
8. **minikube #23163** — good Go infra content, but likely heavier environment; treat as stretch or investigation-only video if reproduction is expensive.

## Episode pattern for each issue

- Cold open: show issue and why it matters.
- Clone/build: get project running and tests green.
- Reproduce: create or run a failing test.
- Root cause: trace the code path and compare to working behavior.
- Fix: smallest change that addresses the cause.
- Verify: targeted test, then relevant wider test suite.
- PR package: explain commit, PR description, and what maintainers need to review.
