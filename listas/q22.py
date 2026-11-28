#Mesma lista de cores: peça um índice e uma nova cor, faça a substituição e mostre a lista atualizada.
cores = ["azul","verde","preto","branco"]
indice = int(input("Escolha um índide da lista: "))
cor = input("Digite uma cor: ")
cores[indice] = cor
print(f"Lista atualizada: {cores}")