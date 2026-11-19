# Edge-disjoint spanning trees and the partition condition (Nash-Williams–Tutte)

**Status:** Proven
**Working folder:** proof-exchange/edge-disjoint-spanning-trees-partition-condition/
**Date:** 2026-11-19
**Reviewed by:** self-review + proof-reviewer agent (1 round)

## Problem

a connected graph G has k edge disjoined spanning trees if and only if for every partition of V(G) into A_1, ... ,A_n the number of edges between A_1, ..., A_n is at least k(n-1)

## Formal statement

**Theorem.** Let $G=(V,E)$ be a finite connected graph (parallel edges are allowed; see the conventions) and let $k \ge 0$ be an integer. Then the following are equivalent:

1. $G$ contains $k$ pairwise edge-disjoint spanning trees.
2. For every $r \ge 1$ and every partition $\mathcal P=\{V_1,\dots,V_r\}$ of $V$ into $r$ non-empty sets, the number $e_G(\mathcal P)$ of edges of $G$ whose two endpoints lie in different sets of $\mathcal P$ satisfies
$$e_G(\mathcal P) \ \ge\ k(r-1).$$

(The problem uses $n$ for the number of parts; we write $r$ instead and reserve nothing else for it.) The proof below does not use that $G$ is connected, so the equivalence holds for every finite loopless multigraph with non-empty vertex set.

## Definitions and conventions

- $G=(V,E)$ is finite, $V \neq \emptyset$. Parallel edges are allowed (so the result covers simple graphs as a special case). Loops are not allowed; this is no restriction, since a loop lies in no spanning tree and never joins two different parts of a partition, so deleting all loops changes neither side of the equivalence.
- Every edge $e$ has two distinct endpoints; we write $e=xy$ (with parallel edges, different edges may have the same endpoints).
- A *partition* of $V$ into $r$ sets means $V = V_1 \cup \dots \cup V_r$ with the $V_j$ pairwise disjoint and **non-empty** (the standard meaning; with empty parts allowed the statement would be false, see Remarks).
- An edge is a *cross edge* of $\mathcal P$ if its endpoints lie in different parts of $\mathcal P$; $e_G(\mathcal P)$ is the number of cross edges, counted with multiplicity.
- For $S \subseteq E$ we write $(V,S)$ for the spanning subgraph with edge set $S$. $S$ is a *spanning forest* if $(V,S)$ has no cycle, and a *spanning tree* if moreover $(V,S)$ is connected. Throughout we identify a spanning forest/tree with its edge set. For $U \subseteq V$, $S[U]$ denotes the set of edges of $S$ with both endpoints in $U$, and $(U,S[U])$ the induced subgraph.
- A path has no repeated vertices; a walk may repeat vertices and edges. In a multigraph two parallel edges form a cycle of length $2$; in particular a forest contains no parallel edges, and in a forest the unique path between the endpoints of an edge $e'$ is the one-edge path $e'$ itself.

**Standard facts used** (all elementary):

- **(F1)** In a forest, two vertices in the same component are joined by exactly one path.
- **(F2)** A forest with $N$ vertices and $c$ components has exactly $N-c$ edges.
- **(F3)** If $(V,S)$ is a forest and $e=xy \notin S$ with $x,y$ in different components of $(V,S)$, then $(V,S\cup\{e\})$ is a forest.
- **(F4)** A connected multigraph on $r$ vertices has at least $r-1$ edges.
- **(F5)** Every $u$–$w$ walk contains a $u$–$w$ path whose edges are among the edges of the walk. In particular, two vertices joined by a walk lie in the same component.

## Proof idea

Necessity: each spanning tree, viewed "between the parts", still connects all $r$ parts, so it needs at least $r-1$ cross edges. Sufficiency: take $k$ edge-disjoint spanning forests with as many edges as possible and look at all edges that can be "freed" by exchanging edges between unused edges and the forests. The components of the graph formed by these freeable edges give a partition $\mathcal P$; the maximality shows every forest is connected inside every part, so all cross edges are forest edges and each forest $F_i$ contributes exactly $r - c_i$ cross edges, where $c_i$ is its number of components. The partition condition then forces $c_i = 1$ for all $i$, i.e. every forest is a spanning tree.

