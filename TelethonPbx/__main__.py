import asyncio
import importlib
import logging
import sys
from pathlib import Path

from telethon import TelegramClient
from telethon.sessions import StringSession

import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
LOG = logging.getLogger("PBX")


async def main():
    if not config.APP_ID or not config.API_HASH:
        LOG.error("APP_ID / API_HASH missing in env")
        sys.exit(1)
    if not config.PBXBOT_SESSION:
        LOG.error("PBXBOT_SESSION missing — run: python3 Pbx_string.py")
        sys.exit(1)

    client = TelegramClient(
        StringSession(config.PBXBOT_SESSION),
        config.APP_ID,
        config.API_HASH,
    )
    await client.connect()
    if not await client.is_user_authorized():
        LOG.error("Invalid or expired PBXBOT_SESSION")
        sys.exit(1)

    plugins_dir = Path(__file__).parent / "plugins"
    for file in sorted(plugins_dir.glob("*.py")):
        if file.name.startswith("_"):
            continue
        mod = importlib.import_module(f"TelethonPbx.plugins.{file.stem}")
        if hasattr(mod, "register"):
            mod.register(client)
            LOG.info("Loaded plugin: %s", file.stem)

    me = await client.get_me()
    LOG.info("PBX online as %s (%s)", me.first_name, me.id)

    if config.LOGGER_ID:
        try:
            await client.send_message(
                config.LOGGER_ID,
                f"✅ **PBX Online**\n👤 {me.first_name}\n🆔 `{me.id}`",
            )
        except Exception as e:
            LOG.warning("LOGGER_ID notify failed: %s", e)

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
