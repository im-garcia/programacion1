class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl():
    '''Representa una torre de control de trafico aereo.'''

    def __init__(self):
        '''Crea una torre de control sin aviones esperando.'''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, id_avion):
        '''Agrega el avion con identificador id_avion 
        a la cola de aviones esperando para aterrizar.'''
        self.arribos.encolar(id_avion)
        
    def nueva_partida(self, id_avion):
        '''Agrega el avion con identificador id_avion 
        a la cola de aviones esperando para despegar.'''
        self.partidas.encolar(id_avion)

    def ver_estado(self):
        '''Imprime el estado actual de las colas de arribos y partidas.'''

        str_arribos = ", ".join(self.arribos.items)
        print(f'Vuelos esperando para aterrizar: {str_arribos}')
        
        str_partidas = ", ".join(self.partidas.items)
        print(f'Vuelos esperando para despegar: {str_partidas}')


    def asignar_pista(self):
        '''Asigna la pista al siguiente avion que debe aterrizar o despegar.
        Devuelve una tupla (id_avion, operacion), donde operacion es 
        'aterrizaje' o 'despegue'.
        Si no hay aviones esperando, levanta ValueError.'''
        if not self.arribos.esta_vacia():
            id_avion = self.arribos.desencolar()
            print(f'El vuelo {id_avion} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            id_avion = self.partidas.desencolar()
            print(f'El vuelo {id_avion} despegó con éxito.')
        else:
            print('No hay vuelos en espera.')