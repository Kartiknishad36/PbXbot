import os
import sys
import traceback
from telethon import events
import config

def _owner(event):
    if not config.OWNER_ID:
        return event.out
    return event.sender_id == config.OWNER_ID or event.out

def register(client):
    h = config.HANDLER

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}eval(?: |\n)([\s\S]+)"))
    async def eval_cmd(event):
        if config.OWNER_ID and event.sender_id != config.OWNER_ID and not event.out:
            return
        code = event.pattern_match.group(1)
        try:
            result = eval(code, {"client": client, "event": event})
            if hasattr(result, "__await__"):
                result = await result
            await event.edit(f"```\n{result}\n```")
        except Exception:
            await event.edit(f"```\n{traceback.format_exc()}\n```")

    @client.on(events.NewMessage(outgoing=True, pattern=rf"\\{h}restart$"))
    async def restart_cmd(event):
        if config.OWNER_ID and event.sender_id != config.OWNER_ID and not event.out:
            return
        await event.edit("Restarting...")
        os.execl(sys.executable, sys.executable, "-m", "TelethonPbx")
