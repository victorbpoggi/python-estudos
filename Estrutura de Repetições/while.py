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