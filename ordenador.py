class Ordenador:
    def selecao_direta (self, lista):
        # Poe a lista em ordem crescente
        
        fim = len(lista)
        
        for i in range(fim - 1):
            # inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i
            
            for j in range (i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            
            # Coloca o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos na posição 'i' e 'posicao_do_minimo'
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            #começa em fim-1, vai ate 0, com step de -1
            for j in range(i):
                if lista [j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1],  lista[j]

        return lista


    def bolha_curta(self, lista):
        fim = len(lista)
        trocou = False

        for i in range(fim-1, 0, -1):
            #começa em fim-1, vai ate 0, com step de -1
            for j in range(i):
                if lista [j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1],  lista[j]
                    trocou = True
            if not trocou:
                return lista

        return lista

    
    
class Check_ordem:
    
    def ordenada_cres(self, lista):
        # Recebe uma lista e retorna True ou False para se a lista esta ou não em ordem crescente
        fim = len(lista)
        for i in range(fim - 1):
            if lista[i] > lista[i+1]:
                return False
        return True