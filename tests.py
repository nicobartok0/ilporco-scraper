from lector2 import Lector
from sesionador2 import Sesionador
from proveedor import Proveedor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os
import cryptocode

lector = Lector(name='andina', ruta='C:\\Users\\nicob\\OneDrive\\Escritorio\\ilporco-scraper\\archivos\\andina.xlsx')
datos = lector.obtener_datos()


maxiconsumo = Proveedor('MAXICONSUMO', 'orlando.piccinini@gmail.com', 'Pampa.64')
andina = Proveedor('ANDINA', '', '')
serenisima = Proveedor('LA SERENISIMA', 'orlando.piccinini@gmail.com', 'Orlando0223')
bees = Proveedor('BEES', '1158108611', 'Ilporco22')

proveedores = [maxiconsumo, andina, serenisima, bees]
lector.intercode(datos)


sesionador = Sesionador()
sesionador.crear_sesiones(proveedores)
sesionador.abrir_sesiones()
sesiones = sesionador.sesiones

for key in sesiones.keys():
    print(f'{key}: {sesiones[key].sess_id}')