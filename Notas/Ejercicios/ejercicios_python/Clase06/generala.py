import random

def tirar(cant_dados):
    return [ random.randint(1,6) for _ in range(cant_dados) ]

def es_generala(tirada):
    return len(set(tirada)) == 1

def mas_repetido(dados):
    cant = []
    for i in range(1,7):
        cant.append(dados.count(i)) 
    maximo = max(cant)
    num_repetido = cant.index(maximo)
    return num_repetido + 1

def jugar_mano_tres_tiradas():
    tirada = tirar(5)
    for i in range(2):
        if es_generala(tirada):
            return True
        repetido = mas_repetido(tirada)
        dados_guardados = [d for d in tirada if d == repetido]
        dados_nuevos = tirar(6 - len(dados_guardados))
        tirada = dados_guardados + dados_nuevos
    return es_generala(tirada)

def prob_generala(N):
    G = sum([jugar_mano_tres_tiradas() for _ in range(N)])
    prob = G/N
    return prob

