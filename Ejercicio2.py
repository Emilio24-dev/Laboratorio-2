import pandas as pd
import matplotlib.pyplot as plt

#importamos el dataset
df = pd.read_csv('anime.csv') 

#Definimos el rango de datos
top_anime = df.head(5)

#Definimos los campos que queremos mostrar
plt.plot(top_anime['name'], top_anime['members'], marker='o', linestyle='-', color='b')

plt.xlabel('Animes')
plt.ylabel('Usuarios')
plt.title('Los 5 animes con más audiencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Muestra un grafico con respecto a la cantidad de audiencia que tiene cada anime, vemos que el resultado varia 
