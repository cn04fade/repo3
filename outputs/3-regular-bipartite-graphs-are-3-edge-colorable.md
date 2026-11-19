# Every 3-regular bipartite graph is 3-edge-colorable

**Status:** Proven
**Date:** 2026-11-19
**Reviewed by:** self-review + proof-reviewer agent (1 round)

## Problem

Every 3 regular bipartite graph is 3 edge colorable.

## Formal statement

Let $G$ be a finite, loopless multigraph that is bipartite and $3$-regular. Then $G$ has a proper $3$-edge-colouring, i.e. there is a map $c : E(G) \to \{1,2,3\}$ such that any two distinct edges with a common endpoint receive different colours.

(We prove the more general statement: for every integer $k \ge 0$, every finite $k$-regular bipartite multigraph has a proper $k$-edge-colouring.)

## Definitions and conventions

- A **multigraph** $G = (V, E)$ consists of a finite vertex set $V$, a finite edge set $E$, and for each edge $e$ a set of two distinct endpoints in $V$. Parallel edges (distinct edges with the same endpoints) are allowed; loops are not. All results hold in particular for simple graphs.
- The **degree** $\deg(v)$ is the number of edges having $v$ as an endpoint. $G$ is **$k$-regular** if $\deg(v) = k$ for all $v \in V$.
- $G$ is **bipartite** with **bipartition** $(A, B)$ if $V = A \cup B$, $A \cap B = \emptyset$, and every edge has exactly one endpoint in $A$ and one in $B$. ($A$ or $B$ may be empty.)
- For $S \subseteq A$, the **neighbourhood** $N(S) \subseteq B$ is the set of vertices joined by at least one edge to a vertex of $S$. We write $N_H(S)$ when the multigraph $H$ must be specified.
- A **matching** is a set of edges, no two of which share an endpoint. A matching **covers** a vertex set $X$ if every vertex of $X$ is an endpoint of an edge of the matching. A **perfect matching** covers $V$.
- A **proper $k$-edge-colouring** is a map $c : E \to \{1, \dots, k\}$ such that $c(e) \ne c(f)$ for any two distinct edges $e, f$ with a common endpoint. (For $k = 0$ this requires $E = \emptyset$, and the empty map is then a proper $0$-edge-colouring.)
- For $M \subseteq E$, $G - M$ denotes the multigraph $(V, E \setminus M)$ (same vertices, edges of $M$ deleted). For $X \subseteq V$, $G[X]$ is the sub-multigraph induced by $X$ (vertex set $X$, all edges with both endpoints in $X$), and $G - X = G[V \setminus X]$.
- The proof is self-contained: Hall's theorem is proven (Lemma 1), not cited.

## Proof idea

In a $k$-regular bipartite graph both sides have the same size, and every set $S$ of vertices on one side has at least $|S|$ neighbours, because the $k|S|$ edges leaving $S$ must all land in $N(S)$, which can absorb only $k|N(S)|$ edges. Hall's theorem then gives a perfect matching. Removing it leaves a $(k-1)$-regular bipartite graph, so by induction the edge set splits into $k$ perfect matchings. Giving each matching its own colour is a proper edge-colouring. For $k = 3$ this is the statement.

## Proof

