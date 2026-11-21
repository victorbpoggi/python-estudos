cont = 0
maior = 0
menor = 0

while True:
    altura = float(input())
    if altura == 0:
        break
    if altura < 0.50 or altura > 2.50:
        print("ALTURA INVALIDA")
        continue
    if cont == 0:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
    cont += 1
print(f"MAIOR: {maior}\nMENOR: {menor}\nDIFERENÇA: {maior - menor:.2f}")