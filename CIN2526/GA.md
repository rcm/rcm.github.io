---
author:
- Rui Mendes
theme: Boadilla
title: Genetic Algorithms
nocite: '@*'
biblio-title: References
---

[//]: # (
pandoc -t beamer -H latex_preamble.tex -s --bibliography biblio.bib --filter pandoc-citeproc -s BioInspiredAlgorithms.md -o BioInspiredAlgorithms.tex
)

# Introduction

::: columns
:::: column
## Characteristics
- Inspired in living systems
- Borrow ideas from evolution
::::
:::: column
## Examples
- Genetic Algorithms
- Genetic Programming
::::
:::

# Genetic Algorithm
* Optimization algorithm
* Inspired in natural selection 
* Uses a population of individuals
* Each individual encodes a solution
* There are three operators:
	1. Selection
	1. Crossover
	1. Mutation
	
# Encoding
* Process that represents a solution in a given alphabet
* There are several encodings, e.g.:
	* binary
	* integer
	* real numbers
	* permutations
* Usually, they are linear sequences of values (chromossomes composed of genes)

# Creating new solutions
* The genetic operators for creating new solutions are:
	* Recombination or Crossover
	* Mutation

# Crossover
* Combines several solutions
* Usually, it takes two parents and creates two offspring
* Usual methods:
	* One point crossover
	* Two point crossover
	* Uniform crossover
	
# One point crossover
* A cutting point is randomly selected
* Each solution takes a part from each parent

:::columns
::::column
## Parents
\centering
$\textcolor{blue}{010}|\textcolor{blue}{110}$

$\textcolor{red}{011}|\textcolor{red}{101}$
::::
::::column
## Offspring
\centering
$\textcolor{blue}{010}|\textcolor{red}{101}$

$\textcolor{red}{011}|\textcolor{blue}{110}$
::::
:::

# Two point crossover
* Two cutting points are randomly selected
* The central parts are exchanged

:::columns
::::column
## Parents
\centering
$\textcolor{blue}{10}|\textcolor{blue}{11}|\textcolor{blue}{0}$

$\textcolor{red}{01}|\textcolor{red}{10}|\textcolor{red}{1}$
::::
::::column
## Offspring
\centering
$\textcolor{blue}{10}|\textcolor{red}{10}|\textcolor{blue}{0}$

$\textcolor{red}{01}|\textcolor{blue}{11}|\textcolor{red}{1}$
::::
:::

# Uniform crossover
* The value of the first parent is randomly copied to one of the offspring
* The value  of the second parent is copied to the other one

:::columns
::::column
## Parents
\centering
$\textcolor{blue}{10110}$

$\textcolor{red}{01101}$
::::
::::column
## Offspring
\centering
$\textcolor{red}{0}\textcolor{blue}{0}\textcolor{blue}{1}\textcolor{red}{0}\textcolor{blue}{0}$

$\textcolor{blue}{1}\textcolor{red}{1}\textcolor{red}{1}\textcolor{blue}{1}\textcolor{red}{1}$
::::
:::

# Mutation
* A position is randomly selected inside the string
* The value is randomly selected among the possible values

:::columns
::::column
## Before
\centering
$\textcolor{blue}{10110}$
::::
::::column
## After
\centering
$\textcolor{blue}{10}\textcolor{red}{0}\textcolor{blue}{10}$
::::
:::

# Fitness
* Quantifies the quality of a solution
* It is usually a *floating point number*
* In order to compare the quality of two solutions, one simply has to compare the fitness values

# Selection
* Process for choosing which individuals will generate offspring or will be copied into the new population
* It usually selects individuals:
	* According to their fitness;
	* By partial or total ordering of the solutions
	* By stochastic choice of the individuals according to their fitness

# Fitness proportionate selection
* The probability of selecting an individual is proportional to their fitness
* If it is a maximization problem, the probability of selecting an individual is $p_i = \frac{f_i}{\sum_i f_i}$

# Genetic Algorithm outline
1. Initialize the population
1. While not finished
	1. Choose individuals
	1. Apply genetic operators
	1. Insert offspring into the next population
