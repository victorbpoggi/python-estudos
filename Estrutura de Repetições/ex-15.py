total = 0 
quantidade_comprada = int(input("Informe a quantidade comprada: "))

while True:
    codigo = int(input("Digite o código do produto: "))

    
    if codigo == 1:
        preço = (quantidade_comprada * 0.50)
        continue
    if codigo == 2:
        preço = (quantidade_comprada * 1)
        continue
    if codigo == 3:
        preço = (quantidade_comprada * 4)
        continue
    if codigo == 5:
        preço = (quantidade_comprada * 7)
        continue
    if codigo == 9:
        preço = (quantidade_comprada * 8)
        continue
    if codigo == 0:
        total = total + preço
        break


print(f"total das compras: {total}")
    