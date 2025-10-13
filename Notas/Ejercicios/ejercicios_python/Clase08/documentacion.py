def valor_absoluto(n):
    '''Devuelve el valor absoluto de un número.

    Pre: Recibe un número.
    Pos: Devuelve n si n es mayor o igual a 0.
         Si n es negativo, devuelve -n.
    '''
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):
    '''Devuelve la suma de todos los números pares de una lista.

    Pre: Recibe l, una lista de números.
    Pos: Devuelve la suma de los números pares de la lista. 
         Si no hay pares, devuelve 0.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

    # El invariante de ciclo es: 
    # res contiene el resultado de la suma 
    # de los elementos pares de la lista en cada iteración.

def veces(a, b):
    '''Devuelve la suma de un mismo número n veces.

    Pre: Recibe dos números
    Pos: Devuelve la suma de b veces a. 
         Si b es igual o menor a 0, se devuelve 0.
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

    # El invariante de ciclo es:
    # res contiene la suma de b veces a por cada iteración.

def collatz(n):
    '''Devuelve la cantidad de pasos necesarios para llegar a 1 
       desde un número entero n, siguiendo la conjetura de Collatz.
    
    Pre: Recibe un número entero.
    Pos: Devuelve 1 si n es 1.
         Si n es mayor a 1, devuelve la cantidad de pasos para llegar a 1
         siguiendo la conjetura de Collatz.
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

    # El invariante de ciclo es:
    # En cada iteración, res guarda la cantidad de pasos realizados hasta ese punto y
    # n contiene el valor actual de la secuencia de Collatz