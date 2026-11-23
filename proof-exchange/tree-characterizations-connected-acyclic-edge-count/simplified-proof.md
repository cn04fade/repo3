# Three equivalent characterizations of trees

**Status:** Simplified version, not independently reviewed
**Based on:** candidate.md
**Checked by:** proof-simplifier only

## Problem

Let G be a finite simple undirected graph with n >= 1 vertices. Prove that the following are equivalent: (a) G is a tree (connected and acyclic); (b) G is connected and has exactly n-1 edges; (c) G is acyclic and has exactly n-1 edges.

## Formal statement

**Theorem.** Let $G=(V,E)$ be a finite simple undirected graph with $n=|V|\ge 1$ vertices and $m=|E|$ edges. The following are equivalent:

- (a) $G$ is connected and acyclic;
- (b) $G$ is connected and $m=n-1$;
- (c) $G$ is acyclic and $m=n-1$.

## Definitions and conventions

All graphs are finite, simple and undirected, with a nonempty vertex set. An edge with endpoints $u,v$ is written $uv=vu$.

- **Walk:** a sequence $x_0,\dots,x_\ell$ of vertices ($\ell\ge 0$) with $x_{i-1}x_i\in E(H)$ for $1\le i\le\ell$. It is an $x_0$-$x_\ell$ walk of length $\ell$.
- **Path:** a walk whose vertices are pairwise distinct.
- **Cycle:** a sequence $v_1,\dots,v_k$ of $k\ge 3$ pairwise distinct vertices with $v_iv_{i+1}\in E(H)$ for $1\le i<k$ and $v_kv_1\in E(H)$. Its edges are these $k$ edges.
- **Acyclic:** containing no cycle.
- **Connected:** any two vertices $u,v$ are joined by a $u$-$v$ path.
- **Components:** write $u\sim_H v$ if $H$ contains a $u$-$v$ path. By Fact 0 below this is an equivalence relation. Its classes are the components of $H$, and $c(H)$ is their number. Since $V(H)\ne\emptyset$, we have $c(H)\ge 1$, and $H$ is connected iff $c(H)=1$.

## Proof idea

Build $G$ from the edgeless graph on $V$ by inserting its edges one at a time. An inserted edge either merges two components, or has both endpoints in one component and is then called *redundant*. Counting components gives $c(G)=n-m+s$, where $s$ is the number of redundant edges, and $s=0$ holds exactly when $G$ is acyclic. All three implications follow from this one identity.

## Proof

**Fact 0.** If $H$ contains a $u$-$v$ walk, then it contains a $u$-$v$ path. Consequently, $\sim_H$ is an equivalence relation.

*Proof.* Take a $u$-$v$ walk $x_0,\dots,x_\ell$ of minimum length. If $x_i=x_j$ with $i<j$, then $x_0,\dots,x_i,x_{j+1},\dots,x_\ell$ is a shorter $u$-$v$ walk, a contradiction. So this walk is a path. The relation $\sim_H$ is reflexive by walks of length $0$, symmetric by reversal, and transitive by concatenating walks and applying the first part. $\square$

---

**Setup.** Enumerate the edges of $G$ as $e_1,\dots,e_m$, with $e_i=x_iy_i$. For $0\le i\le m$ let $H_i=(V,\{e_1,\dots,e_i\})$. Thus $H_0$ is edgeless, $H_m=G$, and $c(H_0)=n$ because in $H_0$ every path has length $0$. Call an index $i\in\{1,\dots,m\}$ **redundant** if $x_i\sim_{H_{i-1}}y_i$, and let $s\ge 0$ be the number of redundant indices.

**Lemma.**

1. $c(G)=n-m+s$.
2. $s=0$ if and only if $G$ is acyclic.

*Proof of 1.* Fix $i\in\{1,\dots,m\}$, and let $A,B$ be the components of $H_{i-1}$ containing $x_i,y_i$ respectively. Let $\mathcal P$ be the partition of $V$ obtained from the components of $H_{i-1}$ by replacing $A$ and $B$ with the single block $A\cup B$ (nothing changes if $A=B$). We show that $\mathcal P$ is the set of components of $H_i$.

