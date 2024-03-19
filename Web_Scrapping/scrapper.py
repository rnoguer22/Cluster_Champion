import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scrapping:

    def __init__(self, url, year) -> None:
        self.url = url
        self.year = year


    #Metodo para obtener el HTML de la web
    def get_html(self, write:bool=False):
        # Realizar una solicitud GET para obtener el HTML de la página
        response = requests.get(self.url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido HTML de la respuesta
            html_content = response.content
            # Crear un objeto BeautifulSoup para analizar el HTML
            self.soup = BeautifulSoup(html_content, 'html.parser')
            if write:
                # Convertir el objeto Tag a una cadena usando prettify()
                html_str = self.soup.prettify()
                # Imprimir el contenido del cuerpo de la página
                path = f'Web_Scrapping/scrapped_html/UEFA_{self.year}.html'
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(html_str)
        else:
            print('Error al obtener el contenido de la página:', response.status_code)


    #Metodo para obtener los datos de la tabla de la champions
    def get_table(self):
        print('Obteniendo datos champions' + ' ' + str(self.year) + '...')
        overall_stats = self.soup.find('div', id=f'div_results{self.year}80_overall')
        soup_overall = BeautifulSoup(str(overall_stats), 'html.parser')

        col = soup_overall.find_all('th', scope='col')
        columns = []
        for th in col:
            content = th.get_text(strip=True)
            columns.append(content)
        tbody = soup_overall.find_all('tbody')
        soup_overall_rows = BeautifulSoup(str(tbody), 'html.parser')

        rows = soup_overall_rows.find_all('tr')
        data = []
        col_i = []
        counter = 0
        for tr in rows:
            #Vamos a eliminar el texto de los span en este caso
            for span in tr.find_all('span'):
                span.decompose()   
            for td in tr:
                content = td.get_text(strip=True)
                col_i.append(content)
                counter += 1
                if counter == len(columns):
                    data.append(col_i)
                    col_i = []
                    counter = 0

        df = pd.DataFrame(data, columns=columns)
        return df
    

    #Metodo para guardar los datos en un archivo CSV
    def save_csv(self, df):
        path = f'Web_Scrapping/scrapped_csv/UEFA_{self.year}.csv'
        df.to_csv(path, index=True, index_label='id', encoding='utf-8-sig')