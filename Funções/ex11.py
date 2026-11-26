# #  Função area_retangulo(base, altura); o principal lê os dados e mostra a área com 2 casas.
def area_retangulo(base, altura):
    return (base*altura)/2


b = float(input())
a = float(input())

x = area_retangulo(b,a)
print(f"Área do retângulo é: {x:.2f}")