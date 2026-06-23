# Open Source Issue Video Project Board

Purpose: turn approachable GitHub issues into focused troubleshooting/build videos.

## Active candidates

| Status | Repo | Issue | Language | Video angle | Next action |
|---|---|---|---|---|---|
| backlog | storybookjs/storybook | [#35213](https://github.com/storybookjs/storybook/issues/35213) | React/TypeScript | Next.js Link mock calls preventDefault before user onClick | Clone repo and run contributor tests |
| backlog | TanStack/query | [#9681](https://github.com/TanStack/query/issues/9681) | React/TypeScript | Query DevTools multiple instances are not isolated | Clone repo and run contributor tests |
| backlog | eslint/eslint | [#20987](https://github.com/eslint/eslint/issues/20987) | JavaScript | prefer-exponentiation-operator autofix can generate SyntaxError | Clone repo and run contributor tests |
| backlog | caddyserver/caddy | [#7833](https://github.com/caddyserver/caddy/issues/7833) | Go | Resource leaks on error paths found by static analyzer | Clone repo and run contributor tests |
| backlog | keploy/keploy | [#2601](https://github.com/keploy/keploy/issues/2601) | Go | Improve GitHub API rate limit handling in stargazers script | Clone repo and run contributor tests |
| backlog | kubernetes/minikube | [#23163](https://github.com/kubernetes/minikube/issues/23163) | Go | Flaky TestDownloadOnly preload tarball missing on Docker | Clone repo and run contributor tests |
| backlog | detekt/detekt | [#9279](https://github.com/detekt/detekt/issues/9279) | Kotlin | Allow UnnecessaryFullyQualifiedName ignore packages | Clone repo and run contributor tests |
| backlog | coil-kt/coil | [#2779](https://github.com/coil-kt/coil/issues/2779) | Kotlin/Compose | Placeholder image changes AsyncImage ContentScale behavior | Clone repo and run contributor tests |

## Working rules

- Do not claim the issue is easy until the project builds locally.
- Start every video with a failing test or reproducible behavior.
- If reproduction takes more than two hours, convert the video into an investigation episode and pick a smaller fix for the PR.
- Prefer issues where the final PR can stay under about 150 changed lines.
- Keep a clean branch name: `fix/<issue-number>-short-slug` or `feat/<issue-number>-short-slug`.
