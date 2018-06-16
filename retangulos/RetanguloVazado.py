def printRetanguloCheio( largura, altura ):

    countL = 1
    countA = 1

    while countA <= altura:
        while countL <= largura :

            if  ( countA == 1 or countA == altura ):
                print("#", end="")
            else:
                if ( countL == 1 or countL == largura ):
                    print("#", end="")
                else:
                    print(" ", end="")

            countL +=1

        countA += 1
        countL = 1
        print("")



largura = int( input("Forneca a largura: ") )
altura = int( input("Forneca a altura: ") )

printRetanguloCheio( largura, altura)