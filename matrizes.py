class Matriz:
    
    def dimensao_matriz():
        lin = int(input("Digite o número de linhas da matriz: "))
        col = int(input("Digite o número de colunas da matriz: "))
        return Matriz.cria_matriz(lin, col)


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
        Matriz.imprime_matriz(matriz)
        print("\n", end = "")
        print("\n", end = "")
        return matriz
    
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
            print("A soma das matrizes resultou na seguinte matriz:")
            Matriz.imprime_matriz(matriz)

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
        print("A multiplicação das matrizes resultou na seguinte matriz: ")
        Matriz.imprime_matriz(C)

    def imprime_matriz(matriz):
        linhas = len(matriz)
        colunas = len(matriz[0])          
        a = 0
        b = 0
        while a < linhas:
            while b < colunas:
                print(matriz[a][b], end = "")
                b = b + 1
                if b < colunas:
                    print("\t", end = "")
                if b == colunas:
                    print("\n", end = "")
            a = a + 1
            b = 0

    def sao_multiplicaveis(m1, m2): #recebe duas matrizes e retorna True ou False, dependendo se são multiplicaveis ou não
        col_m1 = len(m1[0])
        lin_m2 = len(m2)

        if col_m1 == lin_m2:
            return True
        else:
            return False
        
if __name__ == "__main__":
    
    opcao = input("Você deseja somar ou multiplicar as matrizes? ")
    print()
    
    while opcao != 'somar' and opcao != 'multiplicar':
        print("oops, você tem que escolher entre 'somar' ou 'multiplicar' .", end = "\n")
        opcao = input("Você deseja somar ou multiplicar as matrizes? ")

    if opcao == 'somar':
        print("OK, vamos começar!", end = "\n")
        print("Primeira matriz:")
        A = Matriz.dimensao_matriz()
        print("Segunda matriz:")
        B = Matriz.dimensao_matriz()
        Matriz.soma_matrizes(A, B)

    if opcao == 'multiplicar':
        print("\n OK, vamos começar!", end = "\n")
        print("Primeira matriz:")
        A = Matriz.dimensao_matriz()
        print("Segunda matriz:")
        B = Matriz.dimensao_matriz()
        Matriz.multiplica_matrizes(A, B)
