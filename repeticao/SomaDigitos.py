# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 2
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima
# a soma dos dígitos deste número na saída

n = int( input("Digite um número inteiro: ") )

aux = n

soma = 0

while aux > 0:
    soma = soma + ( aux % 10 )
    aux = aux // 10

print(soma)
    