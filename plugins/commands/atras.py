from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from utils.telegram_utils import send_message
from db.database_main import DataBase
from datetime import datetime, timedelta
from __init__ import client_loop

@Client.on_message(filters.regex("Atras") & filters.private)
async def start_bot(client, message):
  async def start_worker(client,message):
    from_user = message.from_user
    user_id = from_user.id
    first_name = from_user.first_name
    username = from_user.username
    
    data = DataBase()
    await data.new_user(user_id,first_name,username)
    user = await data.get_user(user_id)
    user_name = user["username"]
    if username != user_name:
      await data.set_new_key("username",username,user_id)
      user = await data.get_user(user_id)
    text = "👋🏼 **¡Hola! Puede usar los siguientes botones para interactuar con nuestro bot.**"
    button = KeyboardButton("🙋🏼‍♂ Realizar un encargo")
    button1 = KeyboardButton("⁉️ Preguntas Frecuentes")
    markup = ReplyKeyboardMarkup([[button],[button1]],resize_keyboard=True,one_time_keyboard=True)
    await data.set_new_key("encargo",False,user_id)
    await send_message(client,user_id,text,message,markup)
  client_loop.create_task(start_worker(client,message))