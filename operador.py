from valuador import Valuador_Andina, Valuador_Maxiconsumo, Valuador_Oscar_David, Valuador_La_Serenisima
from lector import Lector
from tkinter import *
from tkinter import ttk
import os

class Operador:
    def __init__(self, maxiconsumo_sess_id, andina_sess_id, oscar_david_sess_id, la_serenisima_sess_id,nombre_excel):
        self.nombre_excel = nombre_excel
        self.scanner = Lector(nombre_excel)
        self.valuador_maxiconsumo = Valuador_Maxiconsumo(maxiconsumo_sess_id)
        self.valuador_andina = Valuador_Andina(andina_sess_id)
        self.valuador_oscar_david = Valuador_Oscar_David(oscar_david_sess_id)
        self.valuador_serenisima = Valuador_La_Serenisima(la_serenisima_sess_id)


    def actualizar_precios(self, progress, nuevonombre, progresswindow, currentarticle):
        
        
        self.contador = 0
        self.maxiconsumo, self.andina, self.oscar_david, self.la_serenisima, self.nodata = self.scanner.separar_por_proveedor()
        self.andina = self.scanner.intercode_andina(self.andina)
        self.oscar_david = self.scanner.intercode_od(self.oscar_david)
        self.la_serenisima = self.scanner.intercode_serenisima(self.la_serenisima)
        self.maxiconsumo = self.valuador_maxiconsumo.get_prices(self.maxiconsumo, progress, currentarticle)
        self.andina = self.valuador_andina.get_prices(self.andina, progress, self.valuador_maxiconsumo.contador, currentarticle)
        self.oscar_david = self.valuador_oscar_david.get_prices(self.oscar_david, progress, self.valuador_andina.contador, currentarticle)
        self.la_serenisima = self.valuador_serenisima.get_prices(self.la_serenisima, progress, self.valuador_oscar_david.contador, currentarticle)
        self.scanner.actualizar_precios(self.maxiconsumo, self.andina, self.oscar_david, self.la_serenisima)
        os.system(f'start excel.exe "{os.getcwd()}\\archivos\\{nuevonombre}"')
        progresswindow.destroy()

    def actualizar_precios_doble(self, progress, nuevonombre, progresswindow, currentarticle):
        
        
        self.contador = 0
        self.maxiconsumo, self.andina, self.oscar_david, self.la_serenisima, self.nodata = self.scanner.separar_por_proveedor()
        self.andina = self.scanner.intercode_andina(self.andina)
        self.oscar_david = self.scanner.intercode_od(self.oscar_david)
        self.la_serenisima = self.scanner.intercode_serenisima(self.la_serenisima)
        self.maxiconsumo = self.valuador_maxiconsumo.get_prices(self.maxiconsumo, progress, currentarticle)
        
        # Creamos una lista de los artículos de Maxiconsumo sin precio para después buscarlos en Oscar David

        maxiconsumo_sinprecio = {}
        for key in self.maxiconsumo.keys():
            if self.maxiconsumo[key][4] == 'Sin precio':
                maxiconsumo_sinprecio[key] = self.maxiconsumo[key]

        self.andina = self.valuador_andina.get_prices(self.andina, progress, self.valuador_maxiconsumo.contador, currentarticle)
        self.oscar_david = self.valuador_oscar_david.get_prices(self.oscar_david, progress, self.valuador_andina.contador, currentarticle)
        self.la_serenisima = self.valuador_serenisima.get_prices(self.la_serenisima, progress, self.valuador_oscar_david.contador, currentarticle)

        # Buscamos los artículos extra en Oscar David
        maxiconsumo_sinprecio = self.scanner.intercode_maxi(maxiconsumo_sinprecio)
        currentarticle.set('BUSCANDO PRECIOS NULOS EN OSCAR DAVID...')
        maxiconsumo_sinprecio = self.valuador_oscar_david.get_prices_simple(maxiconsumo_sinprecio)
        
        # Añadimos los artículos extra al diccionario de Maxiconsumo
        for key in maxiconsumo_sinprecio.keys():
            self.maxiconsumo[key] = maxiconsumo_sinprecio[key]
        
        

        self.scanner.actualizar_precios(self.maxiconsumo, self.andina, self.oscar_david, self.la_serenisima)
        os.system(f'start excel.exe "{os.getcwd()}\\archivos\\{nuevonombre}"')
        progresswindow.destroy()


    def cantidad_datos(self):
        self.datos_totales = self.scanner.obtener_datos()
        return len(self.datos_totales) - 1
