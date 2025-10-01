import csv
import matplotlib.pyplot as plt
import numpy as np

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
    alturas = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá' ]
    plt.hist(alturas, bins=25, color='purple')
    plt.title('Histograma de alturas de Jacarandás')
    plt.xlabel('Altura (m)')
    plt.ylabel('Frecuencia')
    plt.show()

def scatter_hd(lista_de_pares):
    # alturas, diametros = zip(*lista_de_pares está buena esta opción
    # si lo hago con numpy:
    lista_de_pares = np.array(lista_de_pares)
    alturas = lista_de_pares[:,0]
    diametros = lista_de_pares[:,1]
    plt.scatter(diametros,alturas, alpha=0.5)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

def scatter_hd_especies(medidas):
    for especie, values in medidas.items():
        lista_de_pares = np.array(values)
        alturas = lista_de_pares[:,0]
        diametros = lista_de_pares[:,1]
        plt.scatter(diametros, alturas, alpha=0.3)
        plt.xlim(0, 100)
        plt.ylim(0, 40)
        plt.xlabel("Diámetro (cm)")
        plt.ylabel("Alto (m)")
        plt.title(f"Relación diámetro-alto para {especie}")
        plt.show()

# lista_de_pares = [ (arbol['altura_tot'], arbol['diametro']) for arbol in arboleda  if arbol['nombre_com'] == 'Jacarandá' ]
# scatter_hd(lista_de_pares)

# arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")

# mespecies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

# medidas = medidas_de_especies(especies, arboleda)

# scatter_hd_especies(medidas)