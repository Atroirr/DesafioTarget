##
## Como nao foi especificado no enunciado um limite 
## para a sequencia tomarei ela como infinita, para saber se um número 
## partence a sequencia de Fibonnaci usarei a formula de Binet, declararei 
## variaveis para o primeiro e segundo numeros como no enunciado mas eles 
## não serão utilizados nos calculos. 
##

import math

def quadrado(i):
    raiz = int(math.sqrt(i))
    return raiz * raiz == i

def fibonnaci(n):
    return quadrado(5*n*n + 4) or  quadrado(5*n*n -4)

entrada = int(input("Digite o número a ser verificado: \n"))

if(fibonnaci(entrada)):
    print(f"{entrada} pertence a sequência de Fibonnaci!")
else:
    print(f"{entrada} não pertence a sequência de Fibonnaci!")