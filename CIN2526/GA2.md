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

# Selection by ordering
* If using total ordering, the individuals are ranked according to their fitness and the top $n$ individuals are chosen
* In a partial ordering, several individuals are chosen at random and they are ordered (it's called *tournament selection*)

# Genetic Algorithm outline
1. Initialize the population
1. While not finished
	1. Choose individuals
	1. Apply genetic operators
	1. Insert offspring into the next population
 
# Generational scheme
* A new population is created in each iteration
* Parents are chosen from the current population
* Offspring are inserted into the new population
* The old population is discarded

# Generational scheme
1. Initialize population
1. While not finished
	1. Evaluate individuals
	1. While the new population is not complete
		1. Select two individuals
		1. Apply genetic operators
		1. Insert offspring into the new population

# Steady state scheme
* There are not generations
* Several individuals are randomly chosen for the tournament
* The best individuals produce offspring using the genetic operators
* The offspring substitute the worse individuals

# Steady state scheme
1. Initialize population
1. While not finished
	1. Choose 4 individuals
	1. Rank the individuals
	1. Apply genetic operators to the best 2 individuals
	1. The offspring substitute the worst 2 individuals

# Representations
* There can be several solution representations
* Each representation has several advantages and disadvantages
* There are several possibilities:
	* Integer
	* Real
	* Ordered

# Integer representation
* Each individual is a sequence of integers, e.g., 
\begin{eqnarray*}
\begin{array}{c c c c c}
2 & 1 & 2 & 3 & 7
\end{array}
\end{eqnarray*}
* Crossover operators defined thus far can be used
* There can be new crossover and mutation operators

## Random value mutation
\centering
$2 \; 1 \;  2  \; 3  \; 7 \rightarrow 2  \; \textcolor{red}{5}  \; 2  \; 3  \; 7$

## Next element mutation
\centering
$2 \; 1 \; 2 \; 3 \; 7 \rightarrow 2 \; \textcolor{red}{2} \; 2 \; 3 \; 7$

# Real representation
- Each individual is a sequence of real numbers, e.g.,

\begin{eqnarray*}
\begin{array}{c c c c}
2.3 & -7.4 & 1.9 & 0.1
\end{array}
\end{eqnarray*}

- There are specific crossover operators:
	- Arithmetic crossover
	- Linear crossover
	- Blend crossover
- And mutation operators:
	- Uniform mutation
	- Gaussian mutation
	- Cauchy modification

# Arithmetic crossover
- Given two parents, $\vec P_1$ and $\vec P_2$
- Create 2 solutions:

	$\vec S_1$
	 : $\lambda \cdot \vec P_1 + (1 - \lambda) \cdot \vec P_2$
	 
	$\vec S_2$
	 : $(1 - \lambda) \cdot \vec P_1 - \lambda \cdot \vec P_2$
- With $\lambda$ usually being $0.6$

# Linear crossover
- Given two parents, $\vec P_1$ and $\vec P_2$
- Create 3 solutions:

	$\vec S_1$
	 : $0.5 \cdot \vec P_1 + 0.5 \cdot \vec P_2$
	 
	$\vec S_2$
	 : $1.5 \cdot \vec P_1 - 0.5 \cdot \vec P_2$

	$\vec S_3$
	 : $0.5 \cdot \vec P_1 + 1.5 \cdot \vec P_2$
- Choose the two best solutions among $\vec P_1$, $\vec P_2$, $\vec S_1$, $\vec S_2$ and $\vec S_3$ to become the children

# Blend crossover
- Given two parents, $x_1$ and $x_2$ where $x_1 < x_2$
- Create solutions using:

\begin{eqnarray*}
U[x_1 - \alpha \cdot (x_2 - x_1), x_2 + \alpha \cdot (x_2 - x_1)]
\end{eqnarray*}

- $\alpha$ is usually chosen to be $0.5$.

# Uniform mutation
- A random mutation where one or more positions are modified
- Modified positions are randomly generated within the entire range
- The modified position has no relationship with the original value
- $x_{new} = U[\min, \max]$

# Random modification
- A random mutation where one or more positions are modified
- Modified positions are  generated in the vicinity of the original value
- $x_{new} = x + U[-\epsilon, \epsilon]$ or
- $x_{new} = x  \cdot (1 + U[-\epsilon, \epsilon])$

# Gaussian mutation
- A random mutation where one or more positions are modified
- Modified positions are  generated in the vicinity of the original value following the gaussian distribution
- $x_{new} = x + N(0, \sigma)$

# Permutation based representations
- Each individual is a sequence of integers representing a permutation
- The integers are in the range $1, \ldots, n$ without repetitions
- Example:
\begin{eqnarray*}
\begin{array}{c c c c c}
2&1&5&4&3
\end{array}
\end{eqnarray*}
- Genetic operators must preserve these constraints

# Order preserving crossover
- Select a cutting position and copy the parts left of the cutting point
directly to the corresponding offspring
- Copy the remaining values by using the order in the other parent
- Can also be used with two cutting points

## Order preserving crossover
:::columns
::::column
\begin{center}
\textcolor{blue}{2 1 5} | \textcolor{blue}{3 4}

\textcolor{red}{1 4 5} | \textcolor{red}{3 2}
\end{center}
::::
::::column
\begin{center}
\textcolor{blue}{2 1 5} | \textcolor{red}{4 3}

\textcolor{red}{1 4 5} | \textcolor{blue}{2 3}
\end{center}
::::
:::

# Partially mapped crossover
- Choose random segment from the first parent $P_1$
- Look for values in the other parent $P_2$ that were not copied
- For each of these values $x \in P_2$, look at what values $y \in P_1$ that was copied in its place
- Place $x$ in the position occupied by $y$ in $P_2$, because we know we will not put $y$ there (because it's already in the child)
- 


# Insertion mutation
- Choose two positions at random
- Move the second position to follow the first

## Insertion mutation
\begin{center}
2 \textcolor{blue}{1} 5 \textcolor{blue}{3} 4 $\rightarrow$ 2 \textcolor{blue}{1 3} 5 4
\end{center}

# Swap mutation
- Choose two positions at random
- Swap their positions

## Swap mutation
\begin{center}
2 \textcolor{blue}{1} 5 \textcolor{blue}{3} 4 $\rightarrow$ 2 \textcolor{blue}{3} 5 \textcolor{blue}{1} 4
\end{center}

# Inversion mutation
- Choose two positions at random
- Invert the values between them

## Inversion mutation
\begin{center}
2 \textcolor{blue}{1 5 3} 4 $\rightarrow$ 2 \textcolor{blue}{3 5 1} 4
\end{center}

# Scramble mutation
- Pick a random subset of genes
- Randomly change the position of the values between them
- The subset need not be contiguous

## Scramble mutation
\begin{center}
2 \textcolor{blue}{1 7 5 3 6} 4 $\rightarrow$ 2 \textcolor{blue}{7 3 6 5 1} 4
\end{center}
