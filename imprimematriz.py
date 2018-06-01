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
                print(" ", end = "")
            if b == col:
                print("\n", end = "")
        a = a + 1
        b = 0
