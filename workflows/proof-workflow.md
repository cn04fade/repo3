# Proof Generation Workflow

This document defines how a mathematical problem (mainly graph theory) is turned into a rigorous proof, or into a clear report of where the attempt got stuck.

It is executed by the `/prove` skill (`.claude/skills/prove/SKILL.md`). Quality always has priority over speed.

---

## Phase 1 — Analyse the problem

1. **Restate the problem formally.** Write the statement as precise hypotheses and a conclusion:
   "Let $G$ be ... . Then ... ."
2. **Fix all definitions.** List every notion used and the convention assumed, e.g.
   - Is the graph finite? Simple (no loops, no multi-edges)? Directed? Connected?
   - Does "path" allow repeated vertices? Is $\mathbb{N}$ starting at 0 or 1?
   - Which notation is used ($n = |V(G)|$, $m = |E(G)|$, $\delta(G)$, $\Delta(G)$, ...)?
3. **Identify the type of statement.** Universal ("for all graphs ..."), existential ("there exists ..."), equivalence ("if and only if" — two directions!), extremal bound ("at most / at least"), or construction.
4. **Test small cases.** Check the statement by hand on small or extreme examples: the empty graph, $K_1$, $K_2$, paths $P_n$, cycles $C_n$, complete graphs $K_n$, stars, trees, complete bipartite graphs $K_{a,b}$, the Petersen graph.
   - If a small case **contradicts** the statement, stop: the statement is false or a hypothesis is missing. Report the counterexample.
   - If an inequality is claimed, check whether it is **tight** (which graphs achieve equality?). Tight examples often show which proof idea is needed.

## Phase 2 — Clarify

If any of the following is unclear, **stop and ask the user** before continuing:

- a definition or convention that changes the meaning of the statement,
- a hypothesis that seems to be missing (found by a counterexample in Phase 1),
- whether known theorems may be cited or must be proven from scratch,
- the expected level of detail.

Do not guess. State the ambiguity and propose the most likely interpretation.

## Phase 3 — Plan

Write a short attack plan (3–6 lines): which techniques look most promising and why, in which order they will be tried, and which lemmas might help.

## Phase 4 — Try proof techniques

Work through the techniques that fit the problem. Record each attempt briefly (what was tried, whether it worked, and if not, **why** it failed); this record is needed for the stuck report.

### General techniques

| Technique | When it tends to work |
|---|---|
| Direct proof | Conclusion follows by a chain of definitions and known facts. |
| Contraposition | "$P \Rightarrow Q$" is hard, but "$\neg Q \Rightarrow \neg P$" gives more structure to work with. |
| Contradiction | Assuming the negation produces a concrete object (a cycle, a vertex of high degree, ...) to argue about. |
| Induction | Statement is about all $n$ or all $m$. Induct on vertices, edges, or use strong induction. **Remove** a vertex/edge from a graph of size $n+1$; do not "build up" from size $n$ (this is a common error). |
| Minimal counterexample | Take a smallest counterexample and show a smaller one exists. Equivalent to induction, often cleaner. |
| Extremal principle | Consider a longest path, a maximum matching, a vertex of maximum/minimum degree, a spanning tree, etc. Its maximality gives information. |
| Pigeonhole principle | Many objects, few categories (e.g. degrees $0,\dots,n-1$). |
| Double counting | Count one set in two ways (e.g. pairs (vertex, incident edge)). |
| Construction | Existential statements: build the object explicitly and verify it. |
| Case distinction | Finitely many structurally different situations. Make sure the cases are exhaustive. |
| Probabilistic method | Existence of objects with a property; show the probability is positive. |
| Parity arguments | Statements about odd/even counts. |

### Useful graph theory lemmas and theorems

Check whether one of these applies (cite them with their standard name; prove them only if the user asked for a self-contained proof):

