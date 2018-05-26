# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1 
# Disponível no coursera.
#
#                     EXERCÍCIO OPCIONAL 1 
# Uma empresa de cartão de crédito envia suas faturas por email 
# com a seguinte mensagem:
#
# Olá, Fulano de Tal
# A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
#
# Escreva um programa que receba (entrada de dados através do teclado) 
# o nome do cliente, o dia de vencimento, o mês de vencimento e o valor 
# da fatura e imprima (saída de dados) a mensagem com os dados recebidos,
#  no mesmo formato da mensagem acima. 



nome = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

saida = "Olá, " + nome
print( saida )

saida = "A sua fatura com vencimento em " + dia + " de " + mes + " no valor de R$ " + valor + " está fechada."
print( saida )