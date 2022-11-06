'''Endpoints Payloads'''

from pydantic import BaseModel
from typing import Union

class OpenSeaNFT(BaseModel):
    address: str

class Covalent(BaseModel):
    chain_id: int
    eth_address: str
    covalent_key: str
    #add live conversion from Coinmarketcap

class Encrypt(BaseModel):
    wallet_address: str
    score_response: dict
    blockchain: str
    is_encrypt: bool
    permit_name: Union[str, None] = None

class PushPoll(BaseModel):
    address: str