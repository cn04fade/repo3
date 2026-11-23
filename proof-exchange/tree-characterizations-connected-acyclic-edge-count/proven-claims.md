# Proven claims

Conventions are those of `round-1/claims.md`: graphs are finite, simple, undirected, with nonempty vertex set; $n(H)=|V(H)|$, $m(H)=|E(H)|$; $c(H)$ is the number of classes of the relation $u\sim_H v$ :⇔ there is a $u$-$v$ path in $H$.

## F0 (walks yield paths)

**Statement.** If there is a $u$-$v$ walk, then there is a $u$-$v$ path. Consequently, $\sim_H$ is an equivalence relation.

**Proof.** Take a $u$-$v$ walk $x_0,\dots,x_\ell$ of minimum length. If $x_i=x_j$ with $i<j$, then $x_0,\dots,x_i,x_{j+1},\dots,x_\ell$ is a shorter $u$-$v$ walk, a contradiction. So the walk is a path. Reflexivity follows from length-$0$ walks, symmetry from reversal, and transitivity from concatenating walks and applying the first part. $\blacksquare$

## C1 (round 1, generator 1)

**Statement.** If $H$ is acyclic with $n(H)\ge 1$, then $m(H)=n(H)-c(H)$.

**Dependencies.** F0, induction.

**Proof.** We use induction on $k=m(H)$, over all acyclic graphs simultaneously.

*Base case $k=0$.* Without edges, every path has length $0$, so $u\sim_H v$ iff $u=v$. Thus $c(H)=n(H)$ and $m(H)=0=n(H)-c(H)$.

*Induction step.* Let $k\ge 1$, assume the statement for all acyclic graphs with $k-1$ edges, and let $H$ be acyclic with $m(H)=k$.

*Step 1: $H$ has a vertex of degree exactly $1$.* Since $H$ has an edge and no loops, it has a path of length at least $1$. Path lengths are at most $n(H)-1$, so there is a path $x_0,x_1,\dots,x_\ell$ of maximum length, and $\ell\ge 1$. Put $v=x_0$, $u=x_1$. Suppose $v$ has a neighbour $w\ne u$. Then $w\ne x_0$ since there are no loops.

- If $w\notin\{x_0,\dots,x_\ell\}$, then $w,x_0,\dots,x_\ell$ is a longer path, a contradiction.
- Otherwise $w=x_j$ with $2\le j\le\ell$. Then $x_0,\dots,x_j$ are $j+1\ge 3$ distinct vertices, consecutive ones are adjacent, and $x_jx_0\in E(H)$. This is a cycle, a contradiction.

Hence $u$ is the only neighbour of $v$.

*Step 2: $H'=H-v$ satisfies the induction hypothesis.* $V(H')$ contains $u$, so it is nonempty, and $n(H')=n(H)-1$. Exactly one edge, $uv$, is removed, so $m(H')=k-1$. Every cycle of $H'$ is a cycle of $H$, so $H'$ is acyclic.

