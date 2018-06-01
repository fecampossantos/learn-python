def main():
    x = int(input("Digite o número: "))
    print(Fatorial.fatorial(x))

class Fatorial:

    def fatorial(x):
        fat = 1
        while x > 1:
            fat = fat * x
            x = x - 1
        return fat

if __name__ == "__main__":
    main()