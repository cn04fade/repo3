---
name: prove-workflow
description: Generate a rigorous proof for a mathematical (mainly graph theory) problem following the project's proof workflow. Use when the user gives a mathematical statement to prove, disprove, or investigate, or types /prove-workflow.
argument-hint: <problem statement>
---

# /prove-workflow — Proof generation workflow

The problem to work on: $ARGUMENTS

If no problem was given, ask the user for it and stop.

## Instructions

Read `workflows/proof-workflow.md` completely before starting, and follow its phases in order. Summary:

1. **Analyse.** Restate the problem formally, fix all definitions and conventions, identify the type of statement, and test small and extreme cases. If a small case contradicts the statement, report the counterexample.
2. **Clarify.** If an important definition, convention or hypothesis is ambiguous, ask the user and **wait for the answer**. Do not guess.
3. **Plan.** Show the user a short attack plan (techniques to try, in order, and candidate lemmas) before working on the proof.
4. **Try techniques.** Use the technique table and lemma list in the workflow document. Check `resources/` for reference material. Keep a short record of each attempt and why it failed.
5. **Write.** Use `workflows/templates/proof-template.md`. Every step must be justified. LaTeX in Markdown.
6. **Review.**
   - Go through the self-review checklist in the workflow document.
   - Then launch the `proof-reviewer` agent. Give it **only** the formal statement, the definitions, and the written proof (not your reasoning). Fix or explicitly rebut every issue it reports. Repeat up to 3 rounds.
7. **Deliver.**
   - Complete proof → save to `outputs/prove-workflow/<descriptive-name>.md` and give a short summary in the chat.
   - No complete proof → save a stuck report to `drafts/prove-workflow/<descriptive-name>-attempt.md` using `workflows/templates/stuck-report-template.md`, and in the chat explain the approaches, the partial results, and exactly where and why it got stuck.
   - Statement false → save the counterexample to `outputs/prove-workflow/<descriptive-name>-counterexample.md`.

File names: lowercase, hyphens instead of spaces, no special characters.

## Non-negotiable rules

- Never present an incomplete or unchecked argument as a proof. Mark every gap with **[GAP]**.
- Never prioritize speed over quality.
- Use precise mathematical language in the proof; explain the main idea in simple language in the chat.
