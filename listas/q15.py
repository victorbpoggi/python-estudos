#Faça o mesmo da q14.py, mas lendo 3 números. Regra: você não pode escrever input três vezes, 
#tem que usar um laço.
a = []
for i in range(3):
    num = int(input(f"Digite um número inteiro, na posição {i+1}: "))
    a.append(num)
print(a)

#com while
a = []
i = 0
while i < 3:
    num = int(input(f"Digite um número inteiro, na posição {i+1}: "))
    a.append(num)
    i = i + 1
print(a)