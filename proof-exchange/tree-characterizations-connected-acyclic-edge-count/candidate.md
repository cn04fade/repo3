# Three equivalent characterizations of trees

**Status:** Proven, awaiting independent review
**Date:** 2026-11-23
**Reviewed by:** supervisor check; proof-reviewer pending

## Problem

Let G be a finite simple undirected graph with n >= 1 vertices. Prove that the following are equivalent: (a) G is a tree (connected and acyclic); (b) G is connected and has exactly n-1 edges; (c) G is acyclic and has exactly n-1 edges.

## Formal statement

**Theorem.** Let $G=(V,E)$ be a finite simple undirected graph with $n=|V|\ge 1$ vertices and $m=|E|$ edges. The following are equivalent:

- (a) $G$ is connected and acyclic;
- (b) $G$ is connected and $m=n-1$;
- (c) $G$ is acyclic and $m=n-1$.

## Definitions and conventions

All graphs are finite, simple and undirected, with a nonempty vertex set. For a graph $H$, write $n(H)=|V(H)|$ and $m(H)=|E(H)|$. An edge with endpoints $u,v$ is written $uv=vu$.

- **Walk:** a sequence $x_0,\dots,x_\ell$ of vertices ($\ell\ge 0$) with $x_{i-1}x_i\in E(H)$ for $1\le i\le\ell$. It is an $x_0$-$x_\ell$ walk of length $\ell$.
- **Path:** a walk whose vertices are pairwise distinct.
- **Cycle:** a sequence $v_1,\dots,v_k$ of $k\ge 3$ pairwise distinct vertices with $v_iv_{i+1}\in E(H)$ for $1\le i<k$ and $v_kv_1\in E(H)$. Its edges are these $k$ edges.
- **Acyclic:** containing no cycle.
- **Connected:** any two vertices $u,v$ are joined by a $u$-$v$ path. In particular, the one-vertex graph is connected and acyclic.
- **Components:** write $u\sim_H v$ if $H$ contains a $u$-$v$ path. By Fact 0 below this is an equivalence relation. Its number of classes is denoted $c(H)$. Since $V(H)\ne\emptyset$, we have $c(H)\ge 1$, and $H$ is connected iff $c(H)=1$.
- **Deletion:** $H-e=(V(H),E(H)\setminus\{e\})$ keeps all vertices. $H-v$ is obtained by removing the vertex $v$ and all edges incident with it.

## Proof idea

Lemma 1 counts the edges of an acyclic graph by repeatedly removing a vertex of degree $1$. Lemma 2 says that deleting an edge of a cycle does not disconnect a graph. Lemma 3 says that a connected graph needs at least $n-1$ edges. Lemma 1 gives (a) ⇒ (b) and (c) ⇒ (a). For (b) ⇒ (c), a cycle would allow us to delete an edge and stay connected with only $n-2$ edges, which Lemma 3 forbids.

## Proof

**Fact 0.** If $H$ contains a $u$-$v$ walk, then it contains a $u$-$v$ path. Consequently, $\sim_H$ is an equivalence relation.

*Proof.* Take a $u$-$v$ walk $x_0,\dots,x_\ell$ of minimum length. If $x_i=x_j$ with $i<j$, then $x_0,\dots,x_i,x_{j+1},\dots,x_\ell$ is a shorter $u$-$v$ walk, a contradiction. So this walk is a path. The relation $\sim_H$ is reflexive by walks of length $0$, symmetric by reversal, and transitive by concatenating walks and applying the first part. $\square$

---

**Lemma 1.** If $H$ is an acyclic graph, then $m(H)=n(H)-c(H)$.

*Proof.* We use induction on $k=m(H)$, for all acyclic graphs simultaneously.

*Base case $k=0$.* Since $H$ has no edges, every path has length $0$, so $u\sim_H v$ iff $u=v$. Thus $c(H)=n(H)$, and $m(H)=0=n(H)-c(H)$.

*Induction step.* Let $k\ge 1$. Assume the statement holds for every acyclic graph with $k-1$ edges, and let $H$ be acyclic with $m(H)=k$.

*Step 1: $H$ has a vertex of degree exactly $1$.* Since $H$ has an edge and no loops, it has a path of length at least $1$. Every path has length at most $n(H)-1$, so there is a path $x_0,x_1,\dots,x_\ell$ of maximum length, and $\ell\ge 1$. Put $v=x_0$ and $u=x_1$. Suppose that $v$ has a neighbour $w\ne u$. Since $H$ has no loops, $w\ne x_0$, so one of two cases holds.

