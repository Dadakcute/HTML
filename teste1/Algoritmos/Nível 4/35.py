a=0
b=0
c=0
while True:
    v=input("Para votar em algum candidato, digite A, B ou C. Para parar de votar, digite 'fim' \n").upper()
    if v == "Fim" or "fim":
        print("Encerrado.")
        print(f"Candidato A: {a}")
        print(f"Candidato B: {b}")
        print(f"Candidato C: {c}")
        continue
    break
if v=="a" or "A":
    a=+1
    print(a)
elif v=="b":
    b=+1
    print(b)
elif v=="c":
    c=+1
    print(c)
else:
    print("Erro, Digite algo válido.")