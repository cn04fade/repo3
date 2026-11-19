# CLAUDE.md

This file provides guidence to Claude Code when working in this repository.

# Project Context

This workspace is used for AI-assisted proof generation in the field of graph theory. The primarly focus is to approach problems and create meaningfull results that are mathematically rigerous.

# About Me

I am a student currently working on a groub project that focuses on AI-assisted problem solving. I am still in the process of figuring out how AI Agents and Tools work.

# Comunication Style

- write clear English
- Use simple language for a casual answer
- Use precise and mathematically correct language to answer a stated problem
- Explain concepts as if speaking to an intelligent beginner

# Rules

- Never make assumptions if important information is missing, ask befor starting the task
- Stay in with requested formats
- Do not add filler content, work on the task you are supposed to
- Review outputs before final delivery

# Core Workflow Rules

- **Always present a written plan and wait for approval befor beginning any multi-step task.**
# File Naming Rules

- Use descriptive names
- Use lowercase file names
- Avoid special characters
- Use hyphens instead of spaces

# Folder Structure

/workflows
Contain workflow instructions, agent definitions and process documents

/outputs
Contains completed work, generated proofs and proof approaches

/resources
Contain reference material, source documents and examples

/drafts
Contain work in progress and temporary files

/pdfs
Contain PDF exports of proofs and proof attempts

# Agent Behavior

If you are given a mathematical problem, work in the following steps:

1. Analyse the stated problem and understand the objective
2. Ask clarification questions if needed
3. Create a plan
4. try different types of proof techniques, for example direct proof, proof by contradiction, contraposition
5. try to use related lemmas
6. If you find a proof try to structure it as clear as possible, If not give all the partial results as an output and mark the parts where you failed to continue
7. Review the output
8. Deliver the final result as a file in the outputs folder

Never prioritize speed over quality.

# Proof Workflow

- The full process is defined in `workflows/proof-workflow.md`; output templates are in `workflows/templates/`.
- Start it with `/prove-workflow <problem>` (skill in `.claude/skills/prove-workflow/`). Also follow it when a problem is given without the command.
- Finished proofs are checked by the `proof-reviewer` agent (`.claude/agents/proof-reviewer.md`) before delivery.
- Complete proofs go to `outputs/`; incomplete attempts (stuck reports) go to `drafts/` and are also summarised in the chat.
- Write math in Markdown with LaTeX (`$...$`, `$$...$$`).
