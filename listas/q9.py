#A cantina atende 8 alunos. Cada um escolhe um lanche:

#1: Coxinha (R$ 5,00)
#2: Pastel (R$ 6,00)
#3: Suco (R$ 4,00)

#Se o código for inválido, avise e pergunte de novo, sem perder o aluno. No final, mostre quantos itens de cada lanche foram vendidos e o total arrecadado em reais, 
# com 2 casas decimais.

#Coxinhas: 3 | Pastéis: 2 | Sucos: 3
#Total arrecadado: R$ 39.00
print("Escolha o código do produto")
total = 0
coxinhas = 0
pasteis = 0
sucos = 0
for i in range(1,9):
    code = int(input("Digite o código do produto: "))
    while code < 1 or code > 3:
        print("Código errado, digite entre 1-3.")
        code = int(input("Digite o código do produto: "))
    if code == 1:
        valor = 5
        coxinhas += 1
    elif code == 2:
        valor = 6
        pasteis += 1
    else:
        valor = 4
        sucos += 1
    total = total + valor
print(f"Coxinhas: {coxinhas} | Pastéis: {pasteis} | Sucos: {sucos}")
print(f"Total arrecadado: R$ {total:.2f}")
