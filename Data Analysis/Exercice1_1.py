"""
1.- cuantos tipos de atributos nos encontramos en el dataset
2.- cuantos datos tenemos en cada region
"""
import pandas as pd

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

#Una tabla de frecuencia
t_frecuencia = df_nations["region"].value_counts()
print(t_frecuencia)

#Tabla de agrupacion
t_agrupacion = df_nations.groupby(["region"])[["country"]].count()
print(t_agrupacion)

