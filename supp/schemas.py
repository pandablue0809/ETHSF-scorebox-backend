'''Endpoints Payloads'''

from pydantic import BaseModel
from typing import Union

class OpenSeaNFT(BaseModel):
    address: str
