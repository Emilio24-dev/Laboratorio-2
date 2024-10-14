import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('anime.csv') 

top_food = df.head(5)

plt.plot(top_food['name'], top_food['members'], marker='o', linestyle='-', color='b')

plt.xlabel('Animes')
plt.ylabel('Usuarios')
plt.title('Los 5 animes con más audiencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
