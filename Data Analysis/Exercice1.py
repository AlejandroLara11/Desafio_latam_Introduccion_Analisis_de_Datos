"""
1.- cuantos tipos de atributos nos encontramos en el dataset
2.- cuantos datos tenemos en cada region
3.- cuantos paises tienen indices de CO_2 mayores que el promedio
4.- que se puede decir del alfabetismo en africa o europa
"""
import pandas as pd

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1", index_col=0)

#1
print(df_nations.info())
#Nos muestra 3 tipos de atributos

#2
print(df_nations["region"].describe())
#regiones guarda una lista de los valores posibles que toma la columna "region"
regiones = df_nations["region"].unique().tolist()
print(regiones)
#tenemos 5 tipos de datos en su mayoria africa

#3
#Calculamos el promedio de co2 para una posterior comparacion
co2_mean = df_nations["co2"].mean()
print(co2_mean)
#realizamos un filtro para obtener los registros en los que co2 sea mayor que el promedio
paises_mayor_co2 = df_nations[df_nations["co2"]>co2_mean]
print(paises_mayor_co2)
#contamos cuantos paises aparecen despues del filtro sin ser paises repetidos
cantidad_paises = paises_mayor_co2["country"].nunique()
print(cantidad_paises)
#mostramos la columna de paises sin repeticiones en la que el co2 es mayor que el promedio
print(paises_mayor_co2["country"].unique().tolist())


#4
#Primero un promedio mundial para realizar una estimacion
promedio_mundial = df_nations['school'].mean()
#Aqui se filtran en dos datasets distintos, uno para africa y otro para europa
df_africa = df_nations[df_nations['region'] == 'Africa']
df_europe = df_nations[df_nations['region'] == 'Europe']
#Calculamos el promedio de educacion en ambos continentes
promedio_africa = df_africa['school'].mean()
promedio_europe = df_europe['school'].mean()

#imprimimos los promedios para calcular
print("Promedio de escolaridad mundial:", promedio_mundial)
print("Promedio de escolaridad en África:", promedio_africa)
print("Promedio de escolaridad en Europa:", promedio_europe)

#Por ultimo se puede ver que el promedio de africa esta tres puntos por debajo de la media y el de europa 3 puntos por arriba de la media, esto solo como un analisis muy simple, existen muchos factores mas a tomar en cuenta para un mejor analisis.