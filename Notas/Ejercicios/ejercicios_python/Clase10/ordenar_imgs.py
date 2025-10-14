import os
from datetime import datetime
import shutil

def procesar_nombre(fname):
    """Procesa el nombre de archivos png
    
    Pre: Recibe un nombre de archivo con formato 'nombre_(...)_YYYYMMDD.png'.
    Pos: Devuelve: El nombre sin la fecha, y la fecha como objeto datetime.
    """
    sufijo = fname.split('_')[-1].removesuffix('.png')
    fecha = datetime.strptime(sufijo, '%Y%m%d')
    nombre = fname.rpartition('_')[0] + '.png'
    return nombre, fecha

def procesar(fname, directorio_destino):
    """Procesa archivos png

    Pre: Recibe dos rutas. La primera a un archivo png, y la segunda a una ruta destino.
    Pos: Cambia la fecha de modificación y acceso según la fecha en el nomnbre,
         renombra el archivo sin la fecha y lo mueve al directorio destino.
    """
    nombre_archivo = os.path.basename(fname)
    nombre, fecha = procesar_nombre(nombre_archivo)
    destino = os.path.join(directorio_destino, nombre)
    timestamp = fecha.timestamp()
    
    os.utime(fname, (timestamp, timestamp))
    shutil.move(fname, destino)

def f_principal(parametros):
    """Recorre recursivamente el directorio original buscando archivos png.
    Procesa cada archivo png y elimina subdirectorios vacíos del directorio orignal.
    """
    directorio_original = parametros[1]
    directorio_destino = parametros[2]
    os.makedirs(directorio_destino, exist_ok=True)
    
    for root, dirs, files in os.walk(directorio_original, topdown=False):
        for name in files:
            if name.lower().endswith('.png'):
                procesar(os.path.join(root, name), directorio_destino)
        for name in dirs:
            dir_path = os.path.join(root, name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} directorio_original directorio_destino')
    f_principal(sys.argv)