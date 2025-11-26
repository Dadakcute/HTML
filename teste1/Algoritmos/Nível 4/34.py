import random
tentativas = 0
numero_secreto = random.randint(1,51)
print("Tente adivinhar o número secreto de 1 a 50 :")
while True:
    tentativa = int(input("Digite um número :"))
    tentativas +=1
    if tentativa == numero_secreto:
        print(f"Parabéns!!! Você acertou o número secreto , {numero_secreto}")
        break
    elif tentativa < numero_secreto:
        print("Valor muito baixo!")
    else:
        print("Valor muito alto!")