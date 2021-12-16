import requests
from bs4 import BeautifulSoup

url = 'https://es.stackoverflow.com/questions'

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

grupo_de_preguntas = soup.find(id='questions')
cada_pregunta = grupo_de_preguntas.find_all(class_='question-summary')


for pregunta in cada_pregunta:
    titulo = pregunta.find('h3').a.text
    descripcion = pregunta.find(class_="excerpt").text
    
    # Limpiar los datos
    # descripcion = descripcion.replace('\n', '')..replace('\r', '').strip()
    descripcion = descripcion.strip()  #mejor
    
    print(f'Titulo: {titulo}')
    print(f'Descripcion: {descripcion}')
    print('')


