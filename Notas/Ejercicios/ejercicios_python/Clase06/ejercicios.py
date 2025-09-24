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

def jugar_mano_tres_tiradas():
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
    G = sum([jugar_mano_tres_tiradas() for i in range(N)])
    prob = G/N
    print(f'Tiré {N} manos de tres jugadas, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala no necesariamente servida mediante {prob:.6f}.')

    return prob

N = 100
prob = prog_generala(N)
print(prob)
