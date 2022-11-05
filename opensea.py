'''Hit an OpenSea endpoint to fetch NFT holdings for an address'''

import json
import requests


def read_nfts(address: str) -> dict:
    '''Pass in a Metamask wallet address and returns NFT data'''

    url = f"https://api.opensea.io/api/v1/assets?owner={address}&order_direction=desc&limit=20&include_orders=false"

    headers = {
        "accept": "application/json",
        "X-API-KEY": ""
    }

    response = requests.get(url, headers=headers, timeout=60).json()
    return response
