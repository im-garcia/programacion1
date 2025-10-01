import random
import numpy as np

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=int)
    return album

def album_incompleto(A):
    return np.any(A == 0)

def comprar_figu(figus_total):
    figu = random.randint(0, figus_total - 1)
    return figu

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compras = 0

    while album_incompleto(album):
        figu_toca = comprar_figu(figus_total)
        compras += 1
        album[figu_toca] += 1

    return compras

def experimento_figus(n_repeticiones, figus_total):
    resultados_compras = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(resultados_compras)
    return promedio


n_repeticiones = 100
figus_total = 670
promedio = experimento_figus(n_repeticiones, figus_total)

print(f"Número de repeticiones: {n_repeticiones}")
print(f"Tamaño del álbum: {figus_total}")
print(f"Promedio de compra de figuritas para completar el álbum de {figus_total} figuritas: {promedio:.2f}")

