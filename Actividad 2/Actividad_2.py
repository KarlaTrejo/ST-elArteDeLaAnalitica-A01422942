""" 
Actividad 2: Obtención de estadísticas descriptivas
Karla Yazmín Trejo Pichardo A01422942

Código que realizá la obtención de un conjunto de estadísticas descriptivas
de dos columnas del dataset seleccionado.

Por facilidad en el manejo de los datos y el cálculo de algunos valores relacionados a la estadistica, 
se hará uso de la librería "pandas" y sus funciones que facilitan el proceso de analisis.
"""

file = './Car accidents/data.csv' # Ruta donde esta el dataset

import pandas as pd # Se importa la lbreria de pandas

########################
# CARGAR LOS DATOS
########################
df = pd.read_csv(file) # Se lee el archivo usando una función de la libreria de pandas

CantRenYCol = df.shape # tupla con número de renglones (número de registros) y número de columnas (número de variables)
NombresCol = df.columns # lista con nombres de las columnas.
TiposCol = df.dtypes # tipos de datos de cada columna.

df.dropna(axis = 0, how = 'any', inplace = True) 

CantRenYColPuro = df.shape # tupla con número de renglones (número de registros) y número de columnas (número de variables) depurado

# Se reestablece el valor del data frame al que estaba sin depurar.
df = pd.read_csv(file)

print('**********************************','\nDatos generales acerca de la tabla\n**********************************\n')
print('Cantidad de registros y variables sin depurar "(Con renglones con NaN)"')
print(CantRenYCol, '\n') 
print('Cantidad de registros y variables depurarada "(Sin renglones con NaN en cualquiera de las columnas, pero no en todos)"')
print(CantRenYColPuro, '\n')
print(NombresCol, '\n')
print(TiposCol, '\n') 

print('***************************************','\nValores observables y calculados de columnas\n***************************************\n')
# Columnas que se revisarán: Severity y Weather_Condition.
# Valores estadisticos de la columna Severity
columna = df["Severity"]       
print("Columna 'Severity'\nValores unicos\n", columna.unique())      # valores únicos de la columna Severity.
print("Máximo\n", columna.max())         # valor máximo
print("Mínimo\n", columna.min())         # valor mínimo
print("Promedio\n", columna.mean())        # promedio
print("Mediana\n", columna.median())      # mediana (valor que se encuentra al centro de la lista ordenada de valores)
print("Desviación estándar\n", columna.std(), "\n")         # desviación estándar, qué tan dispersos están los datos alrededor de la media

# Valores estadisticos de la columna Temperature(F) 
columna = df["Temperature(F)"] 
print("\nColumna 'Temperature(F) '\nValores unicos\n", columna.unique())      # valores únicos de la columna Severity.
print("Máximo\n", columna.max())         # valor máximo
print("Mínimo\n", columna.min())         # valor mínimo
print("Promedio\n", columna.mean())        # promedio
print("Mediana\n", columna.median())      # mediana (valor que se encuentra al centro de la lista ordenada de valores)
print("Desviación estándar\n", columna.std())         # desviación estándar, qué tan dispersos están los datos alrededor de la media
