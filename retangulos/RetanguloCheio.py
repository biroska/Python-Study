def printRetanguloCheio( largura, altura ):

    countL = 1
    countA = 1
    while countA <= altura:
        while countL <= largura :
            print("#", end="")
            countL +=1

        countA += 1
        countL = 1
        print("")



largura = int( input("Forneca a largura: ") )
altura = int( input("Forneca a altura: ") )

printRetanguloCheio( largura, altura)