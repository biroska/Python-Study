def obter_lista():

    entrada = -1
    listaRetorno = []

    while ( entrada != 0 ) :
        entrada = int( input('Digite um número: ') )

        if ( entrada != 0 ):
            listaRetorno.append( entrada )

    return listaRetorno



lista = obter_lista()

for x in reversed(lista):
    print(x)