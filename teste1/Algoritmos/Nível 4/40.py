numero = int(input("Digite um número inteiro positivo :\n"))
binario = ""
octal = ""
hexadecimal = ""
while numero > 0:
    resto_binario = numero % 2
    binario = str(resto_binario) + binario
    resto_octal = numero % 8
    octal = str(resto_octal) + octal
    resto_hexadecimal = numero % 16
    if resto_hexadecimal < 10:
        hexadecimal = str(resto_hexadecimal) + hexadecimal
    else:
        hexadecimal = chr(resto_hexadecimal - 10 + ord('A')) + hexadecimal
    numero = numero // 2
print(f"Número em binário: {binario}")
print(f"Número em octal: {octal}")
print(f"Número em hexadecimal: {hexadecimal}")