import csv

def leer_parque(nombre_archivo, parque):
    lista_parque = []
    with open(nombre_archivo, "rt", encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            if parque in record['espacio_ve']:
                lista_parque.append(record)
    return lista_parque

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        especies.append(arbol["nombre_com"])
    return set(especies)

from collections import Counter

def contar_ejemplares(lista_arboles):
    contador = Counter()
    for arbol in lista_arboles:
        contador[arbol['nombre_com']] += 1
    return contador 

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            alturas.append(float(arbol['altura_tot']))
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            inclinaciones.append(int(arbol['inclinacio']))
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    especie_max = ""
    inclinacion_max = -1
    for especie in especies(lista_arboles):  
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if inclinaciones:   
            max_inc = max(inclinaciones)
            if max_inc > inclinacion_max:
                inclinacion_max = max_inc
                especie_max = especie
    return especie_max, inclinacion_max

def especie_promedio_mas_inclinada(lista_arboles):
    especiess = especies(lista_arboles)
    especie_max_promedio = ""
    promedio_max = 0
    for especie in especiess:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if inclinaciones:
            promedio = sum(inclinaciones) / len(inclinaciones)
            if promedio > promedio_max:
                promedio_max = promedio
                especie_max_promedio = especie
    return (especie_max_promedio, promedio_max)

"""
Todos los prints que usé para ir probando las funciones.

general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")

cantidad_gp = contar_ejemplares(general_paz)
cantidad_la = contar_ejemplares(los_andes)
cantidad_ce = contar_ejemplares(centenario)

print("General Paz", cantidad_gp.most_common(5))
print("Los Andes", cantidad_la.most_common(5))
print("Centenario", cantidad_ce.most_common(5))

especies_gp = especies(general_paz)
especies_la = especies(los_andes)
especies_ce = especies(centenario)

alturas_jacaranda_gp = obtener_alturas(general_paz, "Jacarandá")
alturas_jacaranda_la = obtener_alturas(los_andes, "Jacarandá")
alturas_jacaranda_ce = obtener_alturas(centenario, "Jacarandá")

print("General Paz", max(alturas_jacaranda_gp), sum(alturas_jacaranda_gp)/len(alturas_jacaranda_gp))
print("Los Andes", max(alturas_jacaranda_la), sum(alturas_jacaranda_la)/len(alturas_jacaranda_la))
print("Centenario", max(alturas_jacaranda_ce), sum(alturas_jacaranda_ce)/len(alturas_jacaranda_ce))

print("Centenario:", especimen_mas_inclinado(centenario))

print("Los Andes:", especie_promedio_mas_inclinada(los_andes))
"""