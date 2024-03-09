from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vectors

# Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("LinearRegressionPrediction") \
    .getOrCreate()

# Datos de entrenamiento (los mismos que usamos antes)
data = [(1.0, Vectors.dense(1.0)),
        (2.0, Vectors.dense(2.0)),
        (3.0, Vectors.dense(3.0)),
        (4.0, Vectors.dense(4.0)),
        (5.0, Vectors.dense(5.0))]

# Crear un DataFrame a partir de los datos
df = spark.createDataFrame(data, ["label", "features"])

# Crear un ensamblador para concatenar las características en un solo vector
assembler = VectorAssembler(inputCols=["features"], outputCol="features_vector")
print('\n\n\n')
for i in assembler.getOutputCol():
    print(i)
print('\n\n\n')

# Aplicar el ensamblador al DataFrame
df_assembled = assembler.transform(df)

# Crear el modelo de regresión lineal y ajustarlo al DataFrame
lr = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(df_assembled)

# Crear un nuevo DataFrame con las características para las cuales deseamos hacer la predicción
new_data = [(6.0, Vectors.dense(6.0)),
            (7.0, Vectors.dense(7.0))]

new_df = spark.createDataFrame(new_data, ["label", "features"])

# Aplicar el ensamblador al nuevo DataFrame
new_df_assembled = assembler.transform(new_df)

# Utilizar el modelo para hacer predicciones sobre el nuevo DataFrame
predictions = lr_model.transform(new_df_assembled)

# Mostrar las predicciones
predictions.show()

# Cerrar la sesión de Spark
spark.stop()
