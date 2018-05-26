# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1 
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 3
# Faça um programa em Python que recebe um número inteiro e imprime seu dígito 
# das dezenas. Observe o exemplo abaixo: 



inteiro = input("um número inteiro: ")

dezena = ( int(inteiro) // 10 ) % 10

saida = "O dígito das dezenas é " + str( dezena )
print( saida )