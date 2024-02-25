import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

from UEFA_Predictions.UEFA_Prediction import Prediction



class Prediction2(Prediction):

    def __init__(self, data_path):
        super().__init__(data_path)

    def make_predictions(self, prediction_data_path, classifier):
        X = self.df.iloc[:, 1:].values
        y = self.df.iloc[:, 0].values

        data = pd.read_csv(self.data_path, encoding='utf-8')
        teams = data['Squad'].values
        data.drop(['Squad', 'id'], inplace=True, axis=1)

        classifier = classifier.lower()
        if classifier == 'autoregressive':
            model = AutoReg(data, lags=1)
        model_fit = model.fit()
        predictions = model_fit.predict(start=len(data), end=len(data))

        prediction_df = pd.DataFrame({'Squad':teams, 'Prediction':predictions})
        prediction_df['Prediction'] = prediction_df['Prediction'].apply(self.convert)
        prediction_df.to_csv(f'./UEFA_Predictions/csv/{classifier}_Predictions.csv', index=False)

    def convert(self, standing):
        return super().convert(standing)