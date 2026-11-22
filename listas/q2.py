#Exercício 6.1
notas = [0,0,0,0,0,0,0] #indice 0 a 6
soma = 0
x = 0
while x < 7:
    notas[x]=float(input())
    soma = soma + notas[x]
    x=x+1
x = 0
while x < 7:
    print(f"NOTA {x+1}: {notas[x]:.2f}")
    x=x+1
media = soma / 7
print(f"MEDIA: {media:.2f}")
