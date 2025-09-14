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
