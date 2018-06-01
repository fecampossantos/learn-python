def maiusculas(frase):
    comprimento = len(frase)
    final = ""
    a = 0
    while a < comprimento:
        letra = frase[a]
        if ord(letra) >= 65 and ord(letra) <= 90:
            final = final + letra
        a += 1
    return final
