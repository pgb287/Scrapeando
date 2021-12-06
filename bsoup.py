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
        # for element in soup.find_all(class_='item-price'):
        #     print(element.text)

        '''
        NODOS HIJOS - CONTENTS.
        '''
        # div = soup.find('div', {'title':'buyer-info'})

        # print(div)
        # print(div.contents) # lista con todos las etiquetas que lo contienen
        
        # # Asigno las posiciones que necesito en 2 variables y muestro el atributo text de cada una
        # div_nombre = div.contents[1]
        # div_precio = div.contents[3]
        # print(div_nombre.text, div_precio.text)
        
        # # Otra forma de acceder a los hijos es con children, el cual es un iterador que nos servira si lo recorremos. Mientras que contents devuelve una lista. Tener en cuenta que en ambos toma en cuenta los saltos de linea entre etiquetas 
        # for child in div.children:
        #     print(child) 
        '''
        NODOS HERMANOS - NEXT_SIBLING, PREVIOUS_SIBLING.
        '''
        # div = soup.find('div', {'title':'buyer-name'})        
        # Otra forma de buscar es mediante el contenido de la etiqueta:
        div = soup.find('div', string='Carson Busses')
        
        # Mostrando los nodos hermanos siguientes
        # print(div.next_sibling.next_sibling.next_sibling) 
        
        # Mostrando los nodos hermanos anteriores. En ambos casos si ya no hay mas nodos hermanos muestra None
        # print(div.previous_sibling.previous_sibling)

        # TAMBIEN SE LOS UTILIZA COMO ITERADORES AGREGANDO LA S AL FINAL        
        # for element in div.previous_siblings:
        #     print(element)
        # for element in div.next_siblings:
        #     print(element)
        # print(type(div.next_siblings))

        '''
        ELEMENTO PADRE - PARENT. Agrego parent hasta el nivel de abuelo que necesite
        '''
        # div = soup.find('div', {'title':'buyer-name'})
        # Muestra etiqueta padre entera
        # print(div.parent.parent)
        # Muestra el nombre de la etiqueta padre
        # print(div.parent.parent.name)
        
        # TAMBIEN SE LO UTILIZA COMO ITERADOR AGREGANDO S AL FINAL
        # for parent in div.parents:
        #     print(parent.name)

        '''
        RESUMEN:
        parent = elemento padre
        parents = listado de elementos padres hasta el nivel top
        next_sibling = siguiente elemento despues del elemento actual
        next_siblings = listado de elementos despues del elemento actual
        previous_sibling = elemento anterior al elemento actual
        previous_siblings = listado de elementos anteriores al elemento actual
        contents = listado de todos los elementos hijos
        children = generador de todos los elementos hijos
        descendants = generador de todos los elementos hijos de forma recursiva
        '''









