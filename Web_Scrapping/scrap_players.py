import requests
from bs4 import BeautifulSoup
import pandas as pd
import os



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
            #Obtenemos el encabezado de las columnas de la tabla
            headers = [header.get_text(strip=True) for header in table.find('tr').find_all('th')]
            #Obtenemos el contenido de la tabla
            data = []
            for row in table.find_all('tr')[1:]:
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                data.append(row_data)
            #Devolvemos un dataframe con el contenido
            return pd.DataFrame(data, columns=headers, index=None)
        else:
            print("No se encontró la tabla con la clase 'ctr-stadistics-header__table'")
            return pd.DataFrame()
    

    def save_csv(self, df, path):
        #Verficamos si la carpeta existe, si no la creamos
        folder = '/'.join(path.split('/')[:-1])
        if not os.path.exists(folder):
            os.makedirs(folder)
            print('Carpeta ', folder, ' creada correctamente')
        df.to_csv(path, index=False)

        

goleadores = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/goleadores')
html = goleadores.get_html()
df = goleadores.get_table(html)
goleadores.save_csv(df, 'Web_Scrapping/Players_csv/goleadores.csv')