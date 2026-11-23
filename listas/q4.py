#Desenvolva um programa utilizando o for que faça a tabuada de um número
#inteiro que será digitado pelo usuário. Mas a tabuada não deve necessariamente
#iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados pelo
#usuário.
#Segue um exemplo:
#Montar a tabuada do: 5
#Começar por: 4
#Terminar em: 7

#Saída de dados:
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35

tabuada = int(input("Montar tabuada do: "))
começo = int(input("Começar por: "))
fim = int(input("Terminar em: "))

for i in range(começo,fim + 1):
    print(f"{tabuada} X {i} = {tabuada * i}")



