from openpyxl import load_workbook, Workbook
import cryptocode

# Clase del scaner del libro de excel. El libro debe estar en el mismo
# directorio que el módulo.

class Lector:
    # Constructor de "Lector". Necesita el nombre del archivo excel del que sacar los datos.
    def __init__(self, name, ruta):
        self.name = name
        self.wb = load_workbook(ruta)
        self.ws = self.wb['Hoja1']
        self.intermedia = load_workbook('assets/tabla-intermedia.xlsx')
        self.andina_codesheet = self.intermedia['Andina']
        self.od_codesheet = self.intermedia['Oscar-David']
        self.ser_codesheet = self.intermedia['La-Serenisima']
        self.sku_list = []
        self.name_list = []
        self.prov_list = []
        self.code_list = []
        self.date_list = []
        self.datos = {}

    # Método que toma los SKU's de la primer fila del excel.
    def obtener_skus(self):
        for column_data in self.ws['A']:
            if column_data.value != None:
                valor = str(column_data.value)
                self.sku_list.append(valor)
        return self.sku_list
    
    # Método que toma los nombres de los artículos de la tercer columna del excel.
    def obtener_nombres(self):
        for column_data in self.ws['C']:
            if column_data.value != None:
                valor = str(column_data.value)
                self.name_list.append(valor)
        return self.name_list
    
    # Método que toma los códigos de los artículos de la segunda columna del excel.
    def obtener_codigo(self):
        for column_data in self.ws['B']:
            if column_data.value != None:
                valor = str(column_data.value)
                self.code_list.append(valor)
        return self.code_list
    
    # Método que toma los nombres de los proveedores de los artículos de la séptima columna del excel.
    def obtener_proveedor(self):
        for column_data in self.ws['G']:
            if column_data.value != None:
                valor = str(column_data.value)
                self.prov_list.append(valor)
        return self.prov_list
    
    def obtener_fechas(self):
        for column_data in self.ws['H']:
            if column_data.value != None:
                valor = str(column_data.value)
                self.date_list.append(valor)
        return self.date_list

    # Método que toma los datos utilizando los métodos anteriores
    def obtener_datos(self):
        dataline = []
        Lector.obtener_skus(self)
        Lector.obtener_codigo(self)
        Lector.obtener_nombres(self)
        Lector.obtener_proveedor(self)
        Lector.obtener_fechas(self)
        self.codigo_fecha = {}
        for code in range(len(self.code_list)):
            dataline.append(self.name_list[code])
            dataline.append(self.sku_list[code])
            dataline.append(self.prov_list[code])
            self.datos[self.code_list[code]] = dataline
            dataline = []  
        contador = 0
        for key in self.datos.keys():
            self.codigo_fecha[key] = self.date_list[contador]
            contador +=1
        return self.datos

    # Método que separa por proveedor toda la información del excel
    def separar_por_proveedor(self):
        self.maxiconsumo = {}
        self.andina = {}
        self.oscar_david = {}
        self.serenisima = {}
        self.nodata = {}
        for key in self.datos.keys():
            if 'MAXICONSUMO' in self.datos[key][2]:
                self.maxiconsumo[key] = self.datos[key]
            elif 'ANDINA' in self.datos[key][2]:
                self.andina[key] = self.datos[key]
            elif 'OSCAR DAVID' in self.datos[key][2]:
                self.oscar_david[key] = self.datos[key]
            elif 'SERENISIMA' in self.datos[key][2]:
                self.serenisima[key] = self.datos[key]
            else:
                self.nodata[key] = self.datos[key]

        return self.maxiconsumo, self.andina, self.oscar_david, self.serenisima, self.nodata

    # Método que le asigna a cada artículo de Andina un código interno de la tabla intermedia
    def intercode_andina(self, andina):
        codes = []
        and_codes = []
        counter = 0
        for code in self.andina_codesheet['B']:
            if code.value != None and code.value != 'Ilporco':
                codes.append(str(int(code.value)))
        for and_code in self.andina_codesheet['D']:
            if and_code.value != None and and_code.value != 'Andina':
                and_codes.append(str(int(and_code.value)))
        #new_andina = {}
        for code in codes:
            try:
                andina[code].append(and_codes[counter])
                #new_andina[and_codes[counter]] = andina[code]
            except:
                pass
            counter +=1

        for key in andina.keys():
            try:
                type(andina[key][3])
            except:
                andina[key].append('')
        return andina
    
    def intercode_maxi(self, maxiconsumo):
        codes = []
        od_codes = []
        counter = 0
        # Hacemos una lista con los códigos de IlPorco de la tabla intermedia
        for code in self.od_codesheet['B']:
            if code.value != None and code.value != 'Ilporco':
                codes.append(str(int(code.value)))

        # Hacemos una lista con los códigos de Oscar David de la tabla inttermedia
        for od_code in self.od_codesheet['D']:
            if od_code.value != None and od_code.value != 'Oscar-David':
                od_codes.append(str(int(od_code.value)))
        # Limpiamos los puntos flotantes en los keys del diccionario si es que los hay
        keys = []
        for key in maxiconsumo.keys():
            keys.append(key)

        for key in keys:
            if ".0" in key:
                newkey = key
                newkey = newkey[:-2]
                maxiconsumo[newkey] = maxiconsumo[key]
                del maxiconsumo[key]

        # Por cada código de la tabla intermedia
        for code in codes:
            # Intenta añadir al diccionario de maxiconsumo, en el índice del código de IlPorco si es que existe, 
            # un valor nuevo a la lista de elementos: el código de Oscar David.
            try:
                maxiconsumo[code][3] = od_codes[counter]
            except:
                # Si no encuentra un código correspondiente, simplemente el programa sigue.
                pass
            counter +=1

        # Verificamos la existetncia del elemento que corresponde al código, y si no hay código añadido, añadimos un caracter vacío.
        for key in maxiconsumo.keys():
            try:
                type(maxiconsumo[key][3])
            except:
                maxiconsumo[key][3] = ''
        return maxiconsumo

    def intercode_od(self, oscar_david):
        codes = []
        od_codes = []
        counter = 0
        # Hacemos una lista con los códigos de IlPorco de la tabla intermedia
        for code in self.od_codesheet['B']:
            if code.value != None and code.value != 'Ilporco':
                codes.append(str(int(code.value)))

        # Hacemos una lista con los códigos de Oscar David de la tabla inttermedia
        for od_code in self.od_codesheet['D']:
            if od_code.value != None and od_code.value != 'Oscar-David':
                od_codes.append(str(int(od_code.value)))
        # Limpiamos los puntos flotantes en los keys del diccionario si es que los hay
        keys = []
        for key in oscar_david.keys():
            keys.append(key)

        for key in keys:
            if ".0" in key:
                newkey = key
                newkey = newkey[:-2]
                oscar_david[newkey] = oscar_david[key]
                del oscar_david[key]

        # Por cada código de la tabla intermedia
        for code in codes:
            # Intenta añadir al diccionario de oscar_david, en el índice del código de IlPorco si es que existe, 
            # un valor nuevo a la lista de elementos: el código de Oscar David.
            try:
                oscar_david[code].append(od_codes[counter])
            except:
                # Si no encuentra un código correspondiente, simplemente el programa sigue.
                pass
            counter +=1

        # Verificamos la existetncia del elemento que corresponde al código, y si no hay código añadido, añadimos un caracter vacío.
        for key in oscar_david.keys():
            try:
                type(oscar_david[key][3])
            except:
                oscar_david[key].append('')
        return oscar_david
    
    def intercode_serenisima(self, serenisima):
        codes = []
        ser_codes = []
        counter = 0
        for code in self.ser_codesheet['B']:
            if code.value != None and code.value != 'Ilporco':
                codes.append(str(int(code.value)))
        for ser_code in self.ser_codesheet['D']:
            if ser_code.value != None and ser_code.value != 'La-Serenisima':
                ser_codes.append(str(int(ser_code.value)))
        #new_andina = {}
        for code in codes:
            try:
                serenisima[code].append(ser_codes[counter])
            except:
                pass
            counter +=1

        for key in serenisima.keys():
            try:
                type(serenisima[key][3])
            except:
                serenisima[key].append('')
        return serenisima

    # Método que añade las fechas a los artículos antes de actualizar los precios.
    def anidar_fechas(self, maxiconsumo, andina, oscar_david, serenisima):
        for key in maxiconsumo.keys():
            maxiconsumo[key].append(self.codigo_fecha[key])
        for key in andina.keys():
            andina[key].append(self.codigo_fecha[key])
        for key in oscar_david.keys():
            oscar_david[key].append(self.codigo_fecha[key])
        for key in serenisima.keys():
            serenisima[key].append(self.codigo_fecha[key])
        
        return maxiconsumo, andina, oscar_david, serenisima
    
    def adaptar(self, maxiconsumo, andina, oscar_david, la_serenisima):
        print('MAXICONSUMO: ')
        for key in maxiconsumo.keys():
            print(f'type: {type(maxiconsumo[key][4])}')
            if '$' in maxiconsumo[key][4]:
                print(f'{key}: {maxiconsumo[key][4][2:]}')
        print('ANDINA: ')
        for key in andina.keys():
            print(f'type: {type(andina[key][4])}')
            print(f'{key}: {andina[key][4]}')
        print('OSCAR DAVID: ')
        for key in oscar_david.keys():
            print(f'type: {type(oscar_david[key][4])}')
            print(f'{key}: {oscar_david[key][4]}')
        print('LA SERENÍSIMA: ')
        for key in la_serenisima.keys():
            print(f'type: {type(la_serenisima[key][4])}')
            print(f'{key}: {la_serenisima[key][4]}')

        return maxiconsumo, andina, oscar_david, la_serenisima

    # Método que actualiza los precios en un excel actualizado
    def actualizar_precios(self, maxiconsumo, andina, oscar_david, serenisima):
        nombre_archivo = f'{self.name}-ACTUALIZADO.xlsx'
        wb_act = Workbook()
        ws_act = wb_act[wb_act.sheetnames[0]]
        i = 1
        ws_act.cell(1, 1, 'Il Porco')
        ws_act.cell(1, 2, 'Artículo')
        ws_act.cell(1, 3, 'SKU')
        ws_act.cell(1, 4, 'Distribuidor')
        ws_act.cell(1, 5, 'Cód. Externo')
        ws_act.cell(1, 6, 'Nuevo Precio')
        ws_act.cell(1, 7, 'Última fecha')

        maxiconsumo, andina, oscar_david, serenisima = Lector.anidar_fechas(self, maxiconsumo, andina, oscar_david, serenisima)
        for key in maxiconsumo.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, maxiconsumo[key][0])
            ws_act.cell(i+1, 3, maxiconsumo[key][1])
            ws_act.cell(i+1, 4, maxiconsumo[key][2])
            ws_act.cell(i+1, 5, maxiconsumo[key][3])
            ws_act.cell(i+1, 6, maxiconsumo[key][4])
            ws_act.cell(i+1, 7, maxiconsumo[key][5])
            i+=1
        for key in andina.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, andina[key][0])
            ws_act.cell(i+1, 3, andina[key][1])
            ws_act.cell(i+1, 4, andina[key][2])
            ws_act.cell(i+1, 5, andina[key][3])
            ws_act.cell(i+1, 6, andina[key][4])
            ws_act.cell(i+1, 7, andina[key][5])
            i+=1
        for key in oscar_david.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, oscar_david[key][0])
            ws_act.cell(i+1, 3, oscar_david[key][1])
            ws_act.cell(i+1, 4, oscar_david[key][2])
            ws_act.cell(i+1, 5, oscar_david[key][3])
            ws_act.cell(i+1, 6, oscar_david[key][4])
            ws_act.cell(i+1, 7, oscar_david[key][5])
            i+=1
        for key in serenisima.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, serenisima[key][0])
            ws_act.cell(i+1, 3, serenisima[key][1])
            ws_act.cell(i+1, 4, serenisima[key][2])
            ws_act.cell(i+1, 5, serenisima[key][3])
            ws_act.cell(i+1, 6, serenisima[key][4])
            ws_act.cell(i+1, 7, serenisima[key][5])
            i+=1
        wb_act.save('archivos/'+nombre_archivo)

