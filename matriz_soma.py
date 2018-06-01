def soma_matrizes(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("As matrizes não tem mesmas dimensões, logo não é possivel somá-las.")
        pass
    else:
        matriz = []
        lin = len(A)
        col = len(A[0])
        for a in range(lin):
            linha = []
            for b in range(col):
                valor = A[a][b] + B[a][b]
                linha.append(valor)
            matriz.append(linha)
        imprime_matriz(matriz)

def imprime_matriz(matriz):
    lin = len(matriz)
    col = len(matriz[0])
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
