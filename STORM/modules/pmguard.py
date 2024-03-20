from pyrogram import Client, filters
import asyncio

LOG_GROUP = "-1002068576120"
PM_LOGGER = "-1002068576120"
ALLOWED_USERS = [6257927828]
PM_BLOCKED_MESSAGE = (
"**ᴡᴀʀɴɪɴɢ ⚠️ ᴘʟᴢ ʀᴇᴀᴅ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴠᴇʀʏ ᴄᴀʀᴇꜰᴜʟʟʏ....**"
"**ɪ'ᴍ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ! ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴏꜰ ᴍʏ ꜱᴇɴꜱᴇɪ ! ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴍʏ ꜱᴇɴꜱᴇɪ ꜰʀᴏᴍ ꜱᴘᴀᴍᴍᴇʀꜱ.**"
"**ɪꜰ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ꜱᴘᴀᴍᴍᴇʀ ᴛʜᴇɴ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ!...**"
)


async def pmpermit_guard(filter, client, message):
    # Check if the user is allowed to PM the bot
    if message.chat.id in ALLOWED_USERS:
        return False
    else:
        # If not allowed, send a message and block the user
        await message.reply_text(PM_BLOCKED_MESSAGE)
        await client.block_user(message.chat.id)
        return True

# Command to allow a user to PM the bot
@Client.on_message(filters.command(["allow"], prefixes=".") & filters.me)
async def allow_pm(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        ALLOWED_USERS.append(user_id)
        await message.reply_text(f"User {user_id} has been allowed to PM the bot.")
    else:
        await message.reply_text("Please reply to the user's message to allow them to PM the bot.")


# Command to disallow a user from PMing the bot
@Client.on_message(filters.command(["disallow"], prefixes=".") & filters.me)
async def disallow_pm(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if user_id in ALLOWED_USERS:
            ALLOWED_USERS.remove(user_id)
            await message.reply_text(f"ᴜꜱᴇʀ {user_id} ʜᴀꜱ ʙᴇᴇɴ ᴅɪꜱᴀʟʟᴏᴡᴇᴅ ꜰʀᴏᴍ ᴘᴍɪɴɢ ᴛʜᴇ ʙᴏᴛ")
        else:
            await message.reply_text(f"ᴜꜱᴇʀ {user_id} ɪꜱ ɴᴏᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘᴍ ᴛʜᴇ ʙᴏᴛ")
    else:
        await message.reply_text("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴜꜱᴇʀ'ꜱ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴅɪꜱᴀʟʟᴏᴡ ᴛʜᴇᴍ ꜰʀᴏᴍ ᴘᴍɪɴɢ ᴛʜᴇ ʙᴏᴛ")


# Command to view the list of allowed users
@Client.on_message(filters.command(["allowed"], prefixes=".") & filters.me)
async def view_allowed_users(client, message):
    await message.reply_text(f"ᴀʟʟᴏᴡᴇᴅ ᴜꜱᴇʀꜱ: {', '.join(str(user_id) for user_id in ALLOWED_USERS)}")


# Register the PM permit guard filter
Client.on_message(filters.private & filters.create(pmpermit_guard) & ~filters.me)(lambda _, __, ___: None)
