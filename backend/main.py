from fastapi import FastAPI
from config import Config
from extensions import db
from routes.userRoute import userRoute

app = FastAPI()
app.include_router(userRoute, prefix='/user')

users = db['users']

@app.get('/')
def index():
    print(f"Server running at port {Config.PORT}")
    return {'message': 'Connected to server successfully'}