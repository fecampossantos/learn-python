from random import randrange

class CriaLista:

    def lista_grande1(n):
        # cria uma lista aleatória com n elementos positivos (de 0 a n)
        lista = []
        i = 0
        while i < n:
            x = randrange(n + 1)
            a = busca_sequencial(lista, x)
            if a == False:
                lista.append(x)
                i += 1


        return lista

    def lista_grande2(n):
        # cria uma lista aleatória com n elementos positivos (de 0 a n*10)
        lista = []
        i = 0
        while i < n:
            x = randrange(n*10 + 1)
            a = busca_sequencial(lista, x)
            if a == False:
                lista.append(x)
                i += 1


        return lista
    
    
    
    def busca_sequencial(lista, x):
        # Devolve apenas se o elemento esta ou não na lista
        '''(lista, elemento a ser buscado) -> bool'''
        for i in range(len(lista)):
            if lista[i] == x:
                return True
        return False
