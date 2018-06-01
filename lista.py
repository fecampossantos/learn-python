lista = []
n = 1
while n != 0:
    n = int(input("Digite uma sequência de números terminados por zero: "))
    if n != 0:
        lista.append(n)

x = len(lista)
a = 1
while a <= x:
    print(lista[-a])
    a = a + 1
