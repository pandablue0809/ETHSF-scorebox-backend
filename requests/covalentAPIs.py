'''Fetch Covalent rich API data'''
import requests

def covalent_bal_port(chain_id, eth_address, endpoints, api_key):
    '''get balances or portfolio data'''
    endpoint = f'/{chain_id}/address/{eth_address}/{endpoints}/?key={api_key}'
    url = 'https://api.covalenthq.com/v1' + endpoint
    result = requests.get(url).json()
    r = result['data']
    return r


def covalent_txn(chain_id, eth_address, api_key):
    '''get transaction data'''
    endpoint = f'/{chain_id}/address/{eth_address}/transactions_v2/'\
            f'?no-logs=False&page-size=500&page-number=0&key={api_key}'
    url = 'https://api.covalenthq.com/v1' + endpoint
    result = requests.get(url).json()
    txn = result['data']
    return txn