- *Two vertices in one block are joined in $H_i$.* If they lie in one component of $H_{i-1}$, this holds because $H_{i-1}\subseteq H_i$. If $a\in A$ and $b\in B$, then $a\sim_{H_i}x_i$, $x_i\sim_{H_i}y_i$ and $y_i\sim_{H_i}b$, so $a\sim_{H_i}b$ by transitivity.
- *Two vertices joined in $H_i$ lie in one block.* Both endpoints of every edge of $H_i$ lie in one block: for $e_1,\dots,e_{i-1}$ this is a component of $H_{i-1}$, and for $e_i$ it is $A\cup B$. Hence all vertices of a path in $H_i$ lie in one block.

Index $i$ is redundant iff $A=B$. So $c(H_i)=c(H_{i-1})$ if $i$ is redundant, and $c(H_i)=c(H_{i-1})-1$ otherwise. Of the $m$ indices, $m-s$ are not redundant, so $c(G)=c(H_0)-(m-s)=n-m+s$.

*Proof of 2.* Suppose first that some index $i$ is redundant, and let $P$ be an $x_i$-$y_i$ path in $H_{i-1}$. Since $x_i\ne y_i$, $P$ has length at least $1$. It does not have length $1$, because that would mean $x_iy_i=e_i\in E(H_{i-1})$. So $P$ has at least $3$ vertices, and these vertices together with the closing edge $e_i$ form a cycle in $G$. Thus $G$ is not acyclic.

Conversely, suppose $G$ contains a cycle, and let $e_i$ be the edge of this cycle with the largest index. Rotating the cycle if necessary, we may write it as $v_1,\dots,v_k$ with $e_i=v_kv_1$: if $e_i=v_jv_{j+1}$ with $j<k$, use $v_{j+1},\dots,v_k,v_1,\dots,v_j$, which is a cycle with the same edges and closing edge $v_jv_{j+1}$. For $1\le t<k$, we have $v_tv_{t+1}\ne v_kv_1$, since $\{t,t+1\}=\{1,k\}$ would force $k=2$. So each $v_tv_{t+1}$ is an edge of the cycle other than $e_i$, has index less than $i$, and lies in $H_{i-1}$. Hence $v_1,\dots,v_k$ is a path in $H_{i-1}$ joining the endpoints of $e_i$, so $i$ is redundant and $s\ge 1$. $\square$

---

**Proof of the Theorem.** We prove (a) ⇒ (b) ⇒ (c) ⇒ (a), using the identity $c(G)=n-m+s$ from part 1 of the Lemma.

**(a) ⇒ (b).** If $G$ is connected and acyclic, then $c(G)=1$ and $s=0$ by part 2. So $1=n-m$, i.e. $m=n-1$.

**(b) ⇒ (c).** If $G$ is connected with $m=n-1$, then $1=c(G)=n-(n-1)+s=1+s$. So $s=0$, and $G$ is acyclic by part 2.

**(c) ⇒ (a).** If $G$ is acyclic with $m=n-1$, then $s=0$ by part 2, so $c(G)=n-(n-1)+0=1$. Thus $G$ is connected, and it is acyclic by hypothesis. $\blacksquare$

## Remarks

- **The edge count alone is not sufficient.** The disjoint union of a triangle and an isolated vertex has $n=4$ and $m=3=n-1$, but it is neither connected nor acyclic. Here $s=1$ and $c=2$, in agreement with the identity.
- **Connectedness alone is not sufficient.** The triangle $C_3$ is connected, but $m=3\ne 2$.
- **Acyclicity alone is not sufficient.** The edgeless graph on two vertices is acyclic, but $m=0\ne 1$.
- **Smallest case.** For $n=1$, the graph has no edges (it is simple), so $m=s=0$ and $c=1$, and (a), (b), (c) all hold.
- **Cited results.** The proof uses only the well-ordering principle and a finite count; every auxiliary statement is proved above.
