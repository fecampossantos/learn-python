def main():
    print("Bem-vindo ao programa de potenciação. Primeiro digite o número que será a base (diferente de zero), depois digite até que número deseja que ele seja elevado.")

    base = int(input("Digite a base: "))
    while base == 0:
        print("ops... a base tem que ser diferente de 0")
        base = int(input("Digite a base: "))
    potencia = int(input("Digite a potencia final: "))
    print(Potencia.potenciacao(base, potencia))

class Potencia:
    def potenciacao(base, potencia):
        cont = 0
        while cont <= potencia:
            aux = base ** cont
            print(base, "elevado a", cont, " = ", aux)
            cont += 1
        print("FIM")

if __name__ = '__main__':
    main()