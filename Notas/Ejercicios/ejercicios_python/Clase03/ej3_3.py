import csv

def buscar_precio(archivo):
    'Busca el precio de una fruta o verdura en el archivo de precios'
    precios = {}
    with open(archivo, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print("Hay algo raro en el archivo")
    return precios