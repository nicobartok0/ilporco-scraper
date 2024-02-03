import requests
import time
from bs4 import BeautifulSoup
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Creamos nuestro Valuador que recibe como parámetro la lista de todos los SKUs y 
# el ID De la sesión de Maxiconsumo

class Valuador_Maxiconsumo:
    def __init__(self, sess_id): 
        self.precios = []
        self.contador = 0
        self.cookies = {
            'mage-banners-cache-storage': '%7B%7D',
            'form_key': 'MIEm9usykOi9e32h',
            '_gid': 'GA1.2.1952250118.1704215942',
            'mage-cache-storage': '%7B%7D',
            'mage-cache-storage-section-invalidation': '%7B%7D',
            'mage-messages': '',
            'recently_viewed_product': '%7B%7D',
            'recently_viewed_product_previous': '%7B%7D',
            'recently_compared_product': '%7B%7D',
            'recently_compared_product_previous': '%7B%7D',
            'product_data_storage': '%7B%7D',
            'PHPSESSID': sess_id,
            'private_content_version': 'fa7c33f0689261a1bb460fd123f34891',
            'form_key': 'MIEm9usykOi9e32h',
            'X-Magento-Vary': '94e3f182fc686dbadcb7d7dcb2f86644b734485a',
            'mage-cache-sessid': 'true',
            'section_data_ids': '%7B%22customer%22%3A1704283499%2C%22compare-products%22%3A1704283499%2C%22last-ordered-items%22%3A1704283499%2C%22cart%22%3A1704283499%2C%22directory-data%22%3A1704283499%2C%22captcha%22%3A1704283499%2C%22wishlist%22%3A1704283499%2C%22instant-purchase%22%3A1704283499%2C%22loggedAsCustomer%22%3A1704283499%2C%22multiplewishlist%22%3A1704283499%2C%22persistent%22%3A1704283499%2C%22review%22%3A1704283499%2C%22recently_viewed_product%22%3A1704283499%2C%22recently_compared_product%22%3A1704283499%2C%22product_data_storage%22%3A1704283499%2C%22paypal-billing-agreement%22%3A1704283499%7D',
            '_ga_RVXNLTDS4Z': 'GS1.1.1704283479.5.1.1704283517.22.0.0',
            '_ga': 'GA1.2.865884606.1703870935',
        }

        self.headers = {
            'authority': 'maxiconsumo.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'mage-banners-cache-storage=%7B%7D; mage-banners-cache-storage=%7B%7D; form_key=MIEm9usykOi9e32h; _gid=GA1.2.1952250118.1704215942; mage-messages=; PHPSESSID=7e26263016d053e22c4b0b7d0a0f9740; private_content_version=c2708b23637ed8845cb599b41899354f; form_key=MIEm9usykOi9e32h; X-Magento-Vary=94e3f182fc686dbadcb7d7dcb2f86644b734485a; _gat=1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; section_data_ids=%7B%22customer%22%3A1704223745%2C%22compare-products%22%3A1704223745%2C%22last-ordered-items%22%3A1704223745%2C%22cart%22%3A1704223745%2C%22directory-data%22%3A1704223745%2C%22captcha%22%3A1704223745%2C%22wishlist%22%3A1704223745%2C%22instant-purchase%22%3A1704223745%2C%22loggedAsCustomer%22%3A1704223745%2C%22multiplewishlist%22%3A1704223745%2C%22persistent%22%3A1704223745%2C%22review%22%3A1704223745%2C%22recently_viewed_product%22%3A1704223745%2C%22recently_compared_product%22%3A1704223745%2C%22product_data_storage%22%3A1704223745%2C%22paypal-billing-agreement%22%3A1704223745%2C%22messages%22%3A1704223745%7D; _ga_RVXNLTDS4Z=GS1.1.1704215939.3.1.1704223748.42.0.0; _ga=GA1.2.865884606.1703870935',
            'referer': 'https://maxiconsumo.com/sucursal_mendoza/',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }

    # Método para obtener los precios de los artículos de maxiconsumo
    def get_prices(self, maxiconsumo, progress, currentarticle):
        self.sku_list = []
        article_names = {}
        for key in maxiconsumo.keys():
            self.sku_list.append(maxiconsumo[key][1])
            article_names[maxiconsumo[key][1]] = maxiconsumo[key][0]
        count=0
        for sku in self.sku_list:
            currentarticle.set(article_names[sku])
            count+=1
            params = {
           'q': sku,
            }
            response = requests.get(
            'https://maxiconsumo.com/sucursal_mendoza/catalogsearch/result/',
            params=params,
            cookies=self.cookies,
            headers=self.headers,
            )

            soup = BeautifulSoup(response.content, 'html.parser')
            precios = soup.find_all('span', {'class': 'price'})

            try:
                precio = precios[1].text
                self.precios.append(precio)
                progress.set(self.contador)
                self.contador+=1
               
            except:
                self.precios.append('Sin precio')
                progress.set(self.contador)
                self.contador+=1

        count = 0
        for key in maxiconsumo.keys():
            maxiconsumo[key].append('')
            maxiconsumo[key].append(self.precios[count])
            count+=1
        return maxiconsumo

    def get_cookies(self):
        print(self.cookies)

    def get_headers(self):
        print(self.headers)

