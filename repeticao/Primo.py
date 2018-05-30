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

divisor = 2

while divisor < 100:

    if numero % divisor == 0:
        count += 1

    divisor += 1


if count == 1:
    print("primo")
else:
    print("não primo")