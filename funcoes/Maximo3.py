# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 2
# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros
#  recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
#
# Note que
#
# maximo(30,14,10) deve devolver 30
#
# maximo(0,-1, 1) deve devolver 1
#

def maximo( x1, x2, x3 ):

    parcMax = 0

    if ( x1 > x2 ):
        parcMax = x1
    else:
        parcMax = x2

    if ( parcMax > x3 ):
        return parcMax
    else:
        return x3
