def soma_elementos(listaNumeros):
    listaRetorno = []

    if not listaNumeros:
        return 0

    soma = sum( listaNumeros )

    print("Soma: {0} \n lista: {1}".format(soma, listaNumeros) )

    return soma


# soma_elementos( [2.5, 3, 4, -5] )
