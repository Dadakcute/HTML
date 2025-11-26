par = []
impar = []
for i in range(1,11):
    num = int(input("Digite um número: \n"))
    if num %2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(par)
print(impar)
