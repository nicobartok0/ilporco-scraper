import cryptocode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class Sesion:
    def __init__(self, username, password) -> None:
        self.proveedor = ''
        self.username = username
        self.password = password
        self.url = ''
        self.sess_id = ''
        self.cookies = {}
        self.params = {}
        self.headers = {}

    def abrir_sesion(self, driver):
        self.driver = driver

    def cargar_sess_id(self, sess_id):
        self.sess_id = sess_id
        

class Sesion_Maxiconsumo(Sesion):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        self.proveedor = 'MAXICONSUMO'
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
            'PHPSESSID': self.sess_id,
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
        self.url = 'https://maxiconsumo.com/sucursal_mendoza/catalogsearch/result/'

    def abrir_sesion(self, driver):
        super().abrir_sesion(driver)
        # El driver busca la página y espera 3 segundos
        self.driver.get('https://maxiconsumo.com/sucursal_mendoza/')
        time.sleep(5)
        # Luego busca el botón de "iniciar sesión" y espera un segundo.
        self.driver.find_element(by='xpath', value='//*[@id="html-body"]/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/a[2]').click()
        time.sleep(1)
        # Luego envía a los campos de "email" el correo electrónico enviado al método y en "pswd" la contraseña.
        self.driver.find_element(by='xpath', value='//*[@id="email"]').send_keys(self.username)
        self.driver.find_element(by='xpath', value='//*[@id="pass"]').send_keys(cryptocode.decrypt(self.password, 'ilporco'))
        # El driver hace click en el botón de envío de credenciales.
        self.driver.find_element(by='xpath', value='//*[@id="send2"]/span').click()
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "PHPSESSID", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                self.sess_id = cookie['value']
                self.cookies['PHPSESSID'] = cookie['value']
        

    def cargar_sess_id(self, sess_id):
        self.cookies['PHPSESSID'] = sess_id
        

