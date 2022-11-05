'''Off-chain encryptor'''
from fastapi import APIRouter, status
from supp.schemas import Encrypt
from supp.rijndael import compress
from supp.crud import add_row

router = APIRouter(
    prefix = '/cryptography',
    tags = ['Cryptography']
)


@router.post('/encrypt', status_code=status.HTTP_200_OK)
async def encrypt_score(item: Encrypt):
    '''
    Encrypt a score message (off-chain)

    Input:
    - **wallet_address [str]**: address
    - **score_response [dict]**: output of another endpoint
    - **blockchain [str]**: which blockchain
    - **is_encrypt [bool]**: 1 | 0
    - **permit_name Optional[str]**: custom name for encryption

    Returns:
    - **[object]**: db row
    '''
    row = compress(item)
    add_row(db, row)

    return row
