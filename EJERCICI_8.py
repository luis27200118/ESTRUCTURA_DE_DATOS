def potencia(b,n):
    if n <= 0:
        respuesta = 1
    elif n % 2 == 0:
        pot = potencia(b, n/2)
        respuesta = pot * pot
    else:
        pot = potencia(b, (n-1)/2)
        respuesta = pot * pot * b
    print(respuesta)
    return respuesta
potencia(3,3)