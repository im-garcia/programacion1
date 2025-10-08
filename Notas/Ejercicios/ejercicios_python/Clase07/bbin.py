def donde_insertar(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio     
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return izq
    
def insertar(lista, x):
    i = donde_insertar(lista, x)
    if lista[i] != x:
        lista.insert(i, x)
    return i

a = [0, 2, 4, 6]
q = donde_insertar(a, 4)
print(q)
a = [0, 2, 4, 6]
q = donde_insertar(a, 4)
print(q)
e = insertar(a, 3)
print(e)