# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 2
# Receba um número inteiro na entrada e imprima Fizz se o número for divisível
# por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int( input("Forneca um numero: ") )

if ( numero % 3 == 0 ):
    print( "Fizz" )
else:
    print( numero )