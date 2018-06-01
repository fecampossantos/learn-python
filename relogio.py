def main():   #--- entrada de dados
    x = int(input("Por favor, entre com o número total de segundos que deseja converter para horas/minutos/segundos: "))
    print(Tempo.dias(x), ' dias, ', Tempo.horas(x), ' horas, ', Tempo.minutos(x), ' minutos, ', Tempo.segundos(x), ' segundos.')

class Tempo:
    def dias(x):
        dias = x // 86400
        return dias

    def horas(x):
        x1 = x % 86400
        horas = x1 // 3600
        return horas

    def minutos(x):
        x1 = x % 86400
        x2 = x1 % 3600
        minutos = x2 // 60
        return minutos

    def segundos(x):
        x1 = x % 86400
        x2 = x1 % 3600
        segundos = x2 % 60
        return segundos

if __name__ == '__main__':
    main()
