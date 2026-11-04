# Alteração de uma string
--> Strings são imutáveis em Python

--> Índices são posições dos caracteres na string;

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

 s.lower()

'o rato roeu a roupa do rei de roma'

s.upper()

'O RATO ROEU A ROUPA DO REI DE ROMA'

s.lower().startswith("o rato")

True

s.upper().startswith("O RATO")

True

Não se esqueça de comparar com uma string onde todos os caracteres são maiúsculos ou minúsculos, dependendo se você utilizou *upper* ou *lower*, respectivamente. Outra forma de verificar se uma palavra pertence a uma string é utilizando o operador **in**. Vejamos os exemplo

## Pesquisa de palavras em uma string usando in


s="Maria Amélia Souza"

"Amélia" in s

True

"Maria" in s

True

"Souza" in s

True

"a A" in s

True

"amélia" in s

False

Você também pode testar se uma string não está contida em outra, utilizando **not in**

## Pesquisa de palavras em uma string usando not in 

s="Todos os caminhos levam a Roma"

"levam" not in s

False

"Caminhos" not in s

True

"AS" not in s

True

Veja que aqui também letras maiúsculas e minúsculas são diferentes. Você pode combinar lower e upper com in e not in para ignorar esse tipo de diferença.

##  Combinação de lower e upper com in e not in

s="João comprou um carro"

"joão" in s.lower()

True

"CARRO" in s.upper()

True

"comprou" not in s.lower()

False

"barco" not in s.lower()

True

O operador in também pode ser utilizado com listas normais, facilitando, assim, a pesquisa de elementos dentro de uma lista.

# 7.2 Contagem

Se você precisar contar as ocorrências de uma letra ou palavra em uma string,
utilize o método *count*. Veja o exemplo

##  Contagem de letra e palavras

t="um tigre, dois tigres, três tigres"
t.count("tigre")
3
t.count("tigres")
2
t.count("t")
4
t.count("z")
0

## 7.3 Pesquisa de strings

Para pesquisar se uma string está dentro de outra e obter a posição da primeira ocorrência, você pode utilizar o método *find*.

## Pesquisa de strings com find

 s="Alô mundo"

 s.find("mun")
 
 4

s.find("ok")

-1

Caso a string seja encontrada, você obterá um valor maior ou igual a zero, ou
-1, em caso contrário. Observe que o valor retornado, quando maior ou igual a
zero, é igual ao índice que pode ser utilizado para obter o primeiro caractere da
string procurada.
Se o objetivo for pesquisar, mas da direita para a esquerda, utilize o método *rfind*,
que realiza essa tarefa.

##  Pesquisa de strings com rfind
s="Um dia de sol"

s.rfind("d")

7

s.find("d")

3

Tanto find quanto *rfind* suportam duas opções adicionais: início (*start*) e fim
(*end*). Se você especificar início, a pesquisa começará a partir dessa posição. Se
você especificar o fim, a pesquisa utilizará essa posição como último caractere a
considerar na pesquisa.

##  Pesquisa de strings, limitando o início ou o fim

s="um tigre, dois tigres, três tigres"
 
 s.find("tigres")

15

s.rfind("tigres")

28

s.find("tigres",7) #início=7

15

s.find("tigres",30) #início=30

-1

s.find("tigres",0,10) #início=0 fim=10

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

# 7.4 Posicionamento de strings

Python também traz métodos que ajudam a apresentar strings de formas mais
interessantes. Vejamos o método center, que centraliza a string em um número
de posições passado como parâmetro, preenchendo com espaços à direita e à
esquerda até que a string esteja centralizada.

##  Centralização de texto em uma string

s="tigre"

print("X"+s.center(10)+"X")

X tigre X

print("X"+s.center(10,".")+"X")

X..tigre...X

Se, além do tamanho, você também passar o caractere de preenchimento, este será
utilizado no lugar de espaços em branco.
Se o que você deseja é apenas completar a string com espaços à esquerda, você
pode utilizar o método *ljust*. Se deseja completar com espaços à direita, utilize
*rjust*

##  Preenchimento de strings com espaços

 s="tigre"

s.ljust(20)

'tigre               '

s.rjust(20)

'               tigre'

s.ljust(20,".")

'tigre...............'

s.rjust(20,"-")

'---------------tigre'

Essas funções são úteis quando precisamos criar relatórios ou simplesmente
alinhar a saída dos programas.

# 7.5 Quebra ou separação de strings

O método split quebra uma string a partir de um caractere passado como parâmetro, retornando uma lista com as substrings já separadas. Veja um exemplo na listagem:

## Separação de strings

s="um tigre, dois tigres, três tigres"

s.split(",")

['um tigre', ' dois tigres', ' três tigres']

s.split(" ")

['um', 'tigre,', 'dois', 'tigres,', 'três', 'tigres']

s.split()

['um', 'tigre,', 'dois', 'tigres,', 'três', 'tigres']

Observe que o caractere que utilizamos para dividir a string não é retornado na
lista, ou seja, ele é utilizado para separar a string e depois descartado.
Se você deseja separar uma string, com várias linhas de texto, você pode utilizar
o método splitlines

##  Quebra de strings de várias linhas

