def bubble_sort(lista):
    fim = len(lista)
    
    for i in range(fim-1, 0, -1):
        #começa em fim-1, vai ate 0, com step de -1
        for j in range(i):
            if lista [j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],  lista[j]
                print(lista)
                
    return lista
