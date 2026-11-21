cont = 0
soma = 0
compras_acima_100 = 0
maior_compra = 0
while True:
    compra = float(input())
    if compra == 0:
        break
    if compra < 0:
        print("VALOR INVALIDO")
        continue
    if compra > 100:
        compras_acima_100 += 1
    if cont == 0:
        maior_compra = compra
    else:
        if compra > maior_compra:
            maior_compra = compra
    cont += 1
    soma += compra
if cont == 0:
    print("NENHUMA COMPRA REGISTRADA")
else:
    print(F"TOTAL: R${soma:.2f}")
    print(f"COMPRAS: {cont}")
    print(f"MEDIA: {soma/cont:.2f}")
    print(f"ACIMA DE 100: {compras_acima_100}")
    print(f"MAIOR COMPRA: R$ {maior_compra}")