m="Uma linha\noutra linha\ne mais uma\n"

 m.splitlines()

['Uma linha', 'outra linha', 'e mais uma']

# 7.6 Substituição de strings

Para substituir trechos de uma string por outros, utilize o método replace. Com
o método replace, o primeiro parâmetro é a string a substituir; e o segundo, o
conteúdo que a substituirá. Opcionalmente, podemos passar um terceiro parâmetro que limita quantas vezes queremos realizar a repetição. Vejamos alguns exemplos:

## Substituição de strings

 s="um tigre, dois tigres, três tigres"

s.replace("tigre", "gato")

'um gato, dois gatos, três gatos'

s.replace("tigre", "gato", 1)

'um gato, dois tigres, três tigres'

s.replace("tigre", "gato", 2)

'um gato, dois gatos, três tigres'

s.replace("tigre", "")

'um , dois s, três s'

s.replace("", "-")

'-u-m- -t-i-g-r-e-,- -d-o-i-s- -t-i-g-r-e-s-,- -t-r-ê-s- -t-i-g-r-e-s-'

Se você passar uma string vazia no segundo parâmetro, o trecho será apagado.
Se o primeiro parâmetro for uma string vazia, o segundo será inserido antes de
cada caractere da string.

# 7.7 Remoção de espaços em branco

O método strip é utilizado para remover espaços em branco do início ou fim da
string. Já os métodos lstrip e rstrip removem apenas os caracteres em branco à
esquerda ou à direita, respectivamente.

## Remoção de espaços em branco com strip, lstrip e rstrip

t=" Olá "

t.strip()

'Olá'

t.lstrip()

'Olá '

t.rstrip()

' Olá'

Se você passar um parâmetro tanto para strip quanto para lstrip ou rstrip, este será utilizado como caractere a remover.

## Remoção de caracteres com strip, lstrip e rstrip

s="...///Olá///..."

s.lstrip(".")

'///Olá///...'

s.rstrip(".")

'...///Olá///'

s.strip(".")

'///Olá///'

s.strip("./")

'Olá'

# 7.8 Validação por tipo de conteúdo

Strings em Python podem ter seu conteúdo analisado e verificado utilizando-
-se métodos especiais. Esses métodos verificam se todos os caracteres são letras,
números ou uma combinação deles. Vejamos alguns exemplos:

## Validação de strings por seu conteúdo

s="125"

p="alô mundo"

s.isalnum()

True

p.isalnum()

False

s.isalpha()

False

p.isalpha()

False

O método *isalnum* retorna verdadeiro se a string não estiver vazia, e se todos os
seus caracteres são letras e/ou números. Se a string contiver outros tipos de caracteres, como espaços, vírgula, exclamação, interrogação ou caracteres de controle,
retorna **False**.
Já *isalpha* é mais restritivo, retornando verdadeiro apenas se todos os caracteres
forem letras, incluindo vogais acentuadas. Retorna falso se algum outro tipo de
caractere for encontrado na string ou se estiver vazia.
O método *isdigit* verifica se o valor consiste em números, retornando **True** se a
string não estiver vazia e contiver apenas números. Se a string contiver espaços,
pontos, vírgulas ou sinais (+ ou -), retorna falso

## Validação de strings com números

"771".isdigit()

True

"10.4".isdigit()

False

"+10".isdigit()

False

"-5".isdigit()

False

Os métodos *isdigit* e *isnumeric* são parecidos, e diferenciá-los envolve um conhecimento de Unicode mais aprofundado. *isdigit* retorna **True** para caracteres
definidos como dígitos numéricos em Unicode, indo além de nossos 0 a 9, como,
por exemplo um 9 tibetano (\u0f29). *isnumeric* é mais abrangente, incluindo dígitos e representações numéricas como frações, por exemplo.

##  Diferenciação de isnumeric de isdigit

umterço="\u2153"

novetibetano="\u0f29"

umterço.isdigit()

False

umterço.isnumeric()

True

novetibetano.isdigit()

True

novetibetano.isnumeric()

True

Podemos também verificar se todos os caracteres de uma string são letras maiúsculas ou minúsculas usando isupper e islower, respectivamente 

## Verificação de maiúsculas e minúsculas

s="ABC"

p="abc"

e="aBc"

s.isupper()

True

s.islower()

False

p.isupper()

False

p.islower()

True

e.isupper()

False

e.islower()

False

Temos também como verificar se a string contém apenas caracteres em branco,
como espaços, marcas de tabulação (TAB), quebras de linha (LF) ou retorno de
carro (CR). Para isso, vamos utilizar o método isspace

## Verificação se a string contém apenas caracteres de espaçamento

"\t\n\r ".isspace()

True

"\tAlô".isspace()

False

Se você precisar verificar se algo pode ser impresso na tela, o método *isprintable*
pode ajudar. Ele retorna **False** se algum caractere que não pode ser impresso for
encontrado na string. Você pode utilizá-lo para verificar se a impressão de uma
string pode causar efeitos indesejados no terminal ou na formatação de um arquivo

## Verificação se a string pode ser impressa

"\n\t".isprintable()

False

"\nAlô".isprintable()

False

"Alô mundo".isprintable()

True
