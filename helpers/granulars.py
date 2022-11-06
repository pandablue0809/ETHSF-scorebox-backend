'''Granular functions for Covalent credit scoring generator'''
import numpy as np
from datetime import datetime
NOW = datetime.now().date()


scores = [300, 500, 560, 650, 740, 800, 870, 900]
scalars = {
    'medians': [round(s/scores[-1], 2) for s in scores],
    'duration': [90, 120, 150, 180, 210, 270],
    'volume': [0.25, 0.9, 4, 8, 13, 15],
    'volume_per_txn': [1.4, 3.5, 5.3, 6.3, 7, 8],
    'frequency': [0.3, 0.5, 0.8, 1.3, 2, 4]
}


def kyc(txn, balances, portfolio):
    '''Award points for being a trusted user with legitimate txn history'''
    try:
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
            score = 1
        else:
            score = 0
    except Exception as e:
        score = 0
        print(str(e))

    finally:
        return score


def oldest(txn, fb):
    '''Reward user for wallet longevity'''
    try:
        oldest = datetime.strptime(
            txn['items'][-1]['block_signed_at'].split('T')[0], '%Y-%m-%d').date()
        how_long = (NOW - oldest).days

        score = scalars['medians'][np.digitize(how_long, scalars['duration'], right=True)]
        fb['oldest'] = how_long
        
    except Exception as e:
        score = 0
        fb['error'] = str(e)

    finally:
        return score



def capital(balances, fb):
    '''User cumulative capital now'''
    if balances['quote_currency'] == 'USD':
        total = sum([b['quote'] for b in balances['items']])
        if total == 0:
            score = 0
        else:
            score = scalars['medians'][np.digitize(
                total, scalars['volume'], right=True)]
        fb['capital'] = round(total, 2)
    else:
        score = 0
    return score



def volume(txn, fb):
    '''Reward users with voluminous transactions (little dust)'''
    volume = 0
    for t in txn['items']:
        volume += t['value_quote']
    volume_avg = volume/len(txn['items'])

    score = scalars['medians'][np.digitize(
        volume_avg, scalars['volume_per_txn'], right=True)]
    fb['volume'] = round(volume_avg, 2)
    return score


def dust(txn, fb):
    '''How many txn are legitimate and how many are dust?'''
    try:
        legit = len([t for t in txn['items']
            if t['successful'] and t['value_quote'] > 0])      
        
        legit_ratio = legit / len(txn['items'])
        score = scalars['medians'][np.digitize(
                legit_ratio, scalars['medians'], right=True)]
        fb['dust'] = round(legit_ratio, 2)
        return score
        
    except Exception as e:
        score = 0
        fb['error'] = str(e)

    finally:
        return score


def frequency(txn, fb):
    '''How regular are txn for this user?'''
    oldest = datetime.strptime(
        txn['items'][-1]['block_signed_at'].split('T')[0], '%Y-%M-%d').date()
    duration = int((NOW - oldest).days/30)  # months

    frequency = round(len(txn['items']) / duration, 2)
    score = scalars['medians'][np.digitize(frequency, scalars['frequency'], right=True)]
    fb['frequency'] = f'{frequency} txn/month over {duration} months'
    return score