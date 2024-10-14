import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('gym.csv')

# Contar la cantidad de cada tipo de workout
alimentos = df['Workout_Type'].value_counts()

# Crear el gráfico circular
plt.figure(figsize=(10, 6))
plt.pie(alimentos, labels=alimentos.index, autopct='%1.1f%%', startangle=140)
plt.title('Alimentos')
plt.axis('equal')  # Para que el gráfico sea un círculo
plt.show()