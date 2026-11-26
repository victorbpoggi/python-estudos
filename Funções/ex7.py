#média de vários alunos
def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3
def situacao(m):
    if m >= 7:
        return "Aprovado"
    elif m >= 5:
        return "Recuperação"
    return "Reprovado" # só chega aqui se nenhum return anterior rodou
# programa principal
qtd = int(input("Quantos alunos? "))
for i in range(qtd):
    nome = input(f"Nome do aluno {i+1}: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    m = media(n1, n2, n3)
    print(f"{nome}: média {m:.1f} - {situacao(m)}")