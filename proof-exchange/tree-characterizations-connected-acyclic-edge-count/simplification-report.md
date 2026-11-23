# Simplification report

RESULT: SIMPLIFIED
SIMPLIFIED PROOF: simplified-proof.md

## Errors found in the original

None found.

The checklist was applied to `candidate.md`:

- **Target:** the formal statement matches `problem.md`.
- **Steps:** Fact 0, Lemmas 1 to 3 and all three implications are correct.
- **Hypotheses:** finiteness is used for the extremal choices and the edge count. $n\ge 1$ gives $c(H)\ge 1$. Simplicity is used for the absence of loops and in the edge count.
- **Circularity:** none.
- **Induction:** Lemma 1 reduces from $k$ to $k-1$ edges, and $H-v$ still satisfies the hypotheses (nonempty, acyclic).
- **Cases:** the case distinctions in Lemma 1 Step 1 and Lemma 2 Step 2 are exhaustive.
- **Edge cases:** $n=1$, $m=0$ and disconnected graphs are handled.
- **Equivalence:** the cycle (a) ⇒ (b) ⇒ (c) ⇒ (a) is complete.
- **Sanity checks:** the path $P_3$, the triangle, and the triangle plus an isolated vertex agree with the lemmas. The examples in the Remarks are correct.

## Fixes applied

None.

## Summary

| | Original | Simplified |
|---|---|---|
| Auxiliary claims | Fact 0 and 3 lemmas | Fact 0 and 1 lemma with 2 parts |
| Inductions | 3 (Lemma 1, Lemma 2 Step 3, Lemma 3 Step 1) | none, only a finite count over the insertion steps |
| Approximate length of the "Proof" section | 1,500 words | 650 words |

Word counts are estimates and were not measured by a tool.

The main simplification: insert the edges of $G$ one at a time and count how many merge two components. This gives the single identity $c(G)=n-m+s$, with $s=0$ iff $G$ is acyclic, and all three implications follow from it by arithmetic.

## Changes

1. **Lemma 1 (type: new technique, replaced).** The induction that removes a degree-1 vertex, including the bijection between components, is replaced by part 1 of the new Lemma. The acyclic case is $s=0$. The argument is correct because each insertion changes the component partition by exactly one explicit merge, proved in both directions.
2. **Lemma 2 (type: removed).** The modular-index argument that deleting a cycle edge preserves connectivity is no longer needed. Its role in (b) ⇒ (c) is taken by part 2 of the new Lemma, which uses the cycle edge of largest index.
3. **Lemma 3 (type: removed).** The bound $m\ge n-1$ for connected graphs and the growing-sequence construction are no longer needed. For connected $G$, the bound follows from $1=n-m+s$, since then $m=n-1+s\ge n-1$ because $s\ge 0$, but the proof of the Theorem does not use it.
4. **(b) ⇒ (c) (type: shortened).** The contradiction through $G-e$ is replaced by the direct computation $1=1+s$.
5. **Terminology (type: removed).** The notation $n(H)$, $m(H)$, $H-e$, $H-v$, $\sigma$, $\Phi$ and "growing sequence" is gone. The only new term is "redundant index".
6. **Fact 0 (unchanged).** It is still needed for transitivity of $\sim_H$.

## Techniques tried without improvement

- **Lemma 1, edge deletion instead of insertion:** gives the same identity, but needs a separate statement about cycle edges and bridges, so it is longer.
- **Lemma 1, decomposition into components:** requires the connected acyclic case first and then a summation, so it is longer.
- **(b) ⇒ (a), induction on $n$ via the degree sum:** a connected graph with $n-1$ edges has a degree-1 vertex, but one must then show that removing it preserves connectivity, and (a) ⇒ (b) and (c) ⇒ (a) still need separate arguments.
- **Linear algebra (rank of the incidence matrix over $\mathbb F_2$) or matroid rank:** short only by relying on heavier theory, so it does not count as a simplification.

## Remaining checks

The simplified proof has been checked only by this agent and has not been independently reviewed.
