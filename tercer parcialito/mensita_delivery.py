import os
import pandas as pd
import numpy as np

def cargar_pedidos(ruta_base):
    '''Carga los datos de ventas desde un archivo CSV ubicado en la ruta especificada.
    Para usar la función, se debe proporcionar la ruta base donde se encuentra el archivo 'data/ventas_mensita.csv'.
    Un ejemplo de uso (si el archivo csv se encuentra en el mismo directorio que el archivo .py), sería:
    df = cargar_pedidos('.')
    '''
    fname = os.path.join(ruta_base, 'data/ventas_mensita.csv')
    try:
        df = pd.read_csv(fname)
        return df
    except FileNotFoundError:
        print(f"El archivo {fname} no se encuentra en el directorio especificado.")

def agregar_minutos_entrega(df):
    '''Agrega una columna 'minutos_entrega' al DataFrame, que representa el tiempo en minutos de la diferencia entre
    la fecha de entrega y la fecha del pedido.
    '''
    df_copy = df.copy()
    # Utilicé la función de pandas to_datetime para convertir las columnas de fecha en objetos datetime 
    # y no la de datetime porque me pareció más conveniente en este caso.
    fecha_pedido = pd.to_datetime(df_copy['fecha_pedido'], format = '%d/%m/%Y %H:%M')
    fecha_entrega = pd.to_datetime(df_copy['fecha_entrega'], format = '%d/%m/%Y %H:%M')
    df_copy['minutos_entrega'] = (fecha_entrega - fecha_pedido) / np.timedelta64(1, 'm')
    return df_copy 

def top_productos(df, top_n=5, solo_entregados=True):
    '''Devuelve un DataFrame con los top_n productos más vendidos, junto con la cantidad vendida,
    el total recaudado y el tiempo promedio de entrega en minutos. Si solo_entregados es True, 
    solo se consideran los pedidos que fueron entregados.
    '''
    df_copy = df.copy()

    # Para quedarnos solo con los entregados.
    if solo_entregados:
        df_copy = df_copy[df_copy['entregado'] == 'sí']
    
    # Agrupo por producto recorriendo con un for y calculo las métricas.  
    productos = df_copy['producto'].unique()
    cols = ['producto', 'cantidad', 'total', 'minutos_entrega']
    productos_list = []
    for producto in productos:
        dict_producto = {}
        df_producto = df_copy[df_copy['producto'] == producto]
        df_producto = df_producto[cols]
        dict_producto['producto'] = producto
        dict_producto['cantidad'] = df_producto['cantidad'].sum()
        dict_producto['total'] = df_producto['total'].sum()
        dict_producto['tiempo_promedio_entrega'] = df_producto['minutos_entrega'].mean()
        productos_list.append(dict_producto)

    # Se pasa la lista de diccionarios a DataFrame para ordenar y obtener el top_n.
    df_productos = pd.DataFrame(productos_list)
    top_productos = df_productos.sort_values(by=['cantidad'], ascending=False).head(top_n)
    return top_productos

def generar_informe(ruta_base):
    '''Genera un informe con los top 5 productos más vendidos, considerando solo los pedidos entregados y
    Guarda el DataFrame resultante en un archivo CSV en "salida/top_productos.csv", siendo salida un 
    directorio dentro de ruta_base.
    '''
    df = cargar_pedidos(ruta_base)
    df_con_minutos = agregar_minutos_entrega(df)
    top_5 = top_productos(df_con_minutos, top_n=5, solo_entregados=True)
    
    # Imprime el informe con el top 5"
    print("Top 5 productos más vendidos:")
    print(top_5)

    # Guarda el DataFrame con los minutos de entrega en un nuevo archivo CSV.
    if not os.path.exists(os.path.join(ruta_base, 'salida')):
        os.makedirs(os.path.join(ruta_base, 'salida'))
    df.to_csv(os.path.join(ruta_base, 'salida/top_productos.csv'), index=False)
    print(f"Archivo 'top_productos.csv' guardado en la carpeta 'salida'.")