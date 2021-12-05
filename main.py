import requests
import re

# Almacenar sitio web
URL = 'https://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    
    # Realizar peticion 
    response = requests.get(URL)

    if response.status_code == 200:
        
        # Mostrar todo el html de la pagina
        # print(response.text)

        # Crear html en local para evitar realizar muchas peticiones
        # with open('econpy.html', 'w+') as file:
        #     file.write(response.text)

        '''
        Seleccionamos el string nombre. Recorro las lineas que tienen nombre y 'quito' las posiciones de string que no necesito
        '''
        # content = response.text
        # regexa = '<div title="buyer-name">'
        # regexb = '</div>'
        # for line in content.split('\n'):
        #     if regexa in line:
        #         start = line.find(regexa) + len(regexa)
        #         end = line.find(regexb)
        #         title = line[start:end]
        #         print(title)

        '''
        Otra forma es utilizando expresiones regulares. 
        '''
        content = response.text
        regex = '<div title="buyer-name">(.+?)</div>'
        for title in re.findall(regex, content):
            print(title)

        '''
        Para pruebas se recomienda leer el maquetado directamente del archivo html y asi evitar hacer peticiones constantemente. Ya no necesitariamos estas 3 lineas:
        -> URL = 'https://econpy.pythonanywhere.com/ex/001.html'
        -> response = requests.get(URL)
        -> if response.status_code == 200:        
        '''
        # with open('econpy.html', 'r') as file:
        #     content = file.read()



