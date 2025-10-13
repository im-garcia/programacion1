import informe_funciones

def costo_camion(nombre_archivo):
    'Calcula el costo total de los cajones de frutas de un camión'
    costo_total = 0.0
    camion = informe_funciones.leer_camion(nombre_archivo)
    for row in camion:
        costo_total += row['cajones'] * row['precio']
    return costo_total

# scost = costo_camion('../Data/camion.csv')
# print('Costo total:', cost)