# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 1
# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
# às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder,
# respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
#
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima longe
# na saída. Caso o contrário, quando a distância for menor que 10, imprima perto

import math

x1 = float( input("X1: ") )
y1 = float( input("Y1: ") )

x2 = float( input("X2: ") )
y2 = float( input("Y2: ") )

dX = x2 - x1
dY = y2 - y1

distancia = math.sqrt( dX**2 + dY**2 )

if distancia >= 10:
    print( "longe" )
else:
    print( "perto" )