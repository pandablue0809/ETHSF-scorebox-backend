import requests

def exchange_rate(api_key, coin_in, coin_out):
    '''returns conversion rate for the coin pair coin_in-coin_out'''
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    params = {
        'amount': 1,
        'symbol': coin_in,
        'convert': coin_out
    }
    
    url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

    # Run GET & fetch best cryptos from coinmarketcap API
    r = requests.get(url, headers=headers, params=params).json()
    rate = r['data'][0]['quote'][coin_out]['price']

    return rate
