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
            #Obtenemos el encabezado de las columnas de la tabla
            headers = [header.get_text(strip=True) for header in table.find('tr').find_all('th')]
            #Obtenemos el contenido de la tabla
            data = []
            for row in table.find_all('tr')[1:]:
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                data.append(row_data)
            return headers, data
        else:
            print("No se encontró la tabla con la clase 'ctr-stadistics-header__table'")
            return [], []

        

players = ScrapPlayers('https://www.mediotiempo.com/futbol/champions-league/goleadores')
html = players.get_html()

# Llama a la función get_table y almacena los datos de la tabla y los encabezados
encabezados, datos = players.get_table(html)

# Crear un DataFrame de Pandas
df = pd.DataFrame(datos, columns=encabezados, index=None)

# Guardar el DataFrame en un archivo CSV
print(df)