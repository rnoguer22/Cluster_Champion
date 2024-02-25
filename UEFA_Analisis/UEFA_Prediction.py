import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class Prediction:

    def __init__(self, data_path):
        self.data_path = data_path

    
    def make_predictions(self, prediction_data_path):
        df = pd.read_csv(self.data_path, encoding='utf-8')
        df.drop(['Squad', 'id'], inplace=True, axis=1)
        X = df.iloc[:, 9:].values
        y = df.iloc[:, 0].values
        clf = RandomForestClassifier(n_estimators=100, criterion='entropy')
        clf.fit(X, y)

        prediction_data = pd.read_csv(prediction_data_path, encoding='utf-8')
        teams = prediction_data['Squad'].values
        prediction_data.drop(['Squad', 'id'], inplace=True, axis=1)
        X_pred = prediction_data.iloc[:, 9:]
        y_pred = clf.predict(X_pred)
        prediction_df = pd.DataFrame({'Squad':teams, 'Prediction':y_pred})
        prediction_df['Prediction'] = prediction_df['Prediction'].apply(self.convert)
        prediction_df.to_csv('UEFA_Predictions.csv', index=False)


    #Funcion para convertir el numero de standing a la ronda de la champions
    def convert(self, standing):
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
