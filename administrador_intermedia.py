from openpyxl import load_workbook


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

    
        




