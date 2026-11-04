## Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
#1ª string: CTA
#2ª string: ABC
#3ª string: BT
#A ordem dos caracteres da terceira string não é importante.

frase = input("Digite: ")
frase2 = input("Digite: ")

frase3 = ""

for letra in frase:
    if letra not in frase2:
        frase3 += letra

for letra in frase2:
    if letra not in frase:
        frase3 += letra

print(f"3ª string: {frase3}")