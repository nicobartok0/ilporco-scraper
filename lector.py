from openpyxl import load_workbook

# Clase del scaner del libro de excel. El libro debe estar en el mismo
# directorio que el módulo.

class Lector:
    # Constructor de "Lector". Necesita el nombre del archivo excel del que sacar los datos.
    def __init__(self, name):
        self.name = name
        self.wb = load_workbook(name + '.xlsx')
        self.ws = self.wb['Hoja1']
        self.sku_list = []
        self.name_list = []

    # Método que toma los SKU's de la primer fila del excel.
    def obtener_skus(self):
        for column_data in self.ws['A']:
            if column_data.value != None:
                valor = str(column_data.value)
                self.sku_list.append(valor)

        return self.sku_list
    
    # Método que toma los nombres de los artículos de la tercer columna del excel.
    def obtener_nombres(self):
        self.name_list_elements = self.ws['C']
        for object in self.name_list_elements:
            self.name_list.append(object.value)
        return self.name_list
    
    def actualizar_precios(self, prices_list):
        nombre_archivo = f'{self.name}-ACTUALIZADO.xlsx'
        self.ws.insert_cols(idx=14)
        for i in range(len(prices_list)):
            self.ws.cell(i+1, 14, prices_list[i])
        self.wb.save(nombre_archivo)




