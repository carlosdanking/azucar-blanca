from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from utils.telegram_utils import send_message
from db.database_main import DataBase
from datetime import datetime, timedelta
from __init__ import client_loop

@Client.on_message(filters.text & filters.private)
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
    if user["encargo"]:
      username = user["username"]
      text = f"👤 **Usuario**: **@{username}**\n🆔 **Usuario Id**: `{user_id}`\n📨 **Contacto**: <a href='tg://user?id={user_id}'><b>{first_name}</b></a>\n\n{message.text}"
      await send_message(client,5293594308,text,message,None)
      await send_message(client,758606497,text,message,None)
      await data.set_new_key("encargo",False,user_id)
      text = "**✅ ¡Perfecto!** Contactaremos con usted lo más pronto posible, gracias por confiar en nuestro equipo para hacer realidad sus proyectos."
      await send_message(client,user_id,text,message,None)
  client_loop.create_task(start_worker(client,message))