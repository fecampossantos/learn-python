class Adjacentes:
    def calculo(n):
        adjacentes = False         #false ate que se prove true
        algarismoAnterior = n % 10
        n = n // 10
        while n > 0 and not adjacentes:
            algarismoAtual = n % 10
            n = n // 10
            if algarismoAtual == algarismoAnterior:
                adjacentes = True
            algarismoAnterior = algarismoAtual
        if adjacentes:
            return True, algarismoAtual
        else:
            return False
