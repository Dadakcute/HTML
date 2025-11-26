import random

numeros = []

for _ in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)

maior = max(numeros)


print("Números gerados:", numeros)
print(f"O maior número é: {maior}")