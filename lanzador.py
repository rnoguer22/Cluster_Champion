class Lanzador:
    def __init__(self):
        self.column_combinations = [['GF', 'Pts'], ['GF', 'GD'], ['GF', 'Attendance'], ['GD', 'Pts'], ['GD', 'Attendance']]

    def lanzar_actualizacion_scrapping(self):
        from Web_Scrapping.scrapper import Scrapping
        def scrape(url, year):
            scrap = Scrapping(url, year)
            scrap.get_html()
            df = scrap.get_table()
            scrap.save_csv(df)
        
        urls = ['https://fbref.com/en/comps/8/Champions-League-Stats',
                'https://fbref.com/en/comps/8/2022-2023/2022-2023-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2021-2022/2021-2022-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2020-2021/2020-2021-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2019-2020/2019-2020-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2018-2019/2018-2019-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2017-2018/2017-2018-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2016-2017/2016-2017-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2015-2016/2015-2016-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2014-2015/2014-2015-Champions-League-Stats',  
                'https://fbref.com/en/comps/8/2013-2014/2013-2014-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2012-2013/2012-2013-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2011-2012/2011-2012-Champions-League-Stats',
                'https://fbref.com/en/comps/8/2010-2011/2010-2011-Champions-League-Stats',]
        
        years = ['2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019', '2017-2018', 
                 '2016-2017', '2015-2016', '2014-2015', '2013-2014', '2012-2013', '2011-2012', '2010-2011']

        for url, year in zip(urls, years):
            scrape(url, year) 

    def lanzar_analisis_scrapped_data(self):
        from Web_Scrapping.analisis_scrapped_data import AnalisisScrappedData
        analisis = AnalisisScrappedData()
        analisis.analize_csv()
        analisis.get_final_data()       

    def lanzar_scrap_players(self):
        from Web_Scrapping.scrap_players import ScrapPlayers
        print('Haciendo scrapping de los goleadores...')
        goleadores = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/goleadores')
        html = goleadores.get_html()
        df = goleadores.get_table(html)
        goleadores.save_csv(df, 'Web_Scrapping/Players_csv/goleadores.csv')

    def lanzar_scrap_pass(self):
        from Web_Scrapping.scrap_players import ScrapPlayers
        print('Haciendo scrapping de los pasadores...')
        goleadores = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/pasadores')
        html = goleadores.get_html()
        df = goleadores.get_table(html)
        goleadores.save_csv(df, 'Web_Scrapping/Players_csv/pasadores.csv')

    def lanzar_scrap_gks(self):
        from Web_Scrapping.scrap_players import ScrapPlayers
        print('Haciendo scrapping de los porteros...')
        porteros = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/porteros')
        html = porteros.get_html()
        df = porteros.get_table(html)
        porteros.save_csv(df, 'Web_Scrapping/Players_csv/porteros.csv')
    
    def lanzar_scrap_logos(self):
        from Web_Scrapping.scrap_img import Scrap_Img
        url = 'https://resultados.as.com/resultados/futbol/champions/equipos/'
        scrap_img = Scrap_Img(url)
        soup = scrap_img.get_html()
        img_tags = scrap_img.get_imgs(soup)
        scrap_img.save_imgs('./Web_Scrapping/Logos_img', img_tags)

    

    def lanzar_winrate(self):
        from UEFA_Winrate.winrate import Winrate
        print('Calculando probabilidad de éxito para cada equipo...')
        winrate = Winrate('./UEFA_Predictions/csv')
        combined_df = winrate.combine_data()
        df_prob = winrate.calculate_prob(combined_df, './UEFA_Winrate/csv/winrate.csv')
        winrate.plot_prob('./UEFA_Winrate/img/winrate.png', df_prob)

    

    def lanzar_img_classifier(self):
        from IMG_Classifier.img_classifier import Img_Classifier
        print('Clasificando imagenes...')
        img_classifier = Img_Classifier('./Web_Scrapping/Logos_img')
        img_classifier.data_exploration()
        train_generator, validation_generator, batch_size, classnames = img_classifier.create_data_generators()
        model = img_classifier.define_cnn(train_generator)
        history = img_classifier.train_model(model, train_generator, validation_generator, batch_size)
        img_classifier.plot_loss(history)
        img_classifier.get_model_performance(model, validation_generator, classnames)
        img_classifier.save_model(model, './IMG_Classifier/model.h5')
        classes = img_classifier.get_classes()
        img_classifier.predict('./IMG_Classifier/model.h5', './Web_Scrapping/test', classes)




    def launch_all(self):
        '''
        #Lanzamos el web scrapping de las clasficasiones de la champions
        self.lanzar_actualizacion_scrapping()
        self.lanzar_analisis_scrapped_data()
        #Lanzamos el web scrapping de los jugadores
        lanzador.lanzar_scrap_players()
        lanzador.lanzar_scrap_pass()
        lanzador.lanzar_scrap_gks()
        '''
        #self.lanzar_scrap_logos()
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
        '''
        '''
        #Lanzamos los modelos de prediccion
        self.lanzar_randomforest()
        self.lanzar_gradientboosting()
        self.lanzar_autoregressive()
        self.lanzar_exponentialsmoothing()    
        self.lanzar_arima()
        self.lanzar_sarimax()
        self.lanzar_linear_regression()
        '''
        #self.lanzar_monte_carlo()

        #self.lanzar_winrate()

        #self.lanzar_img_classifier()

    


    def limpiar_pantalla():
        import os
        import platform
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    