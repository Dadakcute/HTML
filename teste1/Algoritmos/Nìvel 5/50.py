try:
    capital_inicial = float(input("Digite o Capital Inicial (R$): "))
    taxa_mensal_percentual = float(input("Digite a Taxa de Juros Mensal (%): "))
    numero_de_meses = int(input("Digite o Número de Meses para a simulação: "))
except ValueError:
    print("\nERROR: Invalid numeric input.")
    exit()

taxa_mensal_decimal = taxa_mensal_percentual / 100.0
saldo_atual = capital_inicial
mes_atual = 1

print("\n" + "="*55)
print(f"SIMULAÇÃO DE JUROS COMPOSTOS - {numero_de_meses} MESES")
print(f"Capital Inicial: R$ {capital_inicial:,.2f} | Taxa Mensal: {taxa_mensal_percentual:.2f}%")
print("="*55)
print(f"{'Mês':<5} | {'Saldo Início (R$)':<20} | {'Juros (R$)':<15} | {'Saldo Final (R$)':<15}")
print("-" * 55)

while mes_atual <= numero_de_meses:
    
    juros_do_mes = saldo_atual * taxa_mensal_decimal
    
    saldo_inicio_mes = saldo_atual
    
    saldo_atual = saldo_atual + juros_do_mes
    
    print(
        f"{mes_atual:<5} | "
        f"R$ {saldo_inicio_mes:,.2f}{'':<14-len(str(f'{saldo_inicio_mes:,.2f}'))} | "
        f"R$ {juros_do_mes:,.2f}{'':<10-len(str(f'{juros_do_mes:,.2f}'))} | "
        f"R$ {saldo_atual:,.2f}"
    )
    
    mes_atual += 1

print("-" * 55)
print(f"RESULTADO FINAL: Após {numero_de_meses} meses")
print(f"Montante Acumulado: R$ {saldo_atual:,.2f}")
print(f"Total de uros Ganhos: R$ {saldo_atual - capital_inicial:,.2f}")
print("="*55)