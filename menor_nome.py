'''o programa receberá uma lista de nomes e retornará o menor nome, com a primeira letra maiuscula.'''

def menor_nome(lista_de_nomes):
    i = 0
    j = 0
    lista_aux = []
    while i < len(lista_de_nomes):
        while j < len(lista_de_nomes):
            nome_aux = lista_de_nomes[j].strip().capitalize()
            lista_aux.append(nome_aux)
            j = j + 1
        ''' após ser criada uma lista com os nomes sem espaços e com a primeira letra maiuscula, falta ver qual dos nomes é menor'''
        padrao = len(lista_aux[-1])
        aux1 = 0
        while aux1 < len(lista_de_nomes):
            tam = len(lista_aux[i])
            if tam < padrao:
                menor = lista_aux[i]
                i = i + 1
                padrao = tam
            else:
                i = i + 1
            aux1 = aux1 + 1
    return menor

def testes():
    lista1 = ["    ana    ", "romero", "paulo", "rebeca", "carlos"]
    if menor_nome(lista1) == "Ana":
        print("1 FUNCIONA!")
    else:
        print("NÃO FUNCIONA... :( ")
    lista2 = ["             PAULO       ", "rodolfitchu" , "TiGrEsiNHa"]
    if menor_nome(lista2) == "Paulo":
        print("2 FUNCIONA!")
    else:
        print("NÃO FUNCIONA... :( ")
    lista3 = ['zé', ' lu', 'fê']
    if menor_nome(lista3) == "lu":
        print("3 FUNCIONA!")
    else:
        print("NÃO FUNCIONA... :( ")
