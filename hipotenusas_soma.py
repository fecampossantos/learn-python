import math
class Hipotenusa:
    def main():
        n = int(input("Digi))
    def soma_hipotenusas(n):
        cateto1 = 1
        cateto2 = 1
        soma = 0
        nada = 0
        while cateto1 < n:
            while cateto2 < n:
                hip = math.sqrt((cateto1**2) + (cateto2**2))
                if hip % 1 == 0:
                    soma = soma + hip
                if cateto2 < n:
                    cateto2 = cateto2 + 1
            cateto2 = 1
            cateto1 = cateto1 + 1
        soma = soma/2
        return soma