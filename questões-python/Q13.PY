#Leia os tempos (em segundos) dos corredores de uma prova até que seja digitado 0. Tempos
#negativos são inválidos: imprima TEMPO INVALIDO. Os corredores válidos são numerados pela
#ordem em que foram digitados (1, 2, 3...). Mostre o melhor tempo (o menor) e o número do
#corredor que fez esse tempo, o pior tempo e a média. Se nenhum tempo válido for registrado,
#imprima NENHUM CORREDOR REGISTRADO.
cont = 0
maior_tempo = 0
menor_tempo = 0
soma_tempo = 0

while True:
    tempo = float(input())
    if tempo == 0:
        break
    if tempo < 0:
        print("TEMPO INVALIDO")
        continue
    if cont == 0:
        maior_tempo = tempo
        menor_tempo = tempo
        ordem = 1
    else:
        if tempo > maior_tempo:
            maior_tempo = tempo
        if tempo < menor_tempo:
            menor_tempo = tempo
            ordem = cont + 1
        
    soma_tempo += tempo
    cont += 1
if cont == 0:
    print("NENHUM CORREDOR REGISTRADO")
else:
    print(f"MELHOR TEMPO: {menor_tempo:.1f} (CORREDOR {ordem})")
    print(f"PIOR TEMPO: {maior_tempo:.1f}")
    print(f"MEDIA: {soma_tempo/cont:.2f}")


