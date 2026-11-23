# Round 1 review

## Answers

**Generator 1, C1: PROVEN.** The answer proves exactly $m(H)=n(H)-c(H)$ for acyclic $H$. Checked points:

- The base case $m=0$ is correct.
- The longest path exists and has length at least $1$. Its end vertex has degree $1$: the two cases for a second neighbour (off the path, or $x_j$ with $j\ge 2$) are exhaustive, and the second gives a cycle with at least $3$ vertices.
- $H-v$ is nonempty, acyclic, and has exactly one edge fewer, so the induction hypothesis applies.
- The map on components is well defined, surjective and injective. Injectivity correctly uses that an internal occurrence of $v$ would force $z_{i-1}=z_{i+1}=u$.
- Edge cases $K_1$, $K_2$ and disconnected graphs are covered.

**Generator 2, C2: PROVEN.** The answer proves exactly the stated claim. Checked points:

- The cyclic indexing covers the closing edge ($j=k$).
- $u_0$ and $u_{k-1}$ are the endpoints of $e$.
- No edge of $W$ equals $e$; this is where $k\ge 3$ is used.
- Both traversal directions of $e$ are handled.
- F0 is applied in $H-e$, which has the same nonempty vertex set.

**Generator 3, C3: PROVEN.** The answer proves exactly $m(H)\ge n(H)-1$ for connected $H$. Checked points:

- The first-exit vertex exists, and connectivity is used there.
- The growing sequence extends up to length $n$.
- The edges $f_i$ are distinct, because the larger-index vertex $w_j$ of $f_j$ cannot lie in $\{w_i,w_{p(i)}\}$ when $i<j$.
- For $n=1$ the bound is $m\ge 0$.

No answer cites a forbidden fact. The dependencies are only F0 and induction, so there is no cycle among the claims.

## Proven so far

F0, C1, C2, C3.

## Connection

The theorem follows by the implication cycle (a) ⇒ (b) ⇒ (c) ⇒ (a).

- **(a) ⇒ (b):** $G$ is acyclic and $c(G)=1$, so C1 gives $m=n-1$. Connectedness is part of (a).
- **(b) ⇒ (c):** Suppose $G$ has a cycle $C$ and let $e\in E(C)$. By C2, $G-e$ is connected. It has $n$ vertices and $m-1=n-2$ edges, while C3 requires at least $n-1$ edges, a contradiction. So $G$ is acyclic, and $m=n-1$ is part of (b).
- **(c) ⇒ (a):** C1 gives $n-1=m=n-c(G)$, so $c(G)=1$ and $G$ is connected. Acyclicity is part of (c).

Sanity checks:

- $K_1$ and $P_3$ satisfy all three conditions.
- $C_3$ is connected with $m=n$, so it satisfies none of (a), (b), (c).
- $C_3\sqcup K_1$ has $n=4$, $m=3=n-1$, but is neither connected nor acyclic, so it also satisfies none of them. This shows that $m=n-1$ alone is not sufficient.
- The edgeless graph on two vertices is acyclic with $m=0\ne 1$, and satisfies none of them.

## Open questions

none

## Decision

COMPLETE. All three claims are proven and connect into a full proof of the formal statement, written to `candidate.md` with status `Proven, awaiting independent review`.
