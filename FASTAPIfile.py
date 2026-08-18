from fastapi import FastAPI
from FileAdminPanel import send_admin
from datetime import datetime
import aiohttp
from SqlFile import init_db
from SqlFile import add_user





#FASTAPIfile.py

app = FastAPI()


@app.get("/name/{username}")
async def echo(username:str, age: int = 0):
 

 await add_user(username,age)
 
 now = datetime.now()
 

 
 await send_admin(username,str(age),str(now))
 return {
 "Your name":username,
 "Your age":age
 }