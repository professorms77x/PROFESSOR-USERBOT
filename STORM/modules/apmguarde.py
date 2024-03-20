from pyrogram import filters, Client
import asyncio
from config import SUDO_USERS
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users
import STORM.database.pmpermitdb as KEX



@Client.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**ɪ ᴏɴʟʏ ᴜɴᴅᴇʀꜱᴛᴀɴᴅ ᴏɴ ᴏʀ ᴏꜰꜰ**")
        return
    if arg == "off":
        await KEX.set_pm(False)
        await message.edit("**ᴘᴍ ɢᴜᴀʀᴅ ᴅɪꜱᴀʙʟᴇᴅ**")
    if arg == "on":
        await KEX.set_pm(True)
        await message.edit("**ᴘᴍ ɢᴜᴀʀᴅ ᴀᴄᴛɪᴠᴀᴛᴇᴅ**")
@Client.on_message(filters.command("setpmmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**ᴡʜᴀᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴇᴛ**")
        return
    if arg == "default":
        await KEX.set_permit_message(KEX.PMPERMIT_MESSAGE)
        await message.edit("**ᴀɴᴛɪ_ᴘᴍ ᴍᴇꜱꜱᴀɢᴇ ꜱᴇᴛ ᴛᴏ ᴅᴇꜰᴀᴜʟᴛ**")
        return
    await KEX.set_permit_message(f"`{arg}`")
    await message.edit("**ᴄᴜꜱᴛᴏᴍ ᴀɴᴛɪ-ᴘᴍ ᴍᴇꜱꜱᴀɢᴇ ꜱᴇᴛ**")
