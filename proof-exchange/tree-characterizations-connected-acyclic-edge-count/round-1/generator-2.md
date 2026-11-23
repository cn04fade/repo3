# Round 1, generator 2

STATUS: PROVEN
CLAIM: C2. Let $H$ be a connected graph, let $C$ be a cycle in $H$, and let $e$ be an edge of $C$. Then $H-e$ is connected.
USED: Fact F0 (a $u$-$v$ walk yields a $u$-$v$ path), applied in the graph $H-e$. No proven claims and no other theorems.

## Proof

Throughout, $H-e=(V(H),E(H)\setminus\{e\})$, so $H-e$ has the same nonempty vertex set as $H$. It is a finite simple graph, so F0 applies to it.

**Setup.** Let $C$ be given by the pairwise distinct vertices $v_1,\dots,v_k$, where $k\ge 3$, with $v_iv_{i+1}\in E(H)$ for $1\le i<k$ and $v_kv_1\in E(H)$.

For an integer $i$, let $\sigma(i)\in\{1,\dots,k\}$ be the unique element with $\sigma(i)\equiv i \pmod k$. For every integer $i$,
$$
v_{\sigma(i)}v_{\sigma(i+1)}\in E(H). \tag{1}
$$
Indeed, if $\sigma(i)=r<k$, then $\sigma(i+1)=r+1$ and the edge is $v_rv_{r+1}$. If $\sigma(i)=k$, then $\sigma(i+1)=1$ and the edge is the closing edge $v_kv_1$.

The edges of $C$ are exactly the edges $v_jv_{\sigma(j+1)}$ with $j\in\{1,\dots,k\}$. Hence there is $j\in\{1,\dots,k\}$ with
$$
e=v_jv_{\sigma(j+1)}.
$$
The case $j=k$ is the case where $e$ is the closing edge $v_kv_1$.

**Step 1: the rest of the cycle is a walk in $H-e$ joining the endpoints of $e$.** Define
$$
u_t:=v_{\sigma(j+1+t)}\qquad (0\le t\le k-1).
$$
We record three properties.

1. *The $u_t$ are pairwise distinct.* The integers $j+1,\dots,j+k$ are $k$ consecutive integers, so they are pairwise incongruent modulo $k$. Thus their $\sigma$-values are pairwise distinct, and $v_1,\dots,v_k$ are pairwise distinct.

2. *The endpoints are those of $e$.* We have $u_0=v_{\sigma(j+1)}$ and $u_{k-1}=v_{\sigma(j+k)}=v_{\sigma(j)}=v_j$. Hence $e=u_0u_{k-1}$. Write $a:=u_0$ and $b:=u_{k-1}$, so $e=ab$.

3. *Consecutive vertices are adjacent in $H-e$.* Let $1\le t\le k-1$. By (1) with $i=j+t$, we have $u_{t-1}u_t\in E(H)$. Suppose $u_{t-1}u_t=e=u_0u_{k-1}$. Then $\{u_{t-1},u_t\}=\{u_0,u_{k-1}\}$, and since the $u_s$ are pairwise distinct, $\{t-1,t\}=\{0,k-1\}$. The smaller elements agree, so $t-1=0$, and the larger elements agree, so $t=k-1$. Thus $k=2$, contradicting $k\ge 3$. Therefore $u_{t-1}u_t\in E(H)\setminus\{e\}=E(H-e)$.

Consequently,
$$
W:=u_0,u_1,\dots,u_{k-1}
$$
is an $a$-$b$ walk in $H-e$, and its reversal $W^{-1}:=u_{k-1},\dots,u_0$ is a $b$-$a$ walk in $H-e$.

**Step 2: every edge of $H$ can be replaced by a walk in $H-e$.** Let $p,q$ be vertices with $pq\in E(H)$. We show that $H-e$ contains a $p$-$q$ walk.

- If $pq\ne e$, then $pq\in E(H-e)$, and $p,q$ is such a walk.
- If $pq=e=ab$, then $(p,q)=(a,b)$ or $(p,q)=(b,a)$. In the first case $W$ is such a walk, and in the second case $W^{-1}$ is such a walk.

These cases are exhaustive.

**Step 3: $H-e$ is connected.** Let $x,y\in V(H-e)=V(H)$. Since $H$ is connected, $H$ contains an $x$-$y$ path $x_0,x_1,\dots,x_\ell$ with $x_0=x$, $x_\ell=y$ and $\ell\ge 0$.

We show by induction on $i\in\{0,\dots,\ell\}$ that $H-e$ contains an $x_0$-$x_i$ walk.

- *Base case $i=0$.* The sequence $x_0$ is a walk of length $0$ in $H-e$.
- *Induction step.* Let $1\le i\le \ell$ and suppose $R$ is an $x_0$-$x_{i-1}$ walk in $H-e$. Since $x_{i-1}x_i\in E(H)$, Step 2 gives an $x_{i-1}$-$x_i$ walk $R'$ in $H-e$. Writing $R$ followed by $R'$, with the common vertex $x_{i-1}$ listed once, gives an $x_0$-$x_i$ walk in $H-e$.

For $i=\ell$, this gives an $x$-$y$ walk in $H-e$. By F0 applied to $H-e$, there is an $x$-$y$ path in $H-e$. Since $x,y$ were arbitrary, $H-e$ is connected. $\blacksquare$

**Check on a small example.** Let $H=K_3$ with $C=v_1,v_2,v_3$ and $e=v_3v_1$, so $j=3$. Then $u_0,u_1,u_2=v_1,v_2,v_3$, which uses the edges $v_1v_2,v_2v_3\ne e$. For $e=v_1v_2$, so $j=1$, we get $u_0,u_1,u_2=v_2,v_3,v_1$, which uses $v_2v_3,v_3v_1\ne e$. In both cases $H-e$ is a path on three vertices, hence connected.

## Gap

none

## Attempts

- Direct proof by rerouting an $x$-$y$ path along the rest of the cycle: succeeded. Cyclic indexing treats the closing edge and the other cycle edges uniformly.
- Self-review checklist: the exact claim is proven; connectivity of $H$ is used in Step 3; the cycle hypothesis is used in Step 1, with $k\ge 3$ needed to show that $W$ avoids $e$; the case distinctions are exhaustive; $x=y$ is covered by $\ell=0$; there is no induction on graph size and no "without loss of generality"; only F0 is cited, and it is applied in $H-e$.

## Suggested next claims

none
