from selenium import webdriver
import time

class Sesionador:
    # Definimos los atributos de nuestro sesionador, que en este caso será la inicialización del Webdriver
    def __init__(self):
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
                maxiconsumo_sess_id = cookie['value']
        
        # Devolvemos el id de sesión.
        return maxiconsumo_sess_id
    
    def sesionar_andina(self):
        # El driver busca la página y espera 3 segundos.
        self.driver.get('https://andinapedidos.com.ar/mayor')
        time.sleep(3)
        # Obtenemos las cookies y luego identificamos aquella cuyo atributo "name" es "PHPSESSID", que es la cookie
        # de ID de Sesión, y guardamos su valor.
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                andina_sess_id = cookie['value']

        # Devolvemos el id de sesión.
        return andina_sess_id
    



        
        