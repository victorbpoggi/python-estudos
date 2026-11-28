#Leia 2 valores com casas decimais (ex: 3.50), guarde numa lista e mostre um embaixo do outro.
numeros = []
for i in range(2):
    decimal = float(input("Digite um valor em decimal: "))
    numeros.append(decimal)
for x in numeros:
    print(f"{x:.2f}")