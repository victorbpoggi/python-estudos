# acumuladores 

#  Soma de 10 números

n = 1
soma = 0 
while n <= 10:
    x = int(input(f"Digite o {n}º número: "))
    soma = soma + x
    n = n + 1
print(f"Soma: {soma}")

#Cálculo de média com acumulador

n = 1
soma = 0
while n <= 5:
    x = int(input(f"Digite o {n}º número: "))
    soma = soma + x
    n = n + 1
print(f"Média: {(soma/n):.2f}")
