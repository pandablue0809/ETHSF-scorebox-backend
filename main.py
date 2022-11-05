'''fastapi App with its endpoints'''
from fastapi import FastAPI


app = FastAPI()

# base router
@app.get('/')
def home():
    '''Launch app'''
    return 'Server up'

