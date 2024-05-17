import requests
import time
from bs4 import BeautifulSoup


class Valuador:
    def __init__(self, sesiones:dict, articulos:list, progresswindow):
        self.sesiones = sesiones
        self.articulos = articulos
        self.window = progresswindow
        

    def obtener_precios(self):
        for articulo in self.articulos:
            self.window.event_generate("<<ArticleRefresh>>", when="tail")
            sesion_actual = self.sesiones[articulo.proveedor.nombre]
            self.articulo = articulo
            
            # Acá van los algoritmos que debe hacer el programa en cada página para encontrar el precio del artículo

            # BÚSQUEDA DE PRECIOS EN MAXICONSUMO
            if sesion_actual.proveedor == 'MAXICONSUMO':
                sesion_actual.params = {
                'q': articulo.sku,
                }
                response = requests.get(
                    'https://maxiconsumo.com/sucursal_mendoza/catalogsearch/result/',
                    params=sesion_actual.params,
                    cookies=sesion_actual.cookies,
                    headers=sesion_actual.headers,
                    )
                    
                soup = BeautifulSoup(response.content, 'html.parser')
                precios = soup.find_all('span', {'class': 'price'})
                try:
                    precio = precios[1].text
                    articulo.precio = precio
                
                
                except:
                    articulo.precio = 'Sin precio'

            # BÚSQUEDA DE PRECIOS EN OSCAR DAVID
            elif sesion_actual.proveedor == 'OSCAR DAVID':
                if articulo.cod_externo != '':    
                    sesion_actual.data['txtbuscar'] = articulo.cod_externo
                    response = requests.post(
                        'https://oscardavid.sig2k.net/webs/oscardavid@sigma.ODKard/sigkart/3.1/swexecute.php',
                        params=sesion_actual.params,
                        cookies=sesion_actual.cookies,
                        headers=sesion_actual.headers,
                        data=sesion_actual.data,
                    )
                    codename = 'Cod. ' + articulo.sku

                    res = response.json()
                    subtits = []
                    for i in res:
                        subtits.append(i['SUBTIT'])
                    if codename in subtits:    
                        for i in res:
                            if i['SUBTIT'] == codename:
                                articulo.precio = i['PRBASE']
                                
                                
                    else:
                        articulo.precio = 'Sin Precio'


                else:
                    articulo.precio = 'Sin precio'


            # BÚSQUEDA DE PRECIOS EN ANDINA
            elif sesion_actual.proveedor == 'ANDINA':
                if articulo.cod_externo != '':    
                    sesion_actual.data['producto'] = articulo.cod_externo
                    response = requests.post(sesion_actual.url, cookies=sesion_actual.cookies, headers=sesion_actual.headers, data=sesion_actual.data)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    #print(soup.text)
                    precio = soup.find('h5')
                    if precio != None:
                        articulo.precio = precio.text
            
                    else:
                        articulo.precio = 'Sin precio'
                        
                else:
                    articulo.precio = 'Sin precio'

            # BÚSQUEDA DE PRECIOS EN LA SERENÍSIMA
            elif sesion_actual.proveedor == 'LA SERENISIMA':
                if articulo.cod_externo != '':    
                    sesion_actual.params['search'] = articulo.cod_externo
                    response = requests.get('https://www.tiendalaserenisima.com.ar/shop', params=sesion_actual.params, cookies=sesion_actual.cookies, headers=sesion_actual.headers)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    precio = soup.find('span', {'class': 'oe_currency_value'})
                    if precio != None:
                        articulo.precio = precio.text
                        
                    
                    else:
                        articulo.precio = 'Sin precio'
                        
                else:
                    articulo.precio = 'Sin precio'

            # BÚSQUEDA DE PRECIOS EN BEES
            elif sesion_actual.proveedor == 'BEES':
                if articulo.cod_externo != '':
                    # Añadimos el sku al parámetro de la consulta
                    sesion_actual.params['term'] = articulo.cod_externo
                    sesion_actual.params['termRaw'] = articulo.cod_externo
                    
                    # Hacemos la consulta y obtenemos el JSON de respuesta
                    response = requests.get(sesion_actual.url, params=sesion_actual.params, cookies=sesion_actual.cookies, headers=sesion_actual.headers)
                    res = response.json()
                    
                    if res != {}:
                        # Creamos un diccionario con TODOS los productos que devuelve la página, para luego comparar los SKUS con el SKU que buscamos.
                        # Tambien creamos una lista con todos los SKUs actuales de la página para comprobar si el SKU en cuestión fue encontrado
                        products_dict = {}
                        current_skus = []
                        

                        try:
                            for element in res['blocks'][4]['meta']['data']['products']:
                                products_dict[element['sku']] = element['price']
                                current_skus.append(element['sku'])
                                a = element['sku']
                        except:
                            articulo.precio = 'Sin precio'    
                        

                        # Comparamos SKUs si existe el SKU que buscamos en la lista de SKUs y guardamos el precio que corresponde si es el caso.
                        if articulo.cod_externo in current_skus:  
                            for key in products_dict:
                                if key == articulo.cod_externo:
                                    articulo.precio = products_dict[key]
                        else:
                            articulo.precio = 'Sin precio'

                    else:
                        articulo.precio = 'Sin precio'
                else:
                    articulo.precio = 'Sin precio'
                    

             
            
            
        

