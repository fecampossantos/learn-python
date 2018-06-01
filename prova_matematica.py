#- o código é de uma prova de matematia. GABARITOS 1-D 2-E 3-E 4-B 5-A 6-C

nota = 0
correcao = []
print ("\n Bem-vindo à prova.\n \n Leia o enunciado e responda todas as questões. Ao final será impressa sua nota e a correção da prova.")
print()

#- Questão 1
print("QUESTÃO 1")
print ("[2014 - FUVEST] Cada uma das cinco listas dadas é a relação de notas obtidas por seis alunos de uma turma em uma certa prova. Assinale a única lista na qual a média das notas é maior do que a mediana. \n (A) 5, 5, 7, 8, 9, 10 \n (B) 4, 5, 6, 7, 8, 8 \n (C) 4, 5, 6, 7, 8, 9 \n (D) 5, 5, 5, 7, 7, 9 \n (E) 5, 5, 10, 10, 10, 10")
print()
gabarito_1 = str(input("Gabarito: "))
while gabarito_1 == "":
    print("Você tem que dar uma resposta!")
    gabarito_1 = str(input("Gabarito: "))
print()
if gabarito_1 == "D" or gabarito_1 == "d":
    nota += 1
    correcao.append("1-CORRETA (D)")
else:
    correcao.append("1-ERRADA (Gabarito Correto = D)")

#- Questão 2
print("QUESTÃO 2")
print ("[2012 - ENEM] Um produtor de café irrigado em Minas Gerais recebeu um relatório de consultoria estatística, constando, entre outras informações, o desvio padrão das produções de uma safra dos talhões de sua propriedade. Os talhões têm a mesma área de 30 000 m2 e o valor obtido para o desvio padrão foi de 90 kg/talhão. O produtor deve apresentaras informações sobre a produção e a variância dessas produções em sacas de 60 kg por hectare (10 000 m2).A variância das produções dos talhões expressa em (sacas/hectare)2 é \n (A) 20,25. \n (B) 4,50. \n (C) 0,71. \n (D) 0,50. \n (E) 0,25.")
print()
gabarito_2 = str(input("Gabarito: "))
while gabarito_2 == "":
    print("Você tem que dar uma resposta!")
    gabarito_2 = str(input("Gabarito: "))
print()
if gabarito_2 == "E" or gabarito_2 == "e":
    nota += 1
    correcao.append("2-CORRETA (E)")
else:
    correcao.append("2-ERRADA (Gabarito Correto = E)")

#- Questão 3
print("QUESTÃO 3")
print ("[2011 - FUVEST-USP]No plano cartesiano, os pontos (0,3) e (-1,0) pertencem à circunferência C. Uma outra circunferência, de centro em (-1/2, 4), é tangente a C no ponto (0,3). Então, o raio de C vale: \n (A) √5/8 \n (B) √5/4 \n (C) √5/2 \n (D) 3(√5/4) \n (E) √5")
print()
gabarito_3 = str(input("Gabarito: "))
while gabarito_3 == "":
    print("Você tem que dar uma resposta!")
    gabarito_3 = str(input("Gabarito: "))
print()
if gabarito_3 == "E" or gabarito_3 == "e":
    nota += 1
    correcao.append("3-CORRETA (E)")
else:
    correcao.append("3-ERRADA (Gabarito Correto = E)")

#- Questão 4
print("QUESTÃO 4")
print("[2010 - FUVEST-USP]No plano cartesiano Oxy, a reta de equação x + y = 2 é tangente à circunferência C no ponto (0,2). Além disso, o ponto (1,0) pertence a C. Então, o raio de C é igual a: \n (A)3(√2/2) \n (B) 5(√2/2) \n (C) 7(√2/2) \n (D) 9(√2/2) \n (E) 11(√2/2)")
print()
gabarito_4 = str(input("Gabarito: "))
while gabarito_4 == "":
    print("Você tem que dar uma resposta!")
    gabarito_4 = str(input("Gabarito: "))
print()
if gabarito_4 == "B" or gabarito_4 == "b":
    nota += 1
    correcao.append("4-CORRETA (B)")
else:
    correcao.append("4-ERRADA (Gabarito Correto = B)")

#- Questão 5
print("QUESTÃO 5")
print("[2009 - FUVEST-USP] Considere, no plano cartesiano Oxy, a circunferência C de equação (𝑥−2)ˆ2 +(𝑦−2)ˆ2 =4 e sejam P e Q os pontos nos quais C tangencia os eixos Ox e Oy, respectivamente.Seja PQR o triângulo isósceles inscrito em C, de base 𝑃𝑄, e com o maior perímetro possível.Então, a área de PQR é igual a: \n (A) 2√2 + 2 \n (B) 2√2 - 1 \n (C) 2√2 \n (D) 2√2 - 2 \n (E) 2√2 + 4")
print()
gabarito_5 = str(input("Gabarito: "))
while gabarito_5 == "":
    print("Você tem que dar uma resposta!")
    gabarito_5 = str(input("Gabarito: "))
print()
if gabarito_5 == "A" or gabarito_5 == "a":
    nota += 1
    correcao.append("5-CORRETA (A)")
else:
    correcao.append("5-ERRADA (Gabarito Correto = A)")

#- Questão 6
print("QUESTÃO 6")
print("[2014 - FUVEST] Considere o triângulo ABC no plano cartesiano com vértices A = (0,0), B = (3,4) e C = (8,0). O retângulo MNPQ tem os vértices M e   N sobre o eixo das abscissas, o vértice Q sobre o lado AB e o vértice P sobre o lado BC. Dentre todos os retângulos construídos desse modo, o que tem área máxima é aquele em que o ponto é \n (A) (4, 16/5) \n (B) (17/4, 3) \n (C) (11/2, 3) \n (D) (5, 12/5) \n (E) (6, 8/5)")
print()
gabarito_6 = str(input("Gabarito: "))
while gabarito_6 == "":
    print("Você tem que dar uma resposta!")
    gabarito_6 = str(input("Gabarito: "))
print()
if gabarito_6 == "C" or gabarito_6 == "c":
    nota += 1
    correcao.append("6-CORRETA (C)")
else:
    correcao.append("6-ERRADA (Gabarito Correto = C)")

#- CORREÇÃO
print("Fim da prova!")
print("Sua nota foi",nota,".")
if nota <=3:
    print("Que pena,você não passou... O mínimo para passar era 4.")
else:
    print("Parabéns! Você passou!")
print("Correção da prova:")
b = 0
while b < len(correcao):
    c = correcao[b]
    print(c)
    b += 1