def dimensoes(matriz):
    ''' a função recebe como parâmetro uma matriz e imprime as dimensões da matriz no formato iXj '''
    
    lin = len(matriz)
    col = len(matriz[0])
    
    print(lin, end="")
    print("X", end="")
    print(col, end="")
