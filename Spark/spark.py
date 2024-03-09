from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



class Spark:

    def __init__(self):
        # Iniciamos una sesión de Spark, esto se hace siempre que se quiera trabajar con Spark
        self.spark = SparkSession.builder \
            .appName("Analisis_Champions_Spark") \
            .config("spark.hadoop.fs.hdfs.impl", "org.apache.hadoop.hdfs.DistributedFileSystem") \
            .config("spark.hadoop.mapreduce.framework.name", "local") \
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
    
    def save_team(self, df, teams):
        for team in teams:
            filtered_df = df.filter(col('Squad').like('%'+team+'%'))
            output_dir = './UEFA_Analisis_CSV/Equipos/'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                print("Carpeta creada exitosamente en: ", output_dir)
            pandas_df = filtered_df.toPandas()
            print(team, ': ', self.linear_regression(pandas_df, 'Rk'))

    def linear_regression(self, df, target):
        rows = df.shape[0]
        #Variable dependiente
        X = list(range(1, rows+1))
        try:
            prediction = max(X) + 1
        except:
            prediction = 1
        #Variable objetivo
        y = list(map(int, df[target]))

        X_train = np.array(X).reshape(-1, 1)
        y_train = np.array(y)
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predecir para nuevos valores de X
        X_test = np.array([prediction]).reshape(-1, 1)  # Nuevos valores de X
        y_pred = model.predict(X_test)

        return y_pred
    

print('Ejecutando...')
spark = Spark()
df = spark.read_file('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
df_target = spark.read_file('./UEFA_Analisis_CSV/UEFA_Target.csv')

spark.save_team(df, spark.get_teams(df_target, 'Squad'))
print('\n\n\n')

spark.stop()