class Valuador_Andina:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = 'http://andinapedidos.com.ar/mayor'
        self.precios = []
        self.contador = 0

    # Método para obtener los precios de los articulos de andina
    def get_prices(self, andina, progress, contador, currentarticle):
        
        self.sku_list = []
        article_names = {}
        self.contador = contador
        for key in andina.keys():
            self.sku_list.append(andina[key][3])
            article_names[andina[key][3]] = andina[key][0]
        self.driver.get(self.url)
        for key in self.sku_list:
            self.contador+=1
            currentarticle.set(article_names[key])
            if key != '':    
                self.driver.find_element(by='xpath', value='//*[@id="buscador"]').send_keys(key)
                time.sleep(3)
                try:
                    precio = self.driver.find_element(by='xpath', value='//*[@id="cat_xxx"]/ul/li/div/div[2]/div/div/div[1]/h5')
                    self.precios.append(precio.text)
                    progress.set(self.contador)
                except:
                    self.precios.append('Sin precio')
                self.driver.find_element(by='xpath', value='//*[@id="buscador"]').clear()
            else:
                self.precios.append('Sin precio')
        count = 0
        for key in andina.keys():
            andina[key].append(self.precios[count])
            count+=1
        return andina


class Valuador_Oscar_David:
    def __init__(self, sess_id):
        
        self.cookies = {
            'PHPSESSID': sess_id,
            '_ga': 'GA1.1.906641195.1705342638',
            '_ga_TWE3V9LPCQ': 'GS1.1.1706819158.8.0.1706819160.0.0.0',
            'twk_uuid_5ebd7913967ae56c5219d614': '%7B%22uuid%22%3A%221.PUnz6BA00ImXLQ5DtUMJgY8hJ0NHmLq2MqMZ9rE3FBkZPO1FftX3xwviUtQPp4yuwPIL86d5fjeKyeXVcLP3ePaE43DL9VcAMVLdQyjR5OiPwnPp8%22%2C%22version%22%3A3%2C%22domain%22%3A%22sig2k.net%22%2C%22ts%22%3A1706819690142%7D',
            'TawkConnectionTime': '0',
        }

        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'PHPSESSID=6f0e1e65e73852a99653643fc9682afe; _ga=GA1.1.906641195.1705342638; _ga_TWE3V9LPCQ=GS1.1.1706819158.8.0.1706819160.0.0.0; twk_uuid_5ebd7913967ae56c5219d614=%7B%22uuid%22%3A%221.PUnz6BA00ImXLQ5DtUMJgY8hJ0NHmLq2MqMZ9rE3FBkZPO1FftX3xwviUtQPp4yuwPIL86d5fjeKyeXVcLP3ePaE43DL9VcAMVLdQyjR5OiPwnPp8%22%2C%22version%22%3A3%2C%22domain%22%3A%22sig2k.net%22%2C%22ts%22%3A1706819690142%7D; TawkConnectionTime=0',
            'Origin': 'https://oscardavid.sig2k.net',
            'Referer': 'https://oscardavid.sig2k.net/webs/oscardavid@sigma.ODKard/sigkart/3.1/kart.php?txtbuscar=1840&catego=&cateid=&vista=cuadricula',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        self.params = {
            'sql': 'articulos',
        }

        self.data = {
            'txtbuscar': '',
            'catego': '',
            'chkcatego': 'false',
            'orden': '',
            'ver': '',
            'nocache': '',
            'rows': '24',
            'skip': '0',
        }
        self.url = 'https://oscardavid.sig2k.net/webs/oscardavid@sigma.ODKard/sigkart/3.1/'
        self.precios = []
        self.contador = 0

    # Método para obtener los precios de los articulos de andina
    def get_prices(self, oscar_david, progress, contador, currentarticle):
        self.sku_list = []
        article_names = {}
        self.contador = contador
        for key in oscar_david.keys():
            self.sku_list.append(oscar_david[key][3])
            article_names[oscar_david[key][3]] = oscar_david[key][0]
        
        for key in self.sku_list:
            self.contador+=1
            currentarticle.set(article_names[key])
            if key != '':    
                self.data['txtbuscar'] = key
                response = requests.post(
                    'https://oscardavid.sig2k.net/webs/oscardavid@sigma.ODKard/sigkart/3.1/swexecute.php',
                    params=self.params,
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,
                )
                codename = 'Cod. ' + key

                res = response.json()
                subtits = []
                for i in res:
                    subtits.append(i['SUBTIT'])

                if codename in subtits:    
                    for i in res:
                        if i['SUBTIT'] == codename:
                            self.precios.append(i['PRBASE'])
                else:
                    self.precios.append('Sin Precio')
                progress.set(self.contador)

            else:
                self.precios.append('Sin precio')
                progress.set(self.contador)

        count = 0

        for key in oscar_david.keys():
            oscar_david[key].append(self.precios[count])
            if count < len(oscar_david.keys())-1:
                count+=1
        return oscar_david

    


    


    
