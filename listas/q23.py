#Uma loja anotou a quantidade de unidades em estoque de 5 produtos ao longo do dia, mas um dos valores foi digitado errado. Escreva um programa em Python que:

#Leia 5 valores inteiros e guarde-os em uma lista.

#Exiba a lista original na tela.

#Leia o índice que deve ser corrigido e valide se ele é válido usando if e len(lista).

#Se o índice for válido, leia o novo valor, faça a substituição na lista e exiba a lista corrigida; se for inválido, mostre uma mensagem de aviso.
estoque = []
for i in range(5):
    valores = int(input("Digite a quantidade de unidades em estoque: "))
    estoque.append(valores)
print(f"Lista original: {estoque}")
indice = int(input("Digite o índice que precisa ser corrigido entre 0-4: "))
if 0 <= indice <= len(estoque) - 1:
    novo_valor = int(input("Digite a nova unidade no estoque: "))
    estoque[indice] = novo_valor
    print(f"Lista atualizada: {estoque}")
else: 
    print(f"índice inválido! Digite entre 0 e {len(estoque) - 1}")
