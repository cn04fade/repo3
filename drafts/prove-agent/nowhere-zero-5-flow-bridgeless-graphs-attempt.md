# Every bridgeless graph has a nowhere-zero 5-flow — Attempt

**Status:** Incomplete. This statement is **Tutte's 5-Flow Conjecture** (1954), an open problem. No complete proof is claimed.
**Date:** 2026-11-19
**Reviewed by:** self-review + proof-reviewer agent (2 rounds), partial results only

## Problem

Every bridgeless graph has a nowhere-zero 5-flow.

## Formal statement

Let $G$ be a finite graph (loops and parallel edges allowed) without a bridge. Then there is an orientation $D$ of $G$ and a map $\varphi : E(G) \to \mathbb{Z}$ with $0 < |\varphi(e)| < 5$ for all $e$, such that $\partial\varphi(v) = 0$ for every vertex $v$ (definitions below).

By Tutte's theorem (Theorem T1 below), this is equivalent to: **every finite bridgeless graph has a nowhere-zero $\mathbb{Z}_5$-flow.** The work below uses this $\mathbb{Z}_5$ form.

## Definitions and conventions

- A **graph** $G = (V, E)$ is finite. Each edge has a set of one endpoint (a **loop**) or two endpoints. Parallel edges are allowed. $\deg(v)$ is the number of edges at $v$, where a loop counts twice.
- For $X \subseteq V$, the **edge cut** $\delta(X)$ is the set of non-loop edges with exactly one endpoint in $X$. Note $\delta(X) = \delta(V \setminus X)$, and a loop is never in an edge cut.
- An edge $e$ is a **bridge** if $G - e$ has more connected components than $G$. $G$ is **bridgeless** if it has no bridge. $G$ is **$k$-edge-connected** if $|\delta(X)| \ge k$ for all $\emptyset \ne X \subsetneq V$.
- An **orientation** assigns to each non-loop edge $e$ one endpoint as its tail $t(e)$ and the other as its head $h(e)$. For a loop, $t(e) = h(e)$ is its vertex.
- Let $\Gamma$ be an abelian group and $\varphi : E \to \Gamma$. The **boundary** of $\varphi$ at $v$ is
  $$\partial\varphi(v) = \sum_{e:\, t(e) = v} \varphi(e) - \sum_{e:\, h(e) = v} \varphi(e).$$
  A loop contributes $\varphi(e) - \varphi(e) = 0$. $\varphi$ is a **$\Gamma$-flow** if $\partial\varphi(v) = 0$ for all $v$. It is **nowhere-zero** if $\varphi(e) \ne 0$ for all $e$. A **nowhere-zero $k$-flow** is a $\mathbb{Z}$-flow with $0 < |\varphi(e)| < k$ for all $e$.
- **Reversal.** Reversing the orientation of an edge $e$ and replacing $\varphi(e)$ by $-\varphi(e)$ turns a flow into a flow and keeps it nowhere-zero. So whether a nowhere-zero flow exists does not depend on the orientation, and we choose orientations freely.
- **Contraction.** For a non-loop edge $e$ with endpoints $x \ne y$, $G/e$ is obtained by deleting $e$ and identifying $x$ and $y$ into a single new vertex. Edges parallel to $e$ become loops. $G - e$ deletes $e$.
- An **even subgraph** is a set $A \subseteq E$ such that every vertex has even degree in $(V, A)$.
- A graph is **cubic** if every vertex has degree $3$. A **proper 3-edge-colouring** assigns colours from $\{1,2,3\}$ to the edges so that edges sharing an endpoint get different colours. A **snark** here means a cubic bridgeless graph with no proper 3-edge-colouring. (Many authors also demand girth $\ge 5$ and cyclic 4-edge-connectivity. We use the weak definition.)
- $G$ is **cyclically $k$-edge-connected** if no edge cut with fewer than $k$ edges has a cycle on both sides.
- A **minimal counterexample** is a bridgeless graph with no nowhere-zero $\mathbb{Z}_5$-flow, chosen with the pair $(|E|, |V|)$ lexicographically smallest.

### Cited results (not proven here, by agreement)

