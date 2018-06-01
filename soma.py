n = int(input("Digite o valor de n: "))
soma = 0
x = 0

if n == 0:
    print ("0")
while n > 0:
    x = n % 10
    n = n // 10
    soma = soma + x
    if n == 0:
        print (soma)
