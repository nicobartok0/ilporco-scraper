import requests

cookies = {
    'OptanonAlertBoxClosed': '2024-03-20T00:26:43.263Z',
    'enable_tracking': 'true',
    'country': 'AR',
    'language': 'es',
    'ajs_anonymous_id': 'fe966072-ea74-4060-a1c1-6434e19afe37',
    'connect.sid': '',
    'REDUXPOC': '36422400004689',
    'DELIVERYDATE': 'j%3Anull',
    'ajs_user_id': '36422400004689_2a765889-fecb-4852-b740-feb42e11282c',
    'APPLICATION': 'CUSTOMER',
    'STOREID': '126a4950-c0ef-4ff2-a587-ddd963349ced',
    'STOREKEY': 'ABI',
    'iad': '1',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Apr+09+2024+11%3A41%3A12+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false',
    '___utmvc': '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',
}

headers = {
    'authority': 'mybees.com.ar',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    # 'cookie': 'OptanonAlertBoxClosed=2024-03-20T00:26:43.263Z; enable_tracking=true; country=AR; language=es; ajs_anonymous_id=fe966072-ea74-4060-a1c1-6434e19afe37; connect.sid=s%3ArOORS7-9P0jKXlCk6TLIpIXYLMb6Wal3.kirg5UACBKPt09va9yNBS5oiST82T6kjQh%2FvHZUv2Io; REDUXPOC=36422400004689; DELIVERYDATE=j%3Anull; ajs_user_id=36422400004689_2a765889-fecb-4852-b740-feb42e11282c; APPLICATION=CUSTOMER; STOREID=126a4950-c0ef-4ff2-a587-ddd963349ced; STOREKEY=ABI; iad=1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Apr+09+2024+11%3A41%3A12+GMT-0300+(hora+est%C3%A1ndar+de+Argentina)&version=6.32.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false; ___utmvc=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',
    'referer': 'https://mybees.com.ar/catalogsearch/result/?q=247',
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
    'term': '247',
    'termRaw': '247',
    'pageSize': '20',
    'page': '0',
    'sortBy': 'DEFAULT',
    'filters': '',
    'noCache': '0',
    'error_block_default': 'global_error_503',
}

response = requests.get('https://mybees.com.ar/api/blocks', params=params, cookies=cookies, headers=headers)
res = response.json()
info = res['blocks'][5]['meta']['data']['products']
for element in info:
    precio = element['price']
    print(f'{precio}\n')