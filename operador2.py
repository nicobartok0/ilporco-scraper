from valuador2 import Valuador
from lector2 import Lector
from proveedor import Proveedor
from sesionador2 import Sesionador
from articulo import Articulo
from tkinter import *
from tkinter import ttk
import os
from sesionador2 import Sesionador

class Operador:
    def __init__(self):
        self.proveedores = {}
        self.articulos = []
        self.sesionador = Sesionador()

    def cargar_componentes(self, name, ruta):
        self.lector = Lector(name, ruta)
        

    def crear_proveedores(self, credentials):
        nom_proveedores = self.lector.obtener_proveedores()
        for nombre in nom_proveedores:
            if nombre == 'MAXICONSUMO':
                proveedor = Proveedor(nombre='MAXICONSUMO',usuario=credentials['MAXICONSUMO'][0], password=credentials['MAXICONSUMO'][1])
                dist = 'MAXICONSUMO'
            elif 'OSCAR DAVID' in nombre:
                proveedor = Proveedor(nombre='OSCAR DAVID',usuario=credentials['OSCAR DAVID'][0], password=credentials['OSCAR DAVID'][1])
                dist = 'OSCAR DAVID'
            elif 'DISTRIBUIDORA ANDINA' in nombre or 'ANDINA SRL' in nombre:
                proveedor = Proveedor(nombre='ANDINA',usuario=credentials['ANDINA'][0], password=credentials['ANDINA'][1])
                dist = 'ANDINA'
            elif 'LA SERENISIMA' in nombre:
                proveedor = Proveedor(nombre='LA SERENISIMA',usuario=credentials['LA SERENISIMA'][0], password=credentials['LA SERENISIMA'][1])
                dist = 'LA SERENISIMA'
            elif 'PANELLA' in nombre or 'SANTO GUILIANO' in nombre:
                proveedor = Proveedor(nombre='BEES',usuario=credentials['BEES'][0], password=credentials['BEES'][1])
                dist = 'BEES'
            else:
                proveedor = Proveedor(nombre=f'DESCONOCIDO - {nombre}', usuario='', password='')
                dist = ''
            self.proveedores[dist] = proveedor



    def crear_articulos(self):
        articulos = self.lector.obtener_datos()
        articulos.pop(0)
        for articulo_dict in articulos:
            if articulo_dict['proveedor'] == 'MAXICONSUMO':
                articulo = Articulo(self.proveedores['MAXICONSUMO'])
            elif 'OSCAR DAVID' in articulo_dict['proveedor']:
                articulo = Articulo(self.proveedores['OSCAR DAVID'])
            elif 'ANDINA' in articulo_dict['proveedor'] or articulo_dict['proveedor'] == 'ANDINA':
                articulo = Articulo(self.proveedores['ANDINA'])
            elif 'LA SERENISIMA' in articulo_dict['proveedor']:
                articulo = Articulo(self.proveedores['LA SERENISIMA'])
            elif 'BEES' in articulo_dict['proveedor']:
                articulo = Articulo(self.proveedores['BEES'])
            else:
                articulo = Articulo(self.proveedores['MAXICONSUMO'])
            articulo.nombre = articulo_dict['nombre']
            articulo.sku = articulo_dict['SKU']
            articulo.fecha = articulo_dict['fecha']
            articulo.codigo = articulo_dict['codigo']
            self.articulos.append(articulo)

    def inicializar(self, credentials, progresswindow):
        self.crear_proveedores(credentials=credentials)
        self.crear_articulos()
        progresswindow.event_generate("<<SetMaxArticles>>", when="tail")
        self.sesionador.crear_sesiones(self.proveedores)
        self.sesionador.abrir_sesiones()
        self.articulos = self.lector.intercode(self.articulos)
        self.valuador = Valuador(self.sesionador.sesiones, self.articulos, progresswindow)
        print('Llegué :D')
        self.valuador.obtener_precios()
        self.lector.actualizar_precios(self.articulos)
        progresswindow.event_generate("<<SearchFinished>>", when="tail")
            
    def abrir_sesion(self, proveedor, sess_id, window):
        self.sesionador.crear_sesion_manual(proveedor, sess_id)
        window.event_generate("<<SessionCreated>>", when='tail')
        
        