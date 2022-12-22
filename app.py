import os
from fastapi import FastAPI
import asyncio
from bot import bot
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

async def my_function():
    await bot.start(os.getenv("TOKEN"))

@app.on_event("startup")
async def startup():
    loop = asyncio.get_event_loop()
    loop.create_task(my_function())

@app.get("/")
def home():
    return "Hello World!"