from datetime import datetime

def vida_en_segundos(fecha_nac):
    """
    Calcula la cantidad de segundos vividos desde la fecha de nacimiento hasta ahora.
    
    Pre: Fecha en formato 'dd/mm/AAAA'
        
    Pos: Cantidad de segundos vividos
    """
    if len(fecha_nac.split('/')[-1]) == 4:
        formato = '%d/%m/%Y'
    else:        
        formato = '%d/%m/%y'

    fecha_nac = datetime.strptime(fecha_nac, formato)
    ahora = datetime.now()
    segundos_vivo = ahora - fecha_nac
    return segundos_vivo.total_seconds()

