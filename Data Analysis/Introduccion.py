import pandas as pd

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

#print(df_nations)

#Imprime los primeros 5 registros
print(df_nations.head())
#Imprime los ultimos 5 registros
print(df_nations.tail())
#En ambos casos si le pasas como parametro un numero, es el numero de registros que se mostraran en pantalla

#Muestra una columna que le solicites
print(df_nations["country"])
#Muestra distintas columnas de igual forma
print(df_nations[["country", "region"]])

#Agregar una columna con el tipo de cambio a pesos mexicanos de la columna gdp que esta en dolares  1usd = 20 pesos mexicanos
df_nations['tipo_de_cambio'] = round(df_nations["gdp"] * 20, 2)

print(df_nations.head())