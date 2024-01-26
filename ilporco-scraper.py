from operador import Operador
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os


# Se genera el elemento base de tkinter
root = Tk()
root.geometry("500x200")
root.title('Il Porco Scraper 2.0')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.grid()

# Definimos las variables que capturan los datos de las entries.
sess_id_label = tk.StringVar()
nombre_label = tk.StringVar()


# Creamos la función que el botón de "Iniciar Búsqueda de precios" ejecutará
def boton():
    progresswindow = Toplevel(root)
    progresswindow.update_idletasks()
    progresswindow.title('Progreso')
    progresswindow.geometry('420x100')
    ttk.Label(progresswindow, text='Espere mientras se buscan los datos...').grid(column=0, row=0)
    nuevonombre= f'{str(nombre_label.get())}-ACTUALIZADO.xlsx'
    progress = IntVar()
    # Creamos un operador de precios y le damos el session id y el nombre del archivo excel
    operador = Operador(maxiconsumo_sess_id=str(sess_id_label.get()), nombre_excel=str(nombre_label.get()))
    barra = ttk.Progressbar(progresswindow, max=float(operador.cantidad_datos()), length=400, variable=progress)
    barra.grid(column=0, row=1, padx=10, pady=10)

    # Ejecutamos la obtención de precios desde el operador
    
    operador.actualizar_precios(progress, progresswindow)
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


