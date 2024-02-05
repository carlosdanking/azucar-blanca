from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from logging import getLogger, Formatter, FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info, warning as log_warning
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tzlocal import get_localzone
from motor import motor_tornado

bot_token = "6633654277:AAFRnC06JQSJB57yKWx3O6rB1shy__KxqRY"
api_id = 19961504
api_hash = "28de3a8f4b68b388bfe47bf84d1b124b"

client = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token,plugins=dict(root="plugins"))

bot_database = motor_tornado.MotorClient("mongodb+srv://fishernemo57:tHv7Bo0MFuWfZTxh@cluster0.xshrglv.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=999999)

client_loop = client.loop

str_localzone = str(get_localzone())
scheduler = AsyncIOScheduler(timezone=str_localzone,event_loop=client_loop,misfire_grace_time=1000)