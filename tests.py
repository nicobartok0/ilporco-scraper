from lector2 import Lector
from sesionador2 import Sesionador
from proveedor import Proveedor
import time
import sys, os
import cryptocode
from operador2 import Operador

operador = Operador('andina-mini', 'C:\\Users\\nicob\\OneDrive\\Escritorio\\ilporco-scraper\\archivos\\andina-mini.xlsx')
credentials = {
    'MAXICONSUMO': ['orlando.piccinini@gmail.com', cryptocode.encrypt('Pampa.64', 'ilporco')],
    'OSCAR DAVID': ['orlando.piccinini@gmail.com', cryptocode.encrypt('Pampa.64', 'ilporco')],
    'ANDINA': ['','']
}

operador.inicializar(credentials=credentials)
for element in operador.articulos:
    print(f'{element.nombre}: {element.precio}')