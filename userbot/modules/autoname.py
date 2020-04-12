import time
from userbot import CMD_HELP, bot
from asyncio import sleep
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)
from userbot.events import register
@register(outgoing=True, pattern="^.autoname")
async def update_name(name):
               DMY = time.strftime("%d.%m.%Y")
               HM = time.strftime("%H:%M")
               firstname = f"rootayush:~# ({DMY} | {HM})"

    while True:
        await bot(UpdateProfileRequest(first_name=firstname))
