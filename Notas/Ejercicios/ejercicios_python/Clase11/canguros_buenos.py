class Canguro():
    def __init__(self, nombre, lista=None): 
        self.nombre = nombre
        if lista is None:
            self.contenido_marsupio = [] 
        else:
            self.contenido_marsupio = lista
    
    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)

    def __str__(self):
        t = [self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            t.append('    ' + str(obj))
        return '\n'.join(t)
    
madre_canguro = Canguro('Madre')
cangurito = Canguro('Hijo')
madre_canguro.meter_en_marsupio('llaves')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)


# # canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver
# """
# 
# class Canguro:
#     """Un Canguro es un marsupial."""
#     
#     def __init__(self, nombre, contenido=None): 
#         # El problema está aquí, lista mutable por defecto
#         # Hay que evitar usar listas (u otros objetos mutables) como valores por defecto
#         # porque son compartidos entre todas las instancias que no proveen ese argumento
#         # Esto puede llevar a comportamientos inesperados
#         # Por ejemplo, todas las instancias de Canguro que no proveen
#         # el argumento 'contenido' compartirán la misma lista por defecto
#         # lo que puede causar que los objetos se mezclen entre instancias
#         # La solución es usar None como valor por defecto y crear una nueva lista dentro del método si es necesario
#         # así evitamos este problema
#         """Inicializar los contenidos del marsupio.
# 
#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         if contenido is None:
#             self.contenido_marsupio = []
#         else:
#             self.contenido_marsupio = contenido
# 
#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)
# 
#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.
# 
#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)
# 
# #%%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)
# 
# print(madre_canguro)
# 
# # Al ejecutar este código todo parece funcionar correctamente.
# # Para ver el problema, imprimí el contenido de cangurito.