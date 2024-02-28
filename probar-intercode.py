from valuador import Valuador_Maxiconsumo, Valuador_Oscar_David
from operador import Operador
from lector import Lector
import tkinter as tk
from tkinter import *


root = Tk()
progress = tk.StringVar()
currentarticle = tk.StringVar()

scanner = Lector('maxi-od-mini')
articulos = scanner.obtener_datos()
maxiconsumo, oscar_david, andina, la_serenisima, no_data = scanner.separar_por_proveedor()

valuador_maxi = Valuador_Maxiconsumo('f8faaed0a2523aa95d98dbb38b25ba15')
valuador_od = Valuador_Oscar_David('34a3c6516aa3d98daf1cd24bf507d6de')
#operador = Operador(maxiconsumo_sess_id='f8faaed0a2523aa95d98dbb38b25ba15',andina_sess_id='',oscar_david_sess_id='34a3c6516aa3d98daf1cd24bf507d6de',la_serenisima_sess_id='',nombre_excel='maxi-od-mini')
#operador.actualizar_precios_doble(progress=progress, progresswindow=progresswindow, nuevonombre='maxi-od-mini-actualizado', currentarticle=currentarticle)

maxiconsumo = valuador_maxi.get_prices(maxiconsumo=maxiconsumo, progress=progress, currentarticle=currentarticle)

maxiconsumo_sinprecio = {}
for key in maxiconsumo.keys():
    if maxiconsumo[key][4] == 'Sin precio':
        maxiconsumo_sinprecio[key] = maxiconsumo[key]

maxiconsumo_sinprecio = scanner.intercode_maxi(maxiconsumo_sinprecio)
print(maxiconsumo_sinprecio)
print('\n')
valuador_od.get_prices_simple(maxiconsumo_sinprecio)
print(maxiconsumo_sinprecio)
root.mainloop()