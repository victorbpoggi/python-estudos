#Crie uma lista fixa com 8 números à sua escolha. Peça um número ao usuário e use for...else para dizer:

#se encontrou: "Encontrado na posição X" (posição começando em 1)
#se não encontrou: "Número não está na lista"

#O programa deve repetir até o usuário digitar 0.

x = [10,20,30,40,50,60,70,80]
for i in x:
    while True:
        num = int(input("Digite um número que talvez esteja dentro da lista: "))
        if num == 0:
            break
        if i == num:
            print(f"Número encontrado na posição {i}")
            continue