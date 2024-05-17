from proveedor import Proveedor

class Articulo:
    def __init__(self, proveedor:Proveedor) -> None:
        self.codigo = 0
        self.nombre = ''
        self.sku = ''
        self.precio = 0.0
        self.fecha = ''
        self.cod_externo = ''
        self.proveedor = proveedor
        self.proveedor_nombre = ''