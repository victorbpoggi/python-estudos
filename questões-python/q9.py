maior = 0
cont = 0
while True:
    num = int(input())
    if num == 0:
        break
    if cont == 0:
        maior = num
    else: 
        if num > maior:
            maior = num
    cont += 1
print(F"MAIOR: {maior}")