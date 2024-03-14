from operador import Operador
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from threading import Thread

root = Tk()
window = Toplevel(root)


progress = tk.IntVar()
nuevonombre = tk.StringVar()
currentarticle = tk.StringVar()


operador = Operador(maxiconsumo_sess_id='1780e5a989e154a1bc7eac702d9d4bc9', oscar_david_sess_id='fdac2342c0c353ce5452f18a6f8a88f4', andina_sess_id='8fee84a78135b6b3a451b56b6a2109a5', la_serenisima_sess_id='207cd87189d3b3e01ff77f29b5c8d5e55971b33d', nombre_excel='maxi-od-3', ruta=f'{os.getcwd()}/archivos/maxi-od-3.xlsx')
operador.actualizar_precios(progress, nuevonombre, window, currentarticle)
Thread(target=operador.actualizar_precios, args=(progress, nuevonombre, window, currentarticle), daemon=True)
print(currentarticle.get())
root.mainloop()