import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

df_europa = df_nations[df_nations['region'] == 'Europe']
df_afr = df_nations[df_nations['region'] == 'Africa']
#Valor promedio de mortalidad infantil en europa y africa
m_euro = df_europa["chldmort"].mean()
m_afr = df_afr["chldmort"].mean()

#Graficamos
# sns.barplot(x =["Europa", "Africa"], y = [m_euro, m_afr])
# plt.show()

#grafico de barras alfabetismo promedio entre Americas y el resto del mundo
df_ame = df_nations[df_nations['region'] == 'Americas']
m_americas = df_ame["literacy"].mean()
#Excluimos americas para hacer una comparativa de americas vs el resto del mundo
m_exclude_ame = df_nations[df_nations['region'] != 'Americas']["literacy"].mean()
#Graficamos
sns.barplot(x =["Americas", "Mundial"], y = [m_americas, m_exclude_ame])
plt.show()