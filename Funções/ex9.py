# Função eh_par(n) que devolve True ou False .
def eh_par(n):
    if n % 2 == 0:
        return True
    return False
a = int(input())
print(eh_par(a))