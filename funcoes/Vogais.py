# Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#
#                     EXERCÍCIO 3
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve
# True se ele for uma vogal e False se for uma consoante.
#
# Note que
#
# vogal("a") deve devolver True
#
# vogal("b") deve devolver False
#
# vogal("E") deve devolver True
#
# Os valores True e False devolvidos devem ser do tipo bool (booleanos)
#
# Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto,
# ou seja, precisa estar entre aspas.
#

def vogal( caractere ):

    if ( caractere == "a" or caractere == "A" or
         caractere == "e" or caractere == "E" or
         caractere == "i" or caractere == "I" or
         caractere == "o" or caractere == "O" or
         caractere == "u" or caractere == "U" ):
        return True

    return False

