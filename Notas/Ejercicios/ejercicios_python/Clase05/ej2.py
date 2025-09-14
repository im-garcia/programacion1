def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista
    
    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    pos = -1 # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos los elementos de la lista
        if z == e:      # si encontramos a e
            pos = i     # guardamos su posición
            break       # y salimos del ciclo
    return pos