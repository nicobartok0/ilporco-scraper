from lector import Lector
from valuador import Valuador_Maxiconsumo
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys, os


# Se genera el elemento base de tkinter
root = Tk()
root.geometry("500x200")
root.title('Il Porco Scraper')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.grid()

# Definimos las variables que capturan los datos de las entries.
sess_id_label = tk.StringVar()
nombre_label = tk.StringVar()


# Creamos la función que el botón de "Iniciar Búsqueda de precios" ejecutará
def boton():
    progresswindow = Toplevel(root)
    progresswindow.title('Progreso')
    progresswindow.geometry('200x200')
    ttk.Label(progresswindow, text='Espere mientras se buscan los datos...').grid(column=0, row=0)
    barra = ttk.Progressbar(progresswindow, mode='determinate')
    barra.grid(column=0, row=1, padx=10, pady=10)

    # Hacemos un scanner del excel y le damos el nombre del archivo.
    scanner = Lector(str(nombre_label.get()))

    # Obtenemos la lista de SKUs y Nombres de los artículos a través del Scanner.
    skus = scanner.obtener_skus()

    # Hacemos un valuador y le damos el id de sesión de Maxiconsumo
    valuador = Valuador_Maxiconsumo(sess_id=str(sess_id_label.get()), sku_list=skus)

    # Obtenemos los precios usando el valuador
    precios = valuador.get_prices(progressbar=barra, progresswindow=progresswindow)
    scanner.actualizar_precios(precios)
    progresswindow.destroy()
    nuevonombre= f'{str(nombre_label.get())}-ACTUALIZADO.xlsx'
    os.system(f'start excel.exe "{os.getcwd()}/{nuevonombre}"')
    

# -- Creación de widgets
    
# Creamos las labels de texto
ttk.Label(frame, text="Il Porco Scraper").grid(column=0, row=0)
ttk.Label(frame, text='Ingrese el ID de Sesión: ').grid(column=0, row=1)
ttk.Label(frame, text='Ingrese el nombre del libro de Excel: ').grid(column=0, row=2)

# Creamos las entries y les asignamos las variables que ya creamos
ttk.Entry(frame, textvariable=sess_id_label).grid(column=1, row=1, pady=10)
ttk.Entry(frame, textvariable=nombre_label).grid(column=1, row=2, pady=10)

# Creamos los botones con sus respectivos comandos (salir del programa y iniciar búsqueda)
ttk.Button(frame, text="Salir", command=root.destroy).grid(column=0, row=3)
ttk.Button(frame, text='Iniciar Búsqueda de precios', command=boton).grid(column=1, row=3)

# Activamos el loop principal 
if __name__ == '__main__':
    root.mainloop()


