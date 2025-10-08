def busqueda_secuencial_comps(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria_comps(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comps = 0
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio, comps  
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return -1, comps

import random

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    import matplotlib.pyplot as plt
    import numpy as np

    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

    plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
    
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos,comps_promedio,label = 'Búsqueda Binaria')

    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la búsqueda secuencial vs la búsqueda binaria")
    plt.legend()
    plt.show()

# m = 10000
# k = 1000

# graficar_bbin_vs_bseq(m, k)

