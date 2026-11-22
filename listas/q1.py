#ex Listagem 6.5 – Cálculo da média
notas = [6,7,5,8,9]
soma = 0
x = 0
while x < 5: #passa por todos os índices dentro de notas
    soma += notas[x] #cada índice soma com soma = 0
    x+=1 #contador
print(f"Média: {soma/x:.2f}")

#Listagem 6.6 – Cálculo da média com notas digitadas
notas = [0,0,0,0,0]
soma = 0
x = 0
while x<5:
    notas[x]=float(input(f"Nota {x+1}: "))
    soma+=notas[x]
    x=x+1
x=0
while x<5:
    print(f"Nota {x+1}: {notas[x]:.2f}")
    x=x+1
media = soma / 5
print(f"Média: {media:.2f}")

