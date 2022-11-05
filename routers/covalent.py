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
    return 'test this endpoint on Swagger'