import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

# Define the chance command handler
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["chance"], [hl]))
async def chance(client, message):
    # Extract the text following the /chance command
    text = message.text.split(hl + "chance ", maxsplit=1)[1]
    
    # Calculate a random chance percentage
    chance_percentage = random.randint(1, 100)
    
    # Send the chance percentage as a reply
    await message.reply(f"**{text}**\n\n**ᴄʜᴀɴᴄᴇ**: {chance_percentage}%")
