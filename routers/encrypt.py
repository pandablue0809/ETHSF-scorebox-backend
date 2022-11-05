'''Off-chain encryptor'''
from fastapi import APIRouter, status
from supp.schemas import Encrypt


router = APIRouter(
    prefix = '/cryptography',
    tags = ['Cryptography']
)


@router.post('/encrypt', status_code=status.HTTP_200_OK)
async def encrypt_score(item: Encrypt):
    return item.wallet_address