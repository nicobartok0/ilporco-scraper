from operador import Operador
from lector import Administrador_de_credenciales, Administrador_Intermedia
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.filedialog
from threading import Thread
from sesionador import Sesionador
import os

# Se genera el elemento base de tkinter
root = Tk()
root.geometry("780x390")
root.title('Il Porco Scraper 5.0')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.grid()

# Definimos las variables que capturan los datos de las entries.
maxi_id_label = tk.StringVar()
andina_id_label = tk.StringVar()
od_id_label = tk.StringVar()
serenisima_id_label = tk.StringVar()
bees_alv_id_label = StringVar()
bees_sr_id_label = StringVar()
nombre_label = tk.StringVar()
currentarticle = tk.StringVar()
maxi_user = StringVar()
maxi_pswd = StringVar()
sere_user = StringVar()
sere_pswd = StringVar()
bees_alv_user = StringVar()
bees_alv_pswd = StringVar()
bees_sr_user = StringVar()
bees_sr_pswd = StringVar()
busqueda = BooleanVar()
new_mu = tk.StringVar()
new_mp = tk.StringVar()
new_su = tk.StringVar()
new_sp = tk.StringVar()
new_bau = tk.StringVar()
new_bap = tk.StringVar()
new_bsu = tk.StringVar()
new_bsp = tk.StringVar()
ti_sku = tk.StringVar()
ti_ilporco = tk.StringVar()
ti_nombre = tk.StringVar()
ti_codigo = tk.StringVar()
ruta = tk.StringVar()

# Creamos la imagen de Il Porco que será usada como ícono de la aplicación.

logo = PhotoImage(file='assets/ilporcologo.png')
search = PhotoImage(file='assets/search.png')
search = search.subsample(25, 25)
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
    global operador
    operador = Operador(maxiconsumo_sess_id=str(maxi_id_label.get()), andina_sess_id=str(andina_id_label.get()), oscar_david_sess_id=str(od_id_label.get()), la_serenisima_sess_id=str(serenisima_id_label.get()), bees_alv_sess_id=str(bees_alv_id_label.get()), bees_sr_sess_id=str(bees_sr_id_label.get()), nombre_excel=str(nombre_label.get()), ruta=ruta.get())
    barra = ttk.Progressbar(progresswindow, max=float(operador.cantidad_datos()), length=400, variable=progress)
    barra.grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(progresswindow, textvariable=currentarticle).grid(column=0, row=2)

    # Ejecutamos la obtención de precios desde el operador en un hilo aparte
    nuevonombre = f'{str(nombre_label.get())}-ACTUALIZADO.xlsx'
    if busqueda.get() == False:
        hilo_operador = Thread(target=operador.actualizar_precios, args=(progress,nuevonombre, progresswindow, currentarticle), daemon=True)
        hilo_operador.start()
    else:
        hilo_operador = Thread(target=operador.actualizar_precios_doble, args=(progress,nuevonombre, progresswindow, currentarticle), daemon=True)
        hilo_operador.start()

    
    

