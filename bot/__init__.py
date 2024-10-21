import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "22553734"))
    API_HASH = os.environ.get("API_HASH", "ce51aef681f6bb66fa3657a6eda5269a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7810740826:AAHoSj9HREduONfaRKcV9lykeiBKfDYI6mU")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Teron69bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
