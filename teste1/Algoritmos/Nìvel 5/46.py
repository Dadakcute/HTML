
numero = 1

while numero <= 10:
    print(f"\nTabuada do {numero}:")
    print("-" * 15)

    multiplicador = 1

    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1
    
    print("-" * 15)
    numero += 1

