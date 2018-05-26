# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 1
# Receba um número inteiro na entrada e imprima par
# quando o número for par ou ímpar quando o número for ímpar.

numero = int( input("Forneca um numero: ") )

if ( numero % 2 == 0 ):
    print( "par" )
else:
    print( "ímpar" )