- If $w\notin\{x_0,\dots,x_\ell\}$, then $w,x_0,\dots,x_\ell$ is a path of length $\ell+1$, contradicting maximality.
- Otherwise $w=x_j$ for some $2\le j\le\ell$. Then $x_0,\dots,x_j$ are $j+1\ge 3$ pairwise distinct vertices, consecutive ones are adjacent, and $x_jx_0=wv\in E(H)$. This is a cycle, contradicting acyclicity.

Hence $u$ is the only neighbour of $v$, and $uv$ is the only edge incident with $v$.

*Step 2: the graph $H'=H-v$ satisfies the induction hypothesis.* Its vertex set contains $u$, so it is nonempty, and $n(H')=n(H)-1$. By Step 1, exactly one edge is removed, so $m(H')=k-1$. Every cycle of $H'$ is a cycle of $H$, so $H'$ is acyclic.

*Step 3: $c(H')=c(H)$.* Let $[x]'$ and $[x]$ denote the classes of $x\in V(H')$ under $\sim_{H'}$ and $\sim_H$. Define $\Phi([x]')=[x]$.

- *$\Phi$ is well defined,* because a path in $H'$ is also a path in $H$.
- *$\Phi$ is surjective.* Let $K$ be a class of $\sim_H$. If $v\notin K$, any element of $K$ lies in $V(H')$. If $v\in K$, then $u\in K$ because $v,u$ is a path, and $u\in V(H')$. In both cases $K=[x]=\Phi([x]')$ for some $x\in V(H')$.
- *$\Phi$ is injective.* Let $x,y\in V(H')$ with $[x]=[y]$, and let $z_0,\dots,z_r$ be an $x$-$y$ path in $H$. Suppose $z_i=v$. Since $x\ne v\ne y$, we have $0<i<r$, so $z_{i-1}$ and $z_{i+1}$ are neighbours of $v$. By Step 1, $z_{i-1}=u=z_{i+1}$, contradicting that path vertices are pairwise distinct. So the path avoids $v$, all its edges lie in $H'$, and $[x]'=[y]'$.

*Step 4: conclusion.* By the induction hypothesis, $m(H')=n(H')-c(H')$. Substituting Steps 2 and 3 gives $m(H)-1=n(H)-1-c(H)$, i.e. $m(H)=n(H)-c(H)$. $\square$

---

**Lemma 2.** Let $H$ be connected, let $C$ be a cycle in $H$, and let $e$ be an edge of $C$. Then $H-e$ is connected.

*Proof.* Let $C$ be $v_1,\dots,v_k$, where $k\ge 3$. For an integer $i$, let $\sigma(i)\in\{1,\dots,k\}$ be the unique element with $\sigma(i)\equiv i\pmod k$. For every integer $i$,
$$v_{\sigma(i)}v_{\sigma(i+1)}\in E(H), \tag{1}$$
since this is $v_rv_{r+1}$ if $\sigma(i)=r<k$, and the closing edge $v_kv_1$ if $\sigma(i)=k$. The edges of $C$ are the edges $v_jv_{\sigma(j+1)}$ with $1\le j\le k$, so $e=v_jv_{\sigma(j+1)}$ for some $j$.

*Step 1: the rest of the cycle joins the endpoints of $e$ in $H-e$.* Put
$$u_t=v_{\sigma(j+1+t)}\qquad(0\le t\le k-1).$$
The integers $j+1,\dots,j+k$ are pairwise incongruent modulo $k$, so the $u_t$ are pairwise distinct. Moreover $u_0=v_{\sigma(j+1)}$ and $u_{k-1}=v_{\sigma(j+k)}=v_j$, so $e=u_0u_{k-1}$.

Let $1\le t\le k-1$. By (1) with $i=j+t$, we have $u_{t-1}u_t\in E(H)$. If $u_{t-1}u_t=e=u_0u_{k-1}$, then distinctness of the $u_s$ gives $\{t-1,t\}=\{0,k-1\}$, hence $t-1=0$ and $t=k-1$, so $k=2$. This contradicts $k\ge 3$. Therefore $W=u_0,u_1,\dots,u_{k-1}$ is a walk in $H-e$ from one endpoint of $e$ to the other, and its reversal $W^{-1}$ is a walk in $H-e$ in the opposite direction.

*Step 2: every edge can be replaced.* Let $pq\in E(H)$. If $pq\ne e$, then $p,q$ is a $p$-$q$ walk in $H-e$. If $pq=e$, then $(p,q)=(u_0,u_{k-1})$ or $(p,q)=(u_{k-1},u_0)$, and $W$ or $W^{-1}$ respectively is a $p$-$q$ walk in $H-e$.

*Step 3: connectivity.* Let $x,y\in V(H-e)=V(H)$. Since $H$ is connected, it contains an $x$-$y$ path $x_0,\dots,x_\ell$. We show by induction on $i$ that $H-e$ contains an $x_0$-$x_i$ walk. For $i=0$, take the walk $x_0$. For $1\le i\le\ell$, append to an $x_0$-$x_{i-1}$ walk the $x_{i-1}$-$x_i$ walk from Step 2. For $i=\ell$ this is an $x$-$y$ walk in $H-e$, and Fact 0 gives an $x$-$y$ path in $H-e$. $\square$

---

**Lemma 3.** Every connected graph $H$ satisfies $m(H)\ge n(H)-1$.

*Proof.* Write $N=n(H)$. For $1\le k\le N$, a *growing sequence of length $k$* consists of pairwise distinct vertices $w_1,\dots,w_k$ and integers $p(2),\dots,p(k)$ such that $1\le p(i)<i$ and $w_iw_{p(i)}\in E(H)$ for $2\le i\le k$.

*Step 1: a growing sequence of length $N$ exists.* We use induction on $k$. For $k=1$, choose any vertex $w_1$. Now let $1\le k<N$, take a growing sequence of length $k$, and put $S=\{w_1,\dots,w_k\}$. Since $|S|=k<N$, there is a vertex $y\in V(H)\setminus S$. As $H$ is connected, there is a $w_1$-$y$ path $x_0,\dots,x_\ell$. Let $j$ be the least index with $x_j\notin S$; it exists because $x_\ell=y\notin S$, and $j\ge 1$ because $x_0=w_1\in S$. Then $x_{j-1}=w_q$ for some $q\in\{1,\dots,k\}$, and $x_{j-1}x_j\in E(H)$. Setting $w_{k+1}=x_j$ and $p(k+1)=q$ gives a growing sequence of length $k+1$.

*Step 2: the edges $f_i=w_iw_{p(i)}$, $2\le i\le N$, are pairwise distinct.* Suppose $f_i=f_j$ with $i<j$. Then $w_j\in\{w_i,w_{p(i)}\}$. Since $p(i)<i<j$, both indices differ from $j$, contradicting that the $w$'s are pairwise distinct.

*Step 3.* Thus $E(H)$ contains the $N-1$ distinct edges $f_2,\dots,f_N$, so $m(H)\ge N-1$. (For $N=1$ the bound reads $m(H)\ge 0$.) $\square$

---

**Proof of the Theorem.** We prove (a) ⇒ (b) ⇒ (c) ⇒ (a).

**(a) ⇒ (b).** Let $G$ be connected and acyclic. Then $c(G)=1$, and Lemma 1 gives $m=n-c(G)=n-1$. So $G$ is connected with $n-1$ edges.

**(b) ⇒ (c).** Let $G$ be connected with $m=n-1$. Suppose, for contradiction, that $G$ contains a cycle $C$, and let $e$ be an edge of $C$. By Lemma 2, $G-e$ is connected. It has $n$ vertices and $m-1=n-2$ edges. Lemma 3 applied to $G-e$ gives $n-2\ge n-1$, a contradiction. Hence $G$ is acyclic, and $m=n-1$ by hypothesis.

**(c) ⇒ (a).** Let $G$ be acyclic with $m=n-1$. Lemma 1 gives $n-1=m=n-c(G)$, so $c(G)=1$. Thus $G$ is connected, and it is acyclic by hypothesis. $\blacksquare$

## Remarks

- **The edge count alone is not sufficient.** The disjoint union of a triangle and an isolated vertex has $n=4$ and $m=3=n-1$, but it is neither connected nor acyclic.
- **Connectedness alone is not sufficient.** The triangle $C_3$ is connected, but $m=3\ne 2$.
- **Acyclicity alone is not sufficient.** The edgeless graph on two vertices is acyclic, but $m=0\ne 1$.
- **Smallest case.** For $n=1$, the graph has no edges (it is simple), and (a), (b), (c) all hold.
- **Cited results.** The proof uses only induction and the well-ordering principle; every auxiliary statement is proved above.
