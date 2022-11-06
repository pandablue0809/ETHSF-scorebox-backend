'''Granular functions for Covalent credit scoring generator'''
import numpy as np
from datetime import datetime
NOW = datetime.now().date()


# global variables
TOP_ERC = ["ETH", "WETH", "USDT", "MATIC", "MKR", "BAT", "CRO", "USDC",\
     "TUSD", "REP", "OMG", "LINK", "PAX", "HOT", "ZRX", "IOST", "HT", \
        "AOA", "ENJ", "MCO", "NEXO", "NET", "GUSD", "ENG", "LAMB"]


def top_erc_only(data, top_erc):
    '''Keep only ERC20 data top ranked in Coinmarketcap'''
    skimmed = list()
    for b in data['items']:
        if b['contract_ticker_symbol'] in top_erc:
            skimmed.append(b)

    data['items'] = skimmed
    return data



def covalent_kyc(txn, balances, portfolio):
    '''Award points for being a trusted user with legitimate txn history
    '''
    oldest = datetime.strptime(
        txn['items'][-1]['block_signed_at'].split('T')[0], '%Y-%m-%d').date()
    how_long = (NOW - oldest).days

    # Assign max score as long as the user owns a
    # tot balance > $150, a credible transaction history,
    # a portfolio, and a wallet opened > 3 months ago
    if txn['items']\
        and portfolio['items']\
            and sum([b['quote'] for b in balances['items']]) > 150\
        and how_long >= 90:
        return True
    else:
        return False