# Creamos la función que el botón "Obtener sesiones" ejecutará.
def ventana_sesiones():
    sessionwindow = Toplevel(root)
    sessionwindow.title('Sesionador')
    sessionwindow.geometry('580x560')
    ttk.Label(sessionwindow, text='Sesionador de Il Porco Scraper').grid(column=1, row=0)
    ttk.Label(sessionwindow, text='Credenciales de Maxiconsumo').grid(column=1, row=1, pady=10)
    ttk.Label(sessionwindow, text='Correo Electrónico: ').grid(column=0, row=2, pady=10)
    ttk.Label(sessionwindow, text='Contraseña: ').grid(column=0, row=3, pady=10)
    ttk.Label(sessionwindow, text='Credenciales de La Serenísima').grid(column=1, row=4, pady=10)
    ttk.Label(sessionwindow, text='Correo Electrónico: ').grid(column=0, row=5, pady=10)
    ttk.Label(sessionwindow, text='Contraseña: ').grid(column=0, row=6, pady=10)
    ttk.Label(sessionwindow, text='Credenciales de Bees (Gral. Alvear)').grid(column=1, row=7, pady=10)
    ttk.Label(sessionwindow, text='Correo Electrónico: ').grid(column=0, row=8, pady=10)
    ttk.Label(sessionwindow, text='Contraseña: ').grid(column=0, row=9, pady=10)
    ttk.Label(sessionwindow, text='Credenciales de Bees (San Rafael)').grid(column=1, row=10, pady=10)
    ttk.Label(sessionwindow, text='Correo Electrónico: ').grid(column=0, row=11, pady=10)
    ttk.Label(sessionwindow, text='Contraseña: ').grid(column=0, row=12, pady=10)
    ttk.Entry(sessionwindow, textvariable=maxi_user).grid(column=1, row=2, pady=10)
    ttk.Entry(sessionwindow, textvariable=maxi_pswd, show='*').grid(column=1, row=3, pady=10)
    ttk.Entry(sessionwindow, textvariable=sere_user).grid(column=1, row=5, pady=10)
    ttk.Entry(sessionwindow, textvariable=sere_pswd, show='*').grid(column=1, row=6, pady=10)
    ttk.Entry(sessionwindow, textvariable=bees_alv_user).grid(column=1, row=8, pady=10)
    ttk.Entry(sessionwindow, textvariable=bees_alv_pswd, show='*').grid(column=1, row=9, pady=10)
    ttk.Entry(sessionwindow, textvariable=bees_sr_user).grid(column=1, row=11, pady=10)
    ttk.Entry(sessionwindow, textvariable=bees_sr_pswd, show='*').grid(column=1, row=12, pady=10)
    
    ttk.Button(sessionwindow, text='Abrir sesiones', command=lambda: sesionar(sessionwindow)).grid(column=1, row=13, pady=10)
    disclaimer2 = ttk.Label(sessionwindow, text='* La sesión de Oscar David debe ser abierta de forma manual')
    disclaimer2.grid(column=0, row=14, pady=20)
    disclaimer2.config(font=("Courier", 6))
    disclaimer2.config(foreground='black')

# Creamos la función que el botón "Abrir sesiones" ejecutará (En la que se obtienen los id de sesión)
def sesionar(sessionwindow):
    sesionador = Sesionador()
    maxi_sess_id = sesionador.sesionar_maxiconsumo(user=maxi_user.get(), pswd=maxi_pswd.get())
    andina_sess_id = sesionador.sesionar_andina()
    serenisima_sess_id = sesionador.sesionar_serenisima(user=sere_user.get(), pswd=sere_pswd.get())
    bees_alv_sess_id = sesionador.sesionar_bees(user=bees_alv_user.get(), pswd=bees_alv_pswd.get())
    bees_sr_sess_id = sesionador.sesionar_bees(user=bees_sr_user.get(), pswd=bees_sr_pswd.get())
    sesionador.driver.quit()
    maxi_id_label.set(maxi_sess_id)
    andina_id_label.set(andina_sess_id)
    serenisima_id_label.set(serenisima_sess_id)
    bees_alv_id_label.set(bees_alv_sess_id)
    bees_sr_id_label.set(bees_sr_sess_id)
    sessionwindow.destroy()

# Creamos las funciones del menú de opciones
def cargar_credenciales():
    administrador = Administrador_de_credenciales()
    user1, pswd1, user2, pswd2, user3, pswd3, user4, pswd4 = administrador.obtener_credenciales()
    maxi_user.set(user1)
    maxi_pswd.set(pswd1)
    sere_user.set(user2)
    sere_pswd.set(pswd2)
    bees_alv_user.set(user3)
    bees_alv_pswd.set(pswd3)
    bees_sr_user.set(user4)
    bees_sr_pswd.set(pswd4)
    tkinter.messagebox.showinfo('Credenciales cargadas', 'Credenciales cargadas con éxito desde el archivo local')

