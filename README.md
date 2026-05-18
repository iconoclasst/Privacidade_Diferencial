# Anotações sobre privacidade diferencial  

## Privacidade  

Privacidade de dados é diferente de segurança de dados. Técnicas de privacidade de dados permitem aprendizado e uso dos dados sem revelar informações sensíveis. Enquanto Segurança de dados evita acesso e exposição, então não podemos usá-los. 

<img src="images/print.jpeg" width=40%>  

Formas de manter privacidade de dados caso a caso são chamados **ad hoc**.  
Para identificar indivíduos em um conjunto de dados, as colunas de informações podem ser divididas entre **PII (Personally Identifier Information)** ou **Quasidentificadores**.  
> PII: Informações usadas para identificar diretamente um indivíduo  
> Quasidentificadores: Informações que podem ser combinadas para fazer ligações e identificar indivíduos.  

## Sensibilidade global  

Sensibilidade global é um conceito necessário para entender a aplicação de ruído em privacidade diferencial. Tendo um universo de dados U, diversos subconjuntos (conjuntos de dados) formados por elementos de U podem ser formados, por exemplo, $D1 \subset U$, $D2 \subset U$, ..., $Dn \subset U$. Se pensarmos em um dataset com as colunas idade, peso, altura, U = idade x peso x altura. Cada componente de U, como idade, tem uma quantidade específica de valores, por exemplo, idade é considerada de 0 até 100 normalmente. A privacidade diferencial garante que a ausência ou presença de um indivíduo em um conjunto de dados não altere significativamente a análise de dados. Para isso é importante definir conjuntos vizinhos: Cada conjunto D é formado por indivíduos com as características de U, e com essa definição conseguimos formar $D$ e $D´$, datasets vizinhos. $D$ é vizinho (ou adjacente) de $D'$ se por adição ou alteração, eles forem diferentes.  
**Por adição:** \(D \sim D'\) se \(|D \triangle D'| = 1')\. Em outras palavras, se a diferença simétrica (ausência ou presença de um indivíduo) for = 1.








