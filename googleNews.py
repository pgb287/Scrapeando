'''SCRAPEA EL TITULO DE LAS PRIMERAS 10 NOTICIAS DE GOOGLE NEWS EN LA SECCION DE CIENCIA Y TECNOLOGIA'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrRlNLQUFQAQ?hl=es-419&gl=AR&ceid=AR%3Aes-419'

if __name__=='__main__':
    response = requests.get(URL)
    
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        # Obtengo la fecha actual
        now = datetime.now().strftime('%d-%m-%Y_%H-%M')
        #print(now)

        # Dentro de la carpeta news guardamos archivo con los titulos
        with open(f'news/news_{now}.txt', 'w+', encoding='utf-8') as file:
            
            for element in soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb', limit=10):

                title = element.a.text
                file.write(title + '\n')
        
        print('Archivo actualizado')


