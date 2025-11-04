class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
    
class FormatoTablaTXT(FormatoTabla):
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    def encabezado(self, headers):
        print('<tr>')
        for h in headers:
            print(f'  <th>{h}</th>')
        print('</tr>')

    def fila(self, data_fila):
        print('<tr>')
        for d in data_fila:
            print(f'  <td>{d}</td>')
        print('</tr>')

def crear_formateador(nombre):
    if nombre == 'txt':
        return FormatoTablaTXT()
    elif nombre == 'csv':
        return FormatoTablaCSV()
    elif nombre == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Formato desconocido {nombre}')
    
def imprimir_tabla(data, headers, formateador):
    formateador.encabezado(headers)
    for obj in data:
        row_data = []
        
        for colname in headers:
            value = getattr(obj, colname)
            row_data.append(str(value))
        formateador.fila(row_data)