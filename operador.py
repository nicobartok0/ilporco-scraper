from valuador import Valuador_Andina, Valuador_Maxiconsumo, Valuador_Oscar_David
from lector import Lector
from tkinter import *
from tkinter import ttk
import os

class Operador:
    def __init__(self, maxiconsumo_sess_id, andina_sess_id, oscar_david_sess_id, nombre_excel):
        self.nombre_excel = nombre_excel
        self.scanner = Lector(nombre_excel)
        self.valuador_maxiconsumo = Valuador_Maxiconsumo(maxiconsumo_sess_id)
        self.valuador_andina = Valuador_Andina(andina_sess_id)
        self.valuador_oscar_david = Valuador_Oscar_David(oscar_david_sess_id)


    def actualizar_precios(self, progress, nuevonombre, progresswindow, currentarticle):
        
        
        self.contador = 0
        self.maxiconsumo, self.andina, self.oscar_david, self.nodata = self.scanner.separar_por_proveedor()
        self.andina = self.scanner.intercode_andina(self.andina)
        self.oscar_david = self.scanner.intercode_od(self.oscar_david)
        self.maxiconsumo = self.valuador_maxiconsumo.get_prices(self.maxiconsumo, progress, currentarticle)
        self.andina = self.valuador_andina.get_prices(self.andina, progress, self.valuador_maxiconsumo.contador, currentarticle)
        self.oscar_david = self.valuador_oscar_david.get_prices(self.oscar_david, progress, self.valuador_andina.contador, currentarticle)
        self.scanner.actualizar_precios(self.maxiconsumo, self.andina, self.oscar_david)
        os.system(f'start excel.exe "{os.getcwd()}/archivos/{nuevonombre}"')
        progresswindow.destroy()


    def cantidad_datos(self):
        self.datos_totales = self.scanner.obtener_datos()
        return len(self.datos_totales) - 1
