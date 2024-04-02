import requests
from bs4 import BeautifulSoup
import os
from unidecode import unidecode
from PIL import Image



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
                img_path = os.path.join(team_directory, img_name)
                with open(img_path, 'wb') as f:
                    f.write(requests.get(img_url).content)
                    print(f'Imagen {img_name} del equipo {team_name} descargada exitosamente.')
                
                #Redimensionamos las imagenes tener mas datos para el modelo de prediccion de imagenes    
                for i in [0.75, 1, 1.25, 1.5]:
                    img_original = Image.open(img_path)
                    img_zoomed = img_original.copy()  
                    # Calcula las nuevas dimensiones de la imagen después del zoom
                    new_width = int(img_zoomed.width / i)
                    new_height = int(img_zoomed.height / i)
                    #Recortamos la imagen para hacer el zoom
                    left = (img_zoomed.width - new_width) / 2
                    top = (img_zoomed.height - new_height) / 2
                    right = (img_zoomed.width + new_width) / 2
                    bottom = (img_zoomed.height + new_height) / 2
                    img_zoomed = img_zoomed.crop((left, top, right, bottom)) #Aplicamos el zoom
                    #Redimensionamos la imagen y la guardamos
                    img_zoomed = img_zoomed.resize((img_original.width, img_original.height))
                    
                    #Rotamos la imagen dimensionada
                    for r in [0, 90, 180, 270]:
                        img_rotated = img_zoomed.rotate(r, expand=True)
                        new_img_name = f'{team_name}_{i}_{r}.png'
                        img_rotated.save(os.path.join(team_directory, new_img_name))

                    if i == 0.75:
                        j = 45
                    elif i == 1:
                        j = 135
                    elif i == 1.25:
                        j = 225
                    elif i == 1.5:
                        j = 315
                    else:
                        print(f'Error al guardar la imagen {new_img_name} del equipo {team_name}.')

                    #Guardamos algunas imagenes de test
                    directory = f'./Web_Scrapping/test'
                    img_rotated = img_zoomed.rotate(j, expand=True)
                    new_img_name = f'{team_name}_{i}_{j}.png'
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    img_rotated.save(os.path.join(directory, new_img_name))



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