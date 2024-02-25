import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor



class Prediction:

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

        prediction_df = pd.DataFrame({'Squad':teams, 'Prediction':y_pred})
        prediction_df['Prediction'] = prediction_df['Prediction'].apply(self.convert)
        prediction_df.to_csv(f'./UEFA_Predictions/csv/{classifier}_Predictions.csv', index=False)


    #Funcion para convertir el numero de standing a la ronda de la champions
    def convert(self, standing):
        standing = round(standing)
        if standing == 1:
            return 'GR'
        elif standing == 2:
            return 'R16'
        elif standing == 3:
            return 'QF'
        elif standing == 4:
            return 'SF'
        elif standing == 5:
            return 'F'
        else:
            return 'W'
