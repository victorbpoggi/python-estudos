cont = 0
soma = 0
maior = 0
menor = 0
aprovados = 0
while True:
    notas = float(input())
    if notas == -1:
        break
    if notas < 0 or notas > 10:
        print("NOTA INVALIDA")
        continue
    if notas >= 7:
        aprovados += 1
        
    if cont == 0:
        maior = notas
        menor = notas
    else:
        if notas > maior:
            maior = notas
        if notas < menor:
            menor = notas
    cont += 1
    soma += notas
if cont == 0:
    print("NENHUMA NOTA REGISTRADA")
else:
    print(F"MAIOR: {maior:.1f}")
    print(f"MENOR: {menor:.1f}")
    print(f"MEDIA: {soma/cont:.2f}")
    print(f"APROVADOS: {aprovados}")
