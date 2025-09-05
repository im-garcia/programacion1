import csv

def costo_camion(nombre_archivo):
    'Calcula el costo total de los cajones de frutas de un camión'
    suma = 0.0
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                suma = suma + (float(row[1]) * float(row[2]))
            except ValueError:
                print("Cuidado, faltan datos en el archivo")
    return suma

cost = costo_camion('../Data/camion.csv')
print('Costo total:', cost)
cost = costo_camion('../Data/missing.csv')
print('Costo total:', cost)