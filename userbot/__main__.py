# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot

from userbot import (
    BOT_TOKEN,
    BOT_USERNAME,
    BOT_VER,
    BOTLOG_CHATID,
    ALIVE_LOGO,
    LOGS,
    mieblacklist,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES
from userbot.utils import autobot
from userbot.utils.tools import bacot_kontol

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    mieblacklist = requests.get(
        "https://raw.githubusercontent.com/IndomieGorengSatu/Mie/master/mieblacklist.json"
    ).json()
    if user.id in mieblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTNYA GUA MATIIN NAJIS BANGET DIPAKE ORANG KEK LU.\nCredits: @IndomieGenetik"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
 
    LOGS.info(f"♨IndomieUserbot♨ ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

async def userbot_on():
    user = await bot.get_me()
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_file(
                BOTLOG_CHATID, ALIVE_LOGO, caption=f"**IndomieUserbot Berhasil Diaktifkan ♨**\n━━━━━━━━━━━━━━━━━━━\n✦ **Oᴡɴᴇʀ Bᴏᴛ :** [{user.first_name}](tg://user?id={user.id})\n✦ **Bᴏᴛ Vᴇʀ :** `8.2`\n━━━━━━━━━━━━━━━━━━━\n✦ **Sᴜᴘᴘᴏʀᴛ​ :** @IndomieProject\n✦ **Sᴛᴏʀᴇ​ :** @IndomieStore \n━━━━━━━━━━━━━━━━━━━"
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(userbot_on())
bot.loop.run_until_complete(bacot_kontol())
if not BOT_TOKEN:
    LOGS.info(
        "Vars BOT_TOKEN ga di isi, otw bikin bot di @Botfather ngeeengg..."
    )
    bot.loop.run_until_complete(autobot())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
