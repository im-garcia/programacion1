import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    También se puede convertir el tipo de cada dato.
    Y trabajar con archivos sin encabezados.
    '''
    with open(nombre_archivo, encoding='utf-8') as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []
        registros = []
        for row in rows:
            if not row:     
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row) ]
                except ValueError:
                    print("Error en la conversión")
            try:
                if has_headers:
                    registro = dict(zip(headers, row))
                else:
                    registro = tuple(row)
                registros.append(registro)
            except ValueError:
                print(f"No se pudo interpretar una fila")
        return registros