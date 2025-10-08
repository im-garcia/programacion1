def buscar_u_elemento(lista, e):
    '''Busca la última apareción de un elemento e en la lista
    
    Si e está en lista devuelve el índice de su última aparición,
    de lo contrario devuelve -1.
    '''
    pos = -1 
    for i in range(len(lista) - 1, -1, -1): 
        if lista[i] == e:     
            pos = i     
            break       
    return pos

def buscar_n_elemento(lista, e):
    '''Devuelve la cantidad de veces que aparece el elemento e 
    en la lista
    '''
    count = 0
    for z in lista: 
        if z == e:      
            count += 1     
    return count

def busqueda_lineal_lordenada(lista,e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    Primero ordena la lista y luego compara si el elemento es igual, y en caso contrario, si es mayor.
    '''
    lista.sort()
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            pos = i 
            break
        elif z>e:
            break
    return pos

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.
    '''
    m = lista[0]
    for e in lista: 
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el mínimo de una lista, 
    la lista debe ser no vacía.
    '''
    m = lista[0]
    for e in lista: 
        if e < m:
            m = e
    return m