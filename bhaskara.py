import math

def main():
    a = float(input("Qual o valor de a? "))
    b = float(input("Qual o valor de b? "))
    c = float(input("Qual o valor de c? "))
    d = Bhaskara.calculo(a, b, c)
    print (d)

class Bhaskara:
        
    def delta(a, b, c):
        delta = (b**2) - (4*a*c)
        return delta
    
    def calculo(a, b, c):
        delta = Bhaskara.delta(a, b, c)
        
        if delta == 0:
            raiz1 = (-(b) + (math.sqrt(delta))) / (2*a)
            return (1, raiz1) #devolve que existe uma raíz e o valor dela

        elif delta < 0:
            return 0

        else:
                raiz1 = (-(b) + (math.sqrt(delta))) / (2*a)
                raiz2 = (-(b) - (math.sqrt(delta))) / (2*a)

                if raiz1 >= raiz2:
                    return (2, raiz1, raiz2)
                else:
                    return (2, raiz2, raiz1)

if __name__ == "__main__":
    main()
