def main():
    print("Opção 1 - Temperatura de Celsius para Farenheit\nOpção 2 - Temperatura de Farenheit para Celsius.")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        celsius = int(input("Digite a temperatura em celsius: "))
        temp1 = Temperatura.CtoF(celsius)
        print("A temperatura em farenheit é ",temp1, "°F.")
    if opcao == 2:
        farenheit = int(input("Digite a temperatura em farenheit: "))
        temp2 = Temperatura.FtoC(farenheit)
        print("A temperatura em celsius é ", temp2, "°C.")

class Temperatura:
    
    def CtoF(celsius): # converte a temperatura de celsius para farenheit
        farenheit = ((celsius * 9) / 5) + 32
        return farenheit
    
    def FtoC(farenheit): # converte a temperatura de farenheit para celsius
        celsius = 5 * ((farenheit - 32) / 9)
        return celsius

if __name__ == '__main__':
    main()
