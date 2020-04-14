import asyncio
import datetime
import time
from telethon.errors import FloodWaitError
from userbot import CMD_HELP, bot
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register

DEL_TIME_OUT = 70

@register(outgoing=True, pattern="^.autoname")
async def _(event):
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d.%m.%y")
        HM = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        name = f"root@ayush:~# {DM} {HM}"
        try:
            await bot(UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

        
