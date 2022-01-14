"""
Actividad Final
Karla Yazmín Trejo Pichardo A01422942

Código que recopila todo aquello que se realizo para el analisis de datos del conjunto de datos
mediante el uso de diversas herramientas estadisticas, ya sea descriptivas como visuales
"""




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







"""
Actividad 3: Mapas de calor y boxplots
Karla Yazmín Trejo Pichardo A01422942

Código con el que podremos ver visualmente de alguna o muchas variables el comportamiento de tienen los datos de los
registros, todo esto mediante el uso de histogramas, diagramas de caja y bigotes y mapas de calor.

Ademñas de la libreria de pandas, se hará uso de otras librerias como numpy para poder hacer facilmente con las
funciones de la libreria los elementos visuales a ocupar.
"""
# He decidido usar las mismas columnas de temperatura y severidad que se usaron anteriormente en la actividad 1.
import matplotlib.pyplot as plt # Importación de la libreria de matplotlib.pyplot
import numpy as np # Importación de la libreria de numpy
import seaborn as sns # importación de libreria de seaborn para el mapa de calor

#######################################################
# Elementos visuales para la columna de "Severity"
#######################################################
# Elementos necesarios para mostrar adecuadamente el histograma
bins = np.arange(0, df.Severity.max() + 1.5) - 0.5
bins = np.arange(0, 5 + 1.5) - 0.5
df.hist(column = "Severity", bins = bins, grid = False, color = "Orange")
plt.show()

# Elementos necesarios para mostrar adecuadamente el diagramas de caja y bigotes  
df.boxplot(column = ["Severity"], color = "Orange", showmeans = True )
plt.show()

#######################################################
# Elementos visuales para la columna de "Temperature(F)"
#######################################################
# Elementos necesarios para mostrar adecuadamente el histograma
df.hist(column = "Temperature(F)", grid = False, color = "Green")
plt.show()

# Elementos necesarios para mostrar adecuadamente el diagramas de caja y bigotes  
df.boxplot(column = ["Temperature(F)"], color = "Green", showmeans = True )
plt.show()

# Elementos necesarios para mostrar adecuadamente el diagramas de caja y bigotes  
df = df[df["Temperature(F)"]<50]
df.boxplot(column = ["Temperature(F)"], color = "Green", showmeans = True )
plt.show()

#######################################################
# Correlación y mapa de calor
#######################################################
df = pd.read_csv(file)
print(df.corr())   #Correlación de los elementos de la tabla
# Elementos necesarios para mostrar adecuadamente el mapa de calor 

#plt.figure(figsize=(100, 5))
sns.heatmap(df.corr(), annot=True, vmin=0, vmax=1, cmap="cividis");
plt.show()






"""
Actividad 4: Patrones con K-means
Karla Yazmín Trejo Pichardo A01422942

Código con el que podremos ver visualmente de alguna o muchas variables el comportamiento de tienen los datos 
de los registros, esto mediante el uso del algoritmo de K-means/k-medias.

Ademñas de la libreria de pandas, se hará uso de la liberia de matplotlib.pyplot para usar las funciones de la 
libreria que nos ayudan a facilitar el proceso del uso del algoritmo de  K-means y la visualización del mismo.
"""
# He decidido usar las mismas columnas de temperatura y severidad que se usaron anteriormente en la actividad 1
# principalmente para ver si puedo encontrar datos aún más interesantes sobre ellas.

from sklearn.cluster import KMeans

test = df[["Severity","Temperature(F)"]]
test = test.dropna(axis = 0, how = 'any')

kmeans = KMeans(n_clusters=2).fit(test)
centroids = kmeans.cluster_centers_
print(centroids)

# Predicciones (cuál es la clase) de acuerdo a los centros calculados

cla = kmeans.predict(test)                   # obtiene las clases de los datos iniciales

# Predicción para un nuevo dato
data = {"Severity": [3], "Temperature(F)": [20.5]}
newdf = pd.DataFrame(data)  
print(kmeans.predict(newdf))


plt.scatter(test["Severity"], test["Temperature(F)"],c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="*",c="red")
plt.scatter(3,20.5,marker="*",c="orange")
plt.show()
