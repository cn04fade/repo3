# Edge-disjoint spanning trees and the partition condition (Nash-Williams–Tutte)

**Status:** Simplified version, not independently reviewed
**Based on:** candidate.md
**Checked by:** proof-simplifier only

## Problem

a connected graph G has k edge disjoined spanning trees if and only if for every partition of V(G) into A_1, ... ,A_n the number of edges between A_1, ..., A_n is at least k(n-1)

## Formal statement

**Theorem.** Let $G=(V,E)$ be a finite connected graph (parallel edges are allowed) and let $k \ge 0$ be an integer. Then the following are equivalent:

1. $G$ contains $k$ pairwise edge-disjoint spanning trees.
2. For every $r \ge 1$ and every partition $\mathcal P=\{V_1,\dots,V_r\}$ of $V$ into $r$ non-empty sets, the number $e_G(\mathcal P)$ of edges of $G$ whose two endpoints lie in different sets of $\mathcal P$ satisfies
$$e_G(\mathcal P) \ \ge\ k(r-1).$$

(The problem's $n$ is written $r$ here.) The proof does not use that $G$ is connected, so the equivalence holds for every finite loopless multigraph with non-empty vertex set.

## Definitions and conventions

- $G$ is finite, $V \neq \emptyset$, and parallel edges are allowed. Loops are excluded; this is no restriction, since a loop lies in no spanning tree and never joins two different parts, so deleting all loops changes neither side of the equivalence.
- A *partition* has pairwise disjoint, **non-empty** parts. A *cross edge* of $\mathcal P$ is an edge with endpoints in different parts; cross edges are counted with multiplicity.
- We identify a spanning subgraph $(V,S)$ with its edge set $S$. $S$ is a *forest* if $(V,S)$ has no cycle, and a *spanning tree* if it is moreover connected. Two parallel edges form a cycle of length $2$, so a forest contains no parallel edges.

**Standard facts used:**

- **(F1)** In a forest, two vertices in the same component are joined by exactly one path.
- **(F2)** A forest with $N$ vertices and $c$ components has exactly $N-c$ edges.
- **(F3)** Adding to a forest an edge whose endpoints lie in different components gives a forest.

## Proof idea

Necessity is an edge count. For sufficiency, take $k$ disjoint forests with as many edges as possible, and collect all edges that can be made unused by a sequence of one-edge swaps. The components of the graph formed by these edges give a partition. Inside each part every forest is connected, and every cross edge lies in a forest. Counting cross edges and applying (2) shows that every forest is a spanning tree.

## Proof

### Part 1: (1) $\Rightarrow$ (2)

Let $T_1,\dots,T_k$ be pairwise edge-disjoint spanning trees and $\mathcal P=\{V_1,\dots,V_r\}$ a partition of $V$. Fix $i$. The edges of $T_i$ with both endpoints in $V_j$ form a forest on the non-empty set $V_j$, so by (F2) there are at most $|V_j|-1$ of them. Hence at most $\sum_{j}(|V_j|-1)=|V|-r$ edges of $T_i$ are not cross edges. Since $|T_i|=|V|-1$, the tree $T_i$ contains at least $r-1$ cross edges. The $T_i$ are pairwise disjoint, so $e_G(\mathcal P)\ge k(r-1)$.

### Part 2: (2) $\Rightarrow$ (1)

Assume (2). If $k=0$ there is nothing to prove, so let $k\ge 1$.

**Setup.** A *packing* is a $k$-tuple $\mathbf F=(F_1,\dots,F_k)$ of pairwise disjoint forests; its *size* is $\sum_i|F_i|$. An edge is *unused* by $\mathbf F$ if it lies in no $F_i$. Fix a packing $\mathbf F$ of maximum size $\mu$ (the tuple of empty forests is a packing, and there are finitely many packings).

Call two packings $\mathbf F',\mathbf F''$ of size $\mu$ *neighbours* if there are an index $l$ and edges $e'\in F'_l$, $e\notin F'_l$ such that
$$F''_l=(F'_l\setminus\{e'\})\cup\{e\},\qquad F''_j=F'_j\ \ (j\ne l).$$
Then $e\in F''_l$, $e'\notin F''_l$ and $F'_l=(F''_l\setminus\{e\})\cup\{e'\}$, so the relation is symmetric. Moreover, by disjointness within each packing, **$e$ is unused by $\mathbf F'$ and $e'$ is unused by $\mathbf F''$.**

Let $\mathcal F$ be the set of packings reachable from $\mathbf F$ by a finite (possibly empty) sequence of steps between neighbours. Let $\hat E$ be the set of edges unused by at least one member of $\mathcal F$, and put $\hat G=(V,\hat E)$. For $\mathbf F'\in\mathcal F$ and an index $i$, let $H_i(\mathbf F')=(V,F'_i\cap\hat E)$.

**Claim 1.** Let $\mathbf F'\in\mathcal F$, let $e=ab$ be unused by $\mathbf F'$, and let $l\in\{1,\dots,k\}$. Then $a$ and $b$ are joined by a path in $H_l(\mathbf F')$.

*Proof.* If $a,b$ lay in different components of $(V,F'_l)$, then by (F3) adding $e$ to $F'_l$ would give a packing of size $\mu+1$. So there is a unique $a$–$b$ path $Q$ in $(V,F'_l)$ by (F1). Let $f\in E(Q)$. By (F1), $a$ and $b$ lie in different components of $F'_l\setminus\{f\}$, so $(F'_l\setminus\{f\})\cup\{e\}$ is a forest by (F3). Replacing $F'_l$ by this forest gives a packing of size $\mu$ (since $e$ is unused by $\mathbf F'$) that is a neighbour of $\mathbf F'$, hence lies in $\mathcal F$, and does not use $f$. Thus $f\in\hat E$. So $Q$ is a path in $H_l(\mathbf F')$. $\square$

**Claim 2.** For each $i$, the graphs $H_i(\mathbf F')$, $\mathbf F'\in\mathcal F$, all have the same components.

*Proof.* Every member of $\mathcal F$ is reached from $\mathbf F$ by steps between neighbours inside $\mathcal F$, so it suffices to compare neighbours $\mathbf F',\mathbf F''\in\mathcal F$, with $l,e',e$ as in the definition. For $i\ne l$ the two graphs are equal. For $i=l$, both $e$ and $e'$ lie in $\hat E$, since $e$ is unused by $\mathbf F'$ and $e'$ is unused by $\mathbf F''$. With $C=(F'_l\setminus\{e'\})\cap\hat E=(F''_l\setminus\{e\})\cap\hat E$ we therefore have
$$H_l(\mathbf F')=(V,C\cup\{e'\}),\qquad H_l(\mathbf F'')=(V,C\cup\{e\}).$$
By Claim 1, the endpoints of $e$ are joined in $H_l(\mathbf F')$, so adding $e$ to $H_l(\mathbf F')$ does not change its components. Likewise, the endpoints of $e'$ are joined in $H_l(\mathbf F'')$, so adding $e'$ to $H_l(\mathbf F'')$ does not change its components. Both operations give the same graph $(V,C\cup\{e,e'\})$, so $H_l(\mathbf F')$ and $H_l(\mathbf F'')$ have the same components. $\square$

**Claim 3.** Let $V_1,\dots,V_r$ be the vertex sets of the components of $\hat G$. Then for every $i$, the components of $H_i(\mathbf F)$ have exactly the vertex sets $V_1,\dots,V_r$.

*Proof.* Since $F_i\cap\hat E\subseteq\hat E$, each component of $H_i(\mathbf F)$ lies inside some $V_j$. Conversely, let $xy\in\hat E$, unused by some $\mathbf F'\in\mathcal F$. By Claim 1, $x$ and $y$ lie in the same component of $H_i(\mathbf F')$, and so by Claim 2 in the same component of $H_i(\mathbf F)$. Following a path of $\hat G$ edge by edge shows that each $V_j$ lies inside one component of $H_i(\mathbf F)$. $\square$

**Counting cross edges.** Let $\mathcal P=\{V_1,\dots,V_r\}$. Every edge unused by $\mathbf F$ lies in $\hat E$, so it has both endpoints in one part. Hence every cross edge of $\mathcal P$ lies in exactly one $F_i$.

Fix $i$, and let $c_i\ge 1$ be the number of components of $(V,F_i)$. Let $Y_i$ be the set of edges of $F_i$ that are not cross edges. Then $Y_i\supseteq F_i\cap\hat E$, so by Claim 3 each $V_j$ is connected in $(V,Y_i)$; and $Y_i$ has no edge between different parts. Thus the forest $(V,Y_i)$ has exactly $r$ components, and (F2) gives $|Y_i|=|V|-r$. Also $|F_i|=|V|-c_i$ by (F2). So $F_i$ contains exactly $|F_i|-|Y_i|=r-c_i$ cross edges, and
$$e_G(\mathcal P)=\sum_{i=1}^k (r-c_i)=kr-\sum_{i=1}^k c_i.$$
By (2), $e_G(\mathcal P)\ge kr-k$, hence $\sum_{i=1}^k c_i\le k$. Since each $c_i\ge 1$, all $c_i=1$. So $F_1,\dots,F_k$ are $k$ pairwise edge-disjoint spanning trees of $G$.

$\blacksquare$

## Remarks

- This is the theorem of Nash-Williams and Tutte (1961). The sufficiency proof is a streamlined form of the exchange argument found e.g. in Diestel, *Graph Theory*, Section 2.4.
- **Connectivity hypothesis.** It is not used. For $k\ge1$ it is implied by either side (a spanning tree is connected; a partition $\{A,V\setminus A\}$ with $\emptyset\ne A\ne V$ has at least $k\ge1$ cross edges by (2)). For $k=0$ both sides hold trivially.
- **Non-empty parts are necessary.** If empty parts were allowed, $G=K_2$, $k=1$ and the "partition" $\{V,\emptyset\}$ would have $0<1=k(2-1)$ cross edges although $K_2$ is a spanning tree of itself.
- **Tightness.** For the partition into singletons, the condition reads $|E|\ge k(|V|-1)$. $K_4$ has $6=2\cdot 3$ edges and the two edge-disjoint spanning trees $\{12,23,34\}$ and $\{13,14,24\}$, so equality holds. In contrast, $C_4$ has $4<2\cdot3$ edges and does not contain $2$ edge-disjoint spanning trees.
- **Multigraphs.** Two vertices joined by $k$ parallel edges have $k$ edge-disjoint spanning trees, and the only partition with $r=2$ has exactly $k=k(2-1)$ cross edges. Simple graphs are the special case without parallel edges.
