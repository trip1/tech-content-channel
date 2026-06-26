# Block script: Stop prompting coding agents. Build them a loop.

## Format notes

- Target length: 10-12 minutes
- Style: practical, skeptical, build-in-public
- Goal: teach the mental model first, then show how it maps to real tools
- Avoid: AI hype, fake autonomy, vague productivity claims

## Open loops to maintain

1. Why do coding agents wander?
2. What is the smallest useful agentic loop?
3. How do Codex, Claude Code, and OpenCode each express the same loop?

---

## Block 1: cold open — the problem is not the prompt

**Time:** 0:00-0:35

**On screen**

- Split screen:
  - left: vague prompt, messy agent changes
  - right: loop diagram ending in tests passing
- Quick flashes: `AGENTS.md`, terminal test output, a git diff

**Voiceover / talking head**

If your coding agent keeps wandering, the problem probably is not the model.

It is the loop you put around it.

A vague prompt like "fix this app" gives the agent permission to guess. A real loop gives it a job, a map, tools, a way to check itself, and a stop condition.

So in this video, I am going to build the simplest useful agentic loop from scratch, then show how I would translate that loop into Codex, Claude Code, and OpenCode.

Not as a toy demo. As a workflow you can actually copy into a real repo.

**Retention beat**

Cut from the phrase "permission to guess" to a messy diff, then hard cut to a green test result.

---

## Block 2: define the loop without mysticism

**Time:** 0:35-1:45

**On screen**

- Diagram animating one node at a time:
  - Goal
  - Context
  - Plan
  - Act
  - Observe
  - Verify
  - Checkpoint

**Voiceover / talking head**

The word agentic gets used like it means magic.

For coding work, I think it means something much more boring and much more useful.

An agentic loop is a repeatable cycle where the model can look at the current state, choose an action, run a tool, read the result, and decide what to do next.

That is it.

The useful version has seven pieces.

First: the goal. What should be true when we are done?

Second: context. What files, rules, constraints, and project conventions matter?

Third: a plan. Not a novel. Just the next few safe steps.

Fourth: action. Read a file. Edit a file. Run a command. Search docs.

Fifth: observation. The tool output comes back into the loop.

Sixth: verification. Tests, builds, type checks, screenshots, curl output — whatever proves the work.

Seventh: checkpoint. Commit, summarize, hand off, or stop.

The reason most agent sessions feel chaotic is that one of these pieces is missing.

---

## Block 3: build the smallest loop from scratch

**Time:** 1:45-3:10

**On screen**

- Editor with pseudocode or a tiny Python loop
- Highlight state, tool call, observation, verification

**Voiceover / talking head**

Here is the smallest version of the loop.

```python
state = {
    "goal": "fix the failing test",
    "context": read_project_rules(),
    "observations": [],
}

while True:
    next_step = model(state)
    result = run_tool(next_step)
    state["observations"].append(result)

    if verification_passed(state):
        checkpoint(state)
        break

    if out_of_budget_or_unclear(state):
        ask_for_help_or_stop(state)
        break
```

This is not production agent code. It is the shape.

The important part is not the while loop. The important part is that every turn changes state, and every action has to eventually face verification.

If the agent edits code but never runs the test, the loop is incomplete.

If it runs the test but ignores the failure, the loop is broken.

If it passes the test but keeps refactoring for fun, there is no stop condition.

That is the mental model I want in your head before we talk about tools.

---

## Block 4: the repo contract — AGENTS.md

**Time:** 3:10-4:30

**On screen**

- `AGENTS.md` file in a repo root
- Sections appearing one by one

```markdown
# AGENTS.md

## Goal of this repo
Explain what the project does.

## Setup
- Install: `pnpm install`
- Run tests: `pnpm test`

## Rules
- Do not edit generated files.
- Keep changes small.
- Run tests before final response.

## Done means
- Tests pass.
- Diff is focused.
- User-facing behavior is verified.
```

**Voiceover / talking head**

This is where `AGENTS.md` matters.

A README is usually written for humans. It explains what the project is and how to get started.

An agent file is different. It tells the agent how to behave inside the loop.

What commands are safe? What files are generated? What does done mean? What test proves the task? What should the agent avoid touching?

This is the difference between giving an agent a prompt and giving it an operating manual.

For Codex, `AGENTS.md` is directly part of the workflow. For other tools, the exact file name or config may differ, but the idea is portable: make the project rules explicit and local to the repo.

---

## Block 5: Codex — make the loop explicit

**Time:** 4:30-5:45

**On screen**

- Codex terminal session
- Repo root with `AGENTS.md`
- Prompt template

**Prompt on screen**

```text
Goal: fix the failing dashboard test.
Loop:
1. Read AGENTS.md and the failing test.
2. Explain the smallest plan.
3. Make the smallest code change.
4. Run the targeted test.
5. If it fails, use the output to repair once.
6. Stop when the test passes and summarize the diff.
Do not refactor unrelated files.
```

