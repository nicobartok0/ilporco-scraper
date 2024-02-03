from operador import Operador
import tkinter as tk
from tkinter import *
from tkinter import ttk
from threading import Thread

# Se genera el elemento base de tkinter
root = Tk()
root.geometry("600x220")
root.title('Il Porco Scraper 3.1')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.grid()

# Definimos las variables que capturan los datos de las entries.
maxi_id_label = tk.StringVar()
od_id_label = tk.StringVar()
nombre_label = tk.StringVar()
currentarticle = tk.StringVar()


# Creamos la función que el botón de "Iniciar Búsqueda de precios" ejecutará
def boton():
    progresswindow = Toplevel(root)
    
    progresswindow.title('Progreso')
    progresswindow.geometry('420x100')
    ttk.Label(progresswindow, text='Espere mientras se buscan los datos...').grid(column=0, row=0)
    nuevonombre= f'{str(nombre_label.get())}-ACTUALIZADO.xlsx'
    progress = IntVar()
    # Creamos un operador de precios y le damos el session id y el nombre del archivo excel
    operador = Operador(maxiconsumo_sess_id=str(maxi_id_label.get()), oscar_david_sess_id=str(od_id_label.get()), nombre_excel=str(nombre_label.get()))
    barra = ttk.Progressbar(progresswindow, max=float(operador.cantidad_datos()), length=400, variable=progress)
    barra.grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(progresswindow, textvariable=currentarticle).grid(column=0, row=2)

    # Ejecutamos la obtención de precios desde el operador en un hilo aparte

    hilo_operador = Thread(target=operador.actualizar_precios, args=(progress,nuevonombre== f'{str(nombre_label.get())}-ACTUALIZADO.xlsx', progresswindow, currentarticle), daemon=True)
    hilo_operador.start()
    

# -- Creación de widgets
    
# Creamos las labels de texto
ttk.Label(frame, text="Il Porco Scraper").grid(column=0, row=0)
ttk.Label(frame, text='Ingrese el ID de Sesión de Maxiconsumo: ').grid(column=0, row=1)
ttk.Label(frame, text='Ingrese el ID de Sesión de Oscar David: ').grid(column=0, row=2)
ttk.Label(frame, text='Ingrese el nombre del libro de Excel: ').grid(column=0, row=3)
disclaimer = ttk.Label(frame, text='* Versión funcional con distribuidores: Maxiconsumo, Andina y Oscar David')
disclaimer.grid(column=0, row=5, pady=20)
disclaimer.config(font=("Courier", 6))
disclaimer.config(foreground='gray')

# Creamos las entries y les asignamos las variables que ya creamos
ttk.Entry(frame, textvariable=maxi_id_label).grid(column=1, row=1, pady=10)
ttk.Entry(frame, textvariable=od_id_label).grid(column=1, row=2, pady=10)
ttk.Entry(frame, textvariable=nombre_label).grid(column=1, row=3, pady=10)

# Creamos los botones con sus respectivos comandos (salir del programa y iniciar búsqueda)
ttk.Button(frame, text="Salir", command=root.destroy).grid(column=0, row=4)
ttk.Button(frame, text='Iniciar Búsqueda de precios', command=boton).grid(column=1, row=4)

# Activamos el loop principal 
if __name__ == '__main__':
    root.mainloop()