- **T1 (Tutte 1949, 1954).** For $k \ge 2$, $G$ has a nowhere-zero $k$-flow if and only if it has a nowhere-zero $\mathbb{Z}_k$-flow. Moreover, the number of nowhere-zero $\Gamma$-flows of $G$ depends only on $|\Gamma|$. It is given by the flow polynomial $F(G, |\Gamma|)$. In particular, existence of a nowhere-zero $\Gamma$-flow depends only on $|\Gamma|$.
- **T2 (Fleischner's Splitting Lemma, 1976).** Let $G$ be connected and bridgeless, and let $v$ be a vertex without loops with $\deg(v) \ge 4$. Then there are two edges $e_1 = vu_1$, $e_2 = vu_2$ at $v$ such that the graph obtained by deleting $e_1, e_2$ and adding a new edge $u_1u_2$ is bridgeless. (The new edge is a loop if $u_1 = u_2$.)
- **T3 (Jaeger 1979; Seymour 1981).** Every bridgeless graph has a nowhere-zero 8-flow (Jaeger) and even a nowhere-zero 6-flow (Seymour).
- **T4 (Kochol 2004, 2010).** If the 5-Flow Conjecture is false, then a counterexample with the fewest vertices is a cyclically 6-edge-connected snark (*J. Combin. Theory Ser. B* 90 (2004)) of girth at least 11 (*J. Combin. Theory Ser. B* 100 (2010)). In particular, if every cyclically 6-edge-connected snark of girth at least 11 has a nowhere-zero 5-flow, the conjecture holds. (T4 is used only in this form, so its notion of "smallest" does not need to match the lexicographic order used in this report.)
- **T5 (Jaeger 1979).** Every 4-edge-connected graph has a nowhere-zero 4-flow.
- **T6 (Petersen 1898).** The Petersen graph has no proper 3-edge-colouring.

## Observations

- **The bridgeless hypothesis is necessary** (Partial result 2).
- **5 cannot be replaced by 4.** The Petersen graph $P$ is bridgeless, has a nowhere-zero $\mathbb{Z}_5$-flow (Partial result 7), but has no nowhere-zero 4-flow.
- **Small cases.**
  - A cycle $C_n$ has a nowhere-zero 2-flow (all values $1$ around the cycle).
  - The theta graph (two vertices, three parallel edges) has the $\mathbb{Z}_5$-flow $1, 1, 3$, with all three edges oriented the same way.
  - $K_4$ and $K_{3,3}$ are 3-edge-colourable cubic graphs, so they have nowhere-zero 4-flows (Partial result 5).
- **Computer check (Petersen graph).** I enumerated all $5^6$ $\mathbb{Z}_5$-flows of $P$, using the fact that its flow space has rank $m - n + 1 = 6$. Exactly $F(P,5) = 240$ of them are nowhere-zero. All $4^6$ $\mathbb{Z}_4$-flows were enumerated as well: $F(P,4) = 0$, and also $F(P,2) = F(P,3) = 0$. A separate backtracking search found no proper 3-edge-colouring of $P$.

## Approaches tried

### Approach 1: Minimal counterexample and reductions

- **Idea.** Take a minimal counterexample $G$ and show it has more and more structure, hoping to reach a contradiction.
- **How far it got.** Proven here (Partial result 4): $G$ is connected, loopless, simple, cubic, 3-edge-connected and triangle-free. It is not 3-edge-colourable (Partial result 5), so it is a snark. Kochol's results (T4) show that a counterexample with the fewest vertices is moreover cyclically 6-edge-connected with girth at least 11.
- **Where it fails.** No further reduction is known that rules out *all* cyclically 6-edge-connected snarks of large girth. Such snarks exist, so structure alone gives no contradiction. The first step I could not do myself is the reduction across a nontrivial 3-edge-cut. Let $\delta(X) = \{e_1, e_2, e_3\}$ have a cycle on both sides. Shrink each side to one vertex, which gives two smaller graphs $G_1$ and $G_2$. Assume both are smaller and bridgeless, so each has a nowhere-zero $\mathbb{Z}_5$-flow. To glue the two flows, their values on $(e_1, e_2, e_3)$ (oriented out of $X$) must agree, up to multiplying one flow by a unit $c \in \mathbb{Z}_5^*$. By Partial result 8, every such boundary triple has exactly two equal entries. There are exactly three classes under scaling, determined by **which** of the three edges carries the odd value. Minimality gives some flow on each side, but no control over its class. So the classes may differ and the flows cannot be glued. Kochol overcomes this (T4) with more elaborate gadgets, which were not reproduced here.

### Approach 2: Building the flow from smaller groups (Jaeger, Seymour)

- **Idea.**
  - **Jaeger.** A nowhere-zero $\mathbb{Z}_2^k$-flow is the same as a cover of $E$ by $k$ even subgraphs: use the indicator functions as coordinates. Three even subgraphs suffice for every bridgeless graph, which gives an 8-flow.
  - **Seymour.** For a 3-edge-connected graph, take a $\mathbb{Z}_3$-flow that is nonzero outside an even subgraph $C$, and pair it with the $\mathbb{Z}_2$-flow $\mathbf{1}_C$. This gives a nowhere-zero $\mathbb{Z}_2 \times \mathbb{Z}_3$-flow, hence a 6-flow by T1.
- **How far it got.** It works for $|\Gamma| = 8$ and $|\Gamma| = 6$ (T3). Two even subgraphs suffice in special cases, giving 4-flows (Partial results 5 and 6).
- **Where it fails.**
  - $|\Gamma| = 5$ is prime, so $\mathbb{Z}_5$ has no nontrivial subgroups. A $\mathbb{Z}_5$-flow can therefore not be split into coordinates in smaller groups that are found separately and then combined.
  - Even subgraphs only give groups $\mathbb{Z}_2^k$, of order $2^k \in \{2, 4, 8, \dots\}$. Order 4 is impossible in general (Petersen), and the next option, order 8, gives 8.
  - This is a barrier for this method, not a proof that the method can never work.
  - Jaeger's 4-edge-connected result (T5) never applies to the reduced graphs of Approach 1. A cubic graph satisfies $|\delta(\{v\})| = 3$, so it is never 4-edge-connected.

### Approach 3: Deletion–contraction for the flow polynomial

- **Idea.** The conjecture says $F(G, 5) > 0$ for every bridgeless $G$. Let $e$ be neither a loop nor a bridge. Every flow of $G/e$ extends uniquely to a flow of $G$ (Partial result 3). The nowhere-zero flows of $G/e$ therefore correspond to the flows of $G$ that are nonzero except possibly on $e$. Those that vanish on $e$ are exactly the nowhere-zero flows of $G - e$. Hence
  $$F(G,5) = F(G/e,5) - F(G - e,5).$$
- **How far it got.** The identity is correct. By induction $F(G/e,5) > 0$, because $G/e$ is bridgeless (Partial result 3). The graph $G - e$ may contain bridges, and then $F(G-e,5) = 0$.
- **Where it fails.** The recursion is a **difference**. Positivity of both terms says nothing about the sign of their difference. One would need the inequality $F(G/e, 5) > F(G - e, 5)$ for some well-chosen edge $e$. I found no way to prove such an inequality.

### Approach 4: Special classes (Hamiltonian, 3-edge-colourable)

- **Idea.** Prove the statement for large natural classes.
- **How far it got.**
  - Hamiltonian graphs have nowhere-zero 4-flows (Partial result 6).
  - 3-edge-colourable bridgeless cubic graphs have nowhere-zero 4-flows (Partial result 5).
- **Where it fails.** These classes contain no snark. Every Hamiltonian cubic graph is 3-edge-colourable: its Hamiltonian cycle has even length $n$, because $3n = 2|E|$. Colour the cycle edges alternately $1, 2$, and colour the remaining edges, which form a perfect matching, with $3$. By Approach 1 the hard cases are exactly snarks, so these special cases never reach the open part of the problem.

## Partial results

**Partial result 1 (Cut lemma).** Let $\varphi$ be a $\Gamma$-flow and $X \subseteq V$. Write $\delta^+(X)$ and $\delta^-(X)$ for the edges of $\delta(X)$ with tail in $X$ and with head in $X$, respectively. Then
$$\sum_{e \in \delta^+(X)} \varphi(e) - \sum_{e \in \delta^-(X)} \varphi(e) = 0.$$

*Proof.* Sum $\partial\varphi(v) = 0$ over $v \in X$. We count each edge's contribution to the sum:

- A non-loop edge with both endpoints in $X$ contributes $+\varphi(e)$ at its tail and $-\varphi(e)$ at its head, so $0$ in total.
- A loop contributes $0$.
- An edge with no endpoint in $X$ contributes nothing.
- An edge of $\delta^+(X)$ contributes $+\varphi(e)$, and an edge of $\delta^-(X)$ contributes $-\varphi(e)$.

Since every term $\partial\varphi(v)$ is $0$, the stated identity follows. $\blacksquare$

**Partial result 2 (Bridges).**
(a) An edge $e$ is a bridge if and only if $\delta(X) = \{e\}$ for some $X \subseteq V$.
(b) A graph with a bridge has no nowhere-zero $\Gamma$-flow for any abelian group $\Gamma$. So the hypothesis "bridgeless" cannot be dropped.

*Proof.*

(a) First let $e$ be a bridge. Then $e$ is not a loop: a walk can skip a loop, so deleting a loop never changes the components. Let $e$ have endpoints $u \ne v$. If $u$ and $v$ were joined by a walk in $G - e$, then every walk in $G$ could replace each use of $e$ by that walk. Then $G$ and $G - e$ would have the same components, a contradiction. So $u$ and $v$ lie in different components of $G - e$. Let $X$ be the vertex set of the component of $G - e$ containing $u$. No edge of $G - e$ leaves $X$, and $e$ leaves $X$ because $v \notin X$. Hence $\delta(X) = \{e\}$.

Conversely, let $\delta(X) = \{e\}$, with $e = uv$, $u \in X$ and $v \notin X$. A $u$–$v$ walk in $G - e$ would have to use an edge of $\delta(X) \setminus \{e\} = \emptyset$, which is impossible. So $u$ and $v$ lie in the same component of $G$ but in different components of $G - e$. Every component of $G - e$ lies inside a component of $G$, and here the component of $G$ containing $u$ splits. Hence $G - e$ has more components than $G$.

(b) Let $e$ be a bridge. By (a), $\delta(X) = \{e\}$ for some $X$. Partial result 1 gives $\pm\varphi(e) = 0$, so $\varphi(e) = 0$. $\blacksquare$

**Partial result 3 (Contraction).** Let $e$ be a non-loop edge with endpoints $x \ne y$.
(a) If $G$ is bridgeless, then $G/e$ is bridgeless. Deleting a loop from a bridgeless graph also leaves it bridgeless.
(b) Every $\Gamma$-flow $\varphi'$ of $G/e$ extends uniquely to a $\Gamma$-flow $\varphi$ of $G$, that is, $\varphi|_{E \setminus \{e\}} = \varphi'$.

*Proof.*

(a) Let $\pi : V(G) \to V(G/e)$ map $x$ and $y$ to the new vertex and fix all other vertices. For $X' \subseteq V(G/e)$ let $X = \pi^{-1}(X')$. Then $x$ and $y$ lie on the same side of $X$, so $e \notin \delta_G(X)$. Every other edge $g$ with endpoints $p, q$ has exactly one endpoint in $X$ if and only if exactly one of $\pi(p), \pi(q)$ lies in $X'$. Hence $\delta_{G/e}(X') = \delta_G(X)$. A bridge $g$ of $G/e$ therefore gives, by Partial result 2(a), a set $X$ with $\delta_G(X) = \{g\}$, so $g$ is a bridge of $G$.

