import random

def tirar(cant_dados):
    return [ random.randint(1,6) for i in range(cant_dados) ]

def es_generala(tirada):
    return len(tirada) == len(set(tirada))

def mas_repetido(dados):
    cant = []
    for i in range(1,7):
        cant.append(dados.count(i)) 
    maximo = max(cant)
    num_repetido = cant.index(maximo)
    return num_repetido + 1

def jugar_mano():
    tirada = tirar(6)
    for i in range(2):
        if es_generala(tirada):
            return True
        repetido = mas_repetido(tirada)
        dados_guardados = [d for d in tirada if d == repetido]
        dados_nuevos = tirar(6 - len(dados_guardados))
        tirada = dados_guardados + dados_nuevos
    return es_generala(tirada)

def prog_generala(N):
    return N

tirada = jugar_mano()
print(tirada)
cantidades = mas_repetido(tirada)
print(cantidades)