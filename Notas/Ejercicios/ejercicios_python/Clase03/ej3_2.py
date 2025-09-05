import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            lote = {}
            lote[headers[0]] = row[0]
            lote[headers[1]] = int(row[1])
            lote[headers[2]] =float(row[2])
            camion.append(lote)
    return camion
