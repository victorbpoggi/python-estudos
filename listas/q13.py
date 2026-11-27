#Comece com uma lista vazia. Adicione 3 números (escritos no código, não digitados) e mostre a lista no final.
a = []
for i in range(3):
    num = int(input(f"Adicione um número na posição {i+1}: "))
    a.append(num)
print(a)