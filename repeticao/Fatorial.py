# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 1
# Escreva um programa que receba um número natural n na entrada e imprima n! na saída.

n = int( input("Digite o valor de n: ") )

fatorial = 1

if n > 0:

    while n > 0:
         fatorial = fatorial * n
         n = n -1
    print(fatorial)
else:
    print( 1 )