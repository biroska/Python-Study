def isPrimo( numeroEntrada ):

    divisor = numeroEntrada - 1

    while divisor > 1:

        if ( numeroEntrada % divisor == 0):
            return False

        divisor -= 1

    return True

def n_primos( numeroEntrada ):

    qtdPrimos = 0
    index = 2

    if ( numeroEntrada < 2 ):
        return 0

    while (index <= numeroEntrada):

        if ( isPrimo( index )  ):
            qtdPrimos += 1

        index += 1

    return qtdPrimos


numero = int( input("Forneca o limite: ") )

print( n_primos( numero ) )