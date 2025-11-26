
valor = int(input("Digite o valor a ser sacado: "))


notas = [100, 50, 20, 10, 5]
quantidades = {}


for nota in notas:
    quantidades[nota] = valor // nota
    valor %= nota


print("\nNotas necessárias:")
for nota, quantidade in quantidades.items():
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {nota}")