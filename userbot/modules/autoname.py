import asyncio
import time
from telethon.errors import FloodWaitError
from time import gmtime, strftime
from userbot import CMD_HELP, bot
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register

@register(outgoing=True, pattern="^.autoname$")
async def _(event):
        firstname = "root@ayush:~#"
        TIME = strftime("%Y-%m-%d %H:%M", gmtime())
        lastname = f"{TIME}"
        TIME_OUT = 70
    while True:
        try:
          await bot(UpdateProfileRequest(first_name=firstname, last_name=lastname))
        except FloodWaitError as ex:
               await asyncio.sleep(ex.seconds)
               await asyncio.sleep(TIME_OUT)
