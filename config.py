import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = int(os.getenv("APP_ID") or os.getenv("API_ID") or "0")
API_HASH = os.getenv("API_HASH", "")
PBXBOT_SESSION = os.getenv("PBXBOT_SESSION") or os.getenv("STRING_SESSION") or ""
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
HANDLER = os.getenv("HANDLER", ".")
OWNER_ID = int(os.getenv("OWNER_ID") or "0")
LOGGER_ID = int(os.getenv("LOGGER_ID") or "0")
DATABASE_URL = os.getenv("DATABASE_URL", "")
BOT_NAME = os.getenv("BOT_NAME", "PBX Userbot")
