from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

from UEFA_Predictions.UEFA_RecursiveForecasting import RecursiveForecasting



class Spark(RecursiveForecasting):

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
        df_coef_gks = self.predict_player('./Web_Scrapping/Players_csv/porteros.csv')
        return equipos, df_coef_players, df_coef_gks
    

    #Metodo para predecir el standing de los equipos en la champions
    def predict(self, df, teams, df_coef_players, df_coef_gks):
        predictions = {}
        for team in teams:
            #startswith solo acepta 3 argumentos como maximo por lo que lo hacemos uno a uno
            if team.startswith('Real Madrid') or team.startswith('Bayern Munich') or team.startswith('Paris S-G') or team.startswith('Dortmund'):
                filtered_df = df.filter(col('Squad').like('%'+team+'%'))
                pandas_df = filtered_df.toPandas()
                #De esta manera nos aseguramos que el dataframe no este vacio
                if pandas_df.shape[0] == 0:
                    data = pd.read_csv('./UEFA_Analisis_CSV/UEFA_Target.csv')
                    pandas_df = data[data['Squad'].str.contains(team)]
                predictions[f'{team} 2023-2024'] = self.linear_regression(pandas_df, 'Rk', df_coef_players, df_coef_gks)
        df_defeated = pd.read_csv('./UEFA_Analisis_CSV/UEFA_Target.csv', skiprows=5, header=None)
        defeated_dict = {equipo: '' for equipo in df_defeated[2]}
        predictions.update(defeated_dict)
        converted_pred = self.convert(predictions)
        df_predictions = pd.DataFrame(list(converted_pred.items()), columns=['Squad', 'Prediction'])
        df_predictions.to_csv('./UEFA_Predictions/csv/LinearRegression_Predictions.csv', index=False)
        return df_predictions


    #Metodo para aplicar una regresion lineal sobre el metodo predict
    def linear_regression(self, df, target, df_coef_players, df_coef_gks):
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
        
        #Añadimos un pequeño coeficiente según el desempeño del portero de cada equipo en las champions anteriores
        for jugador in df_coef_gks['Jugadores']:
            gk = df['Goalkeeper'].iloc[-1]
            if gk == jugador:
                coef_gk = df_coef_gks.loc[df_coef_gks['Jugadores'] == gk, 'pred'].iloc[0]
                y_pred[0] += coef_gk

        return y_pred[0]
    

    #Metodo para convertir el numero de standing a la ronda de la champions
    def convert(self, dictionary):
        return super().convert(dictionary)
    

    #Metodo para calcular un coeficiente para cada jugador, y posteriormente añadirlo a los coeficientes de regresion del equipo
    def predict_player(self, path):  
        return super().predict_player(path)