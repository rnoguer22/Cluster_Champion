import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de entrada (X) y resultados (y)
X_train = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # reshape necesario para convertir X en una matriz 2D
y_train = np.array([2, 4, 6, 8, 10])

# Crear y ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir para nuevos valores de X
X_test = np.array([6, 7]).reshape(-1, 1)  # Nuevos valores de X
y_pred = model.predict(X_test)

# Imprimir las predicciones
print("Predicciones:", y_pred)