# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 5
# Receba 3 números inteiros na entrada e imprima crescente se eles forem dados em
# ordem crescente. Caso contrário, imprima não está em ordem crescente

numero1 = int( input("Forneca um numero: ") )
numero2 = int( input("Forneca um numero: ") )
numero3 = int( input("Forneca um numero: ") )

if ( numero3 >  numero2 and numero2 > numero1 ):
    print( "crescente" )
else:
    print( "não está em ordem crescente" )