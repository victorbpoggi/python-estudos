dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0
resto = dividendo

while resto >= divisor:
    resto = resto - divisor
    quociente = quociente + 1

print(f"Quociente (divisão inteira): {quociente}")
print(f"Resto: {resto}")