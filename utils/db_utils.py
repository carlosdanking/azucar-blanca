from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from utils.btc_utils import get_btc
from db.database_main import DataBase

async def get_level_msg(level,language,user_id):
  data = DataBase()
  if level == "help" or level == "referral" or level == "balance" or level == "deposit" or level == "withdraw":
    if language == "spain":
      text = "¡Hola! Bienvenido a nuestro Bot de Telegram. Aquí, ofrecemos la emocionante oportunidad de apostar a números pares o impares utilizando la criptomoneda BTC. ¡Esperamos que disfrutes de tu tiempo en nuestro grupo! 🎲🚀"
      button = KeyboardButton("🏦 Balance")
      button1 = KeyboardButton("👤 Referidos")
      button2 = KeyboardButton("💵 Depositar")
      button3 = KeyboardButton("💳 Retirar")
      button4 = KeyboardButton("📊 Ranked")
      button5 = KeyboardButton("⁉️ Ayuda")
      button6 = KeyboardButton("📜 FAQ")
      markup = ReplyKeyboardMarkup([[button,button1],[button2,button3],[button4],[button5,button6]],resize_keyboard=True,one_time_keyboard=True)
      await data.set_new_key("level_menu","main",user_id)
      return text, markup
    else:
      text = "Hello! Welcome to our Telegram Bot. Here, we offer the thrilling opportunity to bet on even or odd numbers using the BTC cryptocurrency. We hope you enjoy your time in our group! 🎲🚀"
      button = KeyboardButton("🏦 Balance")
      button1 = KeyboardButton("👤 Referrals")
      button2 = KeyboardButton("💵 Deposit")
      button3 = KeyboardButton("💳 Withdraw")
      button4 = KeyboardButton("📊 Ranked")
      button5 = KeyboardButton("⁉️ Help")
      button6 = KeyboardButton("📜 FAQ")
      markup = ReplyKeyboardMarkup([[button,button1],[button2,button3],[button4],[button5,button6]],resize_keyboard=True,one_time_keyboard=True)
      await data.set_new_key("level_menu","main",user_id)
      return text, markup
  elif level == "help_support" or level == "help_terms":
    if language == "spain":
      text = "❗️ Si tiene alguna duda o algún problema con su depósito deje aquí su problema y revisaremos y le notificaremos sin problema."
      button = KeyboardButton("💬 Soporte")
      button2 = KeyboardButton("📑 Reglas de uso")
      button3 = KeyboardButton("⬅️ Atras")
      markup = ReplyKeyboardMarkup([[button],[button2],[button3]],resize_keyboard=True,one_time_keyboard=True)
      await data.set_new_key("level_menu","help",user_id)
      await data.set_new_key("in_support",False,user_id)
      return text, markup
    else:
      text = "❗️ If you have any questions or problems with your deposit, leave your problem here and we will review and notify you without any problem."
      button = KeyboardButton("💬 Support")
      button2 = KeyboardButton("📑 Terms of use")
      button3 = KeyboardButton("⬅️ Back")
      markup = ReplyKeyboardMarkup([[button],[button2],[button3]],resize_keyboard=True,one_time_keyboard=True)
      await data.set_new_key("level_menu","help",user_id)
      await data.set_new_key("in_support",False,user_id)
      return text, markup
  elif level == "faq_use":
    if language == "spain":
      text = "⁉️ Preguntas y Dudas frecuentes"
      button = KeyboardButton("📑 Uso")
      button2 = KeyboardButton("👥 Grupo")
      button3 = KeyboardButton("⬅️ Atras")
      markup = ReplyKeyboardMarkup([[button],[button2],[button3]],resize_keyboard=True,one_time_keyboard=True)
      await data.set_new_key("level_menu","help",user_id)
      return text, markup
    else:
      text = "⁉️ Frequently Asked Questions and Doubts"
      button = KeyboardButton("📑 Use")
      button2 = KeyboardButton("👥 Group")
      button3 = KeyboardButton("⬅️ Back")
      markup = ReplyKeyboardMarkup([[button],[button2],[button3]],resize_keyboard=True,one_time_keyboard=True)
      await data.set_new_key("level_menu","help",user_id)
      return text, markup
  else:
    pass

