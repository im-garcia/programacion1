import random

def tirar():
    return random.randint(1,365)

def cumplen_dos(grupo_de_personas):
    return len(set(grupo_de_personas)) < len(grupo_de_personas)

def grupo_de_personas(n):
    grupo = [ tirar() for _ in range(n) ]
    return grupo

def simulación_cum():
    return 0


print(cumplen_dos(grupo_de_personas(10)))