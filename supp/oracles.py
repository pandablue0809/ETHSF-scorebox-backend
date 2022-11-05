'''Basic credit scoring algorithm'''
from random import randint

def calculate_score(txn, bal, port):
    score = randint(300, 900)
    myscore = {
        'score': int(score),
        'message': f'Contratulations! Your got a ScoreBox credit score of {score} points',
    }
    return myscore