async def get_winners_and_losers(result,betting,data):
  msg_winners = ""
  msg_losers = ""
  count_win = 0
  count_los = 0
  pot = 0
  prize = 0
  for user_id in betting:
    user = await data.get_user(user_id)
    ranked = await get_emoji_range(user,data)
    first_name = user["firstname"]
    bet_even = user["bet_even"]
    bet_odd = user["bet_odd"]
    win_bets = user["win_bets"]
    losing_bets = user["losing_bets"]
    bet_satoshis = user["bet_satoshis"]
    satoshi = user["satoshis"]
    referred_by = user["referred_by"]
    domain = "tg://resolve?domain="
    if user["result_even"]:
      if result == "Even":
        quantity = bet_even * 0.85
        pot+=quantity
        prize+=bet_even
        win_btc = bet_even + quantity
        await data.set_new_key("satoshis",satoshi+win_btc,user_id)
        satoshis = await get_btc(win_btc)
        if count_win == 15:
          pass
        else:
          msg_winners+=f"{ranked} ฿<b><a href='{domain}'>{satoshis}</a></b> {first_name}\n"
        await data.set_new_key("win_satoshis",win_btc,user_id)
        await data.set_new_key("bet_satoshis",bet_satoshis+win_btc,user_id)
        await data.set_new_key("win_bets",win_bets+1,user_id)
        count_win+=1
      else:
        if referred_by != None:
          profit = bet_even * 0.05
          ref_user = await data.get_user(referred_by)
          claim_referral = ref_user["claim_referral"]
          ref_balance = ref_user["satoshis"]
          await data.set_new_key("satoshis",ref_balance+profit,referred_by)
          await data.set_new_key("claim_referral",claim_referral+profit,referred_by)
        satoshis = await get_btc(bet_even)
        prize+=bet_even
        if count_los == 15:
          pass
        else:
          msg_losers+=f"{ranked} ฿<b><a href='{domain}'>{satoshis}</a></b> {first_name}\n"
        await data.set_new_key("lost_satoshis",bet_even,user_id)
        await data.set_new_key("losing_bets",losing_bets+1,user_id)
        count_los+=1
    if user["result_odd"]:
      if result == "Odd":
        quantity = bet_odd * 0.85
        pot+=quantity
        prize+=bet_odd
        win_btc = bet_odd + quantity
        await data.set_new_key("satoshis",satoshi+win_btc,user_id)
        satoshis = await get_btc(win_btc)
        if count_win == 15:
          pass
        else:
          msg_winners+=f"{ranked} ฿<b><a href='{domain}'>{satoshis}</a></b> {first_name}\n"
        await data.set_new_key("win_satoshis",win_btc,user_id)
        await data.set_new_key("bet_satoshis",bet_satoshis+win_btc,user_id)
        await data.set_new_key("win_bets",win_bets+1,user_id)
        count_win+=1
      else:
        if referred_by != None:
          profit = bet_odd * 0.05
          ref_user = await data.get_user(referred_by)
          claim_referral = ref_user["claim_referral"]
          ref_balance = ref_user["satoshis"]
          await data.set_new_key("satoshis",ref_balance+profit,referred_by)
          await data.set_new_key("claim_referral",claim_referral+profit,referred_by)
        satoshis = await get_btc(bet_odd)
        prize+=bet_odd
        if count_los == 15:
          pass
        else:
          msg_losers+=f"{ranked} ฿<b><a href='{domain}'>{satoshis}</a></b> {first_name}\n"
        await data.set_new_key("lost_satoshis",bet_odd,user_id)
        await data.set_new_key("losing_bets",losing_bets+1,user_id)
        count_los+=1
  pot = await get_btc(pot)
  prize = await get_btc(prize)
  return msg_winners, msg_losers, count_win, count_los, pot, prize

async def get_emoji_range(user,data):
  total_deposit = user["total_deposit"]
  total_withdraw = user["total_withdraw"]
  first_name = user["firstname"]
  global_ranked = await data.get_user_rank()
  ranked = "▫️"
  if total_deposit != 0:
    ranked = "💎"
  if total_withdraw != 0:
    ranked = "🔸"
  if total_deposit != 0 and total_withdraw != 0:
    ranked = "🔹"
  if len(global_ranked) == 1:
    if first_name == global_ranked[0]:
      ranked = "🥇"
  if len(global_ranked) == 2:
    if first_name == global_ranked[0]:
      ranked = "🥇"
    if first_name == global_ranked[1]:
      ranked = "🥈"
  if len(global_ranked) > 2:
    if first_name == global_ranked[0]:
      ranked = "🥇"
    if first_name == global_ranked[1]:
      ranked = "🥈"
    if first_name == global_ranked[2]:
      ranked = "🥉"
  return ranked