from valuador import Valuador_Andina, Valuador_Maxiconsumo, Valuador_Oscar_David, Valuador_La_Serenisima, Valuador_Bees
from lector2 import Lector
from proveedor import Proveedor
from sesionador2 import Sesionador
from tkinter import *
from tkinter import ttk
import os

class Operador:
    def __init__(self, name, ruta):
        self.lector = Lector(name, ruta)
        self.sesionador = Sesionador()
        self.proveedores = {}

    def crear_proveedores(self, credentials):
        nom_proveedores = self.lector.obtener_proveedores()
        for nombre in nom_proveedores:
            if nombre == 'MAXICONSUMO':
                proveedor = Proveedor(nombre='MAXICONSUMO',usuario=credentials['MAXICONSUMO'][0], password=credentials['MAXICONSUMO'][1])
            elif 'OSCAR DAVID' in nombre:
                proveedor = Proveedor(nombre='OSCAR DAVID',usuario=credentials['OSCAR DAVID'][0], password=credentials['OSCAR DAVID'][1])
            elif 'DISTRIBUIDORA ANDINA' in nombre or 'ANDINA SRL' in nombre:
                proveedor = Proveedor(nombre='ANDINA',usuario=credentials['ANDINA'][0], password=credentials['ANDINA'][1])
            elif 'LA SERENISIMA' in nombre:
                proveedor = Proveedor(nombre='LA SERENISIMA',usuario=credentials['LA SERENISIMA'][0], password=credentials['LA SERENISIMA'][1])
            elif 'PANELLA' in nombre or 'SANTO GUILIANO' in nombre:
                proveedor = Proveedor(nombre='BEES',usuario=credentials['BEES'][0], password=credentials['BEES'][1])
            else:
                proveedor = Proveedor(nombre=f'DESCONOCIDO - {nombre}', usuario='', password='')
            self.proveedores[nombre] = proveedor