print("Bem vindo!")
print("Digite 0 para encerrar o programa.")

pedidos = 0
valor_total = 0
pedido_acima_50 = 0

while True:
    valor = float(input(f"Digite o valor do pedido : R$ "))
    if valor == 0:
        break
    
    if valor < 0:
        print("VALOR INVALIDO")
        continue
    
    if valor > 50:
        pedido_acima_50 = pedido_acima_50 + 1
    
    valor_total = valor_total + valor
    pedidos = pedidos + 1

if pedidos == 0:
    print("NENHUM PEDIDO REGISTRADO")

else:
    print(f"TOTAL: R$ {valor_total}")
    print(f"PEDIDOS: {pedidos}")
    print(f"MEDIA: R$ {(valor_total/pedidos):.2f}")
    print(f"ACIMA DE 50: {pedido_acima_50}")
        