from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("🥲𝐁𝐀𝐂𝐊😂", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("😌𝐁𝐀𝐂𝐊😅", data="help")]])


ADMIN_TEXT = """
**✘ A module from which admins of the chat can use!**

‣ `😝end` - To End music streaming.
‣ `😁skip` - To Skip Tracks Going on.
‣ `😉pause` - To Pause streaming.
‣ `🤭resume` - to Resume Streaming.
‣ `🙂leavevc` - force The Userbot to leave Vc Chat (Sometimes Joined).
‣ `😘playlist` - to check playlists.
"""

PLAY_TEXT = """
**✘ A module from which users of the chat can use!**

‣ `🥰play` - To Play Audio from Else Reply to audio file.
‣ `😍vplay` - To Stream Videos.
"""
