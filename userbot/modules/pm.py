# Special module to block pms automatically
<<<<<<< HEAD:userbot/modules/pm.py
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import ReportSpamRequest
=======
>>>>>>> 1ce4916... [REFACTOR] : Linting the stuff (1):userbot/modules/pmpermit.py
import sqlite3

from telethon import TelegramClient, events
from telethon.tl.functions.contacts import BlockRequest

from userbot import COUNT_PM, LOGGER, LOGGER_GROUP, NOTIF_OFF, PM_AUTO_BAN, bot


@bot.on(events.NewMessage(incoming=True))
@bot.on(events.MessageEdited(incoming=True))
async def permitpm(e):
    if PM_AUTO_BAN:
        global COUNT_PM
        if e.is_private and not (await e.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
            except:
                return
<<<<<<< HEAD:userbot/modules/pm.py
            E = is_approved(e.chat_id)
            if not E and e.text != "`Bleep Blop! This is a Bot. Don't fret. \n\nMy Master 'ѕнanυ ғlaѕн #noυ' hasn't approved you to PM. \
=======
            apprv = is_approved(e.chat_id)
            if not apprv and e.text != "`Bleep Blop! This is a Bot. Don't fret. \n\nMy Master hasn't approved you to PM. \
>>>>>>> 1ce4916... [REFACTOR] : Linting the stuff (1):userbot/modules/pmpermit.py
Please wait for my Master to look in, he would mostly approve PMs.\n\n\
As far as i know, he doesn't usually approve Retards.`" :
                await e.reply(
                    "`Bleep Blop! This is a Bot. Don't fret. \n\nMy Master hasn't approved you to PM. \
Please wait for my Master to look in, he would mostly approve PMs.\n\n\
As far as i know, he doesn't usually approve Retards.`"
                )
                if NOTIF_OFF:
                    await bot.send_read_acknowledge(e.chat_id)
                if e.chat_id not in COUNT_PM:
                    COUNT_PM.update({e.chat_id: 1})
                else:
                    COUNT_PM[e.chat_id] = COUNT_PM[e.chat_id] + 1
                if COUNT_PM[e.chat_id] > 4:
                    await e.respond(
                        "`You were spamming my Master's PM, which I don't like. I'mma Report Spam.`"
                    )
                    del COUNT_PM[e.chat_id]
                    await bot(BlockRequest(e.chat_id))
                    await bot(ReportSpamRequest(peer='e.chat_id'))
                    if LOGGER:
                        name = await bot.get_entity(e.chat_id)
                        name0 = str(name.first_name)
                        await bot.send_message(
                            LOGGER_GROUP,
                            "["
                            + name0
                            + "](tg://user?id="
                            + str(e.chat_id)
                            + ")"
                            + " was just another retarded nibba",
                        )


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifoff$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifoff$"))
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF=True
    await e.edit("`Notifications silenced!`")


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifon$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifon$"))
async def notifon(e):
    global NOTIF_OFF
    NOTIF_OFF=False
    await e.edit("`Notifications unmuted!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.approve$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.approve$"))
async def approvepm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except:
            await e.edit("`Running on Non-SQL mode!`")
            return
        approve(e.chat_id)
        await e.edit("`ѕнanυ ғlaѕн #noυ has approved you to PM!`")
        if LOGGER:
            aname = await bot.get_entity(e.chat_id)
            name0 = str(aname.first_name)
            await bot.send_message(
                LOGGER_GROUP,
                "["
                + name0
                + "](tg://user?id="
                + str(e.chat_id)
                + ")"
                + " was approved to PM you.",
            )


@bot.on(events.NewMessage(outgoing=True, pattern="^.disapprove$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.disapprove$"))
async def disapprovepm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import dissprove
        except:
            await e.edit("`Running on Non-SQL mode!`")
            return
        dissprove(e.chat_id)
        await e.edit("`ѕнanυ ғlaѕн #noυ has disapproved you to PM!`")
        if LOGGER:
            aname = await bot.get_entity(e.chat_id)
            name0 = str(aname.first_name)
            await bot.send_message(
                LOGGER_GROUP,
                "["
                + name0
                + "](tg://user?id="
                + str(e.chat_id)
                + ")"
                + " was Disapproved to PM you.",
            )
