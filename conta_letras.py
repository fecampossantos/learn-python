# O código recebe uma frase e conta quantas vogais ou consoantes há nela (se na segunda variavel de conta_letras nao for nada inserido, o código devolve as vogais. Caso o usuário queira que sejam contadas as consoantes, deve ser inserido como segunda variavel a palavra "consoantes")
def main():
    frase = input("Digite a frase: ")
    aux = input("Deseja contar as vogais (digite 'vogais') ou consoantes (digite 'consoantes') ?")
    print(ContaLetras.conta_letras(frase, aux))
    
class ContaLetras:
    def conta_letras(frase, contar="vogais"):
        lista_vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        letras = frase.strip()
        comprimento = len(letras)
        a = 0
        soma = 0
        espaços = 0
        while a < comprimento:
            if letras[a] in lista_vogais:
                soma += 1
                a += 1
            if letras[a] == " ":
                espaços += 1
                a += 1
            else:
                a += 1
        if contar == "vogais":
            return soma
        if contar == "consoantes":
            return len(letras) - soma - espaços

if __name__ == "__main__":
    main()
