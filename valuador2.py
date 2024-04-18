import requests
import time
from bs4 import BeautifulSoup


class Valuador:
    def __init__(self, sesiones:dict, articulos:list):
        self.sesiones = sesiones
        self.articulos = articulos

        for articulo in articulos:
            sesion_actual = sesiones[articulos.proveedor.nombre] 
            requests.get()
        

