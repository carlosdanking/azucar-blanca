from time import sleep
sleep(1200)

from utils.telegram_utils import bot_online_msg, send_message, edit_msg, edit_channel_msg, delete_message, edit_markup, get_chat_data
from __init__ import client, scheduler,InlineKeyboardButton, InlineKeyboardMarkup
from db.database_main import DataBase
from datetime import datetime, timezone
from datetime import timedelta
from asyncio import sleep

if __name__ == "__main__":
  client.start()
  client.loop.create_task(bot_online_msg(client,"✅ Bot online"))
  client.loop.run_forever()