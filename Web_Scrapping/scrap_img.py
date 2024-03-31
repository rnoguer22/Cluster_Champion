import requests
from bs4 import BeautifulSoup
import os



class Scrap_Img:

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


    def get_imgs(self, soup):
        section = soup.find('section', class_='equipos-inferior cf')
        if section:
            return section.find_all('img')
    

    def save_imgs(self, output_path, img_tags):
        # Si el directorio no existe, créalo
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Descargar cada imagen
        for img_tag in img_tags:
            # Obtenemos la URL de la imagen desde el atributo 'data-src'
            img_url = img_tag.get('data-src')
            # Obtenemos el nombre del equipo desde el atributo 'alt'
            alt_text = img_tag.get('alt')
            if img_url and alt_text:
                # Eliminamos la parte común "Escudo/Bandera" del atributo 'alt'
                team_name = alt_text.split(' ')[1] if alt_text.startswith('Escudo/Bandera') else alt_text
                # Creamos una carpeta para el equipo si no existe
                team_directory = os.path.join(output_path, team_name)
                if not os.path.exists(team_directory):
                    os.makedirs(team_directory)
                # Extraemos el nombre del archivo de la URL de la imagen
                img_name = team_name + '.png'
                # Escribimos el contenido de la imagen en un archivo en el directorio del equipo
                with open(os.path.join(team_directory, img_name), 'wb') as f:
                    f.write(requests.get(img_url).content)
                    print(f'Imagen {img_name} del equipo {team_name} descargada exitosamente.')


url = 'https://resultados.as.com/resultados/futbol/champions/equipos/'
scrap_img = Scrap_Img(url)
soup = scrap_img.get_html()
img_tags = scrap_img.get_imgs(soup)
scrap_img.save_imgs('./Web_Scrapping/Logos_img', img_tags)