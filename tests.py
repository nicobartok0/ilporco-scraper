from lector2 import Lector

lector = Lector(name='andina', ruta='C:\\Users\\nicob\\OneDrive\\Escritorio\\ilporco-scraper\\archivos\\andina.xlsx')
datos = lector.obtener_datos()

proveedores_posibles = []
for dato in datos:
    if dato.proveedor not in proveedores_posibles:
        proveedores_posibles.append(dato.proveedor)

datos = lector.intercode(datos)

print('CÓDIGOS EXTERNOS')
for dato in datos:
    print(f'NOMBRE: {dato.nombre} ILPORCO: {dato.codigo} EXTERNO: {dato.cod_externo}')