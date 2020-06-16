# Import Dependencies
from fastapi import FastAPI

# Import local scripts
from busPy import utils as utils

# init FastApi server

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Hello World! FastApi is now up and running"}