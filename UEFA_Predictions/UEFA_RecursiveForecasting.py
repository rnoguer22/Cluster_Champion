import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor

from Spark.spark import Spark



class RecursiveForecasting(Spark):

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(self.data_path, encoding='utf-8')
        self.df.drop(['Squad', 'id'], inplace=True, axis=1)
        self.df = self.df.iloc[:, :-2]


    def make_predictions(self, prediction_data_path, classifier):
        X = self.df.iloc[:, 1:].values
        y = self.df.iloc[:, 0].values

        prediction_data = pd.read_csv(prediction_data_path, encoding='utf-8')
        teams = prediction_data['Squad'].values
        copy_players = prediction_data[['id', 'Squad', 'Top Team Scorer', 'Goalkeeper']]
        prediction_data.drop(['Squad', 'id'], inplace=True, axis=1)
        prediction_data = prediction_data.iloc[:, :-2]
        X_pred = prediction_data.iloc[:, 1:]

        classifier = classifier.lower()
        if classifier == 'randomforest':
            clf = RandomForestClassifier(n_estimators=100, criterion='entropy')
        elif classifier == 'gradientboosting':
            clf = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0, loss='squared_error')
        clf.fit(X, y)
        y_pred = clf.predict(X_pred)
        prediction_dict = self.player_performance(copy_players, dict(zip(teams, y_pred)))
        sorted_prediction = self.convert(prediction_dict)
        prediction_df = pd.DataFrame({'Squad':sorted_prediction.keys(), 'Prediction':sorted_prediction.values()})
        prediction_df.to_csv(f'./UEFA_Predictions/csv/{classifier}_Predictions.csv', index=False)


    #Metodo para hacer predicciones a cada jugador, y posteriormente añadirlo a los coeficientes de prediccion del equipo
    def player_performance(self, df_players, pred_dict):
        df_pred_players = super().predict_player('./Web_Scrapping/Players_csv/goleadores.csv')
        df_pred_gks = super().predict_player('./Web_Scrapping/Players_csv/porteros.csv')
        for team in pred_dict.keys():
            
            #Obtenemos el coeficiente para cada goleador y lo añadimos a la prediccion del equipo
            for jugador in df_pred_players['Jugadores']:
                players = df_players.loc[df_players['Squad'] == team]
                scorer = players['Top Team Scorer'].iloc[-1][:-1]
                for player in scorer.split(','):
                    player = player.replace('...', '')
                    if player == jugador:
                        coef_player = df_pred_players.loc[df_pred_players['Jugadores'] == jugador, 'pred'].iloc[0]
                        pred_dict[team] += coef_player

            #Obtenemos el coeficiente para cada portero y lo añadimos a la prediccion del equipo
            for goalkeeper in df_pred_gks['Jugadores']:
                gk = df_players['Goalkeeper'].loc[df_players['Squad'] == team].iloc[0]
                if gk == goalkeeper:
                    coef_gk = df_pred_gks.loc[df_pred_gks['Jugadores'] == gk, 'pred'].iloc[0]
                    pred_dict[team] += coef_gk

        return pred_dict



    #Metodo para convertir el numero de standing a la ronda de la champions
    def convert(self, dictionary):
        semifinalists_dict = dict(zip(list(dictionary.keys())[:4], list(dictionary.values())[:4]))
        defeated_dict = dict(zip(list(dictionary.keys())[4:], list(dictionary.values())[4:]))
        #Ordenamos los diccionarios de manera descendente
        semifinalists_ordered_dict = dict(sorted(semifinalists_dict.items(), key=lambda x: x[1], reverse=True))
        defeated_ordered_dict = dict(sorted(defeated_dict.items(), key=lambda x: x[1], reverse=True))
        final_dict = {}

        count_semi = 0
        for key, value in semifinalists_ordered_dict.items():
            if count_semi < 32 - len(defeated_ordered_dict):
                if count_semi == 0:
                    final_dict[key] = 'W'
                elif count_semi == 1:
                    final_dict[key] = 'F'
                elif count_semi <= 3:
                    final_dict[key] = 'SF'
                count_semi += 1

        count_defeated = 0
        for key, value in defeated_ordered_dict.items():
            if count_defeated < 32 - len(semifinalists_ordered_dict):
                if count_defeated <= 3:
                    final_dict[key] = 'QF'
                elif 3 < count_defeated <= 11:
                    final_dict[key] = 'R16'
                else:
                    final_dict[key] = 'GR'
                count_defeated += 1
                
        return final_dict