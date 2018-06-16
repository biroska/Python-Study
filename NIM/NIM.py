#  Este programa contempla a resolução do primeiro exercício opcional do curso:
#     Introdução à Ciência da Computação com Python Parte 1
# Disponível no coursera.
#                     EXERCÍCIO OPCIONAL
# Objetivo
# Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM
# contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.
#
# Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada.
# Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
#
# Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida
# com a frase "Você começa"
# Caso contrário, o computador toma a inciativa de começar o jogo.
# Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número
# de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível,
# deverá tirar o número máximo de peças possíveis.
#
# Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.
#
# Seu Programa
# Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o
# jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente
#  às especificações descritas até agora.
#
# Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a
# seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o
#  problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente
# o que está definido abaixo para que a correção automática do trabalho funcione corretamente.
#
# O programa deve implementar:
#
# Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e
# devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.
# Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua
# jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve
# devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
# Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores
# de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às
# duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora,
# como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja,
# quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida,
# essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
# Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente
# no tabuleiro e qual é o máximo de peças a retirar em cada jogada.
#
# Cuidado: o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição
# de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função). Se seu programa
#  usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.
#
# Campeonatos
# Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor
#  jogador. Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função
#  chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar
#  o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma
#
# Placar: Você ??? X ??? Computador
#
#

def valida_config_pecas( qtdPecas, limitePecasRetirar ):
    if ( limitePecasRetirar > qtdPecas ):
        return False

    return True

def computadorInicia( qtdPecas, limitePecasRetirar  ):

    if ( qtdPecas % ( limitePecasRetirar + 1 ) == 0 ):
        return False
    else:
        return True

#
# Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador
# informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido,
#  a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
#
def  usuario_escolhe_jogada ( pecasRestantes, limitePecasRetirar ):

    jogada = int( input( "Quantas peças você vai tirar?" ) )
    quebraLinha()

    while ( jogada > pecasRestantes or jogada < 1 or jogada > limitePecasRetirar ):
        print("Oops! Jogada inválida! Tente de novo.")
        quebraLinha()
        jogada = int( input( "Quantas peças você vai tirar?" ) )
        quebraLinha()

    return jogada
#
# Uma função computador_escolhe_jogada que recebe, como parâmetros,
# os números n e m descritos acima e devolve um inteiro correspondente à
# próxima jogada do computador de acordo com a estratégia vencedora.
#
def computador_escolhe_jogada ( pecasRestantes, limitePecasRetirar ):

    jogada = 1
    count = 0

    if ( pecasRestantes <= limitePecasRetirar  ):
        return pecasRestantes

    while ( jogada > 0 ):

        jogada = limitePecasRetirar - count

        if ( ( pecasRestantes - jogada ) % ( limitePecasRetirar + 1 ) == 0):
            return jogada

        count += 1

    quebraLinha()

    return limitePecasRetirar

def imprimeJogada(isComputador, jogada, pecasRestantes ):

    textoJogada = ""
    textoRestantes = ""

    if ( isComputador ):
        textoJogada = "O computador tirou "
    else:
        textoJogada = "Você tirou "

    if ( jogada > 1 ):
        textoJogada = textoJogada + str(jogada) + " peças."
    else:
        textoJogada = textoJogada + "uma peça."

    if ( pecasRestantes > 0 ):
        if (pecasRestantes > 1):
            textoRestantes = "Agora restam " + str(pecasRestantes) + " peças no tabuleiro."
        else:
            textoRestantes = "Agora resta apenas uma peça no tabuleiro."

    print( textoJogada )
    print( textoRestantes )

def quebraLinha():
    print("")

def partida():
    #
    # Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores
    #  de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas
    # às duas funções anteriores). A escolha da jogada inicial deve ser feita em função
    # da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o
    #  estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam
    #  na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem
    # "O computador ganhou!" ou "Você ganhou!" conforme o caso.
    #

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # while ( not valida_config_pecas( n, m) ):
    #     n = int(input("Quantas peças? "))
    #     m = int(input("Limite de peças por jogada? "))

    quebraLinha()

    pecasRestantes = n
    jogada = 0

    isComputador = computadorInicia(n, m)

    if ( isComputador ):
        print("Computador começa!")
    else:
        print("Voce começa!")

    while ( pecasRestantes > 0 ):

        if ( isComputador ):
            jogada = computador_escolhe_jogada( pecasRestantes, m )
        else:
            jogada = usuario_escolhe_jogada( pecasRestantes, m )

        pecasRestantes -= jogada

        imprimeJogada( isComputador, jogada, pecasRestantes )

        isComputador = not isComputador


    if ( not isComputador ):
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Você ganhou!")

    return not isComputador


def campeonato():

    rodada = 1
    vitComputador = 0
    vitJogador = 0

    while ( rodada <= 3 ):
        print("**** Rodada " + str( rodada ) + " ****")

        if ( partida() ):
            vitComputador += 1
        else:
            vitJogador += 1

        rodada += 1

    print("**** Final do campeonato! ****")

    print("Placar: Você " + str( vitJogador ) +" X " + str( vitComputador ) +" Computador")


def menuPrincipal():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")

    print("1 - para jogar uma partida isolada")
    opcao = int( input("2 - para jogar um campeonato 2") )

    if ( opcao == 1 ):
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonato!")
        campeonato()

menuPrincipal()
