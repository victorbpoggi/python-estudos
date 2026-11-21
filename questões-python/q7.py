#lista claude while #4
soma = 0
maiores = 0
menores = 0


while True:
    idade = int(input())
    if idade == 0:
        break
    if idade < 0:
        print("IDADE INVALIDA")
        continue
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(F"MAIORES: {maiores}")
print(f"MENORES: {menores}")