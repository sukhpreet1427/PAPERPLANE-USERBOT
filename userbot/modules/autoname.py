import asyncio
import datetime
import time
from telethon.errors import FloodWaitError
from userbot import bot
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register
import pytz

DEL_TIME_OUT = 1

@register(outgoing=True, pattern="^.autoname")
async def _(event):
    if event.fwd_from:
        return
    while True:
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        PT = LT.strftime("%d.%m.%y")
        OT = LT.strftime("%H:%M:%S")
        name = f"root@ayush:~# {PT} {OT}"
        try:
            await bot(UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

        
