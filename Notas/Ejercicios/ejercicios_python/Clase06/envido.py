import random

def generar_mazo():
    palos = ["oro", "copa", "espada", "basto"]
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    mazo = [(valor, palo) for valor in valores for palo in palos]
    return mazo

def obtener_mano(naipes, n=3):
    mano = random.sample(naipes, n)
    return mano

def valor_envido(carta):
    valor, palo = carta
    if valor >= 10:
        return 0
    return valor

def calculo_envido():
    mazo = generar_mazo()
    mano = obtener_mano(mazo)
    mejor = 0
    for i in range(3):
        for j in range(i+1, 3):
            if mano[i][1] == mano[j][1]:
                puntos = valor_envido(mano[i]) + valor_envido(mano[j]) + 20
                mejor = max(mejor, puntos)
    return mejor if mejor > 0 else False

def calc_prob_envido(target, N = 1000):
    E = sum([calculo_envido() == target for _ in range(N)])
    prob = E/N
    return prob

N = 10000000
print("Probablidad de hacer envido con 31")
print(calc_prob_envido(31, N))
print("Probablidad de hacer envido con 32")
print(calc_prob_envido(32, N))
print("Probablidad de hacer envido con 33")
print(calc_prob_envido(33, N))