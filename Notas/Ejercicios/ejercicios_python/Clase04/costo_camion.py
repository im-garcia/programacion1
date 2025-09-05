import csv

def costo_camion(nombre_archivo):
    'Calcula el costo total de los cajones de frutas de un camión'
    costo_total = 0.0
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f"Fila {i+1}: No pude interpretar: {row}")
    return costo_total

cost = costo_camion('../Data/camion.csv')
print('Costo total:', cost)
cost = costo_camion('../Data/missing.csv')
print('Costo total:', cost)
cost = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', cost)