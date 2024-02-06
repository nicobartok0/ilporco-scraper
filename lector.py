from openpyxl import load_workbook, Workbook

# Clase del scaner del libro de excel. El libro debe estar en el mismo
# directorio que el módulo.

class Lector:
    # Constructor de "Lector". Necesita el nombre del archivo excel del que sacar los datos.
    def __init__(self, name):
        self.name = name
        self.wb = load_workbook('archivos/' + name + '.xlsx')
        self.ws = self.wb['Hoja1']
        self.intermedia = load_workbook('assets/tabla-intermedia.xlsx')
        self.andina_codesheet = self.intermedia['Andina']
        self.od_codesheet = self.intermedia['Oscar-David']
        self.sku_list = []
        self.name_list = []
        self.prov_list = []
        self.code_list = []
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

    # Método que toma los datos utilizando los métodos anteriores
    def obtener_datos(self):
        dataline = []
        Lector.obtener_skus(self)
        Lector.obtener_codigo(self)
        Lector.obtener_nombres(self)
        Lector.obtener_proveedor(self)
        for code in range(len(self.code_list)):
            dataline.append(self.name_list[code])
            dataline.append(self.sku_list[code])
            dataline.append(self.prov_list[code])
            self.datos[self.code_list[code]] = dataline
            dataline = []  

        return self.datos

    # Método que separa por proveedor toda la información del excel
    def separar_por_proveedor(self):
        self.maxiconsumo = {}
        self.andina = {}
        self.oscar_david = {}
        self.nodata = {}
        for key in self.datos.keys():
            if 'MAXICONSUMO' in self.datos[key][2]:
                self.maxiconsumo[key] = self.datos[key]
            elif 'ANDINA' in self.datos[key][2]:
                self.andina[key] = self.datos[key]
            elif 'OSCAR DAVID' in self.datos[key][2]:
                self.oscar_david[key] = self.datos[key]
            else:
                self.nodata[key] = self.datos[key]

        return self.maxiconsumo, self.andina, self.oscar_david, self.nodata

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

    # Método que actualiza los precios en un excel actualizado
    def actualizar_precios(self, maxiconsumo, andina, oscar_david):
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
        for key in maxiconsumo.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, maxiconsumo[key][0])
            ws_act.cell(i+1, 3, maxiconsumo[key][1])
            ws_act.cell(i+1, 4, maxiconsumo[key][2])
            ws_act.cell(i+1, 5, maxiconsumo[key][3])
            ws_act.cell(i+1, 6, maxiconsumo[key][4])
            i+=1
        for key in andina.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, andina[key][0])
            ws_act.cell(i+1, 3, andina[key][1])
            ws_act.cell(i+1, 4, andina[key][2])
            ws_act.cell(i+1, 5, andina[key][3])
            ws_act.cell(i+1, 6, andina[key][4])
            i+=1
        for key in oscar_david.keys():
            ws_act.cell(i+1, 1, key)
            ws_act.cell(i+1, 2, oscar_david[key][0])
            ws_act.cell(i+1, 3, oscar_david[key][1])
            ws_act.cell(i+1, 4, oscar_david[key][2])
            ws_act.cell(i+1, 5, oscar_david[key][3])
            ws_act.cell(i+1, 6, oscar_david[key][4])
            i+=1
        wb_act.save('archivos/'+nombre_archivo)




