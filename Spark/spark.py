from pyspark.sql import SparkSession


# Iniciamos una sesión de Spark, esto se hace siempre que se quiera trabajar con Spark
spark = SparkSession.builder \
    .appName("Analisis_Champions_Spark") \
    .getOrCreate()

df = spark.read.csv('./UEFA_Predictions/csv/arima_Predictions.csv', header=True, encoding='utf-8')

df.printSchema()

df.show()

#Creamos una vista temporal para poder hacer consultas SQL
df.createOrReplaceTempView("datos")

spark.sql("SELECT * FROM datos WHERE Prediction='F'").show()

spark.stop()