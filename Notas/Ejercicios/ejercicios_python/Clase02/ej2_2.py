suma = 0
with open("../Data/camion.csv", "rt") as file:
    headers = next(file)
    for line in file:
        row = line.split(",")
        suma = suma + (float(row[1]) * float(row[2]))
print("Costo total", suma)