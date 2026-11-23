---
name: prove-parallel
description: Generate a rigorous proof for a mathematical (mainly graph theory) problem with a proof-supervisor that splits it into claims, up to 3 parallel proof-generator agents, at most 5 rounds, a final proof-reviewer check and a proof-simplifier pass. Use when the user types /prove-parallel.
argument-hint: <problem statement>
---

# /prove-parallel — Parallel proof generation

The problem to work on: $ARGUMENTS

If no problem was given, ask the user for it and stop.

## Overview

You (the main session) coordinate the agents and talk to the user. Agents cannot talk to the user or start other agents, so every hand-off goes through you.

- `proof-supervisor` splits the problem into claims, checks the answers and connects them into one proof.
- `proof-generator` (Mode C) works on one claim. At most 3 run at the same time.
- `proof-reviewer` independently checks the assembled proof.
- `proof-simplifier` improves the final result.

All work happens in one folder:

```
proof-exchange/<problem-name>/
  problem.md                       you
  proven-claims.md                 supervisor
  round-<n>/
    claims.md                      supervisor
    generator-1.md ... -3.md       one generator each
    supervisor-review.md           supervisor
  candidate.md                     supervisor: final proof or stuck report
  review-round-<n>.md              proof-reviewer
  simplified-proof.md              simplifier (accepted proof)
  simplified-partial-results.md    simplifier (failed proof)
  simplification-report.md         simplifier
```

Agents never write to `outputs/` or `drafts/`. Only you copy the final result there.

## Instructions

### 1. Set up

Choose a descriptive `<problem-name>` (lowercase, hyphens, no special characters) that is not yet used in `proof-exchange/`, `outputs/` or `drafts/`; if needed, append `-2`, `-3`, .... Create the folder and `round-1/`. Write `problem.md` with a heading `## Problem` containing the problem exactly as the user gave it.

### 2. Plan

Launch `proof-supervisor` with the folder path, `Task: PLAN`, `Round: 1`.

- `NEEDS_CLARIFICATION`: show the user the questions and suggested interpretations, and **wait for the answers**. Do not guess. Add them to `problem.md` under `## Clarifications`, then launch the PLAN task again.
- `COUNTEREXAMPLE`: go to step 5.
- `CLAIMS_READY`: go to step 3 with $n=1$.

### 3. Run round n (n ≤ 5)

1. Read `round-<n>/claims.md` and count its assignments $g$. If $g$ is 0 or greater than 3, send it back to the supervisor to correct; never run more than 3 generators.
2. Record a checksum of all files in the problem folder, stored in your scratchpad:
   `find <folder> -type f -exec sha256sum {} +`
3. Launch $g$ `proof-generator` agents **in one message**, so that they run in parallel. Prompt for generator `<s>`:

   ```
   Mode C: single claim.
   Problem folder: <folder>
   Round: <n>
   Generator number: <s>
   Write only to round-<n>/generator-<s>.md.
   ```

   Pass no other generator's work and no reasoning of your own.
4. Wait until **all** generators have finished.
5. **Check file ownership.** Compare the folder with your checksum. The only change allowed is the creation of the assigned `generator-<s>.md` files.
   - If an assigned file is missing, launch that generator once more. If it is still missing, tell the supervisor that this generator gave no answer.
   - If any other file was created or changed, stop and tell the user what changed. Do not continue until they decide.

### 4. Collect and decide

Launch `proof-supervisor` with the folder path, `Task: COLLECT`, `Round: <n>`. Do not create `round-<n+1>/` yourself: it appears only if the supervisor writes `round-<n+1>/claims.md`.

- `CONTINUE`: set $n \leftarrow n+1$ and go to step 3.
- `COMPLETE` or `COUNTEREXAMPLE`: go to step 5.
- `FAILED`: go to step 6.

If the supervisor returns `CONTINUE` in round 5, treat this as an error and send it back: round 5 must end with `COMPLETE`, `COUNTEREXAMPLE` or `FAILED`.

### 5. Independent review

Launch `proof-reviewer` with the folder path and review round number `<n>` (the current round). Pass nothing else.

- `VERDICT: ACCEPT`: go to step 6 as **accepted**.
- `VERDICT: REJECT`: launch `proof-supervisor` with `Task: REVIEW_FEEDBACK`, `Round: <n>`.
  - `CONTINUE`: set $n \leftarrow n+1$ and go to step 3.
  - `FAILED`: go to step 6 as **failed**.

Rounds used for review feedback count toward the limit of 5.

### 6. Simplify

- **Accepted:** launch `proof-simplifier` with the folder path, in its normal mode.
- **Failed:** launch `proof-simplifier` with the folder path and the words `Use partial-results mode.`

Read `simplification-report.md` (use the highest number if there are several) and the file it names.

If the simplifier reports `ORIGINAL_HAS_CRITICAL_ERROR` for an **accepted** proof, do **not** deliver it to `outputs/`. Treat it as failed in step 7 and tell the user that the reviewer and the simplifier disagree, quoting the issue. Do not start another round.

### 7. Deliver

Use `<name>` = the supervisor's `SUGGESTED FILE NAME`, or `<problem-name>` if that name is already taken. Never overwrite an existing file. In every copy, add below the status line: `**Working folder:** proof-exchange/<problem-name>/`.

| Result | Copy | To |
|---|---|---|
| Accepted proof | `candidate.md` | `outputs/<name>.md`, with **Status:** `Proven` and **Reviewed by:** `proof-supervisor + proof-reviewer agent` |
| Accepted counterexample | `candidate.md` | `outputs/<name>-counterexample.md`, with the same status fields |
| Its simplified version, if one was written | `simplified-proof.md` | `outputs/<name>-simplified.md` or `outputs/<name>-counterexample-simplified.md` |
| Failed | `candidate.md` | `drafts/<name>-attempt.md` |
| Its simplified partial results, if written | `simplified-partial-results.md` | `drafts/<name>-attempt-simplified.md` |

A simplified file keeps its status "not independently reviewed". Set its `**Based on:**` line to the path of the copied original.

If an accepted proof was treated as failed in step 6, deliver `candidate.md` to `drafts/<name>-attempt.md` with **Status:** `Incomplete` and add a section "Open review issues" with the simplifier's critical issue, marked **[GAP]**.

### 8. Report to the user

In simple language:

- the result and the file paths,
- the main idea,
- the number of rounds and what each round achieved,
- the reviewer's verdict and what the simplifier changed,
- if failed: the proven claims, and exactly where and why it got stuck.

File names: lowercase, hyphens instead of spaces, no special characters.

## Non-negotiable rules

- Never run more than 3 generators at once or more than 5 rounds.
- Each generator writes only to its own file.
- Nothing goes to `outputs/` without acceptance by both `proof-supervisor` and `proof-reviewer`, except the simplified copy of such a proof, which is labelled as not independently reviewed.
- Never present an incomplete or unchecked argument as a proof.
- Check the files yourself before reporting; an agent's report is not proof that a file is correct.
- Never prioritize speed over quality.
