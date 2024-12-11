"""
3.- cuantos datos tenemos en cada region
"""
import pandas as pd
import numpy as np

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

#Metodo where
df_nations["co2_recodificada"] = np.where(df_nations['co2']>df_nations['co2'].mean(), 1, 0)
print(df_nations["co2_recodificada"].head())
print(df_nations["co2_recodificada"].value_counts())
paises = df_nations.loc[df_nations["co2_recodificada"] == 1, "country"].tolist()
print(paises)