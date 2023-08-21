from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup

"""
    Solicitud de extraccion de la informacion.

    Esta función manda a llamar a la funcion scrape_billboardy
    hace la solicitud de estraccion a la pagina.

    param request: solicitud.
    type request: str
    return: resultado de la extraccion del top 100 de canciones.

    """

def web_scrape(request):
    bilboard = 'https://www.billboard.com/charts/hot-100/'

    resultado = scrape_billboard(bilboard)

    return render(request, 'index.html', resultado)

"""
    Web Scraper del top 100 de Bilboard.

    Esta función busca la informacion de los nombres de las canciones y el nombre de sus cantantes, tola lista de canciones del top 100 de bilboard y el
    para ser mostrada en la pagina web.

    param url: url del top 100 de Bilboard.
    type request: str
    return: devuelve el titulo de la pagina, el top 100 de canciones y las posicione
    rtype: str,

    """

def scrape_billboard(url):
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        titulo_web = soup.find('title')
        if titulo_web:
            title = titulo_web.get_text()
        else:
            title = 'Título no encontrado'

     
        canciones_bilboard= soup.find_all('li', class_='o-chart-results-list__item')
        nombre_canciones = []
        cantantes = []

        for cancion in canciones_bilboard:
            cancion_nombre = cancion.find('h3', id='title-of-a-story', class_='c-title')
            nombre_cantante = cancion.find('span', class_='c-label')
            
            if cancion_nombre and nombre_cantante:
                nombre_cancion = cancion_nombre.get_text(strip=True)
                nombre_canciones.append(nombre_cancion)
                artista = nombre_cantante.get_text(strip=True)
                cantantes.append(artista)
        
        posiciones = list(range(1, len(nombre_canciones)+1))
        top = zip(posiciones, nombre_canciones,cantantes)
        
        return {
            'titulo': title,
            'top': top,
            'posiciones':posiciones,
        }
    else:
        return {
            'error': f'Error al realizar la solicitud en la pagina: {respuesta.status_code}'
        }