Deleting a loop does not change any edge cut, because loops lie in no edge cut. By Partial result 2(a) it then creates no bridge.

(b) Define $\varphi = \varphi'$ on $E \setminus \{e\}$, with orientations inherited. Let $a$ be the boundary at $x$ of $\varphi$ restricted to $E \setminus \{e\}$, and $b$ the same boundary at $y$. Every vertex other than $x, y$ has the same incident edges in $G - e$ as in $G/e$, so its boundary is $0$.

Edges between $x$ and $y$ other than $e$ contribute opposite amounts at $x$ and $y$, and they are loops in $G/e$, where they contribute $0$. All other edges contribute at $x$ or $y$ exactly what they contribute at the merged vertex. So $a + b$ equals the boundary of $\varphi'$ at the merged vertex, which is $0$, and therefore $b = -a$.

Orient $e$ from $x$ to $y$ and set $\varphi(e) = -a$. The boundary at $x$ becomes $a + (-a) = 0$, and the boundary at $y$ becomes $-a - (-a) = 0$. So $\varphi$ is a flow. It is unique, because $\partial\varphi(x) = 0$ forces $\varphi(e) = -a$. $\blacksquare$

**Partial result 4 (Structure of a minimal counterexample).** A minimal counterexample $G$ is connected, loopless, simple, cubic, 3-edge-connected and has no triangle.

