"""
Programa que saca información de películas realizando una petición a la Api de tmdb.
Este es el menu de opciones para ejecutar el programa, en el cual vamos a realizar las búsquedas de:
    - Buscar película por nombre.
    - Buscar detalles de película por ID.
    - Buscar películas recomendadas pasándole un ID
    - Buscar top 5 trending topic de películas por género o todos los géneros, semana o día.
    - Listar todos los géneros existentes.

Autor: Javier Postigo Arévalo
Fecha: 04-2023
"""
import movie_api
from menu import Menu
str_ = """
********************
|*-- Buscapelis --*|
********************
"""
menu = Menu(str_, 'Buscar código de película según su nombre.',
            'Buscar información de película según su código.',
            'Películas a recomendar si nos gusta una película concreta.',
            'Obtener las 5 películas "trending topic" semanal o del día en función del género.',
            'Mostrar géneros disponibles. ')
while True:

    match menu.choose_option():
        case 1:
            movie_api.show_movie_id_by_name()
        case 2:
            movie_api.return_movie_details()
        case 3:
            movie_api.return_recommended_movies()
        case 4:
            movie_api.print_five_trending_films()
        case 5:
            movie_api.list_all_movies_genres()
        case 6:
            print("Programa cerrado.")
            break
