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
    

    def predict(self, df, teams):
        predictions = {}
        for team in teams:
            filtered_df = df.filter(col('Squad').like('%'+team+'%'))
            pandas_df = filtered_df.toPandas()
            #De esta manera nos aseguramos que el dataframe no este vacio
            if pandas_df.shape[0] == 0:
                data = pd.read_csv('./UEFA_Analisis_CSV/UEFA_Target.csv')
                pandas_df = data[data['Squad'].str.contains(team)]
            predictions[team] = self.linear_regression(pandas_df, 'Rk')
        converted_pred = self.convert(predictions)
        df_predictions = pd.DataFrame(list(converted_pred.items()), columns=['Squad', 'Rk'])
        df_predictions.to_csv('./UEFA_Predictions/csv/LinearRegression_Predictions.csv', index=False)
        return df_predictions


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
        #Predecimos para nuevos valores de X
        X_test = np.array([prediction]).reshape(-1, 1)
        y_pred = model.predict(X_test)
        return y_pred[0]
    

    def convert(self, dictionary):
        #Ordenamos el diccionario de manera descendente
        ordered_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        final_dict = {}
        count = 0
        for key, value in ordered_dict.items():
            if count < 32:
                if count == 0:
                    final_dict[key] = 'W'
                elif count == 1:
                    final_dict[key] = 'F'
                elif count <= 3:
                    final_dict[key] = 'SF'
                elif count <= 7:
                    final_dict[key] = 'QF'
                elif count <= 15:
                    final_dict[key] = 'R16'
                else:
                    final_dict[key] = 'GR'
                count += 1
        return final_dict
        
    

print('Ejecutando...')
spark = Spark()
df = spark.read_file('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
df_target = spark.read_file('./UEFA_Analisis_CSV/UEFA_Target.csv')
teams = spark.get_teams(df_target, 'Squad')
prediction = spark.predict(df, teams)

print('\n\n\n')

spark.stop()