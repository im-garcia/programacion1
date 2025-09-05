def multiplicar(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado
    
print(f'{" ":>7s}', end="")

for i in range(10):
    print(f"{i:<4d}", end="")

print("\n" + "-"*45)

for i in range(10):
    principio = f'{i}:'
    print(f"{principio:<4}", end="")
    for j in range(10):
        resultado = multiplicar(i, j)
        print(f"{resultado:>4}", end="")
    print()