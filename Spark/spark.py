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
    

    #Metodo para obtener una lista con los equipos de la champions, y el coeficiente de cada jugador
    def get_teams(self, df, col_name):
        teams = df.select(col_name).distinct().collect()
        lista_equipos = [row[col_name][:-10] for row in teams]
        equipos = list(set(lista_equipos))
        df_coef_players = self.predict_player('./Web_Scrapping/Players_csv/goleadores.csv')
        return equipos, df_coef_players
    

    #Metodo para predecir el standing de los equipos en la champions
    def predict(self, df, teams, df_coef_players):
        predictions = {}
        for team in teams:
            filtered_df = df.filter(col('Squad').like('%'+team+'%'))
            pandas_df = filtered_df.toPandas()
            #De esta manera nos aseguramos que el dataframe no este vacio
            if pandas_df.shape[0] == 0:
                data = pd.read_csv('./UEFA_Analisis_CSV/UEFA_Target.csv')
                pandas_df = data[data['Squad'].str.contains(team)]
            predictions[team] = self.linear_regression(pandas_df, 'Rk', df_coef_players)
        print(predictions)
        converted_pred = self.convert(predictions)
        df_predictions = pd.DataFrame(list(converted_pred.items()), columns=['Squad', 'Rk'])
        df_predictions.to_csv('./UEFA_Predictions/csv/LinearRegression_Predictions.csv', index=False)
        return df_predictions


    #Metodo para aplicar una regresion lineal sobre el metodo predict
    def linear_regression(self, df, target, df_coef_players):
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

        #Añadimos un pequeño coeficiente según el desempeño del goleador de cada equipo en las champions anteriores
        for jugador in df_coef_players['Jugadores']:
            players = df['Top Team Scorer'].iloc[-1][:-1]
            for player in players.split(','):
                player = player.replace('...', '')
                if player == jugador:
                    coef_player = df_coef_players.loc[df_coef_players['Jugadores'] == jugador, 'pred'].iloc[0]
                    y_pred[0] += coef_player
        return y_pred[0]
    

    #Metodo para convertir el numero de standing a la ronda de la champions
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
    

    #Metodo para calcular un coeficiente para cada jugador, y posteriormente añadirlo a los coeficientes de regresion del equipo
    def predict_player(self, path):  
        df = pd.read_csv(path)
        type_ = path.split('/')[-1][:-4]

        if type_ == 'goleadores':
            ga = df['GA'] / 10
            gc = (10 - df['G/C']) / 10
            df['pred'] = (ga + gc)/2
        
        #elif type_ == 'porteros':
        
        return df[['Jugadores', 'pred']]



print('\n ---------Linear Regression with PySpark---------')
print('Launching PySpark...')
spark = Spark()
df = spark.read_file('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
df_target = spark.read_file('./UEFA_Analisis_CSV/UEFA_Target.csv')
teams, df_coef_players = spark.get_teams(df_target, 'Squad')
spark.predict(df, teams, df_coef_players)
spark.stop()