import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('gym.csv')

#Definimos la longitud de nuestro grafico
ejercicios = df['Workout_Type'].value_counts()

# Crear el gráfico circular
plt.figure(figsize=(10, 6))
plt.pie(ejercicios, labels=ejercicios.index, autopct='%1.1f%%', startangle=140)
plt.title('Ejercicios')
plt.axis('equal') #Aca definimos el tipo de grafico, en este caso circular
plt.show()

#Muestra en un grafico circular según los ejercicios más usados en el gimnasio
