from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import os


class DistributionCluster(CentroidCluster):

    def __init__(self, data_path, cluster_type:str='gmm'):
        super().__init__(data_path, cluster_type)
    

    #Metodo para encuadrar los datos en el modelo especificado
    def fit_model(self, features, clusters:int=3):
        self.X = self.df[features]
        if self.cluster_type == 'gmm':
            model = GaussianMixture(n_components=clusters, covariance_type='full', random_state=0)
        else:
            raise ValueError('Invalid cluster type')
        model.fit(self.X)
        return model
    

    def plot_results(self, model):
        print(f'Obteniendo distribution cluster {self.cluster_type} para {self.X.columns[0]} y {self.X.columns[1]}...')
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X.iloc[:, 0], self.X.iloc[:, 1], c=model.predict(self.X), cmap='viridis', s=50, alpha=0.5)
        plt.xlabel(self.X.columns[0])
        plt.ylabel(self.X.columns[1])
        plt.title(f'{self.cluster_type} Clustering')
        try:
            if not os.path.exists(f'Clusters/DistributionClustering/img/{self.cluster_type}'):
                os.makedirs(f'Clusters/DistributionClustering/img/{self.cluster_type}')
            plt.savefig(f'Clusters/DistributionClustering/img/{self.cluster_type}/{self.cluster_type}-{self.X.columns[0]}-{self.X.columns[1]}.png')    
        except:
            print('Error al guardar la imagen')