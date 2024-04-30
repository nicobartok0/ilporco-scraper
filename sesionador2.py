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
        sys.path.insert(0,chromedriver_path)
        if os.name != 'posix': 
            self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        else:
            self.driver = webdriver.Chrome()
        self.sesiones = {}

    # Definimos la función en la que buscaremos el id de sesión de Maxiconsumo
    def crear_sesiones(self, proveedores:dict):
        for proveedor in proveedores.values():
            if ',' not in proveedor.nombre:    
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

                if self.sesiones[proveedor.nombre] != sesion: 
                    self.sesiones[proveedor.nombre] = sesion
                    
    def crear_sesion_manual(self, proveedor:str, sess_id):
        if 'MAXICONSUMO' in proveedor:
            sesion = Sesion_Maxiconsumo(username='', password='')
        elif 'BEES' in proveedor:
            sesion = Sesion_Bees(username='', password='')
        elif 'ANDINA' in proveedor:
            sesion = Sesion_Andina(username='', password='')
        elif 'LA SERENISIMA' in proveedor:
            sesion = Sesion_La_Serenisima(username='', password='')
        else:
            sesion = Sesion_Oscar_David()

        sesion.sess_id = sess_id
        self.sesiones[proveedor] = sesion

    def abrir_sesiones(self):
        for sesion in self.sesiones.values():
            print(f'ABRIENDO SESIÓN DE {sesion.proveedor}')
            sesion.abrir_sesion(self.driver)
        self.driver.close()

    