*Proof.* By minimality, every bridgeless graph $H$ with $(|E(H)|, |V(H)|)$ lexicographically smaller than $(|E(G)|, |V(G)|)$ has a nowhere-zero $\mathbb{Z}_5$-flow. Each step below derives a contradiction from the negation of one property.

1. **Connected.** Suppose $V = V_1 \cup V_2$ with $V_1, V_2 \ne \emptyset$ and no edge between them. Let $G_1 = G[V_1]$ and $G_2 = G[V_2]$. For $X \subseteq V_i$ we have $\delta_{G_i}(X) = \delta_G(X)$, so each $G_i$ is bridgeless by Partial result 2(a). Each $G_i$ also has at most $|E|$ edges and fewer vertices than $G$, so it is smaller. Nowhere-zero flows of $G_1$ and $G_2$ together form one of $G$, a contradiction.
2. **Loopless.** Let $\ell$ be a loop. Then $G - \ell$ is bridgeless by Partial result 3(a) and has fewer edges, so it has a nowhere-zero flow $\varphi'$. Setting $\varphi(\ell) = 1$ gives a nowhere-zero flow of $G$, because a loop contributes $0$ to every boundary. Contradiction.
3. **$|V| \ge 2$ and minimum degree at least $1$.** If $|V| = 1$, then by step 2 there are no edges, and the empty map is a nowhere-zero flow. So $|V| \ge 2$. Since $G$ is connected, every vertex has an incident edge.
4. **No vertex of degree $1$.** If $\deg(v) = 1$, then $\delta(\{v\})$ is a single edge, which is a bridge by Partial result 2(a). Contradiction.
5. **No vertex of degree $2$.** Let $\deg(v) = 2$ with edges $e_1, e_2$. Both are non-loops by step 2, and $\delta(\{v\}) = \{e_1, e_2\}$.
   - $G/e_1$ is bridgeless (Partial result 3(a)) and has fewer edges, so it has a nowhere-zero flow $\varphi'$.
   - Extend $\varphi'$ to a flow $\varphi$ of $G$ by Partial result 3(b).
   - By Partial result 1 for $X = \{v\}$, $\varphi(e_1) = \pm\varphi(e_2) = \pm\varphi'(e_2) \ne 0$.

   So $\varphi$ is nowhere-zero. Contradiction.
