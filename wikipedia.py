'''Utilizando xpath de la libreria lxml
links:
https://lxml.de/lxmlhtml.html
http://xpather.com/
https://devhints.io/xpath#prefixes

User Agents: es una cadena de texto con la cual se puede identificar el navegador y el SO, por defecto es ROBOT. Por lo general hay que sobreescribir esta variable.
'''

import requests
from lxml import html

url = 'https://www.wikipedia.org/'

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

response = requests.get(url, headers = header)

parser = html.fromstring(response.text)

# Utilizando los metodos de
# palabra = parser.get_element_by_id('js-link-box-es')
# print(palabra.text_content())

# Utilizando xpath
palabra = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
print(palabra)

