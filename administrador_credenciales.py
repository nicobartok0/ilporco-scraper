from openpyxl import load_workbook
import cryptocode


class Administrador_de_credenciales:
    def __init__(self):
        self.wb_credenciales = load_workbook('assets/credenciales.xlsx')
        self.ws_credenciales = self.wb_credenciales['Hoja1']

    def obtener_credenciales(self):
        maxi_user = ''
        maxi_pswd = ''
        sere_user = '' 
        sere_pswd = ''
        bees_user = ''
        bees_pswd = ''
        maxi_user = self.ws_credenciales['B2'].value
        maxi_pswd = cryptocode.decrypt(self.ws_credenciales['C2'].value, 'ilporco')
        sere_user = self.ws_credenciales['B3'].value
        sere_pswd = cryptocode.decrypt(self.ws_credenciales['C3'].value, 'ilporco')
        bees_user = self.ws_credenciales['B4'].value
        bees_pswd = cryptocode.decrypt(self.ws_credenciales['C4'].value, 'ilporco')
        return maxi_user, maxi_pswd, sere_user, sere_pswd, bees_user, bees_pswd

    def escribir_credenciales(self, maxi_user, maxi_pswd, sere_user, sere_pswd, bees_user, bees_pswd):
        self.ws_credenciales['B2'] = maxi_user
        self.ws_credenciales['C2'] = cryptocode.encrypt(maxi_pswd, 'ilporco')
        self.ws_credenciales['B3'] = sere_user
        self.ws_credenciales['C3'] = cryptocode.encrypt(sere_pswd, 'ilporco')
        self.ws_credenciales['B4'] = bees_user
        self.ws_credenciales['C4'] = cryptocode.encrypt(bees_pswd, 'ilporco')
        self.wb_credenciales.save('assets/credenciales.xlsx')