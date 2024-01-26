from valuador import Valuador_Andina, Valuador_Maxiconsumo
from lector import Lector

class Operador:
    def __init__(self, maxiconsumo_sess_id, nombre_excel):
        self.nombre_excel = nombre_excel
        self.scanner = Lector(nombre_excel)
        self.valuador_maxiconsumo = Valuador_Maxiconsumo(maxiconsumo_sess_id)
        self.valuador_andina = Valuador_Andina()

    def actualizar_precios(self):
        
        self.scanner.obtener_datos()
        self.maxiconsumo, self.andina, self.nodata = self.scanner.separar_por_proveedor()
        self.andina = self.scanner.intercode_andina(self.andina)
        self.valuador_maxiconsumo.get_prices(self.maxiconsumo)
        self.valuador_andina.get_prices(self.andina)
        self.scanner.actualizar_precios(self.maxiconsumo, self.andina)
