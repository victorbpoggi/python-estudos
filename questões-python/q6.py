#lista claude while #3
cont = 0
soma = 0

while True:
    nota = float(input())
    if nota == -1:
        break
    if nota > 10:
        print("NOTA INVALIDA")
        continue
    cont += 1
    soma += nota
print(f"NOTAS VALIDAS: {cont}")
print(f"MEDIA: {soma/cont:.2f}")