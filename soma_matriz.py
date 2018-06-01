def soma_matrizes(m1,m2):
    ''' a função recebe duas matrizes. Se as matrizes tiverem mesmas dimensões, fara a soma, caso contrário retorna 'False' . '''
    dimensao1 = dimensoes(m1)
    dimensao2 = dimensoes(m2)
    
    if dimensao1[0] == dimensao2[0]:
        if dimensao1[1] == dimensao2[1]:
            linha_mat_final = []
            matriz_final = []
            i = 0
            j = 0
            a = int(dimensao1[1])
            b = int(dimensao1[0])
            while i < b:
                while j < a:
                    valor1 = int(m1[i][j])
                    valor2 = int(m2[i][j])
                    soma = valor1 + valor2
                    linha_mat_final.append(soma)
                    j += 1
                matriz_final.append(linha_mat_final)
                linha_mat_final = []
                i += 1
                j = 0
        return matriz_final
            
        
    
    else:
        return False

def dimensoes(matriz):
    ''' a função recebe como parâmetro uma matriz e imprime as dimensões da matriz no formato iXj '''
    dimensao = []
    lin = len(matriz)
    col = len(matriz[0])
    dimensao.append(lin)
    dimensao.append(col)
    return dimensao
