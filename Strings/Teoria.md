# Alteração de uma string
--> Strings são imutáveis em Python

S = 'Hello world'

print(S[0])

S[0] = 'h'

TypeError: 'str' object does not support item assignment

-- > Se quisermos trabalhar caractere a caractere com uma string, alterando seu valor, teremos que primeiramente transformá-la em uma lista.

# Convertendo uma string em uma lista

L = list('Alô Mundo!')

L[0] = 'a'
print(L)

s = "".join(L)


print(s)


#alô Mundo



--> A função list transforma cada caractere da string em um elemento da lista retornada. Já o método join faz a operação inversa, transformando os elementos da lista em string.

# 7.1 Verificação parcial de strings

Quando você precisar verificar se uma string começa ou termina com alguns caracteres, você pode usar os métodos startswith e endswith. Esses métodos verificam apenas os primeiros (startswith) ou os últimos (endswith) caracteres da string,
retornando True caso sejam iguais ou False em caso contrário.

nome = "João da Silva"

nome.startswith("João")

#True

nome.startswith("joão")

#False

nome.endswith("Silva")

#True

 comparamos “João da Silva” com “joão” e obtivemos **False**. Esse é um detalhe pequeno, mas importante, pois *startswith* e *endswith*
consideram letras maiúsculas e minúsculas como letras diferentes.
Você pode resolver esse tipo de problema convertendo a string para maiúsculas ou
minúsculas antes de realizar a comparação. O método *lower* retorna uma cópia da
string com todos os caracteres minúsculos, e o método *upper* retorna uma cópia
com todos os caracteres maiúsculos. Veja os exemplos

##  Exemplos de conversão em maiúsculas e minúsculas

s = "O Rato roeu a roupa do Rei de Roma"
>>> s.lower()
'o rato roeu a roupa do rei de roma'
>>> s.upper()
'O RATO ROEU A ROUPA DO REI DE ROMA'
>>> s.lower().startswith("o rato")
True
>>> s.upper().startswith("O RATO")
True

Não se esqueça de comparar com uma string onde todos os caracteres são maiúsculos ou minúsculos, dependendo se você utilizou *upper* ou *lower*, respectivamente. Outra forma de verificar se uma palavra pertence a uma string é utilizando o operador **in**. Vejamos os exemplo

## Pesquisa de palavras em uma string usando in

>>> s="Maria Amélia Souza"
>>> "Amélia" in s
True
>>> "Maria" in s
True
>>> "Souza" in s
True
>>> "a A" in s
True
>>> "amélia" in s
False

Você também pode testar se uma string não está contida em outra, utilizando **not in**

## Pesquisa de palavras em uma string usando not in 

>>> s="Todos os caminhos levam a Roma"
>>> "levam" not in s
False
>>> "Caminhos" not in s
True
>>> "AS" not in s
True

Veja que aqui também letras maiúsculas e minúsculas são diferentes. Você pode combinar lower e upper com in e not in para ignorar esse tipo de diferença.

##  Combinação de lower e upper com in e not in

>>> s="João comprou um carro"
>>> "joão" in s.lower()
True
>>> "CARRO" in s.upper()

True
>>> "comprou" not in s.lower()
False
>>> "barco" not in s.lower()
True

O operador in também pode ser utilizado com listas normais, facilitando, assim, a pesquisa de elementos dentro de uma lista.

# 7.2 Contagem

Se você precisar contar as ocorrências de uma letra ou palavra em uma string,
utilize o método *count*. Veja o exemplo

##  Contagem de letra e palavras

>>> t="um tigre, dois tigres, três tigres"
>>> t.count("tigre")
3
>>> t.count("tigres")
2
>>> t.count("t")
4
>>> t.count("z")
0

## 7.3 Pesquisa de strings

Para pesquisar se uma string está dentro de outra e obter a posição da primeira ocorrência, você pode utilizar o método *find*.

## Pesquisa de strings com find

>>> s="Alô mundo"
>>> s.find("mun")
4
>>> s.find("ok")
-1

Caso a string seja encontrada, você obterá um valor maior ou igual a zero, ou
-1, em caso contrário. Observe que o valor retornado, quando maior ou igual a
zero, é igual ao índice que pode ser utilizado para obter o primeiro caractere da
string procurada.
Se o objetivo for pesquisar, mas da direita para a esquerda, utilize o método *rfind*,
que realiza essa tarefa.

##  Pesquisa de strings com rfind
>>> s="Um dia de sol"
>>> s.rfind("d")
7
>>> s.find("d")
3

Tanto find quanto *rfind* suportam duas opções adicionais: início (*start*) e fim
(*end*). Se você especificar início, a pesquisa começará a partir dessa posição. Se
você especificar o fim, a pesquisa utilizará essa posição como último caractere a
considerar na pesquisa.

##  Pesquisa de strings, limitando o início ou o fim

>>> s="um tigre, dois tigres, três tigres"
>>> s.find("tigres")
15
>>> s.rfind("tigres")
28
>>> s.find("tigres",7) #início=7
15
>>> s.find("tigres",30) #início=30
-1
>>> s.find("tigres",0,10) #início=0 fim=10
-1

Podemos usar o valor retornado por *find* e *rfind* para achar todas as ocorrências da string. Por exemplo, o programa da listagem.

##  Pesquisa de todas as ocorrências

s="um tigre, dois tigres, três tigres"
p=0
while(p>-1):
    p=s.find("tigre", p)
    if p>=0:
        print("Posição: %d" % p)
        p+=1

Posição: 3
Posição: 15
Posição: 28