6. **No vertex of degree $\ge 4$.** Let $\deg(v) \ge 4$. $G$ is connected (step 1), bridgeless, and has no loop at $v$ (step 2). By T2 there are edges $e_1 = vu_1$, $e_2 = vu_2$ such that $G'$, obtained by deleting $e_1, e_2$ and adding a new edge $f = u_1u_2$, is bridgeless. $G'$ has $|E| - 1$ edges, so it has a nowhere-zero flow $\varphi'$.
   - Orient $f$ from $u_1$ to $u_2$ (both ends are $u_1$ if $f$ is a loop).
   - Keep $\varphi'$ on the edges shared by $G$ and $G'$.
   - Orient $e_1$ from $u_1$ to $v$ and $e_2$ from $v$ to $u_2$, and put $\varphi(e_1) = \varphi(e_2) = \varphi'(f) \ne 0$.

   Now check the boundaries:
   - At $v$: $e_1$ contributes $-\varphi'(f)$ and $e_2$ contributes $+\varphi'(f)$, so the boundary is unchanged, namely $0$. (The other edges at $v$ are as in $G'$, where $v$ has boundary $0$.)
   - At $u_1$: $e_1$ contributes $+\varphi'(f)$, exactly as $f$ did as tail.
   - At $u_2$: $e_2$ contributes $-\varphi'(f)$, exactly as $f$ did as head.
   - If $u_1 = u_2$, the total is $0$, exactly as for the loop $f$.

   All other vertices are unchanged. So $\varphi$ is a nowhere-zero flow of $G$. Contradiction. Hence $G$ is cubic.
7. **3-edge-connected.** Let $\emptyset \ne X \subsetneq V$. If $|\delta(X)| = 0$, then $G$ is disconnected, which contradicts step 1. If $|\delta(X)| = 1$, the edge is a bridge (Partial result 2(a)). Now suppose $\delta(X) = \{e, f\}$; $e$ is not a loop, since loops lie in no cut.
   - $G/e$ is bridgeless and has fewer edges, so it has a nowhere-zero flow $\varphi'$.
   - Extend it to a flow $\varphi$ of $G$ (Partial result 3(b)).
   - Partial result 1 gives $\varphi(e) = \pm\varphi(f) = \pm\varphi'(f) \ne 0$. (Note that $f$ remains an edge of $G/e$, possibly as a loop.)

   So $\varphi$ is a nowhere-zero flow of $G$. Contradiction.
8. **Simple.** Suppose $u \ne v$ are joined by at least two parallel edges.
   - If there are three, then $u$ and $v$ have no other edges, since $G$ is cubic. By connectivity $V = \{u, v\}$, so $G$ is the theta graph. That graph has the nowhere-zero flow $1, 1, 3$ with all edges oriented from $u$ to $v$, because $1 + 1 + 3 = 5 \equiv 0$. Contradiction.
   - If there are exactly two, then the third edges at $u$ and at $v$ do not join $u$ to $v$. So $V \ne \{u, v\}$, and $\delta(\{u,v\})$ consists of exactly these two third edges. That cut has size $2$, contradicting step 7.
9. **Triangle-free.** Suppose $a, b, c$ span a triangle with edges $ab$, $bc$, $ca$. Since $G$ is cubic and simple, each of $a, b, c$ has exactly one further edge, called $e_a, e_b, e_c$. These three edges are distinct, and each has its other endpoint outside $\{a,b,c\}$. (A third edge from $a$ to $b$ would be parallel to $ab$.)
   - Let $G''$ be obtained by contracting $ab$ and then $bc$, and deleting the loop that $ca$ has become. All of $a, b, c$ are merged into one vertex $t$, whose edges are $e_a, e_b, e_c$.
   - $G''$ is bridgeless by Partial result 3(a) and has fewer edges, so it has a nowhere-zero flow $\varphi''$.
   - Let $\alpha$ be the contribution of $e_a$ to $\partial\varphi''(t)$, that is, $\pm\varphi''(e_a)$ according to its orientation. Define $\beta$ and $\gamma$ the same way for $e_b$ and $e_c$. Then $\alpha, \beta, \gamma \ne 0$ and $\alpha + \beta + \gamma = \partial\varphi''(t) = 0$.

   In $G$, keep $\varphi''$ on all edges other than $ab, bc, ca$, and orient the triangle as $a \to b \to c \to a$. For $z \in \mathbb{Z}_5$ set
   $$\varphi(ca) = z, \qquad \varphi(ab) = z - \alpha, \qquad \varphi(bc) = z + \gamma.$$
   The boundaries are:
   - at $a$: $\alpha + (z - \alpha) - z = 0$;
   - at $b$: $\beta + (z + \gamma) - (z - \alpha) = \alpha + \beta + \gamma = 0$;
   - at $c$: $\gamma + z - (z + \gamma) = 0$;
   - at every other vertex, the same as in $G''$, namely $0$.

   Choose $z \notin \{0, \alpha, -\gamma\}$. This excludes at most $3$ of the $5$ elements of $\mathbb{Z}_5$, so such a $z$ exists. Then $\varphi$ is a nowhere-zero flow of $G$. Contradiction. $\blacksquare$

**Partial result 5 (Cubic graphs: 4-flows and edge-colourings).**
(a) A cubic bridgeless graph is loopless.
(b) A loopless cubic graph has a nowhere-zero $\mathbb{Z}_2^2$-flow if and only if it has a proper 3-edge-colouring.
(c) Consequently, a 3-edge-colourable **bridgeless** cubic graph (loopless by (a)) has a nowhere-zero 4-flow, and in particular a nowhere-zero $\mathbb{Z}_5$-flow. A minimal counterexample is therefore a snark.

*Proof.*

(a) Suppose a vertex $v$ of a cubic graph has a loop. The loop accounts for $2$ of the degree $3$, so $v$ has exactly one other edge $g$. That edge is not a loop, so $\delta(\{v\}) = \{g\}$, and $g$ is a bridge by Partial result 2(a).

(b) In $\mathbb{Z}_2^2$ we have $-x = x$, so orientations do not matter, and at each vertex the condition reads "the three values sum to $0$".

($\Rightarrow$) Suppose the three values at a vertex are nonzero and two of them are equal, say both $x$. Then $x + x = 0$ forces the third to be $0$, a contradiction. So the three values are pairwise distinct. Using the three nonzero elements of $\mathbb{Z}_2^2$ as colours gives a proper 3-edge-colouring.

($\Leftarrow$) Let $M_1, M_2, M_3$ be the colour classes. Every vertex meets each class exactly once, because it has three edges with distinct colours and there are no loops. Hence $A = M_1 \cup M_2$ and $B = M_1 \cup M_3$ are even subgraphs: every vertex has degree $2$ in each. Put $\varphi(e) = (\mathbf{1}_A(e), \mathbf{1}_B(e)) \in \mathbb{Z}_2^2$. At $v$, the first coordinate of $\partial\varphi(v)$ is the number of $A$-edges at $v$ taken mod $2$, which is $0$. The same holds for the second coordinate. On $M_1$, $M_2$ and $M_3$ the values are $(1,1)$, $(1,0)$ and $(0,1)$, so $\varphi$ is nowhere-zero.

(c) By (a) such a graph is loopless, so (b) applies. By (b) and T1 (orders $|\mathbb{Z}_2^2| = |\mathbb{Z}_4| = 4$), such a graph has a nowhere-zero $\mathbb{Z}_4$-flow, and hence a nowhere-zero integer 4-flow $\psi$ with $0 < |\psi(e)| \le 3$. Reducing $\psi$ modulo $5$ gives a $\mathbb{Z}_5$-flow. It is nowhere-zero because $\psi(e) \in \{\pm 1, \pm 2, \pm 3\}$ is not divisible by $5$. By Partial result 4 a minimal counterexample is cubic and bridgeless, so it cannot be 3-edge-colourable. It is a snark. $\blacksquare$

**Partial result 6 (Hamiltonian graphs).** Let $G$ have $|V| \ge 2$ and a cycle $C$ through all vertices (a Hamiltonian cycle). Then $G$ has a nowhere-zero 4-flow, and hence a nowhere-zero $\mathbb{Z}_5$-flow.

*Proof.* Pick $e_0 \in C$. Then $T = C - e_0$ is a path through all vertices, which is a spanning tree.

For each edge $f \notin T$, let $C_f$ be $f$ together with the path in $T$ between the endpoints of $f$; if $f$ is a loop, $C_f = \{f\}$. Each $C_f$ is an even subgraph and satisfies $C_f \setminus T = \{f\}$.

The symmetric difference of two even subgraphs is even, because $\deg_{A \triangle B}(v) = \deg_A(v) + \deg_B(v) - 2\deg_{A \cap B}(v)$. Let $R = E \setminus C$ be the set of chords and put
$$S = \mathop{\triangle}_{f \in R} C_f.$$
Then $S$ is even, and $S \setminus T = R$, since each chord lies in exactly one of the $C_f$ with $f \in R$. In particular $R \subseteq S$.

The cycle $C$ is also even. Put $\varphi(e) = (\mathbf{1}_C(e), \mathbf{1}_S(e)) \in \mathbb{Z}_2^2$.

- **It is a flow.** In each coordinate, the boundary at $v$ is the number of non-loop edges of that even subgraph at $v$, taken mod $2$. This has the same parity as the degree, because loops add $2$. So it is $0$.
- **It is nowhere-zero.** Edges of $C$ have first coordinate $1$, and edges of $R \subseteq S$ have second coordinate $1$.

As in Partial result 5(c), T1 then gives a nowhere-zero 4-flow, and reducing it mod $5$ gives a nowhere-zero $\mathbb{Z}_5$-flow. $\blacksquare$

**Partial result 7 (Petersen graph).** The Petersen graph $P$ has a nowhere-zero $\mathbb{Z}_5$-flow but no nowhere-zero 4-flow.

*Proof.* Label the outer 5-cycle $0, \dots, 4$, the inner vertices $5, \dots, 9$, the spokes $i$–$(i+5)$, and the inner edges $(5+i)$–$(5 + (i+2 \bmod 5))$. Orient each edge as written below ($\text{tail} \to \text{head}$):

| edge | value | edge | value | edge | value |
|---|---|---|---|---|---|
| $0 \to 1$ | 2 | $5 \to 7$ | 4 | $0 \to 5$ | 1 |
| $1 \to 2$ | 3 | $6 \to 8$ | 1 | $1 \to 6$ | 4 |
| $2 \to 3$ | 1 | $7 \to 9$ | 1 | $2 \to 7$ | 2 |
| $3 \to 4$ | 4 | $8 \to 5$ | 3 | $3 \to 8$ | 2 |
| $4 \to 0$ | 3 | $9 \to 6$ | 2 | $4 \to 9$ | 1 |

The boundaries (out minus in) are, mod $5$:

| vertex | computation | vertex | computation |
|---|---|---|---|
| 0 | $2 + 1 - 3 = 0$ | 5 | $4 - 1 - 3 = 0$ |
| 1 | $3 + 4 - 2 = 5$ | 6 | $1 - 4 - 2 = -5$ |
| 2 | $1 + 2 - 3 = 0$ | 7 | $1 - 4 - 2 = -5$ |
| 3 | $4 + 2 - 1 = 5$ | 8 | $3 - 1 - 2 = 0$ |
| 4 | $3 + 1 - 4 = 0$ | 9 | $2 - 1 - 1 = 0$ |

All of these are $\equiv 0 \pmod 5$, and all values are nonzero.

$P$ is cubic and loopless, and it has no proper 3-edge-colouring by T6. (This was also confirmed by an exhaustive computer search, see Observations, but the proof relies only on T6.) By Partial result 5(b), $P$ has no nowhere-zero $\mathbb{Z}_2^2$-flow. By T1, it then has no nowhere-zero $\mathbb{Z}_4$-flow and no nowhere-zero 4-flow. $\blacksquare$

**Partial result 8 (Boundary triples on a 3-edge-cut).** Let $(a_1, a_2, a_3) \in (\mathbb{Z}_5 \setminus \{0\})^3$ with $a_1 + a_2 + a_3 = 0$. Then exactly two of the $a_i$ are equal. The $12$ such triples fall into exactly $3$ classes under multiplication by $c \in \mathbb{Z}_5^*$, determined by the position of the entry that differs from the other two.

*Proof.* If $a_1 = a_2 = a_3 = a$, then $3a = 0$, so $a = 0$ because $3$ is invertible mod $5$. That is impossible.

If the three entries are pairwise distinct, they are three of the four elements $1, 2, 3, 4$; let $d$ be the missing one. Then $a_1 + a_2 + a_3 = (1 + 2 + 3 + 4) - d = 10 - d \equiv -d \ne 0$. That is also impossible. Hence exactly two entries are equal.

Count the triples: $a_1$ has $4$ choices, then $a_2 \notin \{0, -a_1\}$ has $3$, and $a_3 = -a_1 - a_2$ is determined and nonzero. That gives $12$ triples.

Multiplication by $c \ne 0$ is a bijection of $\mathbb{Z}_5$, so it preserves which entries are equal and hence the position of the odd entry. Each class has exactly $4$ elements, because $c \mapsto c \cdot (a_1, a_2, a_3)$ is injective, as $a_1 \ne 0$. The odd entry can sit in $3$ positions, each position is attained (for example $(3,1,1)$, $(1,3,1)$, $(1,1,3)$), and $3 \cdot 4 = 12$. So the classes are exactly the $3$ positions. $\blacksquare$

## The gap

**[GAP]** Partial results 4 and 5 show that it would suffice to prove the following:

> Every snark that is 3-edge-connected, simple and triangle-free has a nowhere-zero $\mathbb{Z}_5$-flow.

Independently, by T4 it suffices to prove:

> Every cyclically 6-edge-connected snark of girth at least 11 has a nowhere-zero $\mathbb{Z}_5$-flow.

I could not prove either statement. Specifically:

- The 3-edge-cut gluing in Approach 1 needs control over the boundary class (Partial result 8) of the flows on both sides. Minimality gives no such control.
- The even-subgraph and product-group methods in Approach 2 cannot produce a group of prime order $5$.
- Deletion–contraction (Approach 3) would need the inequality $F(G/e, 5) > F(G-e, 5)$ for some edge $e$. I have no argument for it.

## Ideas for next steps

- **Oddness.** The oddness of a cubic bridgeless graph is the minimum number of odd cycles in a 2-factor. It is reported that graphs of oddness 2 have nowhere-zero 5-flows (Jaeger), with extensions to some oddness-4 classes (Steffen; Máčajová and Škoviera). One could try to reproduce the oddness-2 argument as a further partial result.
- **Prescribed boundaries.** Study which boundary classes (Partial result 8) a cubic graph with one marked degree-3 vertex can realise, aiming to show that all three classes are always realisable. That would complete the 3-cut reduction in Approach 1 without Kochol's gadgets.
- **Computation.** The conjecture has been reported verified by computer for all snarks up to 36 vertices (Brinkmann, Goedgebeur, Hägglund, Markström 2013). A local check for small snarks could support conjectured lemmas.
- **References.** C.-Q. Zhang, *Integer Flows and Cycle Covers of Graphs* (1997); F. Jaeger, "Nowhere-zero flow problems" (1988 survey); P. D. Seymour, "Nowhere-zero 6-flows", *J. Combin. Theory Ser. B* 30 (1981).
