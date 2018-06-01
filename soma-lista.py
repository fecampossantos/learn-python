def main():
    print("O código recebe uma lista do usuário e soma. Ao terminar de inserir os números da lista, digite 0 (zero). ")
    lista = []
    valor = 1
    while valor != 0:
        valor = int(input("Digite o valor a ser adicionado à lista: "))
        lista.append(valor)
    print("A soma dos valores da lista é: ", Lista.soma(lista))


class Lista:
    def soma(lista):
        a = len(lista)
        x = 1
        soma = 0
        while x <= a:
            aux = lista[-x]
            soma = soma + aux
            x = x + 1
        return soma


if __name__ == '__main__':
    main()
