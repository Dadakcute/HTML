numero = int(input("Digite um número inteiro :\n"))
numeros = int(input("Digite um número inteiro :\n"))
soma_impares = 0
while numero <= numeros:
    if numero % 2 != 0:
        soma_impares += numero
    numero +=1
print(f"A soma dos números ímpares entre os dois números digitados é: {soma_impares}")
