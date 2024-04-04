from random import randint
from typing import Optional
from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from config import SUDO_USERS
from pyrogram.types import Message
SUDO_USER = SUDO_USERS
def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"**ɴᴏ ɢʀᴏᴜᴘ ᴄᴀʟʟ ꜰᴏᴜɴᴅ** {err_msg}")
    return False


@Client.on_message(
    filters.command(["startvc"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    tex = await message.reply_text(message, "ᴘʀᴏᴄᴇꜱꜱɪɴɢ.....")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"**ꜱᴛᴀʀᴛᴇᴅ ɢʀᴏᴜᴘ ᴄᴀʟʟ\n • **ᴄʜᴀᴛ ɪᴅ** : `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • **ᴛɪᴛʟᴇ:** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await tex.edit(args)
    except Exception as e:
        await tex.edit(f"**ɪɴꜰᴏ:** `{e}`")


@Client.on_message(
    filters.command(["stopvc"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def end_vc_(client: Client, message: Message):
    chat_id = message.chat.id
    if not (
        group_call := (
            await get_group_call(client, message, err_msg=", ɢʀᴏᴜᴘ ᴄᴀʟʟ ᴀʟʀᴇᴀᴅʏ ᴇɴᴅᴇᴅ")
        )
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await message.reply_text(f"ᴇɴᴅᴇᴅ ɢʀᴏᴜᴘ ᴄᴀʟʟ ɪɴ **ᴄʜᴀᴛ ɪᴅ** : `{chat_id}`")
