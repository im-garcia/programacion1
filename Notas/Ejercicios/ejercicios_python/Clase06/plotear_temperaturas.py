import numpy as np

def plotear_temperaturas():
    temps = np.load('../Data/temperaturas.npy')
    import matplotlib.pyplot as plt
    plt.hist(temps,bins=37)
    plt.show()