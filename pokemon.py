import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://pokemondb.net'
URL = '/pokedex/all'

def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        return soup
    else:
        return None

def get_especie(url):
    soup = get_content(url)
    table = soup.find('table', class_='vitals-table')
    especie = table.tbody.find_all('tr')[2].td.text
    return especie


if __name__=='__main__':
        
    # Creo un objeto soup, enviando como parametro el link
    soup = get_content(DOMAIN + URL)

    # Busco la tabla que contiene las filas
    table = soup.find('table', {'id':'pokedex'})
    # Recorro las filas. Para probar limite a 10 filas
    for row in table.tbody.find_all('tr', limit=10):

        # TRAER NOMBRE

        # 1° forma 
        # columns = row.find('td', class_='cell-name')
        # name = columns.a.text
        # print(name)

        # 2° forma. El limit se utiliza para que no llame todas las columnas, solo las primeras 3
        columns = row.find_all('td', limit=3)
        name = columns[1].a.text
        print(f'Nombre {name}')

        # TRAER TIPOS

        # Agrupo el tipo o los tipos en una lista
        tipo = [a.text for a in columns[2].find_all('a')]
        # Opcional: convierto la lista en string
        print(f"Tipo: {' '.join(tipo)}")

        # TRAER ESPECIE

        # Armo el link con el href que me lleva a otra pagina
        url_poke = DOMAIN + columns[1].a['href']        
        especie = get_especie(url_poke)
        print(f'Especie: {especie}')

        
        
        




        

