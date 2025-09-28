import random

def medir_temp(n):
    return [random.normalvariate(37.5, 0.2) for _ in range(n)]

def resumen_temp(n):
    temps = medir_temp(n)
    maximo = max(temps)
    minimo = min(temps)
    prom = sum(temps) / n
    temps.sort()
    if n % 2 == 1:
        mediana = temps[n // 2]
    else:
        mediana = (temps[n // 2 - 1] + temps[n // 2]) / 2
    return maximo, minimo, prom, mediana
