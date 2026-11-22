# Simplification report

RESULT: SIMPLIFIED
SIMPLIFIED PROOF: simplified-proof.md

## Errors found in the original

No `CRITICAL` issues were found. The formal statement is faithful to `problem.md`, and both directions are proven.

1. **MINOR.** Location: Claim 1, "Deleting repetitions from $p(z_0),\dots,p(z_m)$ therefore gives an $a$–$b$ walk in $H_i$."
   Problem: only *consecutive* repetitions may be deleted. Deleting every repeated value from the sequence need not leave a walk.
   Suggestion: write "Deleting consecutive repetitions". The simplified proof no longer needs this step.

2. **STYLE.** Location: Formal statement, "we write $r$ instead and reserve nothing else for it", and Claim 4, which uses $n$ as a sequence length.
   Problem: the sentence is unclear, and $n$ (the problem's number of parts) is reused with another meaning.
   Suggestion: drop the phrase and use another letter in Claim 4. The simplified proof does both.

## Summary

- **Original:** 5 claims, plus a separate replacement construction and 5 standard facts.
- **Simplified:** 3 claims and 3 standard facts. By estimate (not a measured count), the proof section shrinks from about 2000 words to about 1000.
- **Main simplification:** the swap relation is defined symmetrically, so reversibility needs no proof. The path-rerouting induction is replaced by one invariant: for each $i$, the components of $(V,F'_i\cap\hat E)$ are the same for all tuples $\mathbf F'$ in the swap class.

## Changes

1. **Original Claim 1 (necessity). Type: new technique, shortened.**
   The auxiliary quotient multigraph $H_i$ is replaced by an edge count: at most $\sum_j(|V_j|-1)=|V|-r$ edges of $T_i$ lie inside parts, and $|T_i|=|V|-1$.
   Still correct: the edges of $T_i$ inside the non-empty set $V_j$ form a forest on $V_j$, so (F2) applies.

2. **Replacement definition and original Claim 2. Type: removed, new technique.**
   Tuples of maximum size are called neighbours if they differ by a one-edge swap in one coordinate. Both tuples are required to be packings, so the definition is visibly symmetric, and Claim 2(b) and 2(c) disappear.
   Still correct: the only place where a swap must be shown to produce a forest is Claim 1 of the simplified proof, and it is verified there using (F1) and (F3).

3. **Original Claim 3. Type: shortened.**
   Kept as the new Claim 1, stated directly as "$a,b$ are joined by a path in $(V,F'_l\cap\hat E)$".
   Still correct: the maximality and swap arguments are the same as in the original.

4. **Original Claim 4. Type: new technique.**
   The induction with three cases and walk surgery is replaced by the new Claim 2. For neighbours with swap $e'\to e$, adding $e$ to one graph and adding $e'$ to the other yields the same graph, and neither addition changes components by the new Claim 1.
   Still correct: $e,e'\in\hat E$ because each is unused by one of the two neighbours, and every member of $\mathcal F$ is linked to $\mathbf F$ by a chain inside $\mathcal F$.

5. **Original Claim 5. Type: shortened.**
   The new Claim 3 identifies the components of $(V,F_i\cap\hat E)$ with those of $\hat G$, with no concatenation of paths.

6. **Terminology. Type: terminology, removed.**
   "Admissible tuple" became "packing". The notation $E[\mathbf F]$, $\|\mathbf F\|$, $S[U]$ and the facts (F4), (F5) are no longer needed.

The finished proof was re-checked against the full checklist, and traced by hand on these cases:

- $K_2$ with $k=1$: $\hat E=\emptyset$, $r=2$, one cross edge $=r-c_1$.
- $C_3$ with $k=1$: $\hat E=E$, $r=1$.
- $C_3$ with $k=2$, forests $\{ab,bc\},\{ca\}$: $\hat E=\emptyset$, $r=3$, $c_1=1$, $c_2=2$, so $3$ cross edges $<4=k(r-1)$. Condition (2) fails, as it should.
- Path $a,b,c$ with $ab$ doubled, $k=1$: $\hat E$ is the pair of parallel edges, the parts are $\{a,b\},\{c\}$, and there is one cross edge $=r-c_1$.

## Techniques tried without improvement

- **Sufficiency, closure of a single fixed packing.** Define $\hat E$ as the smallest edge set containing the unused edges and closed under taking forest paths, with no family of tuples. This needs a shortest-augmenting-chain argument to show that endpoints stay connected, which is longer than the swap class.
- **Sufficiency, all maximum packings instead of the swap class.** Taking $\mathcal F$ to be every maximum packing would remove reachability, but the invariant in Claim 2 is proved along swap steps, so the reachability structure is still needed.

## Remaining checks

The simplified proof has been checked only by this agent and has not been independently reviewed.
