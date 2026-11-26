# Função saudacao(nome) que imprime "Bom dia, Nome!" com a 1ª letra maiúscula.
def saudacao(nome):
    return (f"Bom dia, {nome.title()}!") #Dá pra usar métodos dentro das chaves do f-string, tipo {variavel.metodo()}. No caso, title!
nome = input("Digite um nome: ")
print(saudacao(nome))
print(saudacao("victor"))
