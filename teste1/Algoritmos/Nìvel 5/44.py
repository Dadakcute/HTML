
numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("\nNúmeros na ordem inversa:")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])