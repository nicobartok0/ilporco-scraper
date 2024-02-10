from operador import Operador
import tkinter as tk
from tkinter import *
from tkinter import ttk
from threading import Thread
from sesionador import Sesionador

# Se genera el elemento base de tkinter
root = Tk()
root.geometry("600x300")
root.title('Il Porco Scraper 3.5')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.grid()

# Definimos las variables que capturan los datos de las entries.
maxi_id_label = tk.StringVar()
andina_id_label = tk.StringVar()
od_id_label = tk.StringVar()
nombre_label = tk.StringVar()
currentarticle = tk.StringVar()
maxi_user = StringVar()
maxi_pswd = StringVar()

# Creamos la imagen de Il Porco que será usada como ícono de la aplicación.

logo = PhotoImage(file='assets/ilporcologo.png')
root.iconphoto(True, logo)

# Creamos la función que el botón de "Iniciar Búsqueda de precios" ejecutará
def boton():
    progresswindow = Toplevel(root)
    
    progresswindow.title('Progreso')
    progresswindow.geometry('420x100')
    ttk.Label(progresswindow, text='Espere mientras se buscan los datos...').grid(column=0, row=0)
    nuevonombre= f'{str(nombre_label.get())}-ACTUALIZADO.xlsx'
    progress = IntVar()
    # Creamos un operador de precios y le damos el session id y el nombre del archivo excel
    operador = Operador(maxiconsumo_sess_id=str(maxi_id_label.get()), andina_sess_id=str(andina_id_label.get()), oscar_david_sess_id=str(od_id_label.get()),  nombre_excel=str(nombre_label.get()))
    barra = ttk.Progressbar(progresswindow, max=float(operador.cantidad_datos()), length=400, variable=progress)
    barra.grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(progresswindow, textvariable=currentarticle).grid(column=0, row=2)

    # Ejecutamos la obtención de precios desde el operador en un hilo aparte
    nuevonombre = f'{str(nombre_label.get())}-ACTUALIZADO.xlsx'
    hilo_operador = Thread(target=operador.actualizar_precios, args=(progress,nuevonombre, progresswindow, currentarticle), daemon=True)
    hilo_operador.start()
    

# Creamos la función que el botón "Obtener sesiones" ejecutará.
def ventana_sesiones():
    sessionwindow = Toplevel(root)
    sessionwindow.title('Sesionador')
    sessionwindow.geometry('580x290')
    ttk.Label(sessionwindow, text='Sesionador de Il Porco Scraper').grid(column=1, row=0)
    ttk.Label(sessionwindow, text='Credenciales de Maxiconsumo').grid(column=1, row=1, pady=10)
    ttk.Label(sessionwindow, text='Correo Electrónico: ').grid(column=0, row=2, pady=10)
    ttk.Label(sessionwindow, text='Contraseña: ').grid(column=0, row=3, pady=10)
    ttk.Entry(sessionwindow, textvariable=maxi_user).grid(column=1, row=2, pady=10)
    ttk.Entry(sessionwindow, textvariable=maxi_pswd, show='*').grid(column=1, row=3, pady=10)
    ttk.Button(sessionwindow, text='Abrir sesiones', command=lambda: sesionar(sessionwindow)).grid(column=1, row=4, pady=10)
    disclaimer2 = ttk.Label(sessionwindow, text='* La sesión de Oscar David debe ser abierta de forma manual')
    disclaimer2.grid(column=0, row=5, pady=20)
    disclaimer2.config(font=("Courier", 6))
    disclaimer2.config(foreground='black')

# Creamos la función que el botón "Abrir sesiones" ejecutará (En la que se obtienen los id de sesión)
def sesionar(sessionwindow):
    sesionador = Sesionador()
    maxi_sess_id = sesionador.sesionar_maxiconsumo(user=maxi_user.get(), pswd=maxi_pswd.get())
    andina_sess_id = sesionador.sesionar_andina()
    maxi_id_label.set(maxi_sess_id)
    andina_id_label.set(andina_sess_id)
    sessionwindow.destroy()

# -- Creación de widgets
    
# Creamos las labels de texto
ttk.Label(frame, text="Il Porco Scraper").grid(column=0, row=0)
ttk.Label(frame, text='Ingrese el ID de Sesión de Maxiconsumo: ').grid(column=0, row=1)
ttk.Label(frame, text='Ingrese el ID de Andina: ').grid(column=0, row=2)
ttk.Label(frame, text='Ingrese el ID de Sesión de Oscar David: ').grid(column=0, row=3)
ttk.Label(frame, text='Ingrese el nombre del libro de Excel: ').grid(column=0, row=4)
disclaimer = ttk.Label(frame, text='* Versión funcional con distribuidores: Maxiconsumo, Andina y Oscar David')
disclaimer.grid(column=0, row=6, pady=20)
disclaimer.config(font=("Courier", 6))
disclaimer.config(foreground='black')

# Creamos las entries y les asignamos las variables que ya creamos
ttk.Entry(frame, textvariable=maxi_id_label).grid(column=1, row=1, pady=10)
ttk.Entry(frame, textvariable=andina_id_label).grid(column=1, row=2, pady=10)
ttk.Entry(frame, textvariable=od_id_label).grid(column=1, row=3, pady=10)
ttk.Entry(frame, textvariable=nombre_label).grid(column=1, row=4, pady=10)

# Creamos los botones con sus respectivos comandos (salir del programa y iniciar búsqueda)
ttk.Button(frame, text='Obtener sesiones', command=ventana_sesiones).grid(column=1, row=0)
ttk.Button(frame, text="Salir", command=root.destroy).grid(column=0, row=5)
ttk.Button(frame, text='Iniciar Búsqueda de precios', command=boton).grid(column=1, row=5)

# Activamos el loop principal 
if __name__ == '__main__':
    root.mainloop()


