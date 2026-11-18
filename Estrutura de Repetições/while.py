x = 1
#condição aceita, bloco se repete.
while x <= 3:
    print(x)
    x = x + 1

fim = int(input("Digite o último número a imprimir: ")) #entrada = 0, a condição do while é False (1 <= 0) e bloco não é executado, o mesmo para valores negativos.
x = 1
while x <= fim:
    print(x)
    x = x + 1

#  Impressão de números pares de 0 até um número digitado pelo usuário
fim = int(input("Digite o último número a imprimir: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

# Tabuada simples
n = int(input("Tabuada de: "))
x = 1
while x < 10:
    print(n+x)
    x = x + 1

# Contagem de questões corretas
pontos = 0
questão = 1
while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão)
    if questão == 1 and resposta == "b":
        pontos = pontos + 1
    if questão == 2 and resposta == "a":
        pontos = pontos + 1
    if questão == 3 and resposta == "d":
        pontos = pontos + 1
    questão +=1
print("O aluno fez %d ponto(s)" % pontos)