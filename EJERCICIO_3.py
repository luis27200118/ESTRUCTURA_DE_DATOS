def seleccion_orden(lista,largo_lista,contador):
    if contador<largo_lista:
        pequeño=lista[contador]
        posicion=contador 
        for i in range(contador+1, largo_lista):
            if lista[i]<pequeño:
                pequeño=lista[i]
                posicion=i
        lista[contador],lista[posicion]=lista[posicion],lista[contador]
        seleccion_orden(lista,largo_lista,contador+1)
A=[7,2,5,3,1,4,9,6]
seleccion_orden(A,len(A),0)
print(A)
