from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.db import models
from .models import Pelicula


def ratings_pelculas(request):
    rotten = 'https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=3'
    resultado = scrape_rottenTomatoes(rotten)
    peliculas_data = {}
  
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        puntuacion_usuario = request.POST.get(f'rating_{titulo}')
        

        if puntuacion_usuario is not None:
            try:
                pelicula = Pelicula.objects.get(titulo=titulo)
                pelicula.puntaje_usuario = puntuacion_usuario
                print(puntuacion_usuario)
                pelicula.save()
            except Pelicula.DoesNotExist:
                pelicula = Pelicula.objects.create(titulo=titulo, puntaje_usuario=puntuacion_usuario)
        
    for titulo, imagen, puntaje in zip(resultado['pelicula'], resultado['imagen'], resultado['puntaje']):
        if titulo not in peliculas_data:
            peliculas_data[titulo] = []
            try:
                pelicula = Pelicula.objects.get(titulo=titulo)
                puntaje_usuario = pelicula.puntaje_usuario
            except Pelicula.DoesNotExist:
                puntaje_usuario = None
            peliculas_data[titulo].append({'imagen': imagen, 'puntaje': puntaje, 'puntaje_usuario': puntaje_usuario})

    return render(request, 'index.html', {'peliculas_data': peliculas_data})




def scrape_rottenTomatoes(url):
    respuesta = requests.get(url)
    peliculas_info = {'pelicula': [], 'imagen': [], 'puntaje': []}

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        peliculas = soup.find_all('div', class_='js-tile-link')
        puntajes = soup.find_all('score-pairs')
        
        for pelicula in peliculas:
            titulo_peliculas = pelicula.find('span', class_='p--small')
            imagenes = pelicula.find('img', class_='posterImage')
            nombre_pelicula = titulo_peliculas.get_text(strip=True)
            peliculas_info['pelicula'].append(nombre_pelicula )
            imagen_src = imagenes .get('src')
            peliculas_info['imagen'].append(imagen_src)

        for puntaje in puntajes:
            audiencescore = puntaje.get('criticsscore')
            peliculas_info['puntaje'].append(audiencescore)
     
        return peliculas_info


