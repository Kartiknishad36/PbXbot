import asyncio
import importlib
import logging
import sys
from pathlib import Path

from telethon import TelegramClient

import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
LOG = logging.getLogger("PBX")


async def main():
    if not config.APP_ID or not config.API_HASH:
        LOG.error("APP_ID / API_HASH missing")
        sys.exit(1)
    if not config.PBXBOT_SESSION:
        LOG.error("PBXBOT_SESSION missing")
        sys.exit(1)

    client = TelegramClient("pbx_session", config.APP_ID, config.API_HASH)
    await client.start(bot_token=None)
    # string session
    from telethon.sessions import StringSession
    client = TelegramClient(StringSession(config.PBXBOT_SESSION), config.APP_ID, config.API_HASH)
    await client.connect()
    if not await client.is_user_authorized():
        LOG.error("Invalid session")
        sys.exit(1)

    plugins_dir = Path(__file__).parent / "plugins"
    for file in sorted(plugins_dir.glob("*.py")):
        if file.name.startswith("_"):
            continue
        mod = importlib.import_module(f"TelethonPbx.plugins.{file.stem}")
        if hasattr(mod, "register"):
            mod.register(client)
            LOG.info("Loaded: %s", file.stem)

    me = await client.get_me()
    LOG.info("Online as %s (%s)", me.first_name, me.id)
    if config.LOGGER_ID:
        try:
            await client.send_message(config.LOGGER_ID, f"PBX Online\n{me.first_name} `{me.id}`")
        except Exception:
            pass
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
