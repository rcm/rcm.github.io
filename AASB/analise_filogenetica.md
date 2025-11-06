---
author:
- Análise Filogenética
theme: Boadilla
title: Algoritmos para Análise de Sequências Biológicas
header-includes:
  - \hypersetup{colorlinks=true,urlcolor = blue, linkcolor=cyan,pdfborderstyle={/S/U/W 1}}
  - \AtBeginDocument{\title[AASB]{Algoritmos para Análise de Sequências Biológicas}}
  - \AtBeginDocument{\usepackage{tikz}}
  - \AtBeginDocument{\usepackage{tikz-qtree}}
  - \AtBeginDocument{\usepackage{relsize}}
---

# Sumário
- Análise filogenética
- Algoritmo UPGMA

# Definição
- **Análise filogenética** de um conjunto de sequências (DNA, RNA, proteínas) é a determinação de como cada sequência pode ter sido derivada ao longo do processo de **evolução** natural.

- Relações evolutivas são visualizadas colocando as sequências como folhas de uma **árvore evolucionária**, onde os nós de ramificação representam eventos de mutação (substituição, inserção, remoção). 

# Análise Filogenética
Uma árvore filogenética sugere as relações de proximidade entre sequências;
Proximidade na árvore sugere proximidade evolutiva

\begin{figure}
\centering
\begin{tikzpicture}%[sibling distance=72pt]
\tikzset{edge from parent/.style= {draw, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\tikzset{frontier/.style={distance from root=100pt}}
\Tree [ [ [ s1 s2 ] [ s3 s4 ] ] s5 ]
\end{tikzpicture}
\end{figure}

# Análise Filogenética
Os nós da árvore indicam ancestrais comuns

\begin{figure}
\centering
\begin{tikzpicture}%[sibling distance=72pt]
\tikzset{edge from parent/.style= {draw, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\tikzset{every node/.style={font=\tiny}}
\tikzset{frontier/.style={distance from root=100pt}}
\Tree [.{ Raiz (ancestral comum)} [ .{ancestral comum a s1, \dots, s4} [ .{ancestral comum a s1 e s2} {\normalsize s1} {\normalsize s2} ] [ .{ancestral comum a s3 e s4} {\normalsize s3} {\normalsize s4} ] ] {\normalsize s5} ]
\end{tikzpicture}
\end{figure}

# Aplicações
- Determinar a **árvore da vida** - evolução das diferentes espécies - complementando os métodos tradicionais baseados na morfologia; permitem estabelecer relações taxonómicas entre espécies ou ancestralidade entre indivíduos ou populações;
- Ajuda na determinação da **função** de sequências de DNA/ proteínas - determinação de ramos com domínios específicos que podem ter consequências funcionais;
- Análise de espécies com mutações rápidas (e.g. virus) – pode ajudar na **epidemiologia**; permite hierarquizar mutações numa árvore - antigas vs. recentes;
- Primeiro passo para alguns algoritmos de Alinhamento Múltiplo (progressivos).

# Árvore de gene/sequência vs. espécie
- A evolução de um gene na maioria dos casos segue a evolução observada da espécie
- A reconstrução filogenética de um gene humano terá preponderância a agrupar o gene humano com o chimpanzé, e ambos com o gorila

## Exceções
- Nem sempre a filogenia pode estar correcta; não se pode fazer inferência a partir de um só gene.
- A relação entre espécies (taxonomia) pode estar incorrecta
- Transferência horizontal
	- Típica das bactérias
	- Gene é incorporado no genoma de uma fonte exterior
	- Não seguiu a história evolutiva da espécie onde se inseriu

# Árvores Evolucionárias
- Indicam o sentido da passagem do tempo
- Pode assumir-se a hipótese do relógio molecular – taxas de mutação uniformes
- Árvores podem ser representadas pelos clusters que se obtêm juntando taxa (folhas) presentes abaixo de cada nó interno (sub-árvores)
- Nº de árvores aumenta muito rapidamente com o aumento do nº de sequências.

# Algoritmos de Análise Filogenética
- Objectivo: a partir de um **conjunto de sequências** (DNA ou proteínas), determinar a **árvore evolucionária** que melhor explique a sua evolução.

- Problema de **otimização**: de entre todas as árvores possíveis, escolher a que maximiza uma dada função objetivo.

- Espaço de procura tipicamente bastante grande – problema muito complexo.

# Complexidade do problema

 \# seqs          \# pares de seqs                      \# arvores  # ramos/árvore
---------  ----------------------- ------------------------------- ---------------
  3               3                         3                        4
  4               6                        15                        6
  5              10                       105                        8
  6              15                       945                       10
 10              45                  34459425                       18
 30             435                 $4.95 \times 10^{38}$             58
 N          $\frac{N (N - 1)}{2}$   $\frac{(2N-3)!}{2^{N-2}(N-2)!}$  $2N-2$
---------  ----------------------- ------------------------------- ---------------

# Algoritmos de previsão filogenética
Baseados na distância
 : Baseia-se na distância (alterações) entre pares de sequências: Neighbor Joining, UPGMA

Máxima parcimónia (ou mínima evolução)
: Retornam a árvore que minimiza nº de mutações necessárias para explicar a variação das sequências

Máxima verosimilhança
 : Emprega modelos probabilísticos

# Métodos baseados na distância
Baseiam-se na **distância** (inverso da similaridade) entre os diversos **pares de sequências** considerados.

Objectivo: tentar identificar sequências a colocar como **vizinhas** e determinar **comprimentos dos ramos** da árvore filogenética que representem, o mais fielmente possível, as distâncias entre os pares de sequências.

São usados como primeiro passo dos **métodos progressivos de AM** (e.g. ClustalW).


# Métodos baseados na distância
Pretende-se encontrar a árvore *T* que minimiza

SQE
 : $\sum_{ij} (d_{ij}(T) - D{ij})^2$

Esta é a soma do quadrado dos erros entre a distância na árvore e a distância nas sequências dos vários taxa

O problema de estimar a árvore que minimiza SQE é um problema **NP-difícil**

# Cálculo da distância
- Tipicamente, distância medida pelo **nº de carateres distintos** entre as duas sequências (edit distance)

- Métodos mais complexos podem fazer uso de matrizes de substituição (e.g. PAM, BLOSUM).

- Pode usar-se a função de mérito dos alinhamentos normalizada entre 0 e 1 (distância será 1 – mérito normalizado).  

# Algoritmo Unweighted Pair Group Method Using Arithmetic Averages (UPGMA)
- Algoritmo heurístico (não dá garantias de soluções óptimas mas é eficiente)
- Começa pelo par de sequências mais próximo e vai agrupando as sequências usando sempre a distância menor como critério
- Usa um algoritmo clássico de clustering: **clustering hierárquico**

# Algoritmo UPGMA
- Assume taxas de mutação uniformes em todos os ramos, logo árvores criadas são **ultramétricas**

::: columns
:::: column
## Correta
\begin{figure}
\centering
\begin{tikzpicture}[scale = 0.75, font = \relsize{2.5}]
\tikzset{edge from parent/.style= {draw, thick, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\Tree [ [ [ [ [ [ 1 ] ] ] 2 ] ] [ 3 [ [ [ [ 4 ]  ]  ]  ]  ] ]
\end{tikzpicture}
\end{figure}
::::


:::: column
## UPGMA
\begin{figure}
\centering
\begin{tikzpicture}[scale = 1.25, font = \relsize{0.25}]
\tikzset{edge from parent/.style= {draw, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\tikzset{frontier/.style={distance from root=100pt}}
\Tree [ 1 [ 4 [ 2 3 ] ] ]
\end{tikzpicture}
\end{figure}
::::
:::

# Algoritmo UPGMA

Cada sequência é agrupada num cluster

::: columns
::::column
\begin{figure}
\centering
\begin{tikzpicture}[roundnode/.style={circle, draw=red!60, fill=red!5, minimum size=7mm}]
	\filldraw[color=red!60, fill=red!5, very thick] (0.6,1.8) ellipse (3.2 and 2);
	\filldraw[color=red!60, fill=red!5, very thick, rotate around={-30:(1.2,1.8)}] (1.2,1.8) ellipse (2 and 1.5);
	\filldraw[color=red!60, fill=red!5, very thick, rotate around={-55:(-1.25,1.4)}] (-1.25,1.4) ellipse (1.5 and 0.6);
	\filldraw[color=red!60, fill=red!5, very thick, rotate around={55:(1.8,1.5)}] (1.8,1.5) ellipse (1.2 and 0.7);
	\node[roundnode] at (-1.5,1.8) {s1};
	\node[roundnode] at (-1,1) {s2};

	\node[roundnode] at (0.6,2) {s3};

	\node[roundnode] at (1.6,1.1) {s4};
	\node[roundnode] at (2.2,2) {s5};
\end{tikzpicture}
\end{figure}
::::
::::column
\begin{figure}
\centering
\begin{tikzpicture}[scale = 1.25, font = \relsize{0.25}]
\tikzset{edge from parent/.style= {draw, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\tikzset{frontier/.style={distance from root=100pt}}
\Tree [ [ 1 2 ] [ [ 4 5 ] 3 ] ]
\end{tikzpicture}
\end{figure}
::::
:::

# Algoritmo UPGMA
1. Criar um cluster para cada sequência: $L = \{ \{s_i\} : s_i \in S\}$
1. Matriz de distâncias entre os clusters é inicializada com a matriz de distâncias entre as sequências
1. Enquanto existir mais do que um cluster
	1. Descobrir os clusters $C_i$ e $C_i$ com distância mínima entre eles
	1. Criar o cluster $C_k = C_i \cup C_j$
	1. Adicionar o novo cluster a $L$ e remover os anteriores: $L = \{C_k\} \cup  L \setminus \{C_i, C_j\}$ 
	1. Remover linhas e colunas $i$ e $j$ da tabela de distâncias
	1. Introduzir linha e coluna para $k$ com as distâncias para o novo cluster na árvore, adicionar vértice ligando os nós referentes a $C_i$ e $C_j$ com valor de altura igual a d_{ij} / 2

# Exemplo
             $\{s_1\}$   $\{s_2\}$   $\{s_3\}$   $\{s_4\}$   $\{s_5\}$
----------- ----------- ----------- ----------- ----------- -----------
 $\{s_1\}$        0
 $\{s_2\}$      **2**        0
 $\{s_3\}$        5          4          0
 $\{s_4\}$        7          6          4            0
 $\{s_5\}$        9          7           6           3           0
----------- ----------- ----------- ----------- ----------- -----------

# Exemplo
                 $\{s_1,s_2\}$   $\{s_3\}$   $\{s_4\}$   $\{s_5\}$
--------------- --------------- ----------- ----------- -----------
 $\{s_1,s_2\}$        0
 $\{s_3\}$            4.5         0
 $\{s_4\}$            6,5         4              0
 $\{s_5\}$            8           6            **3**         0
--------------- --------------- ----------- ----------- -----------

# Exemplo
                 $\{s_1,s_2\}$   $\{s_3\}$   $\{s_4,s_5\}$
--------------- --------------- ----------- ---------------
 $\{s_1,s_2\}$        0
 $\{s_3\}$          **4.5**          0
 $\{s_4,s_5\}$        7,25           5            0
--------------- --------------- ----------- ---------------

# Exemplo
                     $\{s_1,s_2,s_3\}$   $\{s_4,s_5\}$
------------------- ------------------- ---------------
 $\{s_1,s_2,s_3\}$        0
 $\{s_4,s_5\}$        6.125                0
------------------- ------------------- ---------------

# Exemplo
\begin{figure}
\centering
\begin{tikzpicture}[scale = 1.25, font = \relsize{0.25}]
\tikzset{edge from parent/.style= {draw, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\tikzset{frontier/.style={distance from root=100pt}}
\Tree [ [ [ 1 2 ] 3 ] [ 4 5 ] ]
\end{tikzpicture}
\end{figure}

# Neighbor Joining
- Funciona de forma semelhante ao UPGMA

- Muda a forma de escolher os clusters que se juntam em cada passo: usa-se a regra de juntar sub-árvores que estejam próximas, mas afastadas das restantes

- Muda o valor colocado como altura da árvore

# Máxima parcimónia (mínima evolução)
- Objectivo: **minimizar nº de passos evolutivos** (mutações) que explicam a variação das sequências
- Baseia-se num **Alinhamento Múltiplo**; análise de cada posição (coluna do alinhamento)
- São identificadas as árvores que requerem o menor nº de mutações, para todas as posições (informativas)
- Vantagem de ser fácil estabelecer relação entre ramos da árvores e as mutações que ocorrem
- Método **exato** -- **pesado** computacionalmente -– ideal para **filogenias menos profundas** mas não ideal para espécies distantes

# Aferir significância
::: block
## Bootstrap 
- Selecionar colunas do AM aleatoriamente, com substituição;
- Repetir construção da árvore com diferentes seleções;
- Frequência com que dada característica ocorre é indicador da sua confiança.
:::

Se possível usar dois tipos de métodos para construir a árvore e comparar resultados


# Programas de análise filogenetica
MEGA - http://www.megasoftware.net/
 : Inclui métodos de máxima parcimónia, distância, máxima verosimilhança

Mr Bayes - https://nbisweden.github.io/MrBayes/index.html
 : 
Implementa essencialmente métodos de máxima verosimilhança


