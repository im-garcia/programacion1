import fileparse

def leer_camion(nombre_archivo):
    'Lee los datos de un camión.'
    with open(nombre_archivo, encoding='utf-8') as f:
        camion = fileparse.parse_csv(f, types=[str, int, float])
        return camion

def leer_precios(nombre_archivo):
    'Busca el precio de una fruta o verdura en el archivo de precios.'
    with open(nombre_archivo, encoding='utf-8') as f:
        precios = fileparse.parse_csv(f, types=[str, float], has_headers=False)
        return dict(precios)

def hacer_informe(camion, precios):
    informe = []
    for row in camion:
        try: 
            fila = (
                row['nombre'], 
                int(row['cajones']), 
                float(row['precio']), 
                precios[row['nombre']] - float(row['precio']) 
            )
            informe.append(fila)
        except(ValueError, KeyError) as e:
            print(f"Fila con datos inválidos: {row} ({e})")
    return informe

def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

def f_principal(parametros):
    archivo_camion = parametros[1]
    archivo_precios = parametros[2]
    informe_camion(archivo_camion, archivo_precios)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' ' archivo_camion archivo_precios')
    f_principal(sys.argv)