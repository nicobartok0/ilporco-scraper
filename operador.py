from valuador import Valuador_Andina, Valuador_Maxiconsumo
from lector import Lector
from tkinter import *
from tkinter import ttk
import os

class Operador:
    def __init__(self, maxiconsumo_sess_id, nombre_excel):
        self.nombre_excel = nombre_excel
        self.scanner = Lector(nombre_excel)
        self.valuador_maxiconsumo = Valuador_Maxiconsumo(maxiconsumo_sess_id)
        self.valuador_andina = Valuador_Andina()

    def actualizar_precios(self, progress, nuevonombre, progresswindow):
        
        
        self.contador = 0
        self.maxiconsumo, self.andina, self.nodata = self.scanner.separar_por_proveedor()
        self.andina = self.scanner.intercode_andina(self.andina)
        self.maxiconsumo = self.valuador_maxiconsumo.get_prices(self.maxiconsumo, progress)
        self.andina = self.valuador_andina.get_prices(self.andina, progress, contador=self.valuador_maxiconsumo.contador)
        self.scanner.actualizar_precios(self.maxiconsumo, self.andina)
        os.system(f'start excel.exe "{os.getcwd()}/{nuevonombre}"')
        progresswindow.destroy()


    def cantidad_datos(self):
        self.datos_totales = self.scanner.obtener_datos()
        return len(self.datos_totales) - 1
