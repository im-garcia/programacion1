import csv

def parsear_valor(valor):
    try:
        if '.' in valor:
            return float(valor)
        else:
            return int(valor)
    except ValueError:
        return valor

def leer_camion(nombre_archivo):
    'Lee los datos de un camión.'
    camion = []
    with open(nombre_archivo, "rt", encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            if len(row) != len(headers):   
                print(f"Fila {i}: longitud incorrecta {row}")
                continue
            valores = []
            for v in row:
                valores.append(parsear_valor(v))
            record = dict(zip(headers, valores))
            camion.append(record)
    return camion

def leer_precios(nombre_archivo):
    'Busca el precio de una fruta o verdura en el archivo de precios.'
    precios = {}
    with open(nombre_archivo, "rt") as file:
        rows = csv.reader(file)
        for i, row in enumerate(rows, start=1):
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f"La fila {i} de '{nombre_archivo}' no tiene datos.")
    return precios

def hacer_informe(camion, precios):
    informe = []
    for r in camion:
        try: 
            fila = (
                r['nombre'], 
                int(r['cajones']), 
                float(r['precio']), 
                precios[r['nombre']] - float(r['precio']) 
            )
            informe.append(fila)
        except(ValueError, KeyError) as e:
            print(f"Fila con datos inválidos: {r} ({e})")
    return informe

camion = leer_camion("../Data/camion.csv")
precios = leer_precios("../Data/precios.csv")
informe = hacer_informe(camion, precios)

headers = ("Nombre", "Cajones", "Precio", "Cambio")
encabezado = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
separador = ""
for header in headers:
    separador += "-"*10 + " "

print(encabezado)
print(separador)

for nombre, cajones, precio, cambio in informe:
    precio = f'${precio:.2f}'
    print(f"{nombre:>10s} {cajones:>10d} {precio:>10} {cambio:>10.2f}")
