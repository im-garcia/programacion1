# rebotes.py
# Archivo de ejemplo
# Ejercicio
import sys

def rebotar(altura, saltos):
    i = 0
    while i < saltos:
        i += 1
        altura = altura * (3/5)
        print(i, round(altura, 2))

def f_principal(parametros):
    altura = float(parametros[1])
    saltos = float(parametros[2])
    rebotar(altura, saltos)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' ' altura saltos')
    f_principal(sys.argv)