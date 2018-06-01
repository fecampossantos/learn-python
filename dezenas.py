def main():
    x = float(input("Digite o número inteiro: "))
    print(NumeroDasDezenas.conta(x))


class NumeroDasDezenas:
    def conta(x):
        x1 = x / 10
        x = int(x1)
        numero_dezenas = x % 10
        return numero_dezenas

if __name__ == "__main__":
    main()
