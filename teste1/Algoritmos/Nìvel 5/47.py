print("Os 20 primeiros números da sequência de Fibonacci:")

a, b = 0, 1

for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b