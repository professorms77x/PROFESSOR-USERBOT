import asyncio
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from lyricsdb import search_lyrics
from config import SUDO_USERS

@Client.on_message(filters.command(["l", "lyrics"], ".") & filters.me | filters.user(SUDO_USERS))
async def handle_lyrics_command(client: Client, message: Message):
    try:
        # Extract command arguments
        cmd = message.command
        song_title = cmd[1] if len(cmd) > 1 else ""
        artist_name = cmd[2] if len(cmd) > 2 else ""

        if not song_title:
            await message.edit("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ꜱᴏɴɢ ᴛɪᴛʟᴇ...")
            await asyncio.sleep(2)
            await message.delete()
            return

        if not artist_name:
            await message.edit("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴀʀᴛɪꜱᴛ ɴᴀᴍᴇ..")
            await asyncio.sleep(2)
            await message.delete()
            return

        # Retrieve and send lyrics
        await message.edit(f"ꜰᴇᴛᴄʜɪɴɢ ʟʏʀɪᴄꜱ ꜰᴏʀ '{song_title}' ʙʏ {artist_name}...")
        lyrics = await search_lyrics(song_title, artist_name)
        await message.edit(lyrics)

    except Exception as e:
        await message.edit("ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ʟʏʀɪᴄꜱ....")
        await asyncio.sleep(2)
        await message.delete()
