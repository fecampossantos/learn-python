def main():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))
    print("A média é ", media(n1, n2, n3, n4))

def media(n1, n2, n3, n4):
    media = float((n1 + n2 + n3 + n4)/4)
    return media