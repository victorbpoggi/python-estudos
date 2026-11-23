#Um petshop atende 5 cachorros por tarde. Faça um programa que solicite ao
#usuário o código do serviço efetuado:
#1 - banho;
#2 - tosa;
#3 - banho e tosa;
#4- outros.

#Por fim, exiba a quantidade de solicitações para cada um dos serviços.
#Se digitar um valor fora do intervalo 1-4, notificar.
#Utilize o for.

banho = 0
tosas = 0
banho_tosa = 0
outros = 0

for i in range(5):
    codigo = int(input("Informe o código que será utilizado: "))
    if codigo == 1:
        banho += 1
    elif codigo == 2:
        tosas += 1
    elif codigo == 3:
        banho_tosa += 1
    elif codigo == 4:
        outros += 1
    else:
        print("Digite entre 1-4")
print(f"Foram solicitados {banho} banhos.")
print(f"Foram solicitados {tosas} tosas.")
print(f"Foram solicitados {banho_tosa} banhos e tosas.")
print(f"Foram solicitados {outros} outros serviços.")

