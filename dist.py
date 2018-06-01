import math

def main():
    x1 = int(input("Digite a coordenada X do primeiro ponto: "))
    y1 = int(input("Digite a coordenada Y do primeiro ponto: "))
    x2 = int(input("Digite a coordenada X do segundo ponto: "))
    y2 = int(input("Digite a coordenada Y do segundo ponto: "))
    print(Distancia.distancia(x1, x2, y1, y2))

class Distancia:
    
    def distancia(x1, x2, y1, y2):
        d = math.sqrt( ((x2-x1)**2) + ((y2 - y1)**2) )
        return d


if __name__ == '__main__':
    main()
