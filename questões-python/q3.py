# ex2 slide estrutura de repetição marcelo 
cont = 0
soma = 0

while True:
    valor = float(input("Informe o valor da compra: R$ "))

    if valor == 0:
        break
    if valor < 0:
        print("Valor negativo não é permitido, tente novamente.")
        continue
    cont += 1
    soma += valor
if cont == 0:
    print("Nenhum valor foi recebido.")
else:
    if soma > 1000:
        desconto = [soma - (soma*0.1)]
        print(f"Valor total a pagar: R${desconto}")
    print(f"Valor total a pagar: R${soma}")