**Voiceover / talking head**

With Codex, I want the repo instructions and the task prompt to work together.

`AGENTS.md` carries the durable rules: setup, test commands, conventions, and what not to touch.

The prompt carries the temporary goal: this bug, this feature, this verification command.

The mistake is asking Codex for a final answer before you have told it what loop to run.

I like prompts that literally name the loop. Read. Plan. Change. Test. Repair. Stop.

That sounds boring, but boring is good. Boring is how you get a diff you can review.

---

## Block 6: Claude Code — commands, hooks, and guardrails

**Time:** 5:45-7:05

**On screen**

- Claude Code session
- Project instructions file / command examples
- Hook concept diagram: before tool -> after tool -> stop/continue

**Voiceover / talking head**

Claude Code is useful to explain because it makes the loop feel interactive.

You can run natural language tasks, but you can also build repeatable command patterns: review this file, implement this plan, run this check, summarize this diff.

Hooks and commands are powerful because they let you shape what happens around the model.

A pre-tool hook can remind the system about dangerous commands.

A post-tool hook can collect output.

A slash command can package a repeatable workflow so you are not inventing your process every time.

So the Claude Code version of the loop is not "Claude, please code." It is closer to:

```text
Use the project rules.
Inspect before editing.
Make one focused change.
Run the verification command.
Report the exact result.
Stop.
```

That last word matters.

Stop.

A coding agent that does not know when to stop will happily turn a one-file fix into a new architecture.

---

## Block 7: OpenCode — specialized agents without losing the loop

**Time:** 7:05-8:25

**On screen**

- OpenCode docs or local config
- Example markdown agent roles:
  - `review.md`
  - `builder.md`
  - `tester.md`

**Voiceover / talking head**

OpenCode is a good place to talk about specialized agents.

Instead of one giant assistant trying to be everything, you can define narrower roles.

A review agent can inspect the diff without changing files.

A build agent can make the change.

A tester agent can focus on verification and failure output.

But specialization does not replace the loop. It just splits the loop across roles.

The same rules apply.

Each agent needs a goal. Each agent needs boundaries. Each agent needs a stop condition.

If you make a review agent, tell it not to edit.

If you make a build agent, tell it exactly what verification command must pass.

If you make a tester agent, tell it to return failure evidence, not guesses.

That is how you get useful multi-agent work instead of three chatbots arguing in parallel.

---

## Block 8: the copy-paste agent loop template

**Time:** 8:25-9:45

**On screen**

- Full-screen template viewers can pause and copy

```markdown
## Agent loop for this task

Goal:
- [one sentence outcome]

Context:
- Read: [files/docs]
- Constraints: [do not touch / must preserve]

Plan:
- Give a short plan before editing.

Act:
- Make the smallest useful change.
- Prefer existing project patterns.

Verify:
- Run: [exact command]
- If it fails, use the output to repair.

Stop:
- Stop after verification passes.
- Summarize changed files and real test output.
```

**Voiceover / talking head**

This is the template I would actually copy.

The most important line is the verification command.

If you cannot name the command, screenshot, curl request, or manual check that proves the task is done, the agent cannot reliably know when it is done either.

And if the agent cannot know when it is done, it is not really working autonomously. It is just continuing.

---

## Block 9: what not to automate

**Time:** 9:45-10:45

**On screen**

- Red flags checklist

**Voiceover / talking head**

There are a few places I would slow down.

Do not let an agent rewrite auth, payments, migrations, or deployment scripts without a tight plan and real review.

Do not let it run destructive commands just because it sounds confident.

Do not let it hide failing tests under "probably unrelated."

And do not let it replace your judgment.

The loop is not there to make the agent independent of you. The loop is there to make the agent's work inspectable.

That is the standard I care about: can I review what happened, reproduce the check, and trust the boundary?

---

## Block 10: wrap — the model is not the workflow

**Time:** 10:45-11:30

**On screen**

- Final diagram with all three tools mapped to the same loop

| Loop piece | Codex | Claude Code | OpenCode |
|---|---|---|---|
| Context | AGENTS.md | project instructions | agent/command docs |
| Action | tool calls | tool calls/hooks | build agents |
| Verify | tests/commands | slash workflows | tester/reviewer agents |
| Stop | final summary | final summary | role handoff |

**Voiceover / talking head**

The tool names will change.

The loop is the part worth learning.

Goal. Context. Plan. Act. Observe. Verify. Checkpoint.

If you can write that loop clearly, Codex gets better. Claude Code gets better. OpenCode gets better. And honestly, your own engineering process gets better too.

If you want the follow-up, I will build a real starter repo with `AGENTS.md`, Claude Code commands, and OpenCode agents wired around the same loop.

Comment `loop` if you want that build.
