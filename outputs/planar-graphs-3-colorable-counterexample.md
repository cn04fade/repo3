# Not every planar graph is 3-colorable

**Status:** Disproven (counterexample)
**Date:** 2026-11-19
**Reviewed by:** self-review + proof-reviewer agent (1 round)

## Problem

Every planar graph is 3 colorable.

## Formal statement (claimed)

For every finite simple planar graph $G$ there is a map $c : V(G) \to \{1, 2, 3\}$ such that $c(u) \ne c(v)$ for every edge $uv \in E(G)$.

**This statement is false.** We show that the complete graph $K_4$ is planar but has no proper $3$-colouring.

## Definitions and conventions

- Graphs are finite and simple (no loops, no parallel edges).
- A **proper $k$-colouring** of $G$ is a map $c : V(G) \to \{1, \dots, k\}$ with $c(u) \ne c(v)$ for every edge $uv$. $G$ is **$k$-colourable** if it has one. The **chromatic number** $\chi(G)$ is the least such $k$.
- $G$ is **planar** if it has a **plane drawing**. This means the vertices are mapped to distinct points of $\mathbb{R}^2$, and each edge $uv$ is drawn as a simple curve between the points of $u$ and $v$. Two edge-curves may meet only at a common endpoint, and no curve passes through a vertex point other than its own endpoints. Straight-line segments are allowed as curves.
- $K_4$ is the graph with vertex set $\{v_1, v_2, v_3, v_4\}$ and all $\binom{4}{2} = 6$ edges $v_i v_j$ ($i \ne j$).

## Counterexample

**Claim 1.** $K_4$ is planar.

*Proof of Claim 1.* Place the vertices at
$$v_1 = (0,0), \quad v_2 = (4,0), \quad v_3 = (2,4), \quad v_4 = (2,1),$$
and draw every edge as the straight segment between its endpoints. The points $v_1, v_2, v_3$ are not collinear, since $v_3$ has $y$-coordinate $4 \ne 0$ and so does not lie on the line $y = 0$ through $v_1, v_2$. Let $T$ be the closed triangle with corners $v_1, v_2, v_3$. $T$ is convex and its boundary $\partial T$ is the union of the three segments $v_1v_2$, $v_2v_3$, $v_1v_3$.

*$v_4$ lies in the interior of $T$.* The triangle is bounded by the lines $y = 0$, $y = 2x$ (through $v_1, v_3$) and $y = 8 - 2x$ (through $v_2, v_3$). Its interior is $\{(x,y) : y > 0,\ y < 2x,\ y < 8 - 2x\}$. For $(2,1)$ we have $1 > 0$, $1 < 4$ and $1 < 4$.

We check every pair of the six edges.

1. *Two boundary edges* (e.g. $v_1v_2$ and $v_2v_3$): two sides of a non-degenerate triangle meet only in their common corner, which is a common endpoint.
2. *An inner edge $v_4v_i$ ($i \in \{1,2,3\}$) and a boundary edge.* Every point of $v_4v_i$ other than $v_i$ has the form $p = (1-t)v_4 + t v_i$ with $0 \le t < 1$. Since $v_4$ is an interior point of the convex set $T$ and $v_i \in T$, such a $p$ is an interior point of $T$. (A small disc of radius $r$ around $v_4$ lies in $T$. The disc of radius $(1-t)r > 0$ around $p$ is its image under the map $x \mapsto (1-t)x + t v_i$, which maps $T$ into $T$ by convexity.) So $v_4v_i$ meets $\partial T$ only at $v_i$. If the boundary edge contains $v_i$, this is a common endpoint. Otherwise the boundary edge is the side opposite $v_i$, which does not contain $v_i$, and the two segments are disjoint.
3. *Two inner edges $v_4v_i$ and $v_4v_j$ ($i \ne j$).* The point $v_4$ is not on the line through $v_i$ and $v_j$, because that line contains a side of $T$ and $v_4$ is interior. So the vectors $v_i - v_4$ and $v_j - v_4$ are not parallel. The segments lie on two different lines through $v_4$, which meet only at $v_4$, a common endpoint.

Finally, no segment passes through a vertex other than its endpoints. The four points are pairwise distinct and no three of them are collinear: $v_1, v_2, v_3$ are the corners of a non-degenerate triangle, and $v_4$ is not on any line through two corners (same argument as in 3). So this is a plane drawing and $K_4$ is planar. $\square$

**Claim 2.** $K_4$ is not $3$-colourable.

*Proof of Claim 2.* Suppose $c : \{v_1, v_2, v_3, v_4\} \to \{1,2,3\}$ is any map. Four vertices and three colours give, by the pigeonhole principle, $i \ne j$ with $c(v_i) = c(v_j)$. In $K_4$ every two distinct vertices are adjacent, so $v_iv_j$ is an edge whose endpoints have the same colour. Hence $c$ is not proper. Since $c$ was arbitrary, $K_4$ has no proper $3$-colouring. $\square$

**Conclusion.** By Claims 1 and 2, $K_4$ is a planar graph that is not $3$-colourable. So the statement "every planar graph is 3-colorable" is false. $\blacksquare$

## Remarks

- **Smallest counterexample.** Every graph with at most $3$ vertices is $3$-colourable (give each vertex its own colour). So $K_4$ is a counterexample with the fewest possible vertices.
- **The edge-colouring reading is also false.** The star $K_{1,4}$ (one centre joined to four leaves) is planar. Its four edges share the centre, so they need four distinct colours.
- **Not just "4 instead of 3".** Planar graphs can contain $K_4$ as a subgraph, so no "3-colour" statement can hold for all planar graphs. More complicated examples exist too: the wheel $W_5$ (a 5-cycle plus a centre joined to all of it) is planar, contains no $K_4$, and still needs 4 colours. Its odd outer cycle needs 3 colours, and the centre is adjacent to all of them.
- **Corrected statements (cited, not proven here):**
  - *Four Colour Theorem* (Appel–Haken 1976; Robertson–Sanders–Seymour–Thomas 1997): every planar graph is 4-colourable. This bound is tight because of $K_4$.
  - *Five Colour Theorem* (Heawood 1890): every planar graph is 5-colourable. It has a short hand proof.
  - *Grötzsch's theorem* (1959): every triangle-free planar graph is 3-colourable.
  - Every *outerplanar* graph is 3-colourable.
- **Complexity.** Deciding whether a given planar graph is 3-colourable is NP-complete (Garey–Johnson–Stockmeyer 1976). So no simple characterisation of the 3-colourable planar graphs is expected.
