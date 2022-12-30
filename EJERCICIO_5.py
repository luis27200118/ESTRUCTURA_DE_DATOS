import time
def fibonacci_recursivo(numero):
    if numero==0 or numero==1:
        return 1
    else:
        return fibonacci_recursivo(numero-1)+fibonacci_recursivo(numero-2)
tiempo1=time.perf_counter()
fibonacci_recursivo(8)
tiempo2=time.perf_counter()
print("fibonacci recursivo demoro:", tiempo2-tiempo1)

def fibonacci(n):
    a=0
    b=1
    for k in range(n+1):
        c=b+a
        a=b
        b=c
    return a
tiempo1=time.perf_counter()
fibonacci(8)
tiempo2=time.perf_counter()
print("Fibonacci no recursivo demoró", tiempo2-tiempo1)