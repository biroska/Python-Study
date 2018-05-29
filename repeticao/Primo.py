# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 1
# Escreva um programa que receba um número inteiro positivo na entrada e verifique se 
# é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

numero = int( input("Digite um número inteiro: ") )

isPrimo = True
count = 0


if numero % 2 == 0:
    count += 1

if numero % 3 == 0:
    count += 1

if numero % 5 == 0:
    count += 1

if numero % 7 == 0:
    count += 1

if numero % 11 == 0:
    count += 1

if numero % 13 == 0:
    count += 1

if numero % 17 == 0:
    count += 1

if numero % 19 == 0:
    count += 1

if count == 1:
    print("primo")
else:
    print("não primo")