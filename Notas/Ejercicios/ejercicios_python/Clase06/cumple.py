import random

def tirar():
    return random.randint(1,365)

def cumplen_dos(grupo_de_personas):
    return len(set(grupo_de_personas)) < len(grupo_de_personas)

def grupo_de_personas(n):
    grupo = [ tirar() for _ in range(n) ]
    return grupo

def simulación_cum(N, tamaño_grupo):
    G = sum([cumplen_dos(grupo_de_personas(tamaño_grupo)) for _ in range(N)])
    prob = G/N
    return prob

N = 100000
for i in range(1, 80):
    if simulación_cum(N, i) > 0.5:
        print("Para que la probabilidad de que dos personas cumplan el mismo día sea mayor al 50% se necesita al menos un grupo de " + str(i) + " personas")
        break