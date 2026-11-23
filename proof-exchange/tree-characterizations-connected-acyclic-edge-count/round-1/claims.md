# Round 1 claims

## Formal statement

**Theorem.** Let $G=(V,E)$ be a finite simple undirected graph with $n=|V|\ge 1$ vertices and $m=|E|$ edges. The following are equivalent:

- (a) $G$ is a tree, i.e. $G$ is connected and acyclic;
- (b) $G$ is connected and $m=n-1$;
- (c) $G$ is acyclic and $m=n-1$.

## Definitions and conventions

All graphs are finite, simple (no loops, no multiple edges) and undirected, with a **nonempty** vertex set. Write $n(H)=|V(H)|$, $m(H)=|E(H)|$. An edge with endpoints $u,v$ is written $uv=vu$.

- **Walk:** a sequence $x_0,x_1,\dots,x_\ell$ of vertices ($\ell\ge 0$) with $x_{i-1}x_i\in E$ for $1\le i\le \ell$. It is a $x_0$-$x_\ell$ walk of **length** $\ell$. The sequence $x_0$ alone is a walk of length $0$.
- **Path:** a walk whose vertices are pairwise distinct.
- **Cycle:** a sequence $v_1,\dots,v_k$ of $k\ge 3$ pairwise distinct vertices with $v_iv_{i+1}\in E$ for $1\le i<k$ and $v_kv_1\in E$. Its edges are these $k$ pairwise distinct edges.
- **Acyclic:** the graph contains no cycle.
- **Connected:** any two vertices $u,v$ are joined by a $u$-$v$ path. In particular, the one-vertex graph $K_1$ is connected and acyclic.
- **Components:** the equivalence classes of the relation $u\sim v$ :⇔ there is a $u$-$v$ path, together with the subgraphs they induce. $c(H)$ denotes the number of components of $H$. Since $V(H)\neq\emptyset$, $c(H)\ge 1$, and $H$ is connected iff $c(H)=1$.
- **Edge deletion:** $H-e=(V(H),E(H)\setminus\{e\})$. The vertex set does not change.
- **Vertex deletion:** $H-v$ is obtained by removing $v$ and all edges incident with $v$.

**Fact F0 (may be cited in every claim).** If there is a $u$-$v$ walk, then there is a $u$-$v$ path. *Proof.* Take a $u$-$v$ walk $x_0,\dots,x_\ell$ of minimum length. If $x_i=x_j$ with $i<j$, then $x_0,\dots,x_i,x_{j+1},\dots,x_\ell$ is a shorter $u$-$v$ walk, a contradiction. $\blacksquare$ Consequently, $\sim$ is an equivalence relation (reflexive by length-$0$ walks, symmetric by reversal, transitive by concatenating walks and applying F0).

**Citation rule.** The proof must be self-contained apart from F0, induction and the well-ordering principle. Do **not** cite any fact about trees, forests or edge counts of connected graphs. In particular, do not cite: "a tree has $n-1$ edges", "a forest has $n-c$ edges", "a tree has a leaf", "a connected graph has a spanning tree", "a connected graph has at least $n-1$ edges", or "removing a cycle edge preserves connectivity". Do not use the Theorem above. Prove every auxiliary statement you need.

## Proven claims available

none

## Assignment generator-1

ID: C1

Claim: Let $H$ be an acyclic graph with $n(H)\ge 1$ vertices and $c(H)$ components. Then $m(H)=n(H)-c(H)$.

May use: F0, induction, well-ordering. No other claim.

Suggested technique: Induction on $m(H)$, for all acyclic graphs simultaneously. If $m(H)\ge 1$, use a longest path to find a vertex $v$ of degree exactly $1$. Then show that $H-v$ is acyclic, has a nonempty vertex set, and satisfies $c(H-v)=c(H)$. Prove this equality of component counts explicitly, including why a path between two vertices other than $v$ cannot pass through $v$.

## Assignment generator-2

ID: C2

Claim: Let $H$ be a connected graph, let $C$ be a cycle in $H$, and let $e$ be an edge of $C$. Then $H-e$ is connected.

May use: F0. No other claim.

Suggested technique: Direct proof. Let $e=ab$. The remaining edges of $C$ form an $a$-$b$ walk avoiding $e$; verify this explicitly from the definition of a cycle, including the case where $e$ is the closing edge $v_kv_1$. Given $x,y\in V(H)$, take an $x$-$y$ path in $H$, replace each traversal of $e$ (in either direction) by this walk, and apply F0 in $H-e$.

## Assignment generator-3

ID: C3

Claim: Every connected graph $H$ with $n(H)\ge 1$ vertices satisfies $m(H)\ge n(H)-1$.

May use: F0, induction, well-ordering. No other claim.

Suggested technique: Growing-set argument. Construct an ordering $w_1,\dots,w_{n}$ of $V(H)$ such that every $w_i$ with $i\ge 2$ has a neighbour $w_{p(i)}$ with $p(i)<i$. Connectivity must be used to show that the construction cannot stop early: consider an $x$-$y$ path from inside the current set to outside it. Then show that the $n-1$ edges $w_iw_{p(i)}$ are pairwise distinct. Do not use a "remove a leaf" argument, because a general connected graph need not have a leaf.

## Waiting

none
