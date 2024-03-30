import os
from pyrogram import Client, filters

@Client.on_message(cdz(["😋🥰", "op", "wow", "super", "😋😍"])
    & filters.private & filters.me)
async def self_media(client, message):
    try:
        replied = message.reply_to_message
        if not replied:
            return
        if not (replied.photo or replied.video):
            return
        location = await client.download_media(replied)
        await client.send_document("me", location)
        os.remove(location)
    except Exception as e:
        print("Error: `{e}`")
        return
