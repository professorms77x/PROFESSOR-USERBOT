from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

NEWS_TEXT = f"""
**ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}news` » ᴛᴏ ɢᴇᴛ ᴛᴏᴘ 5 ʜᴇᴀᴅʟɪɴᴇꜱ ᴏꜰ ɴᴇᴡꜱ....

• `{hl}weather (ʏᴏᴜʀ ᴄɪᴛʏ)` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....

• `{hl}ai (ʏᴏᴜʀ Qᴜᴇʀʏ)` » ᴄʜᴇᴄᴋ ʏᴏᴜʀꜱᴇʟꜰ......

• `{hl}google (ʏᴏᴜʀ Qᴜᴇʀʏ)` » ᴄʜᴇᴄᴋ ʏᴏᴜʀꜱᴇʟꜰ......
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpnews"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=NEWS_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=NEWS_TEXT) 
