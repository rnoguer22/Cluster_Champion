from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
import matplotlib.pyplot as plt
import os
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage




class HierarchicalCluster(CentroidCluster):

    def __init__(self, data_path, cluster_type:str='agglomerative'):
        super().__init__(data_path, cluster_type)
    

    #Metodo para encuadrar los datos en el modelo especificado
    def fit_model(self, features, clusters:int=None):
        self.X = self.df[features]
        if self.cluster_type == 'agglomerative':
            model = AgglomerativeClustering(n_clusters=clusters)
        else:
            raise ValueError('Invalid cluster type')
        model.fit(self.X)
        return model


    #Metodo para graficar los resultados de la clusterizacion
    def plot_results(self, model):
        print(f'Obteniendo hierarchical cluster {self.cluster_type} para {self.X.columns[0]} y {self.X.columns[1]}...')
        plt.figure(figsize=(8, 6))
        enlace = linkage(self.X, method='ward')
        dendrogram(enlace, no_labels=True)
        plt.xlabel(self.X.columns[0])
        plt.ylabel(self.X.columns[1])
        plt.title(f'{self.cluster_type} Clustering')
        try:
            if not os.path.exists(f'Clusters/HierarchicalClustering/img/{self.cluster_type}'):
                os.makedirs(f'Clusters/HierarchicalClustering/img/{self.cluster_type}')
            plt.savefig(f'Clusters/HierarchicalClustering/img/{self.cluster_type}/{self.cluster_type}-{self.X.columns[0]}-{self.X.columns[1]}.png')    
        except:
            print('Error al guardar la imagen')