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
        self.player_performance(copy_players, teams, y_pred)
        prediction_dict = dict(zip(teams, y_pred))
                    
        sorted_prediction = self.convert(prediction_dict)
        print(sorted_prediction)
        prediction_df = pd.DataFrame({'Squad':sorted_prediction.keys(), 'Prediction':sorted_prediction.values()})
        prediction_df.to_csv(f'./UEFA_Predictions/csv/{classifier}_Predictions.csv', index=False)


    def player_performance(self, df_players, teams, predictions):
        for team in teams:
            players = df_players.loc[df_players['Squad'] == team]
            scorer = players['Top Team Scorer'].iloc[-1][:-1]
            for player in scorer.split(','):
                player = player.replace('...', '')
                print(player)
            print(team[:-9])
            print('\n')


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