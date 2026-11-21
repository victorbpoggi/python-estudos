print("Pressione -1 para encerrar o programa.")

soma = 0
cont = 1

while True:
    nota = float(input("Informe o valor da nota do aluno: "))

    if nota == -1:
        break
    soma = soma + nota
    cont = cont + 1

print(f"Foram recebidas {cont} notas.")
print(f"Média: {soma/cont:.2f}")
