from pyspark.sql import SparkSession


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
            df = self.spark.read.csv(path, header=True, encoding='utf-8')
            return df
    
    def schema(self, df):
        df.printSchema()

    def show(self, df):
        df.show()
    
    def create_temp_view(self, df, name):
        df.createOrReplaceTempView(name)
    
    def sql_query(self, query):
        return self.spark.sql(query).show()

    #Metodo para hacer una regresion lineal de los datos utilizando machine learning de spark
    def mlregression(self):
        pass
    


spark = Spark()
df = spark.read_file('./UEFA_Predictions/csv/arima_Predictions.csv')
print('\n\n\n')
spark.schema(df)
spark.show(df)
spark.create_temp_view(df, 'arima')
query = 'SELECT * FROM arima WHERE Prediction = "F"'
result = spark.sql_query(query)
print('\n\n\n')
spark.stop()