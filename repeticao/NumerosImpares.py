# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 2
# Receba um número inteiro positivo na entrada e imprima os n primeiros 
# números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

n = int( input("Digite o valor de n: ") )

aux = 1

while n > 0:
    print( ( 2 * aux ) -1 )
    aux += 1
    n -= 1