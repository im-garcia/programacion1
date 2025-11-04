import fileparse
import lote
import formato_tabla

def leer_camion(nombre_archivo):
    'Lee los datos de un camión.'
    with open(nombre_archivo, encoding='utf-8') as f:
        camion_dicts = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
        return camion

def leer_precios(nombre_archivo):
    'Busca el precio de una fruta o verdura en el archivo de precios.'
    with open(nombre_archivo, encoding='utf-8') as f:
        precios = fileparse.parse_csv(f, types=[str, float], has_headers=False)
        return dict(precios)

def hacer_informe(camion, precios):
    informe = []
    for lote in camion:
        try: 
            fila = (
                lote.nombre, 
                int(lote.cajones), 
                float(lote.precio), 
                precios[lote.nombre] - float(lote.precio) 
            )
            informe.append(fila)
        except(ValueError, KeyError) as e:
            print(f"Fila con datos inválidos: {lote} ({e})")
    return informe

def imprimir_informe(informe, formateador):
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt='txt'):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)

    informe = hacer_informe(camion, precios)

    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)

def f_principal(parametros):
    archivo_camion = parametros[1]
    archivo_precios = parametros[2]
    if len(parametros) == 3:
        fmt = 'txt'
    else:
        fmt = parametros[3]
    informe_camion(archivo_camion, archivo_precios, fmt)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' ' archivo_camion archivo_precios (formato)')
    f_principal(sys.argv)