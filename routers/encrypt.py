'''Off-chain encryptor'''
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from supp.schemas import Encrypt
from supp.rijndael import compress
from supp.crud import add_row
from supp.db import get_db

router = APIRouter(
    prefix = '/cryptography',
    tags = ['Cryptography']
)


@router.post('/encrypt', status_code=status.HTTP_200_OK)
async def encrypt_score(item: Encrypt, db: Session = Depends(get_db)):
    '''
    Encrypt a score message (off-chain)

    Input:
    - **wallet_address [str]**: address
    - **score_response [dict]**: output of another endpoint
    - **blockchain [str]**: which blockchain
    - **is_encrypt [bool]**: True | False
    - **permit_name Optional[str]**: custom name for encryption

    Returns:
    - **[object]**: db row
    '''
    row = compress(item)
    add_row(db, row)

    return row
