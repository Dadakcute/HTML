
altura = int(input("Digite a altura da pirâmide: "))
for i in range(altura):
    espacos = " " * (altura - i - 1)
    asteriscos = "*" * (2 * i + 1)
    print(espacos + asteriscos)