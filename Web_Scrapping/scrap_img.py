import requests
from bs4 import BeautifulSoup
import os
from unidecode import unidecode



class Scrap_Img:

    def __init__(self, url):
        self.url = url
    

    #Metodo para obtener el contenedor html donde se encuentran las imagenes
    def get_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup
        else:
            print('Error al obtener el contenido de la página:', response.status_code)


    #Metodo para obtener las etiquetas html de las imagenes que necesitamos
    def get_imgs(self, soup):
        section = soup.find('section', class_='equipos-inferior cf')
        if section:
            return section.find_all('img')
    

    #Funcion para descargar cada imagen y guardarla en una carpeta con su nombre
    def save_imgs(self, output_path, img_tags):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for img_tag in img_tags:
            img_url = img_tag.get('data-src')
            alt_text = img_tag.get('alt')
            if img_url and alt_text:
                #Obtenemos el nombre del equipo
                team_name = ' '.join(alt_text.split()[1:]) if alt_text.startswith('Escudo/Bandera') else alt_text
                team_name = unidecode(team_name)
                team_name = self.fix_team_name(team_name)
                # Creamos una carpeta para el equipo si no existe
                team_directory = os.path.join(output_path, team_name)
                if not os.path.exists(team_directory):
                    os.makedirs(team_directory)
                img_name = team_name + '.png'
                #Descargamos la imagen y la guardamos en su carpeta correspondiente
                with open(os.path.join(team_directory, img_name), 'wb') as f:
                    f.write(requests.get(img_url).content)
                    print(f'Imagen {img_name} del equipo {team_name} descargada exitosamente.')
    

    #Metodo para corregir los nombres de los equipos
    def fix_team_name(self, team_name):
        if team_name == 'Atletico':
            team_name = 'Atlético Madrid'
        if team_name == 'E. Roja':
            team_name = 'Red Star'
        if 'M.' in team_name:
            team_name = team_name.replace('M.', 'Manchester')
        if 'B.' in team_name:
            team_name = team_name.replace('B.', 'Borussia')
        if 'R.' in team_name:
            team_name = team_name.replace('R.', 'Real')
        return team_name