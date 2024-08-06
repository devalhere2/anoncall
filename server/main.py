from fastapi import FastAPI,HTTPException,status,WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketDisconnect
from typing import Optional
from pydantic import BaseModel
from faker import Faker 
import random
import redis 
import json


class server_credentials(BaseModel):
    username: Optional[str] = None
    serverId: Optional[str] = None
    password: Optional[str] = None


app = FastAPI()
fake = Faker()
r = redis.Redis(host='localhost', port=6379, decode_responses=True,password='anondb')
r.flushall()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return "Welcome to the anonCall Backend"

@app.post('/create')
def create_server(details: server_credentials):
    username = details.username
    serverId = details.serverId
    password = details.password

    if username == None:
        username = fake.user_name()
    if serverId == None:
        serverId = random.randint(100000,999999)
    data = {
        "creator": username,
        "members": [username],
        "password": password,
        "serverId": serverId
    }
    r.json().set(f'server:{serverId}','$',data)
    return {"username": username,"serverId":serverId}


@app.post('/join')
def join_server(details: server_credentials):
    username = details.username
    serverId = details.serverId
    password = details.password
    if username == None:
        username = fake.user_name()

    real_password = r.json().get(f'server:{serverId}', '$.password')[0]
    
    if real_password == password:
        print('password match',real_password,password)       
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect")
 

@app.websocket("/details")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app',port=8000,host='localhost',reload=True)