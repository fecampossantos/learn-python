def main():
    n = int(input("Digite n: "))
    print('É primo? ', Primo.primo(n))

class Primo:

    def primo(n):
        divisor = 2
        aux = n
        fator = 0
        while divisor < aux:
            if n % divisor != 0:
                divisor = divisor + 1
            else:
                divisor = divisor + 1
                fator = fator + 1
        if fator > 0:
            return False
        else:
            return True


if __name__ == "__main__":
    main()
