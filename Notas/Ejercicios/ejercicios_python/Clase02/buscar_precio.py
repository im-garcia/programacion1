def buscar_precio(item):
    'Busca el precio de una fruta o verdura en el archivo de precios'
    with open("../Data/precios.csv", "rt") as file:
        found = False
        for line in file:
            row = line.split(",")
            if row[0] == item:
                print(f"El precio de un cajón de {item} es: {row[1]}", end="")
                found = True
        if not found:
            print(f"{item} no figura en el listado de precios.")