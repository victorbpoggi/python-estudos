maior = 0
menor = 0
cont = 0
while True:
    num = float(input())
    if num == 0:
        break
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
print(f"MAIOR: {maior} \nMENOR: {menor}")