from fastapi import FastAPI, APIRouter
from extensions import db
from models.user import User, LoginUser
from extensions import pwt_context

app = FastAPI()
users = db['users']

userRoute = APIRouter()

@userRoute.post('/signup')
async def signup(user: User):
    if users.find_one({"email" : user.email}):
        return {"message" : "Email already registered"}
    hashed_password = pwt_context.hash(user.password)
    user.password = hashed_password
    users.insert_one(user.model_dump())
    return {"message" : "Successfully registered"}

@userRoute.post('/login')
async def login(user: LoginUser):
    result = users.find_one({"email" : user.email})
    if not result:
        return {
            "success" : False,
            "message" : "Email not registered"
        }
    if not pwt_context.verify(user.password, result["password"]):
        return {
            "success" : False,
            "message" : "Incorrect password"
        }
    return {
        "success" : True,
        "message" : "Logged in successfully"
    }
