from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from utils.telegram_utils import send_message
from db.database_main import DataBase
from datetime import datetime, timedelta
from __init__ import client_loop

@Client.on_message(filters.regex("Preguntas Frecuentes") & filters.private)
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
    text = '**1-** **__¿Como puedo realizar un pedido mediante este bot?__**:\nPara realizar un pedido de programación a nuestro equipo solo necesita usar el botón "🙋🏼‍♂ Realizar un encargo", a continuación se le mostrará un mensaje que le pedirá enviar un mensaje al bot con una pequeña descripción del encargo que desea que nos hagamos cargo, una vez se nos entregue su mensaje lo analizaremos y contactaremos con usted lo más pronto que nos sea posible.\n\n**2-** **__¿Cuanto puedo demorar en recibir respuesta de algún administrador?__**:\nActualmente no contamos con un amplio equipo de administradores, dado tal caso puede que demore varias horas en recibir su respuesta si por ejemplo realiza su solictiud muy tarde en la madrugada, por eso le recomendamos usar horarios logicos para que pueda recibir su respuesta lo más pronto posible.\n\n**3-** **__¿Cual es el precio de un servicio, en que se basan para determinar el precio de un servicio?__**:\nEl valor de los servicios prestados por nuestro equipo depende mucho de la magnitud de su solicitud, si su encargo es simple nuestros precios serán de acuerdo a la simplicidad del proyecto, si por el contrario su encargo tiene complejidad y el tiempo que puede demorar en desarrollarse puede llegar a ser bastante largo entonces los precios serán de acuerdo a tal complejidad, aunque este tema se negocia directamente entre uno de nuestros programadores y el cliente, asi que pueden haber acuerdos a conveniencia entre ambas partes.'
    button = KeyboardButton("⬅️ Atras")
    markup = ReplyKeyboardMarkup([[button]],resize_keyboard=True,one_time_keyboard=True)
    await send_message(client,user_id,text,message,markup)
  client_loop.create_task(start_worker(client,message))