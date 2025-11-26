
idades = []


for _ in range(5):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)


media = sum(idades) / len(idades)

# Exibe a média
print(f"\nA média das idades é: {media:.2f}")


print("Idades acima da média:")
for idade in idades:
    if idade > media:
        print(idade)

