deposito_inicial = float(input(f"Digite o seu depósito inicial: R$ "))
taxa = float(input("Informe a taxa de juros mensal (%): "))

saldo = deposito_inicial
x = 1
total_juros = 0

while x <= 24:

    juros = saldo * (taxa / 100)
    saldo = saldo + juros 
    total_juros = total_juros + juros
    print(f"Mês {x}: R$ {saldo:.2f}")
    x = x + 1

print(f"Total ganho com juros:R$ {(total_juros):.2f}")
