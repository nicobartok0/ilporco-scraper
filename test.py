import requests

cookies = {
    'PHPSESSID': '6f258581b2c99b8d70fe5a32376c7afc',
}

headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'es-ES,es;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=6f258581b2c99b8d70fe5a32376c7afc',
    'origin': 'https://andinapedidos.com.ar',
    'referer': 'https://andinapedidos.com.ar/mayor',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'producto': '1102',
}

response = requests.post('https://andinapedidos.com.ar/includes/buscador.php', cookies=cookies, headers=headers, data=data)
print(response.text)