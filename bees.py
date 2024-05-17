import requests

cookies = {
    'OptanonAlertBoxClosed': '2024-03-20T00:26:43.263Z',
    'connect.sid': 's%3Aj4ZXxOBdqNGRQ_HNUgA9u_OOvz9prdHK.OoR%2FxXWNz3Bl7FThSbW8G8SNq%2BCD72g0MusnRoMCOjg',
    'REDUXPOC': '10056300002900',
    'DELIVERYDATE': 'j%3Anull',
    'ajs_user_id': '10056300002900_d17f5ddd-0b18-4f19-912c-b91c20a8405b',
    'APPLICATION': 'CUSTOMER',
    'STOREID': '126a4950-c0ef-4ff2-a587-ddd963349ced',
    'STOREKEY': 'ABI',
    'iad': '1',
    'enable_tracking': 'true',
    'country': 'AR',
    'language': 'es',
    'ajs_anonymous_id': '7dd45fff-64f0-4bc2-8258-890fa74d5b94',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+May+16+2024+11%3A25%3A12+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false',
}

headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    # 'cookie': 'OptanonAlertBoxClosed=2024-03-20T00:26:43.263Z; connect.sid=s%3Aj4ZXxOBdqNGRQ_HNUgA9u_OOvz9prdHK.OoR%2FxXWNz3Bl7FThSbW8G8SNq%2BCD72g0MusnRoMCOjg; REDUXPOC=10056300002900; DELIVERYDATE=j%3Anull; ajs_user_id=10056300002900_d17f5ddd-0b18-4f19-912c-b91c20a8405b; APPLICATION=CUSTOMER; STOREID=126a4950-c0ef-4ff2-a587-ddd963349ced; STOREKEY=ABI; iad=1; enable_tracking=true; country=AR; language=es; ajs_anonymous_id=7dd45fff-64f0-4bc2-8258-890fa74d5b94; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+16+2024+11%3A25%3A12+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false',
    'referer': 'https://mybees.com.ar/catalogsearch/result/?q=627',
    'requesttraceid': 'NFA_search_results_es_AR_1715869512213',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'x-newrelic-id': 'VQMBUFFXCxAFV1NSDwkAXlA=',
}

params = {
    'blockName': 'search_deferred_search_list',
    'locale': 'es_AR',
    'term': '627',
    'termRaw': '627',
    'pageSize': '20',
    'page': '0',
    'sortBy': 'DEFAULT',
    'filters': '',
    'noCache': '0',
    'error_block_default': 'global_error_503',
}

response = requests.get(
    'https://mybees.com.ar/api/blocks/search_deferred_search_list',
    params=params,
    cookies=cookies,
    headers=headers,
)
res = response.json()
products = res['blocks'][4]['meta']['data']['products']
sku_list = []
for product in products:
    sku_list.append(product['sku'])
print(products[0]['price'])