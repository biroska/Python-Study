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

dias = segundos // 86400
horas_restantes = segundos % 86400

horas = horas_restantes // 3600
segs_restantes = segundos % 3600

minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

saida = str( dias ) + " dias, " + str( horas ) + " horas, " + str( minutos ) + " minutos e " + str( segs_restantes_final ) + " segundos."
print( saida )