def main():
    lado = int(input("Digite o valor correspondente ao lado do quadrado: "))
    print('Perímetro = ', Quadrado.perimetro(lado), '- Área = ', Quadrado.area(lado))
    
class Quadrado:
    def perimetro(lado):
        perimetro = lado * 4
        return perimetro
    def area(lado):
        area = ladoquadrado ** 2
        return (area)

if __name__ = "__main__":
    main()