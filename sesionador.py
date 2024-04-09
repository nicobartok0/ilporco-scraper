from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os



class Sesionador:

    # Definimos los atributos de nuestro sesionador, que en este caso será la inicialización del Webdriver
    def __init__(self):
        chromedriver_path = f'{os.getcwd()}\\assets\\chromedriver.exe'
        sys.path.insert(0,chromedriver_path)
        if os.name != 'posix': 
            self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        else:
            self.driver = webdriver.Chrome()

    # Definimos la función en la que buscaremos el id de sesión de Maxiconsumo
    def sesionar_maxiconsumo(self, user, pswd):
        # El driver busca la página y espera 3 segundos
        self.driver.get('https://maxiconsumo.com/sucursal_mendoza/')
        time.sleep(5)
        # Luego busca el botón de "iniciar sesión" y espera un segundo.
        self.driver.find_element(by='xpath', value='//*[@id="html-body"]/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/a[2]').click()
        time.sleep(1)
        # Luego envía a los campos de "email" el correo electrónico enviado al método y en "pswd" la contraseña.
        self.driver.find_element(by='xpath', value='//*[@id="email"]').send_keys(user)
        self.driver.find_element(by='xpath', value='//*[@id="pass"]').send_keys(pswd)
        # El driver hace click en el botón de envío de credenciales.
        self.driver.find_element(by='xpath', value='//*[@id="send2"]/span').click()
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "PHPSESSID", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                self.maxiconsumo_sess_id = cookie['value']
        
        # Devolvemos el id de sesión.
        return self.maxiconsumo_sess_id
    
    def sesionar_andina(self):
        # El driver busca la página y espera 3 segundos.
        self.driver.get('https://andinapedidos.com.ar/mayor')
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "PHPSESSID", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                self.andina_sess_id = cookie['value']

        # Devolvemos el id de sesión.
        return self.andina_sess_id

    def sesionar_serenisima(self, user, pswd):
        # El driver busca la página y espera 3 segundos
        self.driver.get('https://www.tiendalaserenisima.com.ar/web/login')
        time.sleep(3)
        # Luego envía a los campos de "email" el correo electrónico enviado al método y en "pswd" la contraseña.
        self.driver.find_element(by='xpath', value='//*[@id="login"]').send_keys(user)
        self.driver.find_element(by='xpath', value='//*[@id="password-login"]').send_keys(pswd)
        # El driver hace click en el botón de envío de credenciales.
        self.driver.find_element(by='xpath', value='//*[@id="dan_login_form_submit_id"]').click()
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "session_id", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'session_id':
                self.serenisima_sess_id = cookie['value']

        return self.serenisima_sess_id
    
    def sesionar_bees(self, user, pswd):
        # El driver busca la página y espera 3 segundos
        #self.driver.delete_network_conditions()
        self.driver.get('https://mybees.com.ar')
        self.driver.fullscreen_window()
        time.sleep(5)
        self.driver.find_element(by='xpath', value='//*[@id="guest_homepage_login_button"]/span').click()
        time.sleep(3)
        # Colocamos el nombre de usuario y contraseña y damos click en "continuar".
        self.driver.find_element(by='xpath', value='//*[@id="signInName"]').send_keys(user)
        self.driver.find_element(by='xpath', value='//*[@id="password"]').send_keys(pswd)
        self.driver.find_element(by='xpath', value='//*[@id="continueNew"]').click()
        time.sleep(3)
        #Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "connect.sid"
        cookies = self.driver.get_cookies()
        result_cookies = {}
        for cookie in cookies:
            result_cookies[cookie['name']] = cookie['value']
            #if cookie['name'] == 'connect.sid':
            #    self.bees_id = cookie['value']  
        for key in result_cookies.keys():
            print(f'{key}: {result_cookies[key]}')
        return result_cookies
    

        
        