import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y

def punto_en_circ():
    x, y = generar_punto()
    if (x**2 + y**2) < 1.0:
        return True
    else:
        return False

def calc_pi(N = 1000):
    M = sum([punto_en_circ() for _ in range(N)])
    pi = 4 * M/N
    return pi

N = 100000
print(calc_pi(N))