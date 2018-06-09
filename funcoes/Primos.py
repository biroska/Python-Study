# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 2
# Exercício 2 - Primos
# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e
# devolve o maior número primo menor ou igual ao número passado à função
#
# Note que
#
# maior_primo(100) deve devolver 97
#
# maior_primo(7) deve devolver 7
#
# Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando
#  se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado
#  na variável é o maior primo encontrado.

def isPrimo( x ):

    divisor = x -1

    while divisor > 1 :

        if ( x % divisor == 0 ):
            return False

        divisor = divisor -1

    return True


def maior_primo( numero ):

    valorInformado = int( numero )

    count = numero -1

    if ( valorInformado < 2 or isPrimo( numero ) ):
        return valorInformado

    while count > 1 :

        if ( isPrimo( count ) ):
            return count

        count = count -1

    return 1
