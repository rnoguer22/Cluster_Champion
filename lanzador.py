from Clusters.CentroidClustering.CentroidCluster import CentroidCluster
from Clusters.DensityClustering.DensityCluster import DensityCluster
from Clusters.DistributionClustering.DistributionCluster import DistributionCluster
from Clusters.HierarchicalClustering.HierarchicalCluster import HierarchicalCluster

from UEFA_Predictions.UEFA_RecursiveForecasting import RecursiveForecasting
from UEFA_Predictions.UEFA_StatisticModel import StatisticModel
from Spark.spark import Spark

from Web_Scrapping.scrap_players import ScrapPlayers
from Web_Scrapping.scrap_img import Scrap_Img

from UEFA_Winrate.winrate import Winrate

from IMG_Classifier.img_classifier import Img_Classifier


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


    def lanzar_randomforest(self):
        print('\n ---------Random Forest---------')
        random_forest = RecursiveForecasting('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        random_forest.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'RandomForest')

    def lanzar_gradientboosting(self):
        print('\n ---------Gradient Boosting---------')
        gradient_boosting = RecursiveForecasting('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        gradient_boosting.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'GradientBoosting')

    def lanzar_autoregressive(self):
        print('\n ---------Autoregressive---------')
        autoregressive = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        autoregressive.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'AutoRegressive')
    
    def lanzar_exponentialsmoothing(self):
        print('\n ---------Exponential Smoothing---------')
        exponentialsmoothing = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        exponentialsmoothing.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'ExponentialSmoothing')
    
    def lanzar_arima(self):
        print('\n ---------ARIMA---------')
        arima = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        arima.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'ARIMA')
    
    def lanzar_sarimax(self):
        print('\n ---------SARIMAX---------')
        sarimax = StatisticModel('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        sarimax.make_predictions('./UEFA_Analisis_CSV/UEFA_Target.csv', 'SARIMAX')

    def lanzar_linear_regression(self):
        print('\n ---------Linear Regression with PySpark---------')
        print('Launching PySpark...')
        spark = Spark()
        df = spark.read_file('./UEFA_Analisis_CSV/UEFA_Final_Data.csv')
        df_target = spark.read_file('./UEFA_Analisis_CSV/UEFA_Target.csv')
        teams, coef_players, coef_gks = spark.get_teams(df_target, 'Squad')
        spark.predict(df, teams, coef_players, coef_gks)
        spark.stop()


    def lanzar_scrap_players(self):
        print('Haciendo scrapping de los goleadores...')
        goleadores = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/goleadores')
        html = goleadores.get_html()
        df = goleadores.get_table(html)
        goleadores.save_csv(df, 'Web_Scrapping/Players_csv/goleadores.csv')

    def lanzar_scrap_pass(self):
        print('Haciendo scrapping de los pasadores...')
        goleadores = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/pasadores')
        html = goleadores.get_html()
        df = goleadores.get_table(html)
        goleadores.save_csv(df, 'Web_Scrapping/Players_csv/pasadores.csv')

    def lanzar_scrap_gks(self):
        print('Haciendo scrapping de los porteros...')
        porteros = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/porteros')
        html = porteros.get_html()
        df = porteros.get_table(html)
        porteros.save_csv(df, 'Web_Scrapping/Players_csv/porteros.csv')
    
    def lanzar_scrap_logos(self):
        url = 'https://resultados.as.com/resultados/futbol/champions/equipos/'
        scrap_img = Scrap_Img(url)
        soup = scrap_img.get_html()
        img_tags = scrap_img.get_imgs(soup)
        scrap_img.save_imgs('./Web_Scrapping/Logos_img', img_tags)

    

    def lanzar_winrate(self):
        print('Calculando probabilidad de éxito para cada equipo...')
        winrate = Winrate('./UEFA_Predictions/csv')
        combined_df = winrate.combine_data()
        df_prob = winrate.calculate_prob(combined_df, './UEFA_Winrate/csv/winrate.csv')
        winrate.plot_prob('./UEFA_Winrate/img/winrate.png', df_prob)

    

    def lanzar_img_classifier(self):
        print('Clasificando imagenes...')
        img_classifier = Img_Classifier('./Web_Scrapping/Logos_img')
        img_classifier.data_exploration()
        train_generator, validation_generator, batch_size, classnames = img_classifier.create_data_generators()
        model = img_classifier.define_cnn(train_generator)
        history = img_classifier.train_model(model, train_generator, validation_generator, batch_size)
        img_classifier.plot_loss(history)
        img_classifier.get_model_performance(model, validation_generator, classnames)
        img_classifier.save_model(model, './IMG_Classifier/model.h5')




    def launch_all(self):
        '''
        #Lanzamos el web scrapping de los jugadores
        lanzador.lanzar_scrap_players()
        lanzador.lanzar_scrap_pass()
        lanzador.lanzar_scrap_gks()
        '''
        self.lanzar_scrap_logos()
        '''
        #Lanzamos los clusters
        self.lanzar_kmeans()
        self.lanzar_mean_shift()
        self.lanzar_minibatch()
        self.lanzar_dbscan()
        self.lanzar_optics()
        self.lanzar_hdbscan()
        self.lanzar_gmm()
        self.lanzar_agglomerative()

        #Lanzamos los modelos de prediccion
        self.lanzar_randomforest()
        self.lanzar_gradientboosting()
    
        self.lanzar_autoregressive()
        self.lanzar_exponentialsmoothing()
        '''
        #self.lanzar_arima()
        #self.lanzar_sarimax()

        #self.lanzar_linear_regression()

        #self.lanzar_winrate()

        #self.lanzar_img_classifier()