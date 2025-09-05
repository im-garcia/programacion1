def diccionario_geringoso(list):
    new_list = []
    for item in list:
        capadepenapa = ""
        for c in item:
            capadepenapa = capadepenapa + c
            if c == "a":
                capadepenapa = capadepenapa + "pa"
            elif c == "e":
                capadepenapa = capadepenapa + "pe"
            elif c == "i":
                capadepenapa = capadepenapa + "pi"
            elif c == "o":
                capadepenapa = capadepenapa + "po"
            elif c == "u":
                capadepenapa = capadepenapa + "pu"
        tuple = (item, capadepenapa)
        new_list.append(tuple)
    return dict(new_list)

print(diccionario_geringoso(['banana', 'manzana', 'mandarina']))