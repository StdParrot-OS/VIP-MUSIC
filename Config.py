import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24232903"))
    API_HASH = os.environ.get("API_HASH", "977a10e8cb23b5aa883faf622b972312")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TG_MANAGER_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "LOVERS_DUNIA") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "VIP_CREATORS") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/f6c19e28af165d3d3e62e.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/f6c19e28af165d3d3e62e.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5609473839")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
