import pandas as pd
import matplotlib.pyplot as plt

#Importamos el dataset
df = pd.read_csv('balon.csv')

#Definimos el orden de nuestra gafica, en este caso será respecto a los goles de los jugadores
top_goleadores = df.sort_values(by='Performance-Gls', ascending=False).head(5)

#Definimos los campos que queremos mostrar 
x = top_goleadores.plot.bar(x='player', y=['Performance-Gls'], rot=45)

plt.title('Top 5 jugadores con más goles de la temporada pasada')
plt.xlabel('Jugador')
plt.ylabel('Cantidad')
plt.show()

#Esta grafica muestra de manera descendente, según los goles de los jugadores, en este caso de los primeros 5
