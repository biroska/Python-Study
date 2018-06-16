def isHipotenusa( hipotenusa ):

    a = b = 1

    while a < hipotenusa:

        while b < hipotenusa:

            if ( a*a + b*b == hipotenusa*hipotenusa ):
                return True

            b += 1

        a += 1
        b = 1

    return False


def soma_hipotenusas( limite ):

    count = 1
    soma = 0;

    while count <= limite :

        if ( isHipotenusa( count ) ):
            soma += count

        count +=1

    return soma


limite = int( input("Forneca o limite: ") )

print( soma_hipotenusas( limite) )