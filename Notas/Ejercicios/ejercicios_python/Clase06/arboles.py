import csv
import matplotlib.pyplot as plt

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

def histogram_h():
    arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
    medidas_jacarandá = medidas_de_especies(['Jacarandá'], arboleda)
    alturas = [alturas for alturas, _ in medidas_jacarandá['Jacarandá']]
    plt.hist(alturas,bins=25)
    plt.show()

def scatter_hd(lista_de_pares):
    alturas = [alturas for alturas, _ in medidas_jacarandá['Jacarandá']]
    diametros = [diametros for _, diametros in medidas_jacarandá['Jacarandá']]
    plt.scatter(diametros,alturas)
    plt.show()

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
medidas_jacarandá = medidas_de_especies(['Jacarandá'], arboleda)
scatter_hd(medidas_jacarandá)