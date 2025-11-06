---
author:
- Ficha 2
theme: Boadilla
title: Algoritmos para Análise de Sequências Biológicas
header-includes:
  - \hypersetup{colorlinks=true,urlcolor = blue, linkcolor=cyan,pdfborderstyle={/S/U/W 1}}
  - \AtBeginDocument{\title[AASB]{Algoritmos para Análise de Sequências Biológicas}}
---

# Objetivo
- Introduzir o tipo de dados *string*
- Introduzir as instruções condicionais e os ciclos

# Conceitos
## Strings
- Uma sequência de carateres
- É um objeto, e por isso possui vários métodos

## Alguns Métodos sobre strings
upper
 : passa para maiúsculas

lower
 : passa para minúsculas

replace
 : substitui uma substring por outra

count
 : conta o nº de ocorrências de uma substring

find
 : devolve o primeiro índice da substring ou -1

## Operadores
`+`
 : Concatenação

in
 : verifica se uma string está contida noutra

[]
 : índices sobre strings


# Índices
## Índices
seq[ind]
 : o caratere que está no índice correspondente

seq[ini:fim]
 : os carateres entre seq[ini] e seq[fim - 1]

seq[ini:fim:incr]
 : o mesmo que o anterior com increment incr

## Exemplos
seq[0]
 : O primeiro caratere

seq[-1]
 : O último caratere

seq[:3]
 : os primeiros 3 carateres

seq[-2:]
 : os últimos 2 carateres

seq[:]
 : uma cópia de seq

seq[::-1]
 : a seq invertida

seq[::3]
 : seq[0], seq[3], ...

# Exemplos
	>>> seq = "acccgTgat"
	>>> len(seq)
	9
	>>> seq.upper()
	'ACCCGTGAT'
	>>> seq.count('t')
	1
	>>> seq.replace('a','C')
	'CcccgTgCt'
	>>> 'gat' in seq
	True
	>>> seq.find('gat')
	6
	>>> seq.find('x')
	-1
	>>> seq[::-1]
	'tagTgccca'

# Sugestões
- Não se esqueça de **TESTAR CORRETAMENTE** o código que escrever
- Cuidado que em Python, as maiúsculas são diferentes das minúsculas
- O seu código deve funcionar em todos os casos
- Os resultados devem ser apresentados em maiúsculas
- O primeiro problema deve devolver **True** ou **False**
- Não se esqueça de testar todos os casos, incluindo as condições de fronteira

# Problemas
1. Escreva uma função que receba uma string e que valide se esta é uma sequência de DNA
1. Escreva uma função que recebe uma sequência e imprime, um por linha, o nº de A, C, G e T
1. Modifique a função anterior para imprimir também o nº de erros
1. Escreva uma função que recebe uma sequência e imprime, uma por linha, a frequência de A, C, G e T
1. Escreva um programa que leia uma cadeia de DNA e imprima a cadeia de RNA correspondente
1. Escreva uma função que receba uma string e imprime o nº de vogais seguido do nº de consoantes
1. Escreva um programa que leia uma cadeia de DNA e imprima o seu complemento inverso
1. Escreva uma função que receba uma string e que devolva um dos 4 possíveis valores: DNA, RNA, AMINO ou ERRO

# Documentação e Testes
- Leia aqui sobre a filosofia da [documentação](https://realpython.com/documenting-python-code/)
- Leia aqui sobre a filosofia de [testes](https://realpython.com/python-testing/)
- Crie a documentação para estas funções
- Crie testes para estas funções
