
frase = input("Digite uma frase: ")




# Conta os espaços na frase
for caractere in frase:
    if caractere == " ":
        contador_espacos += 1

# Exibe o resultado
print(f"A frase possui {contador_espacos} espaço(s).")