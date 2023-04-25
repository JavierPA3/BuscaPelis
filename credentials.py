"""Guardamos la clave de nuestra API tmdb"""

import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