- **Handshake lemma:** $\sum_{v} \deg(v) = 2m$; hence the number of odd-degree vertices is even.
- **Trees:** a tree on $n$ vertices has $n-1$ edges; any two vertices are joined by a unique path; every tree with $n \ge 2$ has at least two leaves; a connected graph has a spanning tree.
- **Connectivity:** a connected graph on $n$ vertices has at least $n-1$ edges; removing an edge on a cycle keeps a graph connected.
- **Bipartite graphs:** $G$ is bipartite iff it contains no odd cycle.
- **Euler:** a connected graph has an Eulerian circuit iff all degrees are even.
- **Planar graphs:** Euler's formula $n - m + f = 2$ (connected); $m \le 3n - 6$ for $n \ge 3$; $m \le 2n - 4$ if also triangle-free; Kuratowski / Wagner.
- **Matchings:** Hall's marriage theorem; König's theorem (bipartite: max matching = min vertex cover); Tutte's theorem; Berge's lemma (augmenting paths).
- **Connectivity (advanced):** Menger's theorem; Whitney ($\kappa \le \lambda \le \delta$).
- **Colouring:** greedy bound $\chi \le \Delta + 1$; Brooks' theorem; $\chi(G) \ge \omega(G)$; $\chi(G) \ge n / \alpha(G)$.
- **Hamiltonicity:** Dirac ($\delta \ge n/2$), Ore ($\deg u + \deg v \ge n$ for non-adjacent $u, v$).
- **Extremal:** Mantel / Turán; Ramsey numbers, e.g. $R(3,3) = 6$.

### Where to look for help

- `resources/` may contain reference material provided by the user. Check it first.
- If no technique works after an honest effort, try to prove a **weaker** version (special case, extra hypothesis, weaker bound). Partial results are valuable.

## Phase 5 — Write the proof

Use `workflows/templates/proof-template.md`. Rules:

- Every step has a justification (definition, hypothesis, earlier step, or named lemma).
- Split long proofs into claims/lemmas, each with its own proof.
- In an induction, state base case, induction hypothesis, and induction step explicitly.
- In a case distinction, state why the cases are exhaustive.
- In a proof by contradiction, state clearly what is assumed and where the contradiction occurs.
- Use LaTeX inside Markdown: inline `$...$`, display `$$...$$`.
- End proofs with $\blacksquare$.

## Phase 6 — Review

### Self-review checklist

- [ ] The proven statement is exactly the stated problem (not a weaker or different one).
- [ ] Every hypothesis is used. (If one is not, either the proof is wrong or the hypothesis is unnecessary — say which.)
- [ ] No circular reasoning: the conclusion is not assumed anywhere.
- [ ] Induction: the base case is correct, and the step works for **all** sizes, including the smallest one after the base case.
- [ ] Case distinctions are exhaustive.
- [ ] Edge cases are handled (empty graph, single vertex, disconnected graphs, $n$ small).
- [ ] "Without loss of generality" is justified each time it is used.
- [ ] Cited theorems are applied with their hypotheses satisfied.
- [ ] Both directions are proven for an "if and only if".
- [ ] The proof is checked once more on a concrete small example.

### Independent review

After the self-review, the `proof-reviewer` agent (`.claude/agents/proof-reviewer.md`) reads **only** the problem statement and the written proof, without the reasoning that produced it, and reports gaps. Every issue it reports must be fixed or explicitly rebutted. Repeat until the reviewer reports no critical issues (at most 3 rounds; if issues remain, the result is treated as incomplete).

## Phase 7 — Deliver

**If a complete proof was found:**

- Save it as `outputs/<descriptive-name>.md` (lowercase, hyphens, no special characters), e.g. `outputs/trees-have-two-leaves.md`.
- In the chat, give a short summary: the main idea and the file path.

**If no complete proof was found:**

- Save a stuck report as `drafts/<descriptive-name>-attempt.md` using `workflows/templates/stuck-report-template.md`.
- In the chat, give an overview: the approaches tried, the partial results obtained, and **exactly** which step fails and why.
- Never present an incomplete proof as complete. Mark every gap clearly with **[GAP]**.

**If the statement turned out to be false:**

- Save the counterexample with its verification as `outputs/<descriptive-name>-counterexample.md`, and suggest a corrected statement if one is apparent.
