class LanzadorScrapping:
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