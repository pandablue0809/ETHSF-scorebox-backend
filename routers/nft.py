'''OpenSea endpoint'''
from fastapi import APIRouter, status
from supp.schemas import OpenSeaNFT
# from opensea import read_nfts


router = APIRouter(
    prefix = '/opensea',
    tags = ['OpenSea']
)


@router.post('/getnft', status_code=status.HTTP_200_OK)
async def get_nft_assets(item: OpenSeaNFT):
    return 'Forgot NFT router. Try now. Should work'
