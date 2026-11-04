# Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
# 1ª string: AATTCGAA
# 2ª string: TG
# 3ª string: AC
# Resultado: AAAACCAA

frase = input("1ª string: ")
frase2 = input("2ª string: ")
frase3 = input("3ª string: ")

resultado = ""

for letra in frase:
    if letra in frase2:
        posicao = frase2.index(letra)
        resultado += frase3[posicao]
    else:
        resultado += letra

print(f"Resultado: {resultado}")