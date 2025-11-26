print("Números primos de 1 a 100:")


for num in range(1, 101):
    if num < 2:
        continue

    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

  
    if primo:
        print(num, end=" ")