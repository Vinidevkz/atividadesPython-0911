decisao = 1
empresa1 = {"nome": "Itau", "clientes": 29000, "valorPCliente ": 378, "regiao": "SP", "vendas2024": 340000, "vendas2025": 350000, "funcionarios2024": 17000 ,"funcionarios2025": 19000}

def verDadosDaEmpresa(empresa):
    return "Dados da empresa: \n ", empresa

def relatorioUltimosDoisAnos(empresa):
    try:
        venda1 = empresa["vendas2024"]
        venda2 = empresa["vendas2025"]

        percent = ((venda2 - venda1) / venda1) * 100

        return f"O numero de vendas cresceu em {percent:.2f}%. {venda1} em 2024 e {venda2} em 2025."
    except:
        return "Os dados da empresa estão inválidos, insira os dados corretamente e tente novamente."
    
def relatorioContratacoes(empresa):
    try:
        func2024 = empresa["funcionarios2024"]
        func2025 = empresa["funcionarios2025"]

        percent = ((func2025 - func2024) / func2024) * 100

        contratados = func2025 - func2024
        return f"O numero de funcionarios cresceu em {percent:.2f}%. Cerca de {contratados} funcionarios foram contratados em 2025."

    except:
        return "Os dados da empresa estão inválidos, insira os dados corretamente e tente novamente."

while decisao != 0:

    print("Digite uma opção: \n (1: Ver todos os dados da empresa) \n (2: Comparar vendas dos ultimos 2 anos) \n (3: Contratações em 2025 em comparação ao ano passado) ")
    decisao = int(input("Digite sua opção: "))

    if decisao == 1:
        print(verDadosDaEmpresa(empresa1))
    elif decisao == 2:
        print(relatorioUltimosDoisAnos(empresa1))
    elif decisao == 3:
        print(relatorioContratacoes(empresa1))
    elif decisao == 0:
        continue
    else:
        print("Numero invalido.")
    






