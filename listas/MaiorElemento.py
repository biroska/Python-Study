def maior_elemento(listaNumeros):
    maior = None

    if not listaNumeros:
        return None

    print(listaNumeros)

    maior = listaNumeros[0]
    for i in listaNumeros:

        if ( i > maior ):
            maior = i

    print("Maior numero: {0} \n lista: {1}".format(str(maior), listaNumeros))

    return maior

maior_elemento([-52, -76, -70, -96, 41, -65, -6, 1, -59, 76, -50, 13, 46, 86, -22, -73, -21, 73, 50, 20,
                15, -99, -56, 64, -75, 52, -64, -67, -66, -51, 56, 83, -64, -66, -38, 10, 75, 38, 66, -61,
                -70, -46, -100, -17, 18, -15, 73, -89, -22, 43, 87, 13, 79, -39, -26, 52, -4, -22, 74, -22,
                7, -81, 89, 13, 20, 40, 53, -87, -80, 57, -48, -67, -22, -86, 88, 20, 42, -25, 74, 68,
                -94, 16, 57, -35, 44, -4, -84, -80, -52, -13, 37, 9, 89, -99, 68, -98, -93, 45, 87, -48])
