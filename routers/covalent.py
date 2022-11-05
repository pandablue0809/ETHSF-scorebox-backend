'''Covalent endpoints'''
from fastapi import APIRouter, status
from supp.schemas import Covalent
from supp.oracles import calculate_score
from requ.covalentAPIs import covalent_bal_port, covalent_txn


router = APIRouter(
    prefix = '/credit_score',
    tags = ['Covalent HQ']
)

CHAIN = {
    1: 'ethereum',
    137: 'polygon'
}

@router.post('/covalent', status_code=status.HTTP_200_OK)
async def credit_score_covalent(item: Covalent):
    '''Calculates credit score'''

    # Fetch data first
    txn = covalent_txn(
            str(item.chain_id),
            item.eth_address,
            item.covalent_key
            )
    print(type(txn))

    bal = covalent_bal_port(
            str(item.chain_id),
            item.eth_address,
            'balances_v2',
            item.covalent_key
            )

    por = covalent_bal_port(
            str(item.chain_id),
            item.eth_address,
            'portfolio_v2',
            item.covalent_key
            )

    out = calculate_score(txn, bal, por)

    # Aggregate data and calculate score
    out['endpoint'] = f'/covalent/{CHAIN[item.chain_id]}'
    return out