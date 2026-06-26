---
target_publish: 2026-07-19
recording_date: 2026-07-05
edit_due: 2026-07-12
thumbnail_due: 2026-07-10
blocked_by: "Need a small demo repo and screen captures from Codex, Claude Code, and OpenCode"
---
# Video project: Agentic loops from scratch

## Working title

**Stop prompting coding agents. Build them a loop.**

## Core promise

Show viewers what an agentic loop actually is, build a tiny one from scratch, then translate that mental model into practical workflows for Codex, Claude Code, and OpenCode.

## Audience

Developers, homelab builders, and technical creators who use AI coding tools but still treat them like chatbots. They know how to ask for code, but they do not yet have a repeatable loop for planning, tool use, verification, context cleanup, and handoff.

## Viewer transformation

Before: "I ask Codex or Claude Code to do things, then I babysit it when it wanders."

After: "I can design a bounded agent loop: goal -> context -> plan -> act -> observe -> verify -> checkpoint, and I know how to express that loop in Codex, Claude Code, and OpenCode."

## Story angle

This is not another "AI coding tools are amazing" video. The story is that the magic is not the model. The magic is the loop around the model. Once the viewer sees the loop, the tools stop feeling mysterious.

## Why now

Coding agents are becoming normal terminal tools. Codex, Claude Code, OpenCode, and AGENTS.md-style project instructions all push in the same direction: agents need more than prompts. They need a repeatable operating loop, project rules, permission boundaries, and verification steps.

## Core beats

1. Show an agent going off track because it only got a vague prompt.
2. Define the agentic loop in plain language.
3. Build a tiny loop from scratch in pseudocode/Python.
4. Convert the loop into repo instructions and task prompts.
5. Show how the same pattern maps to Codex, Claude Code, and OpenCode.
6. End with a checklist viewers can copy into their own `AGENTS.md` or tool-specific config.

## Assets needed

- [ ] Demo repo with a tiny bug or feature task
- [ ] Diagram: agent loop state machine
- [ ] Screen recording: Codex using `AGENTS.md`
- [ ] Screen recording: Claude Code using project context / command workflow
- [ ] Screen recording: OpenCode agents or command workflow
- [ ] Terminal capture of tests passing/failing
- [ ] Thumbnail concept

## Risks / blockers

- Tool UIs and CLI commands may change; verify exact commands at recording time.
- Avoid claiming all tools support the same config format in the same way.
- Keep examples concrete and not hype-driven.

## Repurposing plan

- Short 1: "The 7-step agentic loop in 45 seconds"
- Short 2: "AGENTS.md is a README for coding agents"
- Short 3: "Stop asking agents to code. Ask them to verify."
- Social post: diagram of the loop + one prompt template.
