#Crie um programa que leia o ano de nascimento de cinco pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
#maiores de idade.

#from datetime import date

#ano_atual = date.today().year
from datetime import date
menor_idade = 0
maior_idade = 0
ano_atual = date.today().year
#ano atual = 2026

for v in range(1,6):
    ano = int(input("Você nasceu em qual ano? \n"))
    if ano_atual - ano >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
    
print(f"{menor_idade} são menor de idade e {maior_idade} são maior de idade")
