'''PUSH notification endpoint'''
from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from requ.polling import *
from supp.schemas import PushPoll


router = APIRouter(
    prefix = '/push',
    tags = ['Notifications']
)

@router.post('/polling', status_code=status.HTTP_200_OK)
async def push_notification(request: Request, item: PushPoll):
    '''
    Send PUSH notifications to a user

    Input:
    - **address [str]**: MetaMask wallet address

    Output:
    - **[bool]**: True upon success
    '''
    try:
        print('\033[35;1m Receiving request from: {request.client.host}\033[0m')
        run_leaderboard(item.address)
        return True

    except Exception as e:
        print('\033[35;1m Unable to send leaderboard PUSH notifications \033[0m')
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'endpoint': '/push/polling',
                'status': 'error',
                'message': str(e)
            }
        )
