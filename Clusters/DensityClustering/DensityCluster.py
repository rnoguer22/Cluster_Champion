from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
from sklearn.cluster import DBSCAN, OPTICS, HDBSCAN
import matplotlib.pyplot as plt
import os


class DensityCluster(CentroidCluster):

    def __init__(self, data_path, cluster_type:str='dbscan'):
        super().__init__(data_path, cluster_type)


    #Metodo para encuadrar los datos en el modelo especificado
    def fit_model(self, features):
        self.X = self.df[features]
        if self.cluster_type == 'dbscan':
            model = DBSCAN(eps=2, min_samples=10)
        elif self.cluster_type == 'optics':
            model = OPTICS(min_samples=10, xi=0.05, min_cluster_size=0.05)
        elif self.cluster_type == 'hdbscan':
            model = HDBSCAN(min_cluster_size=15)
        else:
            raise ValueError('Invalid cluster type')
        model.fit(self.X)
        return model

    def plot_results(self, model):
        print(f'Obteniendo density cluster {self.cluster_type} para {self.X.columns[0]} y {self.X.columns[1]}...')
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X.iloc[:, 0], self.X.iloc[:, 1], c=model.labels_, cmap='viridis', s=50, alpha=0.5)
        plt.xlabel(self.X.columns[0])
        plt.ylabel(self.X.columns[1])
        plt.title(f'{self.cluster_type} Clustering')
        try:
            if not os.path.exists(f'Clusters/DensityClustering/img/{self.cluster_type}'):
                os.makedirs(f'Clusters/DensityClustering/img/{self.cluster_type}')
            plt.savefig(f'Clusters/DensityClustering/img/{self.cluster_type}/{self.cluster_type}-{self.X.columns[0]}-{self.X.columns[1]}.png')    
        except:
            print('Error al guardar la imagen')