import pandas as pd
import matplotlib.pyplot as plt
# Caleb Dorado NC = 0039
# 1. Leer el archivo CSV comida pais India
df_food_india = pd.read_csv('indian_food.csv')
print("\n DATOS LEIDOS DESDE CSV, comida India 0039 ")
print(df_food_india)

print("\n Mostrar Nombre + ingredientes de comida 0039 ")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)

print("\n Tiempo de Cocinado mostrar 10 registros con head 0039 ")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)

print("\n Grafica comida (X) Tiempo de Cocinado (Y) 0039 ")
print("\n Grafica comida (X) Texto a 30 grados 0039 ")
nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title('Comida tipica de India Caleb 0039')
plt.xlabel('Nombre de Platillo')
plt.ylabel('Tiempo de Cocinado')
plt.show()

print("\n Grafica multiple 0039 ")
nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora.plot.bar(x='name', rot=30)
plt.title('Grafica de 2 columnas Caleb 0039')
plt.xlabel('Nombre de Platillo')
plt.ylabel('Tiempo de Cocinado prep y comida')
plt.show()

print("\n Graficas apiladas una tras otra verticalmente 0039 ")
nombre_y_hora.plot.bar(x='name', stacked=True, rot=30)
plt.title('Graficas apiladas Caleb 0039')
plt.xlabel('Nombre de Platillo')
plt.ylabel('Tiempo de Cocinado prep y comida')
plt.show()
