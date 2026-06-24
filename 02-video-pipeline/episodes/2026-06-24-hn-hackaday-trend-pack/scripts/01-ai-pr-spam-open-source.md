# Script: AI PR spam is about to hit open source hard

## Episode brief

- Status: ready-to-script
- Pillar: Software Development / Tech Experiments
- Format: YouTube commentary explainer
- Source stories: HN "PR spam today looks like email spam in the early 2000s" and GitHub pull request limit discussion
- Target length: 8-10 minutes

## Packaging

### Title options

1. **Open source is getting its spam moment**
2. **AI pull request spam is already here**
3. **Maintainers are about to drown in AI PRs**
4. **The next spam war is on GitHub**

Best pick: **AI pull request spam is already here**

### Thumbnail

Visual: GitHub pull request page flooded with identical AI bot avatars, red spam stamps, one tired maintainer in the corner.

Text: **PR SPAM**

## Cold open / hook

> Show a fake but believable GitHub PR list filling up fast.

Email spam had a look. Weird subject lines, fake urgency, too many messages from people you never asked to hear from.

Open source is getting its version of that.

It does not arrive as email. It arrives as pull requests. Some are helpful. Some are lazy. Some look useful for about twelve seconds, until a maintainer has to spend real time proving they are not.

That is the scary part. AI makes the cost of opening a PR close to zero, but the cost of reviewing one stays painfully human.

## Setup

- What we're explaining: why AI-generated PR spam is becoming a real maintainer problem.
- Why it matters: open source depends on review attention, and review attention does not scale like generated code.
- Stakes: if maintainers get buried, they add friction, quotas, or gates. That changes open source culture.

## Segment 1: why this feels different from bad PRs

Bad PRs are not new. Maintainers have always dealt with drive-by typo fixes, half-finished refactors, and people changing code they do not understand.

The difference now is volume.

A person can open a bad PR. An AI-assisted workflow can open ten before lunch. The bottleneck moves from writing code to judging whether the code deserves attention.

That is why the email spam comparison works. Spam did not win because each message was clever. It became a problem because sending got cheap and filtering lagged behind.

## Segment 2: the maintainer tax

Every PR carries a hidden bill:

- read the diff
- check whether the issue is real
- test the change
- explain why it is wrong if it is wrong
- deal with the social cost of closing it

AI does not pay that bill. Maintainers do.

And if the PR looks polished, the tax can be higher. A messy PR is easy to reject. A plausible PR wastes your afternoon.

## Segment 3: what platforms will do

This is where pull request limits start to make sense.

Limits sound unfriendly until you look at the incentives. If anyone can generate infinite contribution attempts, maintainers need a way to slow the firehose.

Possible defenses:

- per-user PR limits
- reputation gates
- required issue discussion before code
- bot labeling for AI-assisted PRs
- maintainer-side filters
- stronger project contribution rules

None of these are perfect. All of them make open source feel a little less open. That is the tradeoff.

## Segment 4: what good contributors should do

If you use AI to contribute, the bar should go up, not down.

Before opening the PR:

1. Run the tests.
2. Explain the bug in your own words.
3. Keep the diff small.
4. Say what you used AI for.
5. Be willing to close it yourself if the maintainer says no.

The worst AI PR is not the one with bad code. It is the one where the author does not understand their own diff.

## Result / takeaway

The future is probably not "no AI contributions." That ship has sailed.

The future is proof of care.

Maintainers will trust contributors who show they understand the project, tested the change, and are not just spraying generated diffs across GitHub.

## Wrap

AI can make contribution easier. It can also make maintainership worse.

That is the line to watch.

CTA: If you maintain an open-source project, comment with the rule you wish every AI-assisted contributor followed before opening a PR.

## Shorts cuts

1. "AI makes writing PRs cheap. It does not make reviewing them cheap."
2. "A messy PR is easy to reject. A plausible AI PR can waste your afternoon."
3. "The future of open source might be proof of care."
