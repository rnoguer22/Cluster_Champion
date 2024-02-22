import pandas as pd
from itertools import combinations
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class K_Means:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self.df.drop('Squad', axis=1, inplace=True)
        self.df.drop('Top Team Scorer', axis=1, inplace=True)
        self.df.drop('Goalkeeper', axis=1, inplace=True)


    def fit_model(self, features, clusters:int):
        self.X = self.df[features]
        kmeans = KMeans(n_clusters=clusters)
        kmeans.fit(self.X)
        return kmeans
    
    
    def plot_results(self, model):
        centroids = model.cluster_centers_
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X.iloc[:, 0], self.X.iloc[:, 1], c=model.labels_, cmap='viridis', s=50, alpha=0.5)
        plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='red', label='Centroids')
        plt.xlabel(self.X.columns[0])
        plt.ylabel(self.X.columns[1])
        plt.title('K-Means Clustering')
        plt.legend()
        plt.savefig(f'Clusters/KMeans/KMeans-{self.X.columns[0]}-{self.X.columns[1]}.png')


kmean = K_Means('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
column_combinations = [['GF', 'Pts'], ['GF', 'GD'], ['GF', 'Attendance'], ['GD', 'Pts'], ['GD', 'Attendance']]
for column in column_combinations:
    model = kmean.fit_model(list(column), 5)
    kmean.plot_results(model)



