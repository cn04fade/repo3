# Round 1, generator 1

STATUS: PROVEN
CLAIM: C1. Let $H$ be an acyclic graph with $n(H)\ge 1$ vertices and $c(H)$ components. Then $m(H)=n(H)-c(H)$.
USED: Fact F0 is available but not needed beyond the fact, stated in `claims.md`, that $\sim$ is an equivalence relation. Induction on the number of edges. No proven claims and no theorems about trees or forests.

## Proof

Throughout, graphs are finite, simple and undirected with nonempty vertex set. For a graph $F$, write $\sim_F$ for the relation "there is a $u$-$v$ path in $F$". By F0 it is an equivalence relation, and $c(F)$ is its number of classes.

For an integer $k\ge 0$, let $P(k)$ be the statement:

> Every acyclic graph $H$ with $V(H)\ne\emptyset$ and $m(H)=k$ satisfies $m(H)=n(H)-c(H)$.

We prove $P(k)$ for all $k\ge 0$ by induction on $k$. This is exactly the claim.

### Base case $k=0$

Let $H$ have no edges. A walk of length $\ell\ge 1$ would use an edge, so every path in $H$ has length $0$. Hence $u\sim_H v$ if and only if $u=v$. Every class is a single vertex, so $c(H)=n(H)$, and
$$m(H)=0=n(H)-c(H).$$

### Induction step

Let $k\ge 1$ and assume $P(k-1)$. Let $H$ be an acyclic graph with $V(H)\neq\emptyset$ and $m(H)=k$. Write $n=n(H)$ and $m=m(H)=k$.

**Step 1: $H$ has a vertex of degree exactly $1$.**

Since $m\ge 1$, there is an edge $xy$, and $x\ne y$ because $H$ has no loops. Thus $x,y$ is a path of length $1$, so the set of paths of length at least $1$ is nonempty. The vertices of a path are pairwise distinct, so every path has length at most $n-1$. Therefore we may choose a path
$$x_0,x_1,\dots,x_\ell,\qquad \ell\ge 1,$$
of maximum length among all paths in $H$. Put $v=x_0$ and $u=x_1$. Then $u$ is a neighbour of $v$.

Suppose that $v$ has a neighbour $w\neq u$. Since $H$ has no loops, $w\ne x_0$. So exactly one of the following two cases holds.

- *Case $w\notin\{x_0,\dots,x_\ell\}$.* Then $w,x_0,x_1,\dots,x_\ell$ is a path of length $\ell+1$, contradicting the maximality of $\ell$.
- *Case $w=x_j$ for some $j$ with $2\le j\le \ell$.* (The values $j=0$ and $j=1$ are excluded by $w\ne x_0$ and $w\ne x_1$.) Then $x_0,x_1,\dots,x_j$ are $j+1\ge 3$ pairwise distinct vertices, $x_{i}x_{i+1}\in E(H)$ for $0\le i<j$, and the closing pair $x_jx_0=wv$ is an edge. This is a cycle in $H$, contradicting acyclicity.

Hence $u$ is the only neighbour of $v$, i.e. $\deg_H(v)=1$, and $uv$ is the only edge of $H$ incident with $v$.

**Step 2: $H'=H-v$ satisfies the hypotheses of $P(k-1)$.**

