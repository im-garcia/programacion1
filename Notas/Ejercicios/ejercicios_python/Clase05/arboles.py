import csv
from pprint import pprint

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        arboleda = [ { name: func(val) for name, func, val in zip(headers, types, row) } for row in rows ]
    return arboleda

def medidas_de_especies(especies, arboleda):
    medidas_especies =  { especie: [ (arbol['altura_tot'], arbol['diametro']) for arbol in arboleda  if arbol['nombre_com'] == especie ] for especie in especies}
    return medidas_especies

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

medidas_especies = medidas_de_especies(especies, arboleda)
