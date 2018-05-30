# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 2
# Escreva um programa que receba um número inteiro na entrada e verifique se o número 
# recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, 
# imprima "sim"; se não existir, imprima "não".

strNumero = input("Digite um número inteiro: ")
numero = int( strNumero )

digitoAnterior = -1000
proximoDigito = 1
count = 0

isAdjacente = False
qtdCaracteres = len( strNumero )

while not isAdjacente and count <= qtdCaracteres:
    
    proximoDigito = numero % 10

    if proximoDigito == digitoAnterior:
        isAdjacente = True
    else:
        digitoAnterior = proximoDigito
        numero = numero // 10

    count = count + 1
    

if isAdjacente:
    print("sim")
else:
    print("não")