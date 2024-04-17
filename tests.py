from lector2 import Lector
from sesion import Sesion_Maxiconsumo, Sesion_Oscar_David, Sesion_Andina, Sesion_La_Serenisima, Sesion_Bees
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os
import cryptocode

chromedriver_path = f'{os.getcwd()}\\assets\\chromedriver.exe'
sys.path.insert(0,chromedriver_path)
if os.name != 'posix': 
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

else:
    driver = webdriver.Chrome()

lector = Lector(name='andina', ruta='C:\\Users\\nicob\\OneDrive\\Escritorio\\ilporco-scraper\\archivos\\andina.xlsx')
datos = lector.obtener_datos()

proveedores_posibles = []
for dato in datos:
    if dato.proveedor not in proveedores_posibles:
        proveedores_posibles.append(dato.proveedor)

lector.intercode(datos)

print('CÓDIGOS EXTERNOS')
for dato in datos:
    print(f'NOMBRE: {dato.nombre} ILPORCO: {dato.codigo} EXTERNO: {dato.cod_externo}')

sesion_maxiconsumo = Sesion_Maxiconsumo('orlando.piccinini@gmail.com', cryptocode.encrypt('Pampa.64', 'ilporco'))
sesion_maxiconsumo.abrir_sesion(driver)
print(sesion_maxiconsumo.sess_id)