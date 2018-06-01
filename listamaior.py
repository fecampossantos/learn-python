def maior_elemento(lista):
    lista_arrumada = lista[:]
    lista_arrumada.sort()
    return lista_arrumada[-1]
