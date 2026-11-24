# listas !

#lista vazia
L = [] #os colchetes após a atribuição servem para indicar que L é uma lista e vazia pq n tem nenhum valor dentro dela.

#lista com 3 elementos e acesso a uma lista

   #0 #1 #2
Z =[15,8,9]
#tamanho = 3
print(Z[0])
print(Z[1])
print(Z[2])

# Modificação de uma lista
Z[0]=7
print(Z[0]) #7
print(Z) #[7,8,9]

#trabalho com índices
numeros = [0,0,0,0,0]
x = 0
while x < 5:
    numeros[x] = int(input(f"Número {x+1}: ")) #adicionamos 1 a x, pois não é normal começar a contar a partir do 0.
    x = x + 1
print(numeros)
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido - 1]}") #fizemos a operação inversa. (2-1) = índice 1 = 20.

#Cópia e fatiamento de listas
#Embora listas em Python sejam um recurso muito poderoso, todo poder traz responsabilidades. Amei essa frase kkkkk

#Um dos efeitos colaterais de listas aparece quando tentamos fazer cópias. 

L = [1,2,3,4,5]
V=L
print(L)
print(V)
V[0] = 6
print(V)
print(L)

#Adição de elementos

a = []
a.append("Victor")
a.append(100)
print(a)

# Adição de elementos à lista
L = []
while True:
    n=int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)
x=0       #ex: 3
while x <= len(L): #x < len(L), pois não sabemos quantos elementos a lista vai ter
    print(L[x])
    x=x+1

# Impressão de todos os elementos da lista com for
c = [33 , 12, 7]
for v in c:
    print(v)

#Uso da função range #a função range n retorna uma lista mas sim um gerador.
for v in range(10):
    print(v)

#Uso da função range com intervalos
for v in range(5, 8):
    print(v)

# Uso da função range com saltos
for t in range(3,33,3):
    print(t, end=" ")
print()
# Enumerate
# Impressão de índices usando a função enumerate
c = [33 , 12, 7]
for x, v in enumerate(c):
    print(f"[x,v] {x,v}")

#  Pesquisa usando for
L=[7,9,10,12]
p=int(input("Digite um número a pesquisar:"))
for e in L:
    if e == p:
        print("Elemento encontrado!")
        break 
else: 
    print("Elemento não encontrado.")





