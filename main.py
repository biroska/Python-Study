print("Hello World!")

print(3 < 5)

x = 50

y = 20

aux = x

x = y

y = aux

print("X: ", x, " Y ", y)


def total_Caracteres(x, y, z):
    return len(x) + len(y) + len(z)

print( total_Caracteres("123", "123", "123") )

def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)