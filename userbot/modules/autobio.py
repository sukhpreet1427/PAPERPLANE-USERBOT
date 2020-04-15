import asyncio
import datetime
import time
from telethon.errors import FloodWaitError
from userbot import bot
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register
import pytz

DEL_TIME_OUT = 60

@register(outgoing=True, pattern="^.autobio")
async def _(event):
    if event.fwd_from:
        return
    while True:
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        PT = LT.strftime("%d.%m.%y")
        OT = LT.strftime("%H:%M")
        name = f"Dev | Learning Python,Java,C,Kotlin,Bash | No PM's | {PT} {OT}"
        try:
            await bot(UpdateProfileRequest(about=name))
        except FloodWaitError as ex:
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

        
