from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os
from proveedor import Proveedor
from sesion import Sesion_Andina, Sesion_Bees, Sesion_La_Serenisima, Sesion_Maxiconsumo, Sesion_Oscar_David


class Sesionador:

    # Definimos los atributos de nuestro sesionador, que en este caso será la inicialización del Webdriver
    def __init__(self):
        chromedriver_path = f'{os.getcwd()}\\assets\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        sys.path.insert(0,chromedriver_path)
        if os.name != 'posix': 
            self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome()
        self.sesiones = {}

    # Definimos la función en la que buscaremos el id de sesión de Maxiconsumo
    def crear_sesiones(self, proveedores:dict):
        for proveedor in proveedores.values():
            if ',' not in proveedor.nombre:    
                print(self.sesiones)
                print(proveedor.nombre)
                print(self.sesiones.keys())
                if proveedor.nombre not in self.sesiones.keys():
                    if 'MAXICONSUMO' in proveedor.nombre:
                        sesion = Sesion_Maxiconsumo(proveedor.username, proveedor.password)
                    elif 'BEES' in proveedor.nombre:
                        sesion = Sesion_Bees(proveedor.username, proveedor.password)
                    elif 'ANDINA' in proveedor.nombre:
                        sesion = Sesion_Andina(proveedor.username, proveedor.password)
                    elif 'LA SERENISIMA' in proveedor.nombre:
                        sesion = Sesion_La_Serenisima(proveedor.username, proveedor.password)
                    else:
                        sesion = Sesion_Oscar_David()

                    self.sesiones[proveedor.nombre] = sesion
                      
    def crear_sesion_manual(self, proveedor:str, sess_id):
        if 'MAXICONSUMO' in proveedor:
            sesion = Sesion_Maxiconsumo(username='', password='')
            sesion.cookies['PHPSESSID'] = sess_id
        elif 'BEES' in proveedor:
            sesion = Sesion_Bees(username='', password='')
            sesion.cookies['connect.sid'] = sess_id
        elif 'ANDINA' in proveedor:
            sesion = Sesion_Andina(username='', password='')
            sesion.cookies['PHPSESSID'] = sess_id
        elif 'LA SERENISIMA' in proveedor:
            sesion = Sesion_La_Serenisima(username='', password='')
            sesion.cookies['session.id'] = sess_id
        else:
            sesion = Sesion_Oscar_David()
            sesion.cookies['PHPSESSID'] = sess_id


        sesion.sess_id = sess_id
        self.sesiones[proveedor] = sesion

    def abrir_sesiones(self):
        for sesion in self.sesiones.values():
            print(f'ABRIENDO SESIÓN DE {sesion.proveedor}')
            if sesion.sess_id == '':
                sesion.abrir_sesion(self.driver)
        self.driver.close()

    
