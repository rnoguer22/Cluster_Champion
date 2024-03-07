from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring



class Spark:

    def __init__(self):
        # Iniciamos una sesión de Spark, esto se hace siempre que se quiera trabajar con Spark
        self.spark = SparkSession.builder \
            .appName("Analisis_Champions_Spark") \
            .getOrCreate()
        
    def stop(self):
        self.spark.stop()
        
    def read_file(self, path):
        if path[-3:] == 'csv':
            # Leemos el archivo csv
            self.df = self.spark.read.csv(path, header=True, encoding='utf-8')
            return self.df
    
    def create_temp_view(self, df, name):
        df.createOrReplaceTempView(name)
    
    def sql_query(self, query):
        return self.spark.sql(query).show()
    
    #Metodo para obtener una lista con los equipos de la champions
    def get_teams(self, df, col_name):
        teams = df.select(col_name).distinct().collect()
        lista_equipos = [row[col_name][:-10] for row in teams]
        return list(set(lista_equipos))

    #Metodo para hacer una regresion lineal de los datos utilizando machine learning de spark
    def mlregression(self):
        pass
    

print('Ejecutando...')
spark = Spark()
df = spark.read_file('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
print('\n\n\n')
spark.df.printSchema()
print('\n')
print(spark.get_teams(df, 'Squad'))
print('\n\n\n')

spark.stop()