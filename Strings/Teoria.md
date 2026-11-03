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