'''Covalent endpoints'''
from fastapi import APIRouter, status
from supp.schemas import Covalent


router = APIRouter(
    prefix = '/credit_score',
    tags = ['Credit Score']
)


@router.post('/covalent', status_code=status.HTTP_200_OK)
async def credit_score_covalent(item: Covalent):
    '''Calculates credit score'''
    txn = covalent_get_txn(
            str(item.chain_id),
            item.eth_address,
            item.covalent_key,
            False,
            500, 
            0
            )
    return 'test this endpoint on Swagger'