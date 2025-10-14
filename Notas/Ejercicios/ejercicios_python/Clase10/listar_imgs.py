import os

def archivos_png(directorio):
    '''Devuelve una lista con archivos png dentro del árbol de directorios de 'directorio'

    Pre: Recibe una ruta a un directorio
    Pos: Devuelve una lista de la totalidad de archivos png dentro del árbol de directorios de 'directorio'
    '''
    lista_pngs = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name.lower().endswith('.png'):
                lista_pngs.append(name)
    return lista_pngs

def f_principal(parametros):
    directorio = parametros[1]
    print(archivos_png(directorio))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} directorio')
    f_principal(sys.argv)