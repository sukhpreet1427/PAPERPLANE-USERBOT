import asyncio
import time
from telethon.errors import FloodWaitError
from time import gmtime, strftime
from userbot import CMD_HELP, bot
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register

DEL_TIME_OUT = 70

@register(outgoing=True, pattern="^.autoname$")
async def _(event):
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d.%m.%y")
        HM = time.strftime("%H:%M")
        name = f"⌚{HM} | ayush | 📅{DM}"
        logger.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(  
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

        
