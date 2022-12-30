def sumarecursiva(a,b):
    if b==0:
        return a
    else:
        return sumarecursiva(a,b-1)+1
n=sumarecursiva(5,3)
print(n)