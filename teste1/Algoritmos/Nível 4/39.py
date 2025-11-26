import random
tentativas = 3
numero_secreto = random.randint(1,51)
print("Tente adivinhar o número secreto de 1 a 50 :")
while tentativas > 0:
    tentativa = int(input("Digite um número :"))
    if tentativa == numero_secreto:
        print(f"Parabéns!!! Você acertou o número secreto , {numero_secreto}")
        break
    elif tentativa < numero_secreto:
        tentativas -=1
        print(f"Valor muito baixo! Você ainda tem {tentativas} tentativas.")
    else:
        tentativas -=1
        print(f"Valor muito alto! Você ainda tem {tentativas} tentativas.")
if tentativas == 0:
    print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}")