def main():
    print("O código recebe a largura e a altura do retangulo e desenha ele.")
    larg = int(input("Digite a largura: "))
    alt = int(input("Digite a altura: "))
    forma = input(print('O código pode desenhar dois tipos de retangulo. Você deseja o retangulo "vazio" ou "cheio"? '))

    if forma == 'vazio':
        print()
        DesenhaRetangulo.desenha_vazio(larg, alt)
        print()
    if forma == 'cheio':
        print()
        DesenhaRetangulo.desenha_cheio(larg, alt)
        print()
    

class DesenhaRetangulo:
    
    def desenha_cheio(largura, altura):
        larg_count = 1
        alt_count = 1
        while larg_count > 0 and alt_count > 0:
            larg_count = largura
            alt_count = altura
            while alt_count > 0:
                if larg_count > 1:
                    print("#" ,end= "")
                    larg_count = larg_count - 1
                else:
                    print("#" ,end="\n" )
                    alt_count = alt_count - 1
                    larg_count = largura


    def desenha_vazio(largura, altura):
        linha = 1
        larg_count = 1
        alt_count = 1

        while larg_count > 0 and alt_count > 0:
            larg_count = largura
            alt_count = altura
            while alt_count > 0:
                if linha == 1 or linha == altura:
                    if larg_count > 1:
                        print("#" ,end= "")
                        larg_count = larg_count - 1
                    else:
                        print("#" ,end="\n" )
                        alt_count = alt_count - 1
                        larg_count = largura
                        linha = linha + 1
                else:
                    print("#" ,end= "")
                    while larg_count > 2:
                        print(" " ,end = "")
                        larg_count = larg_count - 1
                    print("#",end="\n")
                    linha = linha + 1
                    alt_count = alt_count - 1
                    larg_count = largura




if __name__ == '__main__':
    main()
