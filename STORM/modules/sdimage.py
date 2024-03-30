import os
from pyrogram import Client, filters

trigger_words = ["😋🥰", "op", "wow", "super", "😋😍"]

@filters.private & filters.me
async def private_message_filter(_, __, message):
    return message

@Client.on_message(filters.text & private_message_filter)
async def self_media_handler(client, message):
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
        print(f"Error: {e}")
