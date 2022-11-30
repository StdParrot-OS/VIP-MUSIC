from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ**.
‣ **ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ**.
‣ **ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ**
‣ **ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ**!
‣ **ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄꜱ**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕𝐀𝐃𝐃 𝐌𝐄 𝐁𝐀𝐁𝐘➕", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🥰𝐎𝐖𝐍𝐄𝐑🥰", "https://t.me/the_vip_boy")],
        [Button.url("🌷𝐉𝐎𝐈𝐍🌷", f"https://t.me/lovers_dunia"), Button.url("🥀𝐎𝐅𝐅𝐈𝐂𝐄🥀", f"https://t.me/vip_creators")],
        [Button.inline("🌺𝐇𝐄𝐋𝐏 & 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒🌺", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("🥺𝐍𝐎𝐖 𝐀𝐃𝐃 𝐏𝐋𝐒𝐒🥺", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👿𝐎𝐖𝐍𝐄𝐑👿", "https://t.me/the_vip_boy")],
        [Button.url("✨𝐉𝐎𝐈𝐍✨", f"https://t.me/{Config.SUPPORT}"), Button.url("🔥𝐎𝐅𝐅𝐈𝐂𝐄🔥", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("🌟𝐇𝐄𝐋𝐏 & 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒🌟", data="help")]])
       return
