import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class K_Means:

    def __init__(self, data_path):
        self.data_path = data_path
    
    def load_data(self):
        df = pd.read_csv(self.data_path)
        return df

    def select_features(self, df, features):
        X = df[features]
        return X
    
    def fit_model(self, X, n_clusters):
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(X)
        return kmeans
    
    def visualize_results(self, X, labels, centroids):
        plt.figure(figsize=(8, 6))
        plt.scatter(X['Feature1'], X['Feature2'], c=labels, cmap='viridis', s=50, alpha=0.5)
        plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='red', label='Centroids')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('K-Means Clustering')
        plt.legend()
        plt.show()