from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
from sklearn.cluster import DBSCAN, OPTICS, HDBSCAN


class DensityCluster(CentroidCluster):

    def __init__(self, data_path, cluster_type:str='kmeans'):
        super().__init__(data_path, cluster_type)


    #Metodo para encuadrar los datos en el modelo especificado
    def fit_model(self, features, clusters:int=3):
        self.X = self.df[features]
        if self.cluster_type == 'dbscan':
            model = DBSCAN(eps=0.3, min_samples=10)
        elif self.cluster_type == 'optics':
            model = OPTICS(min_samples=10, xi=0.05, min_cluster_size=0.05)
        elif self.cluster_type == 'hdbscan':
            model = HDBSCAN(min_cluster_size=15)
        else:
            raise ValueError('Invalid cluster type')
        model.fit(self.X)
        return model