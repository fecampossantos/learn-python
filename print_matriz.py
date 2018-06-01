def forma_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    cria_matriz(lin, col)


def cria_matriz(n_linhas, n_colunas):
    matriz = []
    i = 0
    j = 0
    while i < n_linhas:
        linha = []
        while j < n_colunas:
            valor = int(input("Digite o valor de ["+ str(i) +"] ["+ str(j) +"]."))
            linha.append(valor)
            j = j + 1
        j = 0
        i = i + 1
        matriz.append(linha)
    imprime_matriz(matriz, n_linhas, n_colunas)

def imprime_matriz(matriz, lin, col):
    a = 0
    b = 0
    while a < lin:
        while b < col:
            print(matriz[a][b], end = "")
            b = b + 1
            if b < col:
                print("\t", end = "")
            if b == col:
                print("\n", end = "")
        a = a + 1
        b = 0
