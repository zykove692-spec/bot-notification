from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Bot,Router,Dispatcher
import asyncio
from SqlFile import init_db
from SqlFile import search_info
from SqlFile import get_all
import os
from dotenv import load_dotenv

#FileAdminPanel.py

load_dotenv()

TOKEN = os.getenv("TOKENBOT")


dp = Dispatcher()
router = Router()
dp.include_router(router)
bot=Bot(token=TOKEN)


async def send_admin(name: str,age: str,data:str):
 await bot.send_message(8542369929,f"🔔New notifications\n•Name:{name}\nAge:{age}\nData:[{data}]")
 
 
 
 
 
@router.message(Command("start"))
async def echo(message:Message):
 
 id = message.from_user.id
 if int(id)!= 8542369929:
 	await message.answer("Access denied")
 	return
 
 await message.answer("Hello admin!\nWhen someone will visit your site i'll send to you message\nCommands:\n/AllShow - View the list of users\n/Search_name {name} - find info with help name")
 
 
 
@router.message(Command("AllShow"))
async def get_user(message:Message):
 
 id = message.from_user.id
 
 if int(id)!= 8542369929:
 	await message.answer("Access denied")
 	return
 
 info = await get_all()
 await message.answer(info)
 
 
 
@router.message(Command("Search_name"))
async def xesh(message:Message):
 
 id = message.from_user.id
 if int(id) != 8542369929:
 	await message.answer("Access denied")
 	return
 
 text = message.text
 
 if not text:
 	await message.answer("Write something")
 	return
 	
 words = text.split()
 
 if len(words) != 2:
 	await message.answer("An error...")
 	return
 
 information = await search_info(str(words[1]))
 
 
@router.message()
async def non(message:Message):
 
 id = message.from_user.id
 if int(id) != 8542369929:
 	await message.answer("Access denied")
 	return
 
 await message.answer("Hello,write /start")



async def main():
 await init_db()
 await dp.start_polling(bot)
 
if __name__ == "__main__":
 asyncio.run(main())