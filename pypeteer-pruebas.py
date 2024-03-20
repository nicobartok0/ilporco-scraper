import requests
from bs4 import BeautifulSoup

import requests

cookies = {
    'OptanonAlertBoxClosed': '2024-03-20T00:26:43.263Z',
    'as_csus_viewed_36422400004689_2bd022dd_3c36_4e72_8b7f_b2cda343ed45': 'true',
    'enable_tracking': 'true',
    'country': 'AR',
    'language': 'es',
    'ajs_anonymous_id': '2971b5e1-2ffd-47f2-9ba0-a105ce57a705',
    'connect.sid': 's%3APU6RGFC-S_MT4fwq6twYt-pb8TJsLmH-.1v9euzWROLf1kh11L4ljoKtTa8WEo3W0UwbHlhmpVi8',
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

headers = {
    'authority': 'mybees.com.ar',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    # 'cookie': 'OptanonAlertBoxClosed=2024-03-20T00:26:43.263Z; as_csus_viewed_36422400004689_2bd022dd_3c36_4e72_8b7f_b2cda343ed45=true; enable_tracking=true; country=AR; language=es; ajs_anonymous_id=2971b5e1-2ffd-47f2-9ba0-a105ce57a705; connect.sid=s%3APU6RGFC-S_MT4fwq6twYt-pb8TJsLmH-.1v9euzWROLf1kh11L4ljoKtTa8WEo3W0UwbHlhmpVi8; REDUXPOC=36422400004689; DELIVERYDATE=j%3Anull; ajs_user_id=36422400004689_2a765889-fecb-4852-b740-feb42e11282c; APPLICATION=CUSTOMER; STOREID=126a4950-c0ef-4ff2-a587-ddd963349ced; STOREKEY=ABI; iad=1; ___utmvc=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; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Mar+20+2024+11%3A02%3A29+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false',
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

params = {
    'blockName': 'search_deferred_search_list',
    'locale': 'es_AR',
    'term': '2218',
    'termRaw': '2218',
    'pageSize': '20',
    'page': '0',
    'sortBy': 'DEFAULT',
    'filters': '',
    'noCache': '1710943350223',
    'error_block_default': 'global_error_503',
}

response = requests.get('https://mybees.com.ar/api/blocks', params=params, cookies=cookies, headers=headers)
res = response.json()
print('\n\nRESULT:')
print(res['blocks'][5]['meta']['data']['products'][0]['price'])
for element in res['blocks'][5]['meta']['data']['products']:
    print('//////////////')
    print(element)
    print('//////////////')