import requests
from bs4 import BeautifulSoup
import pandas as pd



class ScrapPlayers:

    def __init__(self, url):
        self.url = url
    
    def get_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup
        else:
            print('Error al obtener el contenido de la página:', response.status_code)

    def get_table(self, soup):
        table = soup.find('table', class_='ctr-stadistics-header__table')
        if table:
            print(table)
        else:
            print('No se encontro la tabla')



players = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/goleadores')
html = players.get_html()
players.get_table(html)