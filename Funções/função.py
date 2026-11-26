#Funções

#def <nome_da_função> (<Parâmetros_da_função>):
#    <comandos>
#     return
# nome_da_função()   #call function

# Definição do retorno de um valor
def soma(a,b):
    return(a+b)
print(soma(2,9))

#Retornando se valor é par ou não

def is_even(x):
    return(x%2==0)
print(is_even(2))
print(is_even(3))
print(is_even(10))

# Reutilização da função épar em outra função (verificar se é par ou ímpar agora)
def is_even(x):
    return(x%2==0)          #even -> par
def odd_or_even(x):         #odd -> ímpar 
    if is_even(x):
        return "even"
    else:
        return "odd"
print(odd_or_even(4))
print(odd_or_even(5))

#  escopo local e global
taxa = 0.1 #global
def preco_final(valor):     #lê a global: funciona
    desconto = valor * taxa #'desconto' é local
    return valor - desconto
print(f"O preço final fica: {preco_final(200):.1f}") #180.0
# print(desconto) ## NameError! só existe dentro da função


