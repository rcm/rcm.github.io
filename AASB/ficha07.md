---
author:
- Ficha 7
theme: Boadilla
title: Algoritmos para Análise de Sequências Biológicas
header-includes:
  - \hypersetup{colorlinks=true,urlcolor = blue, linkcolor=cyan,pdfborderstyle={/S/U/W 1}}
  - \AtBeginDocument{\title[AASB]{Algoritmos para Análise de Sequências Biológicas}}
  - \AtBeginDocument{\renewenvironment{Shaded} {\footnotesize} {}}
---

# Objetivo
- Treinar expressões regulares

# Exercícios
1. Crie uma função chamada ```PROSITE2re(padrao)``` que devolva a expressão regular correspondente ao padrão PROSITE
1. Crie uma função chamada ```enzyme2re(enzyme)``` que devolva a expressão regular correspondente à enzima de restrição
1. Crie uma função chamada ```cut_positions(enzyme, seq)``` que devolva uma lista dos índices correspondentes às posições de corte da enzima
1. Crie uma função chamada ```cut_subseqs(enzyme, seq)``` que devolva uma lista das subsequências correspondentes ao corte da enzima

# Exemplos
~~~ {.python}
>>> PROSITE2re('[AC]-x-V-x(4)-{ED}')
'[AC].V.{4}[^ED]'
>>> enzyme2re('G^AMTV')
'(?=G)A[AC]T[ACG]'
>>> cut_positions('G^AMTV', 'GTAGATGACTGCTGAGATCGAATCTC')
[7, 20]
>>> cut_subseqs('G^AMTV', 'GTAGATGACTGCTGAGATCGAATCTC')
['GTAGATG' 'ACTGCTGAGATCG' 'AATCTC']
~~~
