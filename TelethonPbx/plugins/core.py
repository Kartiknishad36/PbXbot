import time
from telethon import events
import config

START = time.time()

def register(client):
    h = config.HANDLER

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}ping$"))
    async def ping(event):
        t = time.time()
        msg = await event.edit("...")
        ms = (time.time() - t) * 1000
        await msg.edit(f"PONG `{ms:.0f}ms`")

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}alive$"))
    async def alive(event):
        up = int(time.time() - START)
        await event.edit(f"**{config.BOT_NAME} ALIVE**\nUptime `{up}s`\nOwner `{config.OWNER_ID}`")

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}help$"))
    async def help_cmd(event):
        text = (
            f"**PBX USERBOT**\nPrefix `{h}`\n\n"
            f"`.ping` `.alive` `.help` `.id` `.info`\n"
            f"Owner: `.eval` `.restart`"
        )
        await event.edit(text)

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}id$"))
    async def id_cmd(event):
        cid = event.chat_id
        uid = event.sender_id
        if event.is_reply:
            r = await event.get_reply_message()
            uid = r.sender_id
        await event.edit(f"Chat `{cid}`\nUser `{uid}`")

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}info$"))
    async def info_cmd(event):
        if event.is_reply:
            r = await event.get_reply_message()
            u = await event.client.get_entity(r.sender_id)
        else:
            u = await event.get_sender()
        name = getattr(u, "first_name", "") or ""
        un = f"@{u.username}" if getattr(u, "username", None) else "None"
        await event.edit(f"Name: {name}\nID: `{u.id}`\nUser: {un}")