def ventana_editar_credenciales():
    ventana_credenciales = tk.Toplevel(root)
    ventana_credenciales.geometry('500x390')
    ventana_credenciales.title('Edición de credenciales')
    ttk.Label(ventana_credenciales, text='Edición de credenciales').grid(column=1, row=0)
    ttk.Label(ventana_credenciales, text='Nuevo correo de Maxiconsumo: ').grid(column=0, row=1, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nueva contraseña de Maxiconsumo: ').grid(column=0, row=2, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nuevo correo de La Serenísima: ').grid(column=0, row=3, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nueva contraseña de La Serenísima: ').grid(column=0, row=4, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nuevo correo de Bees (Gral. Alvear): ').grid(column=0, row=5, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nueva contraseña Bees (Gral. Alvear): ').grid(column=0, row=6, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nuevo correo de Bees (San Rafael): ').grid(column=0, row=7, pady=10, padx=5)
    ttk.Label(ventana_credenciales, text='Nueva contraseña Bees (San Rafael): ').grid(column=0, row=8, pady=10, padx=5)
    ttk.Entry(ventana_credenciales, textvariable=new_mu).grid(column=2, row=1)
    ttk.Entry(ventana_credenciales, textvariable=new_mp, show='*').grid(column=2, row=2)
    ttk.Entry(ventana_credenciales, textvariable=new_su).grid(column=2, row=3)
    ttk.Entry(ventana_credenciales, textvariable=new_sp, show='*').grid(column=2, row=4)
    ttk.Entry(ventana_credenciales, textvariable=new_bau).grid(column=2, row=5)
    ttk.Entry(ventana_credenciales, textvariable=new_bap, show='*').grid(column=2, row=6)
    ttk.Entry(ventana_credenciales, textvariable=new_bsu).grid(column=2, row=7)
    ttk.Entry(ventana_credenciales, textvariable=new_bsp, show='*').grid(column=2, row=8)
    ttk.Button(ventana_credenciales, text='Editar credenciales', command=lambda: editar_credenciales(ventana_credenciales=ventana_credenciales)).grid(column=2, row=9, pady=10)
    


def editar_credenciales(ventana_credenciales):
    administrador = Administrador_de_credenciales()
    administrador.escribir_credenciales(maxi_user=new_mu.get(), maxi_pswd=new_mp.get(), sere_user=new_su.get(), sere_pswd=new_sp.get(), bees_alv_user=new_bau.get(), bees_alv_pswd=new_bap.get(), bees_sr_user=new_bsu.get(), bees_sr_pswd=new_bsp.get())
    tkinter.messagebox.showinfo('Credenciales Actualizadas', 'Las credenciales han sido actualizadas con éxito en su programa local.')
    ventana_credenciales.destroy()
    

def ventana_mod_tabla_intermedia():
    ventana_mod_ti = tk.Toplevel(root)
    ventana_mod_ti.geometry('670x100')
    ventana_mod_ti.title('Modificación de tabla intermedia')

    ttk.Label(ventana_mod_ti, text='SKU del Artículo').grid(column=0, row=1, padx=10)
    ttk.Label(ventana_mod_ti, text='Cód. de Il Porco').grid(column=1, row=1, padx=10)
    ttk.Label(ventana_mod_ti, text='Nombre del Artículo').grid(column=2, row=1, padx=10)
    ttk.Label(ventana_mod_ti, text='Cód. de Distribuidora').grid(column=3, row=1, padx=10)
    ttk.Entry(ventana_mod_ti, textvariable=ti_sku).grid(column=0, row=2, padx=10)
    ttk.Entry(ventana_mod_ti, textvariable=ti_ilporco).grid(column=1, row=2, padx=10)
    ttk.Entry(ventana_mod_ti, textvariable=ti_nombre).grid(column=2, row=2, padx=10)
    ttk.Entry(ventana_mod_ti, textvariable=ti_codigo).grid(column=3, row=2, padx=10)
    ttk.Button(ventana_mod_ti, command=lambda: añadir_tabla_intermedia(destino=proveedor.get()), text='Añadir artículo').grid(column=1, row=3, padx=10)
    ttk.Button(ventana_mod_ti, command=lambda: quitar_tabla_intermedia(destino=proveedor.get()), text='Eliminar artículo').grid(column=2, row=3, padx=10)
    proveedor = ttk.Combobox(ventana_mod_ti, values=['Andina', 'Oscar David', 'La Serenísima'])
    proveedor.current(0)
    proveedor.grid(column=3, row=3, padx=10)


def añadir_tabla_intermedia(destino):
    administrador_ti = Administrador_Intermedia()
    administrador_ti.añadir_articulo(sku=ti_sku.get(), ilporco=ti_ilporco.get(), nombre=ti_nombre.get(), codigo=ti_codigo.get(), destino=destino)
    tkinter.messagebox.showinfo(f'Artículo {ti_ilporco.get()} añadido con éxito',f'{ti_nombre.get()} añadido con éxito a {destino}')

def quitar_tabla_intermedia(destino):
    administrador_ti = Administrador_Intermedia()
    administrador_ti.quitar_articulo(codigo=ti_ilporco.get(), destino=destino)
    tkinter.messagebox.showinfo(f'Artículo {ti_ilporco.get()} eliminado con éxito', f'El artículo de código {ti_ilporco.get()} ha sido eliminado con éxito.')

