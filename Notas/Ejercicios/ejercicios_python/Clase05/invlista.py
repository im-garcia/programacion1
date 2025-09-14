def invertir_lista(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1): 
        invertida.append(lista[i])        
    return invertida
