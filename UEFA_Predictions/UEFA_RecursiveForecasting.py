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
        final_dict = {}
        semifinalists1_dict = {}
        semifinalists2_dict = {}

        #Emparejamos cada equipo de cada semifinal en un diccionario diferente
        for key, value in semifinalists_dict.items():
            if key.startswith('Real Madrid'):
                semifinalists1_dict[key] = value
            if key.startswith('Bayern Munich'):
                semifinalists1_dict[key] = value
            if key.startswith('Paris S-G'):
                semifinalists2_dict[key] = value
            if key.startswith('Dortmund'):
                semifinalists2_dict[key] = value
        
        #Emparejamos los equipos de las semifinales, y sacamos el ganador y el perdedor
        semifin1_winner = max(semifinalists1_dict.items(), key=lambda x: x[1])
        print(semifin1_winner)
        semifin1_looser = min(semifinalists1_dict.items(), key=lambda x: x[1])
        print(semifin1_looser)
        semifin2_winner = max(semifinalists2_dict.items(), key=lambda x: x[1])
        print(semifin2_winner)
        semifin2_looser = min(semifinalists2_dict.items(), key=lambda x: x[1])
        print(semifin2_looser)

        if semifin1_winner[1] > semifin2_winner[1]:
            final_dict[semifin1_winner[0]] = 'W'
            final_dict[semifin2_winner[0]] = 'F'
            print(semifin1_winner[0], ' ha ganado al ', semifin2_winner[0])
        else:
            final_dict[semifin2_winner[0]] = 'W'
            final_dict[semifin1_winner[0]] = 'F'
            print(semifin2_winner[0], ' ha ganado al ', semifin1_winner[0])
        final_dict[semifin1_looser[0]] = 'SF'
        final_dict[semifin2_looser[0]] = 'SF'

        #Los equipos que no han llegado a la semifinal los dejamos igual
        count_defeated = 0
        for key, value in defeated_dict.items():
            if count_defeated < 32 - len(semifinalists_dict):
                if count_defeated <= 3:
                    final_dict[key] = 'QF'
                elif 3 < count_defeated <= 11:
                    final_dict[key] = 'R16'
                else:
                    final_dict[key] = 'GR'
                count_defeated += 1

        return final_dict