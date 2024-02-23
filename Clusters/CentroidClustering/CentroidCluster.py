import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth, MiniBatchKMeans

class CentroidCluster:

    def __init__(self, data_path, cluster_type:str='kmeans'):
        self.data_path = data_path
        self.cluster_type = cluster_type.lower()
        self.df = pd.read_csv(data_path)
        self.df.drop('Squad', axis=1, inplace=True)
        self.df.drop('Top Team Scorer', axis=1, inplace=True)
        self.df.drop('Goalkeeper', axis=1, inplace=True)


    def fit_model(self, features, clusters:int=3):
        self.X = self.df[features]
        if self.cluster_type == 'kmeans':
            model = KMeans(n_clusters=clusters)
        elif self.cluster_type == 'mean-shift':
            bandwidth = estimate_bandwidth(self.X, quantile=0.2, n_samples=500)
            model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        elif self.cluster_type == 'minibatch':
            model = MiniBatchKMeans(n_clusters=clusters, batch_size=10)
        else:
            raise ValueError('Invalid cluster type')
        model.fit(self.X)
        return model
    
    
    def plot_results(self, model):
        print(f'Obteniendo cluster {self.cluster_type} para {self.X.columns[0]} y {self.X.columns[1]}...')
        centroids = model.cluster_centers_
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X.iloc[:, 0], self.X.iloc[:, 1], c=model.labels_, cmap='viridis', s=50, alpha=0.5)
        plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='red', label='Centroids')
        plt.xlabel(self.X.columns[0])
        plt.ylabel(self.X.columns[1])
        plt.title(f'{self.cluster_type} Clustering')
        plt.legend()
        if not os.path.exists(f'Clusters/CentroidClustering/img/{self.cluster_type}'):
            os.makedirs(f'Clusters/CentroidClustering/img/{self.cluster_type}')
        plt.savefig(f'Clusters/CentroidClustering/img/{self.cluster_type}/{self.cluster_type}-{self.X.columns[0]}-{self.X.columns[1]}.png')