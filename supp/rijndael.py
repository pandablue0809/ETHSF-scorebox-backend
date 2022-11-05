'''Rijndael Symmetric Encryption'''
from time import time
from cryptography.fernet import Fernet
from supp.schemas import Encrypt


def encryptor(data: str):
    key = Fernet.generate_key()
    f = Fernet(key)
    r = f.encrypt(bytes(data, 'utf-8')).decode()
    return r, key


def decryptor(data: str, key: str):
    f = Fernet(key)
    r = f.decrypt(bytes(data, 'utf-8')).decode()
    if not r:
        raise ValueError('Error decryption failed')
    return r


def compress(req: Encrypt):
    if req.is_encrypt:
        msg, key = encryptor(req.score_response['message'])
        permit = req.permit_name
    else:
        msg = req.score_response['message']
        key = None
        permit = None
    
    row = {
        'wallet': req.wallet_address,
        'oracle': req.score_response['endpoint'].split('/')[-1],
        'blockchain': req.blockchain,
        'is_encrypted': req.is_encrypt,
        'permit': permit,
        'score_int': req.score_response['score'],
        'score_blurb': msg,
        'decryption_key': key,
        'timestamp': int(time())
        }

    return row