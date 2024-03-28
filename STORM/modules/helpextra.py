from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

EXTRA_TEXT = f"""
**ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ** 

• `{hl}ping` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ....

• `{hl}restart` » ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ....
    
• `{hl}alive` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ...

• `{hl}repo` » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ...

• `{hl}id` » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ'ꜱ ᴜꜱᴇʀ_ɪᴅ....

• `{hl}addsudo` » ᴛᴏ ᴀᴅᴅ ꜱᴜᴅᴏ....

• `{hl}sudolist` » ᴛᴏ ɢᴇᴛ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ʟɪꜱᴛ....

• `{hl}gitinfo` <username> » ᴛᴏ ɢᴇᴛ ɢɪᴛ ᴀᴄᴄ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpextra"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=EXTRA_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=EXTRA_TEXT)
