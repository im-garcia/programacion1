# Ignacio Miguel García, DNI: 42469590

import numpy as np
import matplotlib.pyplot as plt

def generar_array(N, distribution):
    '''
    Genera un array de NumPy de tamaño N y de distribución normal, uniforme o 
    poisson según el string que se le pase a la función por el argumento distribution
    '''
    if distribution == "gaussian":
        array = np.random.normal(loc=0.0, scale=1, size=N)
    elif distribution == "uniform":
        array = np.random.uniform(low=0, high=10,size=N)
    elif distribution == "poisson":
        array = np.random.poisson(lam=1, size=N)
    else:
        return None
    
    return array

def plot_histograma(array):
    '''
    Recibe un array de NumPy y plotea un histograma del array de bins: 'auto'.
    '''
    # Busqué si había una forma óptima de elegir la cantidad de bins, 
    # y encontré en los docs de matplotlib que se le puede pasar un string a bins que puede ser una de las estrategias
    # soportadas por numpy.histogram_bin_edges: 'auto', 'fd', etc. Dejo los links de donde lo saqué:
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
    # https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges
    plt.hist(array, bins='auto') 
    
    plt.title('Histograma del array')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show()