class Administrador_de_credenciales:
    def __init__(self):
        self.wb_credenciales = load_workbook('assets/credenciales.xlsx')
        self.ws_credenciales = self.wb_credenciales['Hoja1']

    def obtener_credenciales(self):
        maxi_user = ''
        maxi_pswd = ''
        sere_user = '' 
        sere_pswd = ''
        maxi_user = self.ws_credenciales['B1'].value
        maxi_pswd = cryptocode.decrypt(self.ws_credenciales['B2'].value, 'ilporco')
        sere_user = self.ws_credenciales['D1'].value
        sere_pswd = cryptocode.decrypt(self.ws_credenciales['D2'].value, 'ilporco')
        return maxi_user, maxi_pswd, sere_user, sere_pswd

    def escribir_credenciales(self, maxi_user, maxi_pswd, sere_user, sere_pswd):
        self.ws_credenciales['B1'] = maxi_user
        self.ws_credenciales['B2'] = cryptocode.encrypt(maxi_pswd, 'ilporco')
        self.ws_credenciales['D1'] = sere_user
        self.ws_credenciales['D2'] = cryptocode.encrypt(sere_pswd, 'ilporco')
        self.wb_credenciales.save('assets/credenciales.xlsx')

class Administrador_Intermedia:
    def __init__(self):
        self.wb = load_workbook('assets/tabla-intermedia.xlsx')
        self.ws_od = self.wb['Oscar-David']
        self.ws_and = self.wb['Andina']
        self.ws_sere = self.wb['La-Serenisima']

    def añadir_articulo(self, sku, ilporco, nombre, codigo, destino:str):
        data = (
            sku, ilporco, nombre, codigo
        )
            
            
        if destino == 'Oscar David':
            self.ws_od.append(data)
        elif destino == 'Andina':
            self.ws_and.append(data)
        else:
            self.ws_sere.append(data)
        self.wb.save('assets/tabla-intermedia.xlsx')

    def quitar_articulo(self, codigo, destino):
        # Encontramos la fila que contiene el código
        if destino == 'Oscar David':
            sheet = self.ws_od
        elif destino == 'Andina':
            sheet = self.ws_and
        else:
            sheet = self.ws_sere
        
        for row in sheet.rows:
            if row[1].value == codigo:
                sheet.delete_rows(row[0].row)
        
        self.wb.save('assets/tabla-intermedia.xlsx')

    
        