- $V(H')=V(H)\setminus\{v\}$ contains $u$ (as $u\ne v$), so it is nonempty, and $n(H')=n-1$.
- By Step 1, exactly one edge is removed, namely $uv$. So $m(H')=m-1=k-1$.
- Every cycle of $H'$ is, by the definition of a cycle, also a cycle of $H$, because $V(H')\subseteq V(H)$ and $E(H')\subseteq E(H)$. Since $H$ is acyclic, so is $H'$.

**Step 3: $c(H')=c(H)$.**

For $x\in V(H')$, let $[x]'$ be its class under $\sim_{H'}$ and $[x]$ its class under $\sim_H$. Define
$$\Phi:\{\text{classes of }\sim_{H'}\}\to\{\text{classes of }\sim_{H}\},\qquad \Phi([x]')=[x].$$

*$\Phi$ is well defined.* If $x\sim_{H'}y$, then an $x$-$y$ path in $H'$ is also an $x$-$y$ path in $H$, so $[x]=[y]$.

*$\Phi$ is surjective.* Let $K$ be a class of $\sim_H$. We show that $K$ contains a vertex $x\neq v$; then $K=[x]=\Phi([x]')$. If $v\notin K$, any element of the nonempty set $K$ works. If $v\in K$, then $u\in K$, because $v,u$ is a path in $H$, and $u\ne v$.

*$\Phi$ is injective.* Let $x,y\in V(H')$ with $[x]=[y]$, and let $z_0,z_1,\dots,z_r$ be an $x$-$y$ path in $H$, so $z_0=x$ and $z_r=y$. We first show that $v$ does not occur on this path. Suppose $z_i=v$. Since $x\ne v$ and $y\ne v$, we have $0<i<r$, so $z_{i-1}$ and $z_{i+1}$ both exist and both are neighbours of $v$. By Step 1, $z_{i-1}=u=z_{i+1}$. This contradicts the fact that the vertices of a path are pairwise distinct, since $i-1\neq i+1$.

So all $z_j$ lie in $V(H')$. Every edge $z_{j-1}z_j$ is an edge of $H$ with neither endpoint equal to $v$, hence an edge of $H'$. Thus $z_0,\dots,z_r$ is an $x$-$y$ path in $H'$, so $[x]'=[y]'$.

Therefore $\Phi$ is a bijection between two finite sets, and $c(H')=c(H)$.

**Step 4: Conclusion.**

By Step 2 we may apply $P(k-1)$ to $H'$:
$$m(H')=n(H')-c(H').$$
Using $m(H')=m-1$, $n(H')=n-1$ and $c(H')=c(H)$ from Steps 2 and 3, we get
$$m-1=(n-1)-c(H),\qquad\text{i.e.}\qquad m=n-c(H).$$
This proves $P(k)$. By induction, $P(k)$ holds for all $k\ge 0$. $\blacksquare$

### Self-review checklist

- **Exact statement:** $P(k)$ for all $k\ge0$ covers every acyclic graph with nonempty vertex set.
- **Hypotheses used:** acyclicity is used in the second case of Step 1 and inherited in Step 2. The condition $n(H)\ge 1$ keeps every graph in the induction within the stated class; Step 2 verifies it for $H'$.
- **Circularity:** no statement about trees, forests or edge counts is cited. The degree-$1$ vertex is proved to exist in Step 1.
- **Induction:** the step works from $k=1$. There $H'$ has no edges and is covered by the base case. $H'$ is nonempty because it contains $u$.
- **Case distinctions:** in Step 1, a neighbour $w\ne u$ is either off the path or equal to some $x_j$ with $j\ge 2$, since $w\neq x_0,x_1$. In surjectivity, either $v\notin K$ or $v\in K$.
- **Edge cases:** $K_1$ and edgeless graphs fall under the base case. Disconnected graphs are handled, since nothing assumes $c(H)=1$. For $H=K_2$, we get $v,u$ as the longest path and $H'=K_1$, with $1-1=2-1-1$.
- **Concrete check:** let $H$ have vertices $a,b,c,d$ and edges $ab,bc$. Then $n=4$, $m=2$, $c(H)=2$, and $2=4-2$. With longest path $a,b,c$ we get $v=a$, $u=b$. The graph $H'$ has vertices $b,c,d$ and edge $bc$, so $n(H')=3$, $m(H')=1$, $c(H')=2$, and $1=3-2$.

## Gap

none

## Attempts

- Induction on $m(H)$ with removal of a degree-$1$ vertex found from a longest path: succeeded; this is the proof above.

## Suggested next claims

none
