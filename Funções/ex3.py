#Escreva uma função que retorne o maior de dois números.
##Valores esperados:
#máximo(5,6) == 6
#máximo(2,1) == 2
#máximo(7,7) == 7

def maximo(a, b):
    if a > b:
        return a
    return b
print(maximo(5,6) == 6)
print(maximo(2,1) == 2)
print(maximo(7,7) == 7)