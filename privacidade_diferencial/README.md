### Atingindo a definição para "amostra_media_com_ruido_laplaciano"

\(D = [10,12,11,13,12,10]\) e \(D'\ =) \(D\) menos um elemento.

\(U = [0,20]\).

F = média

\(f(D) = \frac{\sum D}{|D|}\)

\(f(D) = \frac{10+12+11+13+12+10}{6} = \frac{68}{6} \approx 11.33\)

---

#### Sensibilidade Global

A sensibilidade global de F é:

\(\Delta f = \max_{D,D'} |f(D)-f(D')|\)

Para |D| = 6 e U = \([0,20]\):

\(\Delta f = \frac{20-0}{6} = \frac{20}{6} = \frac{10}{3} \approx 3.33\)

---

#### Mecanismo de Laplace

\(M(D)=f(D)+\text{Lap}(0,b)\)

onde:

\(b=\frac{\Delta f}{\varepsilon}\)

\(\varepsilon = 1\), temos:

\(b=\frac{10/3}{1}=\frac{10}{3}\)

---

#### Distribuição de Probabilidade

Usando a densidade da distribuição de Laplace: 

\(p_D(y)=\frac{1}{2b}\exp\left(-\frac{|y-f(D)|}{b}\right)\)

e analogamente para \(D'\):

\(p_{D'}(y)=\frac{1}{2b}\exp\left(-\frac{|y-f(D')|}{b}\right)\)

---

#### Razão entre as distribuições

Analisando a razão:

\(\frac{p_D(y)}{p_{D'}(y)}\)

obtemos:

\[
\frac{
\frac{1}{2b}e^{-\frac{|y-f(D)|}{b}}
}{
\frac{1}{2b}e^{-\frac{|y-f(D')|}{b}}
}
=
e^{
\frac{
-|y-f(D)|+|y-f(D')|
}{b}
}
\]

Pela desigualdade triangular:

\(|y-f(D')|-|y-f(D)| \le |f(D)-f(D')|\)

Logo:

\[
\frac{p_D(y)}{p_{D'}(y)}
\le
e^{\frac{|f(D)-f(D')|}{b}}
\]

Como:

\(|f(D)-f(D')| \le \Delta f\)

e

\(b=\frac{\Delta f}{\varepsilon}\)

temos:

\[
\frac{p_D(y)}{p_{D'}(y)}
\le
e^{\frac{\Delta f}{\Delta f/\varepsilon}}
=
e^\varepsilon
\]

Portanto:

\(\Pr[M(D)\in S] \le e^\varepsilon \Pr[M(D')\in S]\)

para qualquer conjunto \(S\).