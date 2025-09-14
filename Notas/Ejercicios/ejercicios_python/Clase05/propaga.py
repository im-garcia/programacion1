def propagar(fosforos):
    i = 0
    lista = fosforos
    while i < len(lista):
        if lista[i] == 1:
            pos = i
            while pos > 0 and lista[pos-1] != -1:
                lista[pos-1] = 1
                pos -= 1
            pos = i
            while pos < len(lista) -1 and lista[pos + 1] != -1:
                lista[pos + 1] = 1
                pos += 1
            i = pos
        i += 1
    return lista

print(propagar([-1, 0, 0, 0, 0]))
print(propagar([1, 0, 0, 0, 0, 0]))
print(propagar([0, 0, 0, 0, 0, 1]))
print(propagar([-1, 1, 1, 1, 0]))
print(propagar([-1, 0, 0, 0, 0, 1]))
print(propagar([0, 0, 0,-1, 1, 0, 0, 0, -1, 0, 1, 0, 0]))
print(propagar([0, 0, 0, 1, 0, 0]))
print(propagar([0, 0, 0, 0, 0, 0]))
print(propagar([1, 1, 1, 1, 1]))
print(propagar([-1, -1, -1, -1, -1]))