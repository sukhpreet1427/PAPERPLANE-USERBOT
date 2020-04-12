import time
from userbot import CMD_HELP, bot
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)
from userbot.events import register

@register(outgoing=True, pattern="^.autoname")
async def update_name(name):
    """ For .autoname command, change your first name in Telegram and shows a running timer beside your name """
        firstname = "rootayush:~#"
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M")
        DEL_TIME_OUT = 60
        lastname = f"{DMY} | {HM}"
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]

    await bot(UpdateProfileRequest(first_name=firstname, last_name=lastname))
    await bot.sleep(DEL_TIME_OUT)
