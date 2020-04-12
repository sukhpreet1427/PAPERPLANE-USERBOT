from asyncio import sleep
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
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]
    while True:
        await bot(UpdateProfileRequest(first_name=firstname, last_name=lastname))
        await sleep(70)
