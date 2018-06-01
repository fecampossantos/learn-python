#----- ordem crescente
class OrdemCrescente:
    def main():
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        z = int(input("Digite o terceiro número: "))
        c = ordem(x, y, z)
        return c
    
    def ordem(x, y, z):
        if x < y and y < z:
            return True
        else:
            return False