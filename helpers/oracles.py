'''Basic credit scoring algorithm'''
from random import randint
from helpers.granulars import *
from helpers.message import msg_formatter

WEIGHTS = [0.1, 0.125, 0.125, 0.1, 0.1, 0.1]
RANGES = [300, 500, 560, 650, 740, 800, 870, 900]
LOANS = [0, 500, 1000, 5000, 10000, 15000, 20000, 25000]
QUALITY = ["out of bounds", "very poor", "poor", "fair",\
     "good", "very good", "excellent", "exceptional"]


def calculate_score(txn, bal, port, coinmarketcap_key, chain_id):
    '''aggregate granular functions into one score'''
    fb = {}
    layer1 = [
        kyc(txn, bal, port),
        oldest(txn, fb),
        capital(bal, fb),
        volume(txn, fb),
        dust(txn, fb),
        frequency(txn, fb)
    ]

    print(fb)
    score = sum([w*b for w,b in zip(WEIGHTS, layer1)])*600+300
    message = msg_formatter(score, fb, RANGES, LOANS, QUALITY, coinmarketcap_key, chain_id)
    myscore = {
        'score': int(score),
        'message': message,
    }

    return myscore