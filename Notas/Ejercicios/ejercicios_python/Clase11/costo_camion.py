import informe_final_finalPosta as informe_final_finalPosta

def costo_camion(nombre_archivo):
    'Calcula el costo total de los cajones de frutas de un camión'
    costo_total = 0.0
    camion = informe_final_finalPosta.leer_camion(nombre_archivo)
    for lote in camion:
        costo_total += lote.cajones * lote.precio
    return costo_total

def f_principal(parametros):
    archivo_camion = parametros[1]
    costo = costo_camion(archivo_camion)
    print(f'Costo total: {costo}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' ' archivo_camion archivo_precios')
    f_principal(sys.argv)