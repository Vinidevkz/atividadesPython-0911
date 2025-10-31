def calcularImposto(valor):

    faixas = [20000, 40000, 60000]
    aliquotas = [0.0, 0.075, 0.15, 0.225]
    imposto = 0

    for i in range(len(faixas)):

        if valor > faixas[i]:

            base = faixas[i] - (faixas[i-1] if i > 0 else 0)
            imposto += base * aliquotas[i]

        else:

            base = valor - (faixas[i-1] if i > 0 else 0)
            imposto += base * aliquotas[i]

            return imposto
        
    return imposto + (valor - faixas[-1]) * aliquotas[-1]

while True:

    try:

        valor = float(input("\nvalor anual (R$): "))
        print(f"Imposto: R$ {calcularImposto(valor):.2f}")
        aumento = float(input("Aumento anual (%): "))
        print(f"O novo imposto é de R$ {calcularImposto(valor*(1+aumento/100)):.2f}")

    except:

        print("Entrada inválida.")

    if input("Nova simulação? (1: Sim. 2: Não.): ") != "1":
        break
