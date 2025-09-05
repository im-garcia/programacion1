import csv

def leer_camion(nombre_archivo):
    'Lee los datos de un camión.'
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

def buscar_precio(nombre_archivo):
    'Busca el precio de una fruta o verdura en el archivo de precios.'
    precios = {}
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print("Hay líneas vacías en el archivo de precios.")
    return precios

camion = leer_camion("../Data/camion.csv")
precios = buscar_precio("../Data/precios.csv")

costo = 0.0
recaudacion = 0.0

for s in camion:
    costo += s['cajones']*s['precio']
    recaudacion += s['cajones'] * precios[s['nombre']]
diferencia = recaudacion - costo

print("-----BALANCE-----")
print("Costo del camión:", costo)
print("Recaudación:", recaudacion)
print("Diferencia:", diferencia)

if diferencia > 0:
    print("Hubo ganancia.")
elif diferencia == 0:
    print("No hubo perdida ni ganancia.")
else:
    print("Hubo perdida")
