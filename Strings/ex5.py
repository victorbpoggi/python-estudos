## Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
# 1ª string: AATTGGAA
# 2ª string: TG
# 3ª string: AAAA

frase = input("Digite: ")
frase2 = input("Digite: ")

frase3 = ""

for letra in frase:
    if letra not in frase2:
        frase3 += letra

print(f"3ª string: {frase3}")

