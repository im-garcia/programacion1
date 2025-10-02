# rebotes.py
# Archivo de ejemplo
# Ejercicio
import sys

n = 0
h = 100.0

if len(sys.argv) > 1:
    h = float(sys.argv[1])

while n < 10:
    n = n + 1
    h = h * (3/5)
    print(n, round(h, 4))