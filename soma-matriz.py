def soma_matrizes(m1, m2):
    dimensoes(m1, m2)
    return matriz

def dimensoes(m1, m2):
    col_m1 = len(m1[0])
    lin_m1 = len(m1)
    col_m2 = len(m2[0])
    lin_m2 = len(m2)
    if col_m1 == col_m2 and lin_m1 == lin_m2:
        cria_matriz(m1, m2)
    else:
        return False

def cria_matriz(m1, m2):
    matriz = []
    i = 0
    j = 0
    while i < len(m1):
        linha = []
        while j < len(m1[0]):
            soma_elementos(m1, m2)
            linha.append(soma_elementos)
            j = j + 1
        j = 0
        i = i + 1
        matriz.append(linha)
        return matriz
    
def soma_elementos(m1, m2):
    a = 0
    b = 0
    c = 0
    d = 0
    while a in range(len(m1)):
        while b in range(len(m1[0])):
            while c in range(len(m1)):
                while d in range(len(m1[0])):
                    soma_elementos = m1[a][b] + m2[c][d]
                d = 0
            d = 0
            c = 0
        d = 0
        c = 0
        b = 0
    return soma_elementos
