from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()
        # Creo un objeto del tipo BSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        '''
        Muestra la primera etiqueta que encuentra con ese nombre, en el caso que hallan varias
        '''
        # print(soup.head)
        # print(soup.body)
        # print(soup.span)
        # print(type(soup.head))

        '''
        FIND. Busca una etiqueta, si hay varias trae la primera en encontrar
        '''
        # title = soup.find('title')
        # print(title)
        # print(title.name)
        # print(title.text)
        # print(title.get_text()) # similar al anterior

        '''
        FIND_ALL. Busqueda por etiqueta y atributo dentro de ella.
        '''
        # for element in soup.find_all('div', {'title':'buyer-info'}):

        #     #Accediendo por find
        #     # div = element.find('div')
        #     # span = element.find('span')

        #     #Accediendo por etiquetas hijos
        #     div = element.div
        #     span = element.span

        #     print(div.text, span.text)

        '''
        CLASES CSS. Accediendo por clases css
        '''
        # 1° forma
        # for element in soup.find_all(attrs={'class':'item-price'}):
        # 2° forma
        for element in soup.find_all(class_='item-price'):
            print(element.text)

        