**Lemma 1 (Hall's theorem).** Let $H$ be a finite bipartite multigraph with bipartition $(A, B)$ such that
$$|N_H(S)| \ge |S| \quad \text{for all } S \subseteq A. \tag{H}$$
Then $H$ has a matching covering $A$.

*Proof of Lemma 1.* Strong induction on $|A|$.

*Base case $|A| = 0$.* The empty matching covers $A = \emptyset$.

*Induction step.* Let $|A| \ge 1$ and assume the lemma holds for all bipartite multigraphs whose first side has fewer than $|A|$ vertices. We distinguish two cases; they are exhaustive because either every nonempty proper subset $S \subsetneq A$ satisfies $|N_H(S)| \ge |S| + 1$, or some nonempty proper subset violates this, in which case by (H) it satisfies $|N_H(S)| = |S|$.

*Case 1: $|N_H(S)| \ge |S| + 1$ for every nonempty $S \subsetneq A$.*
Choose any $a \in A$. By (H) with $S = \{a\}$, $|N_H(\{a\})| \ge 1$, so there is an edge $e$ with endpoints $a$ and some $b \in B$. Let $H' = H - \{a, b\}$, a bipartite multigraph with bipartition $(A \setminus \{a\}, B \setminus \{b\})$. For $S \subseteq A \setminus \{a\}$, deleting the vertices $a$ and $b$ removes from the neighbourhood of $S$ only the vertex $b$ (deleting $a \in A$ does not change which vertices of $B$ are adjacent to $S$), so
$$N_{H'}(S) = N_H(S) \setminus \{b\}.$$
If $S = \emptyset$, then (H) holds trivially for $S$ in $H'$. If $S \ne \emptyset$, then $S$ is a nonempty proper subset of $A$ (as $a \notin S$), so by the case assumption
$$|N_{H'}(S)| \ge |N_H(S)| - 1 \ge |S|.$$
Hence $H'$ satisfies (H). Since $|A \setminus \{a\}| < |A|$, the induction hypothesis gives a matching $M'$ in $H'$ covering $A \setminus \{a\}$. No edge of $M'$ has endpoint $a$ or $b$ (these vertices are not in $H'$), so $M' \cup \{e\}$ is a matching in $H$ covering $A$.

*Case 2: there is a nonempty $S_0 \subsetneq A$ with $|N_H(S_0)| = |S_0|$.*
Let $T_0 = N_H(S_0)$ and define
$$H_1 = H[S_0 \cup T_0], \qquad H_2 = H[(A \setminus S_0) \cup (B \setminus T_0)].$$
Both are bipartite multigraphs, with bipartitions $(S_0, T_0)$ and $(A \setminus S_0, B \setminus T_0)$ respectively.

- *$H_1$ satisfies (H).* For $S \subseteq S_0$ we have $N_H(S) \subseteq N_H(S_0) = T_0$, so every edge of $H$ from $S$ to $N_H(S)$ lies in $H_1$, giving $N_{H_1}(S) = N_H(S)$ and $|N_{H_1}(S)| \ge |S|$ by (H).
- *$H_2$ satisfies (H).* Let $S \subseteq A \setminus S_0$. Then $N_{H_2}(S) = N_H(S) \setminus T_0$. Since $N_H(S \cup S_0) = N_H(S) \cup T_0$ is the disjoint union of $N_H(S) \setminus T_0$ and $T_0$, and $S \cap S_0 = \emptyset$,
$$|N_{H_2}(S)| = |N_H(S \cup S_0)| - |T_0| \ge |S \cup S_0| - |S_0| = |S|,$$
using (H) for $S \cup S_0$ and $|T_0| = |S_0|$.

Since $S_0 \ne \emptyset$ and $S_0 \ne A$, both $|S_0| < |A|$ and $|A \setminus S_0| < |A|$. The induction hypothesis yields a matching $M_1$ in $H_1$ covering $S_0$ and a matching $M_2$ in $H_2$ covering $A \setminus S_0$. The vertex sets of $H_1$ and $H_2$ are disjoint, so no edge of $M_1$ shares an endpoint with an edge of $M_2$. Thus $M_1 \cup M_2$ is a matching in $H$ covering $S_0 \cup (A \setminus S_0) = A$.

This completes the induction. $\square$

**Lemma 2.** Let $k \ge 1$ and let $G$ be a finite $k$-regular bipartite multigraph with bipartition $(A, B)$. Then $|A| = |B|$ and $G$ has a perfect matching.

*Proof of Lemma 2.* Every edge has exactly one endpoint in $A$. Hence counting edges by their endpoint in $A$ gives $|E| = \sum_{a \in A} \deg(a) = k|A|$, and likewise by their endpoint in $B$, $|E| = k|B|$. Since $k \ge 1$, $|A| = |B|$.

We verify (H). Let $S \subseteq A$ and let $E_S$ be the set of edges with an endpoint in $S$. Each edge has exactly one endpoint in $A$, so $|E_S| = \sum_{a \in S} \deg(a) = k|S|$. The endpoint in $B$ of every edge in $E_S$ lies in $N(S)$ by definition, so $E_S$ is contained in the set of edges with an endpoint in $N(S)$, which by the same counting has size $k|N(S)|$. Hence $k|S| \le k|N(S)|$, and since $k \ge 1$, $|S| \le |N(S)|$.

By Lemma 1, $G$ has a matching $M$ covering $A$. Each vertex of $A$ is the endpoint of exactly one edge of $M$ and each edge of $M$ has exactly one endpoint in $A$, so $|M| = |A|$. The $|M|$ edges of $M$ have pairwise distinct endpoints in $B$, so $M$ covers $|A| = |B|$ vertices of $B$, i.e. all of $B$. Thus $M$ is a perfect matching. $\square$

**Lemma 3.** For every integer $k \ge 0$, every finite $k$-regular bipartite multigraph $G$ has a proper $k$-edge-colouring.

*Proof of Lemma 3.* Induction on $k$.

*Base case $k = 0$.* Every vertex has degree $0$, so $E(G) = \emptyset$ and the empty map is a proper $0$-edge-colouring.

*Induction step.* Let $k \ge 1$ and assume the statement for $k - 1$. Let $G$ be $k$-regular bipartite with bipartition $(A, B)$. By Lemma 2, $G$ has a perfect matching $M$. Let $G' = G - M$. Then:

- $G'$ is a loopless bipartite multigraph with the same bipartition $(A, B)$, since its edges are edges of $G$.
- $G'$ is $(k-1)$-regular: $M$ is perfect, so each vertex $v$ is an endpoint of exactly one edge of $M$, hence $\deg_{G'}(v) = k - 1$.

By the induction hypothesis $G'$ has a proper $(k-1)$-edge-colouring $c' : E \setminus M \to \{1, \dots, k-1\}$. Define $c : E \to \{1, \dots, k\}$ by
$$c(e) = \begin{cases} c'(e) & \text{if } e \notin M, \\ k & \text{if } e \in M. \end{cases}$$
Let $e \ne f$ be two edges with a common endpoint. Exactly one of the following holds:

- $e, f \in M$: impossible, because $M$ is a matching.
- exactly one of them lies in $M$: then one has colour $k$ and the other a colour in $\{1, \dots, k-1\}$, so $c(e) \ne c(f)$.
- $e, f \notin M$: then $c(e) = c'(e) \ne c'(f) = c(f)$, because $c'$ is proper and $e, f$ are distinct edges of $G'$ with a common endpoint.

Hence $c$ is a proper $k$-edge-colouring of $G$. $\square$

**Main proof.** Let $G$ be a finite, loopless, bipartite, $3$-regular multigraph. Lemma 3 with $k = 3$ gives a proper $3$-edge-colouring $c : E(G) \to \{1, 2, 3\}$. Hence $G$ is $3$-edge-colourable. $\blacksquare$

## Remarks

- **Tightness.** If $G$ has at least one edge, then $G$ has a vertex with $3$ incident edges, which need $3$ distinct colours. So $\chi'(G) = 3$ exactly.
- **Example.** For $K_{3,3}$ with sides $\{a_0, a_1, a_2\}$ and $\{b_0, b_1, b_2\}$, the colouring $c(a_i b_j) = (i + j) \bmod 3$ is proper; each colour class is one of the three perfect matchings the proof produces.
- **Bipartiteness is necessary.** The Petersen graph is $3$-regular and not bipartite, and it has chromatic index $4$ (a standard fact, not proven here).
- **Regularity can be weakened.** By König's edge-colouring theorem, every bipartite multigraph with maximum degree $\Delta$ has a proper $\Delta$-edge-colouring. This result is not used here.
- **Results used.** Only Hall's theorem, which is proven as Lemma 1. The construction is also an algorithm: repeatedly find a perfect matching and remove it.
