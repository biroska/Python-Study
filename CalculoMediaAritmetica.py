# Este programa contempla a resolução do segundo exercício do curso:
#     Introdução à Ciência da Computação com Python Parte 1 
# Disponível no coursera.

#                                EXERCÍCIO 2
# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética.

nota1 = int(input("Digite a primeira nota: "))

nota2 = int(input("Digite a segunda nota: "))

nota3 = int(input("Digite a terceira nota: "))

nota4 = int(input("Digite a quarta nota: "))

media = ( nota1 + nota2 + nota3 + nota4) / 4

saida = "A média aritmética é " + str( media )

print( saida )