from pyrogram import Client, filters
from STORM import grt
from STORM.Database.afk import *
import time
hl = "."

afk_watcher = 6

@Client.on_message(filters.command('afk', hl) & filters.me)
async def afk(client, message):
  reason = message.text.split(None, 1)[1] if len(message.command) > 1 else ''
  tim = time.time()
  txt = "ꜱᴇᴇ ʏᴀᴀ !, ᴀᴍ ᴀꜰᴋ"+ "\n\n" + f"ʀᴇᴀꜱᴏɴ: `{reason}`" if reason else "see yaa !, am afk"
  await message.edit(txt)
  await add_afk({"afk_time": tim, "afk_reason": reason})
  
@Client.on_message(group=afk_watcher)
async def afk(client, message):
  if not await is_afk():
    return
  det = await get_afk_details()
  if message.from_user.is_self:
    if message.text:
      if message.text.lower().startswith(f'{hl}afk'):
        return
    txt = "ɪ'ᴍ ʙᴀᴄᴋ ᴏɴʟɪɴᴇ, ᴀꜰᴋ ꜰᴏʀ" + f' `{grt(int(time.time() - det[0]))}`.'
    if det[1]:
      txt += "\n\n"
      txt += "ʀᴇᴀꜱᴏɴ :" + f" `{det[1]}`"
    await client.send_message(message.chat.id, txt)
    return await remove_afk()
  user_id = message.from_user.id if message.from_user else 0
  if message.chat.id > 0:
    txt = "ɪ'ᴍ ᴀꜰᴋ, ꜱɪɴᴄᴇ" + f' `{grt(int(time.time() - det[0]))}`.'
    if det[1]:
      txt += "\n\n"
      txt += "ʀᴇᴀꜱᴏɴ :" + f" `{det[1]}`"
    return await message.reply(txt)
  reply = message.reply_to_message
  if reply:
    if reply.from_user.id != client.me.id:
      return
    txt = "ɪ'ᴍ ᴀꜰᴋ, ꜱɪɴᴄᴇ" + f' `{grt(int(time.time() - det[0]))}`.'
    if det[1]:
      txt += "\n\n"
      txt += "ʀᴇᴀꜱᴏɴ:" + f" `{det[1]}`"
    return await message.reply(txt)
  entities = message.entities
  if entities:
    for entity in entities:
      if entity.type.name == "MENTION":
        text = message.text if message.text else message.caption
        text = text.split()
        for tex in text:
          if tex[0] != "@":
            continue
          try:
            id = (await client.get_users(tex)).id
          except:
            continue
          if id != client.me.id:
            continue
          txt = "ɪ'ᴍ ᴀꜰᴋ, ꜱɪɴᴄᴇ" + f' `{grt(int(time.time() - det[0]))}`.'
          if det[1]:
            txt += "\n\n"
            txt += "ʀᴇᴀꜱᴏɴ :" + f" `{det[1]}`"
          return await message.reply(txt)
      if entity.type.name == "TEXT_MENTION":
        if entity.user.id != client.me.id:
          return
        txt = "ɪ'ᴍ ᴀꜰᴋ, ꜱɪɴᴄᴇ" + f' `{grt(int(time.time() - det[0]))}`.'
        if det[1]:
          txt += "\n\n"
          txt += "ʀᴇᴀꜱᴏɴ:" + f" `{det[1]}`"
        return await message.reply(txt)
