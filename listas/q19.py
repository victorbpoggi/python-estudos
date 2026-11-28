#Com uma lista pronta de 4 números, mostre só o primeiro e o último, cada um com uma mensagem tipo Primeiro: 10.
num = [1,2,3,9]
print(f"Primeiro: {num[0]}\nÚltimo: {num[-1]}")

#com len:
print(f"Primeiro: {num[0]}\nÚltimo: {num[len(num) - 1]}") #numa lista de tamanho n, o último índice é sempre n - 1, ou seja, len(numeros) - 1.
