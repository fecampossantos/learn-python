def primo(n):
    divisor = 2
    aux = n
    fator = 0
    while divisor < aux:
        if n % divisor != 0:
            divisor = divisor + 1
        else:
            divisor = divisor + 1
            fator = fator + 1
    if fator > 0:
        return False
    else:
        return True
            

def n_primos(n):
    conta = 0
    parametro = 2
    while parametro <= n:
        if primo(n) == True:
            conta = conta + 1
            n = n - 1
        else:
            n = n - 1
    return conta