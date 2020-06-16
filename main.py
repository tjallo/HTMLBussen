# Import Dependencies
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

# Import local scripts
from busPy import utils as Utils
from busPy import players as Players

# init FastApi server
app = FastAPI()

# Set CORS Settings
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Set some global variables

port = 8000
baseUrl = 'http://127.0.0.1'

url = f'{baseUrl}{port}/'

htmlUrl = "http://127.0.0.1:5500"


@app.get('/')
async def root():
    return {'message': "Hello World! FastApi is now up and running"}


# Card Class

# Player Class
@app.get('/players/addPlayer/')
async def addPlayer(username):
    result = Players.addPlayer(str(username))
    redirect = f'{htmlUrl}/html/gamestart.html'
    return RedirectResponse(redirect)

@app.get('/players/getAllPlayers/')
async def getAllPlayers():
    return Players.getAllPlayers()
