def potencia(n):
    if n % 2 == 0:
        print("Es un número par")
        A = 2*(2*potencia(n)/2)
        print(A)
potencia(4)