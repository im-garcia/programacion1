import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # <- faltaba esto

idx = pd.date_range('20200923 14:00', periods=120, freq='min')
s1 = pd.Series(np.random.randint(-1, 2, 120), index=idx)
s2 = s1.cumsum()

# Primer gráfico: caminata aleatoria
s2.plot()

# Agregamos plt.show() para que se muestre
plt.title("Caminata aleatoria")
plt.show()

# Segundo gráfico: media móvil
w = 5
s3 = s2.rolling(w, min_periods=1).mean()
s3.plot()
plt.title("Media móvil (ventana de 5 minutos)")
plt.show()

# Tercer gráfico: ambas juntas
df_series_23 = pd.DataFrame([s2, s3]).T
df_series_23.plot()
plt.title("Caminata y su media móvil")
plt.show()

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()
plt.show()

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
plt.show()
df_walk_suav.to_csv('caminata_apostolica.csv')