#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.5. Función tiene_a()
#Comentario: El error consiste en solamente comparar en el if el primer caracter de cada string y además de hacer la comparación con una "a" minúscula.
#    Lo corregí sacando el else con el return False, además de hacer un lower para que tuviera sentido la comparación.
#    A continuación va el código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False
        

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.6. Función tiene_a(), nuevamente
#Comentario: El error era de tipo sintáctico. Faltaban los ":", cambié "=" por "==", y "Falso" por "False".
#    A continuación va el código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.7. Función tiene_uno()
#Comentario: El error consiste en los tipos de variables. La función manipula strings pero se la llama con un int en el último ejemplo. Se podría haber cambiado el argumendo de la función, de 1984 a "1984", pero decidí cambiar la función en sí y convertir en string al int. Lo mejor sería agregar un bloque try-except para manejar casos así.
def tiene_uno(expresion):
    n = len(str(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str(expresion)[i].lower() == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


#%%
#Ejercicio 3.8. Función suma()
#Comentario: El error consiste en no devolver nada en la función. Lo solucioné agregando el return.
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.9. Función leer_camion()
#Comentario: El error está en no inicilizar el diccionario adentro del for, para cada fila. Porque lo que termina pasando es que toma los valores de la última fila.
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)