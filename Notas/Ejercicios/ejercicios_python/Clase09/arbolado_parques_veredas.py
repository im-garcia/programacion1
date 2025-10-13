import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][['altura_tot', 'diametro', 'nombre_cie']].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']].copy()

df_tipas_parques = df_tipas_parques.rename(columns={
    'altura_tot': 'altura',
    'nombre_cie': 'nombre_cientifico'
})

df_tipas_veredas = df_tipas_veredas.rename(columns={
    'altura_arbol': 'altura',
    'diametro_altura_pecho': 'diametro'
})

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

df_tipas = pd.concat([df_tipas_parques, df_tipas_veredas])

df_tipas.boxplot(column='diametro', by='ambiente')
plt.title('Diámetro a la altura del pecho')
plt.ylabel('cm')
plt.show()

df_tipas.boxplot(column='altura', by='ambiente')
plt.title('Altura total')
plt.ylabel('m')
plt.show()