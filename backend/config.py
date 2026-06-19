import os
from dotenv import load_dotenv
#load variables from .env into the environment
load_dotenv()
#read variables
TELEGRAM_TOKEN: str | None = os.getenv("TELEGRAM_TOKEN")
HF_TOKEN: str | None = os.getenv("HF_TOKEN")

#validate variables
if not TELEGRAM_TOKEN:
    raise ValueError("Telegram token is not set")
