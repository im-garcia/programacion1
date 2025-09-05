import csv

def leer_camion(nombre_archivo):
    'Lee los datos de un camión.'
    camion = []
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                camion.append(record)
            except ValueError:
                print(f"Fila {i}: No pude interpretar: {row}")
    return camion

def buscar_precio(nombre_archivo):
    'Busca el precio de una fruta o verdura en el archivo de precios.'
    precios = {}
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        for i, row in enumerate(rows, start=1):
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f"Fila {i}: No tiene datos.")
    return precios

camion = leer_camion("../Data/camion.csv")
precios = buscar_precio("../Data/precios.csv")

costo = 0.0
recaudacion = 0.0

for s in camion:
    try:
        costo += int(s['cajones'])*float(s['precio'])
        recaudacion += int(s['cajones'])* float(precios[s['nombre']])
    except ValueError  as e:
        print(f"Datos inválidos: ({e})")

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