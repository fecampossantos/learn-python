def main():
    n = int(input("Digite o número a ser analisado: "))
    print(Paridade.impar_par(n))

class Paridade:
    def impar_par(n):
        if n % 2 == 0 :
            return ("par")
        else:
            return ("ímpar")

if __name__ == '__main__':
    main()