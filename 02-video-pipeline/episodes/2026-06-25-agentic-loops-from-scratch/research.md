# Research: Agentic loops from scratch

## Primary thesis

An agentic loop is a bounded control system around an LLM. The model proposes or selects an action, the environment executes it through tools, the result comes back as observation, and the agent decides whether to continue, repair, verify, or stop.

For coding agents, the useful loop is not just "think, act, repeat." It needs:

1. **Goal** — what outcome are we trying to create?
2. **Context** — repo rules, files, constraints, prior state.
3. **Plan** — small ordered steps, with verification targets.
4. **Act** — read files, edit code, run commands, search docs.
5. **Observe** — tool output, tests, compiler errors, diffs.
6. **Verify** — run the exact check that proves the task is done.
7. **Checkpoint** — summarize, commit, hand off, or stop.

## Sources and references

### OpenAI Codex

- OpenAI: "Unrolling the Codex agent loop" — useful framing source for explaining the internal loop of a coding agent.
  - https://openai.com/index/unrolling-the-codex-agent-loop/
- OpenAI Developers: "Custom instructions with AGENTS.md" — establishes `AGENTS.md` as a way to give Codex repo/project norms.
  - https://developers.openai.com/codex/guides/agents-md

### AGENTS.md ecosystem

- AGENTS.md describes itself as a predictable place for coding-agent instructions: setup commands, code style, project conventions, tests.
  - https://agents.md/
- Important angle: `AGENTS.md` is not for humans first. It complements `README.md` with operational instructions agents need.

### Claude Code

- Claude Code docs around hooks and slash commands are useful examples of agent-loop extension points.
  - Hooks: https://code.claude.com/docs/en/hooks
  - Slash commands SDK: https://code.claude.com/docs/en/agent-sdk/slash-commands
- Framing: Claude Code is not only a prompt box. It can be treated as a repo-aware loop with commands, permissions, hooks, and explicit verification prompts.

### OpenCode

- OpenCode agents docs describe markdown-defined agents and modes, useful for showing how to turn the same loop into specialized roles.
  - https://opencode.ai/docs/agents/
- OpenCode GitHub/docs mention custom commands and terminal-based agent workflows.
  - https://github.com/opencode-ai/opencode

## Key teaching points

### Agentic loop from scratch

Minimal loop pseudocode:

```text
state = collect_goal_and_context()
while not done:
    thought = model(state)
    action = choose_tool_or_response(thought)
    observation = run(action)
    state += observation
    if verification_passes(state):
        checkpoint_and_stop()
    if budget_or_safety_limit_hit():
        ask_or_stop()
```

### Why coding agents fail

- vague task
- missing repo rules
- no stop condition
- no test command
- too much stale context
- permissions too broad or too narrow
- no checkpoint after a good state

### What popular tools have in common

| Tool | Loop expression |
|---|---|
| Codex | prompt + repo context + `AGENTS.md` + tool runs + tests |
| Claude Code | project context + slash commands/hooks + permissioned tool use + verification prompts |
| OpenCode | agent markdown files + custom commands + terminal workflow |

## Claims to verify during recording

- Current Codex `AGENTS.md` behavior and file locations.
- Whether Claude Code project guidance file should be `CLAUDE.md` or another project memory/config in the current release.
- Current OpenCode agent/command file locations.
- A simple demo repo can be fixed by all three tools using the same loop prompt.
