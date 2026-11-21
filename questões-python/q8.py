#lista claude while #5
cont = 0
soma = 0
maior = 0 
menor = 0
while True:
    temp = float(input())
    if temp == 999:
        break
    if temp < -50 or temp > 60:
        print("TEMPERATURA INVALIDA")
        continue

    if cont == 0:
        maior = temp
        menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
    soma += temp
    cont += 1
if cont == 0:
    print("NENHUMA TEMPERATURA REGISTRADA")
else:
    print(f"MAIOR: {maior:.1f}")
    print(f"MENOR: {menor:.1f}")
    print(f"MEDIA: {soma / cont:.1f}")        