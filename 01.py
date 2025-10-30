listaOriginal = [2, 3, "4", 5, "abc", 7.0, 11, "13", None, 17]

listaSaida = []

def primosEmUmaLista(lista):
    countInvalidos = 0

    for valor in lista:
        try:
            valor = int(valor)
        except:
            countInvalidos += 1
            continue

        if (valor == 2):
            listaSaida.append(valor)
        elif (valor % 2 == 0):
            countInvalidos += 1
        else:
            listaSaida.append(valor)
    return listaSaida, countInvalidos

print(primosEmUmaLista(listaOriginal))
