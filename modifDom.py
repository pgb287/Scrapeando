from bs4 import BeautifulSoup

with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    
    div = soup.find('div', {'title':'buyer-info'})
    
    '''MODIFICAR ELEMENTOS DEL DOM'''

    # Acceder al valor de la clave title(como un diccionario)
    #print(div['title'])
    
    # Otra forma de acceder
    #print(div.get('title'))

    # Con get puedo poner un valor por defecto si no encuentra la etiqueta que buscamos
    #print(div.get('titleee', 'default'))

    # AGREGAR ATRIBUTO
    #div['id'] = 'item01'
    
    # MODIFICAR ATRIBUTO
    #div['title'] = 'nuevo-titulo'
    
    # MODIFICAR VALOR DE LA ETIQUETA. En este ejemplo accedo a las etiquetas hijos y su propiedad string(valor)
    # div.div.string = 'Pablo Bustos'
    # div.span.string = '69.69'

    # print(div)
    # print(soup.prettify)


    '''CREAR NUEVA ETIQUETA'''
    
    # div = soup.new_tag('div', id='new-item', title='item-title')

    # a = soup.new_tag('a', href='www.google.com', target='_blank')
    # a.string = 'Link a Google'
       
    # # Con APPEND se agrega la etiqueta 'a' dentro de la etiqueta 'div', se agregan tambien unos saltos de lineas
    # div.append('\n')
    # div.append(a)
    # div.append('\n')
    
    # A la vez puedo agregar esta etiqueta div dentro del body del maquetado:
    
    #soup.body.append(div)  #al final del body
    #soup.body.insert(3, div) #Se inserta en cierta posicion(son posiciones de una lista de etiquetas que contiene body)
    #soup.body.insert(4, '\n') #inserto a continuacion un salto de linea

    # recorro el maquetado para ver bien la insercion
    # for pos, chil in enumerate(soup.body.children):
    #     print(pos)
    #     print(chil)
    
    # sino directamente con:
    #print(soup.prettify)

    '''ELIMINAR ETIQUETA O ATRIBUTOS'''

    #print(div)    
    # Si asignamos una lista vacia al contenido de div entonces borramos todo el contenido. recordemos que se trabaja como lista
    #div.contents = []
    
    #otra forma:
    #div.contents = list()

    # Borrar contenido (texto) de una etiqueta 
    #div.div.string = ''
    #div.span.string = ''

    # Extraer una etiqueta
    #div.span.extract()
    
    #puedo asignar esa extraccion a una variable
    # span = div.span.extract()
    # print(div)
    # print(span)







    


