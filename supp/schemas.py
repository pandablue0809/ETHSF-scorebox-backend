'''Endpoints Payloads'''

from pydantic import BaseModel
from typing import Union

class OpenSeaNFT(BaseModel):
    address: str

class Covalent(BaseModel):
    # chain_id: int
    eth_address: str
    covalent_key: str