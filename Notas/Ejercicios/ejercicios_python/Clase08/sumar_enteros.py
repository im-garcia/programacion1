def sumar_enteros_ciclo(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if hasta < desde:
        return suma

    for i in range(desde, hasta+1):
        suma += i
    return suma

def sumar_enteros_fórmula(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta < desde:
        return 0
    
    suma_desde = desde*(desde-1)/2
    suma_hasta = hasta*(hasta+1)/2
    suma = suma_hasta - suma_desde
    return suma

