compras = int(input("Digite um valor do produto (0 para sair) :\n"))
total = 0
while compras != 0:
    total+=compras
    compras = int(input("Digite um valor do produto (0 para sair) :\n"))
print(f"Valor total da compra é de: {total}")
