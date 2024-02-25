import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX


from UEFA_Predictions.UEFA_Prediction import Prediction



class Prediction2(Prediction):

    def __init__(self, data_path):
        super().__init__(data_path)

    def make_predictions(self, prediction_data_path, classifier):
        X = self.df.iloc[:, 1:].values
        y = self.df.iloc[:, 0].values

        data = pd.read_csv(self.data_path, encoding='utf-8')
        prediction_data = pd.read_csv(prediction_data_path, encoding='utf-8')
        data = pd.concat([data, prediction_data])
        teams = prediction_data['Squad'].values
        rk = prediction_data['Rk'].values

        classifier = classifier.lower()
        if classifier == 'autoregressive' or classifier == 'exponentialsmoothing':
            if classifier == 'autoregressive':
                model = AutoReg(data['Rk'].values, lags=1)
            if classifier == 'exponentialsmoothing':
                model = ExponentialSmoothing(data['Rk'].values, trend='add', seasonal='add', seasonal_periods=12)
            model_fit = model.fit()
            predictions = model_fit.predict(start=len(data['Rk'])+1, end=len(data['Rk'])+len(rk))
        elif classifier == 'arima':
            model = ARIMA(data, order=(5,1,0))
            model_fit = model.fit(disp=0)
            predictions = model_fit.forecast(steps=1)[0]
        elif classifier == 'sarimax':
            model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
            model_fit = model.fit()
            predictions = model_fit.forecast(steps=1)
        else:
            raise ValueError('Invalid classifier')

        print(len(predictions))
        print(len(teams))

        prediction_df = pd.DataFrame({'Squad':teams, 'Prediction':predictions})
        print(prediction_df.head())
        prediction_df['Prediction'] = prediction_df['Prediction'].apply(self.convert)
        prediction_df.to_csv(f'./UEFA_Predictions/csv/{classifier}_Predictions.csv', index=False)

    def convert(self, standing):
        return super().convert(standing)