class Sesion_Oscar_David(Sesion):
    def __init__(self) -> None:
        self.proveedor = 'OSCAR DAVID'
        self.url = ''
        self.sess_id = ''
        self.cookies = {
        'PHPSESSID': self.sess_id,
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
    
    def abrir_sesion(self, driver):
        super().abrir_sesion(driver)

    def cargar_sess_id(self, sess_id):
        self.cookies['PHPSESSID'] = sess_id


    
class Sesion_Andina(Sesion):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        self.proveedor = 'ANDINA'
        self.cookies = {
            'PHPSESSID': self.sess_id,
        }

        self.headers = { 
            'authority': 'andinapedidos.com.ar',
            'accept': 'text/html, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'PHPSESSID=0d4b164dfd2da94b05e5291de9deb977',
            'origin': 'https://andinapedidos.com.ar',
            'referer': 'https://andinapedidos.com.ar/mayor',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        self.data = {
            'producto': '',
        }
        self.url= 'https://andinapedidos.com.ar/includes/buscador.php'

    def abrir_sesion(self, driver):
        super().abrir_sesion(driver)
         # El driver busca la página y espera 3 segundos.
        self.driver.get('https://andinapedidos.com.ar/mayor')
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "PHPSESSID", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                self.sess_id = cookie['value']
                self.cookies['PHPSESSID'] = cookie['value']
    
    def cargar_sess_id(self, sess_id):
        return super().cargar_sess_id(sess_id)



class Sesion_La_Serenisima(Sesion):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        self.proveedor = 'LA SERENISIMA'
        self.cookies = {
            'frontend_lang': 'es_AR',
            'tz': 'America/Buenos_Aires',
            '_gid': 'GA1.3.1842482496.1707941738',
            'session_id': self.sess_id,
            'visitor_uuid': 'd327af60d09a48a9bb9c17fbf81a7e3b',
            '_gat': '1',
            '_ga': 'GA1.1.381898345.1707591214',
            '_ga_GWV00PQ3Y1': 'GS1.1.1707941763.2.1.1707941883.8.0.0',
            '_ga_VVC4ZKVCM2': 'GS1.3.1707941738.2.1.1707941884.0.0.0',
            '_ga_YTRXKYLBLP': 'GS1.1.1707941763.2.1.1707941935.60.0.0',
        }
        self.headers = {
            'authority': 'www.tiendalaserenisima.com.ar',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9',
            # 'cookie': 'frontend_lang=es_AR; tz=America/Buenos_Aires; _gid=GA1.3.1842482496.1707941738; session_id=384f50ec8e340c71ca5a778a2a75b51a88b6dfd5; visitor_uuid=d327af60d09a48a9bb9c17fbf81a7e3b; _gat=1; _ga=GA1.1.381898345.1707591214; _ga_GWV00PQ3Y1=GS1.1.1707941763.2.1.1707941883.8.0.0; _ga_VVC4ZKVCM2=GS1.3.1707941738.2.1.1707941884.0.0.0; _ga_YTRXKYLBLP=GS1.1.1707941763.2.1.1707941935.60.0.0',
            'referer': 'https://www.tiendalaserenisima.com.ar/shop?category=&search=363000&order=',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
        }

        self.params = {
            'category': '',
            'search': '',
            'order': '',
        }
        self.url = 'https://www.tiendalaserenisima.com.ar/shop'

    def abrir_sesion(self, driver):
        super().abrir_sesion(driver)
        # El driver busca la página y espera 3 segundos
        self.driver.get('https://www.tiendalaserenisima.com.ar/web/login')
        time.sleep(3)
        # Luego envía a los campos de "email" el correo electrónico enviado al método y en "pswd" la contraseña.
        self.driver.find_element(by='xpath', value='//*[@id="login"]').send_keys(self.username)
        self.driver.find_element(by='xpath', value='//*[@id="password-login"]').send_keys(cryptocode.decrypt(self.password, 'ilporco'))
        # El driver hace click en el botón de envío de credenciales.
        self.driver.find_element(by='xpath', value='//*[@id="dan_login_form_submit_id"]').click()
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "session_id", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'session_id':
                self.sess_id = cookie['value']
                self.cookies['session_id'] = cookie['value']

    def cargar_sess_id(self, sess_id):
        return super().cargar_sess_id(sess_id)


class Sesion_Bees(Sesion):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        self.proveedor = 'BEES'
        self.cookies = {
            'OptanonAlertBoxClosed': '2024-03-20T00:26:43.263Z',
            'as_csus_viewed_36422400004689_2bd022dd_3c36_4e72_8b7f_b2cda343ed45': 'true',
            'enable_tracking': 'true',
            'country': 'AR',
            'language': 'es',
            'ajs_anonymous_id': '2971b5e1-2ffd-47f2-9ba0-a105ce57a705',
            'connect.sid': self.sess_id,
            'REDUXPOC': '36422400004689',
            'DELIVERYDATE': 'j%3Anull',
            'ajs_user_id': '36422400004689_2a765889-fecb-4852-b740-feb42e11282c',
            'APPLICATION': 'CUSTOMER',
            'STOREID': '126a4950-c0ef-4ff2-a587-ddd963349ced',
            'STOREKEY': 'ABI',
            'iad': '1',
            '___utmvc': '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',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Mar+20+2024+11%3A02%3A29+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false',
        }

        # Definimos los headers
        self.headers = {
            'authority': 'mybees.com.ar',
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9',
            # 'cookie': 'OptanonAlertBoxClosed=2024-03-20T00:26:43.263Z; as_csus_viewed_36422400004689_2bd022dd_3c36_4e72_8b7f_b2cda343ed45=true; enable_tracking=true; country=AR; language=es; ajs_anonymous_id=2971b5e1-2ffd-47f2-9ba0-a105ce57a705; connect.sid=s%3APU6RGFC-S_MT4fwq6twYt-pb8TJsLmH-.1v9euzWROLf1kh11L4ljoKtTa8WEo3W0UwbHlhmpVi8; REDUXPOC=36422400004689; DELIVERYDATE=j%3Anull; ajs_user_id=36422400004689_2a765889-fecb-4852-b740-feb42e11282c; APPLICATION=CUSTOMER; STOREID=126a4950-c0ef-4ff2-a587-ddd963349ced; STOREKEY=ABI; iad=1; ___utmvc=POjU02nThoDfrpkKh/w+yu1yFsOGfiYA7j0nS4Ehe2WdSqU1vsocFrZGI40bgKiCdhREtW/Zhf2++qkIw+cIcgA0w+fZNAm1maBBLk5xEVrwP+teeQDyJtO1oXaPKYyMk0VNCFAlE9CwCPosVmdE1eaXTco+uUYxvQjl+RgWFZcIdap0WYBtjrRMkDCpJ4pBRy/fRk2IjctnDmtFHbvgnw4D131Nbhgb8XOmC4voBpfpN/zDLDb7wQAZNCuAp4MoxBdNr+7lVFZ4Ifm76qsQzJtQbDNfsi/4LaeKWZPd4lnedDmIGeo+y24pAobxON7wrKDfDccmteq9uVa4+HhG81hiX1DX1yONcpP4h7bQCb/JyWRr36OMWxjD0+UzQ9Nzv4Nq5ddP4sc4OlbzLHjhNk0Dqc/0VXb9t5SGoVM/ym53ePPI4JJ2WQbjDmIhaH6UMlBm9AmOJv6sS4JOtFhmdApZepj3R9OmetDQ7PANa2vwJ7z4lR2kpYPKE+LS7+rsgwQd90/JuSpeoX99u84zeIQzyMzyicbV56iiKfDd+e52t2m5NI9EInXIsbZxuJFBdVBHmEacjB4nDMtJlEMw/CnzE2uk5gFkUUk4ci3uyfv/y/64s4fk7cgvJDrySIaFDMjdB3CzJBwZ77tOgDFcAVdGalF8OG5c9JXF8Bffu5i1+FlFC1JhqVbdqgOOD/ffNa6LZOf1DG61vLe9QYUiKgeeE1+vZYZvcnv2rww9aFfkiWOw735YdSc+U7Kgff3XDtW8TUmf2RFbLcAvQAo+4QdDNl3hctdagl04Jqaav3tYlewzk3j0BGgbUkIqicF6T/kkDG3WK+r7S8e1LRzZGyZbdoL3VP1rUANKsrHA78M+pR8SirT4H9Ih4i8hDaKHLN76cAItpbnU8dtpyfejJzqjmZqy6ZNwrGUq1m9wd5yR38Z+w+mTOq96hdcQbLOD1wcMbTez+hOhLH1k1GjTd5yb4a29sLZYIkPCMyli7/jkyl5SzMmP5pDHKXc98N53B+V+0uE+ltbySvyupSTJVeQEEpYnetb+AaAAqINl6CJT63YP2sacE1AOuh3jFnRtmN5h4fxHaA5Y/7Jm23xuzcdQIs1iDJ1a3bASExZaZMDqIRLncIcbpDAIi/G3q04VNyfkrauBBwfN4Fr4OYkuRtq/y2kxS8n4jA1/mJIADcXi2J8GeQpCGEpHw7mkYCt2Iz5HoJx8xs9wF0nkinfA5Uz7VFDJPBC4Agbzgx0PIgeVf3WwlyNdF3AqGWlvUvVrXGI/PP0jepcCKrKkxY/LZ5EZY3ESWBYPekh/Dn1/5WT09cBKmRaIZ8BnpaGGRnamHomK2Akcoa+BijLYwY62al3yT46SYbEyYNQfemsLN89ZVVQqDU16Lvme4qT7l9bUIFLdyyPiH28RaLjGRkOLGjkNJ7f0ICReTfVZu9WVG5SseBopoxTUoUZ7Nk75riWxxhpwuarDM5Ojjh+gVQBBjEP9kYRe/DnR+LLnQoGNRfHKW8dItLCQrdc7WX2mmWxVKFnNmtkNn9A0gomUEd7kX8wVg/IBy001zXvzaF4pwJuALtQWyx5CcfynRwRoj7sK5fm/fbMv19vQ0WcdQR+zl9vKGH2JFq3lfLKLcGWaozSCW6Nzt93kKBfWHLFIvytj8sh1a3z0XISUa/R0fmJB0OEpreu74hT5T8GFP6EtDJ+GBf3d3iMoLYwUF288Zlih+hEULu6Ti8TQUxhZjJMFlDt+Brw2VG63subtCwvkmFY6DtJFFWHfz7NO3g3szYGFLsTtKeI1JZEgW2iRnTsSCjD4k/2/0IpjqBr9Qr1nIRHytSvvi7NhHHOJa3p0Bh3ZW2WpWQ2zJlMhHMTwRnfL2ncCNeun4vBd9qAVdKlVzq1KEVe9+TW4ohSQIbLb1S+Nk8KEMRsEwvxdV7VwFvTnmoxSGOUjOPtN/q5kbWz2vi9uKXpxnPsDGdv26sA3bpfNJIpyUnUtMknTOsnmc4ZchHGU1YtXlRuGWElfKmXLouJQHXsHtb1fCFf4Eo+8bLc0IQ9JqZSEjkNEfaIYwGvTzI6Sr8+HqG1CgS/jSoFO2ZYCe6gZUh1W/7/bjOSGcbLTf8r9KeF84wbUuXdkuqgpnsYNAOAXdd5zSVwRfUUC3noAIKHVgECgvcEZIy8+MUIzo/2/GgCiiWIX1UTh5GJpyaD2a70MQoWj/zWjjMjVxWSxmJ0kL1j9BJa6pkoTh0logK138jTeAEZoPZozQEiCdGlKRri9ptPVoexZTlQFWYcaUm2g61329cJLW+HzVjMdPgRw2MP5ZkYTj2oK11CKvSugnkcDGFh4dLoiRu/bUXPpaRuj55+HLwzE36BeVTeVRGcvP9iFdoQLObJy98VX4fQqdOY0yG/DRfw2P2UkViYipg4kyo2VnYVulW2sF1RFOfFQrLZqfMA9Q8fmg2NC7RIrdFIzur3gvKCoL4lTLumWR3chGmWR2/SOe9UC4u9wg1BSD0y1H0riOM3CNvA8LIVzsmbMGTw7BIXCRBc1Y+Nw73TmxgCBCD9uKBnjBiW0AwPR38rlMvayvJza/BydRP55vlGLe17ANB2i2D1XXIlxLUkDkscbkb9SaO5iDOTMYoDHOFOHb0SHy28o/69H3lT0xJ3dxVTp/fXyJXzWrabSrV3HlHTlFIx+F7r6BXPbk/A/6jzMkdUj6xMUyBwKS8gTuqRgW3NK+A2o6eqMn2uxoEe137SsPOB+SeuVUD+Q8TzcFPZ09mtTdY2QslGe3kCI9YzksIQWa4pKG3Hp37WlfWCYuxYsZGlnZXN0PSxzPU5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTk5hTg==; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Mar+20+2024+11%3A02%3A29+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false',
            'referer': 'https://mybees.com.ar/catalogsearch/result/?q=19342',
            'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
            'x-newrelic-id': 'VQMBUFFXCxAFV1NSDwkAXlA=',
        }

        # Definimos el parámetro. En "term" y "termRaw" va el SKU que debemos buscar.
        self.params = {
            'blockName': 'search_deferred_search_list',
            'locale': 'es_AR',
            'term': '',
            'termRaw': '',
            'pageSize': '20',
            'page': '0',
            'sortBy': 'DEFAULT',
            'filters': '',
            'noCache': '1710943350223',
            'error_block_default': 'global_error_503',
        }
        self.url = 'https://mybees.com.ar/api/blocks'

    def abrir_sesion(self, driver):
        super().abrir_sesion(driver)
        # El driver busca la página y espera 3 segundos
        #self.driver.delete_network_conditions()
        self.driver.get('https://mybees.com.ar')
        self.driver.fullscreen_window()
        time.sleep(5)
        self.driver.find_element(by='xpath', value='//*[@id="guest_homepage_login_button"]/span').click()
        time.sleep(3)
        # Colocamos el nombre de usuario y contraseña y damos click en "continuar".
        self.driver.find_element(by='xpath', value='//*[@id="signInName"]').send_keys(self.username)
        self.driver.find_element(by='xpath', value='//*[@id="password"]').send_keys(cryptocode.decrypt(self.password, 'ilporco'))
        self.driver.find_element(by='xpath', value='//*[@id="continueNew"]').click()
        time.sleep(3)
        #Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "connect.sid"
        cookies = self.driver.get_cookies()
        result_cookies = {}
        for cookie in cookies:
            result_cookies[cookie['name']] = cookie['value']
            if cookie['name'] == 'connect.sid':
                self.sess_id = cookie['value']  
                self.cookies['connect.sid'] = cookie['value']

        
    def cargar_sess_id(self, sess_id):
        return super().cargar_sess_id(sess_id)


