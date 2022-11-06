import numpy as np
from helpers.coinmarketcap import exchange_rate

response = "Congrats, you have successfully obtained a credit score! Your ScoreBox score is {} - {} points. This score qualifies you for a short term loan of up to {:,} {} which is equivalent to {:,} USD."

TOKEN_DICT = {
    1: 'ETH',
    137: 'MATIC'
}

def msg_formatter(score, fb, ranges, loans, quality, coinmarketcap_key, chain_id):

    points = int(score)
    qual = quality[np.digitize(score, ranges, right=False)]
    loan = int(loans[np.digitize(score, ranges, right=False)])

    # init response
    exchange = exchange_rate(coinmarketcap_key, 'USD', TOKEN_DICT[chain_id])
    x = response.format(qual.upper(), points, int(round(loan*exchange, 0)), TOKEN_DICT[chain_id], loan)

    # duration & volume
    if 'duration' in list(fb.keys()):
        dur = fb['duration']
        if 'volume' in list(fb.keys()):
            vol = fb['volume']
            x = x + f' Your wallet address has been active for {dur} days '\
                        f'and your total balance across all cryptocurrencies is ${vol:,.0f} USD.'
        else:
            x = x + f' Your wallet address has been active for {dur} days.'
    else:
        if 'volume' in list(fb.keys()):
            vol = fb['volume']
            x = x + f' Your total balance across all cryptocurrencies is ${vol} USD.'
    
    return x