## Proof

### Part 1: (1) $\Rightarrow$ (2)

Let $T_1,\dots,T_k$ be pairwise edge-disjoint spanning trees and $\mathcal P=\{V_1,\dots,V_r\}$ a partition of $V$ into non-empty sets.

**Claim 1.** Each $T_i$ contains at least $r-1$ cross edges of $\mathcal P$.

*Proof of Claim 1.* Let $H_i$ be the multigraph with vertex set $\{1,\dots,r\}$ which has, for every cross edge $xy \in T_i$ with $x\in V_a$, $y \in V_b$ ($a\neq b$), one edge between $a$ and $b$. Then $|E(H_i)|$ equals the number of cross edges in $T_i$. $H_i$ is connected: let $a \ne b$, pick $x \in V_a$, $y\in V_b$ (possible since parts are non-empty), and let $x=z_0,z_1,\dots,z_m=y$ be an $x$–$y$ path in the tree $T_i$. Let $p(z)$ denote the index of the part containing $z$. For each $t$, either $p(z_{t-1})=p(z_t)$, or $z_{t-1}z_t$ is a cross edge in $T_i$ and hence gives an edge of $H_i$ between $p(z_{t-1})$ and $p(z_t)$. Deleting repetitions from $p(z_0),\dots,p(z_m)$ therefore gives an $a$–$b$ walk in $H_i$. By (F4), $|E(H_i)| \ge r-1$. $\square$

Since the $T_i$ are pairwise edge-disjoint, their cross edges are distinct edges of $G$, so $e_G(\mathcal P) \ge k(r-1)$. This proves (2).

### Part 2: (2) $\Rightarrow$ (1)

Assume (2). If $k=0$ there is nothing to prove, so let $k\ge 1$.

**Setup.** Call a $k$-tuple $\mathbf F=(F_1,\dots,F_k)$ of pairwise disjoint spanning forests of $G$ an *admissible tuple*; put $E[\mathbf F]=F_1\cup\dots\cup F_k$ and $\|\mathbf F\| = |E[\mathbf F]| = \sum_i |F_i|$. Admissible tuples exist ($F_1=\dots=F_k=\emptyset$) and there are finitely many, so we can fix an admissible tuple $\mathbf F$ with $\|\mathbf F\|$ maximum. Write $\mu := \|\mathbf F\|$.

**Replacement.** Let $\mathbf F'$ be admissible, $e=xy\in E\setminus E[\mathbf F']$, and $l\in\{1,\dots,k\}$ such that $x,y$ lie in the same component of $(V,F'_l)$. Let $P$ be the unique $x$–$y$ path in $(V,F'_l)$ (F1) and let $e'\in E(P)$. Define $\mathbf F''$ by $F''_l := (F'_l\setminus\{e'\})\cup\{e\}$ and $F''_j:=F'_j$ for $j \ne l$. We say $\mathbf F''$ *arises from $\mathbf F'$ by replacing $e'$ with $e$ (in index $l$)*.

**Claim 2.** In this situation:
(a) $x$ and $y$ lie in different components of $(V, F'_l\setminus\{e'\})$;
(b) $\mathbf F''$ is admissible and $\|\mathbf F''\|=\|\mathbf F'\|$;
(c) $\mathbf F'$ arises from $\mathbf F''$ by replacing $e$ with $e'$ (in index $l$).

