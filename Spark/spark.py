from pyspark.sql import SparkSession


# Iniciamos una sesión de Spark, esto se hace siempre que se quiera trabajar con Spark
spark = SparkSession.builder \
    .appName("Analisis_Champions_Spark") \
    .getOrCreate()

df = spark.read.csv('UEFA_Analisis_CSV/UEFA_Final_Data.csv', encoding='utf-8')

df.show()

spark.stop()