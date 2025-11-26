
numero = input("Digite um número: ")
inverso = ""

for digito in numero:
    inverso = digito + inverso

print(f"O inverso usando for: {inverso}")

numero = input("Digite um número: ")
inverso = ""
i = len(numero) - 1

while i >= 0:
    inverso += numero[i]
    i -= 1

print(f"O inverso usando while: {inverso}")