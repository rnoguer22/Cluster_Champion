class LanzadorPredict:    
    def lanzar_randomforest(self):
        from UEFA_Predictions.UEFA_RecursiveForecasting import RecursiveForecasting
        print('\n ---------Random Forest---------')
        random_forest = RecursiveForecasting('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        return random_forest.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'RandomForest')

    def lanzar_gradientboosting(self):
        from UEFA_Predictions.UEFA_RecursiveForecasting import RecursiveForecasting
        print('\n ---------Gradient Boosting---------')
        gradient_boosting = RecursiveForecasting('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        return gradient_boosting.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'GradientBoosting')

    def lanzar_autoregressive(self):
        from UEFA_Predictions.UEFA_StatisticModel import StatisticModel
        print('\n ---------Autoregressive---------')
        autoregressive = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        return autoregressive.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'AutoRegressive')
    
    def lanzar_exponentialsmoothing(self):
        from UEFA_Predictions.UEFA_StatisticModel import StatisticModel
        print('\n ---------Exponential Smoothing---------')
        exponentialsmoothing = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        return exponentialsmoothing.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'ExponentialSmoothing')
    
    def lanzar_arima(self):
        from UEFA_Predictions.UEFA_StatisticModel import StatisticModel
        print('\n ---------ARIMA---------')
        arima = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        return arima.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'ARIMA')
    
    def lanzar_sarimax(self):
        from UEFA_Predictions.UEFA_StatisticModel import StatisticModel
        print('\n ---------SARIMAX---------')
        sarimax = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        return sarimax.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'SARIMAX')

    def lanzar_linear_regression(self):
        from Spark.spark import Spark
        print('\n ---------Linear Regression with PySpark---------')
        print('Launching PySpark...')
        spark = Spark()
        df = spark.read_file('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        df_target = spark.read_file('./UEFA_Analisis_CSV/UEFA_Target.csv')
        teams, coef_players, coef_gks = spark.get_teams(df_target, 'Squad')
        prediction = spark.predict(df, teams, coef_players, coef_gks)
        spark.stop()
        return prediction

    def lanzar_monte_carlo(self):
        from Monte_Carlo.monte_carlo import MonteCarlo
        mc = MonteCarlo('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', './UEFA_Analisis_CSV/UEFA_Target.csv')
        return mc.predict_champions_winner('./UEFA_Predictions/csv', num_simulations=1000)
    
    def launch_all(self):
        print(self.lanzar_randomforest())
        print(self.lanzar_gradientboosting())
        print(self.lanzar_autoregressive())
        print(self.lanzar_exponentialsmoothing())
        print(self.lanzar_arima())
        print(self.lanzar_sarimax())
        print(self.lanzar_linear_regression())
        print(self.lanzar_monte_carlo())