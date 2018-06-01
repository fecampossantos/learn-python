# O código devolve quantos e quais (numa lista) os números impares de 0 ate n

def main():
    print("O código recebe um número (n) e devolve a quantidade e todos os impares de 0 ate n em uma lista.")
    n = int(input("Digite n: "))
    print(Impares.conta(n))


class Impares:
    def conta(n):
        aux = n
        j = 1
        lista = []
        while aux > 0:
            aux -= 1
            if j <= n:
                lista.append(j)
                j = j + 2
        quant = len(lista)
        return (quant, lista)


if __name__ == '__main__':
    main()
