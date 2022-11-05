'''fastapi App with its endpoints'''
from fastapi import FastAPI
from routers import nft


app = FastAPI()

# base router
@app.get('/')
def home():
    '''Launch app'''
    return 'Server up'

app.include_router(nft.router)

