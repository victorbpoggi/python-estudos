i = 0
soma = 0
while True:
    num = int(input(f"Digite o número: "))
    if num == 0:
        break
    soma = soma + num
    i = i + 1
print(f"Números digitados: {i}")
print(f"Soma: {soma}")
print(f"Média aritmética: {soma/i:.2f}")