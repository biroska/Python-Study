# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 2
# Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c,  respectivamente, e imprimir o
# resultado na saída da seguinte maneira:
# Quando não houver raízes reais imprima:
#   esta equação não possui raízes reais
# Quando houver apenas uma raiz real imprima:
#   a raiz desta equação é X, onde X é o valor da raiz
# Quando houver duas raízes reais imprima:
# as raízes da equação são X e Y, onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente

import math

a = float( input("Forneca a: ") )
b = float( input("Forneca b: ") )
c = float( input("Forneca c: ") )

delta = b**2 -4*a*c

if delta < 0 :
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x1 = -b / 2*a
        saida = "a raiz desta equação é " + str(x1)
        print( saida )
    else:
        x1 = ( -b + math.sqrt( delta ) ) / (2*a)
        x2 = ( -b - math.sqrt( delta ) ) / (2*a)

        if x2 < x1:
            temp = x1
            x1 = x2
            x2 = temp

        saida = "as raízes da equação são " + str(x1) + " e " + str(x2)
        print( saida )