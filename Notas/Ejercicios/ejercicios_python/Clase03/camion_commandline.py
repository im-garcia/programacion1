import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

cost = costo_camion(nombre_archivo)
print('Costo total:', cost)