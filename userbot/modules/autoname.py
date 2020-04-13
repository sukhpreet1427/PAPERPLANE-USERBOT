from asyncio import sleep
from telethon.errors import FloodWaitError
from time import gmtime, strftime
from userbot import CMD_HELP, bot
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register

@register(outgoing=True, pattern="^.autoname")
async def update_name(name):
    newname = name.text[10:]
    if " " not in newname:
        firstname = newname
        TIME = strftime("%Y-%m-%d %H:%M", gmtime())
        lastname = f"{TIME}"
        TIME_OUT = 70
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]
    while True:
        try:
          await bot(UpdateProfileRequest(first_name=firstname, last_name=lastname))
        except FloodWaitError as ex:
               await asyncio.sleep(ex.seconds)
               await asyncio.sleep(TIME_OUT)
