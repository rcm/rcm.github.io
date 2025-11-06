---
author:
- Análise Filogenética
theme: Boadilla
title: Algoritmos para Análise de Sequências Biológicas
header-includes:
  - \AtBeginDocument{\usepackage{tikz}}
  - \AtBeginDocument{\usepackage{tikz-qtree}}
  - \AtBeginDocument{\usepackage{relsize}}
---

\begin{figure}
\centering
\begin{tikzpicture}[scale = 1.25, font = \relsize{0.25} ]
\tikzset{edge from parent/.style= {draw, edge from parent path={(\tikzparentnode.south) -- +(0,-8pt) -| (\tikzchildnode)}}}
\tikzset{frontier/.style={distance from root=100pt}}
\Tree [ACGTCCT [ACTCAT AGTCAT ] ]
\end{tikzpicture}
\end{figure}
