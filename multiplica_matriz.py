
class Matriz:
    def multiplica_matrizes(A, B):
        linhasA = len(A)
        colunasA = len(A[0])
        linhasB = len(B)
        colunasB = len(B[0])
        assert colunasA == linhasB
        C = []
        for linha in range(linhasA):
            C.append([])
            for coluna in range(colunasB):
                C[linha].append(0)
                for k in range(colunasA):
                    C[linha][coluna] += A[linha][k] * B[k][coluna]
        return C

    def forma_matriz():
        lin = int(input("Digite o número de linhas da matriz: "))
        col = int(input("Digite o número de colunas da matriz: "))
        return cria_matriz(lin, col)


    def cria_matriz(n_linhas, n_colunas):
        matriz = []
        i = 0
        j = 0
        while i < n_linhas:
            linha = []
            while j < n_colunas:
                valor = int(input("Digite o valor de ["+ str(i) +"] ["+ str(j) +"]:"))
                linha.append(valor)
                j = j + 1
            j = 0
            i = i + 1
            matriz.append(linha)
        print("\n", end = "")
        print("A matriz ficou assim:")
        imprime_matriz(matriz, len(matriz), len(matriz[0]))
        print("\n", end = "")
        print("\n", end = "")
        return matriz

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
    def sao_multiplicaveis(m1, m2):
        col_m1 = len(m1[0])
        lin_m2 = len(m2)

        if col_m1 == lin_m2:
            return True
        else:
            return False
        
if __name__ == "__main__":
    A = forma_matriz()
    B = forma_matriz()
    C = multiplica_matrizes(A, B)
    lin = len(A)
    col = len(B[0])
    print("\n", end = "")
    print("As matrizes multiplicadas resultaram na matriz: ")
    print("\n", end = "")
    imprime_matriz(C, lin, col)
