#trabalho com índices
numeros = [0,0,0,0,0]
x = 0
while x < 5:
    numeros[x] = int(input(f"Número {x+1}: ")) #adicionamos 1 a x, pois não é normal começar a contar a partir do 0.
    x = x + 1
print(numeros)
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido - 1]}") #fizemos a operação inversa. (2-1) = índice 1 = 20.



