import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)
df_limpia = df_nations.dropna()
# print(df_limpia.head())

"""
#IMPLEMENTACION BASICA DE REGRESION LINEAL EN 3 PASOs
#CUAL ES LA RELACION ENTRE EMISIONES DE CO2 Y EL PIB(GOP) DE CADA PAIS
"""
#1: PLANTEAR EL MODELO CON SU FORMULA
modelo1 = smf.ols(' gdp ~ co2 ', df_limpia)

#2: AJUSTAR EL MODELO CON FIT
modelo1 = modelo1.fit()

#3: MOSTRAR RESULTADOS DEL MODELO
print(modelo1.summary())