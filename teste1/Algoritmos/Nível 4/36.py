nome = input("Digite uma palavra :\n")
while True:
    if nome == "SAIR" or nome == "sair":
        print("Programa encerrado.")
        break
    else:
        print(f"Você digitou a palavra {nome}")
        nome = input("Digite uma palavra :\n")