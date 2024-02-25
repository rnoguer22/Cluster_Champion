from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
from Clusters.DensityClustering.DensityCluster import DensityCluster
from Clusters.DistributionClustering.DistributionCluster import DistributionCluster
from Clusters.HierarchicalClustering.HierarchicalCluster import HierarchicalCluster

from UEFA_Predictions.UEFA_Prediction import Prediction
from UEFA_Predictions.UEFA_Prediction2 import Prediction2


class Lanzador:
    def __init__(self):
        self.column_combinations = [['GF', 'Pts'], ['GF', 'GD'], ['GF', 'Attendance'], ['GD', 'Pts'], ['GD', 'Attendance']]

    def lanzar_kmeans(self):
        print('\n ---------Kmeans---------')
        kmean = CentroidCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'Kmeans')
        for column in self.column_combinations:
            model = kmean.fit_model(list(column), 5)
            kmean.plot_results(model)
    
    def lanzar_mean_shift(self):
        print('\n ---------Mean Shift---------')
        ms = CentroidCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'mean-shift')
        for column in self.column_combinations:
            model = ms.fit_model(list(column), 5)
            ms.plot_results(model)

    def lanzar_minibatch(self):
        print('\n ---------Mini Batch---------')
        minibatch = CentroidCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'minibatch')
        for column in self.column_combinations:
            model = minibatch.fit_model(list(column), 5)
            minibatch.plot_results(model)

    def lanzar_dbscan(self):
        print('\n ---------DBSCAN---------')
        dbscan = DensityCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'dbscan')
        for column in self.column_combinations:
            model = dbscan.fit_model(list(column))
            dbscan.plot_results(model)
    
    def lanzar_optics(self):
        print('\n ---------OPTICS---------')
        optics = DensityCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'optics')
        for column in self.column_combinations:
            model = optics.fit_model(list(column))
            optics.plot_results(model)
    
    def lanzar_hdbscan(self):
        print('\n ---------HDBSCAN---------')
        hdbscan = DensityCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'hdbscan')
        for column in self.column_combinations:
            model = hdbscan.fit_model(list(column))
            hdbscan.plot_results(model)

    def lanzar_gmm(self):
        print('\n ---------GMM---------')
        gmm = DistributionCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'gmm')
        for column in self.column_combinations:
            model = gmm.fit_model(list(column), 5)
            gmm.plot_results(model)
    
    def lanzar_agglomerative(self):
        print('\n ---------Agglomerative---------')
        agglomerative = HierarchicalCluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'agglomerative')
        for column in self.column_combinations:
            model = agglomerative.fit_model(list(column), 3)
            agglomerative.plot_results(model)

    


    def lanzar_randomforest(self):
        print('\n ---------Random Forest---------')
        random_forest = Prediction('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        random_forest.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'RandomForest')

    def lanzar_gradientboosting(self):
        print('\n ---------Gradient Boosting---------')
        gradient_boosting = Prediction('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        gradient_boosting.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'GradientBoosting')

    def lanzar_autoregressive(self):
        print('\n ---------Autoregressive---------')
        autoregressive = Prediction2('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        autoregressive.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'AutoRegressive')
    
    def lanzar_exponentialsmoothing(self):
        print('\n ---------Exponential Smoothing---------')
        exponentialsmoothing = Prediction2('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        exponentialsmoothing.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'ExponentialSmoothing')
    
    def lanzar_arima(self):
        print('\n ---------ARIMA---------')
        arima = Prediction2('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        arima.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'ARIMA')
    
    def lanzar_sarimax(self):
        print('\n ---------SARIMAX---------')
        sarimax = Prediction2('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        sarimax.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'SARIMAX')