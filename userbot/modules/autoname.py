import time
from userbot import CMD_HELP, bot
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)
from userbot.events import register


@register(outgoing=True, pattern="^.autoname")
async def update_name(name):
        newname = name.text[6:]
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M")

        if " " not in newname:
         firstname = newname
         lastname = f"({DMY} | {HM})"
        else:
         namesplit = newname.split(" ", 1)
         firstname = namesplit[0]
         lastname = namesplit[1]
        await bot(UpdateProfileRequest(first_name=firstname, last_name=lastname))
