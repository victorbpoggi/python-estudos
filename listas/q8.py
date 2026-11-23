#Leia as notas de 6 alunos e guarde todas numa lista. No final, mostre:

#todas as notas na mesma linha, separadas por espaço
#a maior nota
#quantos alunos ficaram com nota maior ou igual a 7

#Exemplo de saída:

#Notas: 5.0 8.5 7.0 3.5 9.0 6.0
#Maior nota: 9.0
#Aprovados: 3

notas = []
maior_nota = 0
aprovados = 0
for i in range(1,7):
    nota = float(input("Digite a sua nota: "))
    while nota < 0 or nota > 10:
        print("Notas inválidas! Digite entre 0-10.")
        nota = float(input("Digite a sua nota: "))
    notas.append(nota)
    if nota >= 7:
        aprovados += 1
    
    if i == 1:
        maior_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
print("Notas:", end=" ")
for v in notas:
    print(v, end=" ")
print()
print(f"Maior nota: {maior_nota:.1f}")
print(f"Aprovados: {aprovados}")