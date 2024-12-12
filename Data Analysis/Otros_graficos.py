import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

# BOXPLOT
# # Esta version marca una recomendacion
sns.boxplot(x = df_nations["region"], y = df_nations["school"], palette='dark')
plt.show()


# # por eso utilizaremos esta
sns.boxplot(y = df_nations["school"], hue=df_nations["region"], palette='dark', gap = 0.1, legend=False)
plt.xlabel("region")
plt.ylabel("school")
plt.show()

# #DISPERSION
#tenemos que limpiar los datos para un mejor resultado y analisis
df_limpia = df_nations.dropna()
print(df_limpia.head())
sns.scatterplot(data = df_limpia, x = df_limpia['school'], y = df_limpia["literacy"])
plt.show()

#MAPA DE CALOR (HEATMAP)
#Trabajamos unicamente con valores numericos
df_numeric_nations = df_nations.select_dtypes(include=("int64", "float64"))
corr = df_numeric_nations.corr()
#1 es una correlacion perfecta POSITIVA y -1 es una correlacion perfecta NEGATIVA
plt.rcParams["figure.figsize"] = (7, 7)
sns.heatmap(corr, cmap='Greens', annot=True)
plt.show()