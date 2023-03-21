import requests
from bs4 import BeautifulSoup
from pagina import Pagina

#función que obtiene el título, la descripción, los subtítulos y el contenido de una página de Wikipedia y los devuelve dentro de una instancia de la clase Página previamente definida en pagina.py
def obtener_datos_wikipedia(url):
    #en response almacenamos el contenido de la página que corresponde a la url del parámetro de entrada.
    response = requests.get(url)
    #creamos una instancia de BeautifulSoup con el contenido de la página para después poder parsearla facilmente.
    soup = BeautifulSoup(response.text, 'html.parser')

    #seleccionamos el texto de la etiqueta h1 que ademas tiene como identificador "firstHeading"
    #<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-main">Inteligencia artificial</span></h1>
    titulo = soup.find('h1', {'id': 'firstHeading'}).text
    #como descripción seleccionamos el primer párrafo de la página
    descripcion = soup.find('div', {'id': 'bodyContent'}).find('p').text
    #como subtítulos seleccionamos las etiquetas <h2>, exceptuando el último, ya que generalmente es "Referencias" o "Véase también"
    subtitulos = [h2.text for h2 in soup.find_all('h2')][:-1]
    #como contenido devolvemos todos los párrafos que forman parte del contenido de la página
    contenido = '\n'.join([p.text for p in soup.find('div', {'id': 'bodyContent'}).find_all('p')])

    #devolvemos una instancia de la clase página
    return Pagina(titulo, descripcion, subtitulos, contenido)



if __name__ == '__main__':
    # Lista de URLs de Wikipedia a obtener
    urls = [
        "https://es.wikipedia.org/wiki/Inteligencia_artificial",
        "https://es.wikipedia.org/wiki/Red_neuronal_artificial",
        "https://es.wikipedia.org/wiki/Aprendizaje_automático",
    ]

    # Lista para almacenar las instancias de la clase Pagina
    paginas = []

    # Iteramos sobre las URLs y obtenemos los datos de cada página
    for url in urls:
        print(f"Obteniendo datos de: {url}")
        pagina = obtener_datos_wikipedia(url)
        paginas.append(pagina)

    # Mostramos la información de cada página almacenada en la lista
    for i, pagina in enumerate(paginas):
        print(f"\n==== Página {i + 1} ====")
        #pagina.mostrar_pagina()
        pagina.imprimir_pagina_a_fichero("fichero"+str(i)+".txt","C:\\Users\\ignac\\Desktop")