*Proof of Claim 2.* (a) If $x,y$ were joined by a path in $(V,F'_l\setminus\{e'\})$, this would be an $x$–$y$ path in $(V,F'_l)$ different from $P$ (it avoids $e'\in E(P)$), contradicting (F1).
(b) By (a) and (F3), $(V,F''_l)$ is a forest. The edge $e$ lies in no $F'_j$ (as $e\notin E[\mathbf F']$), and $e'$ is removed, so the $F''_j$ are pairwise disjoint. Since $e\notin F'_l$ and $e'\in F'_l$, $|F''_l|=|F'_l|$, so $\|\mathbf F''\|=\|\mathbf F'\|$.
(c) Let $e'=uv$, where $P$ runs $x,\dots,u,v,\dots,y$. Then $e'\notin E[\mathbf F'']$: it was removed from $F'_l$ and lies in no other $F'_j=F''_j$ by disjointness. In $(V,F''_l)$ the walk $u \xrightarrow{P} x \xrightarrow{e} y \xrightarrow{P} v$ (using the segments of $P$ other than $e'$) joins $u$ and $v$, so $u,v$ lie in the same component of $(V,F''_l)$. Moreover $F''_l\setminus\{e\} = F'_l\setminus\{e'\}$, in which $u$ and $v$ lie in different components (as in (a): otherwise there would be a second $u$–$v$ path in $(V,F'_l)$ besides the edge $e'$). Hence the unique $u$–$v$ path in $(V,F''_l)$ contains $e$. Replacing $e$ with $e'$ in index $l$ is therefore allowed and gives $(F''_l\setminus\{e\})\cup\{e'\} = F'_l$, i.e. $\mathbf F'$. $\square$

Let $\mathcal F$ be the set of admissible tuples obtainable from $\mathbf F$ by a finite sequence (possibly empty) of replacements. By Claim 2(b), every $\mathbf F'\in\mathcal F$ is admissible with $\|\mathbf F'\|=\mu$, i.e. also of maximum size. By Claim 2(c), every step of such a sequence can be reversed, so for every $\mathbf F'\in\mathcal F$ there is also a finite sequence of replacements leading from $\mathbf F'$ to $\mathbf F$. Also, $\mathcal F$ is closed under replacement by definition.

Define
$$\hat E := \bigcup_{\mathbf F'\in\mathcal F}\bigl(E\setminus E[\mathbf F']\bigr), \qquad \hat G := (V,\hat E).$$
So an edge lies in $\hat E$ iff it is unused by some tuple in $\mathcal F$.

**Claim 3 (freeable edges).** Let $\mathbf F'\in\mathcal F$, let $e''=ab\in E\setminus E[\mathbf F']$ and $l \in \{1,\dots,k\}$. Then $a,b$ lie in the same component of $(V,F'_l)$, and every edge of the unique $a$–$b$ path $Q$ in $(V,F'_l)$ lies in $\hat E$. Also $e''\in\hat E$.

*Proof of Claim 3.* If $a,b$ were in different components of $(V,F'_l)$, then by (F3) replacing $F'_l$ by $F'_l\cup\{e''\}$ would give an admissible tuple (still pairwise disjoint because $e''\notin E[\mathbf F']$) with $\mu+1$ edges, contradicting the maximality of $\mu$. So $Q$ exists. For $f\in E(Q)$, replacing $f$ with $e''$ in index $l$ is allowed and yields a tuple $\mathbf F'''\in\mathcal F$ with $f\notin E[\mathbf F''']$ (as in the proof of Claim 2(c)); hence $f\in\hat E$. Finally $e''\in\hat E$ because $e''\notin E[\mathbf F']$ and $\mathbf F'\in\mathcal F$. $\square$

**Claim 4.** For every $\mathbf F'\in\mathcal F$, every $i\in\{1,\dots,k\}$ and every edge $e=xy\in\hat E$, there is an $x$–$y$ path in $(V,F'_i)$ all of whose edges lie in $\hat E$.

