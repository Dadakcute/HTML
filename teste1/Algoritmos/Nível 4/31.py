doce=1.50
total = 0
while True:
    quantidade = int(input("Quantos doces você quer ? \n"))
    total+=quantidade
    preco = total*doce
    escolha = input(f"{preco}, valor a ser pago até agora, deseja continuar ? Sim ou Não: \n ")
    if escolha == "Não":
        print(preco,"Valor total a ser pago!")
        break
    else:
        print("")
        