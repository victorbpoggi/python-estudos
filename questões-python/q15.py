#Uma estação de tratamento reduz gradualmente a dosagem de
#cloro na água ao longo do dia. Escreva um programa que leia a
#dosagem inicial, a dosagem final e o valor da redução aplicada a
#cada etapa (todos inteiros, em mg/L) e exiba, usando while, cada
#dosagem da sequência, da inicial até a final, no formato: "Etapa
#1: 60 mg/L", "Etapa 2: 55 mg/L", e assim por diante. Ao final,
#exiba quantas etapas foram realizadas.
inicial = int(input())
final = int(input())
reducao = int(input())

dosagem = inicial
etapa = 0

while dosagem >= final:
    etapa += 1
    print(f"Etapa {etapa}: {dosagem} mg/L")
    dosagem -= reducao

print(f"Total de etapas: {etapa}")
    
