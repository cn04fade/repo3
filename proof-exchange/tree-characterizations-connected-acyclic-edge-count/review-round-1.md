# Review round 1: three equivalent characterizations of trees

## Issues

No CRITICAL, MINOR or STYLE issues were found.

## What was checked

**Correct target.** The formal statement matches `problem.md`: same graph class ($n\ge 1$, finite, simple, undirected) and same conditions (a), (b), (c). The cycle (a) ⇒ (b) ⇒ (c) ⇒ (a) gives all the equivalences. The definitions of path, cycle ($k\ge 3$), acyclic and connected are the standard ones for simple graphs.

**Fact 0.** Deleting $x_{i+1},\dots,x_j$ from a shortest walk is valid also when $j=\ell$, because $x_i=x_j$. The forward reference from the definition of components is not circular, since Fact 0 does not use $c(H)$.

**Lemma 1.**
- The induction is on the number of edges and goes from $k$ down to $k-1$. The hypothesis is stated for all acyclic graphs, including disconnected ones, so it applies to $H-v$.
- Step 1: the case split on $w$ is exhaustive, since $w\ne x_0$ (no loops) and $w\ne x_1$ leave only $w\notin\{x_0,\dots,x_\ell\}$ or $w=x_j$ with $j\ge 2$. The second case gives a cycle on $j+1\ge 3$ vertices.
- Step 2: $H-v$ is nonempty and acyclic, with exactly one vertex and one edge fewer.
- Step 3: $\Phi$ is well defined, surjective and injective. In the injectivity argument, $i-1\ne i+1$ gives the required contradiction, and the case $r=0$ is covered because $z_0=x\ne v$.

**Lemma 2.** The index computations are correct: $u_{t-1}=v_{\sigma(j+t)}$, $u_t=v_{\sigma(j+t+1)}$ and $u_{k-1}=v_{\sigma(j+k)}=v_j$ (as $1\le j\le k$). The edge $e$ is not used by $W$, because $\{t-1,t\}=\{0,k-1\}$ forces $k=2$. The hypothesis $k\ge 3$ is used exactly here.

**Lemma 3.** The growing sequence extends correctly: the first vertex outside $S$ on a path from $w_1$ has its predecessor in $S$. The edges $f_i$ are distinct because $w_j$ is an endpoint of $f_j$ but not of $f_i$ when $i<j$. The case $N=1$ is handled.

**Main proof.** Each implication applies the lemmas with their hypotheses satisfied. In (b) ⇒ (c), $e\in E(G)$, so $G-e$ has exactly $m-1=n-2$ edges, and it is connected with a nonempty vertex set.

**Hypotheses and circularity.** Simplicity (no loops) is used in Lemma 1, Step 1. Finiteness gives the maximum path and the induction. $n\ge 1$ gives $c(H)\ge 1$ and the vertex $w_1$. No lemma assumes any of the equivalences.

**Edge cases and sanity checks.**
- $n=1$: $m=0$, $c=1$, and (a), (b), (c) all hold.
- $P_3$ with vertices $a,b,c$: Lemma 1 removes the leaf $a$, leaving $P_2$, and $m=2=3-1$.
- $P_2+K_1$: $n=3$, $m=1$, $c=2$. Removing a leaf leaves two isolated vertices, so $c$ is unchanged.
- $C_4$ with $e=v_4v_1$ (so $j=4$): $u_0,\dots,u_3=v_1,v_2,v_3,v_4$, a path avoiding $e$.
- The three examples in the Remarks are correct.

VERDICT: ACCEPT