*Proof of Claim 4.* Fix $e=xy\in\hat E$. By definition of $\hat E$ there is $\mathbf F^0\in\mathcal F$ with $e\notin E[\mathbf F^0]$. As noted above, there is a sequence $\mathbf F^0,\mathbf F^1,\dots,\mathbf F^m$ of replacements from $\mathbf F^0$ to $\mathbf F$, and from $\mathbf F$ to $\mathbf F'$; concatenating, there is a sequence $\mathbf F^0,\mathbf F^1,\dots,\mathbf F^n=\mathbf F'$ in which each $\mathbf F^{j+1}$ arises from $\mathbf F^j$ by one replacement. All $\mathbf F^j$ lie in $\mathcal F$. We prove by induction on $j$ the statement

$(S_j)$: for every $i$, $(V,F^j_i)$ contains an $x$–$y$ path with all edges in $\hat E$.

*Base case $j=0$.* Since $e\notin E[\mathbf F^0]$, Claim 3 (with $\mathbf F'=\mathbf F^0$, $e''=e$, $l=i$) gives, for every $i$, the $x$–$y$ path in $(V,F^0_i)$ with all edges in $\hat E$.

*Induction step.* Assume $(S_j)$ for some $j<n$. Let $\mathbf F^{j+1}$ arise from $\mathbf F^j$ by replacing $e'=uv$ with $e''=ab$ in index $l$; so $e''\notin E[\mathbf F^j]$, $e'$ lies on the unique $a$–$b$ path $Q$ in $(V,F^j_l)$, and $F^{j+1}_l=(F^j_l\setminus\{e'\})\cup\{e''\}$. Let $i\in\{1,\dots,k\}$ and let $P$ be an $x$–$y$ path in $(V,F^j_i)$ with $E(P)\subseteq\hat E$, given by $(S_j)$.

- If $i\ne l$, then $F^{j+1}_i=F^j_i$ and $P$ works.
- If $i=l$ and $e'\notin E(P)$, then $E(P)\subseteq F^j_l\setminus\{e'\}\subseteq F^{j+1}_l$ and $P$ works.
- If $i=l$ and $e'\in E(P)$: orient $Q$ as $a,\dots,u,v,\dots,b$ (swap the names $u,v$ if necessary). The walk $W$: $u\xrightarrow{Q}a\xrightarrow{e''}b\xrightarrow{Q}v$ uses only edges of $E(Q)\setminus\{e'\}$ and $e''$, all of which lie in $F^{j+1}_l$; by Claim 3 (applied to $\mathbf F^j\in\mathcal F$, $e''$, $l$) they all lie in $\hat E$. Replacing the edge $e'$ in $P$ by the walk $W$ (traversed in the appropriate direction) yields an $x$–$y$ walk in $(V,F^{j+1}_l)$ with all edges in $\hat E$; by (F5) it contains an $x$–$y$ path with all edges in $\hat E$.

So $(S_{j+1})$ holds. By induction $(S_n)$ holds, which is the claim for $\mathbf F^n=\mathbf F'$. $\square$

**Claim 5.** Let $V_1,\dots,V_r$ be the vertex sets of the components of $\hat G=(V,\hat E)$ (so $r\ge1$ and $\mathcal P:=\{V_1,\dots,V_r\}$ is a partition of $V$ into non-empty sets). Then for every $i$ and every $j$, the graph $(V_j,F_i[V_j])$ is connected (here $\mathbf F=(F_1,\dots,F_k)$ is the fixed maximum tuple).

*Proof of Claim 5.* Let $s,t\in V_j$. Since $V_j$ is a component of $\hat G$, there is an $s$–$t$ path $s=w_0,w_1,\dots,w_p=t$ in $\hat G$, i.e. $w_{q-1}w_q\in\hat E$ for each $q$. By Claim 4 (with $\mathbf F'=\mathbf F\in\mathcal F$), for each $q$ there is a $w_{q-1}$–$w_q$ path $R_q$ in $(V,F_i)$ with all edges in $\hat E$. Consecutive vertices of $R_q$ are joined by an edge of $\hat E$, so all vertices of $R_q$ lie in the same component of $\hat G$ as $w_{q-1}$, namely in $V_j$. Hence all edges of $R_q$ belong to $F_i[V_j]$. Concatenating $R_1,\dots,R_p$ gives an $s$–$t$ walk in $(V_j,F_i[V_j])$, so $s$ and $t$ lie in the same component by (F5). $\square$

**Counting cross edges.** Consider the partition $\mathcal P$ from Claim 5.

(i) *Every cross edge of $\mathcal P$ lies in $E[\mathbf F]$.* Indeed, if $f\in E\setminus E[\mathbf F]$, then $f\in\hat E$ (as $\mathbf F\in\mathcal F$), so both endpoints of $f$ lie in the same component of $\hat G$, i.e. $f$ is not a cross edge.

(ii) *For each $i$, the forest $F_i$ contains exactly $r-c_i$ cross edges, where $c_i\ge 1$ is the number of components of $(V,F_i)$.* Let $Y_i := F_i[V_1]\cup\dots\cup F_i[V_r]$ be the set of edges of $F_i$ that are not cross edges, and $X_i := F_i\setminus Y_i$ the cross edges in $F_i$. The graph $(V,Y_i)$ is the disjoint union of the graphs $(V_j,F_i[V_j])$, $j=1,\dots,r$, each connected by Claim 5, and there are no edges of $Y_i$ between different $V_j$. Hence $(V,Y_i)$ has exactly $r$ components. It is a forest (a subgraph of the forest $(V,F_i)$), so by (F2) $|Y_i|=|V|-r$. Also by (F2), $|F_i|=|V|-c_i$. Therefore $|X_i|=|F_i|-|Y_i|=r-c_i$. Since $V\ne\emptyset$, $c_i\ge 1$.

By (i), (ii) and the disjointness of $F_1,\dots,F_k$,
$$e_G(\mathcal P)=\sum_{i=1}^k |X_i| = \sum_{i=1}^k (r-c_i) = kr-\sum_{i=1}^k c_i .$$
By hypothesis (2), $e_G(\mathcal P)\ge k(r-1)=kr-k$, hence $\sum_{i=1}^k c_i\le k$. As each $c_i\ge1$, we get $c_i=1$ for all $i$, i.e. each $(V,F_i)$ is a connected forest, a spanning tree. Thus $F_1,\dots,F_k$ are $k$ pairwise edge-disjoint spanning trees of $G$, which proves (1).

$\blacksquare$

## Remarks

- This is the theorem of Nash-Williams and Tutte (1961). The proof of the sufficiency follows the exchange argument found e.g. in Diestel, *Graph Theory*, Section 2.4; it is given here in full so that nothing beyond the elementary facts (F1)–(F5) is cited.
- **Connectivity hypothesis.** It is not used. For $k\ge1$ it is implied by either side (a spanning tree is connected; the partition $\{A,V\setminus A\}$ with $\emptyset\ne A\ne V$ has at least $k\ge1$ cross edges by (2)). For $k=0$ both sides hold trivially.
- **Non-empty parts are necessary.** If empty parts were allowed, $G=K_2$, $k=1$ and the "partition" $\{V,\emptyset\}$ would have $0<1=k(2-1)$ cross edges although $K_2$ is a spanning tree of itself.
- **Tightness.** For $\mathcal P$ the partition into singletons, the condition reads $|E|\ge k(|V|-1)$. Example: $K_4$ has $6=2\cdot 3$ edges and the two edge-disjoint spanning trees (Hamiltonian paths) $\{12,23,34\}$ and $\{13,14,24\}$; equality holds. In contrast $C_4$ has $4<2\cdot3$ edges, and indeed does not contain $2$ edge-disjoint spanning trees.
- **Multigraphs.** The proof covers multigraphs, which is natural for this statement: e.g. the multigraph with two vertices joined by $k$ parallel edges has $k$ edge-disjoint spanning trees, and its only partition with $r=2$ has exactly $k=k(2-1)$ cross edges. For simple graphs the theorem is the special case without parallel edges.
