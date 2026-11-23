# Round 1, generator 3

STATUS: PROVEN
CLAIM: C3. Every connected graph $H$ with $n(H)\ge 1$ vertices satisfies $m(H)\ge n(H)-1$.
USED: Induction on a finite range of integers and the definitions in `round-1/claims.md`. No proven claims and no facts about trees are used. F0 is permitted but not needed, because the definition of connectedness directly provides a path.

## Proof

Let $H$ be a connected graph, and write $V=V(H)$, $E=E(H)$, $n=n(H)\ge 1$, $m=m(H)$.

For $k\in\{1,\dots,n\}$, call a sequence $w_1,\dots,w_k$ of vertices together with integers $p(2),\dots,p(k)$ a **growing sequence of length $k$** if

1. $w_1,\dots,w_k$ are pairwise distinct, and
2. for every $i$ with $2\le i\le k$, we have $1\le p(i)<i$ and $w_iw_{p(i)}\in E$.

For $k=1$, there are no integers $p(i)$ and condition 2 is vacuous.

**Step 1: A growing sequence of length $n$ exists.** We prove by induction on $k$ that for every $k\in\{1,\dots,n\}$ there is a growing sequence of length $k$.

*Base case $k=1$.* Since $V\neq\emptyset$, we may choose a vertex $w_1\in V$. The one-term sequence $w_1$ satisfies conditions 1 and 2.

*Induction hypothesis.* Let $k$ be an integer with $1\le k<n$, and suppose $w_1,\dots,w_k$ with $p(2),\dots,p(k)$ is a growing sequence of length $k$.

*Induction step.* Put $S=\{w_1,\dots,w_k\}$. By condition 1, $|S|=k<n=|V|$, so there is a vertex $y\in V\setminus S$. Also $w_1\in S$, so $w_1\ne y$. Since $H$ is connected, there is a $w_1$-$y$ path
$$x_0,x_1,\dots,x_\ell,\qquad x_0=w_1,\quad x_\ell=y.$$
The set $\{t\in\{0,\dots,\ell\}: x_t\notin S\}$ contains $\ell$, so it is nonempty. Let $j$ be its least element. Since $x_0=w_1\in S$, we have $j\ge 1$. By minimality of $j$, $x_{j-1}\in S$, so $x_{j-1}=w_q$ for some $q\in\{1,\dots,k\}$. Because $x_0,\dots,x_\ell$ is a walk, $x_{j-1}x_j\in E$.

Define
$$w_{k+1}=x_j,\qquad p(k+1)=q.$$
Then $w_{k+1}\notin S$, so $w_1,\dots,w_{k+1}$ are pairwise distinct. Moreover, $1\le p(k+1)=q\le k<k+1$ and $w_{k+1}w_{p(k+1)}=x_jx_{j-1}\in E$. Condition 2 for indices $i\le k$ holds by the induction hypothesis. Thus we have a growing sequence of length $k+1$.

This completes the induction. In particular, there is a growing sequence $w_1,\dots,w_n$ with integers $p(2),\dots,p(n)$.

**Step 2: The edges $f_i=w_iw_{p(i)}$, $2\le i\le n$, are pairwise distinct.** By condition 2, each $f_i$ belongs to $E$. Suppose, for contradiction, that $f_i=f_j$ for some $2\le i<j\le n$. An undirected edge is determined by its set of endpoints, so
$$\{w_i,w_{p(i)}\}=\{w_j,w_{p(j)}\}.$$
Hence $w_j\in\{w_i,w_{p(i)}\}$. But $p(i)<i<j$, so both $i$ and $p(i)$ are indices different from $j$. By condition 1, $w_j\ne w_i$ and $w_j\ne w_{p(i)}$, a contradiction.

**Step 3: Conclusion.** The set $\{f_i:2\le i\le n\}\subseteq E$ has exactly $n-1$ elements by Step 2. (If $n=1$, this set is empty, and the bound reads $m\ge 0$.) Therefore
$$m=|E|\ge n-1. \qquad\blacksquare$$

## Gap

none

## Attempts

- Growing-set construction with a first-exit vertex on a path (direct construction, induction on $k$): succeeded; this is the proof above.
- Leaf removal: not used, as the assignment directs, because a connected graph need not have a leaf (for example $C_3$).
- Self-review checklist: the statement proved is exactly C3. Connectedness is used in the induction step, and it is necessary: two isolated vertices have $n=2$, $m=0$. The hypothesis $n\ge 1$ is used in the base case. The case $n=1$ is handled in Step 3. There is no circularity and no cited fact about trees. The only case split in Step 2 is the two possible values $w_i,w_{p(i)}$, and both are excluded.
- Small-case check: for the path $a,b,c$ with $w_1=a$, the construction gives $w_2=b$, $p(2)=1$, $w_3=c$, $p(3)=2$, with distinct edges $ab,bc$, so $m=2=n-1$ (the bound is tight). For $K_3$ on $a,b,c$ with $w_1=a$, a possible outcome is $w_2=b$, $p(2)=1$, $w_3=c$, $p(3)=1$, with distinct edges $ab,ac$, so $m=3\ge 2$.

## Suggested next claims

none
