import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('UEFA_Analisis_CSV/UEFA_Final_Data.csv')

# Convertir la variable categórica a numérica
df['Top Team Scorer'] = df['Top Team Scorer'].str.split('-').str[0]

# Cambiar el tipo de dato de algunas variables
df['Rk'] = df['Rk'].astype('int')
df['MP'] = df['MP'].astype('int')
df['W'] = df['W'].astype('int')
df['D'] = df['D'].astype('int')
df['L'] = df['L'].astype('int')
df['GF'] = df['GF'].astype('int')
df['GA'] = df['GA'].astype('int')
df['Pts'] = df['Pts'].astype('int')

# Seleccionar variables para el modelo
features = ['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Attendance']

# Separar variables independientes y dependientes
X = df[features]
y = df['Rk']

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Ajustar el modelo
model = sm.OLS(y_train, X_train).fit()

# Resumen del modelo
print(model.summary())

# Coeficiente de determinación (R^2)
r2 = r2_score(y_test, model.predict(X_test))

# Error cuadrático medio (MSE)
mse = mean_squared_error(y_test, model.predict(X_test))

# Imprimir resultados
print(f'R^2: {r2:.4f}')
print(f'MSE: {mse:.4f}')

print('\n\n\n')

#66,4,Real Madrid 2012-2013,12.0,5.0,4.0,3.0,26.0,18.0,8.0,19.0,71.313,Cristiano Ronaldo-,Diego López

# Predicción para un nuevo equipo
new_team = pd.DataFrame({
    'MP': [12.0],
    'W': [5.0],
    'D': [4.0],
    'L': [3.0],
    'GF': [26],
    'GA': [40],
    'GD': [8],
    'Pts': [19],
    'Attendance': [71.000],
    })

prediction = model.predict(new_team)

print(f'Predicción para el nuevo equipo: {prediction[0]}')

