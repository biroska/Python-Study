# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1 
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 2
# Reescreva o programa contaSegundos para imprimir também a quantidade de dias, 
# ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" 
# esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a
# dias, b horas, c minutos e d segundos.  



input = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos = int( input )

dias = ( ( segundos // 60 ) // 60 ) // 24

saida = dias + " dias, " + horas + " horas, " + minutos + " minutos e " + segundos + " segundos."
print( saida )