#----- JOGO DO NIM -----#
def partida():
    #-- aqui sao definidas as variaveis de jogo (quantidade de peças na partida e maximo a ser retirado)
    n = int(input("Quantas peças terá no tabuleiro? "))
    m = int(input("Qual o limite de peças retiradas por jogada? "))
    while n != 0:
        if (n % (m+1) == 0 ): #--n é multiplo de (m+1),ou seja,o jogador começa
            print ("Você começa!\n")
            #- a partida começa aqui,a vez é do usuario
            while n > 0:
                print ("É a sua vez de jogar\n")
                n = n - usuario_escolhe_jogada(n, m)
                if n <= 0:   #-- se acabarem as peças,o usuario ganha
                    print("Fim de jogo! Você ganhou!\n") #-- se nao acabarem as peças,a vez é do computador
                    break
                else:
                    print ("Ainda restam", n, "peças no tabuleiro.\n")
                print("É a vez do computador\n")
                n = n - computador_escolhe_jogada(n, m)
                if n <= 0: #-- se acabarem as peças,o computador ganha
                    print("Fim de jogo! O computador ganhou!\n")
                    break
                else:
                    print ("Ainda restam", n, "peças no tabuleiro.\n")
        if (n % (m+1) != 0): #--n nao é multiplo de (m+1),ou seja,o computador começa
            print ("Computador começa!\n")
            #-- a partida começa aqui,a vez é do computador
            while n > 0:
                print("É a vez do computador\n")
                n = n - computador_escolhe_jogada(n, m)
                if n <= 0: #-- se acabarem as peças,o computador ganha
                    print("Fim de jogo! O computador ganhou!\n")
                    break
                else:
                    print ("Ainda restam", n, "peças no tabuleiro.\n")
                print ("É a sua vez de jogar\n")
                n = n - usuario_escolhe_jogada(n ,m)
                if n <= 0: #-- se acabarem as peças,o usuario ganha
                    print("Fim de jogo! Você ganhou!\n")
                    break
                else:
                    print ("Ainda restam", n, "peças no tabuleiro.\n")
#-------------------------------------------------------------------------------------

def campeonato():
    usuario = 0
    computador = 0
    rodada = 1
    if rodada != 3:
        while not rodada == 3:
            #- a partir daqui é igual "partida" porem contando pontos por rodada vencida,ate que se tenha 3 rodadas (rodada = 3) -#
            print ("Rodada número" ,rodada , ".\n")
            #-regras
            n = int(input("Quantas peças terá no tabuleiro? "))
            m = int(input("Qual o limite de peças retiradas por jogada? "))
            if n % (m+1) == 0 : #-- numeros validos e n é multiplo de (m+1),ou seja,o jogador começa
                print ("Você começa!\n")
                #- a partida começa aqui,a vez é do usuario
                while n > 0:
                    print ("É a sua vez\n")
                    n = n - usuario_escolhe_jogada(n, m)
                    if n <= 0:   #-- se acabarem as peças,o usuario ganha
                        print("Fim de jogo! Você ganhou!\n")
                        usuario = usuario + 1
                        rodada = rodada + 1
                        break
                    else:
                        print ("Ainda restam", n, "peças no tabuleiro.\n")
                    print("É a vez do computador\n")
                    n = n - computador_escolhe_jogada(n, m)
                    if n <= 0: #-- se acabarem as peças,o computador ganha
                        print("Fim de jogo! O computador ganhou!\n")
                        computador = computador + 1
                        rodada = rodada + 1
                        break
                    else:
                        print ("Ainda restam", n, "peças no tabuleiro.\n")
            if (n % (m+1) != 0): #-- numeros validos e n nao é multiplo de (m+1),ou seja,o computador começa
                print ("Computador começa!\n")
                #-- a partida começa aqui,a vez é do computador
                while n > 0:
                    print("É a vez do computador\n")
                    n = n - computador_escolhe_jogada(n, m)
                    if n <= 0: #-- se acabarem as peças,o computador ganha
                        print("Fim de jogo! O computador ganhou!\n")
                        computador = computador + 1
                        rodada = rodada + 1
                        break
                    else:
                        print ("Ainda restam", n, "peças no tabuleiro.\n")
                    print("É a sua vez")
                    n = n - usuario_escolhe_jogada(n ,m)
                    if n <= 0: #-- se acabarem as peças,o usuario ganha
                        print("Fim de jogo! Você ganhou!\n")
                        usuario = usuario + 1
                        rodada = rodada + 1
                        break
                    else:
                        print ("Ainda restam", n, "peças no tabuleiro.\n")
    if rodada == 3:
        print ("O jogo acabou! O placar final foi: \n Você", usuario, "X", computador,"Computador\n")
        if usuario > computador:
            print("Parabéns! Você ganhou!")
        if computador > usuario:
            print("Que pena... Você perdeu :( ")
    

#-------------------------------------------------------------------------------------

def computador_escolhe_jogada(n, m):
    peca_computador = m
    if peca_computador > 0:
        if not (n - peca_computador)%(m+1)==0:
            while not (n - peca_computador)%(m+1)==0:
                peca_computador = peca_computador - 1
        else:
            peca_computador = m
    print ("O computador tirou", peca_computador, "peças\n")
    return peca_computador

#-------------------------------------------------------------------------------------

def usuario_escolhe_jogada(n, m):
    pecas_usuario = int(input("Quantas peças você quer tirar?"))
    if pecas_usuario > m or pecas_usuario <= 0 or pecas_usuario > n:
        while pecas_usuario > m or pecas_usuario <= 0 or pecas_usuario > n:
            print("Oops! Jogada inválida! Tente de novo.\n")
            pecas_usuario = int(input("Quantas peças você quer tirar?"))
    print ("Você tirou", pecas_usuario, "peças.\n")
    return pecas_usuario






#----- PRINT INICIAIS -----#


#- a interação com o jogo começa aqui -#
print("Bem-vindo ao jogo do NIM! Escolha:\n 1 - para jogar partida isolada. \n 2 - para jogar um campeonato ")
escolha = int(input())
if escolha == 1:
    print ("Você escolheu partida isolada!")
    partida()
if escolha == 2:
    print ("Você escolheu campeonato!")
    campeonato()
if escolha !=1 and escolha !=2:
    while escolha != 1 and escolha != 2:
        print("Oops! Operação inválida! Tente de novo. \n Escolha:\n 1 - para jogar partida isolada. \n 2 - para jogar um campeonato ")
        escolha = int(input())
