# Nombre: Ignacio Miguel García
# DNI: 42469590
# Mail: chonamiguelgarcia@gmail.com

# Ejercicio 1

import csv

def leer_ventas(nombre_archivo):
    '''
    Lee el contenido de un archivo csv. Recibe la ruta del archivo como un string 
    y devuelve el contenido del archivo en una lista de diccionarios.
    '''
    ventas = []
    try:    
        with open(nombre_archivo, 'rt', encoding="utf-8") as file:
            rows = csv.reader(file)
            headers = next(rows)
            for row in rows:   
                venta = {}
                venta[headers[0]] = row[0]
                venta[headers[1]] = row[1]
                venta[headers[2]] = float(row[2])
                venta[headers[3]] = int(row[3])
                ventas.append(venta)
        return ventas
    except FileNotFoundError:
        print("No existe el archivo o la ruta al archivo es incorrecta.")
        return {}

# Ejercicio 2

def ingresos_por_genero(ventas):
    "Calcula los ingresos de ventas por género. Recibe una lista de diccionarios y devuelve un diccionario."
    generos = {}
    # La verdad, no sé si es la solución más bonita, o eficiente, para inicializar el diccionario con ceros. Pero parece que funciona.
    for venta in ventas:
        generos[venta['genero']] = 0
    for venta in ventas:
        generos[venta['genero']] += venta['precio'] * venta['cantidad']
    return(generos)


#Ejercicio 3

def generar_informe(nombre_archivo):
    '''
    Muestra en pantalla un informe de los ingresos por género y el ingreso total. 
    Recibe la ruta de un archivo como string y no devuelve nada.
    '''
    ventas = leer_ventas(nombre_archivo)
    ingresos = ingresos_por_genero(ventas)
    ingresos = ingresos.items()
    print("Ingresos por género:\n")
    total = 0.0
    for k, v in ingresos:
        print(f"{k}: ${round(v, 2)}")
        total += v
    print(f"\nIngreso total: ${round(total,2)}")

import sys

if len(sys.argv) == 2:
    generar_informe(sys.argv[1])
else:
    print("No olvide incluir la ruta al archivo csv.")