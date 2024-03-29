import os
from pyrogram import Client, filters

# Initialize Pyrogram Client
app = Client("sdestructimage_downloader")

# Define the filter for the commands
@Client.on_message(filters.command(["😋🥰", "op", "wow", "super", "😋😍"]) & filters.private & filters.reply)
async def download_self_destruct_image(client, message):
    try:
        replied_message = message.reply_to_message
        if not replied_message or not (replied_message.photo or replied_message.video):
            return
        # Download the media file
        file_path = await client.download_media(replied_message)
        # Send the downloaded media file as a document
        await client.send_document("me", file_path)
        # Remove the downloaded media file from the local storage
        os.remove(file_path)
    except Exception as e:
        print(f"Error: {e}")
        return
