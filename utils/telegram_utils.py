from pyrogram import errors
import asyncio

async def send_message(client,user_id,text,message_id,reply_markup):
  if message_id == None:
    pass
  elif isinstance(message_id,int):
    pass
  elif message_id.reply_to_message:
    message_id = message_id.reply_to_message.id
  else:
    message_id = message_id.id
  try:
    return await client.send_message(user_id,text,reply_to_message_id=message_id,reply_markup=reply_markup,disable_web_page_preview=True)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await send_message(client,user_id,text,message_id,reply_markup)
  except Exception as exc:
    print(exc)
    return None

async def edit_msg(msg,message,reply_markup):
  try:
    await msg.edit(message,reply_markup=reply_markup,disable_web_page_preview=True)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await edit_msg(msg,message,reply_markup)
  except errors.MessageNotModified as exc:
    return await edit_msg(msg,message,reply_markup)
  except Exception as exc:
    print(exc)
    return None

async def edit_channel_msg(client,chat_id,text,message_id,reply_markup):
  try:
    return await client.edit_message_text(chat_id,message_id,text,reply_markup=reply_markup)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await edit_channel_msg(client,chat_id,text,message_id,reply_markup)
  except errors.MessageNotModified as exc:
    return await edit_channel_msg(client,chat_id,text,message_id,reply_markup)
  except Exception as exc:
    print(exc)
    return None

async def edit_markup(client,user_id,message,markup):
  if isinstance(message,int):
    message_id = message
  elif message.reply_to_message:
    message_id = message.reply_to_message.id
  else:
    message_id = message.id
  try:
    return await client.edit_message_reply_markup(user_id,message_id,markup)
  except Exception as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await edit_markup(client,user_id,message,markup)
  except Exception as exc:
    print(exc)
    return None

async def bot_online_msg(client,text,markup=None):
  try:
    await client.send_message(5293594308,text,reply_markup=markup)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await bot_online_msg(client)
  except Exception as exc:
    print(exc)
    return None

async def join_user_group(client,chat_id,user_id):
  try:
    return await client.get_chat_member(chat_id,user_id)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await join_user_group(client,chat_id,user_id)
  except Exception as exc:
    print(exc)
    return None

async def get_chat_data(client,chat_id):
  try:
    total = await client.get_chat_members_count(chat_id)
    active_members = 0
    online_members = 0
    return total, active_members, online_members
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await get_chat_data(client, chat_id)
  except Exception as exc:
    print(exc)
    return None, None, None

async def get_msg(text):
  try:
    userid = int(text.split("ID: ")[1].split("\n")[0])
    try:
      username = text.split("deposito: ")[1].split("\n")[0]
    except:
      username = text.split("retiro: ")[1].split("\n")[0]
    return userid, username
  except:
    return None, None

async def answer_callback_query(client,query_id,text):
  try:
    return await client.answer_callback_query(query_id,text,show_alert=True)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await answer_callback_query(client,query_id,text)
  except Exception as exc:
    print(exc)
    return None

async def delete_message(client,chat_id,message_id):
  try:
    await client.delete_messages(chat_id,message_ids=message_id)
  except errors.FloodWait as exc:
    await asyncio.sleep(exc.value * 1.2)
    return await delete_message(client,chat_id,message_id)
  except Exception as exc:
    print(exc)
    return None