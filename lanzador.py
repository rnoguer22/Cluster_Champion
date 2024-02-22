from Clusters.KMeans import K_Means

class Lanzador:

    def lanzar_kmeans():
        kmean = K_Means('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        column_combinations = [['GF', 'Pts'], ['GF', 'GD'], ['GF', 'Attendance'], ['GD', 'Pts'], ['GD', 'Attendance']]
        for column in column_combinations:
            model = kmean.fit_model(list(column), 5)
            kmean.plot_results(model)