#4.- que se puede decir del alfabetismo en africa o europa

import pandas as pd
import numpy as np

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

df_euro = df_nations[df_nations["region"] == "Europe"]
print(df_euro.head())
df_afr = df_nations[df_nations["region"] == "Africa"]
print(df_afr.head())

print(f'La tasa de alfabetismo en europa es de: {df_euro["literacy"].mean()}')

print(f'Mientras que la tasa de alfabetismo en Africa esta en: {df_afr["literacy"].mean()}')