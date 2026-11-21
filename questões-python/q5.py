cont = 1
soma = 0
while True:
    num = float(input())
    if num == 0:
        break
    cont += 1
    soma += num
print(f"QUANTIDADE: {cont}")
print(f"MEDIA: {soma/cont:.2f}")