*Step 3: $c(H')=c(H)$.* Define $\Phi([x]_{H'})=[x]_H$ for $x\in V(H')$.

- *Well defined:* a path in $H'$ is a path in $H$.
- *Surjective:* let $K$ be a class of $\sim_H$. If $v\notin K$, any element of $K$ lies in $V(H')$. If $v\in K$, then $u\in K$ because $v,u$ is a path, and $u\in V(H')$.
- *Injective:* let $x,y\in V(H')$ with $x\sim_H y$, and let $z_0,\dots,z_r$ be an $x$-$y$ path in $H$. If $z_i=v$, then $0<i<r$ since $x,y\ne v$, so $z_{i-1},z_{i+1}$ are neighbours of $v$. By Step 1 both equal $u$, contradicting distinctness of path vertices. So the path avoids $v$, hence lies in $H'$, and $x\sim_{H'}y$.

*Step 4.* By the induction hypothesis, $m(H')=n(H')-c(H')$, i.e. $m(H)-1=n(H)-1-c(H)$. Hence $m(H)=n(H)-c(H)$. $\blacksquare$

## C2 (round 1, generator 2)

**Statement.** If $H$ is connected, $C$ is a cycle in $H$ and $e$ is an edge of $C$, then $H-e$ is connected.

**Dependencies.** F0.

**Proof.** Let $C$ be $v_1,\dots,v_k$ with $k\ge 3$. For an integer $i$, let $\sigma(i)\in\{1,\dots,k\}$ be the unique element with $\sigma(i)\equiv i\pmod k$. Then $v_{\sigma(i)}v_{\sigma(i+1)}\in E(H)$ for every integer $i$: this is $v_rv_{r+1}$ if $\sigma(i)=r<k$, and the closing edge $v_kv_1$ if $\sigma(i)=k$. The edges of $C$ are the $v_jv_{\sigma(j+1)}$, $1\le j\le k$, so $e=v_jv_{\sigma(j+1)}$ for some $j$.

*Step 1.* Put $u_t=v_{\sigma(j+1+t)}$ for $0\le t\le k-1$. The integers $j+1,\dots,j+k$ are pairwise incongruent modulo $k$, so the $u_t$ are pairwise distinct. Also $u_0=v_{\sigma(j+1)}$ and $u_{k-1}=v_{\sigma(j+k)}=v_j$, so $e=u_0u_{k-1}$. For $1\le t\le k-1$ we have $u_{t-1}u_t\in E(H)$. If $u_{t-1}u_t=e$, then $\{t-1,t\}=\{0,k-1\}$ by distinctness, so $t-1=0$ and $t=k-1$, giving $k=2$, a contradiction. Hence $W=u_0,\dots,u_{k-1}$ is a walk in $H-e$ joining the endpoints of $e$, and so is its reversal in the opposite direction.

*Step 2.* For every $pq\in E(H)$ there is a $p$-$q$ walk in $H-e$: the walk $p,q$ if $pq\ne e$, and $W$ or its reversal if $pq=e$.

*Step 3.* Let $x,y\in V(H)$ and let $x_0,\dots,x_\ell$ be an $x$-$y$ path in $H$. Concatenating the walks from Step 2 for the pairs $x_{i-1},x_i$ (formally, by induction on $i$) gives an $x$-$y$ walk in $H-e$. By F0 there is an $x$-$y$ path in $H-e$. $\blacksquare$

## C3 (round 1, generator 3)

**Statement.** Every connected graph $H$ with $n(H)\ge 1$ satisfies $m(H)\ge n(H)-1$.

**Dependencies.** Induction.

**Proof.** Let $n=n(H)$. For $1\le k\le n$, a *growing sequence of length $k$* consists of pairwise distinct vertices $w_1,\dots,w_k$ and integers $p(2),\dots,p(k)$ with $1\le p(i)<i$ and $w_iw_{p(i)}\in E(H)$ for $2\le i\le k$.

*Step 1: one of length $n$ exists.* For $k=1$, choose any vertex. Let $1\le k<n$, take a growing sequence of length $k$, and put $S=\{w_1,\dots,w_k\}$. Since $|S|<n$, there is $y\in V(H)\setminus S$. Take a $w_1$-$y$ path $x_0,\dots,x_\ell$ and let $j$ be the least index with $x_j\notin S$; it exists because $x_\ell=y\notin S$, and $j\ge 1$ because $x_0\in S$. Then $x_{j-1}=w_q$ for some $q\le k$, and $x_{j-1}x_j\in E(H)$. Setting $w_{k+1}=x_j$, $p(k+1)=q$ gives a growing sequence of length $k+1$.

*Step 2: the edges $f_i=w_iw_{p(i)}$, $2\le i\le n$, are pairwise distinct.* If $f_i=f_j$ with $i<j$, then $w_j\in\{w_i,w_{p(i)}\}$. Since $p(i)<i<j$, this contradicts distinctness of the $w$'s.

*Step 3.* Thus $E(H)$ contains $n-1$ distinct edges, so $m(H)\ge n-1$. $\blacksquare$
