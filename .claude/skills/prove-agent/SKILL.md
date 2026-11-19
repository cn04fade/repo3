---
name: prove-agent
description: Generate a rigorous proof for a mathematical (mainly graph theory) problem by delegating the proof work to the proof-generator agent and the checking to the proof-reviewer agent, which exchange their work in proof-exchange/. Use when the user types /prove-agent.
argument-hint: <problem statement>
---

# /prove-agent — Proof generation with agents

The problem to work on: $ARGUMENTS

If no problem was given, ask the user for it and stop.

## Overview

This skill follows the same process as `workflows/proof-workflow.md`, but the work is split between two agents. You (the main session) coordinate them and talk to the user:

- `proof-generator` (`.claude/agents/proof-generator.md`) analyses the problem, tries techniques and writes the proof or stuck report.
- `proof-reviewer` (`.claude/agents/proof-reviewer.md`) independently checks a written proof.

Agents cannot talk to the user while they run, and they cannot start other agents. So the clarification questions and the hand-off between the two agents go through you.

## The meeting place: proof-exchange/

Both agents can only work inside `proof-exchange/` (a hook enforces this; the generator may also read `workflows/` and `resources/`). Each problem gets its own folder:

```
proof-exchange/<problem-name>/
  problem.md            ← you:             the problem + the user's clarification answers
  candidate.md          ← proof-generator: proof, counterexample or stuck report
  generator-report.md   ← proof-generator: status, plan, attempts, rebuttals
  review-round-<n>.md   ← proof-reviewer:  issues + verdict for round n
```

The agents never write to `outputs/` or `drafts/`. Only you copy the final result there.

## Instructions

1. **Set up.** Choose a descriptive `<problem-name>` (lowercase, hyphens, no special characters). If `proof-exchange/<problem-name>/` already exists, append `-2`, `-3`, .... Create the folder and write `problem.md` with a heading `## Problem` containing the problem exactly as the user gave it.

2. **Generate.** Launch `proof-generator` in **Mode A** with the path of the problem folder. Then read `generator-report.md`.

3. **Clarify.** If the status is `NEEDS_CLARIFICATION`, show the user the questions and the suggested interpretations, and **wait for the answers**. Do not guess. Add a section `## Clarifications` with the user's answers to `problem.md`, then launch `proof-generator` in Mode A again.

4. **Review** (for status `PROVEN` or `COUNTEREXAMPLE`).
   - Launch `proof-reviewer` with the problem folder path and the round number `<n>` (starting at 1). Pass nothing else: no plan, attempts or reasoning from the generator.
   - Read `review-round-<n>.md`. If the verdict is `VERDICT: REJECT`, launch `proof-generator` in **Mode B** with the folder path and the name of the review file. Then review again with round `<n+1>`.
   - At most 3 review rounds in total.

5. **Deliver.** Copy `candidate.md` to its final place; use the `SUGGESTED FILE NAME` from `generator-report.md` as `<name>`. Keep the problem folder in `proof-exchange/` as the record of how the result was reached.
   - **Accepted proof:** copy to `outputs/<name>.md`. In the copy, set **Status:** `Proven` and **Reviewed by:** `self-review + proof-reviewer agent (<number> rounds)`.
   - **Accepted counterexample:** copy to `outputs/<name>-counterexample.md` in the same way.
   - **Still rejected after 3 rounds:** the result is incomplete. Copy to `drafts/<name>-attempt.md`, set **Status:** `Incomplete`, and add a section "Open review issues" listing each remaining critical issue, marked **[GAP]**.
   - **Status `INCOMPLETE` from the generator:** copy the stuck report to `drafts/<name>-attempt.md`.
   - Add a line `**Working folder:** proof-exchange/<problem-name>/` below the status line of the copy.

6. **Report to the user** in simple language:
   - the result and the file path,
   - the main idea,
   - the attack plan and the techniques tried,
   - the number of review rounds and any rebuttals the generator made,
   - if incomplete: the partial results and exactly where and why it got stuck.

File names: lowercase, hyphens instead of spaces, no special characters.

## Non-negotiable rules

- Never present an incomplete or unchecked argument as a proof. Nothing goes to `outputs/` without `VERDICT: ACCEPT` from `proof-reviewer`.
- Check the files yourself before reporting; an agent's report is not proof that the file is correct.
- Never prioritize speed over quality.
