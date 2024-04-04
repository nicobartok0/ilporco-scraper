from lector import Lector


scanner = Lector('pruebas.xlsx', '/home/nicobartok0/Escritorio/Ilporco-scraper-data/BEESPLANILLA.xlsx')

datos = scanner.obtener_datos()
datos = scanner.intercode_bees(datos)

