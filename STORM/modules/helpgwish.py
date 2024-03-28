from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

GWISH_TEXT = f"""
**ɢᴡɪꜱʜ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}gm` » ᴛᴏ ꜱᴘᴀᴍ ɢᴜᴅ ᴍᴏʀɴɪɴɢ ᴍꜱɢ....

• `{hl}ga` » ᴛᴏ ꜱᴘᴀᴍ ɢᴜᴅ ɴᴏᴏɴ ᴍꜱɢ....

• `{hl}gn` » ᴛᴏ ꜱᴘᴀᴍ ɢᴜᴅ ɴɪɢʜᴛ ᴍꜱɢ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpgwish"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=GWISH_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=GWISH_TEXT) 
