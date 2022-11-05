'''OpenSea endpoint'''
from fastapi import APIRouter, status
from supp.schemas import OpenSeaNFT
from opensea import read_nfts


router = APIRouter(
    prefix = '/opensea',
    tags = ['OpenSea']
)


@router.post('/getnft', status_code=status.HTTP_200_OK)
async def get_nft_assets(item: OpenSeaNFT):
    '''
    Get NFT info

    Input:
    - **address [str]**: MetaMask wallet address

    Output:
    - **[object]**: NFT info
    '''
    req = read_nfts(item.address)
    assets = req['assets']

    res = dict(
        total=0,
        nft_count=0,
        nft_with_value=0
    )
    if not assets:
        print('ERR: No assets found')
        return res

    res['nft_count'] = len(assets)
    for asset in assets:
        if asset['last_sale']:
            res['total'] += float(asset['last_sale']['payment_token']['usd_price'])
            res['nft_with_value'] += 1
            
    return res
