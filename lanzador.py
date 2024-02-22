from Clusters.Cluster import Cluster

class Lanzador:

    def __init__(self):
        self.column_combinations = [['GF', 'Pts'], ['GF', 'GD'], ['GF', 'Attendance'], ['GD', 'Pts'], ['GD', 'Attendance']]

    def lanzar_kmeans(self):
        kmean = Cluster('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', 'Kmeans')
        for column in self.column_combinations:
            model = kmean.fit_model(list(column), 5)
            kmean.plot_results(model)