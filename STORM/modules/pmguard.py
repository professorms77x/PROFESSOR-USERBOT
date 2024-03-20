from pyrogram import filters, Client
import asyncio
from pyrogram.types import Message 

from pyrogram.methods import messages
from STORM.database.pmpermitdb import get_approved_users, pm_guard
import STORM.database.pmpermitdb as KEX
LOG_GROUP = "-1002068576120" 
PM_LOGGER = "-1002068576120"
FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}


async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.command("setlimit", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**ꜱᴇᴛ ʟɪᴍɪᴛ ᴛᴏ <ᴄᴏᴜɴᴛ>**")
        return
    await KEX.set_limit(int(arg))
    await message.edit(f"**ʟɪᴍɪᴛ ꜱᴇᴛ ᴛᴏ {arg}**")



@Client.on_message(filters.command("setblockmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**ᴡʜᴀᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴇᴛ**")
        return
    if arg == "default":
        await KEX.set_block_message(KEX.BLOCKED)
        await message.edit("**ʙʟᴏᴄᴋ ᴍᴇꜱꜱᴀɢᴇ ꜱᴇᴛ ᴛᴏ ᴅᴇꜰᴀᴜʟᴛ**")
        return
    await KEX.set_block_message(f"`{arg}`")
    await message.edit("**ᴄᴜꜱᴛᴏᴍ ʙʟᴏᴄᴋ ᴍᴇꜱꜱᴀɢᴇ ꜱᴇᴛ**")


@Client.on_message(filters.command(["allow", "ap", "approve", "a"], ["."]) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await KEX.get_pm_settings()
    await KEX.allow_user(chat_id)
    await message.edit(f"**ɪ ʜᴀᴠᴇ ᴀʟʟᴏᴡᴇᴅ [ʏᴏᴜ](tg://user?id={chat_id}) ᴛᴏ ᴘᴍ ᴍʏ ᴍᴀꜱᴛᴇʀ**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(filters.command(["deny", "dap", "disapprove", "dapp"], ["."]) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await KEX.deny_user(chat_id)
    await message.edit(f"**ɪ ʜᴀᴠᴇ ᴅᴇɴɪᴇᴅ [ʏᴏᴜ](tg://user?id={chat_id}) ᴛᴏ ᴘᴍ ᴍʏ ᴍᴀꜱᴛᴇʀ**")


@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await KEX.get_pm_settings()
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]
    if PM_LOGGER:
        await app.send_message(PM_LOGGER, f"{message.text}")
    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in app.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        await message.reply(pm_message, disable_web_page_preview=True)
        return
    await message.reply(block_message, disable_web_page_preview=True)
    await app.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})
