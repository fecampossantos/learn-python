def remove_repetidos(lista):
    lista.sort()
    aux = lista[-1]
    x = 0
    while x <= aux:
        count = lista.count(x)
        if count > 1:
            lista.remove(x)
            x = x + 1
        else:
            x = x + 1
    return lista
