from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os
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
    def crear_sesiones(self, proveedores:list):
        for proveedor in proveedores:
            if ',' not in proveedor.nombre:    
                if 'MAXICONSUMO' in proveedor.nombre:
                    sesion = Sesion_Maxiconsumo(proveedor.username, proveedor.password)
                elif 'JOSE ESTEBAN PANELLA' in proveedor.nombre or 'SANTO GUILIANO' in proveedor.nombre:
                    sesion = Sesion_Bees(proveedor.username, proveedor.password)
                elif 'DISTRIBUIDORA ANDINA' in proveedor.nombre or 'ANDINA SRL' in proveedor.nombre:
                    sesion = Sesion_Andina(proveedor.username, proveedor.password)
                elif 'LA SERENISIMA' in proveedor.nombre:
                    sesion = Sesion_La_Serenisima(proveedor.username, proveedor.password)
                else:
                    sesion = Sesion_Oscar_David()

                self.sesiones[proveedor.proveedor] = sesion
            
        return self.sesiones
                    