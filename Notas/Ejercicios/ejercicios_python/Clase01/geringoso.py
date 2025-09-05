cadena = "boligoma"
capadepenapa = ""
for c in cadena:
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
print(capadepenapa)