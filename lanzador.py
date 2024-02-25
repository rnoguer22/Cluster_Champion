from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
from Clusters.DensityClustering.DensityCluster import DensityCluster
from Clusters.DistributionClustering.DistributionCluster import DistributionCluster
from Clusters.HierarchicalClustering.HierarchicalCluster import HierarchicalCluster

from UEFA_Predictions.UEFA_Prediction import Prediction


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