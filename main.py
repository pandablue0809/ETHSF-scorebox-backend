'''fastapi App with its endpoints'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import nft, covalent, encrypt


app = FastAPI()


def cors(app: FastAPI):
    '''Enable CORS'''
    try:
        # the wildcard "*" says that all are allowed
        app.add_middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=False,
                allow_methods=["*"],
                allow_headers=["*"],
        )

    except Exception as e:
        print(f'\033[31m Error occurred while enabling CORS {e}\033[0m')


cors(app)

# base router
@app.get('/')
def home():
    '''Launch app'''
    return 'Server up'

app.include_router(nft.router)
app.include_router(covalent.router)
app.include_router(encrypt.router)
