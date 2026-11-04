#Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC
# Resultado:
# T: 2x
# A: 2x
# C: 1x

palavras = input("Digite: ")

print(f"Resultado:\n T: {palavras.count("T")}x\n A: {palavras.count("A")}x\n C: {palavras.count("C")}x")