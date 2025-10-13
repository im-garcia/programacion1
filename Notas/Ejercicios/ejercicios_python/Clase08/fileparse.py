import csv

def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    También se puede convertir el tipo de cada dato.
    Y trabajar con archivos sin encabezados.
    '''
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    rows = csv.reader(lines)
    if has_headers:
        headers = next(rows)
    if select:
        indices = [headers.index(nombre_columna) for nombre_columna in select]
        headers = select
    else:
        indices = []
    registros = []
    for fila_num, row in enumerate(rows):
        if not row:     
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {fila_num + 1}: No pude convertir {row}")
                    print(f"Fila {fila_num + 1}: Motivo {e}")
                continue

        try:
            if has_headers:
                registro = dict(zip(headers, row))
            else:
                registro = tuple(row)
            registros.append(registro)
        except ValueError:
            print("No se pudo interpretar una fila")
    return registros