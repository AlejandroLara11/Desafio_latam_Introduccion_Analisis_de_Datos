import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

sns.displot(df_nations["gini"], kind = "hist")
plt.axvline(df_nations["gini"].mean(), color = "tomato")
plt.show()
