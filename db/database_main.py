from __init__ import bot_database

class DataBase(object):
  
  def __init__(self):
    self.database = bot_database
    self.bot = self.database.BTCUP
    self.col = self.bot.Users
  
  async def new_user(self,user_id,first_name,username):
    if not await self.col.find_one({"user_id":user_id}):
      await self.col.insert_one({"user_id":user_id,"firstname":first_name,"username":username,"encargo":False})
    return
  
  async def global_bot(self):
    await self.col.insert_one({"bot":"global","ranked":[],"min_bet":50,"default_bet":50,"max_bet":85000000,"round_start":None,"msg_bet_id":None,"game":0,"open_bet":False})
  
  async def get_bot(self):
    return await self.col.find_one({"bot":"global"})
  
  async def get_user(self,user_id):
    return await self.col.find_one({"user_id":user_id})
  
  async def set_new_key(self, key, val, user_id):
    await self.col.update_one({"user_id":user_id},{"$set":{key:val}})
  
  async def set_bot_key(self, key, val):
    await self.col.update_one({"bot":"global"},{"$set":{key:val}})
  
  async def get_ranked(self):
    ranked = {}
    async for result in self.col.find({}):
      if not result.get("user_id"):
        continue
      bet_satoshis = result["bet_satoshis"]
      first_name = result["firstname"]
      if bet_satoshis < 1000:
        continue
      ranked[first_name] = bet_satoshis
    best_ranked = sorted(ranked,key=ranked.get,reverse=True)
    list_ranked = best_ranked[:5]
    msg_rank = ""
    position = 0
    for user in list_ranked:
      bet_satoshis = ranked[user]
      number_ext = str(int(bet_satoshis))
      if len(number_ext) == 4:
        satoshis = number_ext[0]
      elif len(number_ext) == 5:
        satoshis = number_ext[:2]
      elif len(number_ext) == 6:
        satoshis = number_ext[:3]
      elif len(number_ext) == 7:
        satoshis = number_ext[:4]
      else:
        pass
      if position == 0:
        msg_rank+=f"🥇{user} +{satoshis}\n"
      elif position == 1:
        msg_rank+=f"🥈{user} +{satoshis}\n"
      elif position == 2:
        msg_rank+=f"🥉{user} +{satoshis}\n"
      elif position == 3:
        msg_rank+=f"🥉{user} +{satoshis}\n"
      elif position == 4:
        msg_rank+=f"🥉{user} +{satoshis}\n"
      position+=1
    return msg_rank
  
  async def get_total_ranked(self):
    ranked = {}
    async for result in self.col.find({}):
      if not result.get("user_id"):
        continue
      bet_satoshis = result["bet_satoshis"]
      first_name = result["firstname"]
      if bet_satoshis < 1000:
        continue
      ranked[result["user_id"]] = bet_satoshis
    best_ranked = sorted(ranked,key=ranked.get,reverse=True)
    list_ranked = best_ranked[:10]
    return list_ranked
  
  async def get_user_rank(self):
    ranked = {}
    async for result in self.col.find({}):
      if not result.get("user_id"):
        continue
      bet_satoshis = result["bet_satoshis"]
      first_name = result["firstname"]
      if bet_satoshis < 1000:
        continue
      ranked[first_name] = bet_satoshis
    best_ranked = sorted(ranked,key=ranked.get,reverse=True)
    list_ranked = best_ranked[:5]
    return list_ranked
  
  async def update_bot(self):
    async for result in self.col.find({}):
      if not result.get("user_id"):
        continue
      user_id = result["user_id"]
      await self.col.delete_one({"user_id":user_id})