def abrir_tabla_intermedia():
    os.system(f'start excel.exe "{os.getcwd()}\\assets\\tabla-intermedia.xlsx"')

def obtener_ruta():
    ruta.set(tkinter.filedialog.askopenfilename())
    index = ruta.get().split('/')
    nombre = index[-1]
    nombre = nombre[:-5]
    nombre_label.set(nombre)


def info():
    os.system(f'start {os.getcwd()}\\assets\\Instructivo-Scraper.pdf')

# -- Creación de widgets
    
# Creamos las labels de texto
ttk.Label(frame, text="Il Porco Scraper").grid(column=0, row=0)
ttk.Label(frame, text='Ingrese el ID de Sesión de Maxiconsumo: ').grid(column=0, row=1)
ttk.Label(frame, text='Ingrese el ID de Andina: ').grid(column=0, row=2)
ttk.Label(frame, text='Ingrese el ID de Sesión de Oscar David: ').grid(column=0, row=3)
ttk.Label(frame, text='Ingrese el ID de Sesión de La Serenísima: ').grid(column=0, row=4)
ttk.Label(frame, text='Ingrese el ID de Sesión de BEES (Alvear): ').grid(column=0, row=5)
ttk.Label(frame, text='Ingrese el ID de Sesión de BEES (San Rafael): ').grid(column=0, row=6)
ttk.Label(frame, text='Libro de EXCEL: ').grid(column=0, row=7)
disclaimer = ttk.Label(frame, text='* Versión funcional con distribuidores: Maxiconsumo, Andina, Oscar David, La Serenísima y BEES')
disclaimer.grid(column=0, row=10, pady=20)
disclaimer.config(font=("Courier", 6))
disclaimer.config(foreground='black')

# Creamos las entries y les asignamos las variables que ya creamos
ttk.Entry(frame, textvariable=maxi_id_label).grid(column=1, row=1, pady=10)
ttk.Entry(frame, textvariable=andina_id_label).grid(column=1, row=2, pady=10)
ttk.Entry(frame, textvariable=od_id_label).grid(column=1, row=3, pady=10)
ttk.Entry(frame, textvariable=serenisima_id_label).grid(column=1, row=4, pady=10)
ttk.Entry(frame, textvariable=bees_alv_id_label).grid(column=1, row=5, pady=10)
ttk.Entry(frame, textvariable=bees_sr_id_label).grid(column=1, row=6, pady=10)
entry_principal = ttk.Label(frame, textvariable=nombre_label)
entry_principal.grid(column=2, row=5, pady=10, padx=10)
ttk.Button(frame, image=search, command=obtener_ruta).grid(column=1, row=7, pady=10)

# Creamos los botones con sus respectivos comandos (salir del programa y iniciar búsqueda)
ttk.Button(frame, text='Obtener sesiones', command=ventana_sesiones).grid(column=1, row=0)
ttk.Button(frame, text="Salir", command=root.destroy).grid(column=0, row=8)
ttk.Button(frame, text='Iniciar Búsqueda de precios', command=boton).grid(column=1, row=8)

# Creamos el menú de opciones
menubar = tk.Menu(root)
root.config(menu=menubar)
opciones_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label='Opciones', menu=opciones_menu)
# Añadimos las opciones
opciones_menu.add_command(label='Abrir sesionador', command=ventana_sesiones)
opciones_menu.add_command(label='Cargar credenciales', command=cargar_credenciales)
opciones_menu.add_command(label='Editar credenciales', command=ventana_editar_credenciales)
opciones_menu.add_command(label='Modificar tabla intermedia', command=ventana_mod_tabla_intermedia)
opciones_menu.add_command(label='Abrir tabla intermedia', command=abrir_tabla_intermedia)
opciones_menu.add_command(label='Obtener archivo...', command=obtener_ruta)
opciones_menu.add_command(label='Información y ayuda', command=info)
opciones_menu.add_separator()
opciones_menu.add_command(label='Salir', command=root.destroy)



# Creamos la checkbox para decirle al programa si es necesario buscar los elementos "Sin Precio" de Maxiconsumo en Oscar David
ttk.Checkbutton(frame, text='Buscar "Sin Precio" en Oscar David', variable=busqueda).grid(column=0, row=7)

# Activamos el loop principal 
if __name__ == '__main__':
    root.mainloop()


