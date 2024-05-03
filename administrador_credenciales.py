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
        maxi_pswd = self.ws_credenciales['C2'].value
        sere_user = self.ws_credenciales['B3'].value
        sere_pswd = self.ws_credenciales['C3'].value
        bees_user = self.ws_credenciales['B4'].value
        bees_pswd = self.ws_credenciales['C4'].value

        creds = {
            'MAXICONSUMO': [maxi_user, maxi_pswd],
            'ANDINA': ['', ''],
            'OSCAR DAVID': ['', ''],
            'LA SERENISIMA': [sere_user, sere_pswd],
            'BEES': [bees_user, bees_pswd]
        }
        return creds

    def escribir_credenciales(self, creds):
        for cred in creds.keys():
            if cred == 'MAXICONSUMO':
                self.ws_credenciales['B2'] = creds['MAXICONSUMO'][0]
                self.ws_credenciales['C2'] = cryptocode.encrypt(creds['MAXICONSUMO'][1], 'ilporco')
            elif cred == 'LA SERENISIMA':
                self.ws_credenciales['B3'] = creds['LA SERENISIMA'][0]
                self.ws_credenciales['C3'] = cryptocode.encrypt(creds['LA SERENISIMA'][1], 'ilporco')
            elif cred == 'BEES':
                self.ws_credenciales['B4'] = creds['BEES'][0]
                self.ws_credenciales['C4'] = cryptocode.encrypt(creds['BEES'][1], 'ilporco')
        self.wb_credenciales.save('assets